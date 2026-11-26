"""
Stylo Landing Page — Streamlit
Website promosi dan gateway menuju aplikasi mobile Stylo.

Jalankan:
    pip install -r requirements.txt
    streamlit run app.py

Typography:
    DM Serif Display -> heading, hero, harga, display text
    Manrope         -> body, cards, navigation, button
    Poppins         -> label, badge, micro text
"""

import base64
from pathlib import Path

import streamlit as st

# ================================================================
# CONFIGURATION
# ================================================================

MOBILE_APP_URL = "#download"

ASSETS = Path(__file__).parent / "images"

st.set_page_config(
    page_title="Stylo — A new look, a new you",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ================================================================
# CONTENT
# ================================================================

HAIRSTYLES = [
    ("Buzz Cut", "buzz_cut.jpe", "Oval · Kotak"),
    ("French Crop", "french_crop.jpe", "Oval · Bulat · Hati"),
    ("Caesar Cut", "caesar_cut.jpe", "Oval · Kotak · Lonjong"),
    ("Mullet", "mullet.jpe", "Oval · Hati · Lonjong"),
    ("Mohawk", "mohawk.jpe", "Oval · Bulat · Kotak"),
    ("Textured Cut", "textured_cut.jpe", "Semua bentuk wajah"),
]

FEATURES = [
    (
        "01",
        "AI hairstyle camera",
        "Visualisasikan gaya rambut langsung pada wajahmu menggunakan kamera "
        "atau foto dari perangkat. Temukan look baru sebelum memutuskan potong rambut.",
    ),
    (
        "02",
        "Face shape detection",
        "Kenali bentuk wajahmu dan temukan inspirasi hairstyle yang dapat "
        "menyesuaikan karakter wajahmu.",
    ),
    (
        "03",
        "Find your salon",
        "Temukan salon dan barber di sekitarmu, lihat layanan, harga, "
        "portofolio, dan hairstylist sebelum menentukan pilihan.",
    ),
    (
        "04",
        "Easy booking",
        "Pilih hairstylist, tanggal, dan waktu yang tersedia. "
        "Atur jadwal potong rambut dengan lebih praktis.",
    ),
    (
        "05",
        "Connect with your stylist",
        "Tanyakan detail layanan, diskusikan gaya rambut, dan konsultasikan "
        "keinginanmu dengan salon sebelum datang.",
    ),
    (
        "06",
        "Stylo AI",
        "Teman konsultasi rambutmu. Dapatkan inspirasi seputar hairstyle, "
        "bentuk wajah, perawatan, warna rambut, dan tips styling.",
    ),
]

STEPS = [
    ("1", "Discover your look", "Temukan inspirasi gaya rambut yang ingin kamu coba."),
    ("2", "Try it virtually", "Visualisasikan hairstyle pada wajahmu dengan AI Camera."),
    ("3", "Find your stylist", "Cari salon atau barber yang sesuai dengan gaya dan budget."),
    ("4", "Book & enjoy", "Atur jadwal, konsultasikan gaya, dan bersiap untuk look baru."),
]

MITRA = [
    "Dashboard booking, chat, dan pendapatan bulanan",
    "Booking masuk: konfirmasi atau tolak dengan sekali klik",
    "Profil, lokasi, dan jam buka salon",
    "Layanan dan harga yang bisa diubah kapan saja",
    "Hairstylist, keahlian, dan portofolio",
    "Chat langsung dengan pelanggan",
    "Promosikan salon melalui fitur iklan Stylo",
]

PLANS = [
    (
        "Gratis",
        "Rp0",
        "selamanya",
        "5 pesan per percakapan",
        "5.000 token per hari",
        False,
    ),
    (
        "Premium Mingguan",
        "Rp15.000",
        "/ 7 hari",
        "30 pesan per percakapan",
        "20.000 token per hari",
        False,
    ),
    (
        "Premium Bulanan",
        "Rp49.000",
        "/ 30 hari",
        "150 pesan per percakapan",
        "50.000 token per hari",
        True,
    ),
]

# ================================================================
# HELPERS
# ================================================================

def b64(path: Path) -> str:
    try:
        return base64.b64encode(path.read_bytes()).decode()
    except OSError:
        return ""


def html(block: str) -> None:
    """Render HTML in Streamlit while normalizing whitespace."""
    cleaned = "\n".join(
        line.strip() for line in block.splitlines() if line.strip()
    )
    st.markdown(cleaned, unsafe_allow_html=True)


# ================================================================
# STYLING
# ================================================================

html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700&display=swap');

:root{
  --yellow:#ffd84d;
  --yellow-hover:#ffe27a;
  --ink:#1e1e1e;
  --bg:#3a3a3a;
  --bar:#262626;
  --tile:#4a4a4a;
  --photo:#6e7378;
  --line:#444444;
  --muted:#c4c4c4;
  --soft:#e0e0e0;
  --radius:18px;
}

/* ---- STREAMLIT DEFAULTS ---- */
#MainMenu, footer, header[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stSidebar"],
[data-testid="collapsedControl"]{
  display:none !important;
}

html{
  scroll-behavior:smooth;
}

.stApp{
  background:var(--bg);
}

.block-container{
  padding:0 !important;
  max-width:100% !important;
}

[data-testid="stVerticalBlock"]{
  gap:0 !important;
}

/* ---- GLOBAL TYPOGRAPHY ---- */
.stylo, .stylo *{
  box-sizing:border-box;
  font-family:"Manrope",sans-serif;
}

.stylo{
  color:#fff;
  font-size:15px;
  line-height:1.75;
  letter-spacing:-.12px;
}

.stylo a{
  color:var(--yellow);
  text-decoration:none;
}

.stylo h1,
.stylo h2,
.stylo h3,
.stylo p{
  margin:0;
  padding:0;
  line-height:1.3;
}

.stylo h1,
.stylo h2,
.stylo h3{
  color:#fff;
  font-weight:600;
}

.stylo .hl{
  color:var(--yellow);
}

.stylo .muted{
  color:var(--muted);
}

.stylo .inner{
  max-width:1200px;
  margin:0 auto;
  padding:0 24px;
}

.stylo section{
  scroll-margin-top:80px;
}

/* ---- NAVIGATION ---- */
.stylo .topbar{
  position:fixed;
  top:0;
  left:0;
  right:0;
  z-index:999;
  background:var(--bar);
  border-bottom:1px solid rgba(255,255,255,.05);
}

.stylo .topbar .inner{
  height:70px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:24px;
}

.stylo .logo{
  font-family:"DM Serif Display",Georgia,serif !important;
  font-size:32px;
  font-weight:400;
  letter-spacing:-1px;
  line-height:1;
  color:#fff !important;
}

.stylo .nav{
  display:flex;
  gap:30px;
  align-items:center;
}

.stylo .nav a{
  color:#ededed;
  font-family:"Manrope",sans-serif;
  font-size:13px;
  font-weight:600;
  letter-spacing:.1px;
  padding:10px 0;
  transition:color .2s;
}

.stylo .nav a:hover{
  color:var(--yellow);
}

@media(max-width:899px){
  .stylo .nav{
    display:none;
  }
}

/* ---- BUTTONS ---- */
.stylo .btn{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:8px;
  min-height:46px;
  padding:0 25px;
  border-radius:999px;
  font-family:"Manrope",sans-serif;
  font-weight:700;
  font-size:14px;
  letter-spacing:-.2px;
  line-height:1.2;
  text-align:center;
  cursor:pointer;
  transition:background .2s,color .2s,transform .2s;
}

.stylo .btn:hover{
  transform:translateY(-2px);
}

.stylo .btn-yellow{
  background:var(--yellow);
  color:var(--ink) !important;
}

.stylo .btn-yellow:hover{
  background:var(--yellow-hover);
}

.stylo .btn-white{
  background:#fff;
  color:var(--ink) !important;
}

.stylo .btn-white:hover{
  background:#f0f0f0;
}

.stylo .btn-ink{
  background:var(--ink);
  color:var(--yellow) !important;
}

.stylo .btn-ink:hover{
  background:#000;
}

.stylo .btn-outline{
  background:transparent;
  color:#fff !important;
  box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.75);
}

