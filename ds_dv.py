# -*- coding: utf-8 -*-
"""Noi dung 9 DICH VU TU VAN ma ASCO co the cung cap cho du an duong sat do thi.

Pham vi da doi chieu voi Luat Kiem toan doc lap (ban hop nhat 17/VBHN-VPQH) Dieu 40:
  - khoan 1: dich vu kiem toan, soat xet, bao dam khac — lam ngay
  - khoan 2: TU VAN kinh te/tai chinh/thue · tu van quan ly, tai co cau · tu van CNTT
             · ke toan · tham dinh gia · boi duong kien thuc — PHAI DANG KY voi Bo Tai chinh
Ca 9 dich vu duoi day thuoc KHOAN 2.

Can cu chuyen nganh da doi chieu tan van ban:
  - Luat Duong sat (VBHN 75/VBHN-VPQH) Dieu 5, 23, 24, 25, 32, 34
  - Nghi dinh 206/2026/ND-CP quan ly chi phi dau tu xay dung
  - Nghi dinh 212/2026/ND-CP dieu kien nang luc hoat dong xay dung
  - Nghi dinh 193/2026/ND-CP Dieu 20 (dinh muc chi phi kiem toan quyet toan)
"""

NHOM = {
    'tc': ('Tài chính và thu hồi vốn', 'var(--muc)'),
    'qt': ('Quản trị Ban quản lý dự án', 'var(--ngoc)'),
    'tk': ('Thuế và năng lực', 'var(--hoacuc)'),
}

