# -*- coding: utf-8 -*-
"""Ban 22 — TRON BO TIENG DUC TRONG MOT LAN. 17 trang.  Trang **80 -> 97**.

/de/quy-trinh/ /de/kiem-toan/ /de/tu-van/ /de/lien-he/ + chan trang tieng Duc
9 trang /de/dich-vu/<slug>/ + /de/van-ban/ /de/thu-vien-rui-ro/ /de/kinh-nghiem/ /de/vuong-mac/

Khac hai bo truoc: tieng Anh lam 4 dot (ban 14-17), tieng Trung 2 dot (18-19),
tieng Nhat 2 dot (20-21). Bo tieng Duc gop TRON trong mot ban vi khuon da chin han.

⚠ KE THUA BAN LIEN TRUOC (ds_v21) — ban 20 da vap loi ke thua nham va roi mat 13 trang
  khoi sitemap. Kiem nhanh: "Da ghi N trang" phai = 80 + 17 = 97.

🔴🔴 BAY DON VI TIEN NGUY HIEM NHAT CUA TIENG DUC:
  **"Billion" tieng Duc = 10^12**, KHONG phai 10^9 nhu tieng Anh.
  1 ty dong  = 1 Milliarde VND   (KHONG phai 1 Billion VND — sai 1.000 lan)
  5 ty dong  = 5 Milliarden VND
  1.000 ty   = 1 Billion VND
  10.000 ty  = 10 Billionen VND
  Ban tieng Anh dung "Billion VND" nghia la TY — dich thang sang Duc la sai 1.000 lan.

⚠ Dau thap phan tieng Duc la DAU PHAY. Ham n() trong khoi JS phai doi '.' thanh ','.

⚠ MOI THU TIENG MOT KHOI JS RIENG — dung va chuoi JS cua ban tieng khac.
"""
import io, json, os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages2 as P2
import ds_v7 as V7
import ds_v8 as V8
import ds_v9 as V9
import ds_v12 as V12
import ds_v13 as V13
import ds_v14 as V14
import ds_v17 as V17
import ds_v21 as V21
from ds_dv import DICH_VU, NHOM
from ds_en_kn import CHAN
from ds_de_qt import QT, QT_GD, QT_NGAN, QT_HO, KT, KT_VS, KT_SS, KT_PH, KT_CD, KT_KL
from ds_de_tv import TV, LH, CHAN_DE
from ds_de_dv import DE, KHUNG
from ds_de_rr import VB, CAP_DE, DIA_DE, RR, RR_NHOM
from ds_de_kn import KN, KN_BH, KN_SL, KN_KT, VM, VM_DS

TM = os.path.dirname(os.path.abspath(__file__))
DL = json.load(io.open(os.path.join(TM, 'vb_phanloai.json'), encoding='utf-8'))
E = html.escape

CHU_DE = ['quy-trinh', 'kiem-toan', 'tu-van', 'lien-he',
          'van-ban', 'thu-vien-rui-ro', 'kinh-nghiem', 'vuong-mac']
for _c in CHU_DE:
    V14.DA_DICH[_c] = V14.DA_DICH.get(_c, set()) | {'de'}
for _d in DICH_VU:
    V14.DA_DICH['dich-vu/' + _d['slug']] = V14.DA_DICH.get('dich-vu/' + _d['slug'], set()) | {'de'}

CHAN['de'] = CHAN_DE
V14.DICH_NHAC['de'] = ('Alle neun Leistungen haben auch eine <b>deutsche Fassung</b> der '
                       'Detailseite. Die zitierten Vorschriften bleiben auf Vietnamesisch — '
                       'nur dieser Wortlaut ist rechtsverbindlich.')

# Nhan "N phần" cho ban tieng Duc — ghi vao bang cua ban 21.
V21._NHAN_PHAN['de'] = '%d Teile'


def _tep_de(d):
    return V21._tep_lang(d, 'de')


def _banner(ten, h1, lede):
    return ("""
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/de/index.html">Start</a> · %s</div>
  <h1>%s</h1>
  <p>%s</p>
</div></div>
""" % (E(ten), E(h1), E(lede)))