.stylo .btn-outline:hover{
  color:var(--yellow) !important;
  box-shadow:inset 0 0 0 1.5px var(--yellow);
}

.stylo .btn-lg{
  min-height:54px;
  font-size:15px;
  padding:0 30px;
}

.stylo .btn-sm{
  min-height:38px;
  padding:0 20px;
  font-size:13px;
}

.stylo .row{
  display:flex;
  gap:12px;
  flex-wrap:wrap;
  align-items:center;
}

/* ---- EYEBROW ---- */
.stylo .eyebrow{
  display:inline-flex;
  align-self:flex-start;
  min-height:30px;
  align-items:center;
  padding:0 14px;
  border-radius:999px;
  font-family:"Poppins",sans-serif;
  font-size:10px;
  font-weight:600;
  letter-spacing:1px;
  text-transform:uppercase;
  color:var(--yellow);
  box-shadow:inset 0 0 0 1.2px var(--yellow);
}

/* ---- HERO ---- */
.stylo .hero{
  padding:142px 0 90px;
}

.stylo .hero .inner{
  display:flex;
  flex-wrap:wrap;
  gap:64px;
  align-items:center;
}

.stylo .hero .text{
  flex:1 1 440px;
  display:flex;
  flex-direction:column;
  gap:24px;
}

