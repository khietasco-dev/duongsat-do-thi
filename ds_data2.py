# -*- coding: utf-8 -*-
"""Noi dung hai muc moi:
   1. Kiem toan Bao cao quyet toan du an hoan thanh — va KIEM TOAN SONG HANH
   2. Thu vien rui ro kiem toan du an (tham khao chung, khong tu don vi nao)
"""

# =====================================================================
# 1. KIEM TOAN BAO CAO QUYET TOAN DU AN HOAN THANH
# =====================================================================

# Vi sao du an lon phai kiem toan song hanh
VI_SAO_SONG_HANH = [
    ("Hồ sơ của giai đoạn đầu không còn nguyên vẹn",
     "Một tuyến metro kéo dài tám đến mười lăm năm. Đợi công trình xong mới bắt đầu kiểm toán thì "
     "chứng từ những năm đầu đã mờ, người ký đã chuyển công tác, nhà thầu phụ đã giải thể. "
     "Kiểm toán viên không tìm được bằng chứng, mà không có bằng chứng thì không đưa ra ý kiến được."),
    ("Khối lượng phần ngầm đã bị che khuất",
     "Cốt thép trước khi đổ bê tông, hệ chống đỡ hầm trước khi lắp vỏ — những thứ này chỉ nhìn được "
     "đúng một lần, tại đúng thời điểm thi công. Sau đó dù có muốn cũng không đo lại được. "
     "Kiểm toán viên đến sau chỉ còn cách tin vào hồ sơ người khác lập."),
    ("Sai sót phát hiện muộn thì không sửa được nữa",
     "Một khoản chi phí thiếu quyết định của cấp có thẩm quyền, nếu phát hiện ngay trong năm phát sinh "
     "thì xin bổ sung được. Phát hiện sau bảy năm thì người có thẩm quyền lúc đó đã nghỉ hưu, và người "
     "đương nhiệm không dám ký cho việc mình không chứng kiến."),
    ("Khối lượng công việc dồn vào cuối làm kéo dài quyết toán",
     "Một dự án nhiều nghìn tỷ có hàng chục nghìn chứng từ. Dồn hết vào một đợt kiểm toán cuối thì "
     "riêng khâu sắp xếp hồ sơ đã mất nhiều tháng, chưa nói tới kiểm tra. Chia theo giai đoạn thì mỗi "
     "đợt gọn, và đợt sau kế thừa được kết quả đợt trước."),
    ("Chủ đầu tư biết mình sai ở đâu khi còn kịp sửa",
     "Đây là giá trị lớn nhất. Kiểm toán song hành không chỉ để phát hiện, mà để chủ đầu tư điều chỉnh "
     "cách lập hồ sơ ngay từ gói thầu tiếp theo. Một lưu ý ở năm thứ hai tiết kiệm được nhiều tháng "
     "ở năm thứ mười."),
]

# So sanh hai cach lam
SO_SANH = [
    ("Thời điểm bắt đầu", "Sau khi công trình hoàn thành", "Ngay từ giai đoạn thi công, theo từng đợt"),
    ("Cách chia công việc", "Một đợt duy nhất, toàn bộ dự án",
     "Nhiều đợt theo giai đoạn hoặc theo gói thầu, đợt cuối tổng hợp"),
    ("Bằng chứng kiểm toán", "Chỉ còn hồ sơ giấy, phần khuất không kiểm tra được",
     "Chứng kiến trực tiếp phần sẽ bị che khuất, kiểm kê tại hiện trường"),
    ("Khi phát hiện sai sót", "Thường đã quá muộn để bổ sung hồ sơ",
     "Còn thời gian để chủ đầu tư hoàn thiện hoặc xin ý kiến cấp có thẩm quyền"),
    ("Thời gian quyết toán", "Kéo dài, vì phải dựng lại hồ sơ nhiều năm trước",
     "Ngắn hơn, vì phần lớn đã được kiểm tra và thống nhất từ trước"),
    ("Chi phí kiểm toán", "Thấp hơn trên một hợp đồng, nhưng rủi ro treo hồ sơ cao",
     "Cao hơn tổng cộng, đổi lại giảm rủi ro và rút ngắn quyết toán"),
    ("Phù hợp với", "Dự án nhỏ, thời gian thực hiện dưới hai năm",
     "Dự án nhóm A, dự án quan trọng quốc gia, dự án nhiều gói thầu, dự án ODA"),
]

