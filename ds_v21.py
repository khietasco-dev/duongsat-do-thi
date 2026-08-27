# -*- coding: utf-8 -*-
"""Ban 21 — 13 TRANG TIENG NHAT CON LAI. BO TIENG NHAT XONG.

9 trang dich vu `/ja/dich-vu/<slug>/` + `/ja/van-ban/` `/ja/thu-vien-rui-ro/`
`/ja/kinh-nghiem/` `/ja/vuong-mac/`.  Trang **67 -> 80**.

Sau ban nay menu tren trang tieng Nhat khong con dau VI nao.

⚠ KE THUA BAN LIEN TRUOC (ds_v20), khong phai ban nao khac — ban 20 da vap loi nay
  (ke thua ds_v18 thay vi ds_v19) va roi mat 13 trang tieng Trung khoi sitemap.

⚠ Trang /ja/van-ban/ nam o thu muc khac voi kho tep /van-ban/tep/ nen phai di qua
  _o_tep() doi duong dan thanh @/van-ban/tep/... — ban 17 da vap 161 lien ket hong.

⚠ Bo dem cua bo loc: viet han mot khoi JS RIENG cho tieng Nhat.
  Ban 19 da vap khi thu va chuoi JS cua ban tieng Anh — phep thay khong an,
  cau tieng Anh lot len trang tieng Trung.
"""
import io, json, os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages2 as P2
import ds_v7 as V7
import ds_v8 as V8
import ds_v12 as V12
import ds_v13 as V13
import ds_v14 as V14
import ds_v17 as V17
import ds_v20 as V20
from ds_dv import DICH_VU, NHOM
from ds_ja_dv import JA, KHUNG
from ds_ja_rr import VB, CAP_JA, DIA_JA, RR, RR_NHOM
from ds_ja_kn import KN, KN_BH, KN_SL, KN_KT, VM, VM_DS

TM = os.path.dirname(os.path.abspath(__file__))
DL = json.load(io.open(os.path.join(TM, 'vb_phanloai.json'), encoding='utf-8'))
E = html.escape

CHU_DE = ['van-ban', 'thu-vien-rui-ro', 'kinh-nghiem', 'vuong-mac']
for _c in CHU_DE:
    V14.DA_DICH[_c] = V14.DA_DICH.get(_c, set()) | {'ja'}
for _d in DICH_VU:
    V14.DA_DICH['dich-vu/' + _d['slug']] = V14.DA_DICH.get('dich-vu/' + _d['slug'], set()) | {'ja'}

V14.DICH_NHAC['ja'] = ('以下九つの業務は、詳細ページにも<b>日本語版</b>があります。'
                       '引用している法令はベトナム語のままです。'
                       '法的効力を持つのはその本文だからです。')


def _banner(ten, h1, lede):
    return ("""
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/ja/index.html">ホーム</a> · %s</div>
  <h1>%s</h1>
  <p>%s</p>
</div></div>
""" % (E(ten), E(h1), E(lede)))


# ============================================================ 9 trang dich vu
def _trang_dv_ja(d):
    z = JA[d['slug']]
    K = KHUNG
    ten_nhom = V13.NHAN_NHOM[d['nhom']]['ja']
    _, mau = NHOM[d['nhom']]

    def ds(items):
        return '<ul>%s</ul>' % ''.join('<li>%s</li>' % E(x) for x in items)

    cc = ''.join('<div class="dv-cc"><b>%s</b><span>%s</span></div>' % (E(a), E(b))
                 for a, b in z['can_cu'])
    bu = ''.join('<li><b>%s</b><span>%s</span></li>' % (E(a), E(b)) for a, b in z['lam_gi'])

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/ja/index.html">%(nha)s</a> ·
    <a href="@/ja/dich-vu/index.html">%(dv)s</a> · %(menu)s</div>
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
      <h3>%(h_daura)s</h3>%(daura)s</div>
    <div class="the" style="border-left:3px solid var(--nhan)">
      <h3>%(h_khinao)s</h3><p style="margin-top:8px">%(khinao)s</p></div>
  </div>

  <div class="dv-luu"><b>%(luu_h)s</b> %(luu)s</div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>%(bt_h)s</h3><p style="margin-top:8px">%(bt)s</p>
    <p class="small" style="margin-top:9px"><a href="@/ja/dich-vu/index.html">%(bt_ve)s</a></p>
  </div>
