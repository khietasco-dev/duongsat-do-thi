# -*- coding: utf-8 -*-
"""Ban 20 — BON TRANG TIENG NHAT + CHAN TRANG (dot 1 cua bo tieng Nhat).

/ja/quy-trinh/ · /ja/kiem-toan/ · /ja/tu-van/ · /ja/lien-he/  -> trang 63 -> 67.

⚠ DON VI TIEN TIENG NHAT — giong bay da vap o ban tieng Trung:
  億 = 100 TRIEU (khong phai ty) · 兆 = 10^12
  1 ty dong = 十億ドン · 5 ty = 50億ドン · 1.000 ty = 1兆ドン · 10.000 ty = 10兆ドン

⚠ MOI THU TIENG MOT KHOI JS RIENG — dung va chuoi JS cua ban tieng khac.

🔧 SUA LUON MOT LOI CU: khoi JS bieu mau trang Tu van (`B.than_js['tu-van']`) chua hai
   cau THONG BAO TIENG VIET, va ban 17 gan nguyen khoi do cho 'en/tu-van', ban 18 gan
   cho 'zh/tu-van'. Nghia la nguoi doc tieng Anh / tieng Trung bam Gui se thay tieng Viet.
   Ban nay sinh khoi JS theo tung thu tieng va gan lai cho ca en, zh, ja.
"""
import os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v7 as V7
import ds_v9 as V9
import ds_v12 as V12
import ds_v13 as V13
import ds_v14 as V14
import ds_v17 as V17
import ds_v18 as V18
import ds_v19 as V19
from ds_en_kn import CHAN
from ds_ja_qt import QT, QT_GD, QT_NGAN, QT_HO, KT, KT_VS, KT_SS, KT_PH, KT_CD, KT_KL
from ds_ja_tv import TV, LH, CHAN_JA

E = html.escape
CHU_DE = ['quy-trinh', 'kiem-toan', 'tu-van', 'lien-he']
for _c in CHU_DE:
    V14.DA_DICH[_c] = V14.DA_DICH.get(_c, set()) | {'ja'}
CHAN['ja'] = CHAN_JA