.stylo .hero h1{
  font-family:"DM Serif Display",serif !important;
  font-size:clamp(48px,6.5vw,78px);
  font-weight:400;
  line-height:1.05;
  letter-spacing:-2px;
}

.stylo .hero h1 .hl{
  font-family:"DM Serif Display",serif !important;
  font-style:italic;
  font-weight:400;
  color:var(--yellow);
}

.stylo .hero p.lead{
  font-family:"Manrope",sans-serif;
  font-size:16px;
  font-weight:400;
  line-height:1.85;
  letter-spacing:0;
  color:#d6d6d6;
  max-width:510px;
}

.stylo .hero-stats{
  display:flex;
  gap:32px;
  flex-wrap:wrap;
  margin-top:8px;
}

.stylo .hero-stats b{
  display:block;
  font-family:"DM Serif Display",serif;
  font-size:30px;
  font-weight:400;
  letter-spacing:-.6px;
  color:var(--yellow);
  line-height:1.2;
}

.stylo .hero-stats span{
  font-family:"Poppins",sans-serif;
  font-size:11px;
  font-weight:400;
  color:var(--muted);
  line-height:1.6;
}

.stylo .cam{
  border-radius:26px;
  background:var(--photo);
  position:relative;
  overflow:hidden;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:16px;
}

.stylo .cam .title{
  position:absolute;
  top:20px;
  left:0;
  right:0;
  text-align:center;
  font-family:"DM Serif Display",serif;
  font-size:26px;
  font-weight:400;
  letter-spacing:.2px;
  text-shadow:0 1px 6px rgba(0,0,0,.5);
}
.stylo .capsule{
  width:175px;
  height:245px;
  border:2px dashed rgba(255,255,255,.85);
  border-radius:999px;
  display:flex;
  align-items:center;
  justify-content:center;
  overflow:hidden;
}

.stylo .capsule svg{
  width:70px;
  height:70px;
  color:#e4e4e4;
}

.stylo .cam .hint{
  font-family:"Manrope",sans-serif;
  font-size:13px;
  font-weight:500;
  letter-spacing:.1px;
  text-shadow:0 1px 6px rgba(0,0,0,.6);
}

.stylo .cam .shutter{
  position:absolute;
  bottom:40px;
  width:56px;
  height:56px;
  border-radius:999px;
  border:2.5px solid var(--yellow);
  display:flex;
  align-items:center;
  justify-content:center;
}

.stylo .cam .shutter i{
  width:36px;
  height:36px;
  border-radius:999px;
  background:var(--yellow);
  display:block;
}

.stylo .cam .chip-float{
  position:absolute;
  top:60px;
  right:16px;
  background:var(--bar);
  border-radius:999px;
  padding:7px 14px;
  font-family:"Poppins",sans-serif;
  font-size:11px;
  font-weight:500;
}

.stylo .cam .capsule img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
  border-radius: inherit;
  display: block;
}

.stylo .cam .chip-float b{
  color:var(--yellow);
  font-weight:600;
}

.stylo .scan-photo {
    position: relative;
    width: auto;
    height: 500px;
    overflow: hidden;
    border-radius: 12px;
}

.stylo .scan-photo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    display: block;
}

