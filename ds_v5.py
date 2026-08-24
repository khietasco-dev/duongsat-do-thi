# -*- coding: utf-8 -*-
"""Ban 5 — trang tieng Anh, tieng Trung + ghi toan bo site."""
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
import ds_v4 as V4

N = P2.N


# ================================================================ TIENG ANH
def trang_en():
    gd = ''.join('<tr><td><b>%d</b></td><td><b>%s</b></td><td>%s</td></tr>' % (i + 1, a, b)
                 for i, (a, b) in enumerate([
        ("Route planning", "Incorporating the line into provincial and urban master plans; route alignment, station and depot locations; preliminary TOD area."),
        ("Investment policy decision", "Pre-feasibility study, capital source appraisal, investment policy decision by the competent authority."),
        ("Project appraisal and approval", "Feasibility study and basic design, or Front-End Engineering Design under the special mechanism; appraisal; approval. The approved total investment becomes the legal ceiling for all later settlement costs."),
        ("Site clearance and resettlement", "Land recovery, compensation, support and resettlement; handover of the site in phases."),
        ("Contractor selection", "Bidding plan, bidding documents, evaluation, approval, contract signing."),
        ("Construction and cost management", "Detailed design, cost estimates, construction, phased acceptance of work volumes, payment, handling of variations."),
        ("Testing, trial run and system safety certification", "Static and dynamic testing, integrated trial run, independent system safety assessment, state acceptance, operating licence."),
        ("Handover and asset recognition", "Handover to the operator, establishment of public asset ownership, asset records, depreciation, fare and subsidy policy."),
        ("Capital settlement", "Settlement report, independent audit of the settlement report, review, approval, handling of receivables and surplus materials."),
    ]))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Vietnamese site</a> · English</div>
  <h1>Urban railway projects in Vietnam — legal framework and audit</h1>
  <p>A reference site for project management units, investors, consultants and contractors
  working on metro and transit-oriented development projects in Vietnam.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="nn-bao">
    <b>About this page.</b> The full site is in Vietnamese, because it works with Vietnamese legal
    documents whose official text exists only in Vietnamese. This English page summarises what the site
    covers and the points that most often surprise foreign contractors and consultants.
    <a href="../index.html">Open the Vietnamese site →</a>
  </div>

  <h2 style="margin-bottom:12px">What foreign parties most often get wrong</h2>
  <div class="luoi g3">
    <div class="the" style="border-top:3px solid var(--do)">
      <h3>Applying superseded legislation</h3>
      <p>Vietnamese law changes often. The Railway Law exists in both a 2017 and a 2025 version;
      the Capital Law was replaced in 2026. A project spanning ten years passes through two or three
      generations of implementing decrees.</p>
    </div>
    <div class="the" style="border-top:3px solid var(--hoacuc)">
      <h3>Assuming the special mechanism applies everywhere</h3>
      <p>A National Assembly resolution allows a shortened procedure for urban railway projects,
      but <b>only in Hanoi and Ho Chi Minh City</b>. It does not extend to other localities.</p>
    </div>
    <div class="the" style="border-top:3px solid var(--ngoc)">
      <h3>EPC contracts without a bill of quantities</h3>
      <p>International lump-sum contracts transfer quantity risk to the contractor. Vietnamese capital
      settlement, however, requires evidence of quantities executed. Agree the price breakdown as a
      contract annex before signing.</p>
    </div>
  </div>

  <h2 style="margin:30px 0 12px">The nine project stages</h2>
  <div class="bang-boc">
    <table>
      <thead><tr><th style="width:56px">Stage</th><th style="width:27%%">Name</th><th>Content</th></tr></thead>
      <tbody>%s</tbody>
    </table>
  </div>

  <h2 style="margin:30px 0 12px">Audit runs in parallel, not only at the end</h2>
  <p>For a metro line the construction period typically runs eight to fifteen years. Waiting until
  completion to begin the audit of the capital settlement report means that early-stage records have
  deteriorated, signatories have moved on, subcontractors have been dissolved, and — most importantly —
  <b>underground works can no longer be inspected</b>.</p>
  <p>For large projects the audit is therefore performed <b>in parallel with project execution</b>, in
  phases aligned with construction stages or packages, with the final phase consolidating everything
  into the audit report on the capital settlement report. This does not replace the final report; it
  makes the final report possible.</p>

  <h2 style="margin:30px 0 12px">What this site contains</h2>
  <div class="luoi g2">
    <div class="the"><h3>Legal document register</h3>
      <p>%d instruments currently governing urban railway and TOD — laws, National Assembly resolutions,
      government decrees, ministerial circulars, technical regulations, and resolutions of the Hanoi and
      Ho Chi Minh City People's Councils. Filterable by level, locality, year and validity status.</p></div>
    <div class="the"><h3>Procedure map</h3>
      <p>Nine stages from route planning to capital settlement, each with the deciding authority,
      the governing instruments, the deliverable, and the problems most often encountered.</p></div>
    <div class="the"><h3>Audit of capital settlement reports</h3>
      <p>Thirteen audit sections, two mandatory balancing equations, and the reasoning behind
      parallel auditing for large projects.</p></div>
    <div class="the"><h3>Risk library</h3>
      <p>Common audit risks grouped into eight categories, each with indicators and the audit procedure
      that responds to it. Compiled from general professional experience and public material — not from
      any specific organisation.</p></div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>Contact</h3>
    <p style="margin-top:8px">Telephone and Zalo: <a href="tel:0825092007"><b>+84 82 509 2007</b></a><br>
    ASCO Building, No. 2, Lane 308, Le Trong Tan Street, Phuong Liet Ward, Hanoi</p>
    <p class="small" style="margin-top:10px">Correspondence in English is welcome. Formal deliverables —
    audit reports, valuation certificates — are issued in Vietnamese, with an English translation where
    the engagement requires one.</p>
  </div>

  <p class="small" style="margin-top:22px">This page is general information, not advice on any particular
  project, and is not a legal source. Vietnamese legislation changes frequently — always verify against
  the official gazette text before relying on it.</p>

