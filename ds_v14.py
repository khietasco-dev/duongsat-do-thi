# -*- coding: utf-8 -*-
"""Ban 14 — TRANG BEN TRONG DOI THEO NGON NGU (dot 1).

CEO 25/08: "bam sang tieng Anh thi cac trang ben trong cung phai tieng Anh".
Ca kho la 28.953 tu × 5 thu tieng = ~145.000 tu — khong the dich trong mot lan.
Dot 1 lam TRANG TONG DICH VU, la trang thuong mai quan trong nhat va la van cua
chinh minh (khong co trich dan dieu luat nen dich an toan).

Hai thu duoc dung o ban nay:
  1. `/en/dich-vu/` `/zh/...` `/ja/...` `/fr/...` `/de/...` — 5 trang dich tron ven
  2. NUT NGON NGU BIET TRANG: dung o trang nao thi doi sang dung trang do o thu tieng
     khac, neu chua co ban dich thi ve trang tong quan cua thu tieng do.
"""
import os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v6 as V6
import ds_v7 as V7
import ds_v12 as V12
import ds_v13 as V13
from ds_dv import DICH_VU, NHOM
from ds_dv_dich import TRANG as DICH, MO_TA

NGON = ['vi', 'en', 'zh', 'ja', 'fr', 'de']
# chu de nao da co ban dich, va co o nhung thu tieng nao
DA_DICH = {'dich-vu': {'en', 'zh', 'ja', 'fr', 'de'}}


def _tach(slug):
    """slug -> (ngon ngu cua trang, chu de). 'en/dich-vu' -> ('en','dich-vu')"""
    if slug in NGON[1:]:
        return slug, ''
    p = slug.split('/', 1)
    if p[0] in NGON[1:]:
        return p[0], (p[1] if len(p) > 1 else '')
    return 'vi', slug


def _dia_chi(lang, chu_de):
    """Dia chi cua mot chu de o mot thu tieng, viet bang dau @/ (= goc trang)."""
    if lang == 'vi':
        return '@/index.html' if not chu_de else '@/%s/index.html' % chu_de
    if chu_de and lang in DA_DICH.get(chu_de, ()):
        return '@/%s/%s/index.html' % (lang, chu_de)
    return '@/%s/index.html' % lang          # chua co ban dich -> trang tong quan


def _bo_ngon_ngu(slug, lang='vi'):
    """Nut chon ngon ngu BIET DANG DUNG TRANG NAO."""
    _, chu_de = _tach(slug)
    muc = []
    for ma, kyhieu, ten, _thumuc in V6.NGON_NGU:
        cur = ' aria-current="true"' if ma == lang else ''
        thieu = ''
        if chu_de and ma != 'vi' and ma not in DA_DICH.get(chu_de, ()):
            thieu = ' class="chua-dich"'
        elif chu_de and ma == 'vi' and lang != 'vi':
            thieu = ''
        muc.append('<a href="%s" hreflang="%s"%s%s><span>%s</span><span class="ma">%s</span></a>'
                   % (_dia_chi(ma, chu_de), ma, cur, thieu, html.escape(ten), kyhieu))
    return ('<details class="nn"><summary aria-label="%s">%s'
            '<span class="nhan">%s</span><span class="cau">▾</span></summary>'
            '<div class="nn-menu">%s</div></details>'
            % (html.escape(V6._NHAN_NUT[lang]), V6._CAU,
               html.escape(V6._TEN[lang]), ''.join(muc)))


V6._bo_ngon_ngu = _bo_ngon_ngu

B.CSS += r"""
/* muc ngon ngu chua co ban dich cho trang dang xem — bao truoc bang dau cham */
.nn-menu a.chua-dich>span:first-child::after{content:"·";margin-left:6px;opacity:.5}
.nn-menu a.chua-dich{opacity:.82}
"""


# ================================================================= trang tong dich vu dich
def _the(d, i, lang):
    return ('<a class="dv-the" href="@/dich-vu/%s/index.html" hreflang="vi">'
            '<div class="so">%02d</div><h3>%s</h3><p>%s</p>'
            '<span class="di">%s</span></a>'
            % (d['slug'], i, html.escape(V13.NHAN_MUC_DV[d['slug']][lang]),
               html.escape(MO_TA[d['slug']][lang]), html.escape(DICH[lang]['xem'])))


