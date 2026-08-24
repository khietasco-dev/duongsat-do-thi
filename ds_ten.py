# -*- coding: utf-8 -*-
"""Ten van ban VIET CO DAU, tra theo so hieu.
Nguon: ten tep trong kho VBPL, viet lai cho dung chinh ta tieng Viet.
"""
import io, json, os, sys
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

TEN = {
    # ---------------- Luat & Nghi quyet Quoc hoi
    '95/2025/QH15':  'Luật Đường sắt',
    '02/2026/QH16':  'Luật Thủ đô',
    '39/2024/QH15':  'Luật Thủ đô (bản gốc, đã được thay thế)',
    '188/2025/QH15': 'Nghị quyết thí điểm cơ chế, chính sách đặc thù phát triển hệ thống '
                     'đường sắt đô thị Hà Nội và TP. Hồ Chí Minh',
    '114/VBHN-VPQH': 'Luật Thủ đô — bản hợp nhất',
    '75/VBHN-VPQH':  'Luật Đường sắt — bản hợp nhất',

    # ---------------- Nghi dinh
    '04/2026/NĐ-CP':  'Giao nhiệm vụ, đặt hàng cung cấp dịch vụ, hàng hoá công nghiệp đường sắt',
    '123/2025/NĐ-CP': 'Thiết kế kỹ thuật tổng thể và cơ chế đặc thù cho một số dự án đường sắt',
    '15/2025/NĐ-CP':  'Quản lý, sử dụng và khai thác tài sản kết cấu hạ tầng đường sắt',
    '16/2026/NĐ-CP':  'Quy định chi tiết một số điều của Luật Đường sắt',
    '81/2026/NĐ-CP':  'Xử phạt vi phạm hành chính trong lĩnh vực giao thông đường sắt',
    '34/VBHN-BXD':    'Nghị định về thiết kế kỹ thuật tổng thể và cơ chế đặc thù dự án đường sắt '
                      '— bản hợp nhất, 143 Điều',

    # ---------------- Thong tu
    '06/2025/TT-BXD':   'Quản lý, bảo trì kết cấu hạ tầng đường sắt quốc gia',
    '33/2025/TT-BXD':   'Quản lý, khai thác vận tải đường sắt',
    '34/2025/TT-BXD':   'Quản lý, khai thác kết cấu hạ tầng đường sắt',
    '44/2025/TT-BXD':   'Các Quy chuẩn kỹ thuật quốc gia về đường sắt',
    '59/2024/TT-BGTVT': 'Định mức kinh tế — kỹ thuật bảo dưỡng kết cấu hạ tầng đường sắt quốc gia',
    '62/2026/TT-BXD':   'Quy chuẩn kỹ thuật quốc gia về Đường sắt đô thị — loại hình metro',
    '75/2025/TT-BTC':   'Tính hao mòn tài sản kết cấu hạ tầng đường sắt',
    '10/VBHN-BXD':      'Thông tư về đăng ký phương tiện giao thông đường sắt — bản hợp nhất',
    '11/VBHN-BXD':      'Thông tư về giải quyết sự cố, tai nạn giao thông đường sắt — bản hợp nhất',
    '12/VBHN-BXD':      'Thông tư về đường ngang và cấp giấy phép xây dựng công trình thiết yếu '
                        '— bản hợp nhất',
    '13/VBHN-BXD':      'Thông tư về kết nối ray đường sắt đô thị, đường sắt chuyên dùng với '
                        'đường sắt quốc gia — bản hợp nhất',
    '14/VBHN-BXD':      'Thông tư về kết nối tín hiệu đèn giao thông đường bộ với đường sắt '
                        '— bản hợp nhất',

    # ---------------- Van ban khac
    '3222/VPCP-CN':    'Dự án đường sắt đô thị Hà Nội tuyến số 5',
    '3357/VPCP-CN':    'Đôn đốc thực hiện Nghị quyết 188/2025/QH15 về đường sắt đô thị',
    '3722/VPCP-CN':    'Cơ chế đặc thù kéo dài tuyến Metro Bến Thành – Suối Tiên',
    '01/2025/NQ-CP':   'Đầu tư mở rộng Cảng hàng không quốc tế Phú Quốc',
    '318/NQ-CP':       'Kế hoạch của Chính phủ triển khai Nghị quyết 188/2025/QH15 về đường sắt đô thị',
    '21/2026/NQ-HĐND': 'Quy hoạch khu vực TOD đối với đường sắt quốc gia và đường sắt địa phương',
    '31/2025/NQ-HĐND': 'Trình tự, thủ tục quyết định chủ trương đầu tư — ĐÃ HẾT HIỆU LỰC',
    '40/2025/NQ-HĐND': 'Lựa chọn áp dụng tiêu chuẩn, quy chuẩn kỹ thuật trong nước và nước ngoài',
    '62/2026/NQ-HĐND': 'Ưu đãi đầu tư phát triển và khai thác không gian ngầm, không gian tầm thấp',
    '64/2026/NQ-HĐND': 'Quy hoạch không gian ngầm và hoạt động quy hoạch đô thị, kiến trúc',
    '65/2026/NQ-HĐND': 'Các khoản thu từ khai thác không gian ngầm và không gian tầm thấp',
    '66/2026/NQ-HĐND': 'Cải tạo, chỉnh trang, tái thiết đô thị và phát triển đô thị tại khu vực TOD',
    '67/2026/NQ-HĐND': 'Các khoản thu từ khai thác giá trị tăng thêm trong khu vực TOD',
    '70/2026/NQ-HĐND': 'Chính sách đầu tư, quản lý, khai thác kết cấu hạ tầng đường bộ và '
                       'đường sắt địa phương',
    '71/2025/NQ-HĐND': 'Quy hoạch khu vực TOD đối với đường sắt quốc gia và đường sắt địa phương',
    '71/2026/NQ-HĐND': 'Chính sách phát triển vận tải công cộng và hạn chế phương tiện cá nhân',
    '88/2025/NQ-HĐND': 'Định mức chi phí, đơn giá lập, thẩm định, phê duyệt Quy hoạch tổng thể TP.HCM',
    '90/2025/NQ-HĐND': 'Phân cấp nguồn thu từ quỹ đất khu vực TOD đường sắt địa phương',
    '109/QĐ-TCTDSDT':  'Thay đổi thành viên Tổ công tác đường sắt đô thị Hà Nội và TP. Hồ Chí Minh',
    '1500/QĐ-TTg':     'Thành lập Ban Quản lý Khu kinh tế Phú Quốc, tỉnh An Giang',
    '2230/QĐ-TTg':     'Đề án đào tạo, phát triển nguồn nhân lực đường sắt đến năm 2035',
    '38/2026/QĐ-UBND': 'Quản lý, bảo trì kết cấu hạ tầng đường sắt địa phương',
    '498/QĐ-TTg':      'Cơ cấu lại Tổng công ty Đường sắt Việt Nam giai đoạn 2026–2030',
    '762/QĐ-TTg':      'Kế hoạch triển khai thi hành Luật Thủ đô',
    '948/QĐ-TTg':      'Triển khai nhanh các dự án phục vụ Hội nghị APEC 2027 tại Phú Quốc',
    '340/TB-VPCP':     'Kết luận Phiên họp thứ 2 Tổ công tác đường sắt đô thị Hà Nội và TP. Hồ Chí Minh',
    '443/TB-VPCP':     'Kết luận Phiên họp thứ 3 Tổ công tác đường sắt đô thị Hà Nội và TP. Hồ Chí Minh',
}

if __name__ == '__main__':
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vb_phanloai.json')
    vb = json.load(io.open(p, encoding='utf-8'))
    thieu = []
    for d in vb:
        t = TEN.get(d['sohieu'])
        if t:
            d['ten_dep'] = t
        else:
            d['ten_dep'] = d['ten_ngan']
            thieu.append(d['sohieu'])
    io.open(p, 'w', encoding='utf-8').write(json.dumps(vb, ensure_ascii=False, indent=1))
    print('Da gan ten co dau: %d/%d' % (len(vb) - len(thieu), len(vb)))
    if thieu:
        print('Thieu:', thieu)
