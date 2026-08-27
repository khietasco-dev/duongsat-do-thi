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

## Ban 14 — TRANG BEN TRONG DOI THEO NGON NGU, DOT 1 (ds_v14.py, ds_dv_dich.py)

CEO 25/08: bam sang tieng Anh thi trang ben trong cung phai tieng Anh.
**Da do: 18 trang tieng Viet = 28.953 tu. Nhan 5 thu tieng = ~145.000 tu.**
Khong dich tron trong mot lan duoc — chia dot.

**Dot 1 (xong):** trang tong dich vu `/en/dich-vu/` `/zh/` `/ja/` `/fr/` `/de/` — 5 trang
dich TRON VEN. Chon trang nay truoc vi: (a) la trang thuong mai quan trong nhat,
(b) la van cua chinh minh, khong co trich dan dieu luat nen dich an toan.
Trang tu 24 len **29**.

**Nut ngon ngu nay BIET DANG DUNG TRANG NAO** (`ds_v14._bo_ngon_ngu`):
- Dung o `/dich-vu/` bam DE -> `/de/dich-vu/` (dung trang do, thu tieng do)
- Dung o `/van-ban/` bam DE -> `/de/` (chua co ban dich thi ve trang tong quan)
- Bang `DA_DICH` khai bao chu de nao da co ban dich o thu tieng nao.
  **Dich xong trang nao thi them vao `DA_DICH`**, nut ngon ngu tu biet duong.

Ban dich nam trong **`ds_dv_dich.py`**: `TRANG` (khung trang) + `MO_TA` (9 the).

### Nguyen tac dich cua trang nay

Chi dich **van cua chinh minh**. KHONG dich ten van ban phap luat, KHONG dich trich dan
dieu khoan — chi dan so hieu kem chu giai. Ly do: ban tieng Viet moi la ban chinh thuc,
dich sai mot chu la doi nghia dieu luat.

**Con lai chua lam:** 8 trang tieng Viet con lai o ban tieng Anh, va ca 18 trang o
4 thu tieng kia — khoang **130.000 tu**.

## Ban 15 — 9 TRANG DICH VU CAP 2 BANG TIENG ANH (dot 2, ds_v15.py, ds_dv_en.py)

CEO 25/08: o che do tieng Anh, bam vao tung dich vu van ra tieng Viet.
Da dung `/en/dich-vu/<slug>/` cho ca 9 dich vu. Trang **29 -> 38**.

**Chay `python ds_v15.py`** — ban moi nhat.

Sau ban nay, o che do TIENG ANH nhanh Dich vu da LIEN MACH:
menu -> bang so xuong -> trang tong -> 9 trang chi tiet, khong con roi ve tieng Viet.

Ban dich trong **`ds_dv_en.py`**: `KHUNG` (khung trang) + `EN` (9 dich vu).

### Cach them mot trang dich moi

1. Viet noi dung vao file `ds_dv_<thu tieng>.py`
2. Khai vao `V14.DA_DICH['<chu de>'] = {'<thu tieng>'}` — nut ngon ngu tu biet duong
3. Them vao `TRANG` voi slug `<thu tieng>/<chu de>`

Trang nam sau BA cap (`en/dich-vu/<slug>`) — bo lui duong dan cua ban 12 tu xu ly,
khong phai sua gi.

### Nguyen tac dich, khong lam khac

Phan "Legal basis" ghi ro la **dien giai cua ASCO, khong phai ban dich chinh thuc**,
va tro nguoi doc ve ban goc tieng Viet o muc Tra cuu van ban. Cau nay nam trong
`KHUNG['cancu_nhac']` — **giu nguyen o moi thu tieng se dich sau**.

**Con lai:** 8 trang tieng Viet con lai o ban tieng Anh, va ca 18 trang o 4 thu tieng kia.

## Ban 16 — BON TRANG TIENG ANH (dot 3, ds_v16.py, ds_en_qt.py, ds_en_tv.py)

