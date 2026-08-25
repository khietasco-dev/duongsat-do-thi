# -*- coding: utf-8 -*-
"""Ban 17 — BON TRANG TIENG ANH CUOI + CHAN TRANG (dot 4). Bo tieng Anh XONG.

/en/van-ban/ · /en/thu-vien-rui-ro/ · /en/kinh-nghiem/ · /en/vuong-mac/  -> trang 42 -> 46.
Chan trang tren trang tieng Anh cung doi sang tieng Anh.

Trang /en/van-ban/ dung bang rieng, KHONG chep tu ban tieng Viet roi thay chu:
ten van ban giu nguyen tieng Viet, chi giao dien la tieng Anh.
"""
import io, json, os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages2 as P2
import ds_v7 as V7
import ds_v8 as V8
import ds_v12 as V12
import ds_v14 as V14
import ds_v16 as V16
from ds_en_rr import VB, RR, RR_NHOM
from ds_en_kn import KN, KN_BH, KN_SL, KN_KT, VM, VM_DS, CHAN

TM = os.path.dirname(os.path.abspath(__file__))
DL = json.load(io.open(os.path.join(TM, 'vb_phanloai.json'), encoding='utf-8'))
E = html.escape

CHU_DE = ['van-ban', 'thu-vien-rui-ro', 'kinh-nghiem', 'vuong-mac']
for _c in CHU_DE:
    V14.DA_DICH[_c] = {'en'}

CAP_EN = {'Luật & Nghị quyết QH': 'Law / NA resolution', 'Nghị định': 'Decree',
          'Thông tư': 'Circular', 'Văn bản khác': 'Other'}
DIA_EN = {'Toàn quốc': 'Nationwide', 'Hà Nội': 'Hanoi', 'TP. Hồ Chí Minh': 'Ho Chi Minh City'}


def _o_tep(d):
    """Kho tep nam o /van-ban/tep/ — trang tieng Anh o /en/van-ban/ nen phai
    tro bang duong dan tinh tu goc trang, khong dung duong dan tuong doi."""
    return V8.o_tep(d).replace('href="tep/', 'href="@/van-ban/tep/')


def _banner(ten, h1, lede):
    return ("""
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/en/index.html">Home</a> · %s</div>
  <h1>%s</h1>
  <p>%s</p>
</div></div>
""" % (E(ten), E(h1), E(lede)))


# ============================================================ 1. VAN BAN
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
        phu = ('<span class="phu">%s</span>' % E(DIA_EN.get(d['diaban'], d['diaban']))
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
               LOP[d['ngan']], E(CAP_EN[d['ngan']]), E(d.get('sohieu') or '—'),
               ten, hn, phu, d['nam'] or '—', tt, _o_tep(d)))

    nam = sorted({str(d['nam']) for d in DL if d['nam']}, reverse=True)
    cach = ''.join('<div class="b"><b>%s</b><span>%s</span></div>' % (E(a), b)
                   for a, b in VB['cach'])
    tk = [len(DL), 110,
          sum(1 for d in DL if len(d['dinhdang']) > 1),
          sum(1 for d in DL if d['dinhdang'] == ['pdf']),
          sum(1 for d in DL if d['hopnhat']),
          sum(1 for d in DL if d['diaban'] in ('Hà Nội', 'TP. Hồ Chí Minh'))]
    thongke = ''.join('<div><b>%d</b><span>%s</span></div>' % (v, E(n))
                      for v, n in zip(tk, VB['tk']))
    cap = ''.join('<div class="b"><div><b>%s</b><span>%s</span></div></div>' % (E(a), E(b))
                  for a, b in VB['cap'])
    luu = ''.join('<div class="the" style="border-left:3px solid var(--do)">'
                  '<h3>%s</h3><p style="margin-top:8px">%s</p></div>' % (E(a), E(b))
                  for a, b in VB['luu'])

    than = _banner(VB['duong'], VB['h1'], VB['lede']) + """
<div class="than"><div class="wrap">

  <h2 style="margin-bottom:12px">%(h_cach)s</h2>
  <div class="huong-dan">%(cach)s</div>

  <h2 style="margin:26px 0 4px">%(h_co)s</h2>
  <div class="thongke">%(thongke)s</div>

  <h2 style="margin:26px 0 14px">%(h1)s</h2>
  <div class="loc">
    <div class="loc-hang">
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
    </div>
    <div class="loc-dem" id="dem"></div>
  </div>

  <div class="bang-boc">
    <table id="bang">
      <thead><tr><th style="width:124px">%(l_cap)s</th><th style="width:142px">%(l_so)s</th>
      <th>%(l_ten)s</th><th style="width:62px">%(l_nam)s</th>
      <th style="width:104px">%(l_hl)s</th><th style="width:130px">%(l_tep)s</th></tr></thead>
      <tbody>%(hang)s</tbody>
    </table>
  </div>

  <h2 style="margin:32px 0 14px">%(h_cap)s</h2>
  <div class="buoc">%(cap)s</div>

  <h2 style="margin:32px 0 12px">%(h_luu)s</h2>
  <div class="luoi g2">%(luu)s</div>

</div></div>
""" % dict(h_cach=E(VB['h_cach']), cach=cach, h_co=E(VB['h_co']), thongke=thongke,
           h1=E(VB['h1']), loc_tim=E(VB['loc_tim']), tim_gy=E(VB['tim_gy']),
           loc_cap=E(VB['loc_cap']), loc_dia=E(VB['loc_dia']), loc_nam=E(VB['loc_nam']),
           loc_tt=E(VB['loc_tt']), tatca=E(VB['loc_tatca']),
           hl_con=E(VB['hl_con']), hl_het=E(VB['hl_het']),
           o_cap=''.join('<option value="%s">%s</option>' % (E(k), E(v)) for k, v in CAP_EN.items()),
           o_dia=''.join('<option value="%s">%s</option>' % (E(k), E(v)) for k, v in DIA_EN.items()),
           o_nam=''.join('<option value="%s">%s</option>' % (n, n) for n in nam),
           l_cap=E(VB['l_cap']), l_so=E(VB['l_so']), l_ten=E(VB['l_ten']), l_nam=E(VB['l_nam']),
           l_hl=E(VB['l_hl']), l_tep=E(VB['l_tep']), hang='\n'.join(hang),
           h_cap=E(VB['h_cap']), cap=cap, h_luu=E(VB['h_luu']), luu=luu)
    return than, [{"@context": "https://schema.org", "@type": "DataCatalog",
                   "name": VB['h1'], "description": VB['mt'], "inLanguage": "en"}]


