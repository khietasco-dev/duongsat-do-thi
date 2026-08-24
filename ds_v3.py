# -*- coding: utf-8 -*-
"""Ban 3 — viet chi tiet bon TRANG GIAO DIEN CAP 2:
   Tra cuu van ban · Xem quy trinh du an · Gui yeu cau tu van · Xem lien he
"""
import io, os, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages as P
import ds_pages2 as P2
import ds_data as D
import ds_v2 as V2

VB, N = P2.VB, P2.N


# ================================================================ CSS bo sung
B.CSS += r"""
/* ---------- lop bo sung cho trang giao dien cap 2 ---------- */
.huong-dan{display:grid;gap:13px;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));margin:16px 0 24px}
.huong-dan .b{background:var(--nen2);border:1px solid var(--vien);border-radius:11px;padding:16px 18px}
.huong-dan .b b{display:block;color:var(--muc);font-size:15.2px;margin-bottom:5px}
.huong-dan .b span{font-size:14.4px;color:var(--chu2)}

.thongke{display:flex;flex-wrap:wrap;gap:11px;margin:14px 0 22px}
.thongke div{background:var(--the);border:1px solid var(--vien);border-radius:10px;padding:12px 17px;min-width:118px}
.thongke b{display:block;font-family:'Times New Roman',Times,serif;font-size:25px;color:var(--muc);line-height:1.15}
.thongke span{font-size:13.2px;color:var(--chu2)}

.buoc{counter-reset:s;display:grid;gap:12px;margin:16px 0}
.buoc .b{display:flex;gap:15px;align-items:flex-start;background:var(--the);border:1px solid var(--vien);
  border-radius:11px;padding:17px 19px}
.buoc .b::before{counter-increment:s;content:counter(s);flex:0 0 auto;width:29px;height:29px;border-radius:50%;
  background:var(--muc);color:#fff;display:grid;place-items:center;font-weight:800;font-size:14.6px}
:root[data-theme="dark"] .buoc .b::before{color:#0D2044}
.buoc .b b{display:block;color:var(--muc);font-size:16px;margin-bottom:3px}
.buoc .b span{font-size:14.9px;color:var(--chu2)}

.cot2{display:grid;gap:22px;grid-template-columns:1.35fr 1fr;align-items:start}
@media(max-width:860px){.cot2{grid-template-columns:1fr}}
.hop-ben{background:var(--nen2);border:1px solid var(--vien);border-radius:var(--r);padding:20px 22px;
  position:sticky;top:78px}
@media(max-width:860px){.hop-ben{position:static}}
.hop-ben h3{font-size:16.5px;margin-bottom:9px}
.hop-ben ul{margin:0;padding-left:18px;font-size:14.6px;color:var(--chu2)}
.hop-ben li{margin-bottom:7px}

.kenh{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(252px,1fr));margin:18px 0}
.kenh .b{background:var(--the);border:1px solid var(--vien);border-radius:var(--r);padding:21px;box-shadow:var(--bong)}
.kenh .b .nh{display:inline-block;font-size:11.6px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  padding:3px 10px;border-radius:999px;margin-bottom:10px}
.nh-nhanh{background:var(--ngoc-nen);color:var(--ngoc)}
.nh-sau{background:var(--hoacuc-nen);color:var(--nhan2)}
.nh-cham{background:var(--nen3);color:var(--muc)}
.kenh .b h3{margin-bottom:6px}
.kenh .b p{margin:0;font-size:14.9px;color:var(--chu2)}
.kenh .b .dm{margin-top:11px;font-size:14px;color:var(--chu2);border-top:1px solid var(--vien);padding-top:9px}
.kenh .b .dm b{color:var(--muc)}
.so-lon{font-family:'Times New Roman',Times,serif;font-size:27px;font-weight:700;color:var(--muc);
  text-decoration:none;letter-spacing:.01em;display:inline-block}
.so-lon:hover{color:var(--nhan2)}
"""