</div></div>
""" % (gd, N)

    ld = [{"@context": "https://schema.org", "@type": "WebPage",
           "name": "Urban railway projects in Vietnam — legal framework and audit",
           "inLanguage": "en",
           "description": "Reference on Vietnamese urban railway and TOD projects: the nine project stages, the special mechanism, and audit of capital settlement reports."}]
    return than, ld


# ================================================================ TIENG TRUNG
def trang_zh():
    gd = ''.join('<tr><td><b>%d</b></td><td><b>%s</b></td><td>%s</td></tr>' % (i + 1, a, b)
                 for i, (a, b) in enumerate([
        ("线路规划", "将线路纳入省级规划和城市总体规划；确定线路走向、车站与车辆段位置；初步划定TOD区域。"),
        ("投资决策", "编制项目预可行性研究报告，审查资金来源，由有权机关作出投资决策。"),
        ("项目审批", "编制可行性研究报告与基础设计，或按特殊机制编制总体技术设计；审查；批准。批准的总投资额是此后全部结算费用的法定上限。"),
        ("征地拆迁与安置", "土地回收、补偿、支持与安置；分段移交施工场地。"),
        ("承包商选择", "编制招标计划与招标文件，评标，审批，签订合同。"),
        ("施工与造价管理", "后续设计，编制与审批概预算，施工，分阶段验收工程量，付款，处理变更。"),
        ("验收、试运行与系统安全认证", "静态与动态试验，全系统联动试运行，独立第三方系统安全评估，国家验收，颁发运营许可。"),
        ("移交与资产确认", "向运营单位移交工程与档案，确立公共资产所有权，建立资产台账，计提折旧，制定票价与补贴方案。"),
        ("竣工决算", "编制决算报告，独立审计决算报告，审查，批准，处理往来款项与积压物资设备。"),
    ]))

    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">越南语版</a> · 中文</div>
  <h1>越南城市轨道交通项目：法律框架与审计</h1>
  <p>面向项目管理单位、业主、咨询单位与承包商的参考资料，涉及越南地铁及以公共交通为导向的开发项目。</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="nn-bao">
    <b>关于本页。</b>本站主体为越南语，因为所依据的法律文件仅有越南语正式文本。本页概述本站内容，
    并说明外国承包商与咨询单位最容易忽略的几点。
    <a href="../index.html">打开越南语版 →</a>
  </div>

  <h2 style="margin-bottom:12px">外方最常出错的三点</h2>
  <div class="luoi g3">
    <div class="the" style="border-top:3px solid var(--do)">
      <h3>援引已失效的法规</h3>
      <p>越南法律更新频繁。《铁路法》同时存在2017年版与2025年版；《首都法》已于2026年被新法取代。
      一个历时十年的项目会经历两至三代实施细则。</p>
    </div>
    <div class="the" style="border-top:3px solid var(--hoacuc)">
      <h3>误以为特殊机制普遍适用</h3>
      <p>国会决议允许城市轨道交通项目适用简化程序，但<b>仅限河内市与胡志明市</b>，不适用于其他地方。</p>
    </div>
    <div class="the" style="border-top:3px solid var(--ngoc)">
      <h3>EPC合同缺少工程量清单</h3>
      <p>国际总价合同将工程量风险转移给承包商，而越南的竣工决算要求提供已完成工程量的证据。
      建议在签约前将价格构成分析表作为合同附件确定下来。</p>
    </div>
  </div>

  <h2 style="margin:30px 0 12px">项目的九个阶段</h2>
  <div class="bang-boc">
    <table>
      <thead><tr><th style="width:56px">阶段</th><th style="width:22%%">名称</th><th>内容</th></tr></thead>
      <tbody>%s</tbody>
    </table>
  </div>

  <h2 style="margin:30px 0 12px">审计与项目实施同步进行</h2>
  <p>地铁线路的建设周期通常为八至十五年。若等到工程竣工才开始对竣工决算报告进行审计，
  早期凭证已经损毁、签字人已经调离、分包单位已经注销，而最关键的是——<b>地下工程已无法再行查验</b>。</p>
  <p>因此，大型项目的审计<b>与项目实施同步进行</b>，按施工阶段或按标段分批开展，
  最后一批汇总形成竣工决算报告审计报告。同步审计并不取代最终报告，而是使最终报告成为可能。</p>

  <h2 style="margin:30px 0 12px">本站内容</h2>
  <div class="luoi g2">
    <div class="the"><h3>法律文件目录</h3>
      <p>现行调整城市轨道交通与TOD的%d件法律文件——法律、国会决议、政府议定、部级通知、
      技术规范，以及河内市与胡志明市人民议会决议。可按层级、地区、年份与效力状态筛选。</p></div>
    <div class="the"><h3>项目程序图</h3>
      <p>从线路规划到竣工决算共九个阶段，每一阶段列明决定机关、适用法规、成果文件与常见问题。</p></div>
    <div class="the"><h3>竣工决算报告审计</h3>
      <p>十三个审计部分、两个必须核对的平衡等式，以及大型项目采用同步审计的理由。</p></div>
    <div class="the"><h3>风险库</h3>
      <p>常见审计风险分为八类，每项列明识别标志与相应审计程序。内容源自一般职业经验与公开资料，
      不取自任何具体单位。</p></div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>联系方式</h3>
    <p style="margin-top:8px">电话及Zalo：<a href="tel:0825092007"><b>+84 82 509 2007</b></a><br>
    河内市方列坊黎仲晋街308巷2号 ASCO 大厦</p>
    <p class="small" style="margin-top:10px">可用中文联系。正式成果文件——审计报告、估价证书——以越南语出具，
    如约定需要，可另附译文。</p>
  </div>

  <p class="small" style="margin-top:22px">本页为一般性信息，不构成针对具体项目的意见，也不是法律依据。
  越南法律变动频繁，援引前请核对公报正式文本。</p>

</div></div>
""" % (gd, N)

    ld = [{"@context": "https://schema.org", "@type": "WebPage",
           "name": "越南城市轨道交通项目：法律框架与审计",
           "inLanguage": "zh",
           "description": "越南城市轨道交通与TOD项目参考：九个项目阶段、特殊机制，以及竣工决算报告审计。"}]
    return than, ld


