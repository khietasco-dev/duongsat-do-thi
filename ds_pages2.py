# -*- coding: utf-8 -*-
"""Trang van ban, kinh nghiem, vuong mac, tu van, lien he + ham ghi file."""
import io, os, json, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages as P

VB, N = P.VB, P.N


import unicodedata


def bo_dau(s):
    """Bo dau tieng Viet de tim kiem khong phu thuoc dau."""
    s = s.replace('đ', 'd').replace('Đ', 'D')
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn').lower()


# ============================================================ 3. VAN BAN
def trang_van_ban():
    LOP = {'Luật & Nghị quyết QH': 'tl-luat', 'Nghị định': 'tl-nd',
           'Thông tư': 'tl-tt', 'Văn bản khác': 'tl-khac'}
    hang = []
    for d in sorted(VB, key=lambda x: (x['ngan'], x['hien'])):
        tt = ('<span class="the-loc" style="background:var(--do-nen);color:var(--do)">Hết hiệu lực</span>'
              if d['hethieuluc'] else
              '<span class="the-loc" style="background:var(--ngoc-nen);color:var(--ngoc)">Còn hiệu lực</span>')
        hn = ' <span class="the-loc tl-tt">Hợp nhất</span>' if d['hopnhat'] else ''
        dd = ' · '.join(x.upper() for x in d['dinhdang'])
        hang.append(
            '<tr data-ngan="%s" data-dia="%s" data-nam="%s" data-tt="%s" data-tim="%s">'
            '<td><span class="the-loc %s">%s</span></td><td>%s%s</td><td>%s</td>'
            '<td>%s</td><td>%s</td><td class="dinh">%s</td></tr>'
            % (html.escape(d['ngan']), html.escape(d['diaban']), d['nam'],
               'het' if d['hethieuluc'] else 'con',
               html.escape(bo_dau(d['hien'] + ' ' + d['diaban'])),
               LOP[d['ngan']], html.escape(d['ngan'].replace(' & Nghị quyết QH', '')),
               html.escape(d['hien']), hn, html.escape(d['diaban']),
               d['nam'] or '—', tt, dd))

    nams = sorted({d['nam'] for d in VB if d['nam']}, reverse=True)
    opt = lambda xs: ''.join('<option>%s</option>' % html.escape(x) for x in xs)

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Cập nhật văn bản</div>
  <h1>Cập nhật văn bản pháp luật đường sắt đô thị</h1>
  <p>%d đầu văn bản, 110 tệp — Luật, Nghị quyết Quốc hội, Nghị định, Thông tư, quy chuẩn kỹ thuật
  và văn bản của Hà Nội, TP. Hồ Chí Minh. Đối chiếu từ Công báo Chính phủ và Cổng Thông tin điện tử
  Chính phủ, không lấy từ trang tổng hợp.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--nhan);margin-bottom:22px">
    <h3>Ba văn bản trục — đọc trước tiên</h3>
    <p style="margin-top:9px">
      <b>Nghị quyết 188/2025/QH15</b> thí điểm cơ chế đặc thù phát triển đường sắt đô thị Hà Nội và
      TP. Hồ Chí Minh. Nhiều bước trình tự đã được rút gọn hợp pháp so với dự án đầu tư công thông thường —
      <b>làm dự án metro ở hai địa bàn này mà không đọc văn bản đó thì sẽ áp nhầm trình tự.</b><br><br>
      <b>VBHN 75/VBHN-VPQH</b> — bản hợp nhất Luật Đường sắt, bản nên đọc thay cho bản gốc.<br>
      <b>VBHN 34/VBHN-BXD</b> — bản hợp nhất Nghị định về thiết kế kỹ thuật tổng thể và cơ chế đặc thù, 143 Điều.
    </p>
  </div>

  <h2 style="margin-bottom:14px">Tra cứu văn bản</h2>

  <div class="loc">
    <div class="loc-hang">
      <div class="loc-o" style="flex:2 1 250px">
        <label for="q">Tìm theo tên hoặc số hiệu</label>
        <input id="q" type="search" placeholder="gõ có dấu hay không dấu đều được: TOD, metro, 188, không gian ngầm…" autocomplete="off">
      </div>
      <div class="loc-o"><label for="f-ngan">Cấp văn bản</label>
        <select id="f-ngan"><option value="">Tất cả</option>%s</select></div>
      <div class="loc-o"><label for="f-dia">Địa bàn</label>
        <select id="f-dia"><option value="">Tất cả</option>%s</select></div>
      <div class="loc-o"><label for="f-nam">Năm</label>
        <select id="f-nam"><option value="">Tất cả</option>%s</select></div>
      <div class="loc-o"><label for="f-tt">Hiệu lực</label>
        <select id="f-tt"><option value="">Tất cả</option>
        <option value="con">Còn hiệu lực</option><option value="het">Hết hiệu lực</option></select></div>
    </div>
    <div class="loc-dem" id="dem"></div>
  </div>

  <div class="bang-boc">
    <table id="bang">
      <thead><tr><th style="width:112px">Cấp</th><th>Tên văn bản</th>
      <th style="width:126px">Địa bàn</th><th style="width:66px">Năm</th>
      <th style="width:118px">Hiệu lực</th><th style="width:92px">Định dạng</th></tr></thead>
      <tbody>%s</tbody>
    </table>
  </div>
  <p class="small" id="rong" hidden>Không có văn bản nào khớp. Thử bỏ bớt điều kiện lọc.</p>

  <h2 style="margin:30px 0 14px">Lưu ý khi dùng</h2>
  <div class="luoi g2">
    <div class="the" style="border-left:3px solid var(--do)">
      <h3>Ba chỗ hồ sơ hay dẫn sai</h3>
      <p style="margin-top:8px">
      <b>Một —</b> Luật Đường sắt có cả bản <b>06/2017/QH14</b> và bản <b>95/2025/QH15</b> cùng hiện
      trên kết quả tìm kiếm. Luật Thủ đô nay là <b>02/2026/QH16</b>, không còn 39/2024/QH15.<br><br>
      <b>Hai —</b> Nghị quyết 188/2025 <b>không áp dụng cho Phú Quốc</b>. Ba văn bản Phú Quốc trong kho
      là nhóm bối cảnh, không phải căn cứ áp dụng cơ chế đặc thù đường sắt đô thị.<br><br>
      <b>Ba —</b> 14 văn bản của Hội đồng nhân dân và Uỷ ban nhân dân địa phương là <b>bản trích xuất</b>,
      tra nhanh được nhưng khi trích dẫn chính thức phải lấy bản gốc.</p>
    </div>
    <div class="the" style="border-left:3px solid var(--nhan)">
      <h3>Về định dạng tệp</h3>
      <p style="margin-top:8px">
      <b>39 văn bản có cả bản Word và PDF; 12 văn bản chỉ có PDF</b> — không phải thiếu sót mà vì nguồn
      chính thức không phát hành bản Word, trong đó có cả Nghị quyết 188/2025 và Luật Thủ đô 02/2026.<br><br>
      Văn bản dài được Công báo đăng nhiều kỳ. Kho lấy cả hai định dạng từ cùng một nguồn để số phần
      khớp nhau — <b>mở một phần là mất phần sau</b>.</p>
    </div>
  </div>