# ================================================================ 1. TRA CUU VAN BAN
def trang_van_ban():
    than, ld = P2.trang_van_ban()

    them_dau = """
  <h2 style="margin-bottom:12px">Cách dùng trang này</h2>
  <div class="huong-dan">
    <div class="b"><b>Gõ có dấu hay không dấu đều được</b>
      <span>Tên tệp trong kho là chữ không dấu, nhưng ô tìm tự bỏ dấu hai phía. Gõ “đường sắt”
      hay “duong sat” ra kết quả như nhau.</span></div>
    <div class="b"><b>Tìm theo số hiệu</b>
      <span>Nhớ số thì gõ số: “188”, “62/2026”, “15/2025”. Nhanh hơn nhớ tên đầy đủ.</span></div>
    <div class="b"><b>Lọc chồng nhiều điều kiện</b>
      <span>Bốn ô lọc cộng dồn với nhau và cộng với ô tìm. Ví dụ Thông tư + Hà Nội + còn hiệu lực.</span></div>
    <div class="b"><b>Đọc cột Định dạng</b>
      <span>DOC hoặc DOCX là bản Word chỉnh sửa, trích dẫn được. Chỉ có PDF nghĩa là nguồn chính thức
      không phát hành bản Word.</span></div>
  </div>

  <h2 style="margin:26px 0 4px">Kho có gì</h2>
  <div class="thongke">
    <div><b>%d</b><span>Đầu văn bản</span></div>
    <div><b>110</b><span>Tệp Word và PDF</span></div>
    <div><b>%d</b><span>Có cả Word và PDF</span></div>
    <div><b>%d</b><span>Chỉ có PDF</span></div>
    <div><b>%d</b><span>Bản hợp nhất</span></div>
    <div><b>%d</b><span>Văn bản địa phương</span></div>
  </div>
""" % (N,
       sum(1 for d in VB if len(d['dinhdang']) > 1),
       sum(1 for d in VB if d['dinhdang'] == ['pdf']),
       sum(1 for d in VB if d['hopnhat']),
       sum(1 for d in VB if d['diaban'] in ('Hà Nội', 'TP. Hồ Chí Minh')))

    than = than.replace('  <h2 style="margin-bottom:14px">Tra cứu văn bản</h2>',
                        them_dau + '\n  <h2 style="margin:26px 0 14px">Tra cứu văn bản</h2>', 1)

    them_cuoi = """
  <h2 style="margin:32px 0 14px">Bốn cấp văn bản, đọc theo thứ tự nào</h2>
  <div class="buoc">
    <div class="b"><div><b>Luật và Nghị quyết Quốc hội</b>
      <span>Nền pháp lý. Với đường sắt đô thị, đọc bản hợp nhất Luật Đường sắt trước, rồi tới
      Nghị quyết 188/2025 về cơ chế đặc thù — đây mới là văn bản làm thay đổi trình tự.</span></div></div>
    <div class="b"><div><b>Nghị định</b>
      <span>Quy định chi tiết thi hành. Bản hợp nhất VBHN 34/VBHN-BXD gồm 143 Điều về thiết kế
      kỹ thuật tổng thể và cơ chế đặc thù là bản nên đọc.</span></div></div>
    <div class="b"><div><b>Thông tư và quy chuẩn kỹ thuật</b>
      <span>Hướng dẫn nghiệp vụ và tiêu chuẩn kỹ thuật. Quy chuẩn riêng cho metro chỉ có
      từ Thông tư 62/2026/TT-BXD ngày 30/7/2026 — tuyến khởi động trước mốc này phải mượn tiêu chuẩn
      nước ngoài, và đó là gốc của một vướng mắc riêng.</span></div></div>
    <div class="b"><div><b>Văn bản khác</b>
      <span>Quyết định, công văn, thông báo kết luận, và toàn bộ nghị quyết của Hội đồng nhân dân
      Hà Nội, TP. Hồ Chí Minh về TOD và không gian ngầm. Nhóm này nhiều nhất và cũng hay bị bỏ sót nhất.</span></div></div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:22px">
    <h3>Trang này không thay thế bản gốc</h3>
    <p style="margin-top:8px">Danh mục ở đây giúp Quý vị biết <b>có văn bản nào</b> và <b>tình trạng ra sao</b>.
    Khi trích dẫn vào tờ trình, báo cáo kiểm toán hay chứng thư, phải mở bản gốc trên Công báo để đối chiếu
    số điều, khoản. Văn bản pháp luật thay đổi thường xuyên — danh mục cập nhật ngày 24/08/2026.</p>
  </div>
"""
    than = than.replace('</div></div>\n', them_cuoi + '\n</div></div>\n')
    return than, ld


