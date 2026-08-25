# -*- coding: utf-8 -*-
"""Ban 10 — theo yeu cau CEO 25/08:
   1. Duoi logo DUONG SAT DO THI ghi HOTLINE 0825092007 (chi ghi, khong bam)
   2. Nut ngon ngu doi nhan thanh "Chon ngon ngu" (thu tu Viet - Anh - Trung - Nhat - Phap - Duc)
   3. Dong duoi cung: "Van ban duoc cap nhat den <NGAY_CAP_NHAT>"
"""
import io, os, sys
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_v4 as V4
import ds_v6 as V6
import ds_v7 as V7
import ds_v8 as V8
import ds_v9 as V9

# ================================ MOT CHO DUY NHAT DE SUA NGAY CAP NHAT
NGAY_CAP_NHAT = '31/08/2026'
HOTLINE = '0825092007'

# ---- 2. nhan nut ngon ngu
V6._TEN = {'vi': 'Chọn ngôn ngữ', 'en': 'Choose language', 'zh': '选择语言',
           'ja': '言語を選択', 'fr': 'Choisir la langue', 'de': 'Sprache wählen'}

B.CSS += r"""
/* ---------- Hotline duoi logo ---------- */
.hieu i{display:block!important;font-size:10.6px;color:var(--do);letter-spacing:.09em;
  font-weight:800;margin-top:1px}
@media(max-width:1400px){.hieu i{display:block}}
@media(max-width:430px){.hieu i{font-size:9.8px;letter-spacing:.05em}}

/* ---------- Dong ngay cap nhat o chan trang ---------- */
.ft-cuoi .ngay{display:block;margin-top:5px;font-weight:700;color:var(--chu)}
"""

_LOGO_CU = '<i>Văn bản · Quy trình · Kinh nghiệm</i>'
_LOGO_MOI = '<i>Hotline: %s</i>' % HOTLINE

_FT_CU = ('<div class="ft-cuoi">Bản quyền của Hãng Kiểm toán và Định giá ASCO · '
          'Nội dung biên soạn từ kho văn bản pháp luật nội bộ, cập nhật 24/08/2026.</div>')
_FT_MOI = ('<div class="ft-cuoi">Bản quyền của Hãng Kiểm toán và Định giá ASCO · '
           'Nội dung biên soạn từ kho văn bản pháp luật nội bộ.'
           '<span class="ngay">Văn bản được cập nhật đến %s.</span></div>' % NGAY_CAP_NHAT)

_V6_KHUNG = V6.khung


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = _V6_KHUNG(slug, tieude, mota, than, jsonld, tang, lang)
    for cu, moi in ((_LOGO_CU, _LOGO_MOI), (_FT_CU, _FT_MOI)):
        if cu not in h:
            raise SystemExit('KHONG TIM THAY CHUOI CAN THAY: %r' % cu[:60])
        h = h.replace(cu, moi, 1)
    return h


B.khung = khung

TRANG = V9.TRANG


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
