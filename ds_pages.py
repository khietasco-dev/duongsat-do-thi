# -*- coding: utf-8 -*-
"""Cac trang cua website Duong sat do thi. Nap khung tu ds_build.py."""
import io, os, json, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B

TM = os.path.dirname(os.path.abspath(__file__))
VB = json.load(io.open(os.path.join(TM, 'vb_phanloai.json'), encoding='utf-8'))
N = len(VB)


# ============================================================ 1. TRANG DICH
def trang_dich():
    than = """
<div class="hero">
  <div class="wrap">
    <span class="nhan-pill">Văn bản · Quy trình · Kinh nghiệm</span>
    <h1>Làm dự án đường sắt đô thị, đúng trình tự ngay từ đầu</h1>
    <p class="lede">
      Trang tra cứu dành cho cán bộ Ban Quản lý dự án, chủ đầu tư và đơn vị tư vấn.
      Tập hợp %d đầu văn bản đang điều chỉnh lĩnh vực đường sắt đô thị và TOD, sơ đồ trình tự
      thực hiện dự án theo từng giai đoạn, cùng những vướng mắc thường gặp ở khâu quyết toán.
    </p>
    <div class="hero-nut">
      <a class="n1" href="van-ban/index.html">Tra cứu văn bản</a>
      <a class="n2" href="quy-trinh/index.html">Xem quy trình dự án</a>
    </div>
    <div class="hero-so">
      <div><b>%d</b><span>Đầu văn bản đã rà soát</span></div>
      <div><b>110</b><span>Tệp Word và PDF</span></div>
      <div><b>9</b><span>Giai đoạn thực hiện dự án</span></div>
      <div><b>10</b><span>Vướng mắc thường gặp</span></div>
    </div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="dau">
      <div class="mac">Vấn đề</div>
      <h2>Cơ chế đặc thù đã đổi luật chơi, nhưng nhiều hồ sơ vẫn đi theo lối cũ</h2>
      <p>
        Nghị quyết 188/2025/QH15 cho phép rút gọn hợp pháp nhiều bước trình tự với dự án đường sắt
        đô thị tại Hà Nội và TP. Hồ Chí Minh. Ai không nắm thì áp nhầm trình tự của dự án đầu tư công
        thông thường — làm chậm chính mình, hoặc tệ hơn là bỏ sót thủ tục bắt buộc rồi vướng ở khâu quyết toán.
      </p>
    </div>
    <div class="luoi g3">
      <div class="the" style="border-top:3px solid var(--do)">
        <h3>Dẫn văn bản đã hết hiệu lực</h3>
        <p>Luật Đường sắt có cả bản 06/2017 và bản 95/2025 cùng hiện trên kết quả tìm kiếm.
        Luật Thủ đô nay là 02/2026/QH16 chứ không còn 39/2024. Dẫn nhầm là sai căn cứ ngay từ tờ trình.</p>
      </div>
      <div class="the" style="border-top:3px solid var(--hoacuc)">
        <h3>Áp nhầm phạm vi cơ chế đặc thù</h3>
        <p>Nghị quyết 188/2025 chỉ áp dụng cho Hà Nội và TP. Hồ Chí Minh. Địa bàn khác vận dụng
        cơ chế này là không có căn cứ.</p>
      </div>
      <div class="the" style="border-top:3px solid var(--ngoc)">
        <h3>Để dồn việc đến khâu quyết toán</h3>
        <p>Phần lớn vướng mắc lúc quyết toán bắt nguồn từ những việc lẽ ra phải làm dứt điểm
        ở giai đoạn chuẩn bị dự án và trong quá trình thi công.</p>
      </div>
    </div>
  </div>
</section>

<section class="nen2">
  <div class="wrap">
    <div class="dau">
      <div class="mac">Nội dung chính</div>
      <h2>Bốn mục tra cứu</h2>
    </div>
    <div class="luoi g2">
      <a class="the lienket" href="van-ban/index.html">
        <div class="ico"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg></div>
        <h3>Cập nhật văn bản</h3>
        <p>%d đầu văn bản chia bốn cấp, lọc theo địa bàn, năm ban hành và tình trạng hiệu lực.
        Có ô tìm theo tên hoặc số hiệu.</p>
        <div class="di">Mở trang tra cứu →</div>
      </a>
      <a class="the lienket" href="quy-trinh/index.html">
        <div class="ico"><svg viewBox="0 0 24 24"><path d="M3 12h4l3-9 4 18 3-9h4"/></svg></div>
        <h3>Quy trình thực hiện dự án</h3>
        <p>Chín giai đoạn từ quy hoạch tuyến đến quyết toán vốn đầu tư. Mỗi giai đoạn nêu rõ thẩm quyền
        quyết định, căn cứ pháp lý, sản phẩm đầu ra và vướng mắc hay gặp.</p>
        <div class="di">Xem quy trình →</div>
      </a>
      <a class="the lienket" href="kinh-nghiem/index.html">
        <div class="ico"><svg viewBox="0 0 24 24"><path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/></svg></div>
        <h3>Kinh nghiệm quản lý dự án</h3>
        <p>Mười hai việc nên làm sớm, danh mục kiểm tra theo từng thời điểm và ba sai lầm lặp lại
        nhiều nhất. Không nêu tên đơn vị nào.</p>
        <div class="di">Đọc bài học →</div>
      </a>
      <a class="the lienket" href="vuong-mac/index.html">
        <div class="ico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg></div>
        <h3>Vướng mắc thường gặp</h3>
        <p>Mười tình huống hay gặp, mỗi tình huống nêu nguyên nhân, căn cứ pháp lý và hướng xử lý.
        Gửi được câu hỏi riêng để chúng tôi trả lời thành bài.</p>
        <div class="di">Xem vướng mắc →</div>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="wrap hep">
    <div class="dau">
      <div class="mac">Nguồn dữ liệu</div>
      <h2>Vì sao dữ liệu ở đây đáng tin</h2>
    </div>
    <p>
      Toàn bộ văn bản được tải và đối chiếu từ <b>Công báo Chính phủ</b> và <b>Cổng Thông tin điện tử
      Chính phủ</b> — không lấy từ trang tổng hợp thương mại. Mỗi văn bản kiểm số hiệu bên trong nội dung
      chứ không chỉ tin vào tên tệp, và kiểm cả số trang để phát hiện trường hợp Công báo đăng nhiều kỳ
      mà chỉ tải được kỳ đầu.
    </p>
    <p>
      Những chỗ chưa chắc chắn đều được ghi rõ thay vì đoán. Ví dụ 14 văn bản của Hội đồng nhân dân và
      Uỷ ban nhân dân địa phương trong kho là <b>bản trích xuất</b>, dùng tra nhanh được nhưng khi trích dẫn
      chính thức thì phải lấy bản gốc.
    </p>
    <div class="luoi g2" style="margin-top:24px">
      <a class="the lienket" href="tu-van/index.html">
        <h3>Gửi yêu cầu tư vấn</h3>
        <p>Mô tả tình huống của dự án, chúng tôi trả lời trong 24 giờ làm việc.</p>
        <div class="di">Gửi yêu cầu →</div>
      </a>
      <a class="the lienket" href="lien-he/index.html">
        <h3>Liên hệ</h3>
        <p>Thông tin liên hệ và cách đặt lịch trao đổi trực tiếp.</p>
        <div class="di">Xem liên hệ →</div>
      </a>
    </div>
  </div>
</section>
""" % (N, N, N)

    ld = [{"@context": "https://schema.org", "@type": "WebSite",
           "name": "Đường sắt đô thị", "url": B.GOC + "/",
           "description": "Trang tra cứu văn bản, quy trình và kinh nghiệm quản lý dự án đường sắt đô thị tại Việt Nam."}]
    return than, ld


