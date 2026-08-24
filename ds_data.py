# -*- coding: utf-8 -*-
"""Noi dung chuyen mon — chin giai doan, bon ngan phap ly, muoi vuong mac,
muoi hai bai hoc, danh muc kiem tra. Nguon: agent kiem-toan-du-an-asco doc kho VBPL.
"""

# ---------------------------------------------------------------- bon ngan
NGAN_PHAP_LY = [
    ("A", "Metro Hà Nội / TP.HCM, vốn đầu tư công", "Địa bàn Hà Nội hoặc TP. Hồ Chí Minh",
     "NQ 188/2025/QH15 · Luật Đường sắt 95/2025/QH15 · VBHN 34/VBHN-BXD", "ngoc"),
    ("B", "Metro địa bàn khác, vốn đầu tư công", "Ngoài Hà Nội và TP. Hồ Chí Minh",
     "Luật Đường sắt 95/2025/QH15 · Luật Đầu tư công 58/2024/QH15 · Luật Xây dựng. "
     "Không được viện dẫn NQ 188", "do"),
    ("C", "Metro theo phương thức PPP", "Thực hiện bằng hợp đồng PPP",
     "Luật PPP 64/2020/QH14 (bản hợp nhất 81/VBHN-VPQH) · NĐ 243/2025 · NĐ 312/2025", "nhan"),
    ("D", "Khu vực TOD gắn với tuyến", "Vùng phụ cận nhà ga, đề-pô",
     "Luật Thủ đô 02/2026/QH16 · Nghị quyết HĐND địa phương "
     "(Hà Nội: NQ 71/2025, 66/2026, 67/2026 — TP.HCM: NQ 21/2026)", "muc"),
]