/* Efek gelap di luar area wajah */
.stylo .scan-shade {
    position: absolute;
    inset: 0;
    background: radial-gradient(
        ellipse 37% 32% at 50% 34%,
        transparent 98%,
        rgba(0, 0, 0, 0.35) 100%
    );
    pointer-events: none;
}

/* Frame oval untuk scanning wajah */
.stylo .face-frame {
    position: absolute;
    width: 74%;
    height: 64%;
    top: 2%;
    left: 13%;
    border: 2px dashed rgba(255, 255, 255, 0.9);
    border-radius: 50%;
    box-sizing: border-box;
    pointer-events: none;
}

/* ---- SECTION HEADINGS ---- */
.stylo .sec{
  padding:80px 0;
}

.stylo .sec-head{
  margin-bottom:36px;
  max-width:700px;
}

.stylo .sec-head h2,
.stylo .steps h2,
.stylo .mitra h2,
.stylo .cta h2{
  font-family:"DM Serif Display",serif !important;
  font-weight:400;
  font-size:clamp(34px,4.3vw,48px);
  line-height:1.16;
  letter-spacing:-1px;
}

.stylo .sec-head p{
  margin-top:14px;
  font-family:"Manrope",sans-serif;
  font-size:15px;
  font-weight:400;
  line-height:1.8;
  max-width:580px;
  color:#d6d6d6;
}

/* ---- FEATURES ---- */
.stylo .grid-3{
  display:grid;
  gap:18px;
  grid-template-columns:repeat(auto-fill,minmax(300px,1fr));
}

.stylo .card{
  background:var(--bar);
  border-radius:18px;
  padding:26px 24px 28px;
  display:flex;
  flex-direction:column;
  gap:12px;
  transition:transform .2s,box-shadow .2s;
}

.stylo .card:hover{
  transform:translateY(-4px);
  box-shadow:inset 0 0 0 1px var(--yellow);
}

.stylo .card .no{
  font-family:"DM Serif Display",serif;
  font-size:28px;
  font-weight:400;
  color:var(--yellow);
  letter-spacing:-1px;
}

.stylo .card h3{
  font-family:"Manrope",sans-serif;
  font-size:18px;
  font-weight:700;
  letter-spacing:-.5px;
}

.stylo .card p{
  font-family:"Manrope",sans-serif;
  font-size:14px;
  font-weight:400;
  line-height:1.8;
  color:#cfcfcf;
}

/* ---- HAIRSTYLE GALLERY ---- */
.stylo .style-grid{
  display:grid;
  gap:14px;
  grid-template-columns:repeat(2,minmax(0,1fr));
}

@media(min-width:700px){
  .stylo .style-grid{
    grid-template-columns:repeat(3,minmax(0,1fr));
  }
}

@media(min-width:1000px){
  .stylo .style-grid{
    grid-template-columns:repeat(6,minmax(0,1fr));
    gap:16px;
  }
}

.stylo .style-card{
  display:flex;
  flex-direction:column;
  background:var(--bar);
  border-radius:14px;
  overflow:hidden;
  transition:transform .2s,outline .2s;
}

.stylo .style-card:hover{
  outline:2px solid var(--yellow);
  transform:translateY(-3px);
}

.stylo .style-card .name{
  padding:12px 8px 10px;
  text-align:center;
  font-family:"Manrope",sans-serif;
  font-size:14px;
  font-weight:700;
  letter-spacing:-.3px;
}
.stylo .style-card .pic{
  height:200px;
  background:var(--photo);
  display:flex;
  align-items:flex-start;
  justify-content:center;
  overflow:hidden;
}

.stylo .style-card .pic img{
  width:100%;
  height:100%;
  object-fit:cover;
  object-position:top;
  display:block;
}

.stylo .style-card .fit{
  padding:10px 8px;
  text-align:center;
  font-family:"Poppins",sans-serif;
  font-size:10px;
  font-weight:400;
  line-height:1.6;
  color:#bdbdbd;
}

.stylo .style-card .try{
  height:36px;
  background:var(--yellow);
  color:var(--ink);
  display:flex;
  align-items:center;
  justify-content:center;
  font-family:"Manrope",sans-serif;
  font-size:11px;
  font-weight:800;
  letter-spacing:.6px;
  text-transform:uppercase;
  transition:background .2s;
}