</div></div>
""" % dict(nha=E(K['duong_nha']), dv=E(K['duong_dv']),
           menu=E(V13.NHAN_MUC_DV[d['slug']]['ja']), nhom=E(ten_nhom), mau=mau,
           ten=E(z['ten']), lede=E(z['lede']),
           h_vande=E(K['h_vande']), vande=ds(z['van_de']),
           h_cancu=E(K['h_cancu']),
           cc_nhac=K['cancu_nhac'] % ('<a href="@/ja/van-ban/index.html">%s</a>'
                                      % E(K['cancu_lk'])),
           cancu=cc, h_lamgi=E(K['h_lamgi']), buoc=bu,
           h_daura=E(K['h_daura']), daura=ds(z['dau_ra']),
           h_khinao=E(K['h_khinao']), khinao=E(z['khi_nao']),
           luu_h=E(K['luu_h']), luu=E(K['luu']), bt_h=E(K['bt_h']),
           bt=K['bt'] % ('<a href="@/ja/tu-van/index.html">%s</a>' % E(K['bt_lk'])),
           bt_ve=E(K['bt_ve']))
    return than, [{"@context": "https://schema.org", "@type": "Service",
                   "name": z['ten'], "description": z['mt'], "serviceType": ten_nhom,
                   "areaServed": "VN", "inLanguage": "ja",
                   "provider": {"@type": "Organization",
                                "name": "ベトナム ASCO 監査・評価事務所",
                                "telephone": "0825092007"}}]


# ============================================================ VAN BAN
# 🔧 SUA MOT LOI CU CO TU BAN 17: o cot "Mo tep", van ban chia nhieu ky hien nhan
# "N phần" bang TIENG VIET tren ca ba ban ngoai ngu (5 van ban moi ban).
# Chuoi do sinh trong ds_v8.o_tep. Nay dich theo tung thu tieng va ghi de lai
# _o_tep cua ban 17 (en) va ban 19 (zh) — sua mot cho, ca ba ban doi theo.
_NHAN_PHAN = {'en': '%d parts', 'zh': '共 %d 部分', 'ja': '全 %d 部'}
_RE_PHAN = re.compile(r'(\d+) phần')


def _tep_lang(d, lang):
    h = V8.o_tep(d).replace('href="tep/', 'href="@/van-ban/tep/')
    return _RE_PHAN.sub(lambda m: _NHAN_PHAN[lang] % int(m.group(1)), h)


def _o_tep(d):
    return _tep_lang(d, 'ja')


V17._o_tep = lambda d: _tep_lang(d, 'en')
V20.V19._o_tep = lambda d: _tep_lang(d, 'zh')


def trang_van_ban():
    LOP = {'Luật & Nghị quyết QH': 'tl-luat', 'Nghị định': 'tl-nd',
           'Thông tư': 'tl-tt', 'Văn bản khác': 'tl-khac'}
    hang = []
    for d in sorted(DL, key=lambda x: (x['ngan'], x['hien'])):
        tt = ('<span class="the-loc" style="background:var(--do-nen);color:var(--do)">%s</span>'
              % E(VB['hl_het']) if d['hethieuluc'] else
              '<span class="the-loc" style="background:var(--ngoc-nen);color:var(--ngoc)">%s</span>'
              % E(VB['hl_con']))
        hn = ' <span class="the-loc tl-tt">%s</span>' % E(VB['hn']) if d['hopnhat'] else ''
        phu = ('<span class="phu">%s</span>' % E(DIA_JA.get(d['diaban'], d['diaban']))
               if d['diaban'] != 'Toàn quốc' else '')
        ten = E(d.get('ten_dep') or d['ten_ngan'] or d['hien'])
        uu = (d['tep']['word'] or d['tep']['pdf'])
        if uu:
            ten = ('<a class="mo" href="@/van-ban/%s" target="_blank" rel="noopener" '
                   'hreflang="vi">%s</a>' % (E(uu[0]['duong_dan']), ten))
        hang.append(
            '<tr data-ngan="%s" data-dia="%s" data-nam="%s" data-tt="%s" data-tim="%s">'
            '<td><span class="the-loc %s">%s</span></td><td class="sohieu">%s</td>'
            '<td class="tenvb">%s%s%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
            % (E(d['ngan']), E(d['diaban']), d['nam'], 'het' if d['hethieuluc'] else 'con',
               E(P2.bo_dau(d['hien'] + ' ' + d.get('ten_dep', '') + ' ' + d['diaban']
                           + ' ' + d.get('sohieu', ''))),
               LOP[d['ngan']], E(CAP_JA[d['ngan']]), E(d.get('sohieu') or '—'),
               ten, hn, phu, d['nam'] or '—', tt, _o_tep(d)))

    nam = sorted({str(d['nam']) for d in DL if d['nam']}, reverse=True)
    tk = [len(DL), 110,
          sum(1 for d in DL if len(d['dinhdang']) > 1),
          sum(1 for d in DL if d['dinhdang'] == ['pdf']),
          sum(1 for d in DL if d['hopnhat']),
          sum(1 for d in DL if d['diaban'] in ('Hà Nội', 'TP. Hồ Chí Minh'))]

    than = _banner(VB['duong'], VB['h1'], VB['lede']) + """