# Chin phan hanh theo Ho so kiem toan mau VACPA
PHAN_HANH = [
    ("1000", "Lập kế hoạch kiểm toán",
     "Chấp nhận khách hàng và đánh giá rủi ro hợp đồng · tìm hiểu dự án và kiểm soát nội bộ · "
     "phân tích sơ bộ báo cáo quyết toán · xác định mức trọng yếu và phương pháp chọn mẫu · "
     "kế hoạch kiểm toán tổng thể và danh mục tài liệu cần cung cấp.",
     "Mức trọng yếu đặt sai thì toàn bộ cỡ mẫu phía sau sai theo."),
    ("3000", "Hồ sơ pháp lý dự án",
     "Đối chiếu danh mục hồ sơ pháp lý với quy định · kiểm tra thẩm quyền phê duyệt · đánh giá việc chấp "
     "hành trình tự đầu tư xây dựng, trình tự lựa chọn nhà thầu và việc ký kết hợp đồng.",
     "Với dự án áp cơ chế đặc thù, phải chứng minh được dự án thuộc phạm vi áp dụng trước khi chấp nhận "
     "các bước đã rút gọn."),
    ("4000", "Nguồn vốn đầu tư",
     "Kiểm tra số dư và biến động từng loại nguồn vốn · đối chiếu vốn thanh toán giữa chủ đầu tư và cơ quan "
     "thanh toán · kiểm tra việc điều chỉnh tăng giảm vốn và cách hạch toán.",
     "Đây là khâu hay phát hiện chênh lệch nhất, và cũng là khâu dễ làm nhất nếu đối chiếu hằng năm."),
    ("5100", "Chi phí bồi thường, hỗ trợ và tái định cư",
     "Đối chiếu với phương án bồi thường được duyệt · kiểm tra tới quyết định đền bù của cấp có thẩm quyền · "
     "bảng tổng hợp thanh toán · chứng từ chi trả và xác nhận của người nhận tiền.",
     "Hồ sơ chi trả thiếu chữ ký thì gần như không bổ sung được vì người dân đã chuyển đi."),
    ("5200", "Chi phí xây dựng",
     "Đối chiếu quyết toán A–B với báo cáo quyết toán · kiểm tra khối lượng và đơn giá theo đúng hình thức "
     "giá hợp đồng · đối chiếu biên bản nghiệm thu và hồ sơ quản lý chất lượng · kiểm tra quyết toán phát sinh.",
     "Phần hành lớn nhất. Áp nhầm cách kiểm của hình thức giá này sang hình thức giá khác là lỗi phổ biến nhất."),
    ("5300", "Chi phí thiết bị",
     "Đối chiếu quyết toán hợp đồng · kiểm tra danh mục, chủng loại, nguồn gốc xuất xứ, chất lượng và "
     "cấu hình thiết bị so với dự toán và hợp đồng · kiểm tra quyết toán phát sinh.",
     "Với metro, thiết bị chiếm tỷ trọng rất lớn và phần lớn nhập khẩu — phải kiểm cả tỷ giá quy đổi."),
    ("5400", "Vật tư, thiết bị do chủ đầu tư cung cấp",
     "Tổng hợp nhập xuất tồn kho · kiểm tra phần nhập gồm khối lượng, chứng chỉ xuất xứ chất lượng, đơn giá · "
     "kiểm tra phần xuất lắp đặt vào công trình theo từng nhà thầu.",
     "Chênh lệch nhập xuất tồn không giải thích được là dấu hiệu cần mở rộng phạm vi kiểm tra."),
    ("5500", "Chi phí quản lý dự án, tư vấn và chi phí khác",
     "Đối chiếu với tổng dự toán được duyệt · kiểm tra chi phí do chủ đầu tư tự thực hiện gồm mua sắm và "
     "chi phí lương của Ban Quản lý dự án · kiểm tra chi phí do các nhà thầu tư vấn thực hiện.",
     "Phải tính lại theo định mức có hiệu lực tại thời điểm áp dụng, không lấy định mức hiện hành."),
    ("6000", "Chi phí không tính vào giá trị tài sản",
     "Hai nhóm: thiệt hại do nguyên nhân bất khả kháng được phép không tính, và chi phí không tạo nên tài sản. "
     "Kiểm tra nội dung, giá trị thiệt hại so với quyết định của cấp có thẩm quyền, thẩm quyền của cấp cho phép, "
     "biên bản xác nhận và mức bồi thường bảo hiểm.",
     "Không có quyết định cho phép thì khoản đó bị treo, không quyết toán được."),
    ("7000", "Giá trị tài sản hình thành qua đầu tư",
     "Tổng hợp tài sản dài hạn và ngắn hạn · chính sách phân bổ chi phí chung · phân loại theo nguồn vốn và "
     "đối tượng sử dụng · quyết định điều chuyển và biên bản bàn giao · giá trị còn lại của tài sản Ban Quản lý dự án.",
     "Với metro, tài sản bàn giao cho nhiều đơn vị khác nhau nên danh mục phải chia rõ ngay từ đầu."),
    ("8000", "Công nợ và vật tư thiết bị tồn đọng",
     "Kiểm tra số dư nợ phải thu và phải trả theo từng nhà thầu · xác nhận số dư bằng thư xác nhận dưới sự "
     "kiểm soát của kiểm toán viên · kiểm tra tiền mặt và tiền gửi · kiểm tra nhập xuất tồn vật tư thiết bị "
     "tồn đọng và kiến nghị phương án xử lý.",
     "Thư xác nhận phải do kiểm toán viên kiểm soát khâu gửi và nhận, không để chủ đầu tư tự làm."),
    ("9000", "Tình hình chấp hành của chủ đầu tư",
     "Xem xét việc chấp hành quy định về quản lý đầu tư và xây dựng · chấp hành chế độ kế toán và quyết toán · "
     "và việc thực hiện kết luận của các cơ quan thanh tra, kiểm tra, Kiểm toán Nhà nước.",
     "Dự án lớn gần như chắc chắn đã qua ít nhất một cuộc thanh tra — bỏ qua phần này thì báo cáo sẽ mâu thuẫn "
     "với kết luận của cơ quan nhà nước."),
    ("2000", "Tổng hợp, soát xét và phát hành",
     "Tổng hợp kết quả kiểm toán và kiểm tra cân đối số liệu · tổng hợp đề nghị điều chỉnh · liệt kê các vấn đề "
     "chưa thống nhất · cam kết của chủ đầu tư · biên bản họp với khách hàng · soát xét các cấp · phê duyệt "
     "và phát hành báo cáo kiểm toán độc lập kèm thư quản lý.",
     "Trước khi phát hành phải chạy phương trình cân đối — không cân thì chưa được phát hành."),
]