# ============================================================ 2. QUY TRINH
GIAI_DOAN = [
    ("Chủ trương đầu tư",
     "Lập, thẩm định và quyết định chủ trương đầu tư. Xác định sơ bộ tổng mức đầu tư, nguồn vốn và phương án tuyến.",
     "Quốc hội với dự án quan trọng quốc gia; Hội đồng nhân dân cấp tỉnh với dự án nhóm A do địa phương quản lý",
     "Luật Đầu tư công · NQ 188/2025/QH15 · Luật Thủ đô 02/2026/QH16",
     "Nghị quyết hoặc quyết định chủ trương đầu tư",
     "Sơ bộ tổng mức đầu tư lập khi chưa đủ dữ liệu kỹ thuật, dẫn tới phải điều chỉnh nhiều lần về sau."),
    ("Chuẩn bị dự án",
     "Lập báo cáo nghiên cứu khả thi, thiết kế kỹ thuật tổng thể, thẩm định và phê duyệt dự án.",
     "Người quyết định đầu tư theo phân cấp",
     "VBHN 34/VBHN-BXD về thiết kế kỹ thuật tổng thể · VBHN 75/VBHN-VPQH Luật Đường sắt",
     "Quyết định phê duyệt dự án · thiết kế kỹ thuật tổng thể",
     "Thiết kế kỹ thuật tổng thể thiếu dữ liệu chi phí nên dự toán không sát; lựa chọn tiêu chuẩn nước ngoài chưa có căn cứ áp dụng."),
    ("Giải phóng mặt bằng và tái định cư",
     "Thu hồi đất, bồi thường, hỗ trợ, bố trí tái định cư. Với dự án ngầm còn thêm phần không gian ngầm.",
     "Uỷ ban nhân dân cấp tỉnh",
     "Luật Đất đai · nghị quyết của Hội đồng nhân dân Hà Nội và TP. Hồ Chí Minh về TOD và không gian ngầm",
     "Bàn giao mặt bằng theo từng đợt",
     "Đây là khâu chậm nhất và là nguyên nhân gốc của phần lớn khiếu nại về kéo dài thời gian và phát sinh chi phí."),
    ("Lựa chọn nhà thầu",
     "Đấu thầu hoặc chỉ định thầu theo cơ chế được áp dụng; ký hợp đồng.",
     "Chủ đầu tư, người quyết định đầu tư theo phân cấp",
     "Luật Đấu thầu · NQ 188/2025/QH15 phần trình tự thủ tục rút gọn",
     "Hợp đồng với nhà thầu",
     "Hợp đồng EPC với nhà thầu nước ngoài dùng mẫu quốc tế, khó khớp với yêu cầu hồ sơ quyết toán trong nước."),
    ("Thi công xây dựng",
     "Thi công, giám sát, quản lý chất lượng, quản lý chi phí và tiến độ; xử lý phát sinh.",
     "Chủ đầu tư và Ban Quản lý dự án",
     "Luật Xây dựng · TT 44/2025/TT-BXD và TT 62/2026/TT-BXD về quy chuẩn kỹ thuật",
     "Khối lượng hoàn thành được nghiệm thu theo từng giai đoạn",
     "Hồ sơ nghiệm thu lập không đồng thời với thi công, đến lúc quyết toán mới đi tìm chữ ký."),
    ("Nghiệm thu, chạy thử và bàn giao",
     "Chạy thử liên động, đánh giá an toàn hệ thống, nghiệm thu hoàn thành và bàn giao cho đơn vị vận hành.",
     "Hội đồng nghiệm thu theo phân cấp; cơ quan chuyên môn kiểm tra công tác nghiệm thu",
     "TT 62/2026/TT-BXD quy chuẩn metro · VBHN 75/VBHN-VPQH",
     "Biên bản nghiệm thu hoàn thành · chứng nhận an toàn hệ thống",
     "Đánh giá an toàn hệ thống do đơn vị nước ngoài thực hiện, thời gian và chi phí thường vượt dự kiến."),
    ("Quyết toán vốn đầu tư",
     "Lập báo cáo quyết toán, kiểm toán độc lập báo cáo quyết toán, thẩm tra và phê duyệt quyết toán.",
     "Người quyết định đầu tư phê duyệt; cơ quan tài chính thẩm tra",
     "Quy định về quyết toán vốn đầu tư công dự án hoàn thành · VSA 1000",
     "Quyết định phê duyệt quyết toán · bàn giao tài sản",
     "Thiếu hồ sơ gốc của các giai đoạn trước; chi phí không tính vào giá trị tài sản chưa được cấp thẩm quyền cho phép bằng văn bản."),
]


