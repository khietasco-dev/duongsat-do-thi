# -*- coding: utf-8 -*-
"""Dung website Duong sat do thi — hai tang giao dien.

  Tang NGOAI : trang dich (index)          -> lop .ngoai
  Tang TRONG : cac trang cong cu           -> lop .trong

Chay: python ds_build.py
"""
import io, os, json, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

KHO = r'C:\Users\Public\BO NAO\duongsat-do-thi'
GOC = 'https://duongsatdothi.vn'
JSON_VB = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vb_duongsat.json')

# ---------------------------------------------------------------- dieu huong
NAV = [
    ('van-ban',    'Cập nhật văn bản'),
    ('quy-trinh',  'Quy trình dự án'),
    ('kinh-nghiem','Kinh nghiệm QLDA'),
    ('vuong-mac',  'Vướng mắc'),
    ('tu-van',     'Tư vấn'),
    ('lien-he',    'Liên hệ'),
]

CSS = r"""
:root{
  --nen:#FFFFFF; --the:#FFFFFF; --nen2:#F4F7FC; --nen3:#EEF2F8;
  --muc:#184088;            /* navy ASCO - mau thuong hieu */
  --muc2:#12305F;           /* navy sau */
  --muc3:#4A6EB0;           /* navy sang - vien, hover */
  --nhan:#B8862A;           /* vang dong ASCO */
  --nhan2:#8E6817;
  --ngoc:#0F6B54;           /* XANH NGOC - mau ho tro moi */
  --ngoc-nen:#E4F2ED;
  --do:#A82420; --do-nen:#FBEAE8;
  --hoacuc:#B8862A; --hoacuc-nen:#FBF3E2;
  --chu:#0E1729; --chu2:#5D687C;
  --vien:#E0E6F0; --vien-nhat:#EEF2F8;
  --bong:0 1px 2px rgba(14,23,41,.05),0 8px 26px rgba(14,23,41,.07);
  --r:13px;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --nen:#0D2044; --the:#13294F; --nen2:#0A1B3B; --nen3:#102A56;
  --muc:#8FB2EE; --muc2:#13294F; --muc3:#5478BE;
  --nhan:#E0B458; --nhan2:#F2CE83;
  --ngoc:#4FC0A2; --ngoc-nen:#0E3A30;
  --do:#F0857E; --do-nen:#3A1A18;
  --hoacuc:#E0B458; --hoacuc-nen:#2E2415;
  --chu:#EEF3FB; --chu2:#8DA0C0;
  --vien:#22406E; --vien-nhat:#1A3260;
  --bong:0 1px 2px rgba(0,0,0,.35),0 10px 30px rgba(0,0,0,.45);
}}
:root[data-theme="dark"]{
  --nen:#0D2044; --the:#13294F; --nen2:#0A1B3B; --nen3:#102A56;
  --muc:#8FB2EE; --muc2:#13294F; --muc3:#5478BE;
  --nhan:#E0B458; --nhan2:#F2CE83;
  --ngoc:#4FC0A2; --ngoc-nen:#0E3A30;
  --do:#F0857E; --do-nen:#3A1A18;
  --hoacuc:#E0B458; --hoacuc-nen:#2E2415;
  --chu:#EEF3FB; --chu2:#8DA0C0;
  --vien:#22406E; --vien-nhat:#1A3260;
  --bong:0 1px 2px rgba(0,0,0,.35),0 10px 30px rgba(0,0,0,.45);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--nen);color:var(--chu);
  font-family:"Segoe UI",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
  font-size:16.6px;line-height:1.7;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
.hep{max-width:900px}
h1,h2,h3{font-family:'Times New Roman',Times,'Nimbus Roman',serif;letter-spacing:-.021em;line-height:1.22;margin:0}
h1{font-size:clamp(28px,4.1vw,45px)}
h2{font-size:clamp(22px,2.9vw,31px);color:var(--muc)}
h3{font-size:18.5px;color:var(--muc)}
p{margin:13px 0}
a{color:var(--muc)}
.small{font-size:14.3px;color:var(--chu2)}

/* ---------- THANH DAU (dung chung 2 tang) ---------- */
header.top{position:sticky;top:0;z-index:60;background:var(--nen);border-bottom:1px solid var(--vien)}
.top-in{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:11px 22px}
.hieu{display:flex;align-items:center;gap:10px;text-decoration:none}
.hieu svg{width:34px;height:34px;flex:0 0 auto}
.hieu b{font-family:'Times New Roman',Times,'Nimbus Roman',serif;font-size:17.6px;color:var(--muc);display:block;line-height:1.2}
.hieu i{font-style:normal;font-size:10.8px;font-weight:700;color:var(--chu2);letter-spacing:.1em;text-transform:uppercase}
.top-nav{display:flex;align-items:center;gap:16px}
.top-nav a{font-size:14.6px;font-weight:600;color:var(--chu);text-decoration:none;white-space:nowrap}
.top-nav a:hover,.top-nav a[aria-current]{color:var(--muc);text-decoration:underline;text-underline-offset:5px}
.nut-lh{background:var(--muc);color:#fff!important;padding:8px 16px;border-radius:999px;font-weight:700}
:root[data-theme="dark"] .nut-lh{color:#0D2044!important}
.menu-nut{display:none;background:none;border:1px solid var(--vien);border-radius:9px;padding:7px 11px;
  font-size:15px;font-family:inherit;color:var(--chu);cursor:pointer}
@media(max-width:1160px){
  .top-nav{position:absolute;top:100%;left:0;right:0;background:var(--nen);border-bottom:1px solid var(--vien);
    flex-direction:column;align-items:stretch;gap:0;padding:8px 22px 16px;display:none}
  .top-nav[data-mo]{display:flex}
  .top-nav a{padding:10px 0;border-bottom:1px solid var(--vien)}
  .top-nav .nut-lh{margin-top:10px;text-align:center;border-bottom:0}
  .menu-nut{display:block}
  header.top{position:relative}
}

/* ================= TANG NGOAI — trang dich ================= */
.ngoai .hero{position:relative;overflow:hidden;color:#EDF2FA;padding:clamp(52px,7vw,104px) 0;
  background:radial-gradient(820px 440px at 84% -20%,rgba(184,134,42,.22),transparent 60%),
             linear-gradient(158deg,#1E4C9E 0%,#184088 48%,#0C2148 100%)}
.ngoai .hero .wrap{position:relative;z-index:2}
.ngoai .hero h1{color:#fff;max-width:19ch}
.ngoai .hero .lede{color:rgba(237,242,250,.9);max-width:62ch;font-size:clamp(16.6px,1.9vw,19px);margin-top:17px}
.nhan-pill{display:inline-block;font-size:12.2px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;
  color:var(--nhan);border:1px solid rgba(184,134,42,.48);padding:6px 14px;border-radius:999px;margin-bottom:19px}
.hero-nut{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.n1,.n2{padding:13px 26px;border-radius:10px;font-weight:700;font-size:16px;text-decoration:none;display:inline-block}
.n1{background:var(--nhan);color:#231B00}
.n1:hover{background:#E4B451}
.n2{border:1.5px solid rgba(237,242,250,.4);color:#EDF2FA}
.n2:hover{border-color:var(--nhan);color:var(--nhan)}
.hero-so{display:flex;flex-wrap:wrap;gap:30px;margin-top:38px;padding-top:24px;border-top:1px solid rgba(237,242,250,.16)}
.hero-so div b{display:block;font-family:'Times New Roman',Times,'Nimbus Roman',serif;font-size:26px;color:var(--nhan);line-height:1.2}
.hero-so div span{font-size:13.4px;color:rgba(237,242,250,.72)}
/* duong ray trang tri */
.ray{position:absolute;left:0;right:0;bottom:0;height:76px;opacity:.5;z-index:1}

/* ================= TANG TRONG — trang cong cu ================= */
.trong .banner{background:var(--muc);color:#EDF2FA;padding:clamp(26px,3.4vw,44px) 0}
:root[data-theme="dark"] .trong .banner{background:var(--muc2);border-bottom:1px solid var(--vien)}
.trong .banner h1{color:#fff;font-size:clamp(25px,3.4vw,37px)}
.trong .banner p{color:rgba(237,242,250,.86);max-width:66ch;margin:11px 0 0;font-size:16.2px}
.duong{font-size:13.4px;color:rgba(237,242,250,.66);margin-bottom:11px}
.duong a{color:rgba(237,242,250,.86)}
.trong .than{padding:clamp(30px,3.8vw,52px) 0}

section{padding:clamp(40px,5vw,70px) 0;border-bottom:1px solid var(--vien)}
section.nen2{background:var(--nen2)}
.dau{margin-bottom:28px;max-width:74ch}
.dau .mac{font-size:12.2px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--nhan2);margin-bottom:8px}
.luoi{display:grid;gap:18px}
.g2{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(245px,1fr))}
.the{background:var(--the);border:1px solid var(--vien);border-radius:var(--r);padding:23px;box-shadow:var(--bong)}
.the h3{margin-bottom:7px}
.the p{margin:0;font-size:15.2px;color:var(--chu2)}
.the.lienket{text-decoration:none;color:inherit;display:block;transition:border-color .15s}
.the.lienket:hover{border-color:var(--muc3)}
.the .di{margin-top:13px;font-size:14.4px;font-weight:700;color:var(--nhan2)}
.ico{width:38px;height:38px;border-radius:10px;background:var(--muc);display:grid;place-items:center;margin-bottom:13px}
.ico svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
:root[data-theme="dark"] .ico svg{stroke:#0D2044}

/* ---------- BANG ---------- */
.bang-boc{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:16px 0;border:1px solid var(--vien);border-radius:var(--r)}
table{border-collapse:collapse;width:100%;min-width:620px;background:var(--the)}
th,td{padding:11px 14px;text-align:left;border-bottom:1px solid var(--vien);font-size:14.9px;vertical-align:top}
th{background:var(--nen2);font-weight:800;color:var(--muc);font-size:13.4px;position:sticky;top:0}
tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--nen2)}
.mã{font-family:Consolas,"Courier New",monospace;font-size:13.6px;color:var(--muc);font-weight:700;white-space:nowrap}

/* ---------- CONG CU LOC ---------- */
.loc{background:var(--the);border:1px solid var(--vien);border-radius:var(--r);padding:18px;margin-bottom:18px;box-shadow:var(--bong)}
.loc-hang{display:flex;flex-wrap:wrap;gap:11px;align-items:flex-end}
.loc-o{flex:1 1 190px;min-width:0}
.loc-o label{display:block;font-size:12.6px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--chu2);margin-bottom:5px}
.loc-o input,.loc-o select{width:100%;padding:9px 12px;border:1px solid var(--vien);border-radius:9px;
  font-size:15px;font-family:inherit;background:var(--nen);color:var(--chu)}
.loc-dem{margin-top:11px;font-size:14.2px;color:var(--chu2)}
.loc-dem b{color:var(--muc)}
.the-loc{display:inline-block;font-size:12.4px;font-weight:700;padding:2px 9px;border-radius:999px;white-space:nowrap}
.tl-luat{background:var(--ngoc-nen);color:var(--ngoc)}
.tl-nd{background:var(--hoacuc-nen);color:var(--nhan2)}
.tl-tt{background:var(--nen3);color:var(--muc)}
.tl-khac{background:var(--vien-nhat);color:var(--chu2)}
.dinh{font-size:12.2px;color:var(--chu2);white-space:nowrap}

/* ---------- MOC / QUY TRINH ---------- */
.gd{counter-reset:g;display:grid;gap:14px}
.gd .b{background:var(--the);border:1px solid var(--vien);border-left:3px solid var(--nhan);border-radius:var(--r);
  padding:21px 23px;box-shadow:var(--bong)}
.gd .b h3::before{counter-increment:g;content:"Giai đoạn " counter(g) " · ";color:var(--nhan2);font-size:14px;
  font-family:"Segoe UI",sans-serif;font-weight:800;letter-spacing:.04em}
.gd .b .ct{margin-top:11px;display:grid;gap:9px;grid-template-columns:repeat(auto-fit,minmax(216px,1fr))}
.gd .b .ct div{font-size:14.4px}
.gd .b .ct b{display:block;font-size:11.8px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--chu2);margin-bottom:2px}

/* ---------- HOI DAP ---------- */
details{background:var(--the);border:1px solid var(--vien);border-radius:11px;padding:15px 18px;margin-bottom:10px}
details[open]{border-color:var(--muc3)}
summary{cursor:pointer;font-weight:700;font-size:15.8px;color:var(--muc);list-style:none}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";float:right;font-size:20px;line-height:1;color:var(--nhan2)}
details[open] summary::after{content:"–"}
details p{font-size:15px;color:var(--chu2)}

/* ---------- BIEU MAU ---------- */
.mau{background:var(--the);border:1px solid var(--vien);border-radius:var(--r);padding:clamp(20px,3vw,32px);box-shadow:var(--bong)}
.mau-luoi{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(232px,1fr))}
.truong label{display:block;font-size:13.4px;font-weight:700;margin-bottom:5px}
.truong input,.truong select,.truong textarea{width:100%;padding:10px 12px;border:1px solid var(--vien);
  border-radius:9px;font-size:15.2px;font-family:inherit;background:var(--nen);color:var(--chu)}
.truong textarea{min-height:112px;resize:vertical}
.rong{grid-column:1/-1}
.nut-gui{margin-top:17px;padding:13px 30px;border:0;border-radius:10px;cursor:pointer;background:var(--muc);
  color:#fff;font-size:16px;font-weight:700;font-family:inherit}
:root[data-theme="dark"] .nut-gui{color:#0D2044}
.nut-gui:hover{background:var(--muc3)}

/* ---------- CHAN TRANG ---------- */
footer{background:var(--nen2);padding:34px 0 24px;font-size:14.2px;color:var(--chu2);border-top:1px solid var(--vien)}
.ft-luoi{display:grid;gap:24px;grid-template-columns:repeat(auto-fit,minmax(215px,1fr))}
footer b{color:var(--chu);display:block;margin-bottom:6px;font-size:14.4px}
footer a{color:var(--chu2);text-decoration:none}
footer a:hover{text-decoration:underline}
footer ul{list-style:none;margin:0;padding:0}
footer li{margin-bottom:4px}
.ft-cuoi{margin-top:24px;padding-top:16px;border-top:1px solid var(--vien);font-size:13.2px}

@media print{
  .top-nav,.menu-nut,.loc,.mau,.hero-nut{display:none!important}
  body{background:#fff;color:#000;font-size:11.5pt}
  section,.gd .b{page-break-inside:avoid;border:0}
  .bang-boc{overflow:visible;border:0}
}
"""