<div class="than"><div class="wrap">
  <h2 style="margin-bottom:12px">%(h_cach)s</h2>
  <div class="huong-dan">%(cach)s</div>

  <h2 style="margin:26px 0 4px">%(h_co)s</h2>
  <div class="thongke">%(thongke)s</div>

  <h2 style="margin:26px 0 14px">%(h1)s</h2>
  <div class="loc"><div class="loc-hang">
    <div class="loc-o" style="flex:2 1 260px"><label for="q">%(loc_tim)s</label>
      <input id="q" type="search" placeholder="%(tim_gy)s"></div>
    <div class="loc-o"><label for="f1">%(loc_cap)s</label><select id="f1">
      <option value="">%(tatca)s</option>%(o_cap)s</select></div>
    <div class="loc-o"><label for="f2">%(loc_dia)s</label><select id="f2">
      <option value="">%(tatca)s</option>%(o_dia)s</select></div>
    <div class="loc-o"><label for="f3">%(loc_nam)s</label><select id="f3">
      <option value="">%(tatca)s</option>%(o_nam)s</select></div>
    <div class="loc-o"><label for="f4">%(loc_tt)s</label><select id="f4">
      <option value="">%(tatca)s</option><option value="con">%(hl_con)s</option>
      <option value="het">%(hl_het)s</option></select></div>
  </div><div class="loc-dem" id="dem"></div></div>

  <div class="bang-boc"><table id="bang">
    <thead><tr><th style="width:118px">%(l_cap)s</th><th style="width:142px">%(l_so)s</th>
    <th>%(l_ten)s</th><th style="width:62px">%(l_nam)s</th>
    <th style="width:96px">%(l_hl)s</th><th style="width:130px">%(l_tep)s</th></tr></thead>
    <tbody>%(hang)s</tbody></table></div>

  <h2 style="margin:32px 0 14px">%(h_cap)s</h2>
  <div class="buoc">%(cap)s</div>

  <h2 style="margin:32px 0 12px">%(h_luu)s</h2>
  <div class="luoi g2">%(luu)s</div>
