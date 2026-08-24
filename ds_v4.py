# -*- coding: utf-8 -*-
"""Ban 4 — them:
   · Bo chuyen ngon ngu Viet / Anh / Trung o goc tren ben phai
   · Trang: Kiem toan Bao cao quyet toan du an hoan thanh (kiem toan song hanh)
   · Trang: Thu vien rui ro kiem toan du an
"""
import io, os, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages as P
import ds_pages2 as P2
import ds_data as D
import ds_data2 as D2
import ds_v2 as V2
import ds_v3 as V3

VB, N = P2.VB, P2.N

# ---------------------------------------------------------------- them 2 muc vao dieu huong
B.NAV = [
    ('van-ban',     'Cập nhật văn bản'),
    ('quy-trinh',   'Quy trình dự án'),
    ('kiem-toan',   'Kiểm toán quyết toán'),
    ('thu-vien-rui-ro', 'Thư viện rủi ro'),
    ('kinh-nghiem', 'Kinh nghiệm QLDA'),
    ('vuong-mac',   'Vướng mắc'),
    ('tu-van',      'Tư vấn'),
    ('lien-he',     'Liên hệ'),
]

# ---------------------------------------------------------------- CSS bo sung
B.CSS += r"""
/* ---------- bo chuyen ngon ngu ---------- */
.top-in{position:relative}
.ngonngu{display:flex;align-items:center;gap:2px;border:1px solid var(--vien);border-radius:999px;
  padding:2px;background:var(--nen2);flex:0 0 auto}
.ngonngu a{font-size:12.6px;font-weight:800;letter-spacing:.03em;padding:5px 11px;border-radius:999px;
  color:var(--chu2);text-decoration:none;white-space:nowrap;line-height:1}
.ngonngu a:hover{color:var(--muc);text-decoration:none}
.ngonngu a[aria-current]{background:var(--muc);color:#fff}
:root[data-theme="dark"] .ngonngu a[aria-current]{color:#0D2044}
/* logo day sang trai, bo ngon ngu bam ngoai cung ben PHAI */
.top-in .hieu{margin-right:auto}
@media(max-width:1000px){
  .ngonngu{order:1;margin-right:8px}
  .menu-nut{order:2}
}
@media(max-width:420px){.ngonngu a{padding:5px 8px;font-size:11.8px}
  .hieu i{display:none}}

/* ---------- bang so sanh hai cach lam ---------- */
.ss td:nth-child(2){color:var(--chu2)}
.ss td:nth-child(3){color:var(--chu);font-weight:600}
.ss thead th:nth-child(3){color:var(--ngoc)}

/* ---------- phan hanh ---------- */
.ph{display:grid;gap:12px;margin:16px 0}
.ph .b{display:grid;grid-template-columns:74px 1fr;gap:16px;background:var(--the);border:1px solid var(--vien);
  border-radius:var(--r);padding:18px 20px;box-shadow:var(--bong)}
@media(max-width:620px){.ph .b{grid-template-columns:1fr;gap:8px}}
.ph .ma{font-family:Consolas,"Courier New",monospace;font-size:19px;font-weight:700;color:var(--nhan2);
  line-height:1.2;padding-top:2px}
.ph h3{font-size:17px;margin-bottom:6px}
.ph p{margin:0;font-size:14.9px;color:var(--chu2)}
.ph .luuy{margin-top:9px;padding-top:8px;border-top:1px solid var(--vien);font-size:14.2px;color:var(--do)}

/* ---------- can doi ---------- */
.cd{background:var(--nen2);border:1px solid var(--vien);border-left:3px solid var(--ngoc);
  border-radius:var(--r);padding:18px 20px;margin-bottom:13px}
.cd b{display:block;color:var(--muc);font-size:16px;margin-bottom:8px}
.cd .ct{font-family:Consolas,"Courier New",monospace;font-size:14.4px;background:var(--the);
  border:1px solid var(--vien);border-radius:8px;padding:11px 13px;color:var(--chu);overflow-x:auto}
.cd .gc{margin-top:9px;font-size:14.3px;color:var(--chu2)}

/* ---------- rui ro ---------- */
.rr-nhom{margin-bottom:26px}
.rr-nhom>h3{font-size:19px;margin-bottom:11px;padding-bottom:7px;border-bottom:2px solid var(--vien)}
.rr{display:grid;gap:11px}
.rr .b{background:var(--the);border:1px solid var(--vien);border-radius:11px;padding:16px 18px}
.rr .b .dau{display:flex;gap:10px;align-items:flex-start;justify-content:space-between}
.rr .b h4{margin:0;font-family:'Times New Roman',Times,serif;font-size:16.6px;color:var(--muc);line-height:1.3}
.rr .b .muc{flex:0 0 auto;font-size:11.4px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
  padding:3px 9px;border-radius:999px}
.m-cao{background:var(--do-nen);color:var(--do)}
.m-trung{background:var(--hoacuc-nen);color:var(--nhan2)}
.m-thap{background:var(--nen3);color:var(--chu2)}
.rr .b .mo{margin:9px 0 0;font-size:14.7px;color:var(--chu2)}
.rr .b .tt{margin:9px 0 0;padding-top:8px;border-top:1px solid var(--vien);font-size:14.5px;color:var(--chu)}
.rr .b .tt b{color:var(--ngoc)}

/* ---------- trang ngoai ngu ---------- */
.nn-bao{background:var(--nen2);border:1px solid var(--vien);border-left:3px solid var(--nhan);
  border-radius:var(--r);padding:18px 20px;margin:22px 0}
"""