# ---------------------------------------------------------------- chin giai doan
GIAI_DOAN = [
    ("Quy hoạch và hình thành ý tưởng tuyến",
     "Đưa tuyến vào quy hoạch tỉnh và quy hoạch chung đô thị; xác định hướng tuyến, vị trí ga và đề-pô; "
     "lập phương án tuyến; khoanh định sơ bộ khu vực TOD.",
     "UBND cấp tỉnh trình, HĐND cấp tỉnh thông qua phần thuộc thẩm quyền",
     "Luật Quy hoạch đô thị và nông thôn 47/2024/QH15 · Luật Quy hoạch 112/2025/QH15 · "
     "Hà Nội: NQ 64/2026/NQ-HĐND về quy hoạch không gian ngầm",
     "Quy hoạch tuyến được duyệt · phương án tuyến · ranh giới sơ bộ khu vực TOD",
     "Hướng tuyến vẽ trên bản đồ nhưng chưa cắm mốc thực địa nên giải phóng mặt bằng về sau bị lệch. "
     "Quy hoạch không gian ngầm chưa có nên chưa xác định được ranh giới tầng ngầm của nhà ga."),

    ("Chủ trương đầu tư",
     "Lập báo cáo đề xuất chủ trương đầu tư hoặc báo cáo nghiên cứu tiền khả thi; thẩm định nguồn vốn "
     "và khả năng cân đối vốn; quyết định chủ trương đầu tư.",
     "Quốc hội với dự án quan trọng quốc gia · Thủ tướng Chính phủ · HĐND cấp tỉnh",
     "Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (sửa bởi NĐ 275/2025) · NĐ 19/2026 về thẩm định "
     "dự án quan trọng quốc gia",
     "Nghị quyết hoặc quyết định chủ trương đầu tư · sơ bộ tổng mức đầu tư · cơ cấu nguồn vốn",
     "Sơ bộ tổng mức đầu tư lập trên khảo sát mỏng nên chênh lệch lớn khi lập dự án. Khi dự án được "
     "miễn bước này theo cơ chế đặc thù thì hồ sơ quyết toán thiếu một mắt xích quen thuộc — phải "
     "chuẩn bị sẵn văn bản giải trình căn cứ miễn."),

    ("Lập, thẩm định và phê duyệt dự án",
     "Khảo sát xây dựng; lập báo cáo nghiên cứu khả thi và thiết kế cơ sở, hoặc thiết kế kỹ thuật "
     "tổng thể theo cơ chế đặc thù; thẩm định của cơ quan chuyên môn; thẩm duyệt phòng cháy chữa cháy "
     "và đánh giá tác động môi trường.",
     "Người quyết định đầu tư theo phân cấp; với dự án thuộc NQ 188 thì phân cấp mạnh cho địa phương",
     "Luật Xây dựng 135/2025/QH15 · NĐ 209/2026 và NĐ 210/2026 · NĐ 206/2026 về quản lý chi phí · "
     "VBHN 34/VBHN-BXD về thiết kế kỹ thuật tổng thể",
     "Quyết định phê duyệt dự án · tổng mức đầu tư được duyệt — đây là trần pháp lý của toàn bộ "
     "chi phí quyết toán về sau",
     "Khối lượng phần ngầm là chỗ sai số lớn nhất giữa thiết kế và địa chất thực tế. Dự án lập trước "
     "ngày 30/7/2026 chưa có quy chuẩn riêng cho metro nên phải mượn tiêu chuẩn nước ngoài."),

    ("Giải phóng mặt bằng và tái định cư",
     "Thông báo thu hồi đất; kiểm đếm; lập, niêm yết và phê duyệt phương án bồi thường, hỗ trợ, "
     "tái định cư; chi trả; bàn giao mặt bằng theo từng đợt. Chạy song song với giai đoạn 3.",
     "UBND cấp có thẩm quyền thu hồi đất và phê duyệt phương án",
     "Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · "
     "Hà Nội tại khu vực TOD: NQ 66/2026/NQ-HĐND",
     "Quyết định thu hồi đất từng thửa · phương án bồi thường được duyệt · biên bản bàn giao mặt bằng",
     "Mặt bằng bàn giao xôi đỗ theo từng đoạn, nhà thầu không tổ chức được dây chuyền nên phát sinh "
     "yêu cầu thanh toán chi phí chờ việc. Hồ sơ chi trả thiếu chữ ký, đến khi quyết toán mới lộ ra "
     "và người dân đã chuyển đi."),

    ("Lựa chọn nhà thầu và ký hợp đồng",
     "Lập và phê duyệt kế hoạch lựa chọn nhà thầu; lập hồ sơ mời thầu; đánh giá; thẩm định và phê duyệt "
     "kết quả; thương thảo và ký hợp đồng.",
     "Người có thẩm quyền và chủ đầu tư theo Luật Đấu thầu",
     "Luật Đấu thầu 22/2023/QH15 (sửa bởi Luật 57/2024 và Luật 90/2025) · NĐ 214/2025 · "
     "với PPP: TT 98/2025/TT-BTC và TT 142/2025/TT-BTC",
     "Quyết định phê duyệt kết quả lựa chọn nhà thầu · hợp đồng kèm hình thức giá hợp đồng",
     "Hình thức giá ghi trong hợp đồng không khớp với cách các bên thực sự thanh toán — ký trọn gói "
     "nhưng thanh toán theo khối lượng thực tế, hoặc ngược lại. Đây là nguồn gốc của phần lớn tranh chấp "
     "ở khâu quyết toán."),

    ("Thi công, quản lý chi phí và điều chỉnh",
     "Thiết kế bước sau; lập, thẩm định và phê duyệt dự toán; thi công; nghiệm thu khối lượng theo "
     "giai đoạn; thanh toán; xử lý phát sinh và điều chỉnh.",
     "Chủ đầu tư với dự toán trong phạm vi được duyệt; người quyết định đầu tư với điều chỉnh dự án",
     "NĐ 206/2026 quản lý chi phí · NĐ 207/2026 quản lý chất lượng · TT 36/2026, TT 37/2026, TT 38/2026 "
     "về định mức và chi phí",
     "Dự toán được duyệt từng hạng mục · biên bản nghiệm thu khối lượng · bản vẽ hoàn công · "
     "hồ sơ thanh toán từng đợt",
     "Định mức là chỗ dễ sai nhất — cùng một công tác nhưng định mức mỗi thời kỳ một khác, phải lấy đúng "
     "bản có hiệu lực tại thời điểm lập dự toán. Công tác đặc thù như khoan hầm, hệ thống tín hiệu không "
     "có trong bộ định mức chung, phải lập và trình duyệt trước khi thi công."),

    ("Nghiệm thu, chạy thử và chứng nhận an toàn hệ thống",
     "Nghiệm thu hoàn thành từng hạng mục; thử nghiệm tĩnh và động; chạy thử liên động toàn hệ thống; "
     "đánh giá và chứng nhận an toàn hệ thống; nghiệm thu của cơ quan nhà nước; cấp phép khai thác.",
     "Chủ đầu tư nghiệm thu; cơ quan chuyên môn kiểm tra công tác nghiệm thu; cơ quan quản lý chuyên "
     "ngành cấp phép khai thác",
     "Luật Đường sắt 95/2025/QH15 (bản hợp nhất 75/VBHN-VPQH) · NĐ 16/2026 · "
     "TT 62/2026/TT-BXD quy chuẩn metro · VBHN 13/VBHN-BXD về kết nối ray với đường sắt quốc gia",
     "Biên bản nghiệm thu hoàn thành · hồ sơ chạy thử · chứng nhận an toàn hệ thống · "
     "quyết định đưa vào khai thác",
     "Đây là giai đoạn kéo dài ngoài dự kiến nhiều nhất. Chi phí điện, nhân công vận hành, bảo hiểm "
     "phát sinh khi công trình chưa bàn giao và chưa có doanh thu — thuộc chi phí đầu tư hay chi phí "
     "vận hành là câu phải trả lời trước, không phải sau."),

    ("Bàn giao, ghi nhận tài sản và đưa vào khai thác",
     "Bàn giao công trình và hồ sơ cho đơn vị khai thác; xác lập quyền sở hữu và giao quản lý tài sản "
     "kết cấu hạ tầng; lập hồ sơ tài sản, kê khai, tính hao mòn; xây dựng phương án giá vé và trợ giá.",
     "Cấp có thẩm quyền giao quản lý tài sản kết cấu hạ tầng; UBND và HĐND cấp tỉnh với giá vé, trợ giá",
     "NĐ 15/2025 về tài sản kết cấu hạ tầng đường sắt · TT 75/2025/TT-BTC về hao mòn · "
     "TT 34/2025 và TT 33/2025/TT-BXD · Luật Quản lý, sử dụng tài sản công 15/2017/QH14",
     "Biên bản bàn giao theo từng đơn vị tiếp nhận · danh mục và giá trị tài sản hình thành qua đầu tư",
     "Bàn giao trước, xác định giá trị sau — công trình đã chạy tàu nhưng giá trị tài sản chưa chốt, "
     "đơn vị khai thác ghi sổ theo giá tạm tính, quyết toán xong phải điều chỉnh lại toàn bộ."),

    ("Quyết toán vốn đầu tư dự án hoàn thành",
     "Khoá sổ và đối chiếu vốn đã thanh toán; lập báo cáo quyết toán; kiểm toán độc lập báo cáo quyết "
     "toán; thẩm tra; phê duyệt quyết toán; xử lý công nợ và vật tư thiết bị tồn đọng.",
     "Người có thẩm quyền phê duyệt quyết toán theo phân cấp; cơ quan tài chính chủ trì thẩm tra",
     "NĐ 254/2025 (thay NĐ 99/2021) · TT 147/2025/TT-BTC · TT 73/2026/TT-BTC hệ thống mẫu biểu · "
     "kiểm toán theo VSA 1000",
     "Báo cáo quyết toán · báo cáo kiểm toán độc lập · báo cáo thẩm tra · quyết định phê duyệt quyết toán",
     "Hồ sơ trải qua nhiều đời nghị định; người lập đã nghỉ việc; chứng từ giai đoạn đầu thất lạc. "
     "Chi phí không tính vào giá trị tài sản chưa được cấp thẩm quyền cho phép bằng văn bản thì bị treo."),
]