.stylo .style-card:hover .try{
  background:var(--yellow-hover);
}

/* ---- HOW IT WORKS ---- */
.stylo .steps{
  background:var(--yellow);
  color:var(--ink);
}

.stylo .steps .inner{
  padding:64px 24px;
}

.stylo .steps h2{
  color:var(--ink);
  font-size:42px;
}

.stylo .steps ol{
  list-style:none;
  margin:30px 0 0;
  padding:0;
  display:grid;
  gap:26px;
  grid-template-columns:repeat(auto-fill,minmax(220px,1fr));
}

.stylo .steps .num{
  width:48px;
  height:48px;
  border-radius:50%;
  background:var(--ink);
  color:var(--yellow);
  font-family:"DM Serif Display",serif;
  font-size:20px;
  font-weight:400;
  display:inline-flex;
  align-items:center;
  justify-content:center;
}

.stylo .steps strong{
  display:block;
  margin-top:14px;
  font-family:"Manrope",sans-serif;
  font-size:18px;
  font-weight:800;
  letter-spacing:-.4px;
}

.stylo .steps li span.d{
  display:block;
  font-family:"Manrope",sans-serif;
  font-size:14px;
  font-weight:400;
  line-height:1.8;
  margin-top:5px;
}

/* ---- SALON PARTNERS ---- */
.stylo .mitra{
  display:flex;
  flex-wrap:wrap;
  gap:40px;
  align-items:stretch;
}

.stylo .mitra .left{
  flex:1 1 420px;
  display:flex;
  flex-direction:column;
  gap:18px;
}

.stylo .mitra ul{
  list-style:none;
  margin:4px 0 10px;
  padding:0;
  display:flex;
  flex-direction:column;
  gap:12px;
}

.stylo .mitra li{
  display:flex;
  gap:12px;
  align-items:flex-start;
  font-family:"Manrope",sans-serif;
  font-size:14px;
  font-weight:400;
  line-height:1.7;
  color:var(--soft);
}

.stylo .mitra li::before{
  content:"";
  flex:0 0 8px;
  height:8px;
  border-radius:999px;
  background:var(--yellow);
  margin-top:9px;
}

.stylo .money{
  flex:1 1 340px;
  background:var(--yellow);
  color:var(--ink);
  border-radius:var(--radius);
  padding:30px;
  display:flex;
  flex-direction:column;
  gap:16px;
}

.stylo .money h3{
  color:var(--ink);
  font-family:"Manrope",sans-serif;
  font-size:21px;
  font-weight:800;
  letter-spacing:-.5px;
}

.stylo .money p{
  font-family:"Manrope",sans-serif;
  font-size:14px;
  font-weight:400;
  line-height:1.8;
}

.stylo .money .line{
  display:flex;
  justify-content:space-between;
  gap:12px;
  padding:12px 0;
  border-bottom:1px solid rgba(30,30,30,.2);
  font-size:14px;
}

.stylo .money .line:last-of-type{
  border-bottom:0;
}

.stylo .money .line b{
  font-size:15px;
  font-weight:800;
}

.stylo .money .big{
  background:var(--ink);
  color:var(--yellow);
  border-radius:12px;
  padding:14px 16px;
  display:flex;
  justify-content:space-between;
  gap:12px;
  font-weight:800;
}

.stylo .money small{
  font-family:"Poppins",sans-serif;
  font-size:10px;
  font-weight:400;
  line-height:1.7;
  opacity:.8;
}

/* ---- PRICING ---- */
.stylo .plans{
  display:grid;
  gap:18px;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
}

.stylo .plan{
  background:var(--bar);
  border-radius:var(--radius);
  padding:26px;
  display:flex;
  flex-direction:column;
  gap:12px;
  transition:transform .2s;
}

.stylo .plan:hover{
  transform:translateY(-3px);
}

.stylo .plan.pop{
  box-shadow:inset 0 0 0 1.5px var(--yellow);
}

.stylo .plan h3{
  font-family:"Manrope",sans-serif;
  font-size:17px;
  font-weight:700;
  letter-spacing:-.4px;
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:8px;
}

