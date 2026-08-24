# -*- coding: utf-8 -*-
"""Ban 6 — theo yeu cau CEO 24/08:
   1. Logo IN HOA, khong vo dong
   2. Sau ngon ngu: Viet Anh Trung Nhat Phap Duc, dang NUT SO XUONG
   3. Trang van ban: hien SO HIEU thanh cot rieng
"""
import io, os, sys, html, json
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
import ds_v5 as V5

TM = os.path.dirname(os.path.abspath(__file__))
VB = json.load(io.open(os.path.join(TM, 'vb_phanloai.json'), encoding='utf-8'))
N = len(VB)

# ---- rut gon nhan menu cho vua thanh dau
B.NAV = [
    ('van-ban',         'Văn bản'),
    ('quy-trinh',       'Quy trình'),
    ('kiem-toan',       'Kiểm toán QT'),
    ('thu-vien-rui-ro', 'Thư viện rủi ro'),
    ('kinh-nghiem',     'Kinh nghiệm'),
    ('vuong-mac',       'Vướng mắc'),
    ('tu-van',          'Tư vấn'),
    ('lien-he',         'Liên hệ'),
]

# ================================================================ 1. LOGO + 2. NGON NGU
B.CSS += r"""
/* ---------- LOGO: in hoa, khong vo dong ---------- */
.hieu{flex:0 0 auto;white-space:nowrap}
.hieu b{font-size:16.4px;letter-spacing:.055em;text-transform:uppercase;white-space:nowrap}
.hieu i{white-space:nowrap;font-size:10.4px}
@media(max-width:1180px){.hieu b{font-size:15.2px;letter-spacing:.04em}}
/* thanh dau chat vi co 8 muc + nut ngon ngu: siet khoang cach, an dong phu */
.top-nav{gap:13px}
.top-nav a{font-size:14.2px}
@media(max-width:1400px){.hieu i{display:none}}
@media(max-width:520px){
  .hieu b{font-size:13.4px;letter-spacing:0}
  .hieu svg{width:27px;height:27px}
  .hieu{gap:8px}
  .top-in{gap:9px;padding-left:16px;padding-right:16px}
}
@media(max-width:390px){.hieu b{font-size:12.6px}}

/* ---------- NGON NGU: nut so xuong ---------- */
.nn{position:relative;flex:0 0 auto}
.nn>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:7px;
  border:1px solid var(--vien);border-radius:999px;padding:7px 13px;background:var(--nen2);
  font-size:13.4px;font-weight:700;color:var(--chu);white-space:nowrap;user-select:none}
.nn>summary::-webkit-details-marker{display:none}
.nn>summary:hover{border-color:var(--muc3);color:var(--muc)}
.nn>summary .cau{font-size:11.6px;opacity:.7;transition:transform .15s}
.nn[open]>summary .cau{transform:rotate(180deg)}
.nn>summary .qc{width:15px;height:15px;flex:0 0 auto;stroke:currentColor;fill:none;stroke-width:1.9}
.nn-menu{position:absolute;top:calc(100% + 7px);right:0;z-index:80;min-width:196px;
  background:var(--the);border:1px solid var(--vien);border-radius:12px;padding:6px;
  box-shadow:0 12px 34px rgba(14,23,41,.18)}
:root[data-theme="dark"] .nn-menu{box-shadow:0 12px 34px rgba(0,0,0,.5)}
.nn-menu a{display:flex;align-items:center;justify-content:space-between;gap:12px;
  padding:9px 12px;border-radius:8px;font-size:14.4px;font-weight:600;color:var(--chu);
  text-decoration:none;white-space:nowrap}
.nn-menu a:hover{background:var(--nen2);color:var(--muc)}
.nn-menu a[aria-current]{background:var(--muc);color:#fff}
:root[data-theme="dark"] .nn-menu a[aria-current]{color:#0D2044}
.nn-menu a .ma{font-size:11.6px;font-weight:800;letter-spacing:.06em;opacity:.65}
.nn-menu a[aria-current] .ma{opacity:.9}
@media(max-width:1160px){.nn{order:1;margin-right:8px}}
@media(max-width:420px){.nn>summary{padding:6px 10px;font-size:12.6px}
  .nn>summary .nhan{display:none}}

/* ---------- BANG VAN BAN: cot so hieu ---------- */
.sohieu{font-family:Consolas,"Courier New",monospace;font-size:13.4px;font-weight:700;
  color:var(--muc);white-space:nowrap}
td.tenvb{line-height:1.45}
td.tenvb .phu{display:block;font-size:12.8px;color:var(--chu2);margin-top:2px}
"""

NGON_NGU = [
    ('vi', 'VI', 'Tiếng Việt',  ''),
    ('en', 'EN', 'English',     'en/'),
    ('zh', 'ZH', '中文',         'zh/'),
    ('ja', 'JA', '日本語',       'ja/'),
    ('fr', 'FR', 'Français',    'fr/'),
    ('de', 'DE', 'Deutsch',     'de/'),
]
_TEN = {m: t for m, _, t, _ in NGON_NGU}
_NHAN_NUT = {'vi': 'Ngôn ngữ', 'en': 'Language', 'zh': '语言', 'ja': '言語',
             'fr': 'Langue', 'de': 'Sprache'}