`/en/quy-trinh/` · `/en/kiem-toan/` · `/en/tu-van/` · `/en/lien-he/`. Trang **38 -> 42**.
**Chay `python ds_v16.py`** — ban moi nhat.

O che do tieng Anh nguoi doc nay di duoc tron mach:
Dich vu -> Quy trinh -> Kiem toan QT -> Tu van -> Lien he.

- `ds_en_qt.py` — Quy trinh (9 giai doan, 4 ngan phap ly, 3 cho ho) + Kiem toan QT
  (5 ly do song hanh, bang so sanh 7 dong, 13 phan hanh, 2 phep can doi, 3 dieu khong lam,
  may tinh phi)
- `ds_en_tv.py` — Tu van (3 loai yeu cau, bieu mau, 9 the dich vu) + Lien he

**May tinh phi ban tieng Anh** o `B.than_js['en/kiem-toan']` — bang ty le van lay tu
`ds_v9.KT` va `ds_v9.TT` nen sua so mot cho la ca hai ban doi theo. Da doi chieu:
120 ty ra 445.500.000 dong, dung y het ban tieng Viet.

⚠️ **TEN VAN BAN PHAP LUAT GIU NGUYEN TIENG VIET** — Luat Dat dai 31/2024/QH15,
NĐ 206/2026… la ten chinh thuc, dich ra la sai. Da ra lai: chu tieng Viet con lai tren
trang tieng Anh CHI la ten van ban va chan trang.

**Con lai o ban tieng Anh:** Van ban · Thu vien rui ro · Kinh nghiem · Vuong mac.
Chan trang cung chua dich.

## Ban 17 — BO TIENG ANH XONG (dot 4, ds_v17.py, ds_en_rr.py, ds_en_kn.py)

`/en/van-ban/` · `/en/thu-vien-rui-ro/` · `/en/kinh-nghiem/` · `/en/vuong-mac/` + CHAN TRANG.
Trang **42 -> 46**. **Chay `python ds_v17.py`** — ban moi nhat.

**Menu tren trang tieng Anh nay 0 dau VI** — moi muc deu co ban tieng Anh.

⚠️ **BAY DA VAP: kho tep nam o `/van-ban/tep/`.** Trang `/en/van-ban/` o thu muc khac nen
duong dan tuong doi `tep/...` tro sai — 161 lien ket hong. Da sua bang `_o_tep()` doi thanh
`@/van-ban/tep/...`. **Bat ky ban dich nao cua trang Van ban sau nay deu phai lam vay.**

Chan trang: `ds_en_kn.CHAN['en']`, thay bang `ds_v17._chan()`. Ngay cap nhat van lay tu
`ds_v10.NGAY_CAP_NHAT` (doc nguoc tu chan trang tieng Viet) nen chi phai sua mot cho.

Trang `/en/van-ban/` da thu that: 51 van ban, o tim bo dau hai phia ("duong sat" ra 33),
bon bo loc chay, bam ten van ban tai duoc tep (681 KB, ma 200).

**Bo tieng Anh coi nhu xong.** Buoc sau: tieng Trung — dung lai khuon nay, chi thay noi dung.

## Ban 18 — BON TRANG TIENG TRUNG (dot 1 bo tieng Trung, ds_v18.py)

`/zh/quy-trinh/` · `/zh/kiem-toan/` · `/zh/tu-van/` · `/zh/lien-he/` + chan trang tieng Trung.
Trang **46 -> 50**. **Chay `python ds_v18.py`** — ban moi nhat.
Ban dich: `ds_zh_qt.py` (Quy trinh + Kiem toan QT) va `ds_zh_tv.py` (Tu van + Lien he + chan trang).

### ⚠️ RANG BUOC THUAT NGU — da nap tu bo cua ASCO

Nguon: `02 - ASCO/Thuat ngu va cau mau song ngu/asco_thuat_ngu.json` (244 muc).