# ---------------------------------------------------------------- 12 bai hoc
BAI_HOC = [
    ("Dựng bản đồ hiệu lực văn bản của chính dự án, và cập nhật nó",
     "Ngay khi dự án được phê duyệt, lập một bảng: mỗi mốc thời gian của dự án ứng với những văn bản nào "
     "đang có hiệu lực. Mỗi lần có nghị định hay thông tư mới thay thế thì thêm một dòng. Bảng này mất "
     "khoảng hai ngày để dựng lần đầu và mười phút mỗi lần cập nhật. Không có nó thì đến lúc quyết toán "
     "phải mất hàng tháng dựng lại bằng trí nhớ của những người còn ở lại."),
    ("Khoá hình thức giá hợp đồng ngay từ hồ sơ mời thầu",
     "Mỗi gói thầu một hình thức giá. Gói ghép nhiều loại công việc thì tách phụ lục giá theo từng phần. "
     "Quan trọng nhất: cách thanh toán thực tế phải khớp với hình thức giá đã ghi. Đây là bài học đắt "
     "nhất — phần lớn thời gian tranh luận ở khâu thẩm tra quyết toán nằm đúng chỗ này."),
    ("Lập hồ sơ đồng thời với công việc, không dồn cuối kỳ",
     "Biên bản nghiệm thu ký cùng ngày nghiệm thu. Bản vẽ hoàn công lập ngay sau khi xong hạng mục. "
     "Nhật ký thi công ghi hằng ngày. Nghe hiển nhiên nhưng đây là điều bị vi phạm thường xuyên nhất, "
     "và là nguyên nhân trực tiếp của phần lớn khoản bị loại khi quyết toán."),
    ("Chụp ảnh và đo đạc phần sẽ bị che khuất, ngay lúc còn thấy được",
     "Với metro, phần ngầm chiếm tỷ trọng chi phí rất lớn và không đo lại được sau khi hoàn thành. "
     "Cốt thép trước khi đổ bê tông, hệ chống đỡ hầm trước khi lắp vỏ — mỗi hạng mục cần ảnh có gắn "
     "thời gian và vị trí, kèm biên bản có xác nhận các bên. Ảnh không có thời gian và vị trí thì giá trị "
     "chứng minh gần bằng không."),
    ("Đối chiếu vốn thanh toán với cơ quan thanh toán hằng năm",
     "Đây là bước hay bị bỏ sót nhất nhưng phát hiện nhiều chênh lệch nhất. Làm hằng năm, có biên bản "
     "ký hai bên. Chênh lệch phát hiện trong năm thì xử lý được; phát hiện sau tám năm thì phải truy lại "
     "toàn bộ chuỗi chứng từ."),
    ("Trình duyệt định mức cho công tác đặc thù trước khi thi công",
     "Khoan hầm bằng máy, lắp đặt hệ thống tín hiệu, cấp điện trên cao, thử nghiệm liên động — những công "
     "tác này không có trong bộ định mức xây dựng chung. Phải lập định mức mới và trình phê duyệt trước "
     "khi thực hiện. Làm trước rồi trình sau thì khoản chi phí đó sẽ bị treo."),
    ("Quyết định trước về chi phí giai đoạn chạy thử",
     "Trước khi bắt đầu chạy thử, trình phê duyệt một văn bản xác định phạm vi, thời gian, danh mục chi phí "
     "và nguồn chi trả. Mở mã theo dõi riêng trong kế toán. Việc này mất một tuần và tiết kiệm được "
     "nhiều tháng ở khâu quyết toán."),
    ("Phân bổ chi phí quản lý dự án theo nguyên tắc, không theo cảm tính",
     "Chi phí liên quan trực tiếp đến hạng mục nào thì phân bổ toàn bộ cho hạng mục đó; chi phí chung "
     "phân bổ theo tỷ lệ vốn. Xây dựng bảng phân bổ từ sớm và duy trì, đừng để đến lúc quyết toán mới "
     "ngồi chia — nhất là khi tài sản sẽ bàn giao cho nhiều đơn vị khác nhau."),
    ("Lập danh mục tài sản dự kiến hình thành ngay từ bước phê duyệt dự án",
     "Đừng đợi đến lúc bàn giao mới nghĩ tài sản này giao cho ai. Lập sớm bảng: hạng mục — loại tài sản — "
     "đơn vị dự kiến tiếp nhận — căn cứ pháp lý giao nhận. Bảng này sẽ được cập nhật nhiều lần, nhưng "
     "có nó từ đầu thì mọi lần cập nhật đều nhẹ."),
    ("Xử lý ngay kết luận thanh tra, kiểm tra, Kiểm toán Nhà nước và lưu vết",
     "Dự án lớn kéo dài gần như chắc chắn có ít nhất một cuộc thanh tra hoặc kiểm toán trong vòng đời. "
     "Với mỗi kết luận: lưu văn bản, lập bảng theo dõi từng nội dung, ghi rõ đã chấp hành thế nào và "
     "chứng từ ở đâu. Đến lúc quyết toán, bảng này là tài liệu được hỏi đến sớm nhất."),
    ("Giữ liên tục nhân sự nắm hồ sơ, không giữ được thì bàn giao có biên bản",
     "Vòng đời mười đến mười lăm năm dài hơn thời gian gắn bó trung bình của một cán bộ dự án. Mỗi lần "
     "thay người phụ trách, làm biên bản bàn giao theo danh mục hồ sơ chứ không bàn giao chung chung. "
     "Danh mục hồ sơ là tài sản của tổ chức, không phải của cá nhân."),
    ("Số hoá hồ sơ từ sớm, đặt tên tệp theo quy ước thống nhất",
     "Chứng từ giấy của những năm đầu sẽ mờ, sẽ thất lạc, sẽ bị ẩm. Quét và đặt tên có quy ước ngay khi "
     "phát sinh — gói thầu, loại chứng từ, ngày, số hiệu. Chi phí việc này rất nhỏ so với chi phí đi tìm "
     "lại một biên bản nghiệm thu của năm thứ hai vào năm thứ mười một."),
]