</div></div>
""" % dict(h_cach=E(VB['h_cach']),
           cach=''.join('<div class="b"><b>%s</b><span>%s</span></div>' % (E(a), b)
                        for a, b in VB['cach']),
           h_co=E(VB['h_co']),
           thongke=''.join('<div><b>%d</b><span>%s</span></div>' % (v, E(n))
                           for v, n in zip(tk, VB['tk'])),
           h1=E(VB['h1']), loc_tim=E(VB['loc_tim']), tim_gy=E(VB['tim_gy']),
           loc_cap=E(VB['loc_cap']), loc_dia=E(VB['loc_dia']), loc_nam=E(VB['loc_nam']),
           loc_tt=E(VB['loc_tt']), tatca=E(VB['loc_tatca']),
           hl_con=E(VB['hl_con']), hl_het=E(VB['hl_het']),
           o_cap=''.join('<option value="%s">%s</option>' % (E(k), E(v)) for k, v in CAP_JA.items()),
           o_dia=''.join('<option value="%s">%s</option>' % (E(k), E(v)) for k, v in DIA_JA.items()),
           o_nam=''.join('<option value="%s">%s</option>' % (n, n) for n in nam),
           l_cap=E(VB['l_cap']), l_so=E(VB['l_so']), l_ten=E(VB['l_ten']), l_nam=E(VB['l_nam']),
           l_hl=E(VB['l_hl']), l_tep=E(VB['l_tep']), hang='\n'.join(hang),
           h_cap=E(VB['h_cap']),
           cap=''.join('<div class="b"><div><b>%s</b><span>%s</span></div></div>' % (E(a), E(b))
                       for a, b in VB['cap']),
           h_luu=E(VB['h_luu']),
           luu=''.join('<div class="the" style="border-left:3px solid var(--do)">'
                       '<h3>%s</h3><p style="margin-top:8px">%s</p></div>' % (E(a), E(b))
                       for a, b in VB['luu']))
    return than, [{"@context": "https://schema.org", "@type": "DataCatalog",
                   "name": VB['h1'], "description": VB['mt'], "inLanguage": "ja"}]


# Bo loc ban TIENG NHAT — khoi JS RIENG, khong va chuoi cua ban tieng khac.
B.than_js['ja/van-ban'] = """
<script>
(function(){
 var q=document.getElementById('q'),f=[1,2,3,4].map(function(i){return document.getElementById('f'+i);}),
     hang=[].slice.call(document.querySelectorAll('#bang tbody tr')),
     dem=document.getElementById('dem'), tong=hang.length;
 function bo(s){return s.normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/đ/g,'d').toLowerCase();}
 function loc(){
  var k=bo(q.value.trim()), n=0;
  hang.forEach(function(r){
   var ok=(!k||r.dataset.tim.toLowerCase().indexOf(k)>=0)
    &&(!f[0].value||r.dataset.ngan===f[0].value)
    &&(!f[1].value||r.dataset.dia===f[1].value)
    &&(!f[2].value||r.dataset.nam===f[2].value)
    &&(!f[3].value||r.dataset.tt===f[3].value);
   r.style.display=ok?'':'none'; if(ok)n++;});
  dem.innerHTML='全 '+tong+' 件中 <b>'+n+'</b> 件を表示';
 }
 [q].concat(f).forEach(function(e){e.addEventListener('input',loc);e.addEventListener('change',loc);});
 loc();
})();
</script>"""


# ============================================================ THU VIEN RUI RO
def trang_rui_ro():
    MAU = {'cao': 'var(--do)', 'trung': 'var(--nhan)', 'thap': 'var(--ngoc)'}
    kh, stt = [], 0
    for nhom, cac in RR_NHOM:
        rr = []
        for ten, dh, kt, muc in cac:
            stt += 1
            rr.append('<div class="b"><div class="ma">%02d</div><div><h3>%s</h3>'
                      '<p><b>%s。</b>%s</p><div class="luuy"><b>%s。</b>%s</div>'
                      '<p class="small" style="margin-top:6px;color:%s"><b>%s：%s</b></p>'
                      '</div></div>' % (stt, E(ten), E(RR['l_dh']), E(dh), E(RR['l_kt']), E(kt),
                                        MAU[muc], E(RR['l_muc']), E(RR['muc'][muc])))
        kh.append('<h3 style="margin:26px 0 4px;font-size:19px;color:var(--muc)">%s '
                  '<span class="small" style="font-weight:400">（%d）</span></h3>'
                  '<div class="gd">%s</div>' % (E(nhom), len(cac), ''.join(rr)))

    than = _banner(RR['duong'], RR['h1'], RR['lede']) + """
<div class="than"><div class="wrap">
  <div class="the" style="border-left:3px solid var(--do)">
    <h3>%(h_ng)s</h3><p style="margin-top:8px">%(ng)s</p></div>

  <h2 style="margin:30px 0 4px">%(h_ds)s <span class="small" style="font-weight:400">（33）</span></h2>
  %(kh)s

  <h2 style="margin:34px 0 10px">%(h_dung)s</h2>
  <div class="the"><ul>%(dung)s</ul></div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p></div>
</div></div>
""" % dict(h_ng=E(RR['h_ng']), ng=RR['ng'], h_ds=E(RR['h_ds']), kh=''.join(kh),
           h_dung=E(RR['h_dung']),
           dung=''.join('<li>%s</li>' % E(x) for x in RR['dung']),
           h_bt=E(RR['h_bt']),
           bt=RR['bt'] % ('<a href="@/ja/tu-van/index.html">%s</a>' % E(RR['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": RR['h1'], "description": RR['mt'], "inLanguage": "ja"}]


# ============================================================ KINH NGHIEM
def trang_kinh_nghiem():
    bh = ''.join('<div class="b"><div class="ma">%02d</div><div><h3>%s</h3><p>%s</p></div></div>'
                 % (i + 1, E(a), E(b)) for i, (a, b) in enumerate(KN_BH))
    sl = ''.join('<div class="the" style="border-left:3px solid var(--do)">'
                 '<h3>%s</h3><p style="margin-top:8px">%s</p></div>' % (E(a), E(b))
                 for a, b in KN_SL)
    kt = ''.join('<div class="the" style="border-left:3px solid var(--muc3)">'
                 '<h3>%s</h3><ul>%s</ul></div>'
                 % (E(a), ''.join('<li>%s</li>' % E(x) for x in b)) for a, b in KN_KT)

    than = _banner(KN['duong'], KN['h1'], KN['lede']) + """