| Viet | Trung | Bay |
|---|---|---|
| Quyet toan DU AN | **竣工决算** | KHONG phai 汇算清缴 (do la quyet toan THUE) |
| Mot ty dong | **十亿越南盾** | ⚠ **亿 chi la 100 TRIEU** — sai 10 lan |
| Hop dong kiem toan | **审计业务约定书** | Khong phai 审计合同 |
| Chung kien kiem ke | **监盘** | Khong phai 盘点 (tu di dem) |
| Khau tru VAT | **增值税进项税额抵扣** | KHAC 税前可扣除费用 (duoc tru thue TNDN) |
| Y kien chap nhan toan phan | **无保留意见** | Thieu chu 无 la thanh y kien NGOAI TRU |

🔴 **DA VAP MOT LAN NGAY TRONG BAN NAY:** viet "几千亿盾" cho "nhieu nghin ty dong" —
sai 10 lan. Da sua thanh **数万亿越南盾** (1.000 ty = 10^12 = 一万亿).
**Moi lan viet so tien tieng Trung phai doi chieu lai bang tren.**

May tinh phi tieng Trung dung don vi **十亿越南盾**, da doi chieu: 120 ty ra
445.500.000 越南盾 — dung y het ban tieng Viet va tieng Anh.

**Con lai o bo tieng Trung:** 9 trang dich vu + Van ban · Thu vien rui ro · Kinh nghiem · Vuong mac.
Menu trang tieng Trung con **13 dau VI** — dung bang so muc chua dich.

## Ban 19 — BO TIENG TRUNG XONG (dot 2, ds_v19.py)

9 trang `/zh/dich-vu/<slug>/` + `/zh/van-ban/` `/zh/thu-vien-rui-ro/` `/zh/kinh-nghiem/`
`/zh/vuong-mac/`. Trang **50 -> 63**. **Chay `python ds_v19.py`** — ban moi nhat.
Ban dich: `ds_zh_dv.py` (9 dich vu) · `ds_zh_rr.py` (Van ban + Rui ro) · `ds_zh_kn.py`
(Kinh nghiem + Vuong mac).

✅ **Menu tren trang tieng Trung: 0 dau VI.** Da kiem tren 4 trang mau o cac cap khac nhau.

⚠️ **BAY MOI: dung va CHUOI JAVASCRIPT cua ban tieng khac.**
Ban dau viet `B.than_js['zh/van-ban'] = B.than_js['en/van-ban'].replace(...)` — phep thay
KHONG an, va cau tieng Anh "51 of 51 instruments" lot len trang tieng Trung.
Da doi thanh viet han mot khoi JS rieng. **Moi thu tieng mot khoi JS rieng, dung va chuoi.**

Bo dem ban tieng Trung nay hien "共 51 份，显示 33 份" — da thu that.

## Ban 20 — BON TRANG TIENG NHAT (dot 1 bo tieng Nhat, ds_v20.py)

`/ja/quy-trinh/` · `/ja/kiem-toan/` · `/ja/tu-van/` · `/ja/lien-he/` + chan trang tieng Nhat.
Trang **63 -> 67**. **Chay `python ds_v20.py`** — ban moi nhat.
Ban dich: `ds_ja_qt.py` (Quy trinh + Kiem toan QT) va `ds_ja_tv.py` (Tu van + Lien he + chan trang).

### ⚠ BAY DA VAP NGAY TRONG BAN NAY — ke thua nham ban cha

Viet `import ds_v18 as V18` roi `TRANG = list(V18.TRANG)`. Chay ra **54 trang thay vi 67** —
roi mat 13 trang tieng Trung cua ban 19, va **sitemap.xml thieu 13 dia chi**.
Cac file index.html cu van con tren dia nen khong lo mat, nhung Google chi doc sitemap.

→ **Moi ban moi phai ke thua ban LIEN TRUOC, khong phai ban minh nho toi.**
Kiem nhanh: dong "Da ghi N trang" phai bang so trang ban truoc cong so trang moi them.

### ⚠ DON VI TIEN TIENG NHAT — cung bay nhu tieng Trung

