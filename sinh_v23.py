# -*- coding: utf-8 -*-
"""Sinh ds_v23.py tu ds_v22.py — doi de -> fr. Khuon giong het, chi doi ngon ngu."""
import io, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(r'C:\Users\Public\BO NAO\duongsat-do-thi')

s = io.open('ds_v22.py', encoding='utf-8').read()

# ---------------------------------------------------------------- 1. import
s = s.replace('import ds_v21 as V21', 'import ds_v22 as V22')
s = s.replace('from ds_de_qt import', 'from ds_fr_qt import')
s = s.replace('from ds_de_tv import TV, LH, CHAN_DE', 'from ds_fr_tv import TV, LH, CHAN_FR')
s = s.replace('from ds_de_dv import DE, KHUNG', 'from ds_fr_dv import FR, KHUNG')
s = s.replace('from ds_de_rr import VB, CAP_DE, DIA_DE, RR, RR_NHOM',
              'from ds_fr_rr import VB, CAP_FR, DIA_FR, RR, RR_NHOM')
s = s.replace('from ds_de_kn import', 'from ds_fr_kn import')

# ---------------------------------------------------------------- 2. dinh danh
s = s.replace('CHAN_DE', 'CHAN_FR').replace('CAP_DE', 'CAP_FR').replace('DIA_DE', 'DIA_FR')
s = s.replace('_bang_dm_de', '_bang_dm_fr').replace('_trang_dv_de', '_trang_dv_fr')
s = s.replace('_tep_de', '_tep_fr')
s = s.replace("DE[d['slug']]", "FR[d['slug']]").replace('z = DE[', 'z = FR[')
s = s.replace("V21._NHAN_PHAN['de']", "V22.V21._NHAN_PHAN['fr']")
s = s.replace("V21._tep_lang(d, 'de')", "V22.V21._tep_lang(d, 'fr')")
s = s.replace('_V21_KHUNG = V21.khung', '_V22_KHUNG = V22.khung')
s = s.replace('h = _V21_KHUNG(', 'h = _V22_KHUNG(')
s = s.replace('TRANG = list(V21.TRANG)', 'TRANG = list(V22.TRANG)')
s = s.replace('V21.V20._JS_MAU', 'V22.V21.V20._JS_MAU')

# ---------------------------------------------------------------- 3. slug
s = s.replace("'de/", "'fr/").replace('@/de/', '@/fr/')
s = s.replace("'de'", "'fr'").replace('"de"', '"fr"')

# ---------------------------------------------------------------- 4. nhan giao dien
s = s.replace('<a href="@/fr/index.html">Start</a>', '<a href="@/fr/index.html">Accueil</a>')
s = s.replace('Strang %s</span>', 'R\u00e9gime %s</span>')
s = s.replace('<th style="width:118px">Strang</th>',
              '<th style="width:118px">R\u00e9gime</th>')
s = s.replace('<th style="width:26%%">Art des Vorhabens</th>',
              '<th style="width:26%%">Type de projet</th>')
s = s.replace("'ASCO Pr\u00fcfungs- und Bewertungsgesellschaft, Vietnam'",
              "'ASCO \u2014 Soci\u00e9t\u00e9 d\u2019audit et d\u2019\u00e9valuation, Vietnam'")
s = s.replace("'%d Teile'", "'%d parties'")

# ---------------------------------------------------------------- 5. cau nhac trang tong dich vu
CU_NHAC = ("V14.DICH_NHAC['fr'] = ('Alle neun Leistungen haben auch eine <b>deutsche Fassung</b> "
           "der '\n                       'Detailseite. Die zitierten Vorschriften bleiben auf "
           "Vietnamesisch \u2014 '\n                       'nur dieser Wortlaut ist "
           "rechtsverbindlich.')")
MOI_NHAC = ("V14.DICH_NHAC['fr'] = ('Les neuf prestations disposent aussi d\u2019une "
            "<b>version fran\u00e7aise</b> '\n                       'de leur page "
            "d\u00e9taill\u00e9e. Les textes cit\u00e9s restent en vietnamien \u2014 seul '\n"
            "                       'ce libell\u00e9 fait foi.')")
assert CU_NHAC in s, 'khong khop cau nhac'
s = s.replace(CU_NHAC, MOI_NHAC)

# ---------------------------------------------------------------- 6. ba khoi JS
DAU = '<' + 'script>'
CUOI = '</' + 'script>"' + '""'


def thay_js(chuoi, khoa, moi):
    d = chuoi.index(khoa)
    c = chuoi.index(CUOI, d) + len(CUOI)
    return chuoi[:d] + moi + chuoi[c:]


