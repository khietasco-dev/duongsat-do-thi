# -*- coding: utf-8 -*-
"""Ban 16 — BON TRANG TIENG ANH: Quy trinh · Kiem toan QT · Tu van · Lien he (dot 3).

Trang 38 -> 42. Sau ban nay, o che do tieng Anh nguoi doc di duoc tron mach:
  Dich vu -> Quy trinh -> Kiem toan QT -> Tu van -> Lien he.
Con lai o ban tieng Anh: Van ban · Thu vien rui ro · Kinh nghiem · Vuong mac.
"""
import os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v7 as V7
import ds_v9 as V9
import ds_v12 as V12
import ds_v14 as V14
import ds_v15 as V15
from ds_en_qt import QT, QT_GD, QT_NGAN, QT_HO, KT, KT_VS, KT_SS, KT_PH, KT_CD, KT_KL
from ds_en_tv import TV, LH

CHU_DE = ['quy-trinh', 'kiem-toan', 'tu-van', 'lien-he']
for _c in CHU_DE:
    V14.DA_DICH[_c] = {'en'}

E = html.escape


def _banner(ten, h1, lede, l1=None):
    return ("""
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/en/index.html">Home</a> · %s</div>
  <h1>%s</h1>
  <p>%s</p>
</div></div>
""" % (E(ten), E(h1), lede))