`億` = **100 TRIEU**, khong phai ty. `兆` = 10^12.

| Viet | Nhat |
|---|---|
| 1 ty dong | 十億ドン |
| 5 ty dong | 50億ドン |
| 1.000 ty dong | 1兆ドン |
| 10.000 ty dong | 10兆ドン |

Da kiem tren trinh duyet that: moc duoi hien "監査対象額 50億ドン以下",
moc tren hien "10兆ドン以上" — dung. Da ra: trang tieng Nhat khong lot `亿`,
`越南盾` hay `billion` cua ban tieng khac.

### 🔧 SUA MOT LOI CU — bieu mau Tu van bao loi bang tieng Viet

`B.than_js['tu-van']` chua hai cau thong bao tieng Viet. Ban 17 gan nguyen khoi do cho
`en/tu-van`, ban 18 gan cho `zh/tu-van`. Nghia la **nguoi doc tieng Anh va tieng Trung
bam Gui van thay tieng Viet** — ton tai tu 25/08.

Ban 20 tach `_JS_MAU` + bang `_MAU_NHAN` sinh khoi JS rieng cho tung thu tieng va gan lai
cho ca `en`, `zh`, `ja`. Da thu that tren trinh duyet: ba ban ra ba thu tieng, 0 ky tu tieng Viet.

### ⚠ MUC FAQ "tra loi bang ngon ngu nao" — da viet THAN TRONG

Ban tieng Trung hua tra loi bang 中文 vi ASCO co bo cong cu ngon ngu Trung Quoc (244 thuat ngu).
**Voi tieng Nhat CHUA co bo tuong duong**, nen ban nay chi hua tra loi chinh thuc bang
**tieng Viet hoac tieng Anh**, con tieng Nhat thi nhan cau hoi. **CEO can quyet: giu nhu vay,
hay nang len thanh co tra loi tieng Nhat?** Neu nang thi phai co nguoi bao dam chat luong.

### Da do that tren trinh duyet

| Muc | Ket qua |
|---|---|
| May tinh phi 120 ty | **445.500.000 ドン** — dung y ban Viet, Anh, Trung |
| Moc duoi 5 ty | 0,96% · 52.800.000 ドン |
| Moc tren 20.000 ty | 0,069% · 15.180.000.000 ドン |
| He so 70% (thiet bi ≥50%) | 311.850.000 ドン |
| Bo trong | "ゼロより大きい数値を入力してください。" |
| Thanh dau 1280px | 107px, menu mot dong, du 458px |
| Thanh dau 375px | 128px, `position:relative`, khong tran |
| Bang ty le tren dien thoai | co thanh cuon rieng, khong lam tran trang |
| Lien ket noi bo toan site | **2.870 lien ket, 0 hong** |
| Sitemap | 67 dia chi, 6 dia chi `/ja/` |

**Chu tieng Viet con lai tren 4 trang tieng Nhat CHI la ten van ban phap luat** va ky hieu
diem `đ` cua dieu luat — dung nguyen tac da chot.

**Menu trang tieng Nhat con 13 dau VI** = 4 muc menu chua dich (Van ban · Thu vien rui ro ·
Kinh nghiem · Vuong mac) + 9 trang dich vu. Dung bang ban tieng Trung sau dot 1.

⚠ **Cot dau chan trang van ghi "Urban railway"** o ca ban `zh` va `ja` — chuoi nay hardcode
trong `ds_v17._chan()`. Khong sai (do la ten thuong hieu) nhung neu muon dich thi them mot
khoa vao `CHAN[lang]` va sua `_chan()` — sua mot cho, ca hai ban doi theo.

**Con lai o bo tieng Nhat:** 9 trang dich vu + Van ban · Thu vien rui ro · Kinh nghiem · Vuong mac
= **13 trang**. Khuon da san, lam theo ds_v19.py.

## Ban 21 — BO TIENG NHAT XONG (dot 2, ds_v21.py)