.stylo .badge{
  display:inline-flex;
  align-items:center;
  height:26px;
  padding:0 10px;
  border-radius:999px;
  font-family:"Poppins",sans-serif;
  font-size:10px;
  font-weight:600;
  letter-spacing:.3px;
  background:var(--yellow);
  color:var(--ink);
}

.stylo .plan .price{
  font-family:"DM Serif Display",serif;
  font-size:38px;
  font-weight:400;
  letter-spacing:-1px;
  line-height:1.2;
  color:var(--yellow);
}

.stylo .plan .price span{
  font-family:"Manrope",sans-serif;
  font-size:12px;
  font-weight:500;
  letter-spacing:0;
  color:#bdbdbd;
}

.stylo .plan p:not(.price){
  font-family:"Manrope",sans-serif;
  font-size:14px;
  font-weight:400;
  line-height:1.75;
  color:#dedede;
}

.stylo .note{
  font-family:"Poppins",sans-serif;
  font-size:11px;
  font-weight:400;
  line-height:1.7;
  color:var(--muted);
  margin-top:18px;
}

/* ---- APP CTA ---- */
.stylo .cta{
  background:var(--bar);
  text-align:center;
}

.stylo .cta .inner{
  padding:78px 24px;
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:22px;
}

.stylo .cta h2{
  font-size:clamp(36px,4.8vw,52px);
}

.stylo .cta p{
  font-family:"Manrope",sans-serif;
  font-size:15px;
  font-weight:400;
  line-height:1.8;
  color:var(--soft);
  max-width:540px;
}

/* ---- FOOTER ---- */
.stylo .footer{
  background:#1b1b1b;
  color:var(--muted);
  font-size:12px;
}

.stylo .footer .inner{
  padding:28px 24px;
  display:flex;
  flex-wrap:wrap;
  gap:10px 24px;
  align-items:center;
  justify-content:space-between;
}

.stylo .footer .logo{
  font-size:26px;
}

/* ---- RESPONSIVE ---- */
@media(max-width:700px){
  .stylo .inner{
    padding:0 20px;
  }

  .stylo .hero{
    padding:112px 0 58px;
  }

  .stylo .hero .inner{
    gap:36px;
  }

  .stylo .hero h1{
    font-size:clamp(44px,12vw,62px);
    letter-spacing:-1.5px;
  }

  .stylo .hero p.lead{
    font-size:14px;
  }

  .stylo .hero-stats{
    gap:22px;
  }

  .stylo .hero-stats b{
    font-size:26px;
  }

  .stylo .cam{
    min-height:380px;
  }

  .stylo .sec{
    padding:58px 0;
  }

  .stylo .sec-head h2,
  .stylo .steps h2,
  .stylo .mitra h2,
  .stylo .cta h2{
    font-size:36px;
    letter-spacing:-.7px;
  }

  .stylo .grid-3{
    grid-template-columns:1fr;
  }

  .stylo .steps .inner{
    padding:48px 20px;
  }

  .stylo .steps ol{
    grid-template-columns:1fr 1fr;
    gap:24px 18px;
  }

  .stylo .money{
    padding:22px;
  }

  .stylo .plan{
    padding:22px;
  }

  .stylo .cta .inner{
    padding:58px 20px;
  }

  .stylo .btn-lg{
    min-height:48px;
    padding:0 22px;
    font-size:14px;
  }
}

@media(max-width:420px){
  .stylo .steps ol{
    grid-template-columns:1fr;
  }

  .stylo .hero-stats{
    gap:18px;
  }

  .stylo .hero-stats span{
    font-size:10px;
  }
}
</style>
""")

# ================================================================
# SVG ICON
# ================================================================

ICON_PERSON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/>'
    '<path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/></svg>'
)

header_image_data = b64(ASSETS / "header.jpe")

header_pic = (
    f'<img src="data:image/jpeg;base64,{header_image_data}" alt="French Crop Hairstyle">'
    if header_image_data
    else ICON_PERSON.replace("<svg", '<svg width="70" height="70"')
)

# ================================================================
# HEADER + HERO
# ================================================================

html(f"""
<div class="stylo">
<header class="topbar">
  <div class="inner">
    <a class="logo" href="#top" target="_self">stylo</a>

    <nav class="nav" aria-label="Navigasi">
      <a href="#fitur" target="_self">Features</a>
      <a href="#gaya" target="_self">Hairstyles</a>
      <a href="#cara-kerja" target="_self">How It Works</a>
      <a href="#mitra" target="_self">For Salons</a>
      <a href="#paket" target="_self">Plans</a>
    </nav>
  </div>
