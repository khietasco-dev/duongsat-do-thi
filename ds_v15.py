# -*- coding: utf-8 -*-
"""Ban 15 — 9 TRANG DICH VU CAP 2 BANG TIENG ANH (dot 2 cua du an dich).

CEO 25/08: o che do tieng Anh, bam vao tung dich vu van ra tieng Viet.
Ban nay dung `/en/dich-vu/<slug>/` cho ca 9 dich vu. Trang 29 -> 38.

Sau ban nay, o che do TIENG ANH toan bo nhanh Dich vu da lien mach:
  menu -> bang so xuong -> trang tong -> 9 trang chi tiet, khong roi ve tieng Viet.
"""
import os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v7 as V7
import ds_v12 as V12
import ds_v13 as V13
import ds_v14 as V14
from ds_dv import DICH_VU, NHOM
from ds_dv_en import EN, KHUNG

# ---- khai bao: chu de nao da co ban dich o thu tieng nao
for _d in DICH_VU:
    V14.DA_DICH['dich-vu/' + _d['slug']] = {'en'}

# ---- trang tong tieng Anh: cac the tro toi ban tieng Anh, khong con la tieng Viet
V14.DICH_NHAC['en'] = ('All nine service pages below are available in <b>English</b>. '
                       'The legal documents they cite remain in Vietnamese — that is the '
                       'authoritative text.')


def _the(d, i, lang):
    co = lang in V14.DA_DICH.get('dich-vu/' + d['slug'], ())
    dia = ('@/%s/dich-vu/%s/index.html' % (lang, d['slug'])) if co \
        else ('@/dich-vu/%s/index.html' % d['slug'])
    return ('<a class="dv-the" href="%s"%s>'
            '<div class="so">%02d</div><h3>%s</h3><p>%s</p>'
            '<span class="di">%s</span></a>'
            % (dia, '' if co else ' hreflang="vi"', i,
               html.escape(V13.NHAN_MUC_DV[d['slug']][lang]),
               html.escape(V14.MO_TA[d['slug']][lang]),
               html.escape(V14.DICH[lang]['xem'])))


V14._the = _the


# ================================================================= trang chi tiet EN
def _trang_en(d):
    e = EN[d['slug']]
    K = KHUNG
    ten_nhom = V13.NHAN_NHOM[d['nhom']]['en']
    _, mau = NHOM[d['nhom']]

    def ds(items):
        return '<ul>%s</ul>' % ''.join('<li>%s</li>' % html.escape(x) for x in items)

    cc = ''.join('<div class="dv-cc"><b>%s</b><span>%s</span></div>'
                 % (html.escape(a), html.escape(b)) for a, b in e['can_cu'])
    bu = ''.join('<li><b>%s</b><span>%s</span></li>' % (html.escape(a), html.escape(b))
                 for a, b in e['lam_gi'])

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/en/index.html">%(nha)s</a> ·
    <a href="@/en/dich-vu/index.html">%(dv)s</a> · %(menu)s</div>
  <span class="the-loc" style="background:var(--nen3);color:%(mau)s">%(nhom)s</span>
  <h1>%(ten)s</h1>
  <p>%(lede)s</p>
</div></div>

<div class="than"><div class="wrap">

  <h2 style="margin-bottom:10px">%(h_vande)s</h2>
  %(vande)s

  <h2 style="margin:30px 0 10px">%(h_cancu)s</h2>
  <p class="small" style="margin-bottom:12px">%(cc_nhac)s</p>
  %(cancu)s

  <h2 style="margin:30px 0 6px">%(h_lamgi)s</h2>
  <ol class="dv-buoc">%(buoc)s</ol>

  <div class="luoi g2" style="margin-top:26px">
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>%(h_daura)s</h3>
      %(daura)s
    </div>
    <div class="the" style="border-left:3px solid var(--nhan)">
      <h3>%(h_khinao)s</h3>
      <p style="margin-top:8px">%(khinao)s</p>
    </div>
  </div>

  <div class="dv-luu"><b>%(luu_h)s</b> %(luu)s</div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>%(bt_h)s</h3>
    <p style="margin-top:8px">%(bt)s</p>
    <p class="small" style="margin-top:9px"><a href="@/en/dich-vu/index.html">%(bt_ve)s</a></p>
  </div>

</div></div>
""" % dict(nha=html.escape(K['duong_nha']), dv=html.escape(K['duong_dv']),
           menu=html.escape(V13.NHAN_MUC_DV[d['slug']]['en']),
           nhom=html.escape(ten_nhom), mau=mau,
           ten=html.escape(e['ten']), lede=html.escape(e['lede']),
           h_vande=html.escape(K['h_vande']), vande=ds(e['van_de']),
           h_cancu=html.escape(K['h_cancu']),
           cc_nhac=K['cancu_nhac'] % ('<a href="@/van-ban/index.html" hreflang="vi">%s</a>'
                                      % html.escape(K['cancu_lk'])),
           cancu=cc,
           h_lamgi=html.escape(K['h_lamgi']), buoc=bu,
           h_daura=html.escape(K['h_daura']), daura=ds(e['dau_ra']),
           h_khinao=html.escape(K['h_khinao']), khinao=html.escape(e['khi_nao']),
           luu_h=html.escape(K['luu_h']), luu=html.escape(K['luu']),
           bt_h=html.escape(K['bt_h']),
           bt=K['bt'] % ('<a href="@/tu-van/index.html" hreflang="vi">%s</a>'
                         % html.escape(K['bt_lk'])),
           bt_ve=html.escape(K['bt_ve']))

    ld = [{"@context": "https://schema.org", "@type": "Service",
           "name": e['ten'], "description": e['mt'], "serviceType": ten_nhom,
           "areaServed": "VN", "inLanguage": "en",
           "provider": {"@type": "Organization",
                        "name": "ASCO Auditing and Valuation Firm",
                        "telephone": "0825092007"}}]
    return than, ld


# ================================================================= khung
_V14_KHUNG = V14.khung
_NAV = re.compile(r'<nav class="top-nav" id="dhuong">.*?</nav>', re.S)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V14_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang != 'en':
        return h
    # tren trang tieng Anh: 9 muc trong bang so xuong tro toi ban tieng Anh
    goc = V12._goc(slug)
    m = _NAV.search(h)
    nav = m.group(0)
    for d in DICH_VU:
        cu = 'href="%sdich-vu/%s/index.html"' % (goc, d['slug'])
        moi = 'href="%sen/dich-vu/%s/index.html"' % (goc, d['slug'])
        nav = nav.replace('hreflang="vi" title="page in Vietnamese" class="vi-dich" ' + cu, moi)
        nav = nav.replace(cu, moi)
    return h[:m.start()] + nav + h[m.end():]


B.khung = khung

TRANG = list(V14.TRANG)
for _d in DICH_VU:
    TRANG.append(('en/dich-vu/' + _d['slug'], 'en', EN[_d['slug']]['td'], EN[_d['slug']]['mt'],
                  (lambda dd=_d: _trang_en(dd)), 'trong'))


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
