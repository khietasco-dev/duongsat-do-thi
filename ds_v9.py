# -*- coding: utf-8 -*-
"""Ban 9 — them MAY TINH PHI KIEM TOAN QUYET TOAN vao trang Kiem toan QT.

Can cu: Nghi dinh 193/2026/ND-CP Dieu 20 (hieu luc 01/7/2026).
Ban goc tai tu Cong bao Chinh phu, so hieu da doi chieu ben trong noi dung.
Bang ty le GIU NGUYEN so voi ND 254/2025 Dieu 45 — da doi chieu tung con so.
"""
import io, os, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages as P
import ds_pages2 as P2
import ds_data2 as D2
import ds_v2 as V2
import ds_v3 as V3
import ds_v4 as V4
import ds_v5 as V5
import ds_v6 as V6
import ds_v7 as V7
import ds_v8 as V8

# --------------------------------------------------- bang dinh muc (ND 193/2026 Dieu 20)
MOC = [5, 10, 50, 100, 500, 1000, 10000]          # ty dong
KT = [0.96, 0.645, 0.45, 0.345, 0.195, 0.129, 0.069]   # % — kiem toan doc lap
TT = [0.57, 0.39, 0.285, 0.225, 0.135, 0.09, 0.048]    # % — tham tra, phe duyet

B.CSS += r"""
/* ---------- may tinh phi ---------- */
.mtp{background:var(--the);border:1px solid var(--vien);border-radius:var(--r);
  padding:clamp(20px,3vw,30px);box-shadow:var(--bong);margin:18px 0}
.mtp-luoi{display:grid;gap:20px;grid-template-columns:1fr 1fr;align-items:start}
@media(max-width:820px){.mtp-luoi{grid-template-columns:1fr}}
.mtp .o{margin-bottom:15px}
.mtp label{display:block;font-size:13.4px;font-weight:700;margin-bottom:5px;color:var(--chu)}
.mtp label .phu{display:block;font-weight:400;font-size:12.6px;color:var(--chu2);margin-top:2px}
.mtp input[type=number],.mtp select{width:100%;padding:11px 13px;border:1px solid var(--vien);
  border-radius:9px;font-size:16.5px;font-family:'Times New Roman',Times,serif;font-weight:700;
  background:var(--nen);color:var(--chu)}
.mtp select{font-family:inherit;font-size:15px;font-weight:400}
.mtp .tick{display:flex;gap:10px;align-items:flex-start;margin-bottom:11px;font-size:14.3px;color:var(--chu2)}
.mtp .tick input{margin-top:3px;width:17px;height:17px;flex:0 0 auto}
.mtp .tick b{color:var(--chu);font-weight:700}
.kq{background:var(--nen2);border:1px solid var(--vien);border-radius:11px;padding:19px 21px}
.kq .dong{display:flex;justify-content:space-between;gap:14px;padding:7px 0;font-size:14.9px;
  border-bottom:1px dashed var(--vien)}
.kq .dong:last-child{border-bottom:0}
.kq .dong span:first-child{color:var(--chu2)}
.kq .dong span:last-child{font-weight:700;color:var(--chu);white-space:nowrap}
.kq .to{margin-top:13px;padding-top:13px;border-top:2px solid var(--muc)}
.kq .to .nhan{font-size:12.6px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
  color:var(--nhan2);display:block;margin-bottom:3px}
.kq .to .so{font-family:'Times New Roman',Times,serif;font-size:clamp(25px,3.6vw,33px);
  font-weight:700;color:var(--muc);line-height:1.15}
.kq .to .phu{font-size:13.4px;color:var(--chu2);margin-top:3px}
.kq .cthuc{margin-top:12px;padding:10px 12px;background:var(--the);border:1px solid var(--vien);
  border-radius:8px;font-family:Consolas,"Courier New",monospace;font-size:12.8px;color:var(--chu2);
  overflow-x:auto;white-space:nowrap}
.kq .loi{color:var(--do);font-weight:700;font-size:14.6px}
.bang-dm td.n,.bang-dm th.n{text-align:right;font-family:Consolas,"Courier New",monospace}
"""


