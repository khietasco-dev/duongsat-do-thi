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
