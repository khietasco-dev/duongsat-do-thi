# Website Đường sắt đô thị — bản demo

## Chạy lại sau khi sửa nội dung

```
python ds_v8.py
```

Kịch bản sinh ra bảy trang HTML + sitemap.xml + robots.txt.

| Tệp | Việc |
|---|---|
| `ds_build.py` | Khung chung: bảng màu, CSS, thanh đầu, chân trang |
| `ds_data.py` | **Nội dung chuyên môn** — sửa ở đây là chính |
| `ds_pages.py` | Trang đích |
| `ds_pages2.py` | Trang văn bản, tư vấn, liên hệ + hàm ghi file |
| `ds_v2.py` | Trang quy trình, kinh nghiệm, vướng mắc |
| `ds_v3.py` | Bốn trang giao diện cấp 2 chi tiết |
| `ds_data2.py` | Nội dung kiểm toán quyết toán + thư viện rủi ro |
| `ds_v4.py` | Bộ chuyển ngôn ngữ + 2 trang mới |
| `ds_v5.py` | Trang tiếng Anh, tiếng Trung |
| `ds_ten.py` | **Tên 51 văn bản viết có dấu** — tra theo số hiệu |
| `ds_v6.py` | Logo in hoa · nút ngôn ngữ sổ xuống · cột Số hiệu |
| `ds_v7.py` | Trang Nhật, Pháp, Đức |
| `ds_tep.py` | **Chép 110 tệp văn bản vào trang** — chạy một lần |
| `ds_v8.py` | Liên kết mở tệp + **chạy file này** |
| `vb_phanloai.json` | 51 đầu văn bản, sinh từ kho VBPL |

## Hai tầng giao diện

Cách gọi thống nhất theo Tổng Giám đốc: **trang giao diện cấp 1** và **trang giao diện cấp 2**.


- **Tầng ngoài** `body.ngoai` — trang đích, nền chuyển sắc navy, ít chữ
- **Tầng trong** `body.trong` — trang công cụ, dải tiêu đề gọn, mật độ thông tin cao

## Bảng màu — lấy từ website ASCO

| Vai trò | Sáng | Tối |
|---|---|---|
| Thương hiệu | `#184088` | `#8FB2EE` |
| Nhấn | `#B8862A` | `#E0B458` |
| Hỗ trợ | `#0F6B54` | `#4FC0A2` |
| Cảnh báo | `#A82420` | `#F0857E` |

## ⚠️ Phông chữ — đừng đổi lại Georgia

Tiêu đề dùng `'Times New Roman', Times, 'Nimbus Roman', serif`.

**Không dùng Georgia.** Georgia thiếu glyph cho các chữ Việt vừa có dấu mũ vừa có dấu thanh
(ắ ầ ế ồ ấ), trình duyệt phải ghép dấu rời nên chữ vỡ: "sắt" hiện thành "să´t".
Đo bằng canvas: bề rộng chữ "ắ" trong Georgia gấp **1,99 lần** chữ "a";
trong Times New Roman tỷ lệ là **1,00**.

## ⚠️ Liên kết phải ghi rõ `index.html`

Mọi liên kết nội bộ viết dạng `van-ban/index.html`, **không viết `van-ban/`**.

Lý do: khi Tổng Giám đốc bấm đúp vào file để xem (giao thức `file://`), trình duyệt
**không tự tìm `index.html` trong thư mục** — nó chỉ liệt kê thư mục ra, thành một
màn hình đen kiểu "Chỉ mục của C:\...". Máy chủ web thì tự làm việc đó, nên lỗi này
chỉ lộ ra khi mở bằng file.

Cách viết `index.html` chạy đúng ở **cả hai** môi trường. Thẻ canonical vẫn khai
`/van-ban/` nên không ảnh hưởng tìm kiếm.

Kiểm nhanh trước khi giao: không được còn liên kết nội bộ nào kết thúc bằng dấu `/`.

## Ba ngôn ngữ

| Ngôn ngữ | Đường dẫn | Phạm vi |
|---|---|---|
| Tiếng Việt | `/` | **Toàn bộ 9 trang** |
| English | `/en/` | Một trang tổng quan |
| 中文 | `/zh/` | Một trang tổng quan |
| 日本語 | `/ja/` | Một trang tổng quan |
| Français | `/fr/` | Một trang tổng quan |
| Deutsch | `/de/` | Một trang tổng quan |

