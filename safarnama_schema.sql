-- ============================================
-- SafarNama Supabase Schema
-- Run this in: Supabase Dashboard → SQL Editor
-- ============================================

-- 1. PROFILES (extends auth.users)
create table if not exists profiles (
  id uuid references auth.users on delete cascade primary key,
  name text not null,
  phone text,
  avatar_color text default '#F7941D',
  created_at timestamptz default now()
);

-- 2. TRIPS
create table if not exists trips (
  id uuid default gen_random_uuid() primary key,
  name text not null,
  destination text not null,
  start_date date,
  end_date date,
  invite_code text unique default upper(substring(md5(random()::text), 1, 8)),
  created_by uuid references profiles(id) on delete cascade,
  created_at timestamptz default now()
);

-- 3. TRIP MEMBERS
create table if not exists trip_members (
  id uuid default gen_random_uuid() primary key,
  trip_id uuid references trips(id) on delete cascade,
  user_id uuid references profiles(id) on delete cascade,
  role text default 'member',       -- 'coordinator' | 'member'
  transport_mode text default 'flight',
  from_city text default 'Your City',
  progress int default 0,           -- 0–100 travel progress
  unique(trip_id, user_id)
);

-- 4. EXPENSES
create table if not exists expenses (
  id uuid default gen_random_uuid() primary key,
  trip_id uuid references trips(id) on delete cascade,
  title text not null,
  amount numeric not null default 0,
  paid_by uuid references profiles(id),
  created_at timestamptz default now()
);

-- ============================================
-- ROW LEVEL SECURITY
-- ============================================

alter table profiles enable row level security;
alter table trips enable row level security;
alter table trip_members enable row level security;
alter table expenses enable row level security;

-- PROFILES
create policy "Anyone can read profiles"
  on profiles for select using (true);

create policy "Users insert own profile"
  on profiles for insert with check (auth.uid() = id);

create policy "Users update own profile"
  on profiles for update using (auth.uid() = id);

-- TRIPS: anyone can read by invite_code (for joining), members see their trips
create policy "Anyone can read trips to join"
  on trips for select using (true);

create policy "Authenticated users create trips"
  on trips for insert with check (auth.uid() = created_by);

create policy "Creator can update trip"
  on trips for update using (auth.uid() = created_by);

-- TRIP MEMBERS
create policy "Members can view trip members"
  on trip_members for select using (true);

create policy "Users join trips"
  on trip_members for insert with check (auth.uid() = user_id);

create policy "Users update own membership"
  on trip_members for update using (auth.uid() = user_id);

-- EXPENSES
create policy "Trip members view expenses"
  on expenses for select using (true);

create policy "Trip members add expenses"
  on expenses for insert with check (
    exists (
      select 1 from trip_members
      where trip_id = expenses.trip_id and user_id = auth.uid()
    )
  );

create policy "Creator deletes expense"
  on expenses for delete using (auth.uid() = paid_by);

-- ============================================
-- AUTO-CREATE PROFILE ON SIGNUP
-- ============================================
create or replace function handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into profiles (id, name, phone, avatar_color)
  values (
    new.id,
    coalesce(new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)),
    new.raw_user_meta_data->>'phone',
    coalesce(new.raw_user_meta_data->>'avatar_color', '#F7941D')
  );
  return new;
end;
$$;

create or replace trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure handle_new_user();

-- DONE ✓
