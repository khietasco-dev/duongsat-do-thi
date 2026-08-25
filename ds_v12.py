# -*- coding: utf-8 -*-
"""Ban 12 — theo yeu cau CEO 25/08:
   1. Menu tren banner viet IN HOA
   2. Them muc menu "DICH VU CUNG CAP" dang so xuong, xo ra 9 dich vu
   3. Moi dich vu mot trang gioi thieu rieng  /dich-vu/<slug>/
   4. Trang /tu-van/ bo sung khoi 9 dich vu

Ky thuat can nho: cac trang dich vu nam SAU HAI CAP (`dich-vu/<slug>`) trong khi
khuon goc chi tinh duong dan lui MOT cap. Xu ly o ham khung() ben duoi:
  - lui them mot cap cho moi lien ket cua khuon (header, chan trang, nut ngon ngu)
  - lien ket trong RUOT trang viet bang dau '@/' = goc trang, thay sau nen khong bi dinh
"""
import io, os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v3 as V3
import ds_v7 as V7
import ds_v11 as V11
from ds_dv import DICH_VU, NHOM

CHU_DV = 'Dịch vụ cung cấp'

# ================================================================= CSS
B.CSS += r"""
/* ---------- menu IN HOA ---------- */
.top-nav a,.top-nav .dv>summary{text-transform:uppercase;font-size:13.2px;font-weight:700;
  letter-spacing:.032em}
.top-nav .nut-lh{letter-spacing:.045em}
/* 9 muc IN HOA tren dien thoai: siet co chu va khoang cach de con 3 dong thay vi 4 */
@media(max-width:700px){
  .top-nav a,.top-nav .dv>summary{font-size:11.9px;letter-spacing:.012em}
  .top-nav{gap:5px 11px}
  .top-nav .nut-lh{padding:4px 11px!important}
}
@media(max-width:400px){
  .top-nav a,.top-nav .dv>summary{font-size:11.2px;letter-spacing:0}
  .top-nav{gap:4px 9px}
}

/* ---------- muc menu so xuong "Dich vu cung cap" ---------- */
.dv{position:relative;margin:0!important;padding:0!important;border:0!important;
  background:none!important;border-radius:0!important}
.dv>summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:6px;
  color:var(--chu);white-space:nowrap;user-select:none;padding:3px 0}
.dv>summary::-webkit-details-marker{display:none}
.dv>summary:hover{color:var(--muc)}
.dv>summary .cau{font-size:10.6px;opacity:.7;transition:transform .15s}
.dv[open]>summary{color:var(--muc)}
.dv[open]>summary .cau{transform:rotate(180deg)}
.dv-menu{position:absolute;top:calc(100% + 9px);left:0;z-index:90;width:330px;
  background:var(--the);border:1px solid var(--vien);border-radius:12px;padding:7px;
  box-shadow:0 14px 38px rgba(14,23,41,.19)}
:root[data-theme="dark"] .dv-menu{box-shadow:0 14px 38px rgba(0,0,0,.55)}
.dv-menu a{display:block;padding:8px 11px;border-radius:8px;font-size:13.8px;font-weight:600;
  color:var(--chu);text-decoration:none;white-space:normal;text-transform:none;letter-spacing:0;
  line-height:1.4}
.dv-menu a:hover{background:var(--nen2);color:var(--muc)}
.dv-menu a[aria-current]{background:var(--muc);color:#fff}
:root[data-theme="dark"] .dv-menu a[aria-current]{color:#0D2044}
.dv-menu .tat{font-weight:800;border-bottom:1px solid var(--vien);border-radius:8px 8px 0 0;
  margin-bottom:4px;padding-bottom:10px}
.dv-menu .nhomdv{font-size:11.2px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  color:var(--nhan2);padding:9px 11px 3px}
/* Tren dien thoai: bang xo ra bam theo CA HANG MENU, trai sang phai het be ngang.
   Khong dung width:100% cho .dv — lam vay no chiem tron mot dong, menu doi tu 3 len 4 dong. */
@media(max-width:700px){
  /* ban 11 dat .top-nav{position:static!important} nen phai ghi de bang !important,
     khong thi bang xo xuong bam nham vao the cha cao hon va tran ra mep man hinh */
  .top-nav{position:relative!important}
  .dv{position:static}
  .dv-menu{top:calc(100% + 6px);left:0;right:0;width:auto;z-index:95;
    box-shadow:0 12px 30px rgba(14,23,41,.22)}
}

/* ---------- the dich vu ---------- */
.dv-luoi{display:grid;gap:15px;grid-template-columns:repeat(3,1fr);margin:14px 0 6px}
@media(max-width:1000px){.dv-luoi{grid-template-columns:repeat(2,1fr)}}
@media(max-width:660px){.dv-luoi{grid-template-columns:1fr}}
.dv-the{display:block;background:var(--the);border:1px solid var(--vien);border-radius:var(--r);
  padding:19px 20px;text-decoration:none;box-shadow:var(--bong);transition:border-color .15s,transform .15s}
.dv-the:hover{border-color:var(--muc3);transform:translateY(-2px)}
.dv-the .so{font-family:Consolas,"Courier New",monospace;font-size:12.4px;font-weight:800;
  color:var(--nhan2);letter-spacing:.06em}
.dv-the h3{margin:5px 0 7px;font-size:16.6px;color:var(--muc);line-height:1.32}
.dv-the p{font-size:14.2px;color:var(--chu2);margin:0;line-height:1.55}
.dv-the .di{display:inline-block;margin-top:10px;font-size:13.2px;font-weight:700;color:var(--muc)}

/* ---------- trang chi tiet dich vu ---------- */
.dv-mo{font-size:17px;line-height:1.68;color:var(--chu);margin-bottom:6px}
.dv-cc{background:var(--nen2);border:1px solid var(--vien);border-radius:11px;padding:16px 18px;
  margin-bottom:11px}
.dv-cc b{display:block;color:var(--muc);font-size:14.4px;margin-bottom:5px}
.dv-cc span{font-size:14.6px;color:var(--chu2);line-height:1.62}
.dv-buoc{counter-reset:b;list-style:none;padding:0;margin:12px 0 0}
.dv-buoc li{counter-increment:b;position:relative;padding:0 0 15px 46px;margin:0}
.dv-buoc li::before{content:counter(b);position:absolute;left:0;top:0;width:31px;height:31px;
  border-radius:50%;background:var(--muc);color:#fff;font-weight:800;font-size:14.2px;
  display:flex;align-items:center;justify-content:center}
:root[data-theme="dark"] .dv-buoc li::before{color:#0D2044}
.dv-buoc b{display:block;font-size:15.6px;color:var(--chu);margin-bottom:3px}
.dv-buoc span{font-size:14.6px;color:var(--chu2);line-height:1.6}
.dv-luu{border-left:3px solid var(--do);background:var(--do-nen);border-radius:9px;
  padding:15px 18px;margin-top:22px;font-size:14.4px;line-height:1.62}
"""