DAU_HIEU = ('<svg viewBox="0 0 34 34" aria-hidden="true">'
  '<circle cx="17" cy="17" r="16" fill="#184088"/>'
  '<rect x="10" y="7" width="14" height="15" rx="3.4" fill="none" stroke="#B8862A" stroke-width="1.7"/>'
  '<path d="M10 16h14" stroke="#B8862A" stroke-width="1.7"/>'
  '<circle cx="13.6" cy="19" r="1.2" fill="#B8862A"/><circle cx="20.4" cy="19" r="1.2" fill="#B8862A"/>'
  '<path d="M12 22l-2 4M22 22l2 4" stroke="#B8862A" stroke-width="1.7" stroke-linecap="round"/>'
  '<path d="M8 28h18" stroke="#B8862A" stroke-width="1.5" stroke-linecap="round"/></svg>')


def nav_html(slug):
    ra = []
    for s, t in NAV:
        goc = '../' if slug else ''
        cur = ' aria-current="page"' if s == slug else ''
        lop = ' class="nut-lh"' if s == 'lien-he' else ''
        ra.append('<a href="%s%s/index.html"%s%s>%s</a>' % (goc, s, lop, cur, t))
    return '\n        '.join(ra)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong'):
    goc = '../' if slug else ''
    dc = GOC + '/' + (slug + '/' if slug else '')
    ld = '\n'.join('<script type="application/ld+json">%s</script>' %
                   json.dumps(x, ensure_ascii=False, separators=(',', ':')) for x in (jsonld or []))
    return """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(td)s</title>
<meta name="description" content="%(mt)s">
<link rel="canonical" href="%(dc)s">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="theme-color" content="#184088">
<link rel="icon" href="data:image/svg+xml,%%3Csvg%%20xmlns%%3D%%22http%%3A%%2F%%2Fwww.w3.org%%2F2000%%2Fsvg%%22%%20viewBox%%3D%%220%%200%%2034%%2034%%22%%3E%%3Crect%%20width%%3D%%2234%%22%%20height%%3D%%2234%%22%%20rx%%3D%%227%%22%%20fill%%3D%%22%%23184088%%22%%2F%%3E%%3Crect%%20x%%3D%%2210%%22%%20y%%3D%%227%%22%%20width%%3D%%2214%%22%%20height%%3D%%2215%%22%%20rx%%3D%%223.4%%22%%20fill%%3D%%22none%%22%%20stroke%%3D%%22%%23B8862A%%22%%20stroke-width%%3D%%221.9%%22%%2F%%3E%%3Cpath%%20d%%3D%%22M10%%2016h14%%22%%20stroke%%3D%%22%%23B8862A%%22%%20stroke-width%%3D%%221.9%%22%%2F%%3E%%3Ccircle%%20cx%%3D%%2213.6%%22%%20cy%%3D%%2219%%22%%20r%%3D%%221.3%%22%%20fill%%3D%%22%%23B8862A%%22%%2F%%3E%%3Ccircle%%20cx%%3D%%2220.4%%22%%20cy%%3D%%2219%%22%%20r%%3D%%221.3%%22%%20fill%%3D%%22%%23B8862A%%22%%2F%%3E%%3Cpath%%20d%%3D%%22M12%%2022l-2%%204M22%%2022l2%%204%%22%%20stroke%%3D%%22%%23B8862A%%22%%20stroke-width%%3D%%221.9%%22%%20stroke-linecap%%3D%%22round%%22%%2F%%3E%%3Cpath%%20d%%3D%%22M8%%2028h18%%22%%20stroke%%3D%%22%%23B8862A%%22%%20stroke-width%%3D%%221.7%%22%%20stroke-linecap%%3D%%22round%%22%%2F%%3E%%3C%%2Fsvg%%3E">
<meta property="og:type" content="website">
<meta property="og:locale" content="vi_VN">
<meta property="og:site_name" content="Đường sắt đô thị">
<meta property="og:title" content="%(td)s">
<meta property="og:description" content="%(mt)s">
<meta property="og:url" content="%(dc)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(td)s">
<meta name="twitter:description" content="%(mt)s">
<style>%(css)s</style>
</head>
<body class="%(tang)s">

<header class="top">
  <div class="wrap top-in">
    <a class="hieu" href="%(goc)sindex.html">%(dh)s<span><b>Đường sắt đô thị</b><i>Văn bản · Quy trình · Kinh nghiệm</i></span></a>
    <button class="menu-nut" id="menu" aria-expanded="false" aria-controls="dhuong">Mục lục</button>
    <nav class="top-nav" id="dhuong">
        %(nav)s
    </nav>
  </div>
</header>

%(than)s

<footer>
  <div class="wrap">
    <div class="ft-luoi">
      <div><b>Đường sắt đô thị</b>Trang thông tin chuyên môn về đầu tư, quản lý và quyết toán
        dự án đường sắt đô thị tại Việt Nam.</div>
      <div><b>Tra cứu</b><ul>
        <li><a href="%(goc)svan-ban/index.html">Cập nhật văn bản</a></li>
        <li><a href="%(goc)squy-trinh/index.html">Quy trình thực hiện dự án</a></li>
        <li><a href="%(goc)skinh-nghiem/index.html">Kinh nghiệm quản lý dự án</a></li></ul></div>
      <div><b>Trao đổi</b><ul>
        <li><a href="%(goc)svuong-mac/index.html">Vướng mắc thường gặp</a></li>
        <li><a href="%(goc)stu-van/index.html">Gửi yêu cầu tư vấn</a></li>
        <li><a href="%(goc)slien-he/index.html">Liên hệ</a></li></ul></div>
      <div><b>Lưu ý</b>Nội dung trên trang là thông tin tham khảo, không thay thế ý kiến tư vấn
        cho một dự án cụ thể. Văn bản pháp luật thay đổi thường xuyên — luôn đối chiếu bản gốc.</div>
    </div>
    <div class="ft-cuoi">Bản quyền của Hãng Kiểm toán và Định giá ASCO · Nội dung biên soạn từ kho văn bản pháp luật nội bộ, cập nhật 24/08/2026.</div>
  </div>
</footer>
%(ld)s
<script>
(function(){var b=document.getElementById('menu'),n=document.getElementById('dhuong');
if(b&&n){b.addEventListener('click',function(){var m=n.hasAttribute('data-mo');
if(m){n.removeAttribute('data-mo');}else{n.setAttribute('data-mo','');}
b.setAttribute('aria-expanded',String(!m));});}})();
</script>
%(js)s
</body>
</html>
""" % dict(td=html.escape(tieude), mt=html.escape(mota), dc=dc, css=CSS, tang=tang,
           goc=goc, dh=DAU_HIEU, nav=nav_html(slug), than=than, ld=ld,
           js=than_js.get(slug, ''))


than_js = {}
print('Khung da nap. CSS %d ky tu.' % len(CSS))