# Phuong trinh can doi
CAN_DOI = [
    ("Cân đối tổng nguồn vốn và chi phí",
     "Tổng nguồn vốn đầu tư (4000) ≈ Tổng chi phí đầu tư đề nghị quyết toán (5000)",
     "Hai vế lệch nhau nghĩa là có nguồn vốn chưa được ghi nhận, hoặc có chi phí chưa có nguồn."),
    ("Cân đối chi phí và giá trị tài sản",
     "Chi phí đầu tư (5000) − Không tính vào giá trị tài sản (6000) − Vật tư thiết bị tồn đọng (8200) "
     "= Giá trị tài sản hình thành (7000)",
     "Đây là phép kiểm cuối cùng trước khi phát hành. Lệch một đồng cũng phải truy ra nguyên nhân."),
]

# Ba dieu khong lam
KHONG_LAM = [
    ("Không kiểm toán khi đang đồng thời là đơn vị tư vấn cho chính dự án đó",
     "Vừa lập hồ sơ vừa kiểm tra hồ sơ mình lập là mất tính độc lập. Đây là điều cấm, không có biện pháp "
     "bảo vệ nào chữa được."),
    ("Không thay chủ đầu tư lập hồ sơ",
     "Kiểm toán viên chỉ ra hồ sơ còn thiếu gì, nhưng người lập và ký hồ sơ phải là chủ đầu tư. "
     "Làm thay là làm mất ranh giới trách nhiệm."),
    ("Không đưa ra ý kiến khi chưa đủ bằng chứng",
     "Thiếu bằng chứng thì nêu rõ là thiếu và nêu ảnh hưởng, chứ không suy đoán để có một con số cho đẹp "
     "báo cáo."),
]