# ================================================================= duong dan
_V11_KHUNG = V11.khung


def _goc(slug):
    return '../' * (slug.count('/') + 1) if slug else ''


def _muc_dv(slug):
    """Khoi <details> "Dich vu cung cap" chen vao thanh menu."""
    dang = slug.startswith('dich-vu')
    ra = ['<a class="tat" href="@/dich-vu/index.html"%s>Tất cả dịch vụ</a>'
          % (' aria-current="page"' if slug == 'dich-vu' else '')]
    nh = None
    for d in DICH_VU:
        if d['nhom'] != nh:
            nh = d['nhom']
            ra.append('<div class="nhomdv">%s</div>' % html.escape(NHOM[nh][0]))
        cur = ' aria-current="page"' if slug == 'dich-vu/' + d['slug'] else ''
        ra.append('<a href="@/dich-vu/%s/index.html"%s>%s</a>'
                  % (d['slug'], cur, html.escape(d['menu'])))
    kieu = ' style="color:var(--muc);text-decoration:underline;text-underline-offset:5px"' if dang else ''
    return ('<details class="dv"><summary%s>%s<span class="cau">▾</span></summary>'
            '<div class="dv-menu">%s</div></details>'
            % (kieu, html.escape(CHU_DV), ''.join(ra)))


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V11_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)

    # 1. trang nam sau hai cap thi moi lien ket cua khuon phai lui them mot cap
    sau = slug.count('/')
    if sau:
        h = h.replace('href="../', 'href="' + '../' * (sau + 1))

    # 2. chen muc "Dich vu cung cap" ngay truoc muc "Tu van"
    neo = '<a href="%stu-van/index.html"' % _goc(slug)
    if neo in h:
        h = h.replace(neo, _muc_dv(slug) + chr(10) + '        ' + neo, 1)
    else:
        raise SystemExit('KHONG TIM THAY muc Tu van tren thanh menu (slug=%r)' % slug)

    # 3. '@/...' trong ruot trang = tinh tu goc trang
    h = h.replace('href="@/', 'href="' + _goc(slug))

    # 4. bam ra ngoai / bam Esc thi dong ca bang "Dich vu cung cap",
    #    khong chi dong nut ngon ngu nhu truoc
    h = h.replace("details.nn[open]", "details.nn[open],details.dv[open]")
    return h