# ---------------------------------------------------------------- khung co bo ngon ngu
_khung_goc = B.khung

NGON_NGU = [('vi', 'VI', ''), ('en', 'EN', 'en/'), ('zh', '中文', 'zh/')]


def _bo_ngon_ngu(slug, lang='vi'):
    """slug: '' hoac 'van-ban'... ; lang: vi|en|zh"""
    ra = []
    for ma, nhan, thumuc in NGON_NGU:
        if lang == 'vi':
            goc = '../' if slug else ''
            dich = (goc + 'index.html') if ma == 'vi' else (goc + thumuc + 'index.html')
        else:
            # dang o trang ngoai ngu (nam trong /en/ hoac /zh/)
            dich = '../index.html' if ma == 'vi' else ('../' + thumuc + 'index.html')
        cur = ' aria-current="true"' if ma == lang else ''
        ra.append('<a href="%s" hreflang="%s"%s>%s</a>' % (dich, ma, cur, nhan))
    return '<div class="ngonngu" role="group" aria-label="Chọn ngôn ngữ">%s</div>' % ''.join(ra)


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _khung_goc(slug, tieude, mota, than, jsonld, tang)
    h = h.replace('</nav>', '</nav>' + chr(10) + '    ' + _bo_ngon_ngu(slug, lang), 1)
    if lang != 'vi':
        h = h.replace('<html lang="vi">', '<html lang="%s">' % lang, 1)
    return h


B.khung = khung