JS_PHI = ("B.than_js['fr/kiem-toan'] = \"\"\"\n" + DAU + """
(function(){
 var MOC=[5,10,50,100,500,1000,10000],
     KT=[0.96,0.645,0.45,0.345,0.195,0.129,0.069],
     TT=[0.57,0.39,0.285,0.225,0.135,0.09,0.048];
 function tyLe(g,B){
  if(g<=MOC[0]) return {k:B[0], ct:'Montant \\u2264 5 milliards de VND \\u2014 taux '+n(B[0])+'\\u202f%'};
  if(g>=MOC[MOC.length-1]) return {k:B[B.length-1], ct:'Montant \\u2265 10\\u202f000 milliards de VND \\u2014 taux '+n(B[B.length-1])+'\\u202f%'};
  for(var i=0;i<MOC.length-1;i++){ if(g>=MOC[i]&&g<=MOC[i+1]){
    var Gb=MOC[i],Ga=MOC[i+1],Kb=B[i],Ka=B[i+1];
    var Ki=Kb-((Kb-Ka)*(g-Gb))/(Ga-Gb);
    return {k:Ki, ct:'Ki = '+n(Kb)+' \\u2212 ('+n(Kb)+'\\u2212'+n(Ka)+')\\u00d7('+n(g)+'\\u2212'+n(Gb)+')\\u00f7('+n(Ga)+'\\u2212'+n(Gb)+') = '+n(Ki)+'\\u202f%'};}}
  return {k:B[B.length-1], ct:''};}
 function n(x){ return String(Math.round(x*10000)/10000).replace('.',','); }
 function tien(x){ return Math.round(x).toLocaleString('fr-FR')+' VND'; }
 var g=document.getElementById('pg'),dv=document.getElementById('pdv'),
     vat=document.getElementById('pvat'),tb=document.getElementById('ptb'),
     bt=document.getElementById('pbt'),kt=document.getElementById('pkt'),
     kq=document.getElementById('pkq');
 function tinh(){
  var so=parseFloat(g.value),hs=parseFloat(dv.value);
  if(!(so>0)){ kq.innerHTML='<p class="loi">Veuillez saisir une valeur sup\\u00e9rieure \\u00e0 z\\u00e9ro.</p>'; return; }
  var dong=so*hs, ty=dong/1e9, a=tyLe(ty,KT), b=tyLe(ty,TT), he=1, mo=[];
  if(tb.checked){ he*=0.7; mo.push('\\u00d770\\u202f% \\u2014 \\u00e9quipements \\u2265 50\\u202f%'); }
  if(bt.checked){ he*=0.5; mo.push('\\u00d750\\u202f% \\u2014 indemnisation et r\\u00e9installation'); }
  var pkt=dong*a.k/100*he, chan=false;
  if(pkt<1000000){ pkt=1000000; chan=true; }
  var tvat=parseFloat(vat.value)/100, thue=pkt*tvat, tong=pkt+thue;
  var ptt=dong*b.k/100*he; if(kt.checked) ptt*=0.5;
  var chan2=false; if(ptt<500000){ ptt=500000; chan2=true; }
  kq.innerHTML=
   '<div class="dong"><span>Assiette de calcul</span><span>'+tien(dong)+'</span></div>'+
   '<div class="dong"><span>Taux appliqu\\u00e9</span><span>'+n(a.k)+'\\u202f%</span></div>'+
   (mo.length?'<div class="dong"><span>Coefficient d\\u2019ajustement</span><span>'+mo.join(' \\u00b7 ')+'</span></div>':'')+
   '<div class="dong"><span>Honoraires hors taxe</span><span>'+tien(pkt)+(chan?' *':'')+'</span></div>'+
   '<div class="dong"><span>TVA '+n(tvat*100)+'\\u202f%</span><span>'+tien(thue)+'</span></div>'+
   '<div class="to"><span class="nhan">Plafond des honoraires d\\u2019audit</span><div class="so">'+tien(tong)+'</div>'+
     '<div class="phu">TVA comprise</div></div>'+
   '<div class="cthuc">'+a.ct+'</div>'+
   (chan?'<p class="small" style="margin-top:9px">* Le minimum d\\u2019un million de VND pr\\u00e9vu \\u00e0 l\\u2019article 20, alin\\u00e9a 1, point b, a \\u00e9t\\u00e9 appliqu\\u00e9.</p>':'')+
   '<div class="dong" style="margin-top:15px;padding-top:13px;border-top:1px solid var(--vien)">'+
     '<span>Frais de contr\\u00f4le et d\\u2019approbation</span><span>'+tien(ptt)+(chan2?' *':'')+'</span></div>'+
   '<p class="small" style="margin-top:6px;margin-bottom:0">Ces frais sont per\\u00e7us par '+
     'l\\u2019autorit\\u00e9 de contr\\u00f4le \\u2014 ce ne sont pas des honoraires vers\\u00e9s '+
     '\\u00e0 l\\u2019auditeur, et la TVA ne s\\u2019y ajoute pas.</p>';
 }
 [g,dv,vat,tb,bt,kt].forEach(function(e){ e.addEventListener('input',tinh); e.addEventListener('change',tinh); });
 tinh();
})();
""" + CUOI)