# ================================================================ GHI TOAN BO
TRANG = [
    ('',                 'vi', 'Đường sắt đô thị — Văn bản, quy trình, kinh nghiệm QLDA',
     'Tra cứu %d đầu văn bản pháp luật đường sắt đô thị và TOD, quy trình dự án chín giai đoạn, kiểm toán quyết toán và thư viện rủi ro.' % N,
     P.trang_dich, 'ngoai'),
    ('van-ban',          'vi', 'Cập nhật văn bản pháp luật đường sắt đô thị và TOD',
     'Tra cứu %d đầu văn bản: Luật, Nghị quyết Quốc hội, Nghị định, Thông tư, quy chuẩn kỹ thuật và văn bản Hà Nội, TP. Hồ Chí Minh.' % N,
     V3.trang_van_ban, 'trong'),
    ('quy-trinh',        'vi', 'Quy trình thực hiện dự án đường sắt đô thị — chín giai đoạn',
     'Chín giai đoạn từ quy hoạch tuyến đến quyết toán vốn đầu tư, kèm bốn ngăn pháp lý, thẩm quyền quyết định và vướng mắc hay gặp.',
     V2.trang_quy_trinh, 'trong'),
    ('kiem-toan',        'vi', 'Kiểm toán Báo cáo quyết toán dự án hoàn thành',
     'Mười ba phần hành, hai phép cân đối bắt buộc, và vì sao dự án lớn phải kiểm toán song hành cùng quá trình thực hiện dự án.',
     V4.trang_kiem_toan, 'trong'),
    ('thu-vien-rui-ro',  'vi', 'Thư viện rủi ro kiểm toán dự án',
     'Rủi ro thường gặp chia tám nhóm, kèm dấu hiệu nhận biết và thủ tục ứng phó. Tài liệu tham khảo chung, không từ đơn vị nào.',
     V4.trang_rui_ro, 'trong'),
    ('kinh-nghiem',      'vi', 'Kinh nghiệm quản lý dự án đường sắt đô thị',
     'Mười hai việc Ban Quản lý dự án nên làm sớm, danh mục kiểm tra theo thời điểm và ba sai lầm lặp lại nhiều nhất.',
     V2.trang_kinh_nghiem, 'trong'),
    ('vuong-mac',        'vi', 'Mười vướng mắc thường gặp ở dự án đường sắt đô thị',
     'Mười tình huống hay gặp: giải phóng mặt bằng, điều chỉnh tổng mức đầu tư, hợp đồng EPC, quyết toán, TOD — kèm hướng xử lý.',
     V2.trang_vuong_mac, 'trong'),
    ('tu-van',           'vi', 'Gửi yêu cầu tư vấn dự án đường sắt đô thị',
     'Ba loại yêu cầu tư vấn, biểu mẫu gửi và quy trình phản hồi trong 24 giờ làm việc. Nêu rõ nên gửi gì và chưa cần gửi gì.',
     V3.trang_tu_van, 'trong'),
    ('lien-he',          'vi', 'Liên hệ — Đường sắt đô thị',
     'Ba cách liên hệ: biểu mẫu tư vấn, gọi điện, đặt lịch trao đổi. Kèm bảng chọn cách nào cho việc gì.',
     V3.trang_lien_he, 'trong'),
    ('en',               'en', 'Vietnam urban railway — legal framework and audit',
     'Vietnamese urban railway and TOD projects: the nine project stages, the special mechanism for Hanoi and HCMC, and audit of capital settlement reports.',
     trang_en, 'trong'),
    ('zh',               'zh', '越南城市轨道交通项目：法律框架与审计',
     '越南城市轨道交通与TOD项目参考：九个项目阶段、河内与胡志明市的特殊机制，以及竣工决算报告审计。',
     trang_zh, 'trong'),
]