# ================================================================ TRANG KIEM TOAN
def trang_kiem_toan():
    vs = ''.join(
        '<div class="the" style="border-left:3px solid var(--nhan);margin-bottom:13px">'
        '<h3>%d. %s</h3><p style="margin-top:8px">%s</p></div>'
        % (i + 1, html.escape(t), html.escape(n)) for i, (t, n) in enumerate(D2.VI_SAO_SONG_HANH))

    ss = ''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>'
                 % (html.escape(a), html.escape(b), html.escape(c)) for a, b, c in D2.SO_SANH)

    ph = ''.join(
        '<div class="b"><div class="ma">%s</div><div><h3>%s</h3><p>%s</p>'
        '<div class="luuy">%s</div></div></div>'
        % (ma, html.escape(t), html.escape(n), html.escape(l))
        for ma, t, n, l in D2.PHAN_HANH)

    cd = ''.join('<div class="cd"><b>%s</b><div class="ct">%s</div><div class="gc">%s</div></div>'
                 % (html.escape(t), html.escape(ct), html.escape(g)) for t, ct, g in D2.CAN_DOI)

    kl = ''.join('<div class="the" style="border-left:3px solid var(--do);margin-bottom:12px">'
                 '<h3>%s</h3><p style="margin-top:8px">%s</p></div>'
                 % (html.escape(t), html.escape(n)) for t, n in D2.KHONG_LAM)

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Kiểm toán quyết toán</div>
  <h1>Kiểm toán Báo cáo quyết toán dự án hoàn thành</h1>
  <p>Nội dung và quy trình kiểm toán theo mười ba phần hành. Với dự án lớn, kiểm toán được thực hiện
  <b>song hành cùng quá trình thực hiện dự án</b> chứ không đợi đến khi công trình hoàn thành.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--ngoc);margin-bottom:26px">
    <h3>Kiểm toán song hành là gì</h3>
    <p style="margin-top:9px">Cách làm thông thường là đợi công trình hoàn thành, chủ đầu tư lập xong
    báo cáo quyết toán rồi mới mời kiểm toán. Cách đó hợp với dự án nhỏ, làm trong một hai năm.</p>
    <p><b>Với dự án đường sắt đô thị thì không hợp.</b> Vòng đời tám đến mười lăm năm, hàng chục nghìn
    chứng từ, phần lớn khối lượng nằm dưới lòng đất. Đợi đến cuối mới kiểm thì nhiều thứ đã không kiểm
    được nữa.</p>
    <p><b>Kiểm toán song hành</b> nghĩa là kiểm toán viên vào cuộc <b>ngay trong quá trình thi công</b>,
    làm theo từng đợt — theo giai đoạn hoặc theo gói thầu — và đợt cuối cùng tổng hợp lại thành báo cáo
    kiểm toán báo cáo quyết toán dự án hoàn thành.</p>
  </div>

  <h2 style="margin-bottom:14px">Năm lý do dự án lớn phải làm song hành</h2>
  %s

  <h2 style="margin:32px 0 12px">Hai cách làm, đặt cạnh nhau</h2>
  <div class="bang-boc">
    <table class="ss">
      <thead><tr><th style="width:22%%">Tiêu chí</th><th style="width:37%%">Kiểm toán sau khi hoàn thành</th>
      <th>Kiểm toán song hành</th></tr></thead>
      <tbody>%s</tbody>
    </table>
  </div>
  <p class="small">Kiểm toán song hành <b>không thay thế</b> báo cáo kiểm toán cuối cùng. Mỗi đợt cho ra
  một biên bản làm việc và thư quản lý; đợt cuối mới phát hành báo cáo kiểm toán báo cáo quyết toán
  dự án hoàn thành theo đúng chuẩn mực.</p>

  <h2 style="margin:32px 0 12px">Mười ba phần hành</h2>
  <p class="small" style="margin-bottom:14px">Theo hệ thống chỉ mục của Hồ sơ kiểm toán mẫu Báo cáo quyết
  toán dự án hoàn thành. Mỗi phần hành nêu nội dung kiểm tra và điểm cần chú ý.</p>
  <div class="ph">%s</div>

  <h2 style="margin:32px 0 12px">Hai phép cân đối trước khi phát hành</h2>
  <p class="small" style="margin-bottom:14px">Đây là hai phép kiểm bắt buộc chạy trên cùng một bộ số.
  Không cân thì chưa được phát hành báo cáo.</p>
  %s

  <h2 style="margin:32px 0 12px">Ba điều kiểm toán viên không làm</h2>
  %s

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>Nếu Quý vị đang cân nhắc cách làm cho dự án của mình</h3>
    <p style="margin-top:8px">Việc chọn kiểm toán sau khi hoàn thành hay kiểm toán song hành phụ thuộc
    quy mô, thời gian thực hiện và số gói thầu của dự án. Gửi thông tin qua trang
    <a href="../tu-van/index.html">Tư vấn</a>, chúng tôi nêu ý kiến về phương án phù hợp và
    khối lượng công việc dự kiến.</p>
  </div>