</header>

<section class="hero" id="top">
  <div class="inner">
    <div class="text">
      <span class="eyebrow">Teman Menemukan Gaya Rambut Terbaikmu</span>

      <h1>
        A new look,<br>
        <span class="hl">a new you.</span>
      </h1>

      <p class="lead">
        Temukan gaya rambut yang sesuai dengan bentuk wajahmu, coba secara virtual, dan temukan salon atau barber terbaik untuk look barumu.
      </p>

      <div class="row">
        <a class="btn btn-yellow btn-lg" href="{MOBILE_APP_URL}" target="_blank">
          Explore Stylo
        </a>
        <a class="btn btn-outline btn-lg" href="#fitur" target="_self">
          Discover Stylo
        </a>
      </div>

      <div class="hero-stats">
        <div>
          <b>100+</b>
          <span>Gaya rambut</span>
        </div>
        <div>
          <b>Rp45K</b>
          <span>Potong rambut mulai dari</span>
        </div>
      </div>
    </div>

    <div class="cam" aria-hidden="true">
      <p class="title">French Crop</p>
      <span class="chip-float">Face shape: <b>Oval</b></span>
      <div class="scan-photo">
          {header_pic}
          <div class="scan-shade"></div>
          <div class="face-frame"></div>
      </div>
      <span class="shutter"><i></i></span>
    </div>
  </div>
</section>
</div>
""")

# ================================================================
# FEATURES
# ================================================================

cards = "".join(
    f'<article class="card">'
    f'<span class="no">{n}</span>'
    f'<h3>{t}</h3>'
    f'<p>{d}</p>'
    f'</article>'
    for n, t, d in FEATURES
)

html(f"""
<div class="stylo">
<section class="sec" id="fitur">
  <div class="inner">
    <div class="sec-head">
      <h2>
        Dari menemukan gaya Anda hingga
        <span class="hl"> kunjungan salon berikutnya.</span>
      </h2>
      <p>
        Semua yang Anda butuhkan untuk potongan rambut berikutnya, semua dalam satu tempat.
        Temukan gaya, coba secara virtual, cari seorang ahli, dan buat janji temu di salon atau barber terbaik di dekat Anda.
      </p>
    </div>

    <div class="grid-3">{cards}</div>
  </div>
</section>
</div>
""")

# ================================================================
# HAIRSTYLE GALLERY
# ================================================================

style_cards = ""

for name, file, fit in HAIRSTYLES:
    image_path = ASSETS / file
    if not image_path.exists():
        # Nama file Buzz Cut pada folder images menggunakan "buzzcut.jpe".
        if file == "buzz_cut.jpe":
            image_path = ASSETS / "buzzcut.jpe"

    data = b64(image_path)
    mime_type = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"

    pic = (
        f'<img src="data:{mime_type};base64,{data}" alt="{name}">'
        if data
        else ICON_PERSON.replace("<svg", '<svg width="44" height="44"')
    )

    style_cards += (
        f'<a class="style-card" href="{MOBILE_APP_URL}" target="_blank">'
        f'<span class="name">{name}</span>'
        f'<span class="pic">{pic}</span>'
        f'<span class="fit">Best for: {fit}</span>'
        f'<span class="try">Explore style</span>'
        f'</a>'
    )

html(f"""
<div class="stylo">
<section class="sec" id="gaya" style="padding-top:8px">
  <div class="inner">
    <div class="sec-head">
      <h2>
        Find your style.
        <span class="hl">Own your look.</span>
      </h2>
      <p>
        Dari gaya rambut klasik hingga tren terbaru, temukan inspirasi untuk potongan rambut berikutnya. Jelajahi berbagai gaya, coba secara virtual, dan temukan salon atau barber terbaik untuk mewujudkan look barumu.
      </p>
    </div>

    <div class="style-grid">{style_cards}</div>
  </div>
