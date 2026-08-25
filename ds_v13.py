# -*- coding: utf-8 -*-
"""Ban 13 — DONG BO NGON NGU CHO THANH MENU.

CEO phat hien 25/08: bam sang trang tieng Anh thi menu tren cung van tieng Viet.
Ban nay dich toan bo nhan menu + bang so xuong "Dich vu cung cap" sang 6 thu tieng.

Nguyen tac trung thuc: cac trang dich den VAN LA TIENG VIET (chi 6 trang tong quan
la co ban dich). Nen tren trang ngoai ngu, moi lien ket menu duoc gan hreflang="vi"
va mot dau "VI" nho — de nguoi doc biet truoc, khong bam vao roi moi ngac nhien.
"""
import os, re, sys, html
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v7 as V7
import ds_v12 as V12
from ds_dv import DICH_VU, NHOM

# ---------------------------------------------------------------- nhan menu
# Nhan tieng Viet la KHOA — phai khop tung chu voi ban dang chay.
NHAN = {
    'van-ban': dict(vi='Văn bản', en='Documents', zh='法规文件', ja='法令集',
                    fr='Textes', de='Vorschriften'),
    'quy-trinh': dict(vi='Quy trình', en='Process', zh='项目流程', ja='手順',
                      fr='Processus', de='Ablauf'),
    'kiem-toan': dict(vi='Kiểm toán QT', en='Audit', zh='竣工审计', ja='決算監査',
                      fr='Audit', de='Prüfung'),
    'thu-vien-rui-ro': dict(vi='Thư viện rủi ro', en='Risk library', zh='风险库',
                            ja='リスク集', fr='Risques', de='Risiken'),
    'kinh-nghiem': dict(vi='Kinh nghiệm', en='Experience', zh='管理经验', ja='実務経験',
                        fr='Expérience', de='Erfahrung'),
    'vuong-mac': dict(vi='Vướng mắc', en='Issues', zh='常见问题', ja='課題',
                      fr='Problèmes', de='Probleme'),
    'tu-van': dict(vi='Tư vấn', en='Advice', zh='咨询', ja='相談',
                   fr='Conseil', de='Beratung'),
    'lien-he': dict(vi='Liên hệ', en='Contact', zh='联系我们', ja='お問い合わせ',
                    fr='Contact', de='Kontakt'),
}

NHAN_DV = dict(vi='Dịch vụ cung cấp', en='Services', zh='服务项目', ja='サービス',
               fr='Services', de='Leistungen')
NHAN_TAT = dict(vi='Tất cả dịch vụ', en='All services', zh='全部服务', ja='サービス一覧',
                fr='Tous les services', de='Alle Leistungen')

NHAN_NHOM = {
    'tc': dict(vi='Tài chính và thu hồi vốn', en='Finance and capital recovery',
               zh='财务与资金回收', ja='財務・資金回収',
               fr='Finance et récupération', de='Finanzen und Rückfluss'),
    'qt': dict(vi='Quản trị Ban quản lý dự án', en='PMU governance',
               zh='项目管理单位治理', ja='事業管理組織の統治',
               fr='Gouvernance de l’unité de gestion', de='Steuerung der Projektleitung'),
    'tk': dict(vi='Thuế và năng lực', en='Tax and capability',
               zh='税务与能力建设', ja='税務と人材育成',
               fr='Fiscalité et compétences', de='Steuern und Kompetenz'),
}

NHAN_MUC_DV = {
    'thu-hoi-von-tod': dict(en='Capital recovery from TOD land', zh='TOD 土地资金回收',
                            ja='TOD用地からの資金回収', fr='Récupération par le foncier TOD',
                            de='Rückfluss über TOD-Flächen'),
    'phuong-an-tai-chinh': dict(en='Financial plan for the line', zh='线路财务方案',
                                ja='路線の財務計画', fr='Plan financier de la ligne',
                                de='Finanzierungsplan der Linie'),
    'co-cau-nguon-von': dict(en='Funding structure', zh='资金来源结构', ja='資金構成',
                             fr='Structure de financement', de='Finanzierungsstruktur'),
    'suat-von-dau-tu': dict(en='Investment rates and norms', zh='投资单价与定额换算',
                            ja='投資原単位と歩掛換算', fr='Ratios et normes de coût',
                            de='Investitionskennwerte und Normen'),
    'kiem-soat-noi-bo': dict(en='Internal control for the PMU', zh='项目管理单位内部控制',
                             ja='事業管理組織の内部統制', fr='Contrôle interne de l’unité',
                             de='Interne Kontrolle der Projektleitung'),
    'ho-so-quyet-toan': dict(en='Settlement records from day one', zh='竣工决算档案管理',
                             ja='決算書類の管理', fr='Dossiers de décompte final',
                             de='Abrechnungsunterlagen'),
    'tai-co-cau-doanh-nghiep': dict(en='Corporate restructuring', zh='项目公司与运营单位重组',
                                    ja='事業会社・運営組織の再編',
                                    fr='Restructuration des sociétés',
                                    de='Umstrukturierung der Gesellschaften'),
    'thue-du-an': dict(en='Tax for the project', zh='项目税务', ja='事業の税務',
                       fr='Fiscalité du projet', de='Steuern im Projekt'),
    'boi-duong-can-bo': dict(en='Training for PMU staff', zh='项目管理人员培训',
                             ja='事業管理職員の研修', fr='Formation des agents',
                             de='Schulung der Mitarbeitenden'),
}