# ---------------------------------------------------------------- danh muc kiem tra
KIEM_TRA = [
    ("Ngay khi dự án được phê duyệt", [
        "Bản đồ hiệu lực văn bản pháp luật theo thời kỳ — đã lập, đã giao người cập nhật",
        "Xác định dự án thuộc ngăn nào trong bốn ngăn pháp lý, lưu văn bản chứng minh",
        "Bảng theo dõi tổng mức đầu tư theo thời kỳ — mở sổ dù chưa có lần điều chỉnh nào",
        "Danh mục tài sản dự kiến hình thành và đơn vị dự kiến tiếp nhận",
        "Quy ước đặt tên tệp và cấu trúc thư mục hồ sơ điện tử — ban hành bằng văn bản",
        "Bảng đối chiếu tiêu chuẩn, quy chuẩn áp dụng — lập và trình phê duyệt",
    ]),
    ("Trước khi phát hành hồ sơ mời thầu từng gói", [
        "Hình thức giá hợp đồng đã chốt, một hình thức cho một phần công việc",
        "Yêu cầu nhà thầu nộp bảng giá phân tích và bảng khối lượng cơ sở làm phụ lục hợp đồng",
        "Danh mục chuyển giao công nghệ có tiêu chí nghiệm thu và giá trị tương ứng",
        "Nghĩa vụ đào tạo gắn với mốc nghiệm thu, không thanh toán trọn gói trước",
        "Ngôn ngữ hợp đồng, trách nhiệm dịch thuật, tỷ giá quy đổi với nhà thầu nước ngoài",
    ]),
    ("Trong suốt quá trình thi công", [
        "Sổ theo dõi bàn giao mặt bằng theo mốc lý trình và theo ngày, xác nhận ba bên",
        "Định mức cho công tác đặc thù đã trình duyệt trước khi thi công",
        "Ảnh và số liệu đo phần sẽ bị che khuất — có thời gian, vị trí, biên bản",
        "Biên bản đối chiếu vốn thanh toán với cơ quan thanh toán — hằng năm",
        "Bảng phân bổ chi phí quản lý dự án và chi phí tư vấn — cập nhật định kỳ",
        "Mỗi lần gia hạn tiến độ đều có phụ lục hợp đồng, không chỉ có công văn",
        "Bảng theo dõi việc chấp hành từng kết luận thanh tra, kiểm tra, kiểm toán",
    ]),
    ("Trước khi chạy thử", [
        "Văn bản phê duyệt phạm vi, thời gian, danh mục chi phí và nguồn chi trả",
        "Mã theo dõi riêng cho chi phí chạy thử trong hệ thống kế toán",
        "Hồ sơ đánh giá, chứng nhận an toàn hệ thống — có dự toán riêng và hợp đồng riêng",
        "Hồ sơ hoàn công phần thiết bị đã có bản tiếng Việt",
    ]),
    ("Trước khi bàn giao", [
        "Danh mục và giá trị tài sản bàn giao theo từng đơn vị tiếp nhận",
        "Phân loại tài sản dài hạn và tài sản ngắn hạn",
        "Tài sản của Ban Quản lý dự án: đối chiếu sổ kế toán với kiểm kê, xác định giá trị còn lại",
        "Vật tư, thiết bị tồn đọng: đối chiếu sổ kế toán với kiểm kê, có phương án xử lý",
        "Công nợ phải thu, phải trả xác định đúng đối tượng, có kiến nghị biện pháp xử lý",
    ]),
]