<div class="than"><div class="wrap">
  <h2 style="margin-bottom:6px">%(h_bh)s</h2>
  <div class="gd">%(bh)s</div>

  <h2 style="margin:34px 0 12px">%(h_sl)s</h2>
  <div class="luoi g3">%(sl)s</div>

  <h2 style="margin:34px 0 6px">%(h_kt)s</h2>
  <p class="small" style="margin-bottom:14px">%(kt_lede)s</p>
  <div class="luoi g2">%(kt)s</div>

  <div class="the" style="border-left:3px solid var(--nhan);margin-top:22px">
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p></div>
</div></div>
""" % dict(h_bh=E(KN['h_bh']), bh=bh, h_sl=E(KN['h_sl']), sl=sl,
           h_kt=E(KN['h_kt']), kt_lede=E(KN['kt_lede']), kt=kt, h_bt=E(KN['h_bt']),
           bt=KN['bt'] % ('<a href="@/ja/dich-vu/ho-so-quyet-toan/index.html">%s</a>'
                          % E(KN['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": KN['h1'], "description": KN['mt'], "inLanguage": "ja"}]


# ============================================================ VUONG MAC
def trang_vuong_mac():
    ds = ''.join("""<div class="b">
  <h3>%s</h3>
  <div class="ct">
    <div><b>%s</b>%s</div><div><b>%s</b>%s</div>
    <div><b>%s</b>%s</div><div><b>%s</b><span style="color:var(--ngoc)">%s</span></div>
  </div>
</div>""" % (E('%d. %s' % (i + 1, ten)), E(VM['l_ht']), E(ht), E(VM['l_ng']), E(ng),
             E(VM['l_cc']), cc, E(VM['l_xl']), E(xl))
        for i, (ten, ht, ng, cc, xl) in enumerate(VM_DS))

    than = _banner(VM['duong'], VM['h1'], VM['lede']) + """
<div class="than"><div class="wrap">
  <div class="gd">%(ds)s</div>
  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p></div>
</div></div>
""" % dict(ds=ds, h_bt=E(VM['h_bt']),
           bt=VM['bt'] % ('<a href="@/ja/tu-van/index.html">%s</a>' % E(VM['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": VM['h1'], "description": VM['mt'], "inLanguage": "ja"}]


# ============================================================ khung
_V20_KHUNG = V20.khung
_NAV = re.compile(r'<nav class="top-nav" id="dhuong">.*?</nav>', re.S)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V20_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang != 'ja':
        return h
    goc = V12._goc(slug)
    m = _NAV.search(h)
    nav = m.group(0)
    nhac = V13.NHAC['ja']
    cac = CHU_DE + ['dich-vu/' + d['slug'] for d in DICH_VU]
    for c in cac:
        cu = 'href="%s%s/index.html"' % (goc, c)
        moi = 'href="%sja/%s/index.html"' % (goc, c)
        nav = nav.replace('hreflang="vi" title="%s" class="vi-dich" ' % nhac + cu, moi)
        nav = nav.replace(cu, moi)
    return h[:m.start()] + nav + h[m.end():]


B.khung = khung

TRANG = list(V20.TRANG) + [
    ('ja/dich-vu/' + d['slug'], 'ja', JA[d['slug']]['td'], JA[d['slug']]['mt'],
     (lambda dd: (lambda: _trang_dv_ja(dd)))(d), 'trong')
    for d in DICH_VU
] + [
    ('ja/van-ban', 'ja', VB['td'], VB['mt'], trang_van_ban, 'trong'),
    ('ja/thu-vien-rui-ro', 'ja', RR['td'], RR['mt'], trang_rui_ro, 'trong'),
    ('ja/kinh-nghiem', 'ja', KN['td'], KN['mt'], trang_kinh_nghiem, 'trong'),
    ('ja/vuong-mac', 'ja', VM['td'], VM['mt'], trang_vuong_mac, 'trong'),
]


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