Bộ chuyển là **nút sổ xuống** nằm ngoài cùng bên phải thanh đầu, dựng bằng thẻ `<details>`
nên chạy được cả khi tắt JavaScript. Trên điện thoại nó đứng giữa logo và nút Mục lục.

Lý do chỉ làm một trang cho mỗi ngoại ngữ: phần lõi của trang là **danh mục văn bản
pháp luật Việt Nam**, mà văn bản đó chỉ có bản chính thức bằng tiếng Việt — dịch tên
văn bản ra tiếng Anh rồi để người ta trích dẫn là tạo rủi ro. Trang ngoại ngữ vì thế
tập trung vào thứ người nước ngoài cần: **chín giai đoạn dự án**, **ba lỗi họ hay mắc**,
và **khái niệm kiểm toán song hành**.

## ⚠️ Thanh đầu rất chật — đừng thêm mục menu

Thanh đầu đang có: logo + **8 mục menu** + nút ngôn ngữ. Ở màn 1425px chỉ còn dư
khoảng 120px. Thêm một mục nữa là tràn.

Muốn thêm mục thì phải làm một trong ba việc: rút ngắn nhãn mục đang có, hạ cỡ chữ
menu, hoặc nâng ngưỡng gộp menu (hiện là 1160px) lên cao hơn.

Hai lỗi đã vấp về thanh đầu:
- `.top-in` đặt `padding:11px 0` **ghi đè lề hai bên** của `.wrap`, làm thanh đầu chạy
  sát mép trên điện thoại. Đã sửa thành `padding:11px 22px`.
- Logo `ĐƯỜNG SẮT ĐÔ THỊ` in hoa dài 181px ở cỡ 14px — trên màn 375px phải hạ xuống
  13,4px và bỏ giãn chữ mới đủ chỗ.

## ⚠️ Favicon nhúng sẵn có ký tự phần trăm

`ds_build.py` nhúng favicon dạng `data:image/svg+xml,...` — chuỗi này chứa **179 ký tự `%`**
đã được nhân đôi thành `%%` để không làm hỏng khuôn định dạng chuỗi của Python.
Sửa favicon thì nhớ nhân đôi lại.

## Bấm vào văn bản là mở được tệp

`van-ban/tep/` chứa **110 tệp Word và PDF, 139 MB**, chép từ kho VBPL trong vault.

| Cách bấm | Mở gì |
|---|---|
| Bấm **tên văn bản** | Bản Word; văn bản nào không có Word thì mở PDF |
| Bấm nút **DOC** hoặc **PDF** ở cột Mở tệp | Đúng định dạng đó |
| Văn bản nhiều phần | Hiện **W1 W2…** hoặc **P1 P2…**, phải mở hết mới đủ |

39/51 văn bản có bản Word · 51/51 có PDF · 5 văn bản chia nhiều phần.

⚠️ **Dung lượng kho nhảy từ 954 KB lên 140 MB.** Các kho ASCO khác chỉ 3–4 MB.
Lần đẩy đầu tiên lên GitHub sẽ lâu. Nếu muốn kho nhẹ thì bỏ `van-ban/tep/` vào
`.gitignore` và thay liên kết bằng đường dẫn tới nguồn chính thức trên Công báo —
nhưng khi đó trang chạy trên mạng sẽ không mở được tệp.

Tên tệp đã **bỏ dấu tiếng Việt và thay khoảng trắng bằng gạch nối** để địa chỉ web
không bị mã hoá lung tung. Xem hàm `gon()` trong `ds_tep.py`.

## Ban 9 — May tinh phi kiem toan quyet toan (ds_v9.py)

Trang `/kiem-toan/` co them khoi may tinh phi theo **Nghi dinh 193/2026/ND-CP Dieu 20**
(ban hanh 01/6/2026, hieu luc 01/7/2026).

Bang ty le nam trong `ds_v9.MOC / KT / TT` **va** lap lai trong khoi JavaScript
`B.than_js['kiem-toan']`. **Sua so thi phai sua CA HAI CHO.**