B.khung = khung


# ================================================================= trang chi tiet
def _trang_dv(d):
    def ds(items):
        return '<ul>%s</ul>' % ''.join('<li>%s</li>' % html.escape(x) for x in items)

    cc = ''.join('<div class="dv-cc"><b>%s</b><span>%s</span></div>'
                 % (html.escape(a), html.escape(b)) for a, b in d['can_cu'])
    bu = ''.join('<li><b>%s</b><span>%s</span></li>' % (html.escape(a), html.escape(b))
                 for a, b in d['lam_gi'])
    ten_nhom, mau = NHOM[d['nhom']]

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/index.html">Trang chủ</a> ·
    <a href="@/dich-vu/index.html">Dịch vụ cung cấp</a> · %(menu)s</div>
  <span class="the-loc" style="background:var(--nen3);color:%(mau)s">%(nhom)s</span>
  <h1>%(ten)s</h1>
  <p>%(lede)s</p>
</div></div>

<div class="than"><div class="wrap">

  <h2 style="margin-bottom:10px">Vấn đề thường gặp</h2>
  %(vande)s

  <h2 style="margin:30px 0 10px">Căn cứ pháp lý</h2>
  <p class="small" style="margin-bottom:12px">Mọi điều khoản dưới đây đều đã đối chiếu với bản gốc
  trong kho văn bản của chúng tôi. Quý vị mở lại được ở mục
  <a href="@/van-ban/index.html">Tra cứu văn bản</a>.</p>
  %(cancu)s

  <h2 style="margin:30px 0 6px">Chúng tôi làm gì</h2>
  <ol class="dv-buoc">%(buoc)s</ol>

  <div class="luoi g2" style="margin-top:26px">
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>Kết quả bàn giao</h3>
      %(daura)s
    </div>
    <div class="the" style="border-left:3px solid var(--nhan)">
      <h3>Khi nào nên gọi chúng tôi</h3>
      <p style="margin-top:8px">%(khinao)s</p>
    </div>
  </div>

  <div class="dv-luu">
    <b>Hai điều kiện phải nói trước.</b>
    Thứ nhất, đây là dịch vụ thuộc khoản 2 Điều 40 Luật Kiểm toán độc lập — doanh nghiệp kiểm toán
    phải đăng ký với Bộ Tài chính mới được thực hiện.
    Thứ hai, nếu chúng tôi đang hoặc sẽ kiểm toán đơn vị của Quý vị thì dịch vụ này phải qua
    kiểm tra tính độc lập trước khi ký, theo Điều 30 cùng luật. Chúng tôi rà việc đó trước, và
    nếu vướng thì nói thẳng là không nhận.
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:20px">
    <h3>Bước tiếp theo</h3>
    <p style="margin-top:8px">Gửi mô tả tình huống qua trang
    <a href="@/tu-van/index.html">Gửi yêu cầu tư vấn</a>, hoặc gọi
    <b>0825092007</b>. Chúng tôi đọc, phân loại và phản hồi trong 24 giờ làm việc — kể cả khi
    câu trả lời là việc này không thuộc phạm vi chúng tôi được làm.</p>
    <p class="small" style="margin-top:9px"><a href="@/dich-vu/index.html">← Xem tất cả 9 dịch vụ</a></p>
  </div>