def trang_quy_trinh():
    kh = []
    for ten, mo, tq, cc, dr, vm in GIAI_DOAN:
        kh.append("""<div class="b">
  <h3>%s</h3>
  <p style="margin:7px 0 0;font-size:15.4px;color:var(--chu2)">%s</p>
  <div class="ct">
    <div><b>Thẩm quyền quyết định</b>%s</div>
    <div><b>Căn cứ pháp lý</b>%s</div>
    <div><b>Sản phẩm đầu ra</b>%s</div>
    <div><b>Vướng mắc hay gặp</b><span style="color:var(--do)">%s</span></div>
  </div>
</div>""" % (html.escape(ten), html.escape(mo), html.escape(tq), html.escape(cc),
             html.escape(dr), html.escape(vm)))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Quy trình dự án</div>
  <h1>Quy trình thực hiện dự án đường sắt đô thị</h1>
  <p>Bảy giai đoạn từ chủ trương đầu tư đến quyết toán và bàn giao khai thác. Mỗi giai đoạn nêu
  thẩm quyền quyết định, căn cứ pháp lý, sản phẩm đầu ra và vướng mắc hay gặp.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--nhan);margin-bottom:24px">
    <h3>Cơ chế đặc thù làm khác đi ở đâu</h3>
    <p style="margin-top:9px">
      Với dự án đường sắt đô thị tại <b>Hà Nội và TP. Hồ Chí Minh</b>, Nghị quyết 188/2025/QH15 cho phép
      rút gọn hợp pháp một số bước ở giai đoạn 1, 2 và 4 — đặc biệt là trình tự thủ tục quyết định
      chủ trương đầu tư và lựa chọn nhà thầu. Bảng dưới đây mô tả trình tự <b>chung</b>; khi làm dự án
      tại hai địa bàn này phải đối chiếu Nghị quyết 188/2025 và bản hợp nhất
      <b>VBHN 34/VBHN-BXD</b> để biết bước nào được rút gọn.
    </p>
    <p style="margin-top:9px;color:var(--do)"><b>Nghị quyết 188/2025 không áp dụng cho địa bàn khác</b>,
    kể cả Phú Quốc.</p>
  </div>

  <div class="gd">%s</div>

  <div class="the" style="border-left:3px solid var(--ngoc);margin-top:26px">
    <h3>Một câu đáng nhớ</h3>
    <p style="margin-top:8px">Phần lớn vướng mắc phát sinh ở <b>giai đoạn 7</b> lại có nguyên nhân
    nằm ở <b>giai đoạn 2 và 5</b>. Hồ sơ nghiệm thu lập đúng lúc thi công thì quyết toán nhẹ nhàng;
    để dồn lại đến cuối thì đi tìm chữ ký của người đã chuyển công tác.</p>
  </div>

</div></div>
""" % '\n'.join(kh)

    ld = [{"@context": "https://schema.org", "@type": "HowTo",
           "name": "Quy trình thực hiện dự án đường sắt đô thị",
           "description": "Bảy giai đoạn từ chủ trương đầu tư đến quyết toán vốn đầu tư và bàn giao khai thác.",
           "step": [{"@type": "HowToStep", "position": i + 1, "name": g[0], "text": g[1]}
                    for i, g in enumerate(GIAI_DOAN)]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Quy trình dự án", "item": B.GOC + "/quy-trinh/"}]}]
    return than, ld


print('ds_pages: da nap trang dich va quy trinh.')