Da doi chieu tung con so: ty le cua ND 193/2026 Dieu 20 **giu nguyen** so voi
ND 254/2025 Dieu 45. Chi doi so dieu (45 -> 20) va dan chieu (Dieu 36 -> Dieu 11).

Ban goc Word + PDF luu tai kho VBPL:
`111 VBPL\VBPL theo Luat\Luat Dau tu cong 58-2024-QH15\02 - Nghi dinh\ND 193 2026 ...`

Quy tac da cai vao may tinh:
- Noi suy tuyen tinh diem a: `Ki = Kb - (Kb-Ka)(Gi-Gb)/(Ga-Gb)`
- Chi phi thiet bi >= 50% -> **70%** (diem d)
- Chi phi boi thuong, ho tro, tai dinh cu -> **50%** (diem d)
- Da kiem toan doc lap / KTNN / thanh tra theo Dieu 11 -> phi **tham tra** = **50%** (diem e)
- Toi thieu: kiem toan **1 trieu dong** + VAT; tham tra **500 nghin dong**
- Phi kiem toan la **muc toi da**, cong VAT; phi tham tra khong cong VAT

## Ban 10 — hotline, nut chon ngon ngu, ngay cap nhat (ds_v10.py)

- Duoi logo ĐƯỜNG SẮT ĐÔ THỊ ghi **HOTLINE: 0825092007** (chi ghi, khong bam duoc —
  vi ca khoi logo da la mot the `<a>` roi, long `<a>` trong `<a>` la HTML sai).
- Nut ngon ngu doi nhan tu ten ngon ngu hien tai thanh **"Chọn ngôn ngữ"**
  (moi ngon ngu mot nhan rieng). Thu tu trong menu: Viet - Anh - Trung - Nhat - Phap - Duc.
- Dong duoi cung chan trang: **"Văn bản được cập nhật đến <NGAY_CAP_NHAT>"**.

⚠️ **Sua ngay cap nhat CHI o MOT CHO**: hang `NGAY_CAP_NHAT` dau file `ds_v10.py`,
roi chay `python ds_v10.py`. Dung sua tay trong cac file index.html.

⚠️ **Chay `ds_v10.py`, khong con chay `ds_v9.py`.** Moi ban ke thua ban truoc.

Thanh dau con **~32px du** o 1175px (diem chat nhat, ngay tren nguong gop menu 1160px).
Them mot muc menu nua la tran — phai rut nhan hoac nang nguong gop.

## Ban 11 — THANH DAU HAI HANG, bo han nut "Muc luc" (ds_v11.py)

CEO chot 25/08/2026: menu phai hien thang tren banner, khong gom vao nut "Muc luc".

- **Hang 1**: logo ĐƯỜNG SẮT ĐÔ THỊ + hotline (trai) · nut Chon ngon ngu (phai)
- **Hang 2**: du 8 muc menu, luon hien, tu xuong dong khi het cho
- Nut "Muc luc" bi go o **MOI kho man hinh** — the `<button>` khong con trong HTML
- Giu nhan viet tat "Kiem toan QT" theo y CEO

### So do da do that trong trinh duyet

| Kho man hinh | Menu | Cao thanh dau | Dinh man hinh |
|---|---|---|---|
| 1280px | 1 dong, du 8 muc | 108px | co |
| 768px  | 1 dong, du 8 muc | 107px | co |
| 375px  | 2 dong, du 8 muc | 125px | **khong** (cuon di) |
| 320px  | 3 dong, du 8 muc | 153px | **khong** |

Duoi 700px thanh dau chuyen `position:relative` — menu hai ba dong ma con dinh
theo man hinh thi an mat mot phan sau man hinh dien thoai.

### 🐛 Loi CU da lo ra khi lam viec nay

Luat chung `details{border;background;padding:15px 18px;margin-bottom:10px}` (dung cho
khoi hoi-dap o trang Vuong mac) **dinh ca vao nut ngon ngu** `<details class="nn">`:
no ve them mot khung vien thua quanh nut va lam hang 1 cao **100px** thay vi 58px.
Da go bang `.nn{padding:0!important;border:0!important;background:none!important;...}`.