# ---------------------------------------------------------------- ba sai lam
SAI_LAM = [
    ("Coi quyết toán là việc của kế toán",
     "Quyết toán vốn đầu tư dự án hoàn thành là công việc của cả Ban Quản lý dự án: phòng kỹ thuật giữ "
     "khối lượng và hồ sơ nghiệm thu, phòng hợp đồng giữ điều khoản giá, phòng kế hoạch giữ tổng mức "
     "đầu tư, phòng kế toán giữ chứng từ. Giao trọn cho kế toán thì kế toán chỉ tổng hợp được những gì "
     "được đưa cho, và những gì không được đưa cho sẽ thành khoản thiếu hồ sơ."),
    ("Áp văn bản hiện hành cho khối lượng đã thực hiện nhiều năm trước",
     "Chi phí phát sinh năm 2022 thì áp văn bản có hiệu lực năm 2022, không áp văn bản năm 2026. "
     "Định mức của công tác nghiệm thu năm 2023 thì lấy bản định mức hiệu lực năm 2023. Đây là lỗi "
     "căn cứ, và bên thẩm tra có quyền bác."),
    ("Dùng cơ chế đặc thù mà không chứng minh được phạm vi áp dụng",
     "Cơ chế đặc thù rút ngắn được nhiều bước, nhưng chỉ khi dự án thuộc đúng phạm vi và đúng thời kỳ "
     "hiệu lực. Hồ sơ phải có văn bản chứng minh: dự án thuộc phạm vi NQ 188/2025, phần việc nào phát "
     "sinh sau ngày Nghị quyết có hiệu lực, bước nào được rút gọn theo điều khoản nào. Viện dẫn "
     "“theo cơ chế đặc thù” chung chung mà không dẫn được điều khoản là không đủ."),
]