_CAU = ('<svg class="qc" viewBox="0 0 24 24" aria-hidden="true">'
        '<circle cx="12" cy="12" r="9"/><path d="M3.6 9h16.8M3.6 15h16.8"/>'
        '<path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18z"/></svg>')


def _bo_ngon_ngu(slug, lang='vi'):
    muc = []
    for ma, kyhieu, ten, thumuc in NGON_NGU:
        if lang == 'vi':
            goc = '../' if slug else ''
            dich = (goc + 'index.html') if ma == 'vi' else (goc + thumuc + 'index.html')
        else:
            dich = '../index.html' if ma == 'vi' else ('../' + thumuc + 'index.html')
        cur = ' aria-current="true"' if ma == lang else ''
        muc.append('<a href="%s" hreflang="%s"%s><span>%s</span><span class="ma">%s</span></a>'
                   % (dich, ma, cur, html.escape(ten), kyhieu))
    return ('<details class="nn"><summary aria-label="%s">%s'
            '<span class="nhan">%s</span><span class="cau">▾</span></summary>'
            '<div class="nn-menu">%s</div></details>'
            % (html.escape(_NHAN_NUT[lang]), _CAU,
               html.escape(_TEN[lang]), ''.join(muc)))


def khung(slug, tieude, mota, than, jsonld=None, tang='trong', lang='vi'):
    h = V4._khung_goc(slug, tieude, mota, than, jsonld, tang)
    h = h.replace('</nav>', '</nav>' + chr(10) + '    ' + _bo_ngon_ngu(slug, lang), 1)
    if lang != 'vi':
        h = h.replace('<html lang="vi">', '<html lang="%s">' % lang, 1)
    # dong nut so xuong khi bam ra ngoai
    h = h.replace('</body>', """<script>
(function(){document.addEventListener('click',function(e){
 document.querySelectorAll('details.nn[open]').forEach(function(d){
  if(!d.contains(e.target)) d.removeAttribute('open');});});
 document.addEventListener('keydown',function(e){ if(e.key==='Escape')
  document.querySelectorAll('details.nn[open]').forEach(function(d){d.removeAttribute('open');});});
})();
</script>
</body>""", 1)
    return h


B.khung = khung


# ================================================================ 3. TRANG VAN BAN CO SO HIEU
def trang_van_ban():
    LOP = {'Luật & Nghị quyết QH': 'tl-luat', 'Nghị định': 'tl-nd',
           'Thông tư': 'tl-tt', 'Văn bản khác': 'tl-khac'}
    hang = []
    for d in sorted(VB, key=lambda x: (x['ngan'], x['hien'])):
        tt = ('<span class="the-loc" style="background:var(--do-nen);color:var(--do)">Hết hiệu lực</span>'
              if d['hethieuluc'] else
              '<span class="the-loc" style="background:var(--ngoc-nen);color:var(--ngoc)">Còn hiệu lực</span>')
        hn = ' <span class="the-loc tl-tt">Hợp nhất</span>' if d['hopnhat'] else ''
        dd = ' · '.join(x.upper() for x in d['dinhdang'])
        phu = ('<span class="phu">%s</span>' % html.escape(d['diaban'])
               if d['diaban'] != 'Toàn quốc' else '')
        hang.append(
            '<tr data-ngan="%s" data-dia="%s" data-nam="%s" data-tt="%s" data-tim="%s">'
            '<td><span class="the-loc %s">%s</span></td>'
            '<td class="sohieu">%s</td>'
            '<td class="tenvb">%s%s%s</td>'
            '<td>%s</td><td>%s</td><td class="dinh">%s</td></tr>'
            % (html.escape(d['ngan']), html.escape(d['diaban']), d['nam'],
               'het' if d['hethieuluc'] else 'con',
               html.escape(P2.bo_dau(d['hien'] + ' ' + d.get('ten_dep','') + ' ' + d['diaban'] + ' ' + d.get('sohieu',''))),
               LOP[d['ngan']], html.escape(d['ngan'].replace(' & Nghị quyết QH', '')),
               html.escape(d.get('sohieu') or '—'),
               html.escape(d.get('ten_dep') or d['ten_ngan'] or d['hien']), hn, phu,
               d['nam'] or '—', tt, dd))

    nams = sorted({d['nam'] for d in VB if d['nam']}, reverse=True)
    opt = lambda xs: ''.join('<option>%s</option>' % html.escape(x) for x in xs)

    than, ld = V3.trang_van_ban()
    # thay ca khoi bang bang bang moi co cot So hieu
    import re
    bang_moi = """<div class="bang-boc">
    <table id="bang">
      <thead><tr><th style="width:104px">Cấp</th><th style="width:142px">Số hiệu</th>
      <th>Tên văn bản</th><th style="width:62px">Năm</th>
      <th style="width:114px">Hiệu lực</th><th style="width:88px">Định dạng</th></tr></thead>
      <tbody>%s</tbody>
    </table>
  </div>""" % '\n'.join(hang)
    than = re.sub(r'<div class="bang-boc">\s*<table id="bang">.*?</table>\s*</div>',
                  bang_moi, than, count=1, flags=re.S)
    return than, ld


print('ds_v6: logo in hoa, 6 ngon ngu dang nut so xuong, bang co cot So hieu.')