→ Nho lay: **them mot the HTML pho thong (`details`, `table`, `ul`) vao thanh dau thi
phai kiem xem luat chung cua the do co dinh vao khong.**

## Ban 12 — MENU IN HOA + muc "DICH VU CUNG CAP" (ds_v12.py, ds_dv.py)

CEO chot 25/08/2026. Trang tu 14 len **24 trang**.

- Menu tren banner **IN HOA** — lam bang `text-transform:uppercase`, chu trong HTML
  van viet thuong (de bo doc man hinh va cong cu tim kiem doc dung).
- Them muc **"Dich vu cung cap"** dang so xuong (`<details class="dv">`), xo ra 10 lien ket:
  1 trang tong + 9 dich vu, chia 3 nhom.
- **9 trang gioi thieu dich vu** tai `/dich-vu/<slug>/` + **1 trang tong** `/dich-vu/`.
- Trang `/tu-van/` duoc chen them khoi 9 the dich vu.

Noi dung 9 dich vu nam trong **`ds_dv.py`** — sua noi dung thi sua file do, khong sua HTML.

### ⚠️ Ba cai bay da vap khi lam ban nay

1. **Trang nam sau HAI cap.** Khuon goc chi tinh duong dan lui MOT cap (`../`).
   Xu ly trong `ds_v12.khung()`: lui them mot cap cho lien ket cua khuon, con lien ket
   trong ruot trang viet bang dau **`@/`** (= goc trang) roi thay sau. **Dung viet `../`
   trong ruot trang dich vu** — no se bi lui nham.
2. **`.top-nav{position:static!important}` cua ban 11** lam bang xo xuong tren dien thoai
   bam nham vao the cha cao hon → tran ra mep man hinh. Phai ghi de bang
   `position:relative!important`.
3. **Dung dat `.dv{width:100%}` tren dien thoai** — muc do se chiem tron mot dong,
   menu doi tu 3 len 4 dong.

### So do da do

| Kho man hinh | Menu | Cao thanh dau | Bang xo xuong |
|---|---|---|---|
| 1280px | 9 muc mot dong | 106px | noi, rong 330px, khong tran |
| 375px  | 9 muc bon dong | 152px | bam theo hang menu, khong lam cao them thanh dau |

**Da ra 1.002 lien ket noi bo tren ca 24 trang: 0 lien ket hong.**

## Ban 13 — DONG BO NGON NGU CHO THANH MENU (ds_v13.py)

CEO phat hien 25/08: bam sang trang tieng Anh thi menu tren cung van tieng Viet.
Nay ca thanh menu + bang so xuong "Dich vu cung cap" doi theo ngon ngu trang.

**Chay `python ds_v13.py`** — ban moi nhat.

Bang nhan nam trong `ds_v13.py`: `NHAN` (8 muc menu) · `NHAN_DV` (nut so xuong) ·
`NHAN_TAT` · `NHAN_NHOM` (3 nhom) · `NHAN_MUC_DV` (9 dich vu) · `NHAC`.
**Nhan tieng Viet la KHOA tra cuu** — doi nhan tieng Viet o ban truoc thi phai doi ca o day,
neu khong script se dung han va bao "KHONG THAY nhan menu".

### Noi that voi nguoi doc nuoc ngoai

Cac trang dich den VAN LA TIENG VIET (chi 6 trang tong quan co ban dich). Nen tren trang
ngoai ngu moi lien ket menu duoc gan:
- `hreflang="vi"` — cho cong cu tim kiem biet
- `title="page in Vietnamese"` (dich theo tung thu tieng) — hien khi ro chuot
- mot dau **VI** nho o goc tren ben phai nhan — nguoi doc biet TRUOC khi bam

### So do da do (be rong hang menu 1.136px)

| Trang | Be rong menu | Con du |
|---|---|---|
| vi | 840px | 160px |
| de | 791px | 209px |
| en | 722px | 278px |
| fr | 709px | 291px |
| zh | 590px | 410px |
| ja | 563px | 437px |

Ca 6 trang: menu **mot dong**, thanh dau **106px**, khong tran ngang.
Tren dien thoai 375px: 3 dong, thanh dau 154px, bang so xuong khong tran mep.
Ra lai 1.002 lien ket noi bo: **0 hong**.