def _bang_dm():
    def hang(nhan, ds, dv=''):
        return ('<tr><td><b>%s</b></td>%s</tr>'
                % (nhan, ''.join('<td class="n">%s</td>' % str(x).replace('.', ',') for x in ds)))
    moc = ['≤ 5', '10', '50', '100', '500', '1.000', '≥ 10.000']
    return """<div class="bang-boc">
  <table class="bang-dm">
    <thead><tr><th style="width:32%%">Giá trị (tỷ đồng)</th>%s</tr></thead>
    <tbody>%s%s</tbody>
  </table>
</div>""" % (''.join('<th class="n">%s</th>' % m for m in moc),
             hang('Kiểm toán độc lập (%)', KT),
             hang('Thẩm tra, phê duyệt (%)', TT))


def trang_kiem_toan():
    than, ld = V4.trang_kiem_toan()

    mt = """
  <h2 style="margin:34px 0 10px">Phí kiểm toán quyết toán — tính thử ngay</h2>
  <p style="margin-bottom:4px">Căn cứ <b>Nghị định 193/2026/NĐ-CP</b> ngày 01/6/2026, <b>Điều 20</b>,
  hiệu lực từ 01/7/2026. Nhập giá trị cần thuê kiểm toán để ra mức phí.</p>
  <p class="small" style="margin-top:6px">Bảng tỷ lệ này <b>giữ nguyên</b> so với Nghị định 254/2025/NĐ-CP
  Điều 45 — chúng tôi đã đối chiếu từng con số. Nghị định mới chỉ đổi số điều và bỏ chữ
  “hoàn thành” khỏi tên gọi.</p>

  <div class="mtp">
    <div class="mtp-luoi">
      <div>
        <div class="o">
          <label for="pg">Giá trị cần thuê kiểm toán
            <span class="phu">Là giá trị đề nghị quyết toán, hoặc tổng mức đầu tư nếu chưa có số quyết toán</span>
          </label>
          <input id="pg" type="number" min="0" step="0.1" value="120" inputmode="decimal">
        </div>
        <div class="o">
          <label for="pdv">Đơn vị</label>
          <select id="pdv">
            <option value="1000000000" selected>Tỷ đồng</option>
            <option value="1000000">Triệu đồng</option>
            <option value="1">Đồng</option>
          </select>
        </div>
        <div class="o">
          <label for="pvat">Thuế giá trị gia tăng</label>
          <select id="pvat">
            <option value="10" selected>10%</option>
            <option value="8">8%</option>
            <option value="0">Không tính</option>
          </select>
        </div>

        <label class="tick"><input type="checkbox" id="ptb">
          <span><b>Chi phí thiết bị chiếm từ 50% trở lên</b> — điểm d khoản 1 Điều 20:
          phí bằng <b>70%</b> mức thường</span></label>
        <label class="tick"><input type="checkbox" id="pbt">
          <span><b>Đây là chi phí bồi thường, hỗ trợ, tái định cư</b> — điểm đ:
          phí bằng <b>50%</b> mức thường</span></label>
        <label class="tick"><input type="checkbox" id="pkt">
          <span><b>Đã có kiểm toán độc lập hoặc Kiểm toán nhà nước, thanh tra đầy đủ</b> — điểm e:
          riêng phí <b>thẩm tra</b> bằng <b>50%</b></span></label>
      </div>

      <div class="kq" id="pkq"></div>
    </div>
  </div>

  <h3 style="margin:26px 0 8px">Bảng tỷ lệ định mức</h3>
  """ + _bang_dm() + """
  <p class="small">Giá trị nằm giữa hai mốc thì <b>nội suy tuyến tính</b> theo công thức tại điểm a
  khoản 1 Điều 20: <code>Ki = Kb − (Kb − Ka) × (Gi − Gb) ÷ (Ga − Gb)</code>.
  Máy tính ở trên đã làm sẵn phép này.</p>

  <div class="luoi g2" style="margin-top:20px">
    <div class="the" style="border-left:3px solid var(--do)">
      <h3>Bốn điều phải nhớ khi dùng con số này</h3>
      <p style="margin-top:8px">
      <b>Một —</b> đây là <b>mức TỐI ĐA</b>, không phải mức phải trả. Giá gói thầu có thể thấp hơn,
      và thực tế đấu thầu thường thấp hơn.<br><br>
      <b>Hai —</b> phí kiểm toán tối thiểu <b>1 triệu đồng</b> cộng thuế; phí thẩm tra tối thiểu
      <b>500 nghìn đồng</b>.<br><br>
      <b>Ba —</b> phí kiểm toán <b>cộng thuế giá trị gia tăng</b>; phí thẩm tra thì không.<br><br>
      <b>Bốn —</b> con số này là <b>căn cứ lập dự toán gói thầu</b>. Phí thực tế của một hợp đồng
      còn phụ thuộc khối lượng hồ sơ, số gói thầu, địa bàn và thời gian thực hiện.</p>
    </div>
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>Với dự án kiểm toán song hành thì tính thế nào</h3>
      <p style="margin-top:8px">Định mức tính trên <b>giá trị cần thuê kiểm toán của cả dự án</b>,
      không phải cộng dồn từng đợt. Chia thành nhiều đợt là cách <b>tổ chức công việc</b>, không phải
      cách nhân phí lên.</p>
      <p>Trên thực tế, tổng chi phí của phương án song hành thường cao hơn mức định mức một đợt, vì
      khối lượng công việc thực sự nhiều hơn — nhiều lần vào hiện trường, nhiều biên bản làm việc.
      Phần chênh đó hai bên thoả thuận trong hợp đồng và phải được cấp có thẩm quyền chấp thuận.</p>
    </div>
  </div>
"""

    neo = '\n  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">\n    <h3>Nếu Quý vị đang cân nhắc cách làm cho dự án của mình</h3>'
    if neo in than:
        than = than.replace(neo, mt + neo, 1)
    else:
        than = than.replace('</div></div>\n', mt + '\n</div></div>\n')
    return than, ld