B.than_js['en/van-ban'] = """
<script>
(function(){
 var q=document.getElementById('q'),f=[1,2,3,4].map(function(i){return document.getElementById('f'+i);}),
     hang=[].slice.call(document.querySelectorAll('#bang tbody tr')),
     dem=document.getElementById('dem'), tong=hang.length;
 function bo(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/đ/g,'d').toLowerCase();}
 function loc(){
  var k=bo(q.value.trim()), n=0;
  hang.forEach(function(r){
   var ok=(!k||r.dataset.tim.toLowerCase().indexOf(k)>=0)
    &&(!f[0].value||r.dataset.ngan===f[0].value)
    &&(!f[1].value||r.dataset.dia===f[1].value)
    &&(!f[2].value||r.dataset.nam===f[2].value)
    &&(!f[3].value||r.dataset.tt===f[3].value);
   r.style.display=ok?'':'none'; if(ok)n++;});
  dem.innerHTML='<b>'+n+'</b> of '+tong+' instruments';
 }
 [q].concat(f).forEach(function(e){e.addEventListener('input',loc);e.addEventListener('change',loc);});
 loc();
})();
</script>"""


# ============================================================ 2. THU VIEN RUI RO
def trang_rui_ro():
    MAU = {'cao': 'var(--do)', 'trung': 'var(--nhan)', 'thap': 'var(--ngoc)'}
    kh = []
    stt = 0
    for nhom, cac in RR_NHOM:
        rr = []
        for ten, dh, kt, muc in cac:
            stt += 1
            rr.append('<div class="b"><div class="ma">%02d</div><div><h3>%s</h3>'
                      '<p><b>%s.</b> %s</p><div class="luuy"><b>%s.</b> %s</div>'
                      '<p class="small" style="margin-top:6px;color:%s"><b>%s: %s</b></p>'
                      '</div></div>'
                      % (stt, E(ten), E(RR['l_dh']), E(dh), E(RR['l_kt']), E(kt),
                         MAU[muc], E(RR['l_muc']), E(RR['muc'][muc])))
        kh.append('<h3 style="margin:26px 0 4px;font-size:19px;color:var(--muc)">%s '
                  '<span class="small" style="font-weight:400">(%d)</span></h3>'
                  '<div class="gd">%s</div>' % (E(nhom), len(cac), ''.join(rr)))
    dung = ''.join('<li>%s</li>' % E(x) for x in RR['dung'])

    than = _banner(RR['duong'], RR['h1'], RR['lede']) + """
<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--do)">
    <h3>%(h_ng)s</h3><p style="margin-top:8px">%(ng)s</p>
  </div>

  <h2 style="margin:30px 0 4px">%(h_ds)s <span class="small" style="font-weight:400">(33)</span></h2>
  %(kh)s

  <h2 style="margin:34px 0 10px">%(h_dung)s</h2>
  <div class="the"><ul>%(dung)s</ul></div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p>
  </div>

</div></div>
""" % dict(h_ng=E(RR['h_ng']), ng=RR['ng'], h_ds=E(RR['h_ds']), kh=''.join(kh),
           h_dung=E(RR['h_dung']), dung=dung, h_bt=E(RR['h_bt']),
           bt=RR['bt'] % ('<a href="@/en/tu-van/index.html">%s</a>' % E(RR['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": RR['h1'], "description": RR['mt'], "inLanguage": "en"}]


# ============================================================ 3. KINH NGHIEM
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
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p>
  </div>

</div></div>
""" % dict(h_bh=E(KN['h_bh']), bh=bh, h_sl=E(KN['h_sl']), sl=sl,
           h_kt=E(KN['h_kt']), kt_lede=E(KN['kt_lede']), kt=kt,
           h_bt=E(KN['h_bt']),
           bt=KN['bt'] % ('<a href="@/en/dich-vu/ho-so-quyet-toan/index.html">%s</a>'
                          % E(KN['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": KN['h1'], "description": KN['mt'], "inLanguage": "en"}]


# ============================================================ 4. VUONG MAC
def trang_vuong_mac():
    ds = ''.join("""<div class="b">
  <h3>%s</h3>
  <div class="ct">
    <div><b>%s</b>%s</div>
    <div><b>%s</b>%s</div>
    <div><b>%s</b>%s</div>
    <div><b>%s</b><span style="color:var(--ngoc)">%s</span></div>
  </div>
</div>""" % (E('%d. %s' % (i + 1, ten)), E(VM['l_ht']), E(ht), E(VM['l_ng']), E(ng),
             E(VM['l_cc']), E(cc), E(VM['l_xl']), E(xl))
        for i, (ten, ht, ng, cc, xl) in enumerate(VM_DS))

    than = _banner(VM['duong'], VM['h1'], VM['lede']) + """
<div class="than"><div class="wrap">
  <div class="gd">%(ds)s</div>
  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p>
  </div>
</div></div>
""" % dict(ds=ds, h_bt=E(VM['h_bt']),
           bt=VM['bt'] % ('<a href="@/en/tu-van/index.html">%s</a>' % E(VM['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": VM['h1'], "description": VM['mt'], "inLanguage": "en"}]


# ============================================================ chan trang tieng Anh
def _chan(h, lang, goc):
    C = CHAN[lang]
    m = re.search(r'<footer>.*?</footer>', h, re.S)
    if not m:
        raise SystemExit('KHONG TIM THAY chan trang')

    def cot(nhan, muc):
        return ('<div><b>%s</b><ul>%s</ul></div>'
                % (E(nhan), ''.join('<li><a href="%s%s/index.html">%s</a></li>'
                                    % (goc, s, E(t)) for s, t in muc)))
    ngay = re.search(r'Văn bản được cập nhật đến ([^<.]+)', m.group(0))
    moi = """<footer>
  <div class="wrap">
    <div class="ft-luoi">
      <div><b>Urban railway</b>%s</div>
      %s
      %s
      <div><b>%s</b>%s</div>
    </div>
    <div class="ft-cuoi">%s<span class="ngay">%s</span></div>
  </div>
</footer>""" % (E(C['gt']), cot(C['c1'], C['m1']), cot(C['c2'], C['m2']),
                E(C['c3']), E(C['luu']), E(C['bq']),
                E(C['ngay'] % (ngay.group(1).strip() if ngay else '')))
    return h[:m.start()] + moi + h[m.end():]


# ============================================================ khung
_V16_KHUNG = V16.khung
_NAV = re.compile(r'<nav class="top-nav" id="dhuong">.*?</nav>', re.S)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V16_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang != 'en':
        return h
    goc = V12._goc(slug)
    m = _NAV.search(h)
    nav = m.group(0)
    for c in CHU_DE:
        cu = 'href="%s%s/index.html"' % (goc, c)
        moi = 'href="%sen/%s/index.html"' % (goc, c)
        nav = nav.replace('hreflang="vi" title="page in Vietnamese" class="vi-dich" ' + cu, moi)
        nav = nav.replace(cu, moi)
    h = h[:m.start()] + nav + h[m.end():]
    return _chan(h, 'en', goc)


B.khung = khung

TRANG = list(V16.TRANG) + [
    ('en/van-ban', 'en', VB['td'], VB['mt'], trang_van_ban, 'trong'),
    ('en/thu-vien-rui-ro', 'en', RR['td'], RR['mt'], trang_rui_ro, 'trong'),
    ('en/kinh-nghiem', 'en', KN['td'], KN['mt'], trang_kinh_nghiem, 'trong'),
    ('en/vuong-mac', 'en', VM['td'], VM['mt'], trang_vuong_mac, 'trong'),
]


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