</div></div>
""" % dict(menu=html.escape(d['menu']), ten=html.escape(d['ten']), lede=html.escape(d['lede']),
           nhom=html.escape(ten_nhom), mau=mau,
           vande=ds(d['van_de']), cancu=cc, buoc=bu,
           daura=ds(d['dau_ra']), khinao=html.escape(d['khi_nao']))

    ld = [{"@context": "https://schema.org", "@type": "Service",
           "name": d['ten'], "description": d['mt'],
           "serviceType": ten_nhom, "areaServed": "VN",
           "provider": {"@type": "Organization",
                        "name": "Hãng Kiểm toán và Định giá ASCO",
                        "telephone": "0825092007"},
           "inLanguage": "vi-VN"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Dịch vụ cung cấp",
               "item": B.GOC + "/dich-vu/"},
              {"@type": "ListItem", "position": 3, "name": d['menu'],
               "item": B.GOC + "/dich-vu/" + d['slug'] + "/"}]}]
    return than, ld


def _the_dv(d, i):
    return ('<a class="dv-the" href="@/dich-vu/%s/index.html">'
            '<div class="so">%02d</div><h3>%s</h3><p>%s</p>'
            '<span class="di">Xem chi tiết →</span></a>'
            % (d['slug'], i, html.escape(d['menu']), html.escape(d['mt'])))


def trang_dich_vu():
    khoi = []
    i = 0
    for ma, (ten_nhom, mau) in NHOM.items():
        cac = [d for d in DICH_VU if d['nhom'] == ma]
        the = []
        for d in cac:
            i += 1
            the.append(_the_dv(d, i))
        khoi.append('<h2 style="margin:30px 0 4px;border-left:4px solid %s;padding-left:12px">%s</h2>'
                    '<div class="dv-luoi">%s</div>' % (mau, html.escape(ten_nhom), ''.join(the)))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="@/index.html">Trang chủ</a> · Dịch vụ cung cấp</div>
  <h1>Chín dịch vụ tư vấn cho dự án đường sắt đô thị</h1>
  <p>Ngoài kiểm toán báo cáo quyết toán dự án hoàn thành, chúng tôi nhận thêm chín việc quanh
  phần tài chính và quản trị của một tuyến metro. Tất cả đều nằm trong phạm vi mà pháp luật
  cho phép một doanh nghiệp kiểm toán thực hiện — và chúng tôi nói rõ ranh giới đó ngay ở đây.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="the" style="border-left:3px solid var(--muc3)">
    <h3>Vì sao một hãng kiểm toán lại làm những việc này</h3>
    <p style="margin-top:8px">Vì cả chín việc đều là <b>bài toán tài chính</b>, không phải bài toán
    kỹ thuật công trình. Thu hồi vốn từ quỹ đất là một mô hình dòng tiền. Quy đổi suất vốn đầu tư
    nước ngoài là một phép quy đổi mặt bằng giá. Kiểm soát nội bộ là thiết kế chốt chặn trong luồng
    tiền. Đây là nghề của chúng tôi.</p>
    <p>Ngược lại, chúng tôi <b>không nhận</b> tư vấn quản lý dự án, giám sát thi công, thiết kế hay
    thẩm tra thiết kế. Không phải vì vướng giấy phép — mà vì chúng tôi không có đội kỹ sư công trình,
    và vì nhận rồi thì sau này lại đi kiểm toán chính công việc của mình.</p>
  </div>

  %(khoi)s

  <h2 style="margin:34px 0 10px">Ranh giới pháp lý, nói trước cho rõ</h2>
  <div class="luoi g2">
    <div class="the" style="border-left:3px solid var(--ngoc)">
      <h3>Chúng tôi được làm gì</h3>
      <p style="margin-top:8px">Điều 40 Luật Kiểm toán độc lập liệt kê dịch vụ mà một doanh nghiệp
      kiểm toán được thực hiện. <b>Khoản 1</b> gồm các dịch vụ kiểm toán, soát xét và dịch vụ bảo đảm
      khác — làm ngay. <b>Khoản 2</b> gồm tư vấn kinh tế, tài chính, thuế; tư vấn quản lý, chuyển đổi
      và tái cơ cấu doanh nghiệp; tư vấn ứng dụng công nghệ thông tin; dịch vụ kế toán; thẩm định giá;
      bồi dưỡng kiến thức tài chính, kế toán, kiểm toán — <b>phải đăng ký với Bộ Tài chính</b>.</p>
      <p>Cả chín dịch vụ trên trang này thuộc khoản 2.</p>
    </div>
    <div class="the" style="border-left:3px solid var(--do)">
      <h3>Chúng tôi không được làm gì</h3>
      <p style="margin-top:8px">Danh sách ở Điều 40 là <b>danh sách đóng</b>. Những gì không có tên
      trong đó thì doanh nghiệp kiểm toán không được bán — <b>kể cả dịch vụ pháp lý</b>. Khi Quý vị
      cần một ý kiến pháp lý thật sự, chúng tôi nói thẳng và giới thiệu tổ chức hành nghề luật sư,
      chứ không nhận rồi làm thay.</p>
      <p>Và theo Điều 30, chúng tôi không được cung cấp dịch vụ làm ảnh hưởng tới tính độc lập đối với
      đơn vị mà chúng tôi kiểm toán. Việc rà tính độc lập luôn chạy trước khi bàn tới giá.</p>
    </div>
  </div>

  <div class="the" style="border-left:3px solid var(--nhan);margin-top:20px">
    <h3>Bắt đầu từ đâu</h3>
    <p style="margin-top:8px">Nếu Quý vị chưa chắc việc mình đang vướng thuộc dịch vụ nào, cứ mô tả
    tình huống ở trang <a href="@/tu-van/index.html">Gửi yêu cầu tư vấn</a>. Chúng tôi phân loại giúp,
    và nếu việc đó không thuộc phạm vi chúng tôi được làm thì chúng tôi nói ngay.</p>
    <p class="small">Đầu mối: <b>0825092007</b> (có Zalo) · Tòa nhà ASCO, số 2, ngõ 308, phố Lê Trọng Tấn,
    phường Phương Liệt, thành phố Hà Nội.</p>
  </div>

</div></div>
""" % dict(khoi=''.join(khoi))

    ld = [{"@context": "https://schema.org", "@type": "ItemList",
           "name": "Dịch vụ tư vấn cho dự án đường sắt đô thị",
           "numberOfItems": len(DICH_VU),
           "itemListElement": [
               {"@type": "ListItem", "position": i + 1, "name": d['ten'],
                "url": B.GOC + "/dich-vu/" + d['slug'] + "/"}
               for i, d in enumerate(DICH_VU)]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B.GOC + "/"},
              {"@type": "ListItem", "position": 2, "name": "Dịch vụ cung cấp",
               "item": B.GOC + "/dich-vu/"}]}]
    return than, ld