</section>
</div>
""")

# ================================================================
# HOW IT WORKS
# ================================================================

steps = "".join(
    f'<li>'
    f'<span class="num">{n}</span>'
    f'<strong>{t}</strong>'
    f'<span class="d">{d}</span>'
    f'</li>'
    for n, t, d in STEPS
)

html(f"""
<div class="stylo">
<section class="steps" id="cara-kerja">
  <div class="inner">
    <h2>Good hair days, made easy.</h2>
    <ol>{steps}</ol>
  </div>
</section>
</div>
""")

# ================================================================
# FOR SALONS / PARTNERS
# ================================================================

mitra_items = "".join(f"<li>{m}</li>" for m in MITRA)

html(f"""
<div class="stylo">
<section class="sec" id="mitra">
  <div class="inner mitra">

    <div class="left">
      <span class="eyebrow">For salons &amp; barbers</span>

      <h2>
        More than a salon.
        <span class="hl">Be part of Stylo.</span>
      </h2>

      <p class="muted">
        Bergabunglah dengan jaringan salon dan barber Stylo untuk menjangkau lebih banyak pelanggan, meningkatkan visibilitas, dan memanfaatkan teknologi kami untuk pengalaman pelanggan yang lebih baik.
      </p>

      <ul>{mitra_items}</ul>

      <div class="row">
        <a class="btn btn-yellow btn-lg" href="{MOBILE_APP_URL}" target="_blank">
          Discover Stylo for partners
        </a>
      </div>
    </div>

    <div class="money">
      <h3>A partnership that makes sense</h3>

      <p>
        Stylo menawarkan kemitraan yang saling menguntungkan bagi salon dan barber. Dengan komisi 15% dari setiap transaksi, salon tetap menerima 85% dari nilai transaksi, memastikan keuntungan yang adil dan berkelanjutan bagi semua pihak.
      </p>

      <div>
        <div class="line">
          <span>Transaction value</span>
          <b>Rp150.000</b>
        </div>

        <div class="line">
          <span>Stylo commission 15%</span>
          <b>Rp22.500</b>
        </div>
      </div>

      <div class="big">
        <span>Salon receives</span>
        <span>Rp127.500</span>
      </div>

      <small>Illustrative calculation. Commission rates may change.</small>
    </div>

  </div>
</section>
</div>
""")

# ================================================================
# PLANS
# ================================================================

plan_cards = ""

for name, price, per, chat, ai, pop in PLANS:
    badge = '<span class="badge">Popular</span>' if pop else ""

    plan_cards += (
        f'<article class="plan{" pop" if pop else ""}">'
        f'<h3>{name}{badge}</h3>'
        f'<p class="price">{price} <span>{per}</span></p>'
        f'<p>Salon chat: {chat}</p>'
        f'<p>Stylo AI: {ai}</p>'
        f'</article>'
    )

html(f"""
<div class="stylo">
<section class="sec" id="paket" style="padding-top:8px">
  <div class="inner">
    <div class="sec-head">
      <h2>
        Start with free.
        <span class="hl">Upgrade when you're ready.</span>
      </h2>
      <p>
        Coba Stylo secara gratis dan nikmati fitur-fitur dasar. Saat Anda siap untuk lebih banyak fitur, tingkatkan ke paket berbayar untuk pengalaman yang lebih lengkap.
      </p>
    </div>

    <div class="plans">{plan_cards}</div>

    <p class="note">
      Harga dan paket dapat berubah sewaktu-waktu. Silakan periksa aplikasi untuk informasi terbaru.
    </p>
  </div>
</section>
</div>
""")

# ================================================================
# FINAL CTA + FOOTER
# ================================================================

html(f"""
<div class="stylo">
<section class="cta" id="download">
  <div class="inner">
    <span class="eyebrow">Your next look awaits</span>

    <h2>
      Ready for a
      <span class="hl">new you?</span>
    </h2>

    <p>
      Gaya rambut baru menunggu Anda. Temukan, coba, dan wujudkan look barumu dengan Stylo.
    </p>

    <div class="row" style="justify-content:center">
      <a class="btn btn-yellow btn-lg" href="{MOBILE_APP_URL}" target="_blank">
        Explore Stylo
      </a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="inner">
    <span class="logo">stylo</span>
    <span>
      Stylo — Your hairstyle companion ·
      Technopreneurship Project, Universitas Tarumanagara
    </span>
  </div>
</footer>
</div>
""")