</div></div>
""" % (vs, ss, ph, cd, kl)

    ld = [{"@context": "https://schema.org", "@type": "Article",
           "headline": "Kiểm toán Báo cáo quyết toán dự án hoàn thành",
           "description": "Nội dung và quy trình kiểm toán theo mười ba phần hành; vì sao dự án lớn phải kiểm toán song hành cùng quá trình thực hiện dự án.",
           "inLanguage": "vi-VN"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Kiểm toán quyết toán", "item": B.GOC + "/kiem-toan/"}]}]
    return than, ld


# ================================================================ THU VIEN RUI RO
def trang_rui_ro():
    NHAN = {'cao': ('m-cao', 'Cao'), 'trung': ('m-trung', 'Trung bình'), 'thap': ('m-thap', 'Thấp')}
    nhom = ''
    tong = 0
    for ten, ds in D2.RUI_RO:
        muc = ''
        for t, mo, tt, m in ds:
            lop, nh = NHAN[m]
            tong += 1
            muc += ('<div class="b"><div class="dau"><h4>%s</h4>'
                    '<span class="muc %s">%s</span></div>'
                    '<p class="mo">%s</p>'
                    '<p class="tt"><b>Thủ tục ứng phó — </b>%s</p></div>'
                    % (html.escape(t), lop, nh, html.escape(mo), html.escape(tt)))
        nhom += '<div class="rr-nhom"><h3>%s</h3><div class="rr">%s</div></div>' % (html.escape(ten), muc)

    dem_cao = sum(1 for _, ds in D2.RUI_RO for x in ds if x[3] == 'cao')

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Trang chủ</a> · Thư viện rủi ro</div>
  <h1>Thư viện rủi ro kiểm toán dự án</h1>
  <p>%d rủi ro thường gặp chia theo tám nhóm, mỗi rủi ro nêu dấu hiệu nhận biết và thủ tục kiểm toán
  ứng phó. Dùng làm danh mục soát khi lập kế hoạch kiểm toán.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--do);margin-bottom:24px">
    <h3>Đọc trước: đây là tài liệu tham khảo chung</h3>
    <p style="margin-top:9px">Thư viện này <b>tổng hợp từ kinh nghiệm nghề nghiệp chung và tài liệu công khai</b>.
    <b>Không có rủi ro nào ở đây được lấy từ thực tiễn của một đơn vị cụ thể</b>, không phản ánh phát hiện
    kiểm toán tại bất kỳ dự án nào, và không nêu tên đơn vị, dự án hay cá nhân nào.</p>
    <p>Mục đích là làm <b>danh mục gợi nhớ</b> khi lập kế hoạch kiểm toán — để không bỏ sót nhóm rủi ro
    nào — chứ không phải danh sách lỗi của ai.</p>
    <p style="color:var(--do)"><b>Mức rủi ro ghi ở đây là mức chung.</b> Mức thực tế của một dự án cụ thể
    phải do kiểm toán viên đánh giá dựa trên hiểu biết về đơn vị và môi trường hoạt động của chính dự án đó.</p>
  </div>

  <div class="thongke">
    <div><b>%d</b><span>Rủi ro</span></div>
    <div><b>8</b><span>Nhóm</span></div>
    <div><b>%d</b><span>Mức cao</span></div>
    <div><b>5</b><span>Riêng đường sắt đô thị</span></div>
  </div>

  <div class="huong-dan" style="margin-bottom:26px">
    <div class="b"><b>Mức Cao</b><span>Nếu xảy ra thì thường dẫn tới việc khoản chi phí bị loại hoặc bị treo,
    không quyết toán được. Cần thủ tục kiểm tra riêng.</span></div>
    <div class="b"><b>Mức Trung bình</b><span>Ảnh hưởng tới giá trị quyết toán nhưng thường xử lý được nếu
    phát hiện sớm và bổ sung được hồ sơ.</span></div>
    <div class="b"><b>Mức Thấp</b><span>Chủ yếu ảnh hưởng tới việc trình bày và thuyết minh, ít khi ảnh hưởng
    tới con số.</span></div>
  </div>

  <h2 style="margin:28px 0 16px">Tám nhóm rủi ro</h2>
  %s

  <h2 style="margin:26px 0 14px">Cách dùng</h2>
  <div class="the" style="border-left:3px solid var(--muc3)">
    <h3>Cách dùng thư viện này</h3>
    <p style="margin-top:8px">Khi lập kế hoạch kiểm toán một dự án, đọc lướt tám nhóm và đánh dấu những
    rủi ro <b>có khả năng xảy ra ở dự án này</b> dựa trên đặc điểm thực tế: quy mô, nguồn vốn, số gói thầu,
    loại hợp đồng, thời gian thực hiện. Những rủi ro được đánh dấu sẽ quyết định phạm vi và cỡ mẫu
    của từng phần hành.</p>
    <p>Danh mục này <b>không đầy đủ và không cố định</b>. Mỗi dự án có thể có rủi ro riêng không nằm ở đây,
    và việc nhận diện rủi ro đó thuộc xét đoán nghề nghiệp của kiểm toán viên.</p>
  </div>

</div></div>
""" % (tong, tong, dem_cao, nhom)

    ld = [{"@context": "https://schema.org", "@type": "Article",
           "headline": "Thư viện rủi ro kiểm toán dự án",
           "description": "%d rủi ro thường gặp trong kiểm toán báo cáo quyết toán dự án hoàn thành, chia tám nhóm, kèm dấu hiệu nhận biết và thủ tục ứng phó. Tài liệu tham khảo chung." % tong,
           "inLanguage": "vi-VN"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Thư viện rủi ro", "item": B.GOC + "/thu-vien-rui-ro/"}]}]
    return than, ld


print('ds_v4: da nap 2 trang moi + bo ngon ngu.')