# ---------------------------------------------------------------- 10 vuong mac
VUONG_MAC = [
    ("Giải phóng mặt bằng và tái định cư",
     "Mặt bằng bàn giao theo từng đoạn ngắn, không liền tuyến. Nhà thầu nhận đoạn A thì đoạn B chưa xong, "
     "máy móc và nhân lực nằm chờ, sau đó gửi yêu cầu thanh toán chi phí chờ việc và đề nghị gia hạn.",
     "Metro chạy qua khu vực đô thị đã ổn định, mật độ dân cư và hạ tầng kỹ thuật dày. Phương án bồi thường "
     "lập trên hồ sơ địa chính nhưng hiện trạng thực tế đã khác. Chi phí được duyệt tại một thời điểm "
     "nhưng chi trả kéo dài nhiều năm.",
     "Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · NĐ 226/2025 · "
     "Hà Nội tại khu vực TOD: NQ 66/2026/NQ-HĐND Điều 11",
     "Lập sổ theo dõi bàn giao mặt bằng theo mốc lý trình và theo ngày, xác nhận ba bên — đây là bằng chứng "
     "gốc quyết định chi phí chờ việc có được quyết toán hay không. Mỗi lần gia hạn làm phụ lục hợp đồng, "
     "không để bằng công văn. Đối chiếu danh sách chi trả với chứng từ thực tế hằng quý."),

    ("Điều chỉnh tổng mức đầu tư nhiều lần",
     "Tổng mức đầu tư ban đầu được duyệt ở một mức, sau vài năm chi phí thực tế vượt xa. Trong thời gian "
     "chờ phê duyệt điều chỉnh, dự án vẫn thi công và thanh toán. Đến khi quyết toán, một phần khối lượng "
     "đã vượt tổng mức đầu tư đang có hiệu lực tại thời điểm thực hiện.",
     "Bốn nguyên nhân thường cộng dồn: sơ bộ tổng mức đầu tư lập trên khảo sát mỏng; trượt giá qua vòng đời "
     "tám đến mười lăm năm; thay đổi thiết kế do địa chất phần ngầm khác dự kiến; chi phí giải phóng mặt bằng "
     "tăng theo giá đất.",
     "Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (sửa bởi NĐ 275/2025) · NĐ 206/2026 về quản lý chi phí · "
     "NĐ 19/2026 về thẩm định và giám sát đầu tư",
     "Chi phí đề nghị quyết toán phải nằm trong phạm vi tổng mức đầu tư đã phê duyệt — phần vượt chưa được "
     "phê duyệt điều chỉnh thì không có căn cứ đưa vào giá trị quyết toán, dù đã thi công và nghiệm thu xong. "
     "Lập bảng theo dõi tổng mức đầu tư theo thời kỳ; trình điều chỉnh trước khi thực hiện phần vượt."),

    ("Hợp đồng EPC và nhà thầu nước ngoài",
     "Gói EPC ký theo mẫu hợp đồng quốc tế, giá trọn gói bằng ngoại tệ, thanh toán theo mốc. Khi quyết toán, "
     "chủ đầu tư không có bảng khối lượng chi tiết để đối chiếu; cơ quan thẩm tra yêu cầu bóc tách, "
     "nhà thầu từ chối vì hợp đồng trọn gói.",
     "Hợp đồng quốc tế và pháp luật quyết toán trong nước dựa trên hai logic khác nhau. Hợp đồng quốc tế coi "
     "trọn gói là chuyển rủi ro khối lượng cho nhà thầu; hồ sơ quyết toán vốn nhà nước lại đòi bằng chứng "
     "khối lượng thực hiện.",
     "NĐ 37/2015 sửa bởi NĐ 50/2021 (bản hợp nhất 07/VBHN-BXD) · Luật Xây dựng 135/2025/QH15 · "
     "Luật Đấu thầu 22/2023/QH15 · VBHN 34/VBHN-BXD · NĐ 04/2026 về công nghiệp đường sắt",
     "Khoá hình thức giá ngay từ hồ sơ mời thầu; gói EPC ghép nhiều loại công việc thì tách phụ lục giá theo "
     "từng phần. Yêu cầu nhà thầu nộp bảng giá phân tích và bảng khối lượng cơ sở làm phụ lục hợp đồng, kể cả "
     "khi giá trọn gói. Quy định rõ ngôn ngữ hợp đồng, trách nhiệm dịch thuật và tỷ giá quy đổi."),

    ("Chi phí giai đoạn chạy thử khi chưa khai thác",
     "Chạy thử kéo dài nhiều tháng, có khi hơn một năm. Phát sinh tiền điện chạy tàu, lương nhân sự vận hành, "
     "bảo hiểm, chi phí chuyên gia nước ngoài. Công trình chưa bàn giao, chưa có doanh thu. Khoản này là "
     "chi phí đầu tư hay chi phí vận hành?",
     "Ranh giới giữa kết thúc đầu tư và bắt đầu khai thác của metro không phải một điểm mà là một khoảng. "
     "Chạy thử vừa là bước nghiệm thu vừa là hoạt động vận hành. Pháp luật xây dựng và pháp luật tài sản công "
     "không nối liền ở đúng chỗ này.",
     "NĐ 207/2026 và TT 32/2026/TT-BXD · TT 62/2026/TT-BXD quy chuẩn metro · NĐ 16/2026 · "
     "NĐ 15/2025 về tài sản kết cấu hạ tầng · TT 79/2026/TT-BTC",
     "Quyết định trước khi chạy thử, không phải sau: trình phê duyệt văn bản xác định phạm vi, thời gian, "
     "danh mục chi phí và nguồn chi trả. Mở mã theo dõi riêng trong kế toán. Coi hồ sơ chứng nhận an toàn "
     "hệ thống là một hạng mục hợp đồng độc lập có dự toán riêng."),

    ("Áp dụng tiêu chuẩn, quy chuẩn nước ngoài",
     "Thiết kế và thiết bị theo hệ tiêu chuẩn của nước cung cấp công nghệ. Đến khi nghiệm thu và quyết toán, "
     "cơ quan trong nước yêu cầu đối chiếu với quy chuẩn Việt Nam, nhiều chỉ tiêu không có hoặc khác cách đo.",
     "Việt Nam chỉ có quy chuẩn riêng cho đường sắt đô thị loại hình metro từ TT 62/2026/TT-BXD ngày 30/7/2026. "
     "Các tuyến khởi động trước mốc này buộc phải mượn tiêu chuẩn nước ngoài, và mỗi tuyến dùng công nghệ của "
     "một nước khác nhau.",
     "Hà Nội: NQ 40/2025/NQ-HĐND — lưu ý khoản 2 Điều 1 nói rõ đường sắt đô thị đi theo đường riêng, "
     "KHÔNG theo trình tự chung của Nghị quyết này · TT 62/2026/TT-BXD · TT 44/2025/TT-BXD",
     "Lập bảng đối chiếu tiêu chuẩn ngay ở bước thiết kế và trình phê duyệt, không để là tài liệu nội bộ của "
     "tư vấn. Với dự án Hà Nội, không viện dẫn NQ 40/2025 làm căn cứ cho đường sắt đô thị — chính nghị quyết "
     "đó đã loại trừ; phải dẫn Luật Thủ đô 02/2026/QH16 và NQ 188/2025/QH15."),

    ("Quyết toán dự án kéo dài nhiều năm",
     "Dự án trải qua nhiều đời nghị định về quản lý chi phí, quản lý dự án và quyết toán, cùng nhiều lần sửa "
     "thông tư định mức. Người lập hồ sơ đã nghỉ việc, chứng từ giai đoạn đầu lưu ở kho và một phần đã mờ.",
     "Đây là bản chất của loại dự án có vòng đời tám đến mười lăm năm. Không có cách nào tránh, chỉ có cách "
     "quản lý.",
     "Chuỗi thay thế cần nắm — quản lý dự án: NĐ 59/2015 → NĐ 15/2021 → NĐ 175/2024 → NĐ 209/2026 và NĐ 210/2026. "
     "Quản lý chi phí: NĐ 32/2015 → NĐ 68/2019 → NĐ 10/2021 → NĐ 206/2026. "
     "Quyết toán: TT 09/2016 → TT 10/2020 → NĐ 99/2021 → NĐ 254/2025",
     "Việc đầu tiên là dựng bản đồ hiệu lực văn bản theo thời kỳ của chính dự án, gán mỗi mốc vào một đời "
     "văn bản. Kết luận không dẫn được số hiệu văn bản của đúng thời kỳ là kết luận không đứng vững. "
     "Đối chiếu vốn thanh toán với cơ quan thanh toán hằng năm, không đợi đến cuối."),

    ("TOD và khai thác giá trị tăng thêm từ đất",
     "Chính sách cho phép Thành phố thu phần giá trị đất tăng thêm quanh nhà ga để bù đắp chi phí đầu tư tuyến. "
     "Nhưng khi triển khai, cơ quan thực hiện không tính ra được số tiền phải thu.",
     "Cơ chế đã đủ ở tầng Luật và Nghị quyết Hội đồng nhân dân, nhưng thiếu văn bản định lượng ở tầng dưới cùng. "
     "Thêm một lệch pha nữa: quy hoạch TOD phải được duyệt trước, mà quy hoạch TOD lại phụ thuộc vào hướng tuyến "
     "và vị trí ga đã chốt — trong khi tuyến vẫn đang điều chỉnh thiết kế.",
     "Luật Thủ đô 02/2026/QH16 Điều 12 · NQ 188/2025/QH15 · Hà Nội: NQ 71/2025, NQ 66/2026, NQ 67/2026 · "
     "TP.HCM: NQ 21/2026 (thay NQ 38/2025 từ 19/6/2026), NQ 90/2025",
     "Xác định ranh giới sổ sách giữa dự án tuyến và dự án TOD ngay từ đầu. Với Hà Nội, theo dõi Công báo "
     "để bắt Nghị quyết về Hệ số lợi thế TOD ngay khi ban hành — trước khi có văn bản đó, mọi con số về "
     "khoản thu TOD chỉ là ước tính nội bộ, không đưa vào phương án tài chính chính thức."),

    ("Không gian ngầm",
     "Ga ngầm và đoạn hầm nằm dưới đất của nhiều chủ sử dụng khác nhau. Thu hồi đất đến độ sâu nào, bồi thường "
     "phần ngầm ra sao, đơn giá thuê đất cho công trình ngầm là bao nhiêu, phần thương mại trong ga ngầm được "
     "khai thác đến mức nào.",
     "Pháp luật đất đai truyền thống quản lý theo thửa đất trên bề mặt. Không gian ngầm là lớp quản lý mới, "
     "vừa được đặt nền ở tầng Luật Thủ đô và các nghị quyết Hội đồng nhân dân Hà Nội năm 2026.",
     "Luật Thủ đô 02/2026/QH16 Điều 11 · Hà Nội: NQ 64/2026 (quy hoạch không gian ngầm), NQ 65/2026 "
     "(các khoản thu), NQ 62/2026 (ưu đãi đầu tư)",
     "Xác định và ghi rõ cao độ đáy công trình của từng ga, từng đoạn hầm ngay trong hồ sơ thiết kế và hoàn công "
     "— mốc mười lăm mét quyết định trực tiếp nghĩa vụ tài chính. Tách rõ diện tích sàn ngầm phục vụ vận hành "
     "và diện tích khai thác thương mại, vì hai loại có chế độ tài chính khác nhau."),

    ("Đào tạo nhân lực vận hành",
     "Chi phí đào tạo lái tàu, điều độ, bảo trì được tính vào tổng mức đầu tư. Đến khi quyết toán, câu hỏi đặt ra: "
     "khoản này có tạo nên tài sản không? Nếu không thì xử lý thế nào?",
     "Đào tạo là chi phí đầu tư về mặt kinh tế nhưng không hình thành tài sản cố định về mặt kế toán. Người được "
     "đào tạo có thể nghỉ việc trước khi tuyến vận hành, làm phát sinh câu hỏi về hiệu quả sử dụng vốn.",
     "NQ 188/2025/QH15 nhóm cơ chế về chuyển giao công nghệ và đào tạo nhân lực · "
     "QĐ 2230/QĐ-TTg đề án đào tạo nhân lực đường sắt đến 2035 · NĐ 254/2025",
     "Xác định ngay từ bước lập dự án: chi phí đào tạo thuộc khoản mục nào và có tính vào giá trị tài sản không. "
     "Nếu không tính thì phải trình cấp có thẩm quyền cho phép — đây là thủ tục riêng, chủ đầu tư không tự quyết "
     "được. Lưu đủ bằng chứng vì đây là loại chi phí không có sản phẩm vật chất."),

    ("Chuyển giao công nghệ và nội địa hoá",
     "Hợp đồng có điều khoản chuyển giao công nghệ nhưng mô tả chung chung, không có danh mục cụ thể, không có "
     "tiêu chí nghiệm thu, không có mốc thanh toán riêng. Đến khi quyết toán, không ai xác định được điều khoản "
     "đó đã hoàn thành hay chưa và giá trị bao nhiêu trong tổng giá hợp đồng.",
     "Chuyển giao công nghệ là loại nghĩa vụ khó lượng hoá. Bên bán có động cơ giữ lại phần lõi. Bên mua thường "
     "chưa đủ năng lực kỹ thuật để định nghĩa chính xác mình cần nhận cái gì tại thời điểm ký hợp đồng.",
     "NQ 188/2025/QH15 · NĐ 04/2026 về giao nhiệm vụ, đặt hàng công nghiệp đường sắt · "
     "QĐ 498/QĐ-TTg cơ cấu lại Tổng công ty Đường sắt Việt Nam · Luật Chuyển giao công nghệ 07/2017/QH14",
     "Lập danh mục chuyển giao dạng bảng ngay trong hồ sơ mời thầu: nội dung — hình thức — tiêu chí nghiệm thu — "
     "mốc thời gian — giá trị tương ứng. Không có cột giá trị thì không quyết toán được. Tách thành hạng mục "
     "thanh toán riêng, giữ lại tỷ lệ cuối cùng đến khi nghiệm thu đủ danh mục."),
]