# cau nhac "trang dich den la tieng Viet"
NHAC = dict(en='page in Vietnamese', zh='越南语页面', ja='ベトナム語のページ',
            fr='page en vietnamien', de='Seite auf Vietnamesisch')

B.CSS += r"""
/* ---------- dau "VI" tren trang ngoai ngu: bao truoc trang dich den la tieng Viet ---------- */
.top-nav a.vi-dich::after{content:"VI";font-size:8.6px;font-weight:800;letter-spacing:.06em;
  vertical-align:super;margin-left:3px;opacity:.62;color:var(--nhan2)}
.top-nav .nut-lh.vi-dich::after{color:#fff;opacity:.75}
:root[data-theme="dark"] .top-nav .nut-lh.vi-dich::after{color:#0D2044}
.dv-menu a.vi-dich::after{content:"VI";font-size:9px;font-weight:800;vertical-align:super;
  margin-left:4px;opacity:.55}
"""

_V12_KHUNG = V12.khung
_NAV = re.compile(r'<nav class="top-nav" id="dhuong">.*?</nav>', re.S)


def _dich_nav(nav, lang):
    """Doi nhan menu sang ngon ngu khac + danh dau lien ket tro toi trang tieng Viet."""
    # 1. tam mucs menu chinh
    for slug, bo in NHAN.items():
        cu, moi = bo['vi'], bo[lang]
        neo = '>%s</a>' % html.escape(cu)
        if neo not in nav:
            raise SystemExit('KHONG THAY nhan menu %r trong thanh dieu huong' % cu)
        nav = nav.replace(neo, '>%s</a>' % html.escape(moi), 1)

    # 2. nut so xuong + cac muc ben trong
    nav = nav.replace('<summary>%s<' % html.escape(NHAN_DV['vi']),
                      '<summary>%s<' % html.escape(NHAN_DV[lang]), 1)
    nav = nav.replace('>%s</a>' % html.escape(NHAN_TAT['vi']),
                      '>%s</a>' % html.escape(NHAN_TAT[lang]), 1)
    for ma, bo in NHAN_NHOM.items():
        nav = nav.replace('>%s</div>' % html.escape(bo['vi']),
                          '>%s</div>' % html.escape(bo[lang]), 1)
    for d in DICH_VU:
        cu = html.escape(d['menu'])
        moi = html.escape(NHAN_MUC_DV[d['slug']][lang])
        if '>%s</a>' % cu not in nav:
            raise SystemExit('KHONG THAY muc dich vu %r' % d['menu'])
        nav = nav.replace('>%s</a>' % cu, '>%s</a>' % moi, 1)

    # 3. moi lien ket deu tro toi trang tieng Viet — noi ro ra
    nhac = html.escape(NHAC[lang])
    nav = re.sub(r'<a (?!hreflang)', '<a hreflang="vi" title="%s" ' % nhac, nav)
    nav = nav.replace('<a hreflang="vi" title="%s" class="' % nhac,
                      '<a hreflang="vi" title="%s" class="vi-dich ' % nhac)
    nav = nav.replace('<a hreflang="vi" title="%s" href=' % nhac,
                      '<a hreflang="vi" title="%s" class="vi-dich" href=' % nhac)
    return nav


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V12_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    if lang == 'vi':
        return h
    m = _NAV.search(h)
    if not m:
        raise SystemExit('KHONG TIM THAY thanh dieu huong (slug=%r)' % slug)
    return h[:m.start()] + _dich_nav(m.group(0), lang) + h[m.end():]


B.khung = khung
TRANG = V12.TRANG


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