def ghi():
    os.makedirs(B.KHO, exist_ok=True)
    qua = []
    for slug, lang, td, mt, fn, tang in TRANG:
        than, ld = fn()
        h = B.khung(slug, td, mt, than, ld, tang, lang)
        d = os.path.join(B.KHO, slug) if slug else B.KHO
        os.makedirs(d, exist_ok=True)
        io.open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h)
        print('  %-18s %-3s %7d byte   title %2d   desc %3d'
              % (slug or '.', lang, len(h), len(td), len(mt)))
        if len(td) > 60 or len(mt) > 160:
            qua.append((slug or '.', len(td), len(mt)))

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for slug, lang, td, mt, fn, tang in TRANG:
        u = B.GOC + '/' + (slug + '/' if slug else '')
        sm.append('  <url><loc>%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>'
                  % (u, 'weekly' if slug == 'van-ban' else 'monthly', '1.0' if not slug else '0.8'))
    sm.append('</urlset>')
    io.open(os.path.join(B.KHO, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
    io.open(os.path.join(B.KHO, 'robots.txt'), 'w', encoding='utf-8').write(
        'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % B.GOC)
    print('\nDa ghi %d trang + sitemap.xml + robots.txt' % len(TRANG))
    print('Vuot nguong SEO:', qua if qua else 'khong co')


if __name__ == '__main__':
    ghi()
