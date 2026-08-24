# -*- coding: utf-8 -*-
"""Ban 2 — dung lai ba trang noi dung bang du lieu day du tu ds_data."""
import io, os, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages as P
import ds_pages2 as P2
import ds_data as D


# ---------------------------------------------------------- QUY TRINH (9 gd)
def trang_quy_trinh():
    ngan = ''.join(
        '<tr><td><span class="the-loc tl-%s" style="font-size:13px">Ngăn %s</span></td>'
        '<td><b>%s</b></td><td>%s</td><td>%s</td></tr>'
        % ({'ngoc': 'luat', 'do': 'khac', 'nhan': 'nd', 'muc': 'tt'}[m],
           k, html.escape(t), html.escape(dk), html.escape(vb))
        for k, t, dk, vb, m in D.NGAN_PHAP_LY)

    gd = ''.join("""<div class="b">
  <h3>%s</h3>
  <p style="margin:7px 0 0;font-size:15.3px;color:var(--chu2)">%s</p>
  <div class="ct">
    <div><b>Thẩm quyền quyết định</b>%s</div>
    <div><b>Căn cứ pháp lý</b>%s</div>
    <div><b>Sản phẩm đầu ra</b>%s</div>
    <div><b>Vướng mắc hay gặp</b><span style="color:var(--do)">%s</span></div>
  </div>
</div>""" % (html.escape(t), html.escape(m), html.escape(tq), html.escape(cc),
             html.escape(dr), html.escape(vm)) for t, m, tq, cc, dr, vm in D.GIAI_DOAN)

    ho = ''.join(
        '<div class="the" style="border-left:3px solid var(--do);margin-bottom:14px">'
        '<h3>%s</h3><p style="margin-top:8px">%s</p></div>'
        % (html.escape(t), html.escape(n)) for t, n in D.CHO_HO)

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Quy trình dự án</div>
  <h1>Quy trình thực hiện dự án đường sắt đô thị</h1>
  <p>Chín giai đoạn từ quy hoạch tuyến đến quyết toán vốn đầu tư. Mỗi giai đoạn nêu thẩm quyền
  quyết định, căn cứ pháp lý, sản phẩm đầu ra và vướng mắc hay gặp.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--nhan);margin-bottom:22px">
    <h3>Trước hết: dự án của Quý vị thuộc ngăn nào?</h3>
    <p style="margin-top:9px">Đường sắt đô thị là loại dự án hiếm hoi mà <b>ba hệ pháp luật chồng lên nhau
    trên cùng một công trình</b> — pháp luật xây dựng, pháp luật đầu tư công hoặc PPP, và một tầng cơ chế
    đặc thù riêng. Chọn sai ngăn thì toàn bộ trình tự phía sau sai theo.</p>
  </div>

  <div class="bang-boc">
    <table>
      <thead><tr><th style="width:96px">Ngăn</th><th style="width:26%%">Loại dự án</th>
      <th style="width:22%%">Điều kiện</th><th>Trục pháp lý</th></tr></thead>
      <tbody>%s</tbody>
    </table>
  </div>

  <div class="the" style="border-left:3px solid var(--do);margin:18px 0 26px">
    <h3>Nguyên tắc nền, không thoả hiệp</h3>
    <p style="margin-top:8px">Vòng đời một tuyến metro thường <b>tám đến mười lăm năm</b>, đủ dài để đi qua
    hai ba đời nghị định. Vì vậy: <b>áp dụng văn bản có hiệu lực tại thời điểm phát sinh công việc, không áp
    văn bản hiện hành cho khối lượng đã thực hiện nhiều năm trước.</b></p>
    <p style="margin-top:8px;color:var(--do)"><b>Nghị quyết 188/2025/QH15 chỉ thí điểm cho Hà Nội và
    TP. Hồ Chí Minh</b> — không áp dụng cho Phú Quốc hay bất kỳ địa bàn nào khác. Bê cơ chế TOD của
    hai thành phố này sang địa bàn thứ ba là lỗi căn cứ, không phải lỗi diễn đạt.</p>
  </div>

  <h2 style="margin-bottom:16px">Chín giai đoạn</h2>
  <div class="gd">%s</div>

  <h2 style="margin:34px 0 8px">Ba chỗ cơ chế còn hở</h2>
  <p class="small" style="margin-bottom:16px">Cơ chế đã đủ ở tầng Luật và Nghị quyết, nhưng thiếu văn bản
  định lượng ở tầng dưới cùng. Biết trước để không đưa con số ước tính vào phương án tài chính chính thức.</p>
  %s

  <div class="the" style="border-left:3px solid var(--ngoc);margin-top:20px">
    <h3>Một câu đáng nhớ</h3>
    <p style="margin-top:8px">Phần lớn vướng mắc phát sinh ở <b>giai đoạn 9</b> lại có nguyên nhân nằm ở
    <b>giai đoạn 3 và 6</b>. Quyết toán không phải việc diễn ra ở cuối dự án — nó là <b>kết quả của cách
    hồ sơ được lập trong suốt mười năm trước đó</b>. Chi phí sửa một thiếu sót hồ sơ tăng theo hàm mũ
    của thời gian: bổ sung một chữ ký lúc đang thi công mất nửa buổi; bổ sung chữ ký đó sau bảy năm,
    khi người ký đã nghỉ hưu, thường là không làm được.</p>
  </div>