# =====================================================================
# 2. THU VIEN RUI RO KIEM TOAN DU AN
# =====================================================================

RUI_RO = [
    ("Hồ sơ pháp lý", [
        ("Trình tự đầu tư bị đảo hoặc bỏ bước",
         "Ký hợp đồng trước khi có quyết định phê duyệt dự án; khởi công trước khi có giấy phép xây dựng.",
         "Đối chiếu ngày ký của từng văn bản theo trục thời gian, không chỉ kiểm tra có đủ văn bản hay không.",
         "cao"),
        ("Thẩm quyền phê duyệt không đúng cấp",
         "Người ký quyết định không thuộc cấp có thẩm quyền theo phân loại dự án hoặc theo hạn mức giá trị.",
         "Đối chiếu chức danh người ký với quy định phân cấp có hiệu lực tại thời điểm ký.",
         "cao"),
        ("Áp dụng cơ chế đặc thù không đúng phạm vi",
         "Vận dụng cơ chế rút gọn trình tự cho dự án hoặc địa bàn không thuộc phạm vi được thí điểm.",
         "Yêu cầu chủ đầu tư xuất trình văn bản chứng minh dự án thuộc phạm vi áp dụng.",
         "cao"),
        ("Hồ sơ lập sau, ghi lùi ngày",
         "Biên bản, quyết định lập muộn nhưng ghi ngày của thời điểm lẽ ra phải có.",
         "So sánh chất liệu và hình thức văn bản trong cùng bộ hồ sơ; đối chiếu với nhật ký thi công và "
         "chứng từ thanh toán cùng kỳ.",
         "trung"),
    ]),
    ("Nguồn vốn và thanh toán", [
        ("Chênh lệch giữa sổ chủ đầu tư và cơ quan thanh toán",
         "Số vốn đã thanh toán trên sổ kế toán khác số của Kho bạc hoặc ngân hàng phục vụ.",
         "Yêu cầu biên bản đối chiếu từng năm; truy nguyên nhân từng khoản lệch, không chấp nhận lệch tổng.",
         "cao"),
        ("Thanh toán vượt giá trị hợp đồng",
         "Tổng các đợt thanh toán lớn hơn giá hợp đồng cộng phụ lục hợp lệ.",
         "Cộng dồn toàn bộ đợt thanh toán và đối chiếu với giá hợp đồng sau điều chỉnh.",
         "cao"),
        ("Tạm ứng chưa thu hồi hết",
         "Khoản tạm ứng theo hợp đồng chưa được khấu trừ đủ khi công trình đã hoàn thành.",
         "Lập bảng theo dõi tạm ứng và thu hồi theo từng hợp đồng, đối chiếu với bảo lãnh tạm ứng.",
         "trung"),
        ("Chi phí phát sinh không có nguồn vốn bố trí",
         "Khối lượng đã thực hiện nhưng chưa được bố trí vốn trong kế hoạch đầu tư công.",
         "Đối chiếu chi phí đề nghị quyết toán với kế hoạch vốn được giao từng năm.",
         "trung"),
    ]),
    ("Khối lượng và đơn giá", [
        ("Khối lượng quyết toán vượt khối lượng nghiệm thu",
         "Bảng quyết toán ghi khối lượng lớn hơn biên bản nghiệm thu tương ứng.",
         "Đối chiếu ba chiều: bảng quyết toán — biên bản nghiệm thu — bản vẽ hoàn công.",
         "cao"),
        ("Trùng khối lượng giữa các gói thầu",
         "Cùng một hạng mục được tính ở hai gói thầu khác nhau, thường xảy ra ở phần giao nhau giữa hai gói.",
         "Dò trùng theo mã hiệu đơn giá và theo lý trình; đặc biệt chú ý ranh giới giữa các gói.",
         "cao"),
        ("Áp sai định mức theo thời kỳ",
         "Dùng định mức hiện hành cho khối lượng đã nghiệm thu nhiều năm trước.",
         "Xác định thời điểm áp dụng của từng công tác, tra định mức có hiệu lực tại đúng thời điểm đó.",
         "cao"),
        ("Công tác đặc thù chưa được duyệt định mức",
         "Khoan hầm, lắp đặt hệ thống tín hiệu, thử nghiệm liên động — không có trong bộ định mức chung.",
         "Yêu cầu quyết định phê duyệt định mức mới; không có thì khoản đó chưa đủ căn cứ quyết toán.",
         "cao"),
        ("Điều chỉnh giá không đúng hình thức giá hợp đồng",
         "Bù giá trượt giá cho hợp đồng trọn gói hoặc hợp đồng theo đơn giá cố định.",
         "Xác định hình thức giá ghi trong hợp đồng trước, rồi mới xét khoản điều chỉnh có được phép không.",
         "cao"),
        ("Chỉ số giá dùng để điều chỉnh không đúng nguồn",
         "Dùng chỉ số giá của địa phương khác, của loại công trình khác, hoặc của kỳ khác.",
         "Đối chiếu nguồn chỉ số giá với quy định trong hợp đồng và với văn bản công bố của cơ quan có thẩm quyền.",
         "trung"),
    ]),
    ("Hợp đồng", [
        ("Hình thức giá trong hợp đồng khác cách thanh toán thực tế",
         "Ký trọn gói nhưng thanh toán theo khối lượng thực tế, hoặc ngược lại.",
         "Đọc điều khoản giá và điều khoản thanh toán của hợp đồng trước khi kiểm bất kỳ con số nào.",
         "cao"),
        ("Phụ lục hợp đồng ký sau khi đã thi công xong",
         "Phụ lục điều chỉnh khối lượng hoặc giá ký sau thời điểm nghiệm thu phần việc đó.",
         "Đối chiếu ngày ký phụ lục với ngày nghiệm thu khối lượng tương ứng.",
         "cao"),
        ("Hợp đồng EPC không có bảng khối lượng chi tiết",
         "Hợp đồng theo mẫu quốc tế mô tả phạm vi theo kết quả đầu ra, không có bảng khối lượng để đối chiếu.",
         "Yêu cầu bảng giá phân tích và bảng khối lượng cơ sở; nếu không có thì nêu rõ hạn chế phạm vi.",
         "cao"),
        ("Giá sau điều chỉnh vượt giá gói thầu được duyệt",
         "Tổng giá hợp đồng cộng các phụ lục vượt giá gói thầu trong kế hoạch lựa chọn nhà thầu.",
         "Cộng dồn và đối chiếu với quyết định phê duyệt kế hoạch lựa chọn nhà thầu.",
         "trung"),
    ]),
    ("Chi phí quản lý dự án, tư vấn và chi phí khác", [
        ("Chi phí quản lý dự án vượt định mức",
         "Chi phí thực tế lớn hơn mức tính theo tỷ lệ định mức trên chi phí xây dựng và thiết bị.",
         "Tính lại theo định mức có nội suy giữa hai mốc quy mô; so với số chủ đầu tư đề nghị.",
         "trung"),
        ("Khoản đã nằm trong định mức nhưng vẫn tính riêng",
         "Chi phí văn phòng phẩm, điện nước của Ban Quản lý dự án tính thêm ngoài định mức.",
         "Đối chiếu danh mục chi phí đã bao gồm trong định mức với các khoản chi thực tế.",
         "trung"),
        ("Chi phí tư vấn vượt hợp đồng",
         "Giá trị quyết toán hợp đồng tư vấn lớn hơn giá hợp đồng và phụ lục.",
         "Đối chiếu từng hợp đồng tư vấn, kiểm tra sản phẩm bàn giao có đủ theo hợp đồng không.",
         "trung"),
    ]),
    ("Tài sản và bàn giao", [
        ("Giá trị tài sản không cân với chi phí đầu tư",
         "Phương trình cân đối không khớp: chi phí trừ khoản không tính vào tài sản trừ tồn đọng "
         "không bằng giá trị tài sản.",
         "Chạy phương trình cân đối trên cùng một bộ số; truy từng khoản lệch trước khi phát hành.",
         "cao"),
        ("Phân bổ chi phí chung không theo nguyên tắc",
         "Chi phí chung chia cho các hạng mục theo cảm tính thay vì theo tỷ lệ vốn.",
         "Kiểm tra bảng phân bổ, đối chiếu tiêu thức phân bổ với chính sách đã được phê duyệt.",
         "trung"),
        ("Tài sản bàn giao thiếu hoặc trùng giữa các đơn vị nhận",
         "Cùng một hạng mục xuất hiện ở hai biên bản bàn giao, hoặc không xuất hiện ở biên bản nào.",
         "Đối chiếu tổng danh mục tài sản với tổng các biên bản bàn giao.",
         "trung"),
        ("Chi phí không tính vào giá trị tài sản chưa được cho phép",
         "Khoản thiệt hại, khoản của hạng mục bị huỷ bỏ chưa có quyết định của cấp có thẩm quyền.",
         "Yêu cầu quyết định cho phép; không có thì khoản đó phải treo, không được kết chuyển.",
         "cao"),
    ]),
    ("Công nợ và tồn đọng", [
        ("Công nợ xác định không đúng đối tượng",
         "Số dư ghi theo tên gói thầu thay vì theo pháp nhân nhà thầu, hoặc gộp nhiều nhà thầu.",
         "Đối chiếu số dư theo từng pháp nhân; gửi thư xác nhận dưới sự kiểm soát của kiểm toán viên.",
         "trung"),
        ("Thư xác nhận do chủ đầu tư tự gửi và tự nhận",
         "Kiểm toán viên không kiểm soát khâu gửi và nhận nên bằng chứng mất độ tin cậy.",
         "Kiểm toán viên trực tiếp kiểm soát địa chỉ gửi và nhận thư phản hồi.",
         "cao"),
        ("Vật tư thiết bị tồn đọng chưa có phương án xử lý",
         "Vật tư còn trong kho sau khi công trình hoàn thành nhưng chưa xác định xử lý thế nào.",
         "Kiểm kê thực tế đối chiếu sổ sách; kiến nghị phương án xử lý trong báo cáo.",
         "thap"),
    ]),
    ("Rủi ro riêng của dự án đường sắt đô thị", [
        ("Chi phí giai đoạn chạy thử phân loại sai",
         "Tiền điện, lương nhân sự vận hành, bảo hiểm trong thời gian chạy thử tính vào chi phí đầu tư "
         "mà chưa có căn cứ.",
         "Yêu cầu văn bản phê duyệt phạm vi và nguồn chi trả cho giai đoạn chạy thử được lập trước khi chạy thử.",
         "cao"),
        ("Chi phí đánh giá an toàn hệ thống chưa nằm trong tổng mức đầu tư",
         "Hạng mục do tổ chức độc lập nước ngoài thực hiện, thường bị bỏ sót khi lập dự án.",
         "Đối chiếu hợp đồng đánh giá an toàn với tổng mức đầu tư được duyệt.",
         "trung"),
        ("Chênh lệch tỷ giá của phần vốn vay và thiết bị nhập khẩu",
         "Tỷ giá áp dụng cho từng loại giao dịch không nhất quán hoặc không đúng thời điểm.",
         "Kiểm tra riêng khoản chênh lệch tỷ giá; đối chiếu tỷ giá áp dụng với quy định trong hợp đồng.",
         "cao"),
        ("Chi phí đào tạo và chuyển giao công nghệ không rõ có tạo tài sản không",
         "Khoản lớn nhưng không hình thành tài sản cố định, dễ bị treo khi quyết toán.",
         "Yêu cầu quyết định của cấp có thẩm quyền về việc có tính vào giá trị tài sản hay không.",
         "trung"),
        ("Ranh giới chi phí giữa phần tuyến và khu vực TOD không rõ",
         "Dòng tiền và tài sản của hai phần trộn vào nhau, đến khi bàn giao không tách được.",
         "Kiểm tra chính sách tách bạch chi phí có được lập từ giai đoạn lập dự án hay không.",
         "trung"),
    ]),
]