# ================================================================ 3. GUI YEU CAU TU VAN
def trang_tu_van():
    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Tư vấn</div>
  <h1>Gửi yêu cầu tư vấn</h1>
  <p>Mô tả tình huống dự án đang vướng. Chúng tôi đọc, phân loại và phản hồi trong 24 giờ làm việc.</p>
</div></div>

<div class="than"><div class="wrap">

  <h2 style="margin-bottom:12px">Ba loại yêu cầu chúng tôi nhận</h2>
  <div class="kenh">
    <div class="b">
      <span class="nh nh-nhanh">Trả lời nhanh</span>
      <h3>Hỏi một điểm cụ thể</h3>
      <p>Một câu hỏi rõ ràng về căn cứ pháp lý, trình tự thủ tục hoặc cách xử lý một khoản chi phí.
      Loại này thường trả lời được ngay trong thư phản hồi đầu tiên.</p>
      <div class="dm">Thời gian: <b>trong 24 giờ làm việc</b> · Không mất phí</div>
    </div>
    <div class="b">
      <span class="nh nh-sau">Cần đọc hồ sơ</span>
      <h3>Vướng mắc có nhiều tình tiết</h3>
      <p>Tình huống liên quan tới nhiều văn bản, nhiều mốc thời gian, hoặc cần đối chiếu hợp đồng và
      hồ sơ nghiệm thu. Chúng tôi trả lời sơ bộ trước, rồi hẹn buổi trao đổi nếu cần.</p>
      <div class="dm">Thời gian: <b>2 đến 3 ngày làm việc</b> · Có thể cần ký thoả thuận bảo mật</div>
    </div>
    <div class="b">
      <span class="nh nh-cham">Thành dịch vụ</span>
      <h3>Rà soát cả bộ hồ sơ dự án</h3>
      <p>Soát toàn bộ hồ sơ trước khi trình quyết toán, hoặc dựng lại bản đồ hiệu lực văn bản cho một
      dự án kéo dài nhiều năm. Đây là công việc có phạm vi và thời gian riêng.</p>
      <div class="dm">Thời gian: <b>theo thoả thuận</b> · Có hợp đồng dịch vụ</div>
    </div>
  </div>

  <div class="cot2">
    <div>
      <h2 style="margin-bottom:12px">Biểu mẫu</h2>
      <div class="mau">
        <form class="mau-luoi" id="mau" novalidate>
          <div class="truong"><label for="t1">Họ và tên <span style="color:var(--do)">*</span></label><input id="t1" type="text" required></div>
          <div class="truong"><label for="t2">Chức vụ</label><input id="t2" type="text"></div>
          <div class="truong"><label for="t3">Đơn vị công tác <span style="color:var(--do)">*</span></label><input id="t3" type="text" required></div>
          <div class="truong"><label for="t4">Điện thoại <span style="color:var(--do)">*</span></label><input id="t4" type="tel" required></div>
          <div class="truong"><label for="t5">Email</label><input id="t5" type="email"></div>
          <div class="truong"><label for="t6">Địa bàn dự án</label>
            <select id="t6"><option value="">— Chọn —</option><option>Hà Nội</option>
            <option>TP. Hồ Chí Minh</option><option>Địa bàn khác</option></select></div>
          <div class="truong"><label for="t7">Dự án đang ở giai đoạn nào</label>
            <select id="t7"><option value="">— Chọn —</option>
            <option>Quy hoạch tuyến</option><option>Chủ trương đầu tư</option>
            <option>Lập, thẩm định, phê duyệt dự án</option><option>Giải phóng mặt bằng</option>
            <option>Lựa chọn nhà thầu</option><option>Thi công xây dựng</option>
            <option>Nghiệm thu, chạy thử</option><option>Bàn giao, ghi nhận tài sản</option>
            <option>Quyết toán vốn đầu tư</option></select></div>
          <div class="truong"><label for="t8">Nhóm vướng mắc</label>
            <select id="t8"><option value="">— Chọn —</option>
            <option>Trình tự, thủ tục đầu tư</option><option>Giải phóng mặt bằng</option>
            <option>Hợp đồng và thanh toán</option><option>Nghiệm thu, hồ sơ hoàn công</option>
            <option>Quyết toán vốn đầu tư</option><option>TOD và khai thác quỹ đất</option>
            <option>Không gian ngầm</option><option>Đào tạo, chuyển giao công nghệ</option>
            <option>Khác</option></select></div>
          <div class="truong"><label for="t10">Loại yêu cầu</label>
            <select id="t10"><option value="">— Chọn —</option>
            <option>Hỏi một điểm cụ thể</option><option>Vướng mắc có nhiều tình tiết</option>
            <option>Rà soát cả bộ hồ sơ dự án</option></select></div>
          <div class="truong rong"><label for="t9">Mô tả tình huống <span style="color:var(--do)">*</span></label>
            <textarea id="t9" required placeholder="Dự án đang vướng ở đâu · đã xử lý những gì · cần hỗ trợ điều gì · có mốc thời gian nào phải kịp không"></textarea></div>
          <div class="rong">
            <button class="nut-gui" type="submit">Gửi yêu cầu</button>
            <p class="small" id="kq" style="margin-top:11px"></p>
          </div>
        </form>
      </div>
    </div>

    <div class="hop-ben">
      <h3>Nên nêu gì trong phần mô tả</h3>
      <ul>
        <li>Dự án thuộc địa bàn nào — Hà Nội và TP. Hồ Chí Minh có cơ chế riêng, địa bàn khác thì không</li>
        <li>Nguồn vốn: đầu tư công, ODA hay PPP</li>
        <li>Mốc thời gian của việc đang vướng — vì văn bản áp dụng theo thời kỳ phát sinh</li>
        <li>Đã có văn bản nào của cấp có thẩm quyền về việc này chưa</li>
        <li>Có mốc phải kịp không, ví dụ hạn trình thẩm tra</li>
      </ul>
      <h3 style="margin-top:16px">Chưa cần gửi ở bước này</h3>
      <ul>
        <li>Tài liệu mật hoặc hồ sơ gốc</li>
        <li>Số liệu hợp đồng, giá trị gói thầu</li>
        <li>Tên nhà thầu, tên cán bộ</li>
      </ul>
      <p class="small" style="margin-top:12px;margin-bottom:0">Mô tả tình huống là đủ để chúng tôi biết
      vấn đề thuộc nhóm nào. Nếu cần đọc hồ sơ, hai bên sẽ thoả thuận cách gửi an toàn.</p>
    </div>
  </div>

  <h2 style="margin:32px 0 12px">Sau khi Quý vị bấm gửi</h2>
  <div class="buoc">
    <div class="b"><div><b>Chúng tôi đọc và phân loại</b>
      <span>Xác định yêu cầu thuộc loại nào trong ba loại trên, và thuộc nhóm vướng mắc nào.</span></div></div>
    <div class="b"><div><b>Phản hồi lần đầu trong 24 giờ làm việc</b>
      <span>Nêu hướng xử lý sơ bộ và căn cứ liên quan, hoặc hỏi thêm thông tin nếu tình huống chưa đủ rõ.</span></div></div>
    <div class="b"><div><b>Trao đổi sâu nếu cần</b>
      <span>Với tình huống nhiều tình tiết, hai bên hẹn một buổi trao đổi. Nếu phải xem hồ sơ thì
      ký thoả thuận bảo mật trước.</span></div></div>
    <div class="b"><div><b>Câu hỏi có giá trị chung thành bài</b>
      <span>Nếu tình huống của Quý vị hay gặp ở nhiều dự án, chúng tôi biên tập thành một mục trên trang
      <a href="../vuong-mac/index.html">Vướng mắc</a> — <b>không nêu tên đơn vị hỏi</b>.</span></div></div>
  </div>

  <div class="luoi g2" style="margin-top:24px">
    <div class="the" style="border-left:3px solid var(--muc3)">
      <h3>Về bảo mật</h3>
      <p style="margin-top:8px">Thông tin Quý vị gửi chỉ dùng để trả lời yêu cầu. Không chuyển cho bên thứ ba,
      không dùng làm ví dụ công khai khi chưa có sự đồng ý bằng văn bản. Quý vị có thể yêu cầu xoá thông tin
      bất cứ lúc nào.</p>
    </div>
    <div class="the" style="border-left:3px solid var(--do)">
      <h3>Về phạm vi trả lời</h3>
      <p style="margin-top:8px">Ý kiến trên trang này là thông tin tham khảo chuyên môn, <b>không thay thế
      tư vấn chính thức cho một dự án cụ thể</b> và không phải căn cứ pháp lý. Quyết định thuộc về người có
      thẩm quyền của dự án.</p>
    </div>
  </div>