def _banner(ten, h1, lede):
    return ("""
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/ja/index.html">ホーム</a> · %s</div>
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
    ng = ''.join('<tr><td><span class="the-loc %s" style="font-size:13px">%s 系統</span></td>'
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
    <thead><tr><th style="width:104px">系統</th><th style="width:26%%">事業の種類</th>
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
           ke=QT['ke'] % ('<a href="@/ja/kiem-toan/index.html">%s</a>' % E(QT['ke_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": QT['h1'], "description": QT['mt'], "inLanguage": "ja"}]


# ============================================================ 2. KIEM TOAN QT
def _bang_dm_ja():
    moc = ['≤ 5', '10', '50', '100', '500', '1,000', '≥ 10,000']

    def hang(n, ds):
        return ('<tr><td><b>%s</b></td>%s</tr>'
                % (n, ''.join('<td class="n">%s</td>' % x for x in ds)))
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
           h_bang=E(KT['h_bang']), bang=_bang_dm_ja(), bang_ghi=KT['bang_ghi'],
           h_nho=E(KT['h_nho']), nho=KT['nho'],
           h_sh2=E(KT['h_sh2']), sh2=KT['sh2'], sh3=E(KT['sh3']), h_bt=E(KT['h_bt']),
           bt=KT['bt'] % ('<a href="@/ja/tu-van/index.html">%s</a>' % E(KT['bt_lk'])))
    return than, [{"@context": "https://schema.org", "@type": "Article",
                   "headline": KT['h1'], "description": KT['mt'], "inLanguage": "ja"}]


# May tinh phi ban TIENG NHAT — khoi JS RIENG, khong va chuoi cua ban khac.
# ⚠ Don vi: 5 ty dong = 50億ドン · 10.000 ty dong = 10兆ドン. 億 chi la 100 trieu.
B.than_js['ja/kiem-toan'] = """
<script>
(function(){
 var MOC=[5,10,50,100,500,1000,10000],
     KT=[0.96,0.645,0.45,0.345,0.195,0.129,0.069],
     TT=[0.57,0.39,0.285,0.225,0.135,0.09,0.048];
 function tyLe(g,B){
  if(g<=MOC[0]) return {k:B[0], ct:'監査対象額 50億ドン以下 — 料率 '+n(B[0])+'%'};
  if(g>=MOC[MOC.length-1]) return {k:B[B.length-1], ct:'監査対象額 10兆ドン以上 — 料率 '+n(B[B.length-1])+'%'};
  for(var i=0;i<MOC.length-1;i++){ if(g>=MOC[i]&&g<=MOC[i+1]){
    var Gb=MOC[i],Ga=MOC[i+1],Kb=B[i],Ka=B[i+1];
    var Ki=Kb-((Kb-Ka)*(g-Gb))/(Ga-Gb);
    return {k:Ki, ct:'Ki = '+n(Kb)+' − ('+n(Kb)+'−'+n(Ka)+')×('+n(g)+'−'+Gb+')÷('+Ga+'−'+Gb+') = '+n(Ki)+'%'};}}
  return {k:B[B.length-1], ct:''};}
 function n(x){ return String(Math.round(x*10000)/10000); }
 function tien(x){ return Math.round(x).toLocaleString('ja-JP')+' ドン'; }
 var g=document.getElementById('pg'),dv=document.getElementById('pdv'),
     vat=document.getElementById('pvat'),tb=document.getElementById('ptb'),
     bt=document.getElementById('pbt'),kt=document.getElementById('pkt'),
     kq=document.getElementById('pkq');
 function tinh(){
  var so=parseFloat(g.value),hs=parseFloat(dv.value);
  if(!(so>0)){ kq.innerHTML='<p class="loi">ゼロより大きい数値を入力してください。</p>'; return; }
  var dong=so*hs, ty=dong/1e9, a=tyLe(ty,KT), b=tyLe(ty,TT), he=1, mo=[];
  if(tb.checked){ he*=0.7; mo.push('×70％ — 機器費 50％ 以上'); }
  if(bt.checked){ he*=0.5; mo.push('×50％ — 補償・再定住費用'); }
  var pkt=dong*a.k/100*he, chan=false;
  if(pkt<1000000){ pkt=1000000; chan=true; }
  var tvat=parseFloat(vat.value)/100, thue=pkt*tvat, tong=pkt+thue;
  var ptt=dong*b.k/100*he; if(kt.checked) ptt*=0.5;
  var chan2=false; if(ptt<500000){ ptt=500000; chan2=true; }
  kq.innerHTML=
   '<div class="dong"><span>報酬計算の基礎額</span><span>'+tien(dong)+'</span></div>'+
   '<div class="dong"><span>適用料率</span><span>'+n(a.k)+'%</span></div>'+
   (mo.length?'<div class="dong"><span>調整係数</span><span>'+mo.join(' · ')+'</span></div>':'')+
   '<div class="dong"><span>税抜監査報酬</span><span>'+tien(pkt)+(chan?' *':'')+'</span></div>'+
   '<div class="dong"><span>付加価値税 '+(tvat*100)+'%</span><span>'+tien(thue)+'</span></div>'+
   '<div class="to"><span class="nhan">監査報酬の上限</span><div class="so">'+tien(tong)+'</div>'+
     '<div class="phu">付加価値税込み</div></div>'+
   '<div class="cthuc">'+a.ct+'</div>'+
   (chan?'<p class="small" style="margin-top:9px">* 第 20 条第 1 項 b 号による下限額 100 万ドンを適用しました。</p>':'')+
   '<div class="dong" style="margin-top:15px;padding-top:13px;border-top:1px solid var(--vien)">'+
     '<span>決算の審査・承認手数料</span><span>'+tien(ptt)+(chan2?' *':'')+'</span></div>'+
   '<p class="small" style="margin-top:6px;margin-bottom:0">この手数料は審査機関が徴収するものであり、'+
     '監査人に支払う報酬ではありません。また付加価値税は加算されません。</p>';
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
    the = ''.join(V17.V16.V15._the(d, i + 1, 'ja') for i, d in enumerate(V14.DICH_VU))
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
           dv_ghi=TV['dv_ghi'] % ('<a href="@/ja/dich-vu/index.html">%s</a>' % E(TV['dv_lk'])),
           the=the, h_mau=E(TV['h_mau']),
           f_ten=E(TV['f_ten']), f_cv=E(TV['f_cv']), f_dv=E(TV['f_dv']),
           f_dt=E(TV['f_dt']), f_em=E(TV['f_em']),
           s_db=sel('t6', TV['f_db'], TV['db']), s_gd=sel('t7', TV['f_gd'], TV['gd']),
           s_nh=sel('t8', TV['f_nh'], TV['nh']), s_loai=sel('t10', TV['f_loai'], TV['loai']),
           f_mo=E(TV['f_mo']), f_mo_gy=E(TV['f_mo_gy']), f_gui=E(TV['f_gui']),
           h_nen=E(TV['h_nen']), nen=nen, h_bm=E(TV['h_bm']), bm=E(TV['bm']),
           h_kh=E(TV['h_kh']), kh=E(TV['kh']))
    return than, [{"@context": "https://schema.org", "@type": "ContactPage",
                   "name": TV['h1'], "description": TV['mt'], "inLanguage": "ja"}]


# --- Bieu mau: khoi JS RIENG cho tung thu tieng -----------------------------
# Loi cu: ban 17 va 18 gan nguyen khoi JS tieng Viet cho 'en/tu-van' va 'zh/tu-van',
# nen nguoi doc ngoai ngu bam Gui van thay hai cau tieng Viet. Sua o day cho ca ba.
_JS_MAU = """
<script>
(function(){var f=document.getElementById('mau'),k=document.getElementById('kq');
f.addEventListener('submit',function(e){e.preventDefault();
 var ids=['t1','t3','t4','t9'],thieu=[];
 for(var i=0;i<ids.length;i++){if(!document.getElementById(ids[i]).value.trim())thieu.push(ids[i]);}
 if(thieu.length){k.textContent=%s;
  k.style.color='var(--do)';document.getElementById(thieu[0]).focus();return;}
 k.style.color='var(--ngoc)';
 k.textContent=%s;});
})();
</script>"""

_MAU_NHAN = {
    'en': ("'Please complete your name, organisation, telephone and a description of the situation.'",
           "'This form is not yet connected to a receiving service. Please use the details on the Contact page.'"),
    'zh': ("'请填写姓名、单位、电话和情况说明。'",
           "'本表单尚未接入接收服务。请按联系页面上的方式与我们联系。'"),
    'ja': ("'お名前、所属組織、電話番号、状況説明をご記入ください。'",
           "'本フォームはまだ受信サービスに接続されていません。お問い合わせページの連絡先をご利用ください。'"),
}
for _l, (_a, _b) in _MAU_NHAN.items():
    B.than_js['%s/tu-van' % _l] = _JS_MAU % (_a, _b)


# ============================================================ 4. LIEN HE
def trang_lien_he():
    NH = ('nh-nhanh', 'nh-sau', 'nh-cham')
    kh = []
    for i, (nhan, ten, mo, dm, lk) in enumerate(LH['ba']):
        if i == 0:
            them = ('<p style="margin-top:10px"><a href="@/ja/tu-van/index.html" '
                    'style="font-weight:700">%s</a></p>' % E(lk))
        elif i == 1:
            them = ('<p style="margin-top:10px;font-size:20px;font-weight:700;color:var(--muc)">'
                    '08 2509 2007</p><p class="small">%s</p>' % LH['dt_ghi'])
        else:
            them = ('<p class="small" style="margin-top:10px">%s</p>'
                    % (LH['dl_ghi'] % ('<a href="@/ja/tu-van/index.html">%s</a>' % E(LH['dl_lk']))))
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
                   "name": LH['h1'], "description": LH['mt'], "inLanguage": "ja"}]


# ============================================================ khung
_V19_KHUNG = V19.khung
_NAV = re.compile(r'<nav class="top-nav" id="dhuong">.*?</nav>', re.S)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V19_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang != 'ja':
        return h
    goc = V12._goc(slug)
    m = _NAV.search(h)
    nav = m.group(0)
    nhac = V13.NHAC['ja']
    for c in CHU_DE:
        cu = 'href="%s%s/index.html"' % (goc, c)
        moi = 'href="%sja/%s/index.html"' % (goc, c)
        nav = nav.replace('hreflang="vi" title="%s" class="vi-dich" ' % nhac + cu, moi)
        nav = nav.replace(cu, moi)
    h = h[:m.start()] + nav + h[m.end():]
    return V17._chan(h, 'ja', goc)


B.khung = khung

TRANG = list(V19.TRANG) + [
    ('ja/quy-trinh', 'ja', QT['td'], QT['mt'], trang_quy_trinh, 'trong'),
    ('ja/kiem-toan', 'ja', KT['td'], KT['mt'], trang_kiem_toan, 'trong'),
    ('ja/tu-van', 'ja', TV['td'], TV['mt'], trang_tu_van, 'trong'),
    ('ja/lien-he', 'ja', LH['td'], LH['mt'], trang_lien_he, 'trong'),
]


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