DICH_VU = [
    # ------------------------------------------------------------------ 1
    dict(
        slug='thu-hoi-von-tod', nhom='tc',
        menu='Thu hồi vốn từ quỹ đất TOD',
        ten='Tư vấn phương án thu hồi vốn từ khai thác quỹ đất TOD',
        td='Tư vấn thu hồi vốn từ khai thác quỹ đất TOD',
        mt='Dựng mô hình dòng tiền quỹ đất TOD theo Điều 25 Luật Đường sắt: tiến độ thu, '
           'tỷ lệ để lại ngân sách địa phương, độ nhạy khi giá đất và tiến độ thay đổi.',
        lede='Đường sắt đô thị gần như không bao giờ hoàn vốn bằng tiền vé. Nguồn hoàn vốn thật '
             'nằm ở phần giá trị đất tăng lên quanh nhà ga — và pháp luật đã mở đường để địa phương '
             'giữ lại phần đó. Vấn đề là chuyển cơ chế trên giấy thành một dòng tiền có thể '
             'đưa vào phương án tài chính và bảo vệ được trước cơ quan thẩm định.',
        van_de=[
            'Cơ chế cho phép tạo quỹ đất đấu giá đã có, nhưng chưa ai lượng hoá được nó mang về bao nhiêu và về vào lúc nào.',
            'Tiền đấu giá đất về sau, chi phí giải phóng mặt bằng phải bỏ ra trước — khoảng lệch này chưa được mô hình hoá.',
            'Phương án tài chính của tuyến và phương án khai thác quỹ đất được lập bởi hai bộ phận khác nhau, không khớp số.',
            'Giá đất giả định quá lạc quan, tới lúc đấu giá thật thì hụt, nhưng lúc đó dự án đã cam kết tiến độ.',
        ],
        can_cu=[
            ('Luật Đường sắt (bản hợp nhất 75/VBHN-VPQH) — Điều 25 khoản 2',
             'Hội đồng nhân dân cấp tỉnh được quyết định dùng ngân sách địa phương triển khai '
             'dự án đầu tư công độc lập thực hiện bồi thường, hỗ trợ, tái định cư theo quy hoạch '
             'khu vực TOD để tạo quỹ đất đấu giá.'),
            ('Luật Đường sắt — Điều 25 khoản 3',
             'Tiền thu từ khai thác quỹ đất khu vực TOD: với đường sắt quốc gia, sau khi trừ chi phí '
             'bồi thường và chi phí liên quan, địa phương giữ lại 50%, nộp ngân sách trung ương 50%. '
             'Với đường sắt địa phương, địa phương giữ lại 100%.'),
            ('Luật Đường sắt — Điều 3 khoản 6 và khoản 7',
             'Định nghĩa khu vực TOD và dự án đường sắt địa phương theo mô hình TOD — xác định đúng '
             'loại dự án mới biết áp tỷ lệ nào.'),
        ],
        lam_gi=[
            ('Xác định loại dự án và tỷ lệ được giữ lại',
             'Đường sắt quốc gia hay đường sắt địa phương quyết định tỷ lệ 50% hay 100%. '
             'Đây là câu đầu tiên phải trả lời, vì nó đổi toàn bộ con số.'),
            ('Lập bảng quỹ đất theo từng khu vực TOD',
             'Diện tích, hiện trạng, chỉ tiêu quy hoạch sau khi điều chỉnh, thời điểm dự kiến '
             'đủ điều kiện đấu giá.'),
            ('Dựng mô hình dòng tiền hai chiều',
             'Chiều ra: chi phí bồi thường, hỗ trợ, tái định cư và chi phí tổ chức thực hiện. '
             'Chiều vào: tiền đấu giá theo từng đợt. Khoảng lệch giữa hai chiều chính là phần '
             'ngân sách địa phương phải gánh trước.'),
            ('Chạy độ nhạy',
             'Giá đất giảm 10–30%, tiến độ đấu giá chậm 1–3 năm, tỷ lệ đất đấu giá thành công '
             'thấp hơn dự kiến. Kết quả cho biết phương án chịu được đến đâu.'),
            ('Viết phần thuyết minh',
             'Trình bày theo ngôn ngữ hồ sơ trình duyệt, dẫn đúng điều khoản, để cơ quan thẩm định '
             'kiểm được từng con số.'),
        ],
        dau_ra=[
            'Bảng quỹ đất TOD theo từng khu vực, kèm mốc thời gian dự kiến',
            'Mô hình dòng tiền quỹ đất, mở được và sửa được, không phải hộp đen',
            'Bảng phân tích độ nhạy theo giá đất và tiến độ',
            'Thuyết minh phương án thu hồi vốn, dẫn chiếu điều khoản đầy đủ',
        ],
        khi_nao='Khi lập báo cáo nghiên cứu tiền khả thi hoặc khả thi cho tuyến có gắn TOD; khi Hội '
                'đồng nhân dân cấp tỉnh chuẩn bị quyết nghị dùng ngân sách địa phương tạo quỹ đất; '
                'hoặc khi phương án tài chính hiện có bị cơ quan thẩm định trả lại vì phần hoàn vốn '
                'chưa thuyết phục.',
    ),
    # ------------------------------------------------------------------ 2
    dict(
        slug='phuong-an-tai-chinh', nhom='tc',
        menu='Phương án tài chính tuyến và dự án TOD',
        ten='Tư vấn phương án tài chính tổng thể tuyến và dự án TOD',
        td='Tư vấn phương án tài chính tuyến đường sắt đô thị',
        mt='Dựng phương án tài chính cả vòng đời tuyến: vốn đầu tư, trợ giá vận hành, nguồn thu '
           'từ TOD, khả năng cân đối ngân sách địa phương và phân tích độ nhạy.',
        lede='Một tuyến đường sắt đô thị không kết thúc ở ngày cắt băng. Sau đó là hai ba chục năm '
             'vận hành, bảo trì, thay thế thiết bị và trợ giá. Phương án tài chính chỉ tính tới lúc '
             'hoàn thành xây dựng là phương án thiếu một nửa.',
        van_de=[
            'Tổng mức đầu tư được tính kỹ, nhưng chi phí vận hành và bảo trì cả vòng đời thì ước lượng qua loa.',
            'Trợ giá vận tải hành khách công cộng chưa được đưa vào cân đối ngân sách địa phương dài hạn.',
            'Chi phí thay thế thiết bị lớn ở năm thứ 15–20 không xuất hiện ở đâu trong hồ sơ.',
            'Nguồn thu ngoài vé — quảng cáo, thương mại tại ga, khai thác quỹ đất — bị bỏ ngoài mô hình.',
        ],
        can_cu=[
            ('Luật Đường sắt — Điều 5 khoản 1 và khoản 2',
             'Chính sách ưu tiên phân bổ ngân sách đầu tư, nâng cấp, bảo trì; Nhà nước trợ giá cho '
             'hoạt động vận tải hành khách công cộng bằng đường sắt đô thị.'),
            ('Luật Đường sắt — Điều 32 khoản 3 và khoản 4',
             'Được dùng hệ thống định mức, đơn giá vận hành và bảo trì do tổ chức trong nước, nước '
             'ngoài công bố khi hệ thống trong nước chưa có hoặc chưa phù hợp. Chi phí vận hành thử, '
             'đào tạo, tiếp nhận chuyển giao công nghệ được tính trong tổng mức đầu tư.'),
            ('Nghị định 206/2026/NĐ-CP', 'Quản lý chi phí đầu tư xây dựng — tổng mức đầu tư, dự toán '
             'xây dựng, dự toán gói thầu và chi phí vận hành, bảo trì.'),
        ],
        lam_gi=[
            ('Dựng khung dòng tiền cả vòng đời',
             'Giai đoạn đầu tư, giai đoạn vận hành ổn định, các mốc thay thế thiết bị lớn.'),
            ('Bóc tách nguồn thu',
             'Doanh thu vé, trợ giá, nguồn thu ngoài vé, và nguồn thu từ khai thác quỹ đất TOD nếu có.'),
            ('Xác định chi phí vận hành và bảo trì',
             'Dùng định mức trong nước nếu có; nếu chưa có thì dẫn định mức của tuyến tương tự '
             'và quy đổi về thời điểm tính toán theo Điều 32.'),
            ('Cân đối với khả năng ngân sách địa phương',
             'Chỉ ra mỗi năm ngân sách phải bố trí bao nhiêu, và con số đó chiếm bao nhiêu phần '
             'chi đầu tư phát triển của địa phương.'),
            ('Phân tích độ nhạy và điểm gãy',
             'Lượng khách thấp hơn dự báo, giá điện tăng, tỷ giá biến động với hợp đồng ngoại tệ.'),
        ],
        dau_ra=[
            'Mô hình tài chính cả vòng đời, có bảng giả định tách riêng',
            'Bảng cân đối nhu cầu ngân sách địa phương theo từng năm',
            'Phân tích độ nhạy và các điểm gãy của phương án',
            'Thuyết minh phương án tài chính theo cấu trúc hồ sơ trình duyệt',
        ],
        khi_nao='Khi lập hoặc thẩm tra báo cáo nghiên cứu tiền khả thi, khả thi; khi điều chỉnh chủ '
                'trương đầu tư; hoặc khi chuẩn bị đưa tuyến vào vận hành và cần biết ngân sách phải '
                'gánh bao nhiêu mỗi năm.',
    ),
    # ------------------------------------------------------------------ 3
    dict(
        slug='co-cau-nguon-von', nhom='tc',
        menu='Cơ cấu nguồn vốn dự án',
        ten='Tư vấn cơ cấu nguồn vốn dự án đường sắt đô thị',
        td='Tư vấn cơ cấu nguồn vốn dự án đường sắt đô thị',
        mt='So sánh và phối hợp các nguồn vốn cho tuyến metro: ngân sách, ODA, vốn ngoài nhà nước '
           'và PPP; ai chịu rủi ro nào và chi phí thật của từng nguồn.',
        lede='Mỗi nguồn vốn đi kèm một bộ ràng buộc riêng: về thủ tục, về tiến độ giải ngân, về '
             'xuất xứ hàng hoá, về ai gánh rủi ro tỷ giá. Chọn sai cơ cấu thì dự án không thiếu tiền '
             'nhưng vẫn tắc.',
        van_de=[
            'Vốn ODA rẻ trên danh nghĩa nhưng kèm ràng buộc nhà thầu và xuất xứ thiết bị, làm đội chi phí thật.',
            'Rủi ro tỷ giá của khoản vay ngoại tệ kéo dài hai ba chục năm chưa được định lượng.',
            'Phần vốn đối ứng trong nước không được bố trí kịp, làm chậm giải ngân phần vốn vay.',
            'Chưa rõ phần nào nên để nhà đầu tư ngoài nhà nước làm, phần nào bắt buộc nhà nước giữ.',
        ],
        can_cu=[
            ('Luật Đường sắt — Điều 24',
             'Dự án đường sắt đầu tư theo pháp luật về đầu tư, pháp luật về đầu tư theo phương thức '
             'đối tác công tư được Nhà nước bảo đảm toàn bộ kinh phí bồi thường, hỗ trợ, tái định cư '
             'từ ngân sách nhà nước; việc bồi thường được tách thành dự án riêng.'),
            ('Luật Đường sắt — Điều 23',
             'Phân chia dự án đường sắt: dự án thành phần về bồi thường, hỗ trợ, tái định cư được '
             'quản lý như dự án độc lập và không phải đáp ứng yêu cầu vận hành độc lập.'),
            ('Luật Đường sắt — Điều 5 khoản 2 và khoản 4',
             'Cơ chế vay lại, hỗ trợ vốn tín dụng ưu đãi; kinh doanh kết cấu hạ tầng đường sắt, '
             'vận tải đường sắt, công nghiệp đường sắt và đào tạo nhân lực là ngành nghề ưu đãi đầu tư.'),
        ],
        lam_gi=[
            ('Liệt kê nguồn vốn khả dụng và điều kiện đi kèm',
             'Từng nguồn: lãi suất, thời hạn, ân hạn, ràng buộc mua sắm, thủ tục giải ngân.'),
            ('Quy về một mặt bằng so sánh',
             'Tính chi phí vốn thật sau khi cộng ràng buộc mua sắm và chi phí thủ tục, không chỉ nhìn lãi suất.'),
            ('Lập bản đồ rủi ro',
             'Rủi ro tỷ giá, rủi ro giải ngân, rủi ro tiến độ giải phóng mặt bằng — ai gánh, gánh bằng cơ chế nào.'),
            ('Đề xuất cơ cấu và kịch bản dự phòng',
             'Kèm điều kiện kích hoạt: nếu nguồn A chậm quá bao lâu thì chuyển sang phương án nào.'),
        ],
        dau_ra=[
            'Bảng so sánh các nguồn vốn quy về cùng mặt bằng',
            'Bản đồ phân bổ rủi ro giữa các bên',
            'Đề xuất cơ cấu nguồn vốn kèm kịch bản dự phòng',
        ],
        khi_nao='Khi chuẩn bị hồ sơ chủ trương đầu tư; khi cân nhắc chuyển một phần tuyến sang hình '
                'thức đối tác công tư; hoặc khi nguồn vốn đang dùng phát sinh vướng mắc về giải ngân.',
    ),
    # ------------------------------------------------------------------ 4
    dict(
        slug='suat-von-dau-tu', nhom='tc',
        menu='Suất vốn đầu tư và quy đổi định mức',
        ten='Tư vấn suất vốn đầu tư và quy đổi định mức nước ngoài',
        td='Tư vấn suất vốn đầu tư và quy đổi định mức metro',
        mt='Chọn dự án tương tự, quy đổi suất vốn đầu tư và định mức nước ngoài về thời điểm '
           'tính toán theo Điều 32 Luật Đường sắt, kèm lập luận bảo vệ hồ sơ.',
        lede='Hệ thống định mức xây dựng của Việt Nam chưa phủ hết các hạng mục của đường sắt đô thị. '
             'Luật đã cho phép dùng định mức và suất vốn đầu tư của nước ngoài. Nhưng cho phép là một '
             'chuyện, chứng minh được lựa chọn của mình trước cơ quan thẩm định lại là chuyện khác — '
             'và đây là chỗ hồ sơ hay bị trả lại nhất.',
        van_de=[
            'Không có định mức trong nước cho hạng mục hầm, đầu máy toa xe, hệ thống tín hiệu và điều khiển chạy tàu.',
            'Lấy số của dự án nước ngoài nhưng không giải trình được vì sao dự án đó là "tương tự".',
            'Quy đổi về thời điểm tính toán làm qua loa, không tách bạch trượt giá, tỷ giá và khác biệt điều kiện thi công.',
            'Mỗi lần điều chỉnh dự án lại phải làm lại từ đầu vì không có bộ dữ liệu gốc lưu lại.',
        ],
        can_cu=[
            ('Luật Đường sắt — Điều 32 khoản 1',
             'Với hạng mục chưa phù hợp hoặc chưa có trong hệ thống định mức, giá xây dựng, suất vốn '
             'đầu tư được cấp có thẩm quyền ban hành, dự án đường sắt được dùng hệ thống của tổ chức '
             'trong nước, nước ngoài công bố cho hạng mục tương tự hoặc dự án đường sắt tương tự, '
             'và quy đổi về thời điểm tính toán.'),
            ('Luật Đường sắt — Điều 32 khoản 2 và khoản 5',
             'Trường hợp vẫn không xác định được thì dùng suất vốn đầu tư của dự án tương tự trên thế giới. '
             'Khoản mục chi phí chưa được quy định trong pháp luật Việt Nam được áp dụng theo dự án '
             'đường sắt tương tự trên thế giới.'),
            ('Nghị định 206/2026/NĐ-CP — Điều 16',
             'Thẩm định, thẩm tra dự toán xây dựng — nội dung cơ quan thẩm định sẽ soi.'),
        ],
        lam_gi=[
            ('Xác định hạng mục nào thiếu định mức',
             'Đối chiếu danh mục công việc của dự án với hệ thống định mức hiện hành, lập danh sách khuyết.'),
            ('Chọn dự án tương tự và chứng minh tính tương tự',
             'Theo khổ đường, loại hình, tỷ lệ ngầm trên cao, điều kiện địa chất, mức độ tự động hoá. '
             'Phần chứng minh này quan trọng ngang phần số.'),
            ('Quy đổi về thời điểm tính toán',
             'Tách bạch ba lớp điều chỉnh: trượt giá theo thời gian, chênh lệch mặt bằng giá giữa hai '
             'quốc gia, khác biệt điều kiện thi công và tiêu chuẩn áp dụng.'),
            ('Lưu bộ dữ liệu gốc',
             'Nguồn công bố, ngày công bố, tỷ giá dùng, chỉ số giá dùng — để lần điều chỉnh sau '
             'không phải làm lại từ đầu.'),
            ('Viết bản thuyết minh phương pháp',
             'Đủ chi tiết để người thẩm định lần theo được từng bước tính.'),
        ],
        dau_ra=[
            'Danh mục hạng mục thiếu định mức trong nước',
            'Hồ sơ chọn dự án tương tự kèm lập luận',
            'Bảng quy đổi ba lớp về thời điểm tính toán',
            'Bộ dữ liệu gốc lưu lại để dùng cho các lần điều chỉnh sau',
        ],
        khi_nao='Khi lập hoặc điều chỉnh tổng mức đầu tư; khi lập dự toán gói thầu cho hạng mục '
                'chuyên ngành; hoặc khi hồ sơ bị cơ quan thẩm định yêu cầu giải trình cơ sở của đơn giá.',
    ),
    # ------------------------------------------------------------------ 5
    dict(
        slug='kiem-soat-noi-bo', nhom='qt',
        menu='Kiểm soát nội bộ Ban quản lý dự án',
        ten='Tư vấn thiết lập kiểm soát nội bộ cho Ban quản lý dự án',
        td='Tư vấn kiểm soát nội bộ cho Ban quản lý dự án',
        mt='Thiết kế quy chế chi tiêu, phân nhiệm và chốt kiểm soát khối lượng — thanh toán cho Ban '
           'quản lý dự án đường sắt đô thị, gắn với yêu cầu quyết toán về sau.',
        lede='Phần lớn sai sót bị phát hiện lúc quyết toán không phải do ai cố tình, mà do trong suốt '
             'quá trình thực hiện không có ai được giao việc kiểm lại. Kiểm soát nội bộ dựng đúng ngay '
             'từ đầu rẻ hơn nhiều so với xử lý hậu quả sau tám năm.',
        van_de=[
            'Một người vừa nghiệm thu khối lượng vừa xác nhận thanh toán — không có chốt chặn nào ở giữa.',
            'Quy chế chi tiêu nội bộ có, nhưng không ai đối chiếu với quy định về quản lý chi phí đầu tư xây dựng.',
            'Hồ sơ phát sinh được duyệt bằng lời trước, làm thủ tục sau, đến lúc quyết toán không đủ căn cứ.',
            'Nhân sự Ban thay đổi qua nhiều nhiệm kỳ, mỗi thời kỳ làm một kiểu, không có chuẩn chung.',
        ],
        can_cu=[
            ('Nghị định 206/2026/NĐ-CP',
             'Quản lý chi phí đầu tư xây dựng: thẩm quyền phê duyệt dự toán, dự toán gói thầu, '
             'điều chỉnh — cơ sở để thiết kế bậc phê duyệt trong quy chế nội bộ.'),
            ('Nghị định 207/2026/NĐ-CP',
             'Quản lý chất lượng thi công và bảo trì — cơ sở cho chốt kiểm soát nghiệm thu.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Quyết toán vốn đầu tư dự án — biết trước hồ sơ quyết toán đòi gì thì thiết kế kiểm soát '
             'cho khớp ngay từ đầu.'),
        ],
        lam_gi=[
            ('Vẽ lại luồng công việc hiện tại',
             'Từ đề nghị thanh toán tới lúc tiền ra khỏi kho bạc, đi qua những ai, ai ký gì.'),
            ('Chỉ ra chỗ hở',
             'Nơi một người nắm cả hai vai; nơi không có ai đối chiếu; nơi hồ sơ đi sau tiền.'),
            ('Thiết kế lại chốt kiểm soát',
             'Tách vai nghiệm thu và vai xác nhận thanh toán; đặt hạn mức phê duyệt theo cấp; '
             'quy định hồ sơ tối thiểu cho từng loại chi.'),
            ('Soạn quy chế và biểu mẫu',
             'Quy chế chi tiêu nội bộ, quy trình kiểm soát khối lượng — thanh toán, biểu mẫu kèm theo.'),
            ('Đào tạo và chạy thử',
             'Chạy thử trên vài hồ sơ thật, chỉnh lại chỗ vướng rồi mới ban hành chính thức.'),
        ],
        dau_ra=[
            'Sơ đồ luồng công việc hiện tại và luồng đề xuất, đặt cạnh nhau',
            'Danh sách chỗ hở kèm mức độ rủi ro',
            'Dự thảo quy chế chi tiêu nội bộ và quy trình kiểm soát',
            'Bộ biểu mẫu kèm theo, dùng được ngay',
        ],
        khi_nao='Khi Ban quản lý dự án mới thành lập; khi tuyến bước vào giai đoạn thi công có khối '
                'lượng thanh toán lớn; hoặc sau một kỳ thanh tra, kiểm toán có kiến nghị về kiểm soát.',
    ),
    # ------------------------------------------------------------------ 6
    dict(
        slug='ho-so-quyet-toan', nhom='qt',
        menu='Quản lý hồ sơ quyết toán từ ngày đầu',
        ten='Tư vấn quy trình quản lý hồ sơ quyết toán từ ngày đầu dự án',
        td='Tư vấn quản lý hồ sơ quyết toán dự án metro',
        mt='Dựng quy tắc lập, đánh mã, lưu và bàn giao hồ sơ quyết toán ngay từ gói thầu đầu tiên, '
           'cho dự án kéo dài tám tới mười hai năm.',
        lede='Một tuyến metro chạy tám tới mười hai năm. Nhà thầu của gói thầu đầu tiên có thể đã giải '
             'thể trước khi tuyến chạy chuyến đầu. Người ký biên bản nghiệm thu năm thứ hai có thể đã '
             'nghỉ hưu. Hồ sơ nào không được thu đúng lúc thì về sau không thu được nữa — không phải '
             'vì ai giấu, mà vì nó không còn tồn tại.',
        van_de=[
            'Hồ sơ phần ngầm và phần khuất bị che lấp, sau này không kiểm chứng lại được bằng cách nào khác.',
            'Nhà thầu giai đoạn đầu giải thể hoặc đổi chủ, không còn ai xác nhận khối lượng.',
            'Hồ sơ nằm rải ở nhiều bộ phận, không có mã chung, không biết thiếu cái gì cho tới lúc lập báo cáo quyết toán.',
            'Bản vẽ hoàn công và biên bản nghiệm thu không khớp nhau, phát hiện quá muộn để sửa.',
        ],
        can_cu=[
            ('Nghị định 193/2026/NĐ-CP',
             'Quy định về quyết toán vốn đầu tư dự án — danh mục hồ sơ và nội dung báo cáo quyết toán. '
             'Biết đích đến thì thiết kế được đường đi.'),
            ('Nghị định 207/2026/NĐ-CP',
             'Quản lý chất lượng thi công xây dựng và bảo trì — hồ sơ nghiệm thu, hồ sơ hoàn thành công trình.'),
            ('Luật Đường sắt — Điều 23',
             'Phân chia dự án thành phần: mỗi dự án thành phần được quản lý như dự án độc lập, '
             'nên hồ sơ cũng phải khép được theo từng dự án thành phần.'),
        ],
        lam_gi=[
            ('Dựng danh mục hồ sơ đích',
             'Đi ngược từ yêu cầu của báo cáo quyết toán về từng giai đoạn: giai đoạn nào phải sinh ra hồ sơ gì.'),
            ('Đặt hệ mã hồ sơ dùng chung',
             'Một mã duy nhất theo dự án thành phần, gói thầu, hạng mục — để mọi bộ phận gọi cùng một tên.'),
            ('Quy định mốc thu hồ sơ bắt buộc',
             'Gắn với mốc nghiệm thu và mốc thanh toán, không để hồ sơ đi sau tiền. '
             'Đặc biệt với phần ngầm và phần sẽ bị che lấp.'),
            ('Thiết kế cách lưu và sao lưu',
             'Bản giấy và bản điện tử, nơi lưu, ai giữ, sao lưu ở đâu, giữ trong bao lâu.'),
            ('Đặt lịch tự kiểm định kỳ',
             'Mỗi quý rà một lần xem thiếu gì, thiếu thì đòi ngay khi còn đòi được.'),
        ],
        dau_ra=[
            'Danh mục hồ sơ quyết toán theo từng giai đoạn dự án',
            'Hệ mã hồ sơ và quy tắc đặt tên dùng chung',
            'Quy trình thu, lưu, sao lưu và bàn giao hồ sơ',
            'Biểu tự kiểm theo quý',
        ],
        khi_nao='Tốt nhất là trước khi ký gói thầu đầu tiên. Muộn hơn thì vẫn làm được, nhưng phải kèm '
                'một đợt rà soát ngược để dựng lại phần hồ sơ đã hụt.',
    ),
    # ------------------------------------------------------------------ 7
    dict(
        slug='tai-co-cau-doanh-nghiep', nhom='qt',
        menu='Tái cơ cấu doanh nghiệp dự án và vận hành',
        ten='Tư vấn tái cơ cấu doanh nghiệp dự án và đơn vị vận hành',
        td='Tư vấn tái cơ cấu doanh nghiệp dự án đường sắt',
        mt='Tư vấn chuyển đổi mô hình tổ chức khi tuyến chuyển từ giai đoạn đầu tư sang khai thác: '
           'bàn giao tài sản, tổ chức bộ máy, cơ chế tài chính của đơn vị vận hành.',
        lede='Ngày tuyến chạy chuyến đầu tiên cũng là ngày một tổ chức phải đổi bản chất: từ bộ máy '
             'quản lý đầu tư sang bộ máy khai thác. Hai việc này đòi hỏi con người khác nhau, quy trình '
             'khác nhau, cơ chế tài chính khác nhau. Chuyển không kịp thì tuyến chạy nhưng sổ sách rối.',
        van_de=[
            'Tài sản hình thành qua đầu tư chưa được ghi nhận đủ và đúng trước khi bàn giao cho đơn vị vận hành.',
            'Chưa rõ đơn vị vận hành nhận tài sản theo hình thức nào, và ghi nhận trên sổ ra sao.',
            'Cơ chế trợ giá chưa có công thức ổn định, mỗi năm thương lượng lại một lần.',
            'Ban quản lý dự án vẫn còn công việc quyết toán dở dang trong khi nhân sự đã chuyển sang vận hành.',
        ],
        can_cu=[
            ('Luật Đường sắt — Điều 5 khoản 2 điểm c',
             'Nhà nước trợ giá cho hoạt động vận tải hành khách công cộng bằng đường sắt đô thị.'),
            ('Luật Kiểm toán độc lập — Điều 40 khoản 2 điểm b',
             'Doanh nghiệp kiểm toán được đăng ký thực hiện dịch vụ tư vấn quản lý, chuyển đổi và '
             'tái cơ cấu doanh nghiệp.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Giá trị tài sản hình thành qua đầu tư và việc bàn giao — phần này phải khép trước khi '
             'chuyển giao cho đơn vị vận hành.'),
        ],
        lam_gi=[
            ('Rà tình trạng tài sản và công nợ trước chuyển giao',
             'Tài sản đã đủ hồ sơ chưa, công nợ với nhà thầu còn treo bao nhiêu, ai chịu trách nhiệm tiếp.'),
            ('Thiết kế mô hình tổ chức của đơn vị vận hành',
             'Chức năng, bộ máy, định biên, và phần việc quyết toán còn lại của Ban quản lý dự án.'),
            ('Dựng cơ chế tài chính vận hành',
             'Công thức trợ giá, cơ chế điều chỉnh, chỉ tiêu đánh giá hiệu quả khai thác.'),
            ('Lập lộ trình chuyển giao theo mốc',
             'Việc nào phải xong trước ngày vận hành thương mại, việc nào có thể xong sau.'),
        ],
        dau_ra=[
            'Báo cáo rà soát tài sản và công nợ trước chuyển giao',
            'Đề án tổ chức đơn vị vận hành',
            'Cơ chế tài chính và công thức trợ giá đề xuất',
            'Lộ trình chuyển giao theo mốc thời gian',
        ],
        khi_nao='Khoảng mười hai tới mười tám tháng trước ngày dự kiến vận hành thương mại; hoặc khi '
                'địa phương chuẩn bị thành lập, sắp xếp lại đơn vị vận hành đường sắt đô thị.',
    ),
    # ------------------------------------------------------------------ 8
    dict(
        slug='thue-du-an', nhom='tk',
        menu='Thuế cho dự án đường sắt đô thị',
        ten='Tư vấn thuế cho dự án đường sắt đô thị',
        td='Tư vấn thuế cho dự án đường sắt đô thị',
        mt='Xử lý thuế nhà thầu nước ngoài với đoàn tàu và hệ thống tín hiệu, thuế giá trị gia tăng '
           'với nguồn vốn ODA, và các ưu đãi theo Điều 5 Luật Đường sắt.',
        lede='Đường sắt đô thị nhập gần như toàn bộ phần công nghệ lõi: đoàn tàu, hệ thống tín hiệu, '
             'hệ thống điều khiển chạy tàu, cùng với chuyên gia nước ngoài đi kèm. Mỗi hợp đồng như vậy '
             'kéo theo một bài toán thuế nhà thầu, và sai sót thường chỉ lộ ra khi thanh tra thuế — '
             'lúc đó tiền đã trả cho nhà thầu rồi.',
        van_de=[
            'Hợp đồng trọn gói gồm cả thiết bị, lắp đặt, đào tạo và chuyển giao công nghệ nhưng không tách giá trị từng phần, dẫn tới áp sai tỷ lệ thuế nhà thầu.',
            'Chưa xác định rõ bên nào chịu thuế nhà thầu, đến lúc quyết toán mới phát hiện thiếu tiền.',
            'Xử lý thuế giá trị gia tăng với phần vốn ODA chưa nhất quán giữa các gói thầu.',
            'Chưa vận dụng hết các ưu đãi đầu tư mà pháp luật đã dành cho ngành đường sắt.',
        ],
        can_cu=[
            ('Luật Đường sắt — Điều 5 khoản 4',
             'Kinh doanh kết cấu hạ tầng đường sắt, kinh doanh vận tải đường sắt, công nghiệp đường sắt '
             'và đào tạo nguồn nhân lực đường sắt là các ngành, nghề ưu đãi đầu tư.'),
            ('Luật Đường sắt — Điều 32 khoản 4',
             'Chi phí vận hành thử, đào tạo, tiếp nhận chuyển giao công nghệ được tính trong tổng mức '
             'đầu tư — cách tách các khoản này ảnh hưởng trực tiếp tới nghĩa vụ thuế.'),
            ('Luật Kiểm toán độc lập — Điều 40 khoản 2 điểm a',
             'Doanh nghiệp kiểm toán được đăng ký thực hiện dịch vụ tư vấn kinh tế, tài chính, thuế.'),
        ],
        lam_gi=[
            ('Rà soát hợp đồng trước khi ký',
             'Tách giá trị theo từng cấu phần, xác định nghĩa vụ thuế của từng cấu phần, '
             'làm rõ bên nào chịu thuế.'),
            ('Xác định nghĩa vụ thuế nhà thầu',
             'Theo từng loại hoạt động: cung cấp hàng hoá, dịch vụ lắp đặt, đào tạo, chuyển giao công nghệ.'),
            ('Xử lý thuế giá trị gia tăng theo nguồn vốn',
             'Thống nhất cách xử lý giữa các gói thầu trong cùng dự án.'),
            ('Rà soát ưu đãi đầu tư',
             'Đối chiếu điều kiện hưởng ưu đãi và hồ sơ cần có để được hưởng.'),
            ('Chuẩn bị hồ sơ giải trình',
             'Lập sẵn hồ sơ lập luận để dùng khi cơ quan thuế kiểm tra.'),
        ],
        dau_ra=[
            'Bản rà soát điều khoản thuế trong hợp đồng, kèm khuyến nghị sửa',
            'Bảng xác định nghĩa vụ thuế nhà thầu theo từng cấu phần',
            'Hướng dẫn xử lý thuế giá trị gia tăng thống nhất trong dự án',
            'Hồ sơ giải trình cho cơ quan thuế',
        ],
        khi_nao='Trước khi ký hợp đồng với nhà thầu nước ngoài — đây là thời điểm còn sửa được điều '
                'khoản. Sau khi ký thì chỉ còn xử lý hậu quả.',
    ),
    # ------------------------------------------------------------------ 9
    dict(
        slug='boi-duong-can-bo', nhom='tk',
        menu='Bồi dưỡng cán bộ Ban quản lý dự án',
        ten='Bồi dưỡng kiến thức tài chính, kế toán, kiểm toán cho cán bộ Ban quản lý dự án',
        td='Bồi dưỡng cán bộ Ban quản lý dự án đường sắt',
        mt='Chương trình bồi dưỡng theo yêu cầu về quyết toán vốn đầu tư, kiểm soát chi phí, hồ sơ '
           'thanh toán và chuẩn bị đón kiểm toán, dành cho cán bộ Ban quản lý dự án.',
        lede='Cán bộ Ban quản lý dự án phần lớn xuất thân kỹ thuật. Họ đọc bản vẽ tốt hơn đọc quy định '
             'về quyết toán. Khoảng trống đó là nguyên nhân của rất nhiều hồ sơ phải làm lại — và nó '
             'lấp được bằng đào tạo đúng nội dung, không cần ai đi học lại một bằng khác.',
        van_de=[
            'Hồ sơ thanh toán bị trả lại nhiều lần vì thiếu thành phần, mất thời gian của cả hai bên.',
            'Cán bộ không biết trước kiểm toán sẽ hỏi gì nên chuẩn bị bị động.',
            'Mỗi người làm một kiểu vì chưa có chuẩn chung trong Ban.',
            'Nhân sự mới về không có tài liệu nào để tự học, phải học truyền miệng.',
        ],
        can_cu=[
            ('Luật Kiểm toán độc lập — Điều 40 khoản 2 điểm e',
             'Doanh nghiệp kiểm toán được đăng ký thực hiện dịch vụ bồi dưỡng kiến thức tài chính, '
             'kế toán, kiểm toán. Chương trình của chúng tôi khuôn đúng trong ba lĩnh vực này.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Quyết toán vốn đầu tư dự án — nội dung cốt lõi của chương trình.'),
            ('Nghị định 206/2026/NĐ-CP', 'Quản lý chi phí đầu tư xây dựng.'),
        ],
        lam_gi=[
            ('Khảo sát nhu cầu trước',
             'Xem hồ sơ thực tế của Ban đang vướng ở đâu, rồi mới thiết kế nội dung. '
             'Không mang giáo án có sẵn tới dạy.'),
            ('Thiết kế chương trình theo nhóm học viên',
             'Cán bộ kỹ thuật, cán bộ kế toán và lãnh đạo Ban cần ba mức nội dung khác nhau.'),
            ('Dạy trên hồ sơ thật',
             'Dùng chính hồ sơ của dự án, đã ẩn danh, thay cho ví dụ giả định.'),
            ('Giao bài tập áp dụng và chấm',
             'Học xong phải làm được, không chỉ nghe xong.'),
            ('Bàn giao bộ tài liệu để tự học',
             'Để nhân sự mới về sau còn dùng được.'),
        ],
        dau_ra=[
            'Báo cáo khảo sát nhu cầu đào tạo',
            'Chương trình và tài liệu giảng dạy, bàn giao lại cho Ban',
            'Kết quả đánh giá theo từng học viên',
            'Bộ tài liệu tự học cho nhân sự mới',
        ],
        khi_nao='Trước mùa quyết toán; khi Ban tiếp nhận nhiều nhân sự mới; hoặc sau một đợt kiểm toán, '
                'thanh tra có nhiều kiến nghị lặp lại.',
    ),
]

assert len(DICH_VU) == 9