</div></div>
"""
    ld = [{"@context": "https://schema.org", "@type": "ContactPage",
           "name": "Gửi yêu cầu tư vấn dự án đường sắt đô thị", "url": B.GOC + "/tu-van/",
           "description": "Ba loại yêu cầu tư vấn, biểu mẫu gửi và quy trình phản hồi trong 24 giờ làm việc."},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Tư vấn", "item": B.GOC + "/tu-van/"}]}]
    return than, ld


# ================================================================ 4. XEM LIEN HE
def trang_lien_he():
    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Liên hệ</div>
  <h1>Liên hệ</h1>
  <p>Ba cách liên hệ, mỗi cách hợp với một loại việc. Chọn đúng cách thì được trả lời nhanh hơn.</p>
</div></div>

<div class="than"><div class="wrap">

  <h2 style="margin-bottom:12px">Ba cách liên hệ</h2>
  <div class="kenh">
    <div class="b">
      <span class="nh nh-sau">Nên dùng nhất</span>
      <h3>Gửi qua biểu mẫu tư vấn</h3>
      <p>Cách này giúp chúng tôi nắm đủ bối cảnh trước khi trả lời, nên phản hồi thường dùng được ngay
      thay vì phải hỏi đi hỏi lại.</p>
      <div class="dm">Phản hồi: <b>trong 24 giờ làm việc</b></div>
      <p style="margin-top:12px"><a href="../tu-van/index.html" style="font-weight:700">Mở biểu mẫu tư vấn →</a></p>
    </div>
    <div class="b">
      <span class="nh nh-nhanh">Việc gấp</span>
      <h3>Gọi điện trực tiếp</h3>
      <p>Hợp với việc có mốc phải kịp trong vài ngày, hoặc khi cần hỏi nhanh một điểm trước khi quyết định.</p>
      <div class="dm">Giờ làm việc: <b>Thứ Hai – Thứ Sáu, 8g00 – 17g30</b></div>
      <p style="margin-top:13px"><a href="tel:0825092007" class="so-lon">08 2509 2007</a></p>
      <p class="small" style="margin-top:4px;margin-bottom:0">Số này cũng dùng được trên
      <a href="https://zalo.me/0825092007" rel="noopener">Zalo</a> — nhắn tin ngoài giờ, chúng tôi đọc vào đầu giờ sáng.</p>
    </div>
    <div class="b">
      <span class="nh nh-cham">Việc phức tạp</span>
      <h3>Đặt lịch trao đổi</h3>
      <p>Với dự án đang vướng ở nhiều khâu cùng lúc, một buổi trao đổi thường hiệu quả hơn nhiều lần
      hỏi đáp qua thư. Có thể trao đổi trực tuyến hoặc tại trụ sở của Quý vị.</p>
      <div class="dm">Thời lượng: <b>60 đến 90 phút</b></div>
      <p class="small" style="margin-top:12px;margin-bottom:0">Đặt lịch bằng một trong hai cách:
      nhắn <a href="https://zalo.me/0825092007" rel="noopener">Zalo 08 2509 2007</a>,
      hoặc điền <a href="../tu-van/index.html">biểu mẫu tư vấn</a> và chọn loại yêu cầu
      <i>“Vướng mắc có nhiều tình tiết”</i>.</p>
    </div>
  </div>

  <h2 style="margin:30px 0 12px">Trụ sở</h2>
  <div class="luoi g2">
    <div class="the">
      <h3>Hãng Kiểm toán và Định giá ASCO</h3>
      <p style="margin-top:8px;font-size:15.6px;color:var(--chu)">
        Tòa nhà ASCO, số 2, ngõ 308, phố Lê Trọng Tấn,<br>
        phường Phương Liệt, thành phố Hà Nội
      </p>
      <div class="dm" style="margin-top:12px;font-size:14.2px;color:var(--chu2);
        border-top:1px solid var(--vien);padding-top:9px">
        Điện thoại và Zalo: <a href="tel:0825092007"><b>08 2509 2007</b></a>
      </div>
    </div>
    <div class="the">
      <h3>Trao đổi trực tuyến cũng được</h3>
      <p style="margin-top:8px">Với đơn vị ở xa Hà Nội, phần lớn buổi trao đổi làm trực tuyến —
      nhanh hơn và không ai phải đi lại. Chúng tôi gửi đường dẫn phòng họp sau khi chốt giờ.</p>
      <p style="margin-top:10px;font-size:14.6px;color:var(--chu2)">Nếu Quý vị muốn gặp trực tiếp tại
      trụ sở của mình, xin nêu rõ khi đặt lịch để chúng tôi bố trí người đi.</p>
    </div>
  </div>

  <h2 style="margin:30px 0 12px">Chọn cách nào cho việc gì</h2>
  <div class="bang-boc">
    <table>
      <thead><tr><th style="width:42%">Việc của Quý vị</th><th style="width:26%">Nên dùng</th><th>Vì sao</th></tr></thead>
      <tbody>
        <tr><td>Hỏi một điểm về căn cứ pháp lý</td><td><b>Biểu mẫu</b></td>
          <td>Trả lời bằng văn bản có dẫn số hiệu, Quý vị lưu lại được</td></tr>
        <tr><td>Sắp đến hạn trình thẩm tra, cần hỏi gấp</td><td><b>Gọi điện</b></td>
          <td>Không mất thời gian chờ thư qua lại</td></tr>
        <tr><td>Dự án vướng nhiều khâu, chưa biết bắt đầu từ đâu</td><td><b>Đặt lịch</b></td>
          <td>Cần nhìn tổng thể mới gỡ được, thư từ không đủ</td></tr>
        <tr><td>Muốn rà soát cả bộ hồ sơ trước khi quyết toán</td><td><b>Biểu mẫu</b>, chọn loại thứ ba</td>
          <td>Đây là công việc có phạm vi riêng, cần thoả thuận trước</td></tr>
        <tr><td>Góp ý về nội dung trên trang này</td><td><b>Biểu mẫu</b></td>
          <td>Chúng tôi sửa và ghi nhận nguồn góp ý</td></tr>
      </tbody>
    </table>
  </div>

  <h2 style="margin:30px 0 12px">Câu hỏi hay gặp trước khi liên hệ</h2>
  <details><summary>Có mất phí không?</summary>
    <p>Trả lời một điểm cụ thể thì không. Việc phải đọc hồ sơ hoặc rà soát cả bộ hồ sơ dự án là công việc
    có phạm vi và thời gian riêng, hai bên thoả thuận trước khi bắt đầu.</p></details>
  <details><summary>Tôi không thuộc Ban Quản lý dự án, có hỏi được không?</summary>
    <p>Được. Trang này phục vụ cán bộ Ban Quản lý dự án, chủ đầu tư, đơn vị tư vấn và nhà thầu.
    Xin nêu rõ vai trò của Quý vị trong dự án để chúng tôi trả lời đúng góc nhìn.</p></details>
  <details><summary>Dự án của tôi không phải đường sắt đô thị thì sao?</summary>
    <p>Nhiều nội dung trên trang — quản lý chi phí, hợp đồng, quyết toán vốn đầu tư — áp dụng chung cho
    dự án đầu tư công. Phần riêng của đường sắt đô thị là cơ chế đặc thù và quy chuẩn kỹ thuật.
    Xin nêu rõ loại dự án khi gửi câu hỏi.</p></details>
  <details><summary>Tôi cần gửi tài liệu, gửi thế nào cho an toàn?</summary>
    <p>Đừng đính kèm tài liệu ở lần liên hệ đầu. Sau khi trao đổi và xác định phạm vi, hai bên thống nhất
    cách gửi và ký thoả thuận bảo mật nếu cần.</p></details>
  <details><summary>Bao lâu thì được trả lời?</summary>
    <p>Phản hồi lần đầu trong 24 giờ làm việc. Với tình huống nhiều tình tiết, phản hồi lần đầu là xác nhận
    đã nhận và nêu hướng sơ bộ, trả lời đầy đủ trong 2 đến 3 ngày làm việc.</p></details>

  <div class="the" style="margin-top:24px;border-left:3px solid var(--muc3)">
    <h3>Một lưu ý về phạm vi</h3>
    <p style="margin-top:8px">Nội dung trên trang này là thông tin tham khảo chuyên môn, không thay thế
    ý kiến tư vấn chính thức cho một dự án cụ thể và không phải là căn cứ pháp lý. Văn bản pháp luật
    thay đổi thường xuyên — trước khi dùng làm căn cứ, luôn đối chiếu bản gốc trên Công báo.</p>
  </div>

</div></div>
"""
    ld = [{"@context": "https://schema.org", "@type": "ContactPage", "name": "Liên hệ",
           "url": B.GOC + "/lien-he/",
           "description": "Ba cách liên hệ về dự án đường sắt đô thị: biểu mẫu tư vấn, gọi điện và đặt lịch trao đổi."},
          {"@context": "https://schema.org", "@type": "Organization",
           "name": "Hãng Kiểm toán và Định giá ASCO",
           "url": B.GOC + "/",
           "telephone": "+84825092007",
           "address": {"@type": "PostalAddress",
                       "streetAddress": "Tòa nhà ASCO, số 2, ngõ 308, phố Lê Trọng Tấn",
                       "addressLocality": "Phường Phương Liệt",
                       "addressRegion": "Thành phố Hà Nội",
                       "addressCountry": "VN"},
           "contactPoint": {"@type": "ContactPoint", "telephone": "+84825092007",
                            "contactType": "customer support", "availableLanguage": "Vietnamese"}},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": "Có mất phí không?", "acceptedAnswer": {"@type": "Answer",
               "text": "Trả lời một điểm cụ thể thì không. Việc phải đọc hồ sơ hoặc rà soát cả bộ hồ sơ dự án là công việc có phạm vi và thời gian riêng, hai bên thoả thuận trước."}},
              {"@type": "Question", "name": "Bao lâu thì được trả lời?", "acceptedAnswer": {"@type": "Answer",
               "text": "Phản hồi lần đầu trong 24 giờ làm việc. Với tình huống nhiều tình tiết, trả lời đầy đủ trong 2 đến 3 ngày làm việc."}},
              {"@type": "Question", "name": "Tôi cần gửi tài liệu, gửi thế nào cho an toàn?", "acceptedAnswer": {"@type": "Answer",
               "text": "Đừng đính kèm tài liệu ở lần liên hệ đầu. Sau khi xác định phạm vi, hai bên thống nhất cách gửi và ký thoả thuận bảo mật nếu cần."}}]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Liên hệ", "item": B.GOC + "/lien-he/"}]}]
    return than, ld


# ---------------------------------------------------------- ghi de
_MAP = {'van-ban': trang_van_ban, 'tu-van': trang_tu_van, 'lien-he': trang_lien_he}
P2.TRANG = [(s, td, mt, _MAP.get(s, fn), tang) for s, td, mt, fn, tang in P2.TRANG]

for i, (s, td, mt, fn, tang) in enumerate(P2.TRANG):
    if s == 'tu-van':
        P2.TRANG[i] = (s, 'Gửi yêu cầu tư vấn dự án đường sắt đô thị',
                       'Ba loại yêu cầu tư vấn, biểu mẫu gửi và quy trình phản hồi trong 24 giờ làm việc. Nêu rõ nên gửi gì và chưa cần gửi gì.', fn, tang)
    if s == 'lien-he':
        P2.TRANG[i] = (s, 'Liên hệ — Đường sắt đô thị',
                       'Ba cách liên hệ: biểu mẫu tư vấn, gọi điện, đặt lịch trao đổi. Kèm bảng chọn cách nào cho việc gì.', fn, tang)

if __name__ == '__main__':
    P2.ghi()