</div></div>
""" % (ngan, gd, ho)

    ld = [{"@context": "https://schema.org", "@type": "HowTo",
           "name": "Quy trình thực hiện dự án đường sắt đô thị",
           "description": "Chín giai đoạn từ quy hoạch tuyến đến quyết toán vốn đầu tư dự án hoàn thành.",
           "step": [{"@type": "HowToStep", "position": i + 1, "name": g[0], "text": g[1]}
                    for i, g in enumerate(D.GIAI_DOAN)]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Quy trình dự án", "item": B.GOC + "/quy-trinh/"}]}]
    return than, ld


# ---------------------------------------------------------- KINH NGHIEM
def trang_kinh_nghiem():
    bh = ''.join(
        '<div class="the" style="border-left:3px solid var(--muc3);margin-bottom:14px">'
        '<h3>%d. %s</h3><p style="margin-top:8px">%s</p></div>'
        % (i + 1, html.escape(t), html.escape(n)) for i, (t, n) in enumerate(D.BAI_HOC))

    kt = ''.join(
        '<details><summary>%s</summary><ul style="margin:12px 0 2px;padding-left:20px;'
        'font-size:15px;color:var(--chu2)">%s</ul></details>'
        % (html.escape(moc), ''.join('<li style="margin-bottom:6px">%s</li>' % html.escape(x) for x in ds))
        for moc, ds in D.KIEM_TRA)

    sl = ''.join(
        '<div class="the" style="border-left:3px solid var(--do);margin-bottom:14px">'
        '<h3>%s</h3><p style="margin-top:8px">%s</p></div>'
        % (html.escape(t), html.escape(n)) for t, n in D.SAI_LAM)

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Kinh nghiệm QLDA</div>
  <h1>Kinh nghiệm quản lý dự án đường sắt đô thị</h1>
  <p>Mười hai việc nên làm sớm, danh mục kiểm tra theo từng thời điểm, và ba sai lầm lặp lại
  nhiều nhất. Viết ở tầm quy trình, không nêu tên đơn vị nào.</p>
</div></div>

<div class="than"><div class="wrap hep">

  <div class="the" style="border-left:3px solid var(--nhan);margin-bottom:24px">
    <h3>Nguyên lý chung</h3>
    <p style="margin-top:8px">Gần như mọi vướng mắc quyết toán đều có nguồn gốc ở một quyết định hoặc
    một sự bỏ sót từ nhiều năm trước — thường ở giai đoạn lập dự án hoặc giai đoạn ký hợp đồng, tức là
    lúc mọi người còn đang bận với những việc <i>trông có vẻ</i> cấp bách hơn.</p>
  </div>

  <h2 style="margin-bottom:16px">Mười hai việc nên làm sớm</h2>
  %s

  <h2 style="margin:32px 0 14px">Danh mục kiểm tra theo thời điểm</h2>
  <p class="small" style="margin-bottom:14px">Bấm vào từng mốc để mở danh mục.</p>
  %s

  <h2 style="margin:32px 0 14px">Ba sai lầm lặp lại nhiều nhất</h2>
  %s

  <div class="the" style="border-left:3px solid var(--ngoc);margin-top:8px">
    <h3>Về nguyên tắc viết những bài này</h3>
    <p style="margin-top:8px">Không nêu tên dự án, tên đơn vị, số liệu hợp đồng hay phát hiện kiểm toán
    của khách hàng. Đây không phải quy tắc hình thức — nghĩa vụ bảo mật của nghề áp cả với bài viết
    chia sẻ kinh nghiệm tưởng chừng vô hại.</p>
  </div>

</div></div>
""" % (bh, kt, sl)

    ld = [{"@context": "https://schema.org", "@type": "Article",
           "headline": "Kinh nghiệm quản lý dự án đường sắt đô thị",
           "description": "Mười hai việc Ban Quản lý dự án nên làm sớm, danh mục kiểm tra theo thời điểm và ba sai lầm lặp lại nhiều nhất.",
           "inLanguage": "vi-VN"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Kinh nghiệm QLDA", "item": B.GOC + "/kinh-nghiem/"}]}]
    return than, ld


# ---------------------------------------------------------- VUONG MAC
def trang_vuong_mac():
    kh = ''.join(
        '<details><summary>%d. %s</summary>'
        '<p><b>Tình huống — </b>%s</p>'
        '<p><b>Vì sao phát sinh — </b>%s</p>'
        '<p><b>Căn cứ liên quan — </b>%s</p>'
        '<p style="color:var(--ngoc)"><b>Hướng xử lý — </b>%s</p></details>'
        % (i + 1, html.escape(t), html.escape(a), html.escape(b), html.escape(c), html.escape(d))
        for i, (t, a, b, c, d) in enumerate(D.VUONG_MAC))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Vướng mắc</div>
  <h1>Mười vướng mắc thường gặp</h1>
  <p>Mỗi tình huống nêu bối cảnh, nguyên nhân phát sinh, căn cứ pháp lý liên quan và hướng xử lý.
  Bấm vào từng mục để mở nội dung.</p>
</div></div>

<div class="than"><div class="wrap hep">
  <h2 style="margin-bottom:16px">Mười tình huống</h2>
  %s

  <div class="the" style="border-left:3px solid var(--nhan);margin-top:22px">
    <h3>Không thấy tình huống của mình ở đây?</h3>
    <p style="margin-top:8px">Gửi câu hỏi qua trang <a href="../tu-van/index.html">Tư vấn</a>. Chúng tôi trả lời riêng
    cho Quý vị, và nếu câu hỏi có giá trị chung thì biên tập lại thành một mục trên trang này —
    <b>không nêu tên đơn vị hỏi</b>.</p>
  </div>
</div></div>
""" % kh

    ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": t,
         "acceptedAnswer": {"@type": "Answer", "text": a + " " + d}}
        for t, a, b, c, d in D.VUONG_MAC]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
            {"@type": "ListItem", "position": 2, "name": "Vướng mắc", "item": B.GOC + "/vuong-mac/"}]}]
    return than, ld


# ---------------------------------------------------------- ghi de
P.trang_quy_trinh = trang_quy_trinh
P2.trang_kinh_nghiem = trang_kinh_nghiem
P2.trang_vuong_mac = trang_vuong_mac

P2.TRANG = [
    (s, td, mt,
     {'quy-trinh': trang_quy_trinh, 'kinh-nghiem': trang_kinh_nghiem,
      'vuong-mac': trang_vuong_mac}.get(s, fn), tang)
    for s, td, mt, fn, tang in P2.TRANG]

# sua mo ta hai trang cho khop noi dung moi
def _sua(slug, td=None, mt=None):
    for i, (s, a, b, fn, tang) in enumerate(P2.TRANG):
        if s == slug:
            P2.TRANG[i] = (s, td or a, mt or b, fn, tang)

_sua('quy-trinh',
     'Quy trình thực hiện dự án đường sắt đô thị — chín giai đoạn',
     'Chín giai đoạn từ quy hoạch tuyến đến quyết toán vốn đầu tư, kèm bốn ngăn pháp lý, thẩm quyền quyết định và vướng mắc hay gặp.')
_sua('kinh-nghiem',
     'Kinh nghiệm quản lý dự án đường sắt đô thị',
     'Mười hai việc Ban Quản lý dự án nên làm sớm, danh mục kiểm tra theo thời điểm và ba sai lầm lặp lại nhiều nhất.')

if __name__ == '__main__':
    P2.ghi()
