# -*- coding: utf-8 -*-
"""Ban 11 — THANH DAU HAI HANG, bo han nut "Muc luc".

CEO chot 25/08/2026:
  - Hang tren: logo ĐƯỜNG SẮT ĐÔ THỊ + hotline (trai) · nut Chon ngon ngu (phai)
  - Hang duoi: DU 8 MUC MENU, luon hien, khong gom vao nut "Muc luc"
  - Tren dien thoai menu XUONG DONG cho du 8 muc (khong vuot ngang, khong an mucQ)
  - Giu nguyen nhan "Kiem toan QT", khong doi thanh ten day du

So do da do trong trinh duyet truoc khi lam:
  - 8 muc o co chu 14,6px + khoang cach 16px = 589px
  - Hang rieng rong 1.136px  ->  thua 547px, thoai mai mot dong
  - Man 375px: khoang chu 343px, can 527px  ->  2 dong
  - Menu bat dau xuong dong tu khoang 640px tro xuong
"""
import io, os, re, sys
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v6 as V6
import ds_v7 as V7
import ds_v10 as V10

B.CSS += r"""
/* ================= THANH DAU HAI HANG (ban 11) ================= */
/* Hang 1: logo + hotline ben trai, nut ngon ngu ben phai */
.top-in{padding:10px 22px 9px;gap:12px}
.top-in .hieu{margin-right:auto}
/* Luat chung `details{...}` (dung cho khoi hoi-dap) dinh ca vao nut ngon ngu:
   no boc them mot khung vien + nen + padding 15/18, lam hang 1 cao vong len
   100px va ve mot cai hop thua quanh nut. Go sach o day. */
.nn{margin:0!important;padding:0!important;border:0!important;background:none!important;
  border-radius:0!important}

/* Bo han nut Muc luc o MOI kho man hinh */
.menu-nut{display:none!important}

/* Hang 2: day du menu, tu xuong dong khi het cho */
.hang-menu{border-top:1px solid var(--vien)}
.top-nav{position:static!important;display:flex!important;flex-direction:row!important;
  flex-wrap:wrap;align-items:center;justify-content:flex-start;gap:7px 17px;
  padding:8px 0 9px!important;background:none!important;border:0!important;
  top:auto;left:auto;right:auto}
.top-nav a{font-size:14.6px;padding:3px 0!important;border-bottom:0!important;line-height:1.35}
.top-nav .nut-lh{padding:6px 15px!important;margin-top:0!important;text-align:center}

/* Thanh dau dinh theo man hinh khi menu con gon mot dong.
   Duoi 700px menu thanh hai dong, thanh dau cao ~140px — de dinh thi an mat
   mot phan sau man hinh dien thoai, nen tha cho no cuon di. */
@media(max-width:1160px){
  header.top{position:sticky}
  .top-nav{gap:7px 15px}
}
@media(max-width:700px){
  header.top{position:relative}
  .top-nav{gap:6px 13px}
  .top-nav a{font-size:13px}
  .top-nav .nut-lh{padding:5px 13px!important}
}
@media(max-width:400px){
  .top-nav{gap:5px 11px}
  .top-nav a{font-size:12.4px}
}
@media print{.top-nav,.hang-menu{display:none!important}}
"""

_V10_KHUNG = V10.khung
_NUT = re.compile(r'\s*<button class="menu-nut"[^>]*>.*?</button>', re.S)
_NAV = re.compile(r'[ \t]*<nav class="top-nav" id="dhuong">.*?</nav>\n?', re.S)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V10_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)

    # 1. bo nut "Muc luc"
    h, n1 = _NUT.subn('', h, count=1)

    # 2. nhac khoi <nav> ra khoi hang 1
    m = _NAV.search(h)
    if not (n1 and m):
        raise SystemExit('KHONG TIM THAY nut Muc luc (%d) hoac khoi nav (%s)'
                         % (n1, bool(m)))
    nav = m.group(0).strip()
    h = h[:m.start()] + h[m.end():]

    # 3. dat lai thanh HANG 2, ngay truoc </header>
    hang2 = '  <div class="hang-menu">\n    <div class="wrap">\n      %s\n    </div>\n  </div>\n' % nav
    neo = '  </div>\n</header>'
    if neo not in h:
        raise SystemExit('KHONG TIM THAY cho dong hang 1 cua thanh dau')
    h = h.replace(neo, '  </div>\n' + hang2 + '</header>', 1)
    return h


B.khung = khung
TRANG = V10.TRANG


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