# ============================================================ 1. QUY TRINH
def trang_quy_trinh():
    gd = ''.join("""<div class="b">
  <h3>%s</h3>
  <p style="margin:7px 0 0;font-size:15.3px;color:var(--chu2)">%s</p>
  <div class="ct">
    <div><b>%s</b>%s</div><div><b>%s</b>%s</div>
    <div><b>%s</b>%s</div><div><b>%s</b><span style="color:var(--do)">%s</span></div>
  </div>
</div>""" % (E(ten), E(viec), E(QT['l_tq']), E(tq), E(QT['l_cc']), E(cc),
             E(QT['l_kq']), E(kq), E(QT['l_bay']), E(bay))
        for ten, viec, tq, cc, kq, bay in QT_GD)

    LOP = {'ngoc': 'tl-luat', 'do': 'tl-khac', 'nhan': 'tl-nd', 'muc': 'tl-tt'}
    ng = ''.join('<tr><td><span class="the-loc %s" style="font-size:13px">Strang %s</span></td>'
                 '<td><b>%s</b></td><td>%s</td><td>%s</td></tr>'
                 % (LOP[mau], E(ma), E(ten), E(pv), E(vb)) for ma, ten, pv, vb, mau in QT_NGAN)
    ho = ''.join('<div class="the" style="border-left:3px solid var(--do)">'
                 '<h3>%s</h3><p style="margin-top:8px">%s</p></div>' % (E(a), E(b))
                 for a, b in QT_HO)

    than = _banner(QT['duong'], QT['h1'], QT['lede']) + """
<div class="than"><div class="wrap">
  <h2 style="margin-bottom:14px">%(h_gd)s</h2>
  <div class="gd">%(gd)s</div>

  <h2 style="margin:34px 0 8px">%(h_ngan)s</h2>
  <p style="margin-bottom:14px">%(ngan_lede)s</p>
  <div class="bang-boc"><table>
    <thead><tr><th style="width:118px">Strang</th><th style="width:26%%">Art des Vorhabens</th>
    <th style="width:22%%">%(l_pv)s</th><th>%(l_vb)s</th></tr></thead>
    <tbody>%(ngan)s</tbody></table></div>

  <h2 style="margin:34px 0 8px">%(h_ho)s</h2>
  <p style="margin-bottom:14px">%(ho_lede)s</p>
  <div class="luoi g3">%(ho)s</div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>%(h_ke)s</h3><p style="margin-top:8px">%(ke)s</p>
  </div>
</div></div>
""" % dict(h_gd=E(QT['h_gd']), gd=gd, h_ngan=E(QT['h_ngan']), ngan_lede=E(QT['ngan_lede']),
           l_pv=E(QT['l_pv']), l_vb=E(QT['l_vb']), ngan=ng,
           h_ho=E(QT['h_ho']), ho_lede=E(QT['ho_lede']), ho=ho, h_ke=E(QT['h_ke']),
           ke=QT['ke'] % ('<a href="@/de/kiem-toan/index.html">%s</a>' % E(QT['ke_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": QT['h1'], "description": QT['mt'], "inLanguage": "de"}]


# ============================================================ 2. KIEM TOAN QT
def _bang_dm_de():
    moc = ['≤ 5', '10', '50', '100', '500', '1.000', '≥ 10.000']

    def hang(n, ds):
        return ('<tr><td><b>%s</b></td>%s</tr>'
                % (n, ''.join('<td class="n">%s</td>' % str(x).replace('.', ',') for x in ds)))
    return """<div class="bang-boc"><table class="bang-dm">
    <thead><tr><th style="width:32%%">%s</th>%s</tr></thead>
    <tbody>%s%s</tbody></table></div>""" % (
        E(KT['bang_gt']), ''.join('<th class="n">%s</th>' % m for m in moc),
        hang(E(KT['bang_kt']), V9.KT), hang(E(KT['bang_tt']), V9.TT))


def trang_kiem_toan():
    vs = ''.join('<div class="the" style="border-left:3px solid var(--nhan);margin-bottom:13px">'
                 '<h3>%d. %s</h3><p style="margin-top:8px">%s</p></div>' % (i + 1, E(a), E(b))
                 for i, (a, b) in enumerate(KT_VS))
    ss = ''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (E(a), E(b), E(c))
                 for a, b, c in KT_SS)
    ph = ''.join('<div class="b"><div class="ma">%s</div><div><h3>%s</h3><p>%s</p>'
                 '<div class="luuy">%s</div></div></div>' % (E(m), E(t), E(n), E(l))
                 for m, t, n, l in KT_PH)
    cd = ''.join('<div class="the" style="border-left:3px solid var(--ngoc)">'
                 '<h3>%s</h3><p style="margin-top:8px"><code>%s</code></p><p>%s</p></div>'
                 % (E(a), E(b), E(c)) for a, b, c in KT_CD)
    kl = ''.join('<div class="the" style="border-left:3px solid var(--do)">'
                 '<h3>%s</h3><p style="margin-top:8px">%s</p></div>' % (E(a), E(b))
                 for a, b in KT_KL)

    than = _banner(KT['duong'], KT['h1'], KT['lede']) + """
<div class="than"><div class="wrap">
  <div class="the" style="border-left:3px solid var(--muc3)">
    <h3>%(h_sh)s</h3><p style="margin-top:8px">%(sh)s</p></div>

  <h2 style="margin:32px 0 12px">%(h_vs)s</h2>
  %(vs)s

  <h2 style="margin:32px 0 12px">%(h_ss)s</h2>
  <div class="bang-boc"><table>
    <thead><tr><th style="width:24%%"></th><th>%(c1)s</th><th>%(c2)s</th></tr></thead>
    <tbody>%(ss)s</tbody></table></div>

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

  <div class="mtp"><div class="mtp-luoi">
    <div>
      <div class="o"><label for="pg">%(l_gt)s<span class="phu">%(l_gt_phu)s</span></label>
        <input id="pg" type="number" min="0" step="0.1" value="120" inputmode="decimal"></div>
      <div class="o"><label for="pdv">%(l_dv)s</label><select id="pdv">
        <option value="1000000000" selected>%(l_ty)s</option>
        <option value="1000000">%(l_tr)s</option><option value="1">%(l_d)s</option></select></div>
      <div class="o"><label for="pvat">%(l_vat)s</label><select id="pvat">
        <option value="10" selected>10%%</option><option value="8">8%%</option>
        <option value="0">%(l_kvat)s</option></select></div>
      <label class="tick"><input type="checkbox" id="ptb"><span>%(tick_tb)s</span></label>
      <label class="tick"><input type="checkbox" id="pbt"><span>%(tick_bt)s</span></label>
      <label class="tick"><input type="checkbox" id="pkt"><span>%(tick_kt)s</span></label>
    </div>
    <div class="kq" id="pkq"></div>
  </div></div>

  <h3 style="margin:26px 0 8px">%(h_bang)s</h3>
  %(bang)s
  <p class="small">%(bang_ghi)s</p>

  <div class="luoi g2" style="margin-top:20px">
    <div class="the" style="border-left:3px solid var(--do)">
      <h3>%(h_nho)s</h3><p style="margin-top:8px">%(nho)s</p></div>
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>%(h_sh2)s</h3><p style="margin-top:8px">%(sh2)s</p><p>%(sh3)s</p></div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>%(h_bt)s</h3><p style="margin-top:8px">%(bt)s</p></div>
</div></div>
""" % dict(h_sh=E(KT['h_sh']), sh=E(KT['sh']), h_vs=E(KT['h_vs']), vs=vs,
           h_ss=E(KT['h_ss']), c1=E(KT['ss_cot'][1]), c2=E(KT['ss_cot'][2]), ss=ss,
           h_ph=E(KT['h_ph']), ph_lede=E(KT['ph_lede']), ph=ph,
           h_cd=E(KT['h_cd']), cd_lede=E(KT['cd_lede']), cd=cd,
           h_kl=E(KT['h_kl']), kl=kl,
           h_phi=E(KT['h_phi']), phi_1=KT['phi_1'], phi_2=KT['phi_2'],
           l_gt=E(KT['l_gt']), l_gt_phu=E(KT['l_gt_phu']), l_dv=E(KT['l_dv']),
           l_ty=E(KT['l_ty']), l_tr=E(KT['l_tr']), l_d=E(KT['l_d']),
           l_vat=E(KT['l_vat']), l_kvat=E(KT['l_kvat']),
           tick_tb=KT['tick_tb'], tick_bt=KT['tick_bt'], tick_kt=KT['tick_kt'],
           h_bang=E(KT['h_bang']), bang=_bang_dm_de(), bang_ghi=KT['bang_ghi'],
           h_nho=E(KT['h_nho']), nho=KT['nho'],
           h_sh2=E(KT['h_sh2']), sh2=KT['sh2'], sh3=E(KT['sh3']), h_bt=E(KT['h_bt']),
           bt=KT['bt'] % ('<a href="@/de/tu-van/index.html">%s</a>' % E(KT['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": KT['h1'], "description": KT['mt'], "inLanguage": "de"}]


# May tinh phi ban TIENG DUC — khoi JS RIENG.
# 🔴 5 ty = "5 Milliarden VND" · 10.000 ty = "10 Billionen VND" (Billion Duc = 10^12).
# ⚠ n() doi dau cham thap phan thanh dau phay theo cach viet Duc.
B.than_js['de/kiem-toan'] = """
<script>
(function(){
 var MOC=[5,10,50,100,500,1000,10000],
     KT=[0.96,0.645,0.45,0.345,0.195,0.129,0.069],
     TT=[0.57,0.39,0.285,0.225,0.135,0.09,0.048];
 function tyLe(g,B){
  if(g<=MOC[0]) return {k:B[0], ct:'Prüfungsgegenstand ≤ 5 Milliarden VND — Satz '+n(B[0])+' %'};
  if(g>=MOC[MOC.length-1]) return {k:B[B.length-1], ct:'Prüfungsgegenstand ≥ 10 Billionen VND — Satz '+n(B[B.length-1])+' %'};
  for(var i=0;i<MOC.length-1;i++){ if(g>=MOC[i]&&g<=MOC[i+1]){
    var Gb=MOC[i],Ga=MOC[i+1],Kb=B[i],Ka=B[i+1];
    var Ki=Kb-((Kb-Ka)*(g-Gb))/(Ga-Gb);
    return {k:Ki, ct:'Ki = '+n(Kb)+' − ('+n(Kb)+'−'+n(Ka)+')×('+n(g)+'−'+n(Gb)+')÷('+n(Ga)+'−'+n(Gb)+') = '+n(Ki)+' %'};}}
  return {k:B[B.length-1], ct:''};}
 function n(x){ return String(Math.round(x*10000)/10000).replace('.',','); }
 function tien(x){ return Math.round(x).toLocaleString('de-DE')+' VND'; }
 var g=document.getElementById('pg'),dv=document.getElementById('pdv'),
     vat=document.getElementById('pvat'),tb=document.getElementById('ptb'),
     bt=document.getElementById('pbt'),kt=document.getElementById('pkt'),
     kq=document.getElementById('pkq');
 function tinh(){
  var so=parseFloat(g.value),hs=parseFloat(dv.value);
  if(!(so>0)){ kq.innerHTML='<p class="loi">Bitte geben Sie einen Wert größer als null ein.</p>'; return; }
  var dong=so*hs, ty=dong/1e9, a=tyLe(ty,KT), b=tyLe(ty,TT), he=1, mo=[];
  if(tb.checked){ he*=0.7; mo.push('×70 % — Geräteanteil ≥ 50 %'); }
  if(bt.checked){ he*=0.5; mo.push('×50 % — Entschädigung und Umsiedlung'); }
  var pkt=dong*a.k/100*he, chan=false;
  if(pkt<1000000){ pkt=1000000; chan=true; }
  var tvat=parseFloat(vat.value)/100, thue=pkt*tvat, tong=pkt+thue;
  var ptt=dong*b.k/100*he; if(kt.checked) ptt*=0.5;
  var chan2=false; if(ptt<500000){ ptt=500000; chan2=true; }
  kq.innerHTML=
   '<div class="dong"><span>Bemessungsgrundlage</span><span>'+tien(dong)+'</span></div>'+
   '<div class="dong"><span>Angewandter Satz</span><span>'+n(a.k)+' %</span></div>'+
   (mo.length?'<div class="dong"><span>Anpassungsfaktor</span><span>'+mo.join(' · ')+'</span></div>':'')+
   '<div class="dong"><span>Prüfungshonorar ohne Steuer</span><span>'+tien(pkt)+(chan?' *':'')+'</span></div>'+
   '<div class="dong"><span>Umsatzsteuer '+n(tvat*100)+' %</span><span>'+tien(thue)+'</span></div>'+
   '<div class="to"><span class="nhan">Höchstbetrag des Prüfungshonorars</span><div class="so">'+tien(tong)+'</div>'+
     '<div class="phu">einschließlich Umsatzsteuer</div></div>'+
   '<div class="cthuc">'+a.ct+'</div>'+
   (chan?'<p class="small" style="margin-top:9px">* Der Mindestbetrag von 1 Million VND nach Artikel 20 Absatz 1 Buchstabe b wurde angewandt.</p>':'')+
   '<div class="dong" style="margin-top:15px;padding-top:13px;border-top:1px solid var(--vien)">'+
     '<span>Gebühr für Nachprüfung und Genehmigung</span><span>'+tien(ptt)+(chan2?' *':'')+'</span></div>'+
   '<p class="small" style="margin-top:6px;margin-bottom:0">Diese Gebühr erhebt die nachprüfende '+
     'Behörde — sie ist kein an die Prüferin oder den Prüfer zu zahlendes Honorar, und '+
     'Umsatzsteuer wird darauf nicht erhoben.</p>';
 }
 [g,dv,vat,tb,bt,kt].forEach(function(e){ e.addEventListener('input',tinh); e.addEventListener('change',tinh); });
 tinh();
})();
</script>"""


# ============================================================ 3. TU VAN
def trang_tu_van():
    NH = ('nh-nhanh', 'nh-sau', 'nh-cham')
    ba = ''.join('<div class="b"><span class="nh %s">%s</span><h3>%s</h3><p>%s</p>'
                 '<div class="dm">%s</div></div>' % (NH[i], E(a), E(b), E(c), d)
                 for i, (a, b, c, d) in enumerate(TV['ba']))
    the = ''.join(V17.V16.V15._the(d, i + 1, 'de') for i, d in enumerate(V14.DICH_VU))
    nen = ''.join('<li>%s</li>' % E(x) for x in TV['nen'])

    def sel(idd, nhan, cac):
        return ('<div class="truong"><label for="%s">%s</label><select id="%s">'
                '<option value="">%s</option>%s</select></div>'
                % (idd, E(nhan), idd, E(TV['f_chon']),
                   ''.join('<option>%s</option>' % E(x) for x in cac)))

    than = _banner(TV['duong'], TV['h1'], TV['lede']) + """
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
      <div class="mau"><form class="mau-luoi" id="mau" novalidate>
        <div class="truong"><label for="t1">%(f_ten)s <span style="color:var(--do)">*</span></label><input id="t1" type="text" required></div>
        <div class="truong"><label for="t2">%(f_cv)s</label><input id="t2" type="text"></div>
        <div class="truong"><label for="t3">%(f_dv)s <span style="color:var(--do)">*</span></label><input id="t3" type="text" required></div>
        <div class="truong"><label for="t4">%(f_dt)s <span style="color:var(--do)">*</span></label><input id="t4" type="tel" required></div>
        <div class="truong"><label for="t5">%(f_em)s</label><input id="t5" type="email"></div>
        %(s_db)s %(s_gd)s %(s_nh)s %(s_loai)s
        <div class="truong rong"><label for="t9">%(f_mo)s <span style="color:var(--do)">*</span></label>
          <textarea id="t9" required placeholder="%(f_mo_gy)s"></textarea></div>
        <div class="rong"><button class="nut-gui" type="submit">%(f_gui)s</button>
          <p class="small" id="kq" style="margin-top:11px"></p></div>
      </form></div>
    </div>
    <div class="hop-ben">
      <h3>%(h_nen)s</h3><ul>%(nen)s</ul>
      <h3 style="margin-top:18px">%(h_bm)s</h3><p>%(bm)s</p>
      <h3 style="margin-top:18px">%(h_kh)s</h3><p>%(kh)s</p>
    </div>
  </div>
</div></div>
""" % dict(h_ba=E(TV['h_ba']), ba=ba, h_dv=E(TV['h_dv']), dv_lede=E(TV['dv_lede']),
           dv_ghi=TV['dv_ghi'] % ('<a href="@/de/dich-vu/index.html">%s</a>' % E(TV['dv_lk'])),
           the=the, h_mau=E(TV['h_mau']),
           f_ten=E(TV['f_ten']), f_cv=E(TV['f_cv']), f_dv=E(TV['f_dv']),
           f_dt=E(TV['f_dt']), f_em=E(TV['f_em']),
           s_db=sel('t6', TV['f_db'], TV['db']), s_gd=sel('t7', TV['f_gd'], TV['gd']),
           s_nh=sel('t8', TV['f_nh'], TV['nh']), s_loai=sel('t10', TV['f_loai'], TV['loai']),
           f_mo=E(TV['f_mo']), f_mo_gy=E(TV['f_mo_gy']), f_gui=E(TV['f_gui']),
           h_nen=E(TV['h_nen']), nen=nen, h_bm=E(TV['h_bm']), bm=E(TV['bm']),
           h_kh=E(TV['h_kh']), kh=E(TV['kh']))
    return than, [{"@context": "https://schema.org", "@type": "ContactPage",
                   "name": TV['h1'], "description": TV['mt'], "inLanguage": "de"}]


# Bieu mau tieng Duc — khoi JS rieng, theo bang cua ban 20.
B.than_js['de/tu-van'] = V21.V20._JS_MAU % (
    "'Bitte füllen Sie Name, Organisation, Telefon und die Schilderung der Lage aus.'",
    "'Dieses Formular ist noch nicht an einen empfangenden Dienst angebunden. "
    "Bitte nutzen Sie die Angaben auf der Kontaktseite.'")


# ============================================================ 4. LIEN HE
def trang_lien_he():
    NH = ('nh-nhanh', 'nh-sau', 'nh-cham')
    kh = []
    for i, (nhan, ten, mo, dm, lk) in enumerate(LH['ba']):
        if i == 0:
            them = ('<p style="margin-top:10px"><a href="@/de/tu-van/index.html" '
                    'style="font-weight:700">%s</a></p>' % E(lk))
        elif i == 1:
            them = ('<p style="margin-top:10px;font-size:20px;font-weight:700;color:var(--muc)">'
                    '08 2509 2007</p><p class="small">%s</p>' % LH['dt_ghi'])
        else:
            them = ('<p class="small" style="margin-top:10px">%s</p>'
                    % (LH['dl_ghi'] % ('<a href="@/de/tu-van/index.html">%s</a>' % E(LH['dl_lk']))))
        kh.append('<div class="b"><span class="nh %s">%s</span><h3>%s</h3><p>%s</p>'
                  '<div class="dm">%s</div>%s</div>' % (NH[i], E(nhan), E(ten), E(mo), dm, them))
    ch = ''.join('<tr><td>%s</td><td><b>%s</b></td><td>%s</td></tr>' % (E(a), E(b), E(c))
                 for a, b, c in LH['chon'])
    fa = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (E(a), b)
                 for a, b in LH['fa'])

    than = _banner(LH['duong'], LH['h1'], LH['lede']) + """
<div class="than"><div class="wrap">
  <h2 style="margin-bottom:12px">%(h_ba)s</h2>
  <div class="kenh">%(kh)s</div>

  <div class="luoi g2" style="margin-top:26px">
    <div class="the" style="border-left:3px solid var(--muc)">
      <h3>%(h_ts)s</h3><p style="margin-top:8px"><b>%(ts_ten)s</b><br>%(ts)s</p></div>
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>%(h_tt)s</h3><p style="margin-top:8px">%(tt)s</p></div>
  </div>

  <h2 style="margin:34px 0 12px">%(h_chon)s</h2>
  <div class="bang-boc"><table>
    <thead><tr><th style="width:40%%">%(c1)s</th><th style="width:20%%">%(c2)s</th>
    <th>%(c3)s</th></tr></thead><tbody>%(ch)s</tbody></table></div>

  <h2 style="margin:34px 0 12px">%(h_fa)s</h2>
  %(fa)s

  <div class="the" style="border-left:3px solid var(--nhan);margin-top:22px">
    <h3>%(h_bm)s</h3><p style="margin-top:8px">%(bm)s</p></div>
</div></div>
""" % dict(h_ba=E(LH['h_ba']), kh=''.join(kh), h_ts=E(LH['h_ts']), ts_ten=E(LH['ts_ten']),
           ts=LH['ts'], h_tt=E(LH['h_tt']), tt=E(LH['tt']), h_chon=E(LH['h_chon']),
           c1=E(LH['chon_cot'][0]), c2=E(LH['chon_cot'][1]), c3=E(LH['chon_cot'][2]), ch=ch,
           h_fa=E(LH['h_fa']), fa=fa, h_bm=E(LH['h_bm']), bm=E(LH['bm']))
    return than, [{"@context": "https://schema.org", "@type": "ContactPage",
                   "name": LH['h1'], "description": LH['mt'], "inLanguage": "de"}]


# ============================================================ 9 trang dich vu
def _trang_dv_de(d):
    z = DE[d['slug']]
    K = KHUNG
    ten_nhom = V13.NHAN_NHOM[d['nhom']]['de']
    _, mau = NHOM[d['nhom']]

    def ds(items):
        return '<ul>%s</ul>' % ''.join('<li>%s</li>' % E(x) for x in items)

    cc = ''.join('<div class="dv-cc"><b>%s</b><span>%s</span></div>' % (E(a), E(b))
                 for a, b in z['can_cu'])
    bu = ''.join('<li><b>%s</b><span>%s</span></li>' % (E(a), E(b)) for a, b in z['lam_gi'])

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/de/index.html">%(nha)s</a> ·
    <a href="@/de/dich-vu/index.html">%(dv)s</a> · %(menu)s</div>
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
    <p class="small" style="margin-top:9px"><a href="@/de/dich-vu/index.html">%(bt_ve)s</a></p>
  </div>
</div></div>
""" % dict(nha=E(K['duong_nha']), dv=E(K['duong_dv']),
           menu=E(V13.NHAN_MUC_DV[d['slug']]['de']), nhom=E(ten_nhom), mau=mau,
           ten=E(z['ten']), lede=E(z['lede']),
           h_vande=E(K['h_vande']), vande=ds(z['van_de']),
           h_cancu=E(K['h_cancu']),
           cc_nhac=K['cancu_nhac'] % ('<a href="@/de/van-ban/index.html">%s</a>'
                                      % E(K['cancu_lk'])),
           cancu=cc, h_lamgi=E(K['h_lamgi']), buoc=bu,
           h_daura=E(K['h_daura']), daura=ds(z['dau_ra']),
           h_khinao=E(K['h_khinao']), khinao=E(z['khi_nao']),
           luu_h=E(K['luu_h']), luu=E(K['luu']), bt_h=E(K['bt_h']),
           bt=K['bt'] % ('<a href="@/de/tu-van/index.html">%s</a>' % E(K['bt_lk'])),
           bt_ve=E(K['bt_ve']))
    return than, [{"@context": "https://schema.org", "@type": "Service",
                   "name": z['ten'], "description": z['mt'], "serviceType": ten_nhom,
                   "areaServed": "VN", "inLanguage": "de",
                   "provider": {"@type": "Organization",
                                "name": "ASCO Prüfungs- und Bewertungsgesellschaft, Vietnam",
                                "telephone": "0825092007"}}]


# ============================================================ VAN BAN
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
        phu = ('<span class="phu">%s</span>' % E(DIA_DE.get(d['diaban'], d['diaban']))
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
               LOP[d['ngan']], E(CAP_DE[d['ngan']]), E(d.get('sohieu') or '—'),
               ten, hn, phu, d['nam'] or '—', tt, _tep_de(d)))

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
    <thead><tr><th style="width:132px">%(l_cap)s</th><th style="width:142px">%(l_so)s</th>
    <th>%(l_ten)s</th><th style="width:62px">%(l_nam)s</th>
    <th style="width:104px">%(l_hl)s</th><th style="width:130px">%(l_tep)s</th></tr></thead>
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
           o_cap=''.join('<option value="%s">%s</option>' % (E(k), E(v)) for k, v in CAP_DE.items()),
           o_dia=''.join('<option value="%s">%s</option>' % (E(k), E(v)) for k, v in DIA_DE.items()),
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
                   "name": VB['h1'], "description": VB['mt'], "inLanguage": "de"}]


# Bo loc ban TIENG DUC — khoi JS RIENG.
B.than_js['de/van-ban'] = """
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
  dem.innerHTML='<b>'+n+'</b> von '+tong+' Vorschriften';
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
                      '<p><b>%s.</b> %s</p><div class="luuy"><b>%s.</b> %s</div>'
                      '<p class="small" style="margin-top:6px;color:%s"><b>%s: %s</b></p>'
                      '</div></div>' % (stt, E(ten), E(RR['l_dh']), E(dh), E(RR['l_kt']), E(kt),
                                        MAU[muc], E(RR['l_muc']), E(RR['muc'][muc])))
        kh.append('<h3 style="margin:26px 0 4px;font-size:19px;color:var(--muc)">%s '
                  '<span class="small" style="font-weight:400">(%d)</span></h3>'
                  '<div class="gd">%s</div>' % (E(nhom), len(cac), ''.join(rr)))

    than = _banner(RR['duong'], RR['h1'], RR['lede']) + """
<div class="than"><div class="wrap">
  <div class="the" style="border-left:3px solid var(--do)">
    <h3>%(h_ng)s</h3><p style="margin-top:8px">%(ng)s</p></div>

  <h2 style="margin:30px 0 4px">%(h_ds)s <span class="small" style="font-weight:400">(33)</span></h2>
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
           bt=RR['bt'] % ('<a href="@/de/tu-van/index.html">%s</a>' % E(RR['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": RR['h1'], "description": RR['mt'], "inLanguage": "de"}]


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
           bt=KN['bt'] % ('<a href="@/de/dich-vu/ho-so-quyet-toan/index.html">%s</a>'
                          % E(KN['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": KN['h1'], "description": KN['mt'], "inLanguage": "de"}]


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
           bt=VM['bt'] % ('<a href="@/de/tu-van/index.html">%s</a>' % E(VM['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": VM['h1'], "description": VM['mt'], "inLanguage": "de"}]


# ============================================================ khung
_V21_KHUNG = V21.khung
_NAV = re.compile(r'<nav class="top-nav" id="dhuong">.*?</nav>', re.S)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V21_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang != 'de':
        return h
    goc = V12._goc(slug)
    m = _NAV.search(h)
    nav = m.group(0)
    nhac = V13.NHAC['de']
    cac = CHU_DE + ['dich-vu/' + d['slug'] for d in DICH_VU]
    for c in cac:
        cu = 'href="%s%s/index.html"' % (goc, c)
        moi = 'href="%sde/%s/index.html"' % (goc, c)
        nav = nav.replace('hreflang="vi" title="%s" class="vi-dich" ' % nhac + cu, moi)
        nav = nav.replace(cu, moi)
    h = h[:m.start()] + nav + h[m.end():]
    return V17._chan(h, 'de', goc)


B.khung = khung

TRANG = list(V21.TRANG) + [
    ('de/quy-trinh', 'de', QT['td'], QT['mt'], trang_quy_trinh, 'trong'),
    ('de/kiem-toan', 'de', KT['td'], KT['mt'], trang_kiem_toan, 'trong'),
    ('de/tu-van', 'de', TV['td'], TV['mt'], trang_tu_van, 'trong'),
    ('de/lien-he', 'de', LH['td'], LH['mt'], trang_lien_he, 'trong'),
] + [
    ('de/dich-vu/' + d['slug'], 'de', DE[d['slug']]['td'], DE[d['slug']]['mt'],
     (lambda dd: (lambda: _trang_dv_de(dd)))(d), 'trong')
    for d in DICH_VU
] + [
    ('de/van-ban', 'de', VB['td'], VB['mt'], trang_van_ban, 'trong'),
    ('de/thu-vien-rui-ro', 'de', RR['td'], RR['mt'], trang_rui_ro, 'trong'),
    ('de/kinh-nghiem', 'de', KN['td'], KN['mt'], trang_kinh_nghiem, 'trong'),
    ('de/vuong-mac', 'de', VM['td'], VM['mt'], trang_vuong_mac, 'trong'),
]


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