# ---------------------------------------------------------------- cho ho phap ly
CHO_HO = [
    ("Hệ số lợi thế TOD của Hà Nội — chưa ban hành",
     "NQ 67/2026/NQ-HĐND Điều 8 giao Uỷ ban nhân dân trình Hội đồng nhân dân quy định Hệ số lợi thế TOD và "
     "các tỷ lệ phần trăm, sau khi quy hoạch khu vực TOD được duyệt. Nghị quyết đó chưa ban hành. "
     "Chưa có nó thì bốn khoản thu TOD chưa quy ra tiền được."),
    ("Phí kết nối không gian ngầm của Hà Nội — chưa ban hành",
     "NQ 65/2026/NQ-HĐND Điều 3 khoản 2 giao trình mức thu phí kết nối không gian ngầm sau khi quy hoạch "
     "không gian ngầm được duyệt. Chưa có văn bản này thì chưa xác định được nghĩa vụ phí kết nối của các "
     "công trình lân cận đấu nối vào ga ngầm."),
    ("Nghị định quy định chi tiết Luật Thủ đô 02/2026 — chưa tìm thấy",
     "QĐ 762/QĐ-TTg là kế hoạch triển khai Luật Thủ đô 39/2024, ban hành trước khi có luật mới. "
     "Chưa tìm thấy quyết định thay thế cho Luật 02/2026, và cũng chưa tìm thấy nghị định quy định chi tiết."),
]