JS_LOC = ("B.than_js['fr/van-ban'] = \"\"\"\n" + DAU + """
(function(){
 var q=document.getElementById('q'),f=[1,2,3,4].map(function(i){return document.getElementById('f'+i);}),
     hang=[].slice.call(document.querySelectorAll('#bang tbody tr')),
     dem=document.getElementById('dem'), tong=hang.length;
 function bo(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/\\u0111/g,'d').toLowerCase();}
 function loc(){
  var k=bo(q.value.trim()), n=0;
  hang.forEach(function(r){
   var ok=(!k||r.dataset.tim.toLowerCase().indexOf(k)>=0)
    &&(!f[0].value||r.dataset.ngan===f[0].value)
    &&(!f[1].value||r.dataset.dia===f[1].value)
    &&(!f[2].value||r.dataset.nam===f[2].value)
    &&(!f[3].value||r.dataset.tt===f[3].value);
   r.style.display=ok?'':'none'; if(ok)n++;});
  dem.innerHTML='<b>'+n+'</b> textes sur '+tong;
 }
 [q].concat(f).forEach(function(e){e.addEventListener('input',loc);e.addEventListener('change',loc);});
 loc();
})();
""" + CUOI)

s = thay_js(s, "B.than_js['fr/kiem-toan'] = ", JS_PHI)
s = thay_js(s, "B.than_js['fr/van-ban'] = ", JS_LOC)

# bieu mau
_KHOA = "B.than_js['fr/tu-van'] = V22.V21.V20._JS_MAU % ("
_KET = "Kontaktseite.'\")"
_d = s.index(_KHOA)
_c = s.index(_KET, _d) + len(_KET)
s = s[:_d] + (
    "B.than_js['fr/tu-van'] = V22.V21.V20._JS_MAU % (\n"
    "    \"'Veuillez renseigner le nom, l\\u2019organisme, le t\\u00e9l\\u00e9phone et la \"\n"
    "    \"description de la situation.'\",\n"
    "    \"'Ce formulaire n\\u2019est pas encore reli\\u00e9 \\u00e0 un service de r\\u00e9ception. \"\n"
    "    \"Merci d\\u2019utiliser les coordonn\\u00e9es de la page Contact.'\")"
) + s[_c:]

# ---------------------------------------------------------------- 7. doc-string
d0 = s.index('"""')
d1 = s.index('"""', d0 + 3) + 3
DOC = '"' + '""' + '''Ban 23 — TRON BO TIENG PHAP. 17 trang.  Trang **97 -> 114**.

BO SAU NGON NGU DA XONG: Viet · Anh · Trung · Nhat · Duc · Phap.

⚠ KE THUA BAN LIEN TRUOC (ds_v22). Kiem: "Da ghi N trang" phai = 97 + 17 = 114.

🔴 BAY DON VI TIEN — tieng Phap dung THANG DAI giong tieng Duc:
  **"billion" tieng Phap = 10^12**, ty = **milliard**.
  5 ty = "5 milliards de VND" · 10.000 ty = "10 000 milliards de VND".
  Ban tieng Anh dung "Billion VND" nghia la TY — dich thang sang Phap la sai 1.000 lan.

⚠ Cach viet so tieng Phap: dau thap phan la DAU PHAY (0,3375), phan cach nghin va
  truoc dau % la KHOANG TRANG HEP U+202F. toLocaleString('fr-FR') tu lam phan nghin.

⚠ MOI THU TIENG MOT KHOI JS RIENG — da viet han ba khoi cho fr.
''' + '"' + '""'
s = '# -*- coding: utf-8 -*-\n' + DOC + s[d1:]

io.open('ds_v23.py', 'w', encoding='utf-8').write(s)
print('DA SINH ds_v23.py — %d dong' % s.count('\n'))
print()
print('RA CHU CON SOT CUA BAN TIENG DUC:')
for x in ['ds_de', 'CHAN_DE', "'de/", '@/de/', 'V21.khung', 'Milliarden', 'Billionen',
          'Strang', 'Teile', 'Vorhaben', 'Pr\u00fcfung']:
    n = s.count(x)
    print('  %-16s %s' % (x, ('*** %d' % n) if n else 'khong'))