# ============================================================ 1. QUY TRINH
def trang_quy_trinh():
    gd = []
    for ten, viec, tq, cc, kq, bay in QT_GD:
        gd.append("""<div class="b">
  <h3>%s</h3>
  <p style="margin:7px 0 0;font-size:15.3px;color:var(--chu2)">%s</p>
  <div class="ct">
    <div><b>%s</b>%s</div>
    <div><b>%s</b>%s</div>
    <div><b>%s</b>%s</div>
    <div><b>%s</b><span style="color:var(--do)">%s</span></div>
  </div>
</div>""" % (E(ten), E(viec), E(QT['l_tq']), E(tq), E(QT['l_cc']), E(cc),
             E(QT['l_kq']), E(kq), E(QT['l_bay']), E(bay)))

    LOP = {'ngoc': 'tl-luat', 'do': 'tl-khac', 'nhan': 'tl-nd', 'muc': 'tl-tt'}
    ng = ''.join(
        '<tr><td><span class="the-loc %s" style="font-size:13px">Track %s</span></td>'
        '<td><b>%s</b></td><td>%s</td><td>%s</td></tr>'
        % (LOP[mau], E(ma), E(ten), E(pv), E(vb)) for ma, ten, pv, vb, mau in QT_NGAN)

    ho = ''.join('<div class="the" style="border-left:3px solid var(--do)">'
                 '<h3>%s</h3><p style="margin-top:8px">%s</p></div>' % (E(a), E(b))
                 for a, b in QT_HO)

    than = _banner(QT['duong'], QT['h1'], E(QT['lede'])) + """
<div class="than"><div class="wrap">

  <h2 style="margin-bottom:14px">%(h_gd)s</h2>
  <div class="gd">%(gd)s</div>

  <h2 style="margin:34px 0 8px">%(h_ngan)s</h2>
  <p style="margin-bottom:14px">%(ngan_lede)s</p>
  <div class="bang-boc"><table>
    <thead><tr><th style="width:104px">Track</th><th style="width:26%%">Project type</th>
    <th style="width:22%%">%(l_pv)s</th><th>%(l_vb)s</th></tr></thead>
    <tbody>%(ngan)s</tbody>
  </table></div>

  <h2 style="margin:34px 0 8px">%(h_ho)s</h2>
  <p style="margin-bottom:14px">%(ho_lede)s</p>
  <div class="luoi g3">%(ho)s</div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>%(h_ke)s</h3>
    <p style="margin-top:8px">%(ke)s</p>
  </div>

</div></div>
""" % dict(h_gd=E(QT['h_gd']), gd=''.join(gd),
           h_ngan=E(QT['h_ngan']), ngan_lede=E(QT['ngan_lede']),
           l_pv=E(QT['l_pv']), l_vb=E(QT['l_vb']), ngan=ng,
           h_ho=E(QT['h_ho']), ho_lede=E(QT['ho_lede']), ho=ho,
           h_ke=E(QT['h_ke']),
           ke=QT['ke'] % ('<a href="@/en/kiem-toan/index.html">%s</a>' % E(QT['ke_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": QT['h1'], "description": QT['mt'], "inLanguage": "en"}]


# ============================================================ 2. KIEM TOAN QT
def _bang_dm_en():
    moc = ['≤ 5', '10', '50', '100', '500', '1,000', '≥ 10,000']

    def hang(nhan, ds):
        return ('<tr><td><b>%s</b></td>%s</tr>'
                % (nhan, ''.join('<td class="n">%s</td>' % x for x in ds)))
    return """<div class="bang-boc"><table class="bang-dm">
    <thead><tr><th style="width:32%%">%s</th>%s</tr></thead>
    <tbody>%s%s</tbody>
  </table></div>""" % (E(KT['bang_gt']), ''.join('<th class="n">%s</th>' % m for m in moc),
                       hang(E(KT['bang_kt']), V9.KT), hang(E(KT['bang_tt']), V9.TT))


def trang_kiem_toan():
    vs = ''.join('<div class="the" style="border-left:3px solid var(--nhan);margin-bottom:13px">'
                 '<h3>%d. %s</h3><p style="margin-top:8px">%s</p></div>'
                 % (i + 1, E(a), E(b)) for i, (a, b) in enumerate(KT_VS))
    ss = ''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (E(a), E(b), E(c))
                 for a, b, c in KT_SS)
    ph = ''.join('<div class="b"><div class="ma">%s</div><div><h3>%s</h3><p>%s</p>'
                 '<div class="luuy">%s</div></div></div>' % (E(ma), E(t), E(n), E(l))
                 for ma, t, n, l in KT_PH)
    cd = ''.join('<div class="the" style="border-left:3px solid var(--ngoc)">'
                 '<h3>%s</h3><p style="margin-top:8px"><code>%s</code></p><p>%s</p></div>'
                 % (E(a), E(b), E(c)) for a, b, c in KT_CD)
    kl = ''.join('<div class="the" style="border-left:3px solid var(--do)">'
                 '<h3>%s</h3><p style="margin-top:8px">%s</p></div>' % (E(a), E(b))
                 for a, b in KT_KL)

    than = _banner(KT['duong'], KT['h1'], E(KT['lede'])) + """
<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--muc3)">
    <h3>%(h_sh)s</h3><p style="margin-top:8px">%(sh)s</p>
  </div>

  <h2 style="margin:32px 0 12px">%(h_vs)s</h2>
  %(vs)s

  <h2 style="margin:32px 0 12px">%(h_ss)s</h2>
  <div class="bang-boc"><table>
    <thead><tr><th style="width:24%%"></th><th>%(c1)s</th><th>%(c2)s</th></tr></thead>
    <tbody>%(ss)s</tbody>
  </table></div>

  <h2 style="margin:32px 0 6px">%(h_ph)s</h2>
  <p class="small" style="margin-bottom:14px">%(ph_lede)s</p>
  <div class="gd">%(ph)s</div>

  <h2 style="margin:32px 0 8px">%(h_cd)s</h2>
  <p class="small" style="margin-bottom:14px">%(cd_lede)s</p>
  <div class="luoi g2">%(cd)s</div>

  <h2 style="margin:32px 0 12px">%(h_kl)s</h2>
  <div class="luoi g3">%(kl)s</div>

  <h2 style="margin:34px 0 10px">%(h_phi)s</h2>
  <p style="margin-bottom:4px">%(phi_1)s</p>
  <p class="small" style="margin-top:6px">%(phi_2)s</p>

  <div class="mtp">
    <div class="mtp-luoi">
      <div>
        <div class="o">
          <label for="pg">%(l_gt)s<span class="phu">%(l_gt_phu)s</span></label>
          <input id="pg" type="number" min="0" step="0.1" value="120" inputmode="decimal">
        </div>
        <div class="o">
          <label for="pdv">%(l_dv)s</label>
          <select id="pdv"><option value="1000000000" selected>%(l_ty)s</option>
          <option value="1000000">%(l_tr)s</option><option value="1">%(l_d)s</option></select>
        </div>
        <div class="o">
          <label for="pvat">%(l_vat)s</label>
          <select id="pvat"><option value="10" selected>10%%</option>
          <option value="8">8%%</option><option value="0">%(l_kvat)s</option></select>
        </div>
        <label class="tick"><input type="checkbox" id="ptb"><span>%(tick_tb)s</span></label>
        <label class="tick"><input type="checkbox" id="pbt"><span>%(tick_bt)s</span></label>
        <label class="tick"><input type="checkbox" id="pkt"><span>%(tick_kt)s</span></label>
      </div>
      <div class="kq" id="pkq"></div>
    </div>
  </div>

  <h3 style="margin:26px 0 8px">%(h_bang)s</h3>
  %(bang)s
  <p class="small">%(bang_ghi)s</p>

  <div class="luoi g2" style="margin-top:20px">
    <div class="the" style="border-left:3px solid var(--do)">
      <h3>%(h_nho)s</h3><p style="margin-top:8px">%(nho)s</p>
    </div>
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>%(h_sh2)s</h3>
      <p style="margin-top:8px">%(sh2)s</p><p>%(sh3)s</p>
    </div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p>
  </div>

</div></div>
""" % dict(h_sh=E(KT['h_sh']), sh=E(KT['sh']),
           h_vs=E(KT['h_vs']), vs=vs,
           h_ss=E(KT['h_ss']), c1=E(KT['ss_cot'][1]), c2=E(KT['ss_cot'][2]), ss=ss,
           h_ph=E(KT['h_ph']), ph_lede=E(KT['ph_lede']), ph=ph,
           h_cd=E(KT['h_cd']), cd_lede=E(KT['cd_lede']), cd=cd,
           h_kl=E(KT['h_kl']), kl=kl,
           h_phi=E(KT['h_phi']), phi_1=KT['phi_1'], phi_2=KT['phi_2'],
           l_gt=E(KT['l_gt']), l_gt_phu=E(KT['l_gt_phu']),
           l_dv=E(KT['l_dv']), l_ty=E(KT['l_ty']), l_tr=E(KT['l_tr']), l_d=E(KT['l_d']),
           l_vat=E(KT['l_vat']), l_kvat=E(KT['l_kvat']),
           tick_tb=KT['tick_tb'], tick_bt=KT['tick_bt'], tick_kt=KT['tick_kt'],
           h_bang=E(KT['h_bang']), bang=_bang_dm_en(), bang_ghi=KT['bang_ghi'],
           h_nho=E(KT['h_nho']), nho=KT['nho'],
           h_sh2=E(KT['h_sh2']), sh2=KT['sh2'], sh3=E(KT['sh3']),
           h_bt=E(KT['h_bt']),
           bt=KT['bt'] % ('<a href="@/en/tu-van/index.html">%s</a>' % E(KT['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": KT['h1'], "description": KT['mt'], "inLanguage": "en"}]


# may tinh phi ban tieng Anh
B.than_js['en/kiem-toan'] = """
<script>
(function(){
 var MOC=[5,10,50,100,500,1000,10000],
     KT=[0.96,0.645,0.45,0.345,0.195,0.129,0.069],
     TT=[0.57,0.39,0.285,0.225,0.135,0.09,0.048];
 function tyLe(g,B){
  if(g<=MOC[0]) return {k:B[0], ct:'Value ≤ 5 billion — the rate is '+n(B[0])+'%'};
  if(g>=MOC[MOC.length-1]) return {k:B[B.length-1], ct:'Value ≥ 10,000 billion — the rate is '+n(B[B.length-1])+'%'};
  for(var i=0;i<MOC.length-1;i++){ if(g>=MOC[i]&&g<=MOC[i+1]){
    var Gb=MOC[i],Ga=MOC[i+1],Kb=B[i],Ka=B[i+1];
    var Ki=Kb-((Kb-Ka)*(g-Gb))/(Ga-Gb);
    return {k:Ki, ct:'Ki = '+n(Kb)+' − ('+n(Kb)+'−'+n(Ka)+')×('+n(g)+'−'+Gb+')÷('+Ga+'−'+Gb+') = '+n(Ki)+'%'};}}
  return {k:B[B.length-1], ct:''};}
 function n(x){ return String(Math.round(x*10000)/10000); }
 function tien(x){ return Math.round(x).toLocaleString('en-GB')+' VND'; }
 var g=document.getElementById('pg'),dv=document.getElementById('pdv'),
     vat=document.getElementById('pvat'),tb=document.getElementById('ptb'),
     bt=document.getElementById('pbt'),kt=document.getElementById('pkt'),
     kq=document.getElementById('pkq');
 function tinh(){
  var so=parseFloat(g.value),hs=parseFloat(dv.value);
  if(!(so>0)){ kq.innerHTML='<p class="loi">Please enter a value greater than zero.</p>'; return; }
  var dong=so*hs, ty=dong/1e9, a=tyLe(ty,KT), b=tyLe(ty,TT), he=1, mo=[];
  if(tb.checked){ he*=0.7; mo.push('×70% — equipment ≥ 50%'); }
  if(bt.checked){ he*=0.5; mo.push('×50% — compensation and resettlement'); }
  var pkt=dong*a.k/100*he, chan=false;
  if(pkt<1000000){ pkt=1000000; chan=true; }
  var tvat=parseFloat(vat.value)/100, thue=pkt*tvat, tong=pkt+thue;
  var ptt=dong*b.k/100*he; if(kt.checked) ptt*=0.5;
  var chan2=false; if(ptt<500000){ ptt=500000; chan2=true; }
  kq.innerHTML=
   '<div class="dong"><span>Value used for the fee</span><span>'+tien(dong)+'</span></div>'+
   '<div class="dong"><span>Rate applied</span><span>'+n(a.k)+'%</span></div>'+
   (mo.length?'<div class="dong"><span>Adjustment factor</span><span>'+mo.join(' · ')+'</span></div>':'')+
   '<div class="dong"><span>Audit fee before tax</span><span>'+tien(pkt)+(chan?' *':'')+'</span></div>'+
   '<div class="dong"><span>Value added tax '+(tvat*100)+'%</span><span>'+tien(thue)+'</span></div>'+
   '<div class="to"><span class="nhan">Maximum audit fee</span><div class="so">'+tien(tong)+'</div>'+
     '<div class="phu">Value added tax included</div></div>'+
   '<div class="cthuc">'+a.ct+'</div>'+
   (chan?'<p class="small" style="margin-top:9px">* The minimum of 1,000,000 VND under point b, clause 1, Article 20 has been applied.</p>':'')+
   '<div class="dong" style="margin-top:15px;padding-top:13px;border-top:1px solid var(--vien)">'+
     '<span>Settlement verification fee</span><span>'+tien(ptt)+(chan2?' *':'')+'</span></div>'+
   '<p class="small" style="margin-top:6px;margin-bottom:0">Collected by the verifying authority, '+
     'not paid to the auditor. No value added tax is added.</p>';
 }
 [g,dv,vat,tb,bt,kt].forEach(function(e){ e.addEventListener('input',tinh); e.addEventListener('change',tinh); });
 tinh();
})();
</script>"""


# ============================================================ 3. TU VAN
def trang_tu_van():
    NH = ('nh-nhanh', 'nh-sau', 'nh-cham')
    ba = ''.join('<div class="b"><span class="nh %s">%s</span><h3>%s</h3><p>%s</p>'
                 '<div class="dm">%s</div></div>'
                 % (NH[i], E(a), E(b), E(c), d) for i, (a, b, c, d) in enumerate(TV['ba']))
    the = ''.join(V15._the(d, i + 1, 'en') for i, d in enumerate(V14.DICH_VU)) \
        if hasattr(V14, 'DICH_VU') else ''
    nen = ''.join('<li>%s</li>' % E(x) for x in TV['nen'])

    def sel(idd, nhan, cac):
        return ('<div class="truong"><label for="%s">%s</label><select id="%s">'
                '<option value="">%s</option>%s</select></div>'
                % (idd, E(nhan), idd, E(TV['f_chon']),
                   ''.join('<option>%s</option>' % E(x) for x in cac)))

    than = _banner(TV['duong'], TV['h1'], E(TV['lede'])) + """
<div class="than"><div class="wrap">

  <h2 style="margin-bottom:12px">%(h_ba)s</h2>
  <div class="kenh">%(ba)s</div>

  <h2 style="margin:34px 0 6px">%(h_dv)s</h2>
  <p style="margin-bottom:4px">%(dv_lede)s</p>
  <p class="small" style="margin-bottom:6px">%(dv_ghi)s</p>
  <div class="dv-luoi">%(the)s</div>

  <div class="cot2">
    <div>
      <h2 style="margin-bottom:12px">%(h_mau)s</h2>
      <div class="mau">
        <form class="mau-luoi" id="mau" novalidate>
          <div class="truong"><label for="t1">%(f_ten)s <span style="color:var(--do)">*</span></label><input id="t1" type="text" required></div>
          <div class="truong"><label for="t2">%(f_cv)s</label><input id="t2" type="text"></div>
          <div class="truong"><label for="t3">%(f_dv)s <span style="color:var(--do)">*</span></label><input id="t3" type="text" required></div>
          <div class="truong"><label for="t4">%(f_dt)s <span style="color:var(--do)">*</span></label><input id="t4" type="tel" required></div>
          <div class="truong"><label for="t5">%(f_em)s</label><input id="t5" type="email"></div>
          %(s_db)s
          %(s_gd)s
          %(s_nh)s
          %(s_loai)s
          <div class="truong rong"><label for="t9">%(f_mo)s <span style="color:var(--do)">*</span></label>
            <textarea id="t9" required placeholder="%(f_mo_gy)s"></textarea></div>
          <div class="rong">
            <button class="nut-gui" type="submit">%(f_gui)s</button>
            <p class="small" id="kq" style="margin-top:11px"></p>
          </div>
        </form>
      </div>
    </div>

    <div class="hop-ben">
      <h3>%(h_nen)s</h3>
      <ul>%(nen)s</ul>
      <h3 style="margin-top:18px">%(h_bm)s</h3>
      <p>%(bm)s</p>
      <h3 style="margin-top:18px">%(h_kh)s</h3>
      <p>%(kh)s</p>
    </div>
  </div>

</div></div>
""" % dict(h_ba=E(TV['h_ba']), ba=ba,
           h_dv=E(TV['h_dv']), dv_lede=E(TV['dv_lede']),
           dv_ghi=TV['dv_ghi'] % ('<a href="@/en/dich-vu/index.html">%s</a>' % E(TV['dv_lk'])),
           the=the,
           h_mau=E(TV['h_mau']),
           f_ten=E(TV['f_ten']), f_cv=E(TV['f_cv']), f_dv=E(TV['f_dv']),
           f_dt=E(TV['f_dt']), f_em=E(TV['f_em']),
           s_db=sel('t6', TV['f_db'], TV['db']), s_gd=sel('t7', TV['f_gd'], TV['gd']),
           s_nh=sel('t8', TV['f_nh'], TV['nh']), s_loai=sel('t10', TV['f_loai'], TV['loai']),
           f_mo=E(TV['f_mo']), f_mo_gy=E(TV['f_mo_gy']), f_gui=E(TV['f_gui']),
           h_nen=E(TV['h_nen']), nen=nen,
           h_bm=E(TV['h_bm']), bm=E(TV['bm']),
           h_kh=E(TV['h_kh']), kh=E(TV['kh']))
    return than, [{"@context": "https://schema.org", "@type": "ContactPage",
                   "name": TV['h1'], "description": TV['mt'], "inLanguage": "en"}]


B.than_js['en/tu-van'] = B.than_js.get('tu-van', '')


# ============================================================ 4. LIEN HE
def trang_lien_he():
    NH = ('nh-nhanh', 'nh-sau', 'nh-cham')
    kh = []
    for i, (nhan, ten, mo, dm, lk) in enumerate(LH['ba']):
        them = ''
        if i == 0:
            them = ('<p style="margin-top:10px"><a href="@/en/tu-van/index.html" '
                    'style="font-weight:700">%s</a></p>' % E(lk))
        elif i == 1:
            them = ('<p style="margin-top:10px;font-size:20px;font-weight:700;color:var(--muc)">'
                    '08 2509 2007</p><p class="small">%s</p>' % LH['dt_ghi'])
        else:
            them = ('<p class="small" style="margin-top:10px">%s</p>'
                    % (LH['dl_ghi'] % ('<a href="@/en/tu-van/index.html">%s</a>' % E(LH['dl_lk']))))
        kh.append('<div class="b"><span class="nh %s">%s</span><h3>%s</h3><p>%s</p>'
                  '<div class="dm">%s</div>%s</div>'
                  % (NH[i], E(nhan), E(ten), E(mo), dm, them))

    ch = ''.join('<tr><td>%s</td><td><b>%s</b></td><td>%s</td></tr>' % (E(a), E(b), E(c))
                 for a, b, c in LH['chon'])
    fa = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (E(a), E(b))
                 for a, b in LH['fa'])

    than = _banner(LH['duong'], LH['h1'], E(LH['lede'])) + """
<div class="than"><div class="wrap">

  <h2 style="margin-bottom:12px">%(h_ba)s</h2>
  <div class="kenh">%(kh)s</div>

  <div class="luoi g2" style="margin-top:26px">
    <div class="the" style="border-left:3px solid var(--muc)">
      <h3>%(h_ts)s</h3>
      <p style="margin-top:8px"><b>%(ts_ten)s</b><br>%(ts)s</p>
    </div>
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>%(h_tt)s</h3>
      <p style="margin-top:8px">%(tt)s</p>
    </div>
  </div>

  <h2 style="margin:34px 0 12px">%(h_chon)s</h2>
  <div class="bang-boc"><table>
    <thead><tr><th style="width:40%%">%(c1)s</th><th style="width:20%%">%(c2)s</th>
    <th>%(c3)s</th></tr></thead>
    <tbody>%(ch)s</tbody>
  </table></div>

  <h2 style="margin:34px 0 12px">%(h_fa)s</h2>
  %(fa)s

  <div class="the" style="border-left:3px solid var(--nhan);margin-top:22px">
    <h3>%(h_bm)s</h3><p style="margin-top:8px">%(bm)s</p>
  </div>

</div></div>
""" % dict(h_ba=E(LH['h_ba']), kh=''.join(kh),
           h_ts=E(LH['h_ts']), ts_ten=E(LH['ts_ten']), ts=LH['ts'],
           h_tt=E(LH['h_tt']), tt=E(LH['tt']),
           h_chon=E(LH['h_chon']), c1=E(LH['chon_cot'][0]), c2=E(LH['chon_cot'][1]),
           c3=E(LH['chon_cot'][2]), ch=ch,
           h_fa=E(LH['h_fa']), fa=fa,
           h_bm=E(LH['h_bm']), bm=E(LH['bm']))
    return than, [{"@context": "https://schema.org", "@type": "ContactPage",
                   "name": LH['h1'], "description": LH['mt'], "inLanguage": "en"}]


# ============================================================ khung
_V15_KHUNG = V15.khung
_NAV = re.compile(r'<nav class="top-nav" id="dhuong">.*?</nav>', re.S)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V15_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang != 'en':
        return h
    goc = V12._goc(slug)
    m = _NAV.search(h)
    nav = m.group(0)
    for c in CHU_DE:
        cu = 'href="%s%s/index.html"' % (goc, c)
        moi = 'href="%sen/%s/index.html"' % (goc, c)
        nav = nav.replace('hreflang="vi" title="page in Vietnamese" class="vi-dich" ' + cu, moi)
        nav = nav.replace('hreflang="vi" title="page in Vietnamese" class="vi-dich nut-lh" ' + cu,
                          'class="nut-lh" ' + moi)
        nav = nav.replace(cu, moi)
    return h[:m.start()] + nav + h[m.end():]


B.khung = khung

TRANG = list(V15.TRANG) + [
    ('en/quy-trinh', 'en', QT['td'], QT['mt'], trang_quy_trinh, 'trong'),
    ('en/kiem-toan', 'en', KT['td'], KT['mt'], trang_kiem_toan, 'trong'),
    ('en/tu-van', 'en', TV['td'], TV['mt'], trang_tu_van, 'trong'),
    ('en/lien-he', 'en', LH['td'], LH['mt'], trang_lien_he, 'trong'),
]


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