# ---------------------------------------------------------------- ma chay may tinh
B.than_js['kiem-toan'] = """
<script>
(function(){
 var MOC=[5,10,50,100,500,1000,10000],
     KT=[0.96,0.645,0.45,0.345,0.195,0.129,0.069],
     TT=[0.57,0.39,0.285,0.225,0.135,0.09,0.048];

 function tyLe(g, B){
  if(g<=MOC[0]) return {k:B[0], ct:'Giá trị ≤ 5 tỷ — lấy thẳng mức '+n(B[0])+'%'};
  if(g>=MOC[MOC.length-1]) return {k:B[B.length-1], ct:'Giá trị ≥ 10.000 tỷ — lấy thẳng mức '+n(B[B.length-1])+'%'};
  for(var i=0;i<MOC.length-1;i++){
   if(g>=MOC[i] && g<=MOC[i+1]){
    var Gb=MOC[i], Ga=MOC[i+1], Kb=B[i], Ka=B[i+1];
    var Ki=Kb-((Kb-Ka)*(g-Gb))/(Ga-Gb);
    return {k:Ki, ct:'Ki = '+n(Kb)+' − ('+n(Kb)+'−'+n(Ka)+')×('+n(g)+'−'+Gb+')÷('+Ga+'−'+Gb+') = '+n(Ki)+'%'};
   }}
  return {k:B[B.length-1], ct:''};
 }
 function n(x){ return String(Math.round(x*10000)/10000).replace('.',','); }
 function tien(x){ return Math.round(x).toLocaleString('vi-VN')+' đ'; }

 var g=document.getElementById('pg'), dv=document.getElementById('pdv'),
     vat=document.getElementById('pvat'), tb=document.getElementById('ptb'),
     bt=document.getElementById('pbt'), kt=document.getElementById('pkt'),
     kq=document.getElementById('pkq');

 function tinh(){
  var so=parseFloat(g.value), hs=parseFloat(dv.value);
  if(!(so>0)){ kq.innerHTML='<p class="loi">Xin nhập giá trị lớn hơn 0.</p>'; return; }
  var dong=so*hs, ty=dong/1e9;
  var a=tyLe(ty,KT), b=tyLe(ty,TT);
  var he=1, mo=[];
  if(tb.checked){ he*=0.7; mo.push('×70% do chi phí thiết bị ≥ 50%'); }
  if(bt.checked){ he*=0.5; mo.push('×50% do là chi phí bồi thường, tái định cư'); }

  var pkt=dong*a.k/100*he, chan=false;
  if(pkt<1000000){ pkt=1000000; chan=true; }
  var tvat=parseFloat(vat.value)/100, thue=pkt*tvat, tong=pkt+thue;

  var ptt=dong*b.k/100*he;
  if(kt.checked) ptt*=0.5;
  var chan2=false;
  if(ptt<500000){ ptt=500000; chan2=true; }

  kq.innerHTML=
   '<div class="dong"><span>Giá trị tính phí</span><span>'+tien(dong)+'</span></div>'+
   '<div class="dong"><span>Tỷ lệ định mức kiểm toán</span><span>'+n(a.k)+'%</span></div>'+
   (mo.length?'<div class="dong"><span>Hệ số điều chỉnh</span><span>'+mo.join(' · ')+'</span></div>':'')+
   '<div class="dong"><span>Phí kiểm toán trước thuế</span><span>'+tien(pkt)+(chan?' *':'')+'</span></div>'+
   '<div class="dong"><span>Thuế giá trị gia tăng '+(tvat*100)+'%</span><span>'+tien(thue)+'</span></div>'+
   '<div class="to"><span class="nhan">Phí kiểm toán tối đa</span>'+
     '<div class="so">'+tien(tong)+'</div>'+
     '<div class="phu">Đã gồm thuế giá trị gia tăng</div></div>'+
   '<div class="cthuc">'+a.ct+'</div>'+
   (chan?'<p class="small" style="margin-top:9px">* Đã áp mức tối thiểu 1 triệu đồng theo điểm b khoản 1 Điều 20.</p>':'')+
   '<div class="dong" style="margin-top:15px;padding-top:13px;border-top:1px solid var(--vien)">'+
     '<span>Phí thẩm tra, phê duyệt quyết toán</span><span>'+tien(ptt)+(chan2?' *':'')+'</span></div>'+
   '<p class="small" style="margin-top:6px;margin-bottom:0">Khoản này do cơ quan chủ trì thẩm tra thu, '+
     'không phải phí trả cho đơn vị kiểm toán. Không cộng thuế giá trị gia tăng.</p>';
 }
 [g,dv,vat,tb,bt,kt].forEach(function(e){ e.addEventListener('input',tinh); e.addEventListener('change',tinh); });
 tinh();
})();
</script>"""


TRANG = [(s, l, td, mt, (trang_kiem_toan if s == 'kiem-toan' else fn), tang)
         for s, l, td, mt, fn, tang in V8.TRANG]
# doi mo ta trang kiem toan cho khop noi dung moi
TRANG = [(s, l,
          'Kiểm toán quyết toán dự án hoàn thành và phí kiểm toán' if s == 'kiem-toan' else td,
          'Mười ba phần hành, kiểm toán song hành, và máy tính phí kiểm toán theo Nghị định 193/2026/NĐ-CP Điều 20.' if s == 'kiem-toan' else mt,
          fn, tang)
         for s, l, td, mt, fn, tang in TRANG]


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
