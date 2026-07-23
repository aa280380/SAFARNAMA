import base64, os

with open('/tmp/logo.svg', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode()
logo_uri = f'data:image/svg+xml;base64,{logo_b64}'

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>SafarNama — Your 24/7 Travel Planner</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.2/babel.min.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
:root{{
  --navy:#1B2B6B;--orange:#F7941D;--orange2:#FF6B35;
  --light:#FFF8F0;--gray:#F5F7FA;--text:#333;--muted:#888;
  --white:#fff;--green:#27AE60;--red:#E74C3C;
  --shadow:0 4px 20px rgba(27,43,107,0.12);
}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#F5F7FA;color:var(--text);}}
#root{{min-height:100vh;}}
/* NAV */
.nav{{background:var(--navy);padding:12px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(0,0,0,0.2);}}
.nav-logo{{display:flex;align-items:center;gap:10px;cursor:pointer;}}
.nav-logo img{{width:44px;height:44px;border-radius:50%;border:2px solid var(--orange);}}
.nav-logo-text{{color:white;font-size:18px;font-weight:700;letter-spacing:0.5px;}}
.nav-logo-sub{{color:var(--orange);font-size:10px;letter-spacing:1px;}}
.nav-links{{display:flex;gap:8px;align-items:center;}}
.nav-btn{{background:var(--orange);color:white;border:none;padding:8px 18px;border-radius:20px;cursor:pointer;font-size:13px;font-weight:600;transition:all .2s;}}
.nav-btn:hover{{background:#e8830a;transform:translateY(-1px);}}
.nav-btn.ghost{{background:transparent;border:1.5px solid var(--orange);color:var(--orange);}}
.avatar{{width:36px;height:36px;border-radius:50%;background:var(--orange);display:flex;align-items:center;justify-content:center;color:white;font-weight:700;font-size:14px;}}
/* SCREENS */
.screen{{min-height:calc(100vh - 68px);animation:fadeIn .3s ease;}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
/* HERO / LANDING */
.hero{{background:linear-gradient(135deg,var(--navy) 0%,#2d4a9e 50%,#1B2B6B 100%);min-height:calc(100vh - 68px);display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 20px;position:relative;overflow:hidden;}}
.hero-content{{position:relative;z-index:1;max-width:700px;}}
.hero-logo{{width:130px;height:130px;border-radius:50%;border:3px solid var(--orange);margin:0 auto 24px;box-shadow:0 0 40px rgba(247,148,29,0.4);}}
.hero h1{{font-size:40px;font-weight:800;color:white;line-height:1.2;margin-bottom:16px;}}
.hero h1 span{{color:var(--orange);}}
.hero p{{font-size:17px;color:rgba(255,255,255,0.82);margin-bottom:36px;line-height:1.6;}}
.hero-btns{{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;}}
.btn-primary{{background:var(--orange);color:white;border:none;padding:14px 32px;border-radius:30px;cursor:pointer;font-size:16px;font-weight:700;transition:all .3s;box-shadow:0 4px 20px rgba(247,148,29,0.4);}}
.btn-primary:hover{{transform:translateY(-3px);box-shadow:0 8px 30px rgba(247,148,29,0.5);}}
.btn-secondary{{background:transparent;color:white;border:2px solid white;padding:14px 32px;border-radius:30px;cursor:pointer;font-size:16px;font-weight:600;transition:all .3s;}}
.btn-secondary:hover{{background:white;color:var(--navy);}}
.features-strip{{display:flex;gap:32px;justify-content:center;margin-top:48px;flex-wrap:wrap;}}
.feat{{display:flex;flex-direction:column;align-items:center;gap:8px;color:rgba(255,255,255,0.85);}}
.feat-icon{{font-size:32px;}}
.feat span{{font-size:13px;font-weight:500;}}
/* AUTH */
.auth-wrap{{display:flex;align-items:center;justify-content:center;min-height:calc(100vh - 68px);padding:40px 20px;background:linear-gradient(135deg,#f0f4ff 0%,#fff8f0 100%);}}
.auth-card{{background:white;border-radius:20px;padding:40px;width:100%;max-width:420px;box-shadow:var(--shadow);}}
.auth-logo{{text-align:center;margin-bottom:28px;}}
.auth-logo img{{width:80px;height:80px;border-radius:50%;}}
.auth-card h2{{text-align:center;color:var(--navy);font-size:22px;margin-bottom:6px;}}
.auth-card p{{text-align:center;color:var(--muted);font-size:14px;margin-bottom:28px;}}
.tabs{{display:flex;background:#f0f4ff;border-radius:12px;padding:4px;margin-bottom:28px;}}
.tab{{flex:1;padding:10px;text-align:center;border-radius:8px;cursor:pointer;font-size:14px;font-weight:600;color:var(--muted);transition:all .2s;}}
.tab.active{{background:var(--navy);color:white;}}
.form-group{{margin-bottom:18px;}}
.form-group label{{display:block;font-size:13px;font-weight:600;color:var(--navy);margin-bottom:6px;}}
.form-group input,.form-group select{{width:100%;padding:12px 16px;border:1.5px solid #e0e0e0;border-radius:10px;font-size:14px;transition:border .2s;outline:none;}}
.form-group input:focus,.form-group select:focus{{border-color:var(--orange);}}
.btn-full{{width:100%;padding:14px;background:var(--navy);color:white;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;transition:all .2s;}}
.btn-full:hover{{background:#2d4a9e;}}
.divider{{text-align:center;color:var(--muted);font-size:13px;margin:16px 0;}}
/* DASHBOARD */
.dash{{padding:28px 24px;max-width:900px;margin:0 auto;}}
.dash-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;}}
.dash-header h2{{font-size:24px;font-weight:800;color:var(--navy);}}
.greeting{{color:var(--muted);font-size:14px;margin-top:2px;}}
.card-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px;margin-bottom:32px;}}
.trip-card{{background:white;border-radius:16px;overflow:hidden;box-shadow:var(--shadow);cursor:pointer;transition:all .25s;}}
.trip-card:hover{{transform:translateY(-4px);box-shadow:0 8px 30px rgba(27,43,107,0.18);}}
.trip-card-img{{height:130px;display:flex;align-items:center;justify-content:center;font-size:60px;position:relative;}}
.trip-card-img .badge{{position:absolute;top:10px;right:10px;background:var(--green);color:white;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;}}
.trip-card-body{{padding:16px;}}
.trip-card-body h3{{font-size:16px;font-weight:700;color:var(--navy);margin-bottom:4px;}}
.trip-meta{{display:flex;gap:12px;color:var(--muted);font-size:12px;margin-top:8px;flex-wrap:wrap;}}
.create-card{{background:linear-gradient(135deg,var(--navy),#2d4a9e);border-radius:16px;padding:28px;color:white;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:200px;text-align:center;transition:all .25s;}}
.create-card:hover{{transform:translateY(-4px);}}
.create-card .plus{{font-size:48px;margin-bottom:12px;}}
.create-card h3{{font-size:18px;font-weight:700;}}
.create-card p{{font-size:13px;opacity:0.8;margin-top:6px;}}
.section-title{{font-size:18px;font-weight:700;color:var(--navy);margin-bottom:16px;}}
/* PERSONA CHIP */
.persona-strip{{display:flex;gap:12px;margin-bottom:24px;overflow-x:auto;padding-bottom:4px;}}
.persona-chip{{display:flex;align-items:center;gap:8px;background:white;border:1.5px solid #e0e0e0;border-radius:20px;padding:8px 16px;white-space:nowrap;cursor:pointer;transition:all .2s;flex-shrink:0;}}
.persona-chip.active{{border-color:var(--orange);background:#fff8f0;}}
.p-av{{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:11px;font-weight:700;}}
.p-name{{font-size:13px;font-weight:700;color:var(--navy);}}
.p-role{{font-size:10px;color:var(--muted);}}
/* CREATE TRIP */
.create-wrap{{max-width:680px;margin:0 auto;padding:28px 24px;}}
.step-bar{{display:flex;gap:0;margin-bottom:36px;align-items:flex-start;}}
.step{{display:flex;flex-direction:column;align-items:center;gap:6px;}}
.step-circle{{width:36px;height:36px;border-radius:50%;background:#e0e0e0;color:#999;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;transition:all .3s;}}
.step.active .step-circle{{background:var(--orange);color:white;}}
.step.done .step-circle{{background:var(--green);color:white;}}
.step-label{{font-size:11px;color:var(--muted);font-weight:500;}}
.step.active .step-label{{color:var(--orange);font-weight:700;}}
.step-line{{flex:1;height:2px;background:#e0e0e0;margin-top:18px;}}
.step-line.done{{background:var(--green);}}
.form-card{{background:white;border-radius:20px;padding:28px;box-shadow:var(--shadow);}}
.form-card h3{{font-size:18px;font-weight:700;color:var(--navy);margin-bottom:6px;}}
.form-card > p{{color:var(--muted);font-size:13px;margin-bottom:24px;}}
.dest-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;}}
.dest-option{{border:2px solid #e0e0e0;border-radius:12px;padding:16px;cursor:pointer;text-align:center;transition:all .2s;}}
.dest-option.selected{{border-color:var(--orange);background:#fff8f0;}}
.dest-option .emoji{{font-size:32px;margin-bottom:8px;}}
.dest-option .name{{font-size:14px;font-weight:700;color:var(--navy);}}
.dest-option .sub{{font-size:11px;color:var(--muted);}}
.friend-row{{display:flex;align-items:center;gap:12px;padding:12px;background:#f8f9ff;border-radius:12px;margin-bottom:10px;}}
.friend-avatar{{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:700;font-size:16px;flex-shrink:0;}}
.friend-info{{flex:1;}}
.friend-info .fname{{font-size:14px;font-weight:700;color:var(--navy);}}
.friend-info .fcity{{font-size:12px;color:var(--muted);}}
.friend-status{{font-size:11px;padding:4px 10px;border-radius:20px;font-weight:600;}}
.status-pending{{background:#fff3e0;color:#e65100;}}
.status-joined{{background:#e8f5e9;color:#2e7d32;}}
.btn-row{{display:flex;gap:12px;margin-top:24px;}}
.btn-next{{flex:1;padding:13px;background:var(--orange);color:white;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;}}
.btn-next:disabled{{opacity:0.5;cursor:not-allowed;}}
.btn-back{{padding:13px 20px;background:#f0f0f0;color:var(--navy);border:none;border-radius:12px;font-size:15px;font-weight:600;cursor:pointer;}}
/* TRACKER */
.tracker{{padding:20px 24px;max-width:900px;margin:0 auto;}}
.tracker h2{{font-size:22px;font-weight:800;color:var(--navy);margin-bottom:4px;}}
.tracker-sub{{color:var(--muted);font-size:14px;margin-bottom:24px;}}
.map-container{{background:linear-gradient(160deg,#ddf1fa,#cce8f7);border-radius:20px;height:360px;position:relative;overflow:hidden;margin-bottom:24px;border:1.5px solid #b0d4ea;}}
.map-grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(100,149,200,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(100,149,200,.08) 1px,transparent 1px);background-size:40px 40px;}}
.map-label{{position:absolute;font-size:10px;font-weight:600;color:#4a7aaa;}}
.friend-pin{{position:absolute;display:flex;flex-direction:column;align-items:center;cursor:pointer;transition:left 1s linear, top 1s linear;}}
.pin-avatar{{width:36px;height:36px;border-radius:50%;color:white;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;border:2.5px solid white;box-shadow:0 3px 12px rgba(0,0,0,0.25);}}
.pin-name{{background:white;border-radius:8px;padding:3px 8px;font-size:10px;font-weight:700;color:var(--navy);margin-top:4px;box-shadow:0 2px 8px rgba(0,0,0,0.15);white-space:nowrap;}}
.destination-pin{{position:absolute;display:flex;flex-direction:column;align-items:center;}}
.dest-marker{{width:20px;height:20px;background:var(--red);border-radius:50% 50% 50% 0;transform:rotate(-45deg);border:2px solid white;box-shadow:0 2px 8px rgba(0,0,0,0.3);}}
.dest-label{{background:var(--red);color:white;font-size:10px;font-weight:700;padding:3px 8px;border-radius:8px;margin-top:6px;white-space:nowrap;}}
.friend-cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;}}
.friend-track-card{{background:white;border-radius:14px;padding:16px;box-shadow:var(--shadow);border-left:4px solid var(--orange);}}
.friend-track-card.arrived{{border-left-color:var(--green);}}
.friend-track-card.delayed{{border-left-color:var(--red);}}
.ftc-top{{display:flex;align-items:center;gap:10px;margin-bottom:10px;}}
.ftc-avatar{{width:40px;height:40px;border-radius:50%;color:white;font-weight:700;font-size:15px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.ftc-name{{font-size:14px;font-weight:700;color:var(--navy);}}
.ftc-city{{font-size:11px;color:var(--muted);}}
.ftc-status{{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text);}}
.status-dot{{width:8px;height:8px;border-radius:50%;flex-shrink:0;}}
.dot-moving{{background:var(--orange);animation:pulse 1.5s infinite;}}
.dot-arrived{{background:var(--green);}}
.dot-delayed{{background:var(--red);}}
@keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:0.6;transform:scale(1.3)}}}}
.eta-bar{{background:#f5f5f5;border-radius:8px;height:6px;margin-top:10px;}}
.eta-fill{{height:100%;border-radius:8px;background:linear-gradient(90deg,var(--orange),#FFB347);transition:width 1.5s;}}
.eta-fill.arrived{{background:var(--green);}}
.eta-fill.delayed{{background:var(--red);}}
/* PLACES */
.places{{padding:20px 24px;max-width:900px;margin:0 auto;}}
.places h2{{font-size:22px;font-weight:800;color:var(--navy);margin-bottom:4px;}}
.filter-row{{display:flex;gap:8px;margin-bottom:24px;flex-wrap:wrap;}}
.filter-btn{{padding:8px 18px;border-radius:20px;border:1.5px solid #e0e0e0;background:white;cursor:pointer;font-size:13px;font-weight:600;color:var(--muted);transition:all .2s;}}
.filter-btn.active{{background:var(--navy);color:white;border-color:var(--navy);}}
.places-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px;}}
.place-card{{background:white;border-radius:16px;overflow:hidden;box-shadow:var(--shadow);cursor:pointer;transition:all .25s;}}
.place-card:hover{{transform:translateY(-4px);}}
.place-img{{height:150px;display:flex;align-items:center;justify-content:center;font-size:72px;}}
.place-body{{padding:16px;}}
.place-body h3{{font-size:15px;font-weight:700;color:var(--navy);margin-bottom:4px;}}
.place-body p{{font-size:12px;color:var(--muted);margin-bottom:10px;line-height:1.5;}}
.place-meta{{display:flex;justify-content:space-between;align-items:center;}}
.rating{{color:#F7941D;font-size:12px;font-weight:600;}}
.vote-btn{{background:#f0f4ff;color:var(--navy);border:none;padding:6px 14px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;transition:all .2s;}}
.vote-btn.voted{{background:var(--navy);color:white;}}
.vote-count{{font-size:11px;color:var(--muted);margin-top:4px;text-align:right;}}
/* HOTELS */
.hotels{{padding:20px 24px;max-width:900px;margin:0 auto;}}
.hotels h2{{font-size:22px;font-weight:800;color:var(--navy);margin-bottom:4px;}}
.hotel-card{{background:white;border-radius:16px;padding:20px;box-shadow:var(--shadow);margin-bottom:16px;display:flex;gap:20px;cursor:pointer;transition:all .25s;}}
.hotel-card:hover{{transform:translateX(4px);}}
.hotel-img{{width:100px;height:100px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:50px;flex-shrink:0;}}
.hotel-info{{flex:1;}}
.hotel-info h3{{font-size:16px;font-weight:700;color:var(--navy);margin-bottom:4px;}}
.hotel-stars{{color:#F7941D;font-size:12px;margin-bottom:8px;}}
.hotel-tags{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px;}}
.htag{{background:#f0f4ff;color:var(--navy);font-size:10px;font-weight:600;padding:3px 8px;border-radius:8px;}}
.hotel-bottom{{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;}}
.hotel-price{{font-size:18px;font-weight:800;color:var(--navy);}}
.hotel-price span{{font-size:12px;font-weight:400;color:var(--muted);}}
.hotel-per-person{{font-size:11px;color:var(--green);font-weight:600;}}
.book-btn{{background:var(--orange);color:white;border:none;padding:10px 22px;border-radius:12px;font-size:13px;font-weight:700;cursor:pointer;transition:all .2s;}}
.book-btn.booked{{background:var(--green);}}
/* COST */
.cost{{padding:20px 24px;max-width:780px;margin:0 auto;}}
.cost h2{{font-size:22px;font-weight:800;color:var(--navy);margin-bottom:4px;}}
.summary-cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:28px;}}
.sum-card{{background:white;border-radius:14px;padding:18px;box-shadow:var(--shadow);text-align:center;}}
.sum-card .val{{font-size:22px;font-weight:800;color:var(--navy);}}
.sum-card .lbl{{font-size:12px;color:var(--muted);margin-top:4px;}}
.expense-row{{background:white;border-radius:14px;padding:16px 20px;box-shadow:0 2px 10px rgba(0,0,0,0.06);margin-bottom:14px;}}
.exp-top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;}}
.exp-name{{font-size:15px;font-weight:700;color:var(--navy);}}
.exp-total{{font-size:15px;font-weight:800;color:var(--navy);}}
.exp-payers{{display:flex;gap:8px;flex-wrap:wrap;}}
.payer{{display:flex;align-items:center;gap:8px;background:#f8f9ff;padding:8px 12px;border-radius:10px;flex:1;min-width:140px;}}
.payer-av{{width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:12px;font-weight:700;flex-shrink:0;}}
.pname{{font-size:12px;font-weight:700;color:var(--navy);}}
.pamount{{font-size:11px;color:var(--muted);}}
.pay-status{{margin-left:auto;font-size:10px;font-weight:700;padding:3px 8px;border-radius:8px;white-space:nowrap;}}
.paid{{background:#e8f5e9;color:#2e7d32;}}
.unpaid{{background:#fff3e0;color:#e65100;}}
/* BOTTOM NAV */
.bottom-nav{{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid #eee;display:flex;z-index:99;box-shadow:0 -4px 20px rgba(0,0,0,0.08);}}
.bnav-item{{flex:1;display:flex;flex-direction:column;align-items:center;padding:10px 4px;cursor:pointer;transition:all .2s;border:none;background:none;}}
.bnav-item .icon{{font-size:22px;margin-bottom:2px;}}
.bnav-item .label{{font-size:10px;font-weight:600;color:var(--muted);}}
.bnav-item.active .label{{color:var(--orange);}}
.bnav-item.active .icon{{transform:scale(1.15);}}
.pb{{padding-bottom:72px;}}
/* MODAL */
.modal-overlay{{position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:200;display:flex;align-items:flex-end;justify-content:center;}}
.modal{{background:white;border-radius:24px 24px 0 0;padding:28px;width:100%;max-width:500px;animation:slideUp .3s ease;}}
@keyframes slideUp{{from{{transform:translateY(100%)}}to{{transform:translateY(0)}}}}
.modal-close{{float:right;background:none;border:none;font-size:22px;cursor:pointer;color:var(--muted);line-height:1;}}
/* PERSONA BOX */
.persona-box{{background:#fff8f0;border:1px solid #ffe0b2;border-radius:12px;padding:12px 16px;margin-bottom:24px;font-size:13px;color:#555;}}
</style>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const {{ useState, useEffect }} = React;
const LOGO = "{logo_uri}";

const PERSONAS = [
  {{id:1,name:"Arjun Mehta",role:"The Coordinator",emoji:"👨‍💼",color:"#F7941D",city:"Mumbai",desc:"Planning Goa trip for 7 friends arriving from different cities. His main need: see where everyone is in real time, find the best spots together, and track who paid what."}},
  {{id:2,name:"Priya Sharma",role:"The Joiner",emoji:"👩",color:"#9C27B0",city:"Delhi",desc:"Joining Arjun's Goa trip. Wants to see itinerary, vote on places to visit, and pay her share in one tap."}},
  {{id:3,name:"Rahul Das",role:"The Explorer",emoji:"🧑‍🎒",color:"#1565C0",city:"Bangalore",desc:"Already in Goa! Votes on the best activities and helps the group decide where to go next."}},
];

const FRIENDS = [
  {{id:1,name:"Arjun",city:"Mumbai",color:"#F7941D",status:"moving",progress:70,eta:"2h 10m",transport:"✈️",startL:72,startT:20}},
  {{id:2,name:"Priya",city:"Delhi",color:"#9C27B0",status:"moving",progress:50,eta:"3h 40m",transport:"✈️",startL:50,startT:8}},
  {{id:3,name:"Rahul",city:"Bangalore",color:"#1565C0",status:"arrived",progress:100,eta:"Arrived!",transport:"🛬",startL:68,startT:65}},
  {{id:4,name:"Sneha",city:"Pune",color:"#E53935",status:"delayed",progress:28,eta:"5h (delayed)",transport:"🚂",startL:58,startT:28}},
  {{id:5,name:"Karan",city:"Chennai",color:"#2E7D32",status:"moving",progress:78,eta:"1h 20m",transport:"✈️",startL:72,startT:62}},
  {{id:6,name:"Isha",city:"Hyderabad",color:"#795548",status:"moving",progress:58,eta:"2h 45m",transport:"🚌",startL:65,startT:45}},
  {{id:7,name:"Dev",city:"Ahmedabad",color:"#0097A7",status:"moving",progress:62,eta:"2h 00m",transport:"✈️",startL:55,startT:18}},
];

const PLACES = [
  {{id:1,cat:"beach",name:"Baga Beach",desc:"Perfect for the whole group — water sports, beach shacks & legendary sunsets.",emoji:"🏖️",rating:"4.8",votes:4,bg:"linear-gradient(135deg,#e3f2fd,#bbdefb)"}},
  {{id:2,cat:"food",name:"Infantaria Café",desc:"Best croissants & all-day breakfast in North Goa. Group tables available.",emoji:"☕",rating:"4.6",votes:3,bg:"linear-gradient(135deg,#fff8e1,#ffe082)"}},
  {{id:3,cat:"adventure",name:"Water Sports Hub",desc:"Parasailing, banana boat & jet ski — group packages save 30%.",emoji:"🤿",rating:"4.7",votes:5,bg:"linear-gradient(135deg,#e8f5e9,#a5d6a7)"}},
  {{id:4,cat:"culture",name:"Basilica of Bom Jesus",desc:"UNESCO Heritage site. A must-see landmark — only 20 min from the beach.",emoji:"⛪",rating:"4.9",votes:2,bg:"linear-gradient(135deg,#f3e5f5,#ce93d8)"}},
  {{id:5,cat:"nightlife",name:"Tito's Lane",desc:"Goa's iconic nightlife strip. Open till dawn — whole group can enter free before 10pm.",emoji:"🎶",rating:"4.5",votes:6,bg:"linear-gradient(135deg,#fce4ec,#f48fb1)"}},
  {{id:6,cat:"food",name:"Vinayak Family Restaurant",desc:"Authentic Goan fish curry, rice & feni. Group thalis ₹280/person.",emoji:"🍛",rating:"4.8",votes:3,bg:"linear-gradient(135deg,#fff3e0,#ffcc80)"}},
];

const HOTELS = [
  {{id:1,name:"The Leela Goa",stars:"★★★★★",img:"🏨",tags:["Group-friendly","Pool","Beach View","Breakfast incl."],price:"₹8,200",perPerson:"₹1,171",bg:"linear-gradient(135deg,#e3f2fd,#bbdefb)"}},
  {{id:2,name:"Taj Exotica Resort",stars:"★★★★★",img:"🌅",tags:["Luxury","Spa","Private Beach","Group Rates"],price:"₹11,500",perPerson:"₹1,643",bg:"linear-gradient(135deg,#f3e5f5,#ce93d8)"}},
  {{id:3,name:"O Hotel Goa",stars:"★★★★",img:"🏩",tags:["Villa","Party Pool","City View","Rooftop Bar"],price:"₹5,400",perPerson:"₹771",bg:"linear-gradient(135deg,#e8f5e9,#a5d6a7)"}},
  {{id:4,name:"Treehouse Silversands",stars:"★★★★",img:"🌴",tags:["Beachfront","Budget Pick","Large Group OK"],price:"₹3,800",perPerson:"₹543",bg:"linear-gradient(135deg,#fff8e1,#ffe082)"}},
];

const EXPENSES = [
  {{id:1,name:"✈️ Flight Tickets",total:"₹47,600",payers:[
    {{name:"Arjun",amount:"₹6,800",color:"#F7941D",paid:true}},
    {{name:"Priya",amount:"₹6,800",color:"#9C27B0",paid:true}},
    {{name:"Rahul",amount:"₹6,800",color:"#1565C0",paid:false}},
    {{name:"Sneha",amount:"₹6,800",color:"#E53935",paid:false}},
    {{name:"Karan",amount:"₹6,800",color:"#2E7D32",paid:true}},
    {{name:"Isha",amount:"₹6,800",color:"#795548",paid:false}},
    {{name:"Dev",amount:"₹6,800",color:"#0097A7",paid:true}},
  ]}},
  {{id:2,name:"🏨 Hotel — The Leela (3 nights)",total:"₹24,600",payers:[
    {{name:"Arjun",amount:"₹3,514",color:"#F7941D",paid:true}},
    {{name:"Priya",amount:"₹3,514",color:"#9C27B0",paid:true}},
    {{name:"Rahul",amount:"₹3,514",color:"#1565C0",paid:false}},
    {{name:"Sneha",amount:"₹3,514",color:"#E53935",paid:false}},
    {{name:"Karan",amount:"₹3,514",color:"#2E7D32",paid:true}},
    {{name:"Isha",amount:"₹3,514",color:"#795548",paid:false}},
    {{name:"Dev",amount:"₹3,516",color:"#0097A7",paid:true}},
  ]}},
  {{id:3,name:"🤿 Water Sports Package",total:"₹14,000",payers:[
    {{name:"Arjun",amount:"₹2,000",color:"#F7941D",paid:true}},
    {{name:"Priya",amount:"₹2,000",color:"#9C27B0",paid:false}},
    {{name:"Rahul",amount:"₹2,000",color:"#1565C0",paid:false}},
    {{name:"Sneha",amount:"₹2,000",color:"#E53935",paid:false}},
    {{name:"Karan",amount:"₹2,000",color:"#2E7D32",paid:true}},
    {{name:"Isha",amount:"₹2,000",color:"#795548",paid:false}},
    {{name:"Dev",amount:"₹2,000",color:"#0097A7",paid:false}},
  ]}},
];

function App() {{
  const [screen, setScreen] = useState("landing");
  const [authTab, setAuthTab] = useState("login");
  const [createStep, setCreateStep] = useState(1);
  const [selectedDest, setSelectedDest] = useState(null);
  const [votes, setVotes] = useState({{}});
  const [filter, setFilter] = useState("all");
  const [activePersona, setActivePersona] = useState(1);
  const [bookedHotel, setBookedHotel] = useState(null);
  const [modal, setModal] = useState(null);
  const [friendProgress, setFriendProgress] = useState(FRIENDS.map(f => f.progress));

  const loggedIn = !["landing","auth"].includes(screen);

  useEffect(() => {{
    if (screen !== "tracker") return;
    const t = setInterval(() => {{
      setFriendProgress(prev => prev.map((p, i) =>
        FRIENDS[i].status === "moving" ? Math.min(p + Math.random() * 0.5, 96) : p
      ));
    }}, 1200);
    return () => clearInterval(t);
  }}, [screen]);

  const go = s => {{ setScreen(s); window.scrollTo(0,0); }};

  function Nav() {{
    return (
      <nav className="nav">
        <div className="nav-logo" onClick={() => go(loggedIn ? "dashboard" : "landing")}>
          <img src={{LOGO}} alt="SafarNama"/>
          <div>
            <div className="nav-logo-text">SafarNama</div>
            <div className="nav-logo-sub">HORIZONS TOGETHER</div>
          </div>
        </div>
        {{!loggedIn ? (
          <div className="nav-links">
            <button className="nav-btn ghost" onClick={() => go("auth")}>Login</button>
            <button className="nav-btn" onClick={() => {{ setAuthTab("signup"); go("auth"); }}}>Sign Up Free</button>
          </div>
        ) : (
          <div style={{{{display:"flex",alignItems:"center",gap:12}}}}>
            <button className="nav-btn" style={{{{fontSize:12}}}} onClick={() => {{ setCreateStep(1); go("create"); }}}> + New Trip</button>
            <div className="avatar">A</div>
          </div>
        )}}
      </nav>
    );
  }}

  function BottomNav() {{
    if (!loggedIn) return null;
    const items = [
      {{id:"dashboard",icon:"🏠",label:"Home"}},
      {{id:"tracker",icon:"📍",label:"Track"}},
      {{id:"places",icon:"🗺️",label:"Explore"}},
      {{id:"hotels",icon:"🏨",label:"Hotels"}},
      {{id:"cost",icon:"💰",label:"Split"}},
    ];
    return (
      <nav className="bottom-nav">
        {{items.map(i => (
          <button key={{i.id}} className={{"bnav-item" + (screen===i.id?" active":"")}} onClick={() => go(i.id)}>
            <span className="icon">{{i.icon}}</span>
            <span className="label">{{i.label}}</span>
          </button>
        ))}}
      </nav>
    );
  }}

  /* ── LANDING ── */
  function Landing() {{
    return (
      <div className="screen">
        <div className="hero">
          <div className="hero-content">
            <img src={{LOGO}} className="hero-logo" alt="SafarNama"/>
            <h1>Travel Together,<br/><span>Stress Never.</span></h1>
            <p>Plan group trips with friends from anywhere in India.<br/>Track everyone live, explore top spots, split costs — one app.</p>
            <div className="hero-btns">
              <button className="btn-primary" onClick={() => {{ setAuthTab("signup"); go("auth"); }}}>Start a Group Trip →</button>
              <button className="btn-secondary" onClick={() => go("auth")}>Login</button>
            </div>
            <div className="features-strip">
              {{[["📍","Live Friend Tracking"],["🗺️","Group Explore"],["🏨","Best Hotels"],["💰","Smart Cost Split"]].map(([e,l]) => (
                <div className="feat" key={{l}}><span className="feat-icon">{{e}}</span><span>{{l}}</span></div>
              ))}}
            </div>
          </div>
        </div>
      </div>
    );
  }}

  /* ── AUTH ── */
  function Auth() {{
    return (
      <div className="screen">
        <div className="auth-wrap">
          <div className="auth-card">
            <div className="auth-logo"><img src={{LOGO}} alt="SafarNama"/></div>
            <h2>Welcome to SafarNama</h2>
            <p>Your 24/7 group travel companion</p>
            <div className="tabs">
              <div className={{"tab"+(authTab==="login"?" active":"")}} onClick={{()=>setAuthTab("login")}}>Login</div>
              <div className={{"tab"+(authTab==="signup"?" active":"")}} onClick={{()=>setAuthTab("signup")}}>Sign Up</div>
            </div>
            {{authTab==="signup" && <div className="form-group"><label>Full Name</label><input placeholder="Arjun Mehta"/></div>}}
            <div className="form-group"><label>Email</label><input placeholder="arjun@email.com" type="email"/></div>
            <div className="form-group"><label>Password</label><input placeholder="••••••••" type="password"/></div>
            {{authTab==="signup" && (
              <div className="form-group"><label>Your Departure City</label>
                <select><option>Mumbai</option><option>Delhi</option><option>Bangalore</option><option>Hyderabad</option><option>Chennai</option><option>Pune</option><option>Ahmedabad</option></select>
              </div>
            )}}
            <button className="btn-full" onClick={{()=>go("dashboard")}}>{{authTab==="login"?"Login →":"Create Account →"}}</button>
            <div className="divider">or</div>
            <button className="btn-full" style={{{{background:"white",color:"#333",border:"1.5px solid #e0e0e0"}}}} onClick={{()=>go("dashboard")}}>🇮🇳 Continue with Google</button>
          </div>
        </div>
      </div>
    );
  }}

  /* ── DASHBOARD ── */
  function Dashboard() {{
    const persona = PERSONAS.find(p=>p.id===activePersona);
    return (
      <div className="screen pb">
        <div className="dash">
          <div className="dash-header">
            <div><div className="greeting">Good morning 👋</div><h2>Hey Arjun!</h2></div>
            <button className="nav-btn" onClick={{()=>{{setCreateStep(1);go("create");}}}}>+ New Trip</button>
          </div>

          <div className="section-title">👤 User Persona</div>
          <div className="persona-strip">
            {{PERSONAS.map(p => (
              <div key={{p.id}} className={{"persona-chip"+(activePersona===p.id?" active":"")}} onClick={{()=>setActivePersona(p.id)}}>
                <div className="p-av" style={{{{background:p.color}}}}>{{p.emoji}}</div>
                <div><div className="p-name">{{p.name}}</div><div className="p-role">{{p.role}} · {{p.city}}</div></div>
              </div>
            ))}}
          </div>
          {{persona && (
            <div className="persona-box">💡 <strong>{{persona.name}}</strong>: {{persona.desc}}</div>
          )}}

          <div className="section-title">🧳 My Trips</div>
          <div className="card-grid">
            <div className="trip-card" onClick={{()=>go("tracker")}}>
              <div className="trip-card-img" style={{{{background:"linear-gradient(135deg,#e3f2fd,#90caf9)"}}}}>
                🏖️<div className="badge">● LIVE</div>
              </div>
              <div className="trip-card-body">
                <h3>Goa — Beach Gang 2025</h3>
                <div className="trip-meta">
                  <span>📅 Aug 15–19</span><span>👥 7 friends</span><span>✈️ 5 cities</span>
                </div>
                <div style={{{{marginTop:10,background:"#e8f5e9",borderRadius:8,padding:"6px 10px",fontSize:12,color:"#2e7d32",fontWeight:600}}}}>
                  📍 Rahul arrived · 5 still in transit
                </div>
              </div>
            </div>
            <div className="trip-card" onClick={{()=>go("tracker")}}>
              <div className="trip-card-img" style={{{{background:"linear-gradient(135deg,#f3e5f5,#ce93d8)"}}}}>🏰</div>
              <div className="trip-card-body">
                <h3>Rajasthan Heritage Tour</h3>
                <div className="trip-meta"><span>📅 Oct 3–8</span><span>👥 4 friends</span><span>🗓️ Planning</span></div>
              </div>
            </div>
            <div className="create-card" onClick={{()=>{{setCreateStep(1);go("create");}}}}>
              <div className="plus">+</div>
              <h3>Plan a New Trip</h3>
              <p>Add destination, invite friends from any city</p>
            </div>
          </div>

          <div className="section-title">⚡ Quick Actions</div>
          <div style={{{{display:"flex",gap:12,flexWrap:"wrap"}}}}>
            {{[["📍","Track Friends","tracker"],["🗺️","Explore Goa","places"],["🏨","Find Hotels","hotels"],["💰","Split Costs","cost"]].map(([e,l,s])=>(
              <button key={{s}} onClick={{()=>go(s)}} style={{{{background:"white",border:"1.5px solid #e0e0e0",borderRadius:12,padding:"12px 18px",cursor:"pointer",display:"flex",alignItems:"center",gap:8,fontSize:13,fontWeight:600,color:"var(--navy)"}}}}>
                {{e}} {{l}}
              </button>
            ))}}
          </div>
        </div>
      </div>
    );
  }}

  /* ── CREATE TRIP ── */
  function CreateTrip() {{
    const dests = [
      {{id:1,name:"Goa",sub:"Beaches & Nightlife",emoji:"🏖️",bg:"#e3f2fd"}},
      {{id:2,name:"Manali",sub:"Mountains & Snow",emoji:"🏔️",bg:"#e8f5e9"}},
      {{id:3,name:"Jaipur",sub:"Heritage & Culture",emoji:"🏰",bg:"#f3e5f5"}},
      {{id:4,name:"Kerala",sub:"Backwaters & Nature",emoji:"🌴",bg:"#fff8e1"}},
    ];
    const steps = ["Destination","Dates","Friends","Launch"];
    return (
      <div className="screen pb">
        <div className="create-wrap">
          <h2 style={{{{fontSize:22,fontWeight:800,color:"var(--navy)",marginBottom:24}}}}>Plan Your Group Trip</h2>
          <div className="step-bar">
            {{steps.map((s,i) => (
              <React.Fragment key={{s}}>
                <div className={{"step"+(createStep>i+1?" done":createStep===i+1?" active":"")}}>
                  <div className="step-circle">{{createStep>i+1?"✓":i+1}}</div>
                  <div className="step-label">{{s}}</div>
                </div>
                {{i<steps.length-1 && <div className={{"step-line"+(createStep>i+1?" done":"")}}/>}}
              </React.Fragment>
            ))}}
          </div>

          {{createStep===1 && (
            <div className="form-card">
              <h3>Where are you heading?</h3>
              <p>Pick a destination for the group</p>
              <div className="dest-grid">
                {{dests.map(d=>(
                  <div key={{d.id}} className={{"dest-option"+(selectedDest===d.id?" selected":"")}} style={{{{background:selectedDest===d.id?"#fff8f0":d.bg}}}} onClick={{()=>setSelectedDest(d.id)}}>
                    <div className="emoji">{{d.emoji}}</div>
                    <div className="name">{{d.name}}</div>
                    <div className="sub">{{d.sub}}</div>
                  </div>
                ))}}
              </div>
              <div className="btn-row"><button className="btn-next" onClick={{()=>setCreateStep(2)}} disabled={{!selectedDest}}>Next: Set Dates →</button></div>
            </div>
          )}}

          {{createStep===2 && (
            <div className="form-card">
              <h3>When are you going?</h3>
              <p>Set travel dates for the whole group</p>
              <div className="form-group"><label>Departure Date</label><input type="date" defaultValue="2025-08-15"/></div>
              <div className="form-group"><label>Return Date</label><input type="date" defaultValue="2025-08-19"/></div>
              <div className="form-group"><label>Number of Travellers</label>
                <select defaultValue="7">{{[2,3,4,5,6,7,8,10,12,15].map(n=><option key={{n}}>{{n}} people</option>)}}</select>
              </div>
              <div className="btn-row">
                <button className="btn-back" onClick={{()=>setCreateStep(1)}}>← Back</button>
                <button className="btn-next" onClick={{()=>setCreateStep(3)}}>Next: Add Friends →</button>
              </div>
            </div>
          )}}

          {{createStep===3 && (
            <div className="form-card">
              <h3>Add your travel group</h3>
              <p>Each friend sets their own departure city — SafarNama tracks everyone live</p>
              {{FRIENDS.map(f=>(
                <div key={{f.id}} className="friend-row">
                  <div className="friend-avatar" style={{{{background:f.color}}}}>{{f.name[0]}}</div>
                  <div className="friend-info"><div className="fname">{{f.name}}</div><div className="fcity">From {{f.city}}</div></div>
                  <div className={{"friend-status "+(f.status==="arrived"?"status-joined":"status-pending")}}>
                    {{f.status==="arrived"?"✓ Joined":"Invited"}}
                  </div>
                </div>
              ))}}
              <button style={{{{width:"100%",padding:"12px",background:"#f0f4ff",border:"2px dashed #c0d0f0",borderRadius:12,color:"var(--navy)",fontWeight:600,cursor:"pointer",marginTop:12}}}}>
                + Invite More Friends
              </button>
              <div className="btn-row">
                <button className="btn-back" onClick={{()=>setCreateStep(2)}}>← Back</button>
                <button className="btn-next" onClick={{()=>setCreateStep(4)}}>Review →</button>
              </div>
            </div>
          )}}

          {{createStep===4 && (
            <div className="form-card">
              <h3>🎉 Ready to Launch!</h3>
              <p>Your group trip summary</p>
              {{[["📍","Destination","Goa — Beach Gang 2025"],["📅","Dates","Aug 15–19, 2025 (5 days)"],["👥","Group","7 friends from 5 cities"],["✈️","Departures","Mumbai, Delhi, Bangalore, Pune, Chennai, Hyderabad, Ahmedabad"]].map(([e,l,v])=>(
                <div key={{l}} style={{{{display:"flex",gap:12,padding:"12px 0",borderBottom:"1px solid #f0f0f0"}}}}>
                  <span style={{{{fontSize:20}}}}>{{e}}</span>
                  <div><div style={{{{fontSize:12,color:"var(--muted)"}}}}> {{l}}</div><div style={{{{fontWeight:600,color:"var(--navy)"}}}}> {{v}}</div></div>
                </div>
              ))}}
              <div className="btn-row">
                <button className="btn-back" onClick={{()=>setCreateStep(3)}}>← Back</button>
                <button className="btn-next" onClick={{()=>go("tracker")}}>🚀 Launch Trip!</button>
              </div>
            </div>
          )}}
        </div>
      </div>
    );
  }}

  /* ── TRACKER ── */
  function Tracker() {{
    // Map: India roughly 0-100% L/T. Goa is at ~15% L, 42% T
    const destL = 15, destT = 42;
    return (
      <div className="screen pb">
        <div className="tracker">
          <h2>📍 Live Friend Tracker</h2>
          <div className="tracker-sub">Goa Trip · Aug 15 · 7 friends · 5 cities · All tracked live</div>
          <div className="map-container">
            <div className="map-grid"/>
            {{/* India city labels */}}
            {{[["Mumbai",74,23],["Delhi",52,12],["Bangalore",68,66],["Pune",62,30],["Chennai",74,65],["Hyderabad",65,48],["Ahmedabad",52,22]].map(([c,l,t])=>(
              <span key={{c}} className="map-label" style={{{{left:`${{l}}%`,top:`${{t}}%`}}}}>{{c}}</span>
            ))}}
            {{/* Destination pin */}}
            <div className="destination-pin" style={{{{left:`${{destL}}%`,top:`${{destT}}%`,transform:"translate(-50%,-100%)"}}}}>
              <div className="dest-marker"/>
              <div className="dest-label">🏖️ GOA</div>
            </div>
            {{/* Friend pins moving toward Goa */}}
            {{FRIENDS.map((f,i) => {{
              const p = friendProgress[i] / 100;
              const l = f.startL + (destL - f.startL) * p;
              const t = f.startT + (destT - f.startT) * p;
              return (
                <div key={{f.id}} className="friend-pin" style={{{{left:`${{l}}%`,top:`${{t}}%`,transform:"translate(-50%,-50%)"}}}}>
                  <div className="pin-avatar" style={{{{background:f.color}}}}>{{f.name[0]}}</div>
                  <div className="pin-name">{{f.transport}} {{f.name}}</div>
                </div>
              );
            }})}}
          </div>

          <div className="friend-cards">
            {{FRIENDS.map((f,i) => (
              <div key={{f.id}} className={{"friend-track-card"+(f.status==="arrived"?" arrived":f.status==="delayed"?" delayed":"")}}>
                <div className="ftc-top">
                  <div className="ftc-avatar" style={{{{background:f.color}}}}>{{f.name[0]}}</div>
                  <div><div className="ftc-name">{{f.name}}</div><div className="ftc-city">{{f.transport}} from {{f.city}}</div></div>
                </div>
                <div className="ftc-status">
                  <div className={{"status-dot dot-"+f.status}}/>
                  {{f.status==="arrived"?"🎉 Arrived in Goa!":f.status==="delayed"?"⚠️ Delayed · "+f.eta:"In transit · ETA "+f.eta}}
                </div>
                <div className="eta-bar">
                  <div className={{"eta-fill "+f.status}} style={{{{width:`${{Math.round(friendProgress[i])}}%`}}}}/>
                </div>
              </div>
            ))}}
          </div>

          <div style={{{{background:"#fff8f0",border:"1px solid #ffe0b2",borderRadius:14,padding:16,marginTop:20}}}}>
            <div style={{{{fontWeight:700,color:"var(--navy)",marginBottom:8}}}}>📊 Group Travel Status</div>
            <div style={{{{display:"flex",gap:20,fontSize:13,flexWrap:"wrap"}}}}>
              <span>🟢 1 Arrived</span><span>🟠 5 In Transit</span><span>🔴 1 Delayed</span>
            </div>
          </div>
        </div>
      </div>
    );
  }}

  /* ── PLACES ── */
  function Places() {{
    const cats = ["all","beach","food","adventure","culture","nightlife"];
    const filtered = filter==="all" ? PLACES : PLACES.filter(p=>p.cat===filter);
    return (
      <div className="screen pb">
        <div className="places">
          <h2>🗺️ Explore Goa Together</h2>
          <p style={{{{color:"var(--muted)",fontSize:14,marginBottom:16}}}}>Vote on what the group wants to do — top votes go on the itinerary</p>
          <div className="filter-row">
            {{cats.map(c=>(
              <button key={{c}} className={{"filter-btn"+(filter===c?" active":"")}} onClick={{()=>setFilter(c)}}>
                {{{{all:"All",beach:"🏖️ Beach",food:"🍛 Food",adventure:"🤿 Adventure",culture:"⛪ Culture",nightlife:"🎶 Nightlife"}}[c]}}
              </button>
            ))}}
          </div>
          <div className="places-grid">
            {{filtered.map(p=>(
              <div key={{p.id}} className="place-card">
                <div className="place-img" style={{{{background:p.bg}}}}>{{p.emoji}}</div>
                <div className="place-body">
                  <h3>{{p.name}}</h3>
                  <p>{{p.desc}}</p>
                  <div className="place-meta">
                    <div><div className="rating">★ {{p.rating}}</div></div>
                    <div style={{{{textAlign:"right"}}}}>
                      <button className={{"vote-btn"+(votes[p.id]?" voted":"")}} onClick={{()=>setVotes(v=>{{...v,[p.id]:!v[p.id]}})}}>
                        {{votes[p.id]?"✓ I'm in!":"👍 Count me in"}}
                      </button>
                      <div className="vote-count">{{p.votes+(votes[p.id]?1:0)}} friends want this</div>
                    </div>
                  </div>
                </div>
              </div>
            ))}}
          </div>
        </div>
      </div>
    );
  }}

  /* ── HOTELS ── */
  function Hotels() {{
    return (
      <div className="screen pb">
        <div className="hotels">
          <h2>🏨 Best Hotels in Goa</h2>
          <p style={{{{color:"var(--muted)",fontSize:14,marginBottom:20}}}}>Group-friendly picks · 7 people · Aug 15–19 · Price per night</p>
          {{HOTELS.map(h=>(
            <div key={{h.id}} className="hotel-card">
              <div className="hotel-img" style={{{{background:h.bg}}}}>{{h.img}}</div>
              <div className="hotel-info">
                <h3>{{h.name}}</h3>
                <div className="hotel-stars">{{h.stars}}</div>
                <div className="hotel-tags">{{h.tags.map(t=><span key={{t}} className="htag">{{t}}</span>)}}</div>
                <div className="hotel-bottom">
                  <div>
                    <div className="hotel-price">{{h.price}} <span>/night</span></div>
                    <div className="hotel-per-person">✓ {{h.perPerson}}/person (7 people)</div>
                  </div>
                  <button
                    className={{"book-btn"+(bookedHotel===h.id?" booked":"")}}
                    onClick={{()=>{{setBookedHotel(h.id);setModal({{type:"booked",name:h.name}}); }}}}
                  >
                    {{bookedHotel===h.id?"✓ Booked!":"Book Now"}}
                  </button>
                </div>
              </div>
            </div>
          ))}}
        </div>
        {{modal?.type==="booked" && (
          <div className="modal-overlay" onClick={{()=>setModal(null)}}>
            <div className="modal" onClick={{e=>e.stopPropagation()}}>
              <button className="modal-close" onClick={{()=>setModal(null)}}>×</button>
              <div style={{{{textAlign:"center",padding:"10px 0"}}}}>
                <div style={{{{fontSize:56,marginBottom:12}}}}>🎉</div>
                <h3>{{modal.name}} Booked!</h3>
                <p style={{{{color:"var(--muted)",margin:"12px 0 20px"}}}}>Cost split sent to all 7 members automatically.</p>
                <button className="btn-full" onClick={{()=>{{setModal(null);go("cost");}}}}>View Cost Split →</button>
              </div>
            </div>
          </div>
        )}}
      </div>
    );
  }}

  /* ── COST SPLIT ── */
  function CostSplit() {{
    return (
      <div className="screen pb">
        <div className="cost">
          <h2>💰 Cost Split</h2>
          <p style={{{{color:"var(--muted)",fontSize:14,marginBottom:20}}}}>Goa Trip · 7 friends · All expenses tracked</p>
          <div className="summary-cards">
            <div className="sum-card"><div className="val">₹86,200</div><div className="lbl">Total Spent</div></div>
            <div className="sum-card"><div className="val">₹12,314</div><div className="lbl">Per Person</div></div>
            <div className="sum-card"><div className="val" style={{{{color:"var(--red)"}}}}>₹29,456</div><div className="lbl">Still Pending</div></div>
          </div>
          {{EXPENSES.map(e=>(
            <div key={{e.id}} className="expense-row">
              <div className="exp-top">
                <div className="exp-name">{{e.name}}</div>
                <div className="exp-total">{{e.total}}</div>
              </div>
              <div className="exp-payers">
                {{e.payers.map(p=>(
                  <div key={{p.name}} className="payer">
                    <div className="payer-av" style={{{{background:p.color}}}}>{{p.name[0]}}</div>
                    <div><div className="pname">{{p.name}}</div><div className="pamount">{{p.amount}}</div></div>
                    <div className={{"pay-status "+(p.paid?"paid":"unpaid")}}>{{p.paid?"✓ Paid":"Pending"}}</div>
                  </div>
                ))}}
              </div>
            </div>
          ))}}
          <div style={{{{background:"var(--navy)",borderRadius:14,padding:"18px 20px",marginTop:8,display:"flex",justifyContent:"space-between",alignItems:"center",flexWrap:"wrap",gap:12}}}}>
            <div style={{{{color:"white"}}}}>
              <div style={{{{fontSize:13,opacity:0.8}}}}>Still to collect</div>
              <div style={{{{fontSize:24,fontWeight:800}}}}>₹29,456</div>
            </div>
            <button style={{{{background:"var(--orange)",color:"white",border:"none",padding:"12px 24px",borderRadius:12,fontWeight:700,cursor:"pointer",fontSize:14}}}}>
              📲 Send Reminders
            </button>
          </div>
        </div>
      </div>
    );
  }}

  const SCREENS = {{landing:Landing,auth:Auth,dashboard:Dashboard,create:CreateTrip,tracker:Tracker,places:Places,hotels:Hotels,cost:CostSplit}};
  const Screen = SCREENS[screen] || Dashboard;

  return (
    <div>
      <Nav/>
      <Screen/>
      <BottomNav/>
    </div>
  );
}}

ReactDOM.createRoot(document.getElementById("root")).render(<App/>);
</script>
</body>
</html>"""

out = "/sessions/funny-nice-pasteur/mnt/outputs/safarnama.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Written {len(html):,} chars to {out}")