</div></div>
""" % (N, opt(['Luật & Nghị quyết QH', 'Nghị định', 'Thông tư', 'Văn bản khác']),
       opt(['Toàn quốc', 'Hà Nội', 'TP. Hồ Chí Minh', 'Phú Quốc']),
       opt(nams), '\n'.join(hang))

    ld = [{"@context": "https://schema.org", "@type": "CollectionPage",
           "name": "Cập nhật văn bản pháp luật đường sắt đô thị",
           "url": B.GOC + "/van-ban/",
           "description": "%d đầu văn bản về đường sắt đô thị và TOD: Luật, Nghị quyết Quốc hội, Nghị định, Thông tư, quy chuẩn kỹ thuật và văn bản địa phương." % N},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Cập nhật văn bản", "item": B.GOC + "/van-ban/"}]}]
    return than, ld


B.than_js['van-ban'] = """
<script>
(function(){
 var q=document.getElementById('q'),fn=document.getElementById('f-ngan'),fd=document.getElementById('f-dia'),
     fy=document.getElementById('f-nam'),ft=document.getElementById('f-tt'),
     rows=[].slice.call(document.querySelectorAll('#bang tbody tr')),
     dem=document.getElementById('dem'),rong=document.getElementById('rong');
 function bd(x){ return x.normalize('NFD').replace(/[\u0300-\u036f]/g,'')
   .replace(/đ/g,'d').replace(/Đ/g,'D').toLowerCase(); }
 function loc(){
  var s=bd(q.value.trim()),n=fn.value,d=fd.value,y=fy.value,t=ft.value,c=0;
  for(var i=0;i<rows.length;i++){var r=rows[i];
   var ok=(!s||r.getAttribute('data-tim').indexOf(s)>-1)&&(!n||r.getAttribute('data-ngan')===n)
     &&(!d||r.getAttribute('data-dia')===d)&&(!y||r.getAttribute('data-nam')===y)
     &&(!t||r.getAttribute('data-tt')===t);
   r.hidden=!ok; if(ok)c++;}
  dem.innerHTML='Đang hiện <b>'+c+'</b> trên tổng '+rows.length+' văn bản.';
  rong.hidden=c>0;
 }
 [q,fn,fd,fy,ft].forEach(function(e){e.addEventListener('input',loc);});
 loc();
})();
</script>"""


# ============================================================ 4. KINH NGHIEM
BAI_HOC = [
    ("Chốt phạm vi công việc trước khi ký hợp đồng EPC",
     "Hợp đồng EPC với nhà thầu nước ngoài thường dùng mẫu quốc tế, mô tả phạm vi theo kết quả đầu ra "
     "chứ không theo khối lượng chi tiết. Đến lúc quyết toán, cơ quan thẩm tra cần bảng khối lượng để "
     "đối chiếu thì không có. Nên thoả thuận ngay trong hợp đồng rằng nhà thầu phải cung cấp bảng khối "
     "lượng theo mẫu hồ sơ quyết toán trong nước, coi đó là một phần nghĩa vụ hợp đồng."),
    ("Lập hồ sơ nghiệm thu đồng thời với thi công",
     "Đây là bài học lặp lại ở gần như mọi dự án hạ tầng lớn. Hồ sơ để dồn đến cuối thì người ký đã "
     "chuyển công tác, nhà thầu phụ đã giải thể, ảnh hiện trường không còn. Ban Quản lý dự án nên đặt "
     "một mốc kiểm hồ sơ định kỳ theo quý, coi hồ sơ là sản phẩm phải nghiệm thu chứ không phải thủ tục."),
    ("Xin ý kiến bằng văn bản với mọi khoản chi phí bất thường",
     "Chi phí không tính vào giá trị tài sản, chi phí do nguyên nhân bất khả kháng, chi phí phát sinh "
     "ngoài hợp đồng — tất cả đều cần quyết định của cấp có thẩm quyền. Xin muộn thì hồ sơ treo, "
     "và người phê duyệt sau này không dám ký cho việc đã xảy ra nhiều năm trước."),
    ("Xác định sớm căn cứ áp dụng tiêu chuẩn nước ngoài",
     "Dự án đường sắt đô thị thường dùng tiêu chuẩn châu Âu hoặc Nhật Bản theo yêu cầu của nhà tài trợ. "
     "Việc lựa chọn áp dụng tiêu chuẩn nước ngoài phải có căn cứ và được cấp thẩm quyền chấp thuận — "
     "Hà Nội đã có nghị quyết riêng về nội dung này. Làm sau thì mọi hạng mục đã nghiệm thu bị đặt câu hỏi."),
    ("Tách bạch chi phí của phần TOD và phần tuyến",
     "Khi dự án gắn với khu vực TOD, dòng tiền và tài sản của hai phần dễ trộn vào nhau. Việc tách bạch "
     "phải làm từ khâu lập dự án, vì đến lúc bàn giao tài sản mới tách thì không còn chứng từ để chia."),
    ("Chuẩn bị nhân lực vận hành từ giai đoạn thi công",
     "Đào tạo nhân lực vận hành và tiếp nhận chuyển giao công nghệ cần thời gian dài hơn nhiều so với "
     "dự kiến. Bắt đầu khi công trình sắp xong là muộn, và chi phí đào tạo phát sinh về sau thường "
     "không nằm trong tổng mức đầu tư được duyệt."),
]


def trang_kinh_nghiem():
    kh = ''.join(
        '<div class="the" style="border-left:3px solid var(--muc3);margin-bottom:16px">'
        '<h3>%d. %s</h3><p style="margin-top:9px">%s</p></div>'
        % (i + 1, html.escape(t), html.escape(n)) for i, (t, n) in enumerate(BAI_HOC))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Kinh nghiệm QLDA</div>
  <h1>Kinh nghiệm quản lý dự án đường sắt đô thị</h1>
  <p>Bài học rút ra ở tầm quy trình. Trọng tâm là những việc Ban Quản lý dự án nên làm sớm
  để không vướng ở khâu quyết toán sau này.</p>
</div></div>

<div class="than"><div class="wrap hep">

  <div class="the" style="border-left:3px solid var(--nhan);margin-bottom:24px">
    <h3>Nguyên tắc viết những bài này</h3>
    <p style="margin-top:8px">Không nêu tên dự án, tên đơn vị hay số liệu hợp đồng của khách hàng.
    Những gì đã được công bố công khai rộng rãi trên báo chí chính thống thì dẫn ở mức thông tin chung.
    Đây không phải quy tắc hình thức — nghĩa vụ bảo mật của nghề áp cả với bài viết chia sẻ kinh nghiệm
    tưởng chừng vô hại.</p>
  </div>

  <h2 style="margin-bottom:18px">Sáu việc nên làm sớm</h2>
  %s

  <div class="the" style="border-left:3px solid var(--ngoc);margin-top:8px">
    <h3>Nhìn chung lại</h3>
    <p style="margin-top:8px">Năm trong sáu bài học trên đều có chung một dạng: <b>việc đúng ra phải làm
    ở giai đoạn đầu, nhưng hậu quả chỉ lộ ra ở giai đoạn cuối</b>. Đó là lý do khâu quyết toán của
    dự án đường sắt đô thị thường kéo dài — không phải vì khâu quyết toán khó, mà vì nó phải dọn lại
    những gì các giai đoạn trước để lại.</p>
  </div>

</div></div>
""" % kh

    ld = [{"@context": "https://schema.org", "@type": "Article",
           "headline": "Kinh nghiệm quản lý dự án đường sắt đô thị",
           "description": "Sáu bài học ở tầm quy trình giúp Ban Quản lý dự án tránh vướng mắc ở khâu quyết toán vốn đầu tư.",
           "inLanguage": "vi-VN"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Kinh nghiệm QLDA", "item": B.GOC + "/kinh-nghiem/"}]}]
    return than, ld


# ============================================================ 5. VUONG MAC
VUONG = [
    ("Giải phóng mặt bằng chậm, chi phí bồi thường tăng so với phê duyệt",
     "Đơn giá bồi thường thay đổi trong thời gian kéo dài; phạm vi thu hồi phát sinh khi thiết kế điều chỉnh.",
     "Luật Đất đai và các nghị quyết của Hội đồng nhân dân địa phương về bồi thường, hỗ trợ, tái định cư.",
     "Lập phương án bồi thường theo từng đợt bàn giao thay vì một lần cho toàn tuyến; mỗi lần điều chỉnh "
     "đơn giá phải có quyết định của cấp có thẩm quyền kèm theo hồ sơ."),
    ("Điều chỉnh tổng mức đầu tư nhiều lần",
     "Sơ bộ tổng mức đầu tư lập khi chưa đủ dữ liệu kỹ thuật; biến động tỷ giá với phần vốn vay nước ngoài; "
     "kéo dài thời gian thực hiện.",
     "Luật Đầu tư công; quy định về quản lý chi phí đầu tư xây dựng.",
     "Mỗi lần điều chỉnh phải làm rõ nguyên nhân thuộc nhóm nào, vì nhóm nguyên nhân quyết định thẩm quyền "
     "phê duyệt điều chỉnh. Ghi lại đầy đủ hồ sơ từng lần, không gộp."),
    ("Hợp đồng EPC không có bảng khối lượng chi tiết",
     "Hợp đồng dùng mẫu quốc tế, mô tả phạm vi theo kết quả đầu ra.",
     "Luật Xây dựng; quy định về hợp đồng xây dựng và về quyết toán vốn đầu tư.",
     "Thoả thuận bổ sung nghĩa vụ cung cấp bảng khối lượng theo mẫu trong nước. Nếu hợp đồng đã ký thì "
     "làm phụ lục, xử lý sớm chừng nào tốt chừng đó."),
    ("Chi phí đánh giá an toàn hệ thống vượt dự kiến",
     "Đơn vị đánh giá độc lập nước ngoài, khối lượng công việc phát sinh khi hệ thống chưa đạt ngay lần đầu.",
     "Quy chuẩn kỹ thuật quốc gia về đường sắt đô thị loại hình metro.",
     "Đưa chi phí này vào tổng mức đầu tư ngay từ giai đoạn lập dự án, kèm dự phòng cho khả năng phải "
     "đánh giá lại."),
    ("Áp dụng tiêu chuẩn nước ngoài chưa có căn cứ",
     "Nhà tài trợ yêu cầu áp dụng tiêu chuẩn của nước cấp vốn, trong khi hồ sơ dự án chưa nêu căn cứ.",
     "Nghị quyết của Hội đồng nhân dân Hà Nội về lựa chọn áp dụng tiêu chuẩn, quy chuẩn kỹ thuật "
     "trong nước và nước ngoài.",
     "Xin chấp thuận bằng văn bản trước khi triển khai thiết kế. Đã lỡ thì hợp thức hoá càng sớm càng ít tốn kém."),
    ("Quyết toán dự án kéo dài nhiều năm, thiếu hồ sơ gốc",
     "Người ký chuyển công tác, nhà thầu phụ giải thể, hồ sơ lưu trữ phân tán qua nhiều lần thay đổi bộ máy.",
     "Quy định về quyết toán vốn đầu tư công dự án hoàn thành.",
     "Lập danh mục hồ sơ phải có ngay từ đầu dự án và kiểm theo quý. Với hồ sơ đã mất, lập biên bản "
     "xác nhận của các bên còn lại kèm bằng chứng gián tiếp, xin ý kiến cơ quan thẩm tra sớm."),
    ("Chi phí không tính vào giá trị tài sản chưa được cho phép",
     "Thiệt hại do nguyên nhân bất khả kháng, chi phí của hạng mục bị huỷ bỏ, chi phí chạy thử không đạt.",
     "Quy định về quyết toán vốn đầu tư; hồ sơ kiểm toán mẫu báo cáo quyết toán dự án hoàn thành.",
     "Phải có quyết định của cấp có thẩm quyền cho phép không tính vào giá trị tài sản. Không có văn bản "
     "thì khoản đó treo, không quyết toán được."),
    ("Tài sản bàn giao cho nhiều đơn vị quản lý khác nhau",
     "Phần tuyến, phần nhà ga, phần depot và phần hạ tầng kỹ thuật đi kèm thuộc các đầu mối quản lý khác nhau.",
     "Quy định về quản lý, sử dụng và khai thác tài sản kết cấu hạ tầng đường sắt.",
     "Lập phương án phân giao tài sản từ giai đoạn chuẩn bị nghiệm thu, không đợi đến khi quyết toán xong."),
    ("Khai thác giá trị tăng thêm từ đất khu vực TOD",
     "Cơ chế thu và phân chia nguồn thu từ quỹ đất TOD còn mới, các bên hiểu khác nhau.",
     "Nghị quyết của Hội đồng nhân dân Hà Nội và TP. Hồ Chí Minh về quy hoạch khu vực TOD và các khoản thu "
     "từ khai thác giá trị tăng thêm.",
     "Xác định ranh giới khu vực TOD và cơ chế phân chia nguồn thu bằng văn bản trước khi triển khai, "
     "vì đây là nội dung mỗi địa phương quy định khác nhau."),
    ("Chi phí đào tạo và chuyển giao công nghệ phát sinh",
     "Thời gian đào tạo dài hơn dự kiến; nhân sự được đào tạo nghỉ việc trước khi tuyến đi vào khai thác.",
     "Đề án đào tạo, phát triển nguồn nhân lực đường sắt; nội dung chuyển giao công nghệ trong Nghị quyết 188/2025.",
     "Đưa cam kết thời gian làm việc tối thiểu vào hợp đồng lao động của người được cử đi đào tạo; "
     "tính chi phí đào tạo vào tổng mức đầu tư ngay từ đầu."),
]


def trang_vuong_mac():
    kh = ''.join(
        '<details><summary>%d. %s</summary>'
        '<p><b>Vì sao phát sinh — </b>%s</p>'
        '<p><b>Căn cứ liên quan — </b>%s</p>'
        '<p style="color:var(--ngoc)"><b>Hướng xử lý — </b>%s</p></details>'
        % (i + 1, html.escape(t), html.escape(a), html.escape(b), html.escape(c))
        for i, (t, a, b, c) in enumerate(VUONG))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Vướng mắc</div>
  <h1>Mười vướng mắc thường gặp</h1>
  <p>Mỗi tình huống nêu nguyên nhân phát sinh, căn cứ pháp lý liên quan và hướng xử lý.
  Bấm vào từng mục để mở nội dung.</p>
</div></div>

<div class="than"><div class="wrap hep">
  %s

  <div class="the" style="border-left:3px solid var(--nhan);margin-top:24px">
    <h3>Không thấy tình huống của mình ở đây?</h3>
    <p style="margin-top:8px">Gửi câu hỏi qua trang <a href="../tu-van/index.html">Tư vấn</a>. Chúng tôi trả lời
    riêng cho Quý vị, và nếu câu hỏi có giá trị chung thì biên tập lại thành một mục trên trang này —
    <b>không nêu tên đơn vị hỏi</b>.</p>
  </div>
</div></div>
""" % kh

    ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": t, "acceptedAnswer": {"@type": "Answer", "text": a + " " + c}}
        for t, a, b, c in VUONG]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
            {"@type": "ListItem", "position": 2, "name": "Vướng mắc", "item": B.GOC + "/vuong-mac/"}]}]
    return than, ld


# ============================================================ 6. TU VAN
def trang_tu_van():
    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Tư vấn</div>
  <h1>Gửi yêu cầu tư vấn</h1>
  <p>Mô tả tình huống của dự án. Chúng tôi phản hồi trong 24 giờ làm việc.</p>
</div></div>

<div class="than"><div class="wrap hep">

  <div class="luoi g3" style="margin-bottom:26px">
    <div class="the"><h3>Trước khi gửi</h3><p>Nêu rõ dự án ở giai đoạn nào và vướng ở khâu nào.
    Càng cụ thể thì trả lời càng dùng được ngay.</p></div>
    <div class="the"><h3>Về bảo mật</h3><p>Không cần gửi tài liệu mật ở bước này. Mô tả tình huống
    là đủ để chúng tôi biết vấn đề thuộc nhóm nào.</p></div>
    <div class="the"><h3>Phạm vi trả lời</h3><p>Ý kiến ở đây là thông tin tham khảo, không thay thế
    tư vấn chính thức cho một dự án cụ thể.</p></div>
  </div>

  <h2 style="margin-bottom:14px">Biểu mẫu</h2>
  <div class="mau">
    <form class="mau-luoi" id="mau" novalidate>
      <div class="truong"><label for="t1">Họ và tên</label><input id="t1" type="text" required></div>
      <div class="truong"><label for="t2">Chức vụ</label><input id="t2" type="text"></div>
      <div class="truong"><label for="t3">Đơn vị công tác</label><input id="t3" type="text" required></div>
      <div class="truong"><label for="t4">Điện thoại</label><input id="t4" type="tel" required></div>
      <div class="truong"><label for="t5">Email</label><input id="t5" type="email"></div>
      <div class="truong"><label for="t6">Địa bàn dự án</label>
        <select id="t6"><option value="">— Chọn —</option><option>Hà Nội</option>
        <option>TP. Hồ Chí Minh</option><option>Địa bàn khác</option></select></div>
      <div class="truong"><label for="t7">Dự án đang ở giai đoạn nào</label>
        <select id="t7"><option value="">— Chọn —</option>
        <option>Chủ trương đầu tư</option><option>Chuẩn bị dự án</option>
        <option>Giải phóng mặt bằng</option><option>Lựa chọn nhà thầu</option>
        <option>Thi công xây dựng</option><option>Nghiệm thu, chạy thử</option>
        <option>Quyết toán vốn đầu tư</option></select></div>
      <div class="truong"><label for="t8">Nhóm vướng mắc</label>
        <select id="t8"><option value="">— Chọn —</option>
        <option>Trình tự, thủ tục đầu tư</option><option>Giải phóng mặt bằng</option>
        <option>Hợp đồng và thanh toán</option><option>Nghiệm thu, hồ sơ hoàn công</option>
        <option>Quyết toán vốn đầu tư</option><option>TOD và khai thác quỹ đất</option>
        <option>Khác</option></select></div>
      <div class="truong rong"><label for="t9">Mô tả tình huống</label>
        <textarea id="t9" required placeholder="Dự án đang vướng ở đâu, đã xử lý những gì, cần hỗ trợ điều gì…"></textarea></div>
      <div class="rong">
        <button class="nut-gui" type="submit">Gửi yêu cầu</button>
        <p class="small" id="kq" style="margin-top:11px"></p>
      </div>
    </form>
  </div>

</div></div>
"""
    ld = [{"@context": "https://schema.org", "@type": "ContactPage",
           "name": "Gửi yêu cầu tư vấn dự án đường sắt đô thị", "url": B.GOC + "/tu-van/"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Tư vấn", "item": B.GOC + "/tu-van/"}]}]
    return than, ld


B.than_js['tu-van'] = """
<script>
(function(){var f=document.getElementById('mau'),k=document.getElementById('kq');
f.addEventListener('submit',function(e){e.preventDefault();
 var ids=['t1','t3','t4','t9'],thieu=[];
 for(var i=0;i<ids.length;i++){if(!document.getElementById(ids[i]).value.trim())thieu.push(ids[i]);}
 if(thieu.length){k.textContent='Xin điền đủ họ tên, đơn vị, điện thoại và mô tả tình huống.';
  k.style.color='var(--do)';document.getElementById(thieu[0]).focus();return;}
 k.style.color='var(--ngoc)';
 k.textContent='Biểu mẫu chưa nối dịch vụ nhận. Xin liên hệ theo thông tin ở trang Liên hệ.';});
})();
</script>"""


# ============================================================ 7. LIEN HE
def trang_lien_he():
    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Liên hệ</div>
  <h1>Liên hệ</h1>
  <p>Trao đổi trực tiếp là nhanh nhất với những tình huống phức tạp.</p>
</div></div>

<div class="than"><div class="wrap hep">
  <h2 style="margin-bottom:16px">Hai cách liên hệ</h2>
  <div class="luoi g2">
    <div class="the">
      <h3>Gửi yêu cầu qua biểu mẫu</h3>
      <p style="margin-top:8px">Cách này giúp chúng tôi nắm đủ bối cảnh trước khi trả lời,
      nên phản hồi thường dùng được ngay.</p>
      <p style="margin-top:12px"><a class="di" href="../tu-van/index.html" style="text-decoration:none">Mở biểu mẫu tư vấn →</a></p>
    </div>
    <div class="the">
      <h3>Đặt lịch trao đổi</h3>
      <p style="margin-top:8px">Với dự án đang vướng ở nhiều khâu cùng lúc, một buổi trao đổi
      thường hiệu quả hơn nhiều lần hỏi đáp qua thư.</p>
      <div class="oTrong" style="margin-top:12px;background:var(--nen2);border:1px dashed var(--nhan);
        border-radius:10px;padding:13px 15px">
        <b style="display:block;font-size:12px;letter-spacing:.09em;text-transform:uppercase;
        color:var(--nhan2);margin-bottom:4px">Cần điền</b>
        <span class="small">Số điện thoại, địa chỉ và hộp thư của đơn vị cần điền trước khi trang chạy thật.</span>
      </div>
    </div>
  </div>

  <div class="the" style="margin-top:22px;border-left:3px solid var(--muc3)">
    <h3>Một lưu ý về phạm vi</h3>
    <p style="margin-top:8px">Nội dung trên trang này là thông tin tham khảo chuyên môn, không thay thế
    ý kiến tư vấn chính thức cho một dự án cụ thể và không phải là căn cứ pháp lý. Văn bản pháp luật
    thay đổi thường xuyên — trước khi dùng làm căn cứ, luôn đối chiếu bản gốc trên Công báo.</p>
  </div>
</div></div>
"""
    ld = [{"@context": "https://schema.org", "@type": "ContactPage",
           "name": "Liên hệ", "url": B.GOC + "/lien-he/"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Liên hệ", "item": B.GOC + "/lien-he/"}]}]
    return than, ld


# ============================================================ GHI FILE
TRANG = [
    ('',            'Đường sắt đô thị — Văn bản, quy trình, kinh nghiệm QLDA',
     'Tra cứu %d đầu văn bản pháp luật đường sắt đô thị và TOD, quy trình thực hiện dự án bảy giai đoạn, mười vướng mắc thường gặp.' % N,
     P.trang_dich, 'ngoai'),
    ('van-ban',     'Cập nhật văn bản pháp luật đường sắt đô thị và TOD',
     'Tra cứu %d đầu văn bản: Luật, Nghị quyết Quốc hội, Nghị định, Thông tư, quy chuẩn kỹ thuật và văn bản Hà Nội, TP. Hồ Chí Minh.' % N,
     trang_van_ban, 'trong'),
    ('quy-trinh',   'Quy trình thực hiện dự án đường sắt đô thị — bảy giai đoạn',
     'Bảy giai đoạn từ chủ trương đầu tư đến quyết toán vốn đầu tư, kèm thẩm quyền quyết định, căn cứ pháp lý và vướng mắc hay gặp.',
     P.trang_quy_trinh, 'trong'),
    ('kinh-nghiem', 'Kinh nghiệm quản lý dự án đường sắt đô thị',
     'Sáu bài học ở tầm quy trình giúp Ban Quản lý dự án tránh vướng mắc ở khâu quyết toán vốn đầu tư dự án hoàn thành.',
     trang_kinh_nghiem, 'trong'),
    ('vuong-mac',   'Mười vướng mắc thường gặp ở dự án đường sắt đô thị',
     'Mười tình huống hay gặp: giải phóng mặt bằng, điều chỉnh tổng mức đầu tư, hợp đồng EPC, quyết toán, TOD — kèm hướng xử lý.',
     trang_vuong_mac, 'trong'),
    ('tu-van',      'Gửi yêu cầu tư vấn dự án đường sắt đô thị',
     'Mô tả tình huống dự án đang vướng, chúng tôi phản hồi trong 24 giờ làm việc.',
     trang_tu_van, 'trong'),
    ('lien-he',     'Liên hệ — Đường sắt đô thị',
     'Cách gửi yêu cầu tư vấn và đặt lịch trao đổi về dự án đường sắt đô thị.',
     trang_lien_he, 'trong'),
]


def ghi():
    os.makedirs(B.KHO, exist_ok=True)
    ra = []
    for slug, td, mt, fn, tang in TRANG:
        than, ld = fn()
        h = B.khung(slug, td, mt, than, ld, tang)
        d = os.path.join(B.KHO, slug) if slug else B.KHO
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, 'index.html')
        io.open(p, 'w', encoding='utf-8').write(h)
        ra.append((slug or '(trang chủ)', len(h), len(td), len(mt)))
        print('  %-14s %7d byte   title %2d   desc %3d' % (slug or '.', len(h), len(td), len(mt)))

    # sitemap + robots
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for slug, td, mt, fn, tang in TRANG:
        u = B.GOC + '/' + (slug + '/' if slug else '')
        sm.append('  <url><loc>%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>'
                  % (u, 'weekly' if slug == 'van-ban' else 'monthly', '1.0' if not slug else '0.8'))
    sm.append('</urlset>')
    io.open(os.path.join(B.KHO, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
    io.open(os.path.join(B.KHO, 'robots.txt'), 'w', encoding='utf-8').write(
        'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % B.GOC)
    print('\nDa ghi %d trang + sitemap.xml + robots.txt' % len(TRANG))
    qua = [(s, t, d) for s, _, t, d in ra if t > 60 or d > 160]
    print('Vuot nguong SEO:', qua if qua else 'khong co')


if __name__ == '__main__':
    ghi()