def _trang_dich_vu(lang):
    T = DICH[lang]
    khoi, i = [], 0
    for ma, (_ten_vi, mau) in NHOM.items():
        cac = []
        for d in [x for x in DICH_VU if x['nhom'] == ma]:
            i += 1
            cac.append(_the(d, i, lang))
        khoi.append('<h2 style="margin:30px 0 4px;border-left:4px solid %s;padding-left:12px">%s</h2>'
                    '<div class="dv-luoi">%s</div>'
                    % (mau, html.escape(V13.NHAN_NHOM[ma][lang]), ''.join(cac)))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/%(l)s/index.html">%(duong)s</a> · %(ten)s</div>
  <h1>%(h1)s</h1>
  <p>%(lede)s</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--muc3)">
    <h3>%(vs_h)s</h3>
    <p style="margin-top:8px">%(vs_1)s</p>
    <p>%(vs_2)s</p>
  </div>

  %(khoi)s

  <p class="small" style="margin-top:16px">%(nhac)s</p>

  <h2 style="margin:34px 0 10px">%(rg_h)s</h2>
  <div class="luoi g2">
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>%(duoc_h)s</h3>
      <p style="margin-top:8px">%(duoc_1)s</p>
      <p>%(duoc_2)s</p>
    </div>
    <div class="the" style="border-left:3px solid var(--do)">
      <h3>%(khong_h)s</h3>
      <p style="margin-top:8px">%(khong_1)s</p>
      <p>%(khong_2)s</p>
    </div>
  </div>

  <div class="the" style="border-left:3px solid var(--nhan);margin-top:20px">
    <h3>%(bd_h)s</h3>
    <p style="margin-top:8px">%(bd_1)s</p>
    <p class="small">%(bd_2)s</p>
  </div>

</div></div>
""" % dict(l=lang, duong=html.escape(T['duong']), ten=html.escape(T['ten']),
           h1=html.escape(T['h1']), lede=html.escape(T['lede']),
           vs_h=html.escape(T['vs_h']), vs_1=T['vs_1'], vs_2=T['vs_2'],
           khoi=''.join(khoi),
           nhac=DICH_NHAC[lang],
           rg_h=html.escape(T['rg_h']),
           duoc_h=html.escape(T['duoc_h']), duoc_1=T['duoc_1'], duoc_2=html.escape(T['duoc_2']),
           khong_h=html.escape(T['khong_h']), khong_1=T['khong_1'], khong_2=T['khong_2'],
           bd_h=html.escape(T['bd_h']),
           bd_1=T['bd_1'] % ('<a href="@/tu-van/index.html" hreflang="vi">%s</a>'
                            % html.escape(T['bd_lk'])),
           bd_2=T['bd_2'])

    ld = [{"@context": "https://schema.org", "@type": "ItemList",
           "name": T['h1'], "numberOfItems": len(DICH_VU),
           "itemListElement": [{"@type": "ListItem", "position": k + 1,
                                "name": V13.NHAN_MUC_DV[d['slug']][lang],
                                "url": B.GOC + "/dich-vu/" + d['slug'] + "/"}
                               for k, d in enumerate(DICH_VU)]}]
    return than, ld


# cau nhac: trang chi tiet van la tieng Viet
DICH_NHAC = {
    'en': 'Each service page below opens in <b>Vietnamese</b>. The nine summaries on this page are '
          'the full description available in English for now.',
    'zh': '下列各服务的详情页面为<b>越南语</b>。本页九段说明即目前可提供的中文完整介绍。',
    'ja': '以下の各サービスの詳細ページは<b>ベトナム語</b>です。本ページの九つの要約が、'
          '現時点で日本語で用意できる説明のすべてです。',
    'fr': 'Chaque page de service ci-dessous s’ouvre en <b>vietnamien</b>. Les neuf résumés de cette '
          'page constituent la description disponible en français à ce jour.',
    'de': 'Jede Leistungsseite unten öffnet auf <b>Vietnamesisch</b>. Die neun Kurzbeschreibungen '
          'auf dieser Seite sind das, was derzeit auf Deutsch vorliegt.',
}

_V13_KHUNG = V13.khung


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V13_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang == 'vi':
        return h
    # tren trang ngoai ngu: muc "Tat ca dich vu" tro toi ban dich, khong phai ban tieng Viet
    goc = V12._goc(slug)
    cu = 'href="%sdich-vu/index.html"' % goc
    moi = 'href="%s%s/dich-vu/index.html"' % (goc, lang)
    m = re.search(r'<nav class="top-nav" id="dhuong">.*?</nav>', h, re.S)
    nav = m.group(0)
    nav = nav.replace('class="vi-dich tat" ' + cu, 'class="tat" ' + moi, 1)
    nav = nav.replace(cu, moi, 1)
    return h[:m.start()] + nav + h[m.end():]


B.khung = khung

TRANG = list(V13.TRANG)
for _l in ('en', 'zh', 'ja', 'fr', 'de'):
    TRANG.append((_l + '/dich-vu', _l, DICH[_l]['td'], DICH[_l]['mt'],
                  (lambda L=_l: _trang_dich_vu(L)), 'trong'))


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