# ================================================================= trang Tu van
def trang_tu_van():
    than, ld = V3.trang_tu_van()
    the = ''.join(_the_dv(d, i + 1) for i, d in enumerate(DICH_VU))
    khoi = """
  <h2 style="margin:34px 0 6px">Chín dịch vụ chúng tôi có thể nhận</h2>
  <p style="margin-bottom:4px">Ngoài việc trả lời vướng mắc, chúng tôi nhận thêm chín việc quanh phần
  tài chính và quản trị của dự án đường sắt đô thị. Bấm vào từng dịch vụ để xem chúng tôi làm gì,
  căn cứ nào và bàn giao lại những gì.</p>
  <p class="small" style="margin-bottom:6px">Tất cả đều thuộc khoản 2 Điều 40 Luật Kiểm toán độc lập
  và phải qua kiểm tra tính độc lập trước khi ký — chi tiết ở trang
  <a href="@/dich-vu/index.html">Dịch vụ cung cấp</a>.</p>
  <div class="dv-luoi">%s</div>
""" % the
    neo = '\n  <div class="cot2">'
    if neo not in than:
        raise SystemExit('KHONG TIM THAY cho chen khoi dich vu vao trang Tu van')
    than = than.replace(neo, khoi + neo, 1)
    return than, ld


# ================================================================= danh sach trang
TRANG = [(s, l, td, mt, (trang_tu_van if s == 'tu-van' else fn), tang)
         for s, l, td, mt, fn, tang in V11.TRANG]

TRANG += [('dich-vu', 'vi',
           'Dịch vụ tư vấn dự án đường sắt đô thị của ASCO',
           'Chín dịch vụ tư vấn tài chính và quản trị cho dự án đường sắt đô thị: thu hồi vốn TOD, '
           'phương án tài chính, suất vốn đầu tư, kiểm soát nội bộ và thuế.',
           trang_dich_vu, 'trong')]

for _d in DICH_VU:
    TRANG.append(('dich-vu/' + _d['slug'], 'vi', _d['td'], _d['mt'],
                  (lambda dd=_d: _trang_dv(dd)), 'trong'))


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