9 trang `/ja/dich-vu/<slug>/` + `/ja/van-ban/` `/ja/thu-vien-rui-ro/` `/ja/kinh-nghiem/`
`/ja/vuong-mac/`. Trang **67 -> 80**. **Chay `python ds_v21.py`** — ban moi nhat.
Ban dich: `ds_ja_dv.py` (9 dich vu) · `ds_ja_rr.py` (Van ban + Rui ro) ·
`ds_ja_kn.py` (Kinh nghiem + Vuong mac).

✅ **Menu tren ca 19 trang tieng Nhat: 0 dau VI.** Chan trang tieng Nhat: 19/19 trang.

### 🔧 SUA MOT LOI CU NUA — nhan "N phần" tieng Viet tren ban ngoai ngu

O cot **Mo tep** cua trang Van ban, van ban chia nhieu ky hien nhan `N phần`.
Chuoi do sinh trong `ds_v8.o_tep()` va **ban 17 (en) va ban 19 (zh) deu bi**, moi ban
5 van ban. Nay `ds_v21._tep_lang(d, lang)` dich theo tung thu tieng va **ghi de lai**
`V17._o_tep` va `V19._o_tep` — sua mot cho, ca ba ban doi theo.

| Ban | Nhan |
|---|---|
| vi | `5 phần` |
| en | `5 parts` |
| zh | `共 5 部分` |
| ja | `全 5 部` |

### Da do that tren trinh duyet

| Muc | Ket qua |
|---|---|
| Bo dem trang Van ban ja | `全 51 件中 51 件を表示` |
| Tim bo dau hai phia | `duong sat` va `đường sắt` deu ra **33/51** — dung y ban Viet va Trung |
| Tim theo so hieu `188` | 3 van ban |
| Loc `Thông tư` | 12 van ban |
| Lien ket tep tren /ja/van-ban/ | **161 lien ket**, thu 4 mau deu ma **200** (681 KB · 1.170 KB · 246 KB) |
| Nhan phan nhieu ky | 全 2 部 · 全 2 部 · 全 3 部 · 全 2 部 · **全 6 部** (TT 59/2024) |
| Trang dich vu TOD | 3 can cu · 5 buoc · thanh dau 106px · 0 dau VI |
| Trang Kinh nghiem | 12 bai hoc · 3 sai lam · 5 moc |
| Thu vien rui ro | **33 rui ro · 8 nhom**, danh so den 33, 33 muc do |
| Vuong mac | 10 vuong mac, 4 o nhan tieng Nhat |
| Trang tong dich vu ja | 9 the, **0 the tro ve tieng Viet** |
| Lien ket noi bo toan site | **3.486 lien ket, 0 hong** |
| Sitemap | **80 dia chi** — ja 19 · zh 19 · en 19 |

**Nhanh Dich vu o che do tieng Nhat nay LIEN MACH:** menu → bang so xuong → trang tong
→ 9 trang chi tiet, khong con roi ve tieng Viet.

⚠ **Cau bat buoc o moi ban dich** (`ds_ja_dv.KHUNG['cancu_nhac']`): phan 根拠法令 ghi ro
day la **cach doc cua ASCO, khong phai ban dich chinh thuc**, va tro ve ban goc tieng Viet.
Da kiem tren trang chay that: co.

⚠ **Hai dieu kien truoc khi ky** (`KHUNG['luu']`): dang ky voi Bo Tai chinh theo
Dieu 40 khoan 2, va kiem tinh doc lap theo Dieu 30. Da kiem: co tren trang.

### Con lai cua ca du an

**Ba thu tieng con lai — Phap, Duc — moi thu 18 trang.** Khuon da san, lam theo
ds_v20 + ds_v21. Nhung can nhac truoc: nha thau Phap va Duc lam ODA o Viet Nam deu doc
duoc tieng Anh, nen gia tri tang them thap hon nhieu so voi ba bo da lam.

🔴 **Van con: canonical tro vao ten mien khong ton tai** (`ds_build.GOC`), nay anh huong
**ca 80 trang**. Chua sua vi cho CEO quyet.
