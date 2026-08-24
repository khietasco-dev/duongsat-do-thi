# -*- coding: utf-8 -*-
"""Ban 8 — bam vao van ban la MO DUOC tep Word hoac PDF."""
import io, os, sys, html, json, re
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ds_build as B
import ds_pages as P
import ds_pages2 as P2
import ds_v2 as V2
import ds_v3 as V3
import ds_v4 as V4
import ds_v5 as V5
import ds_v6 as V6
import ds_v7 as V7

TM = os.path.dirname(os.path.abspath(__file__))
VB = json.load(io.open(os.path.join(TM, 'vb_phanloai.json'), encoding='utf-8'))
N = len(VB)

B.CSS += r"""
/* ---------- lien ket mo tep ---------- */
td.tenvb a.mo{color:var(--chu);text-decoration:none;border-bottom:1px solid transparent}
td.tenvb a.mo:hover{color:var(--muc);border-bottom-color:var(--muc3)}
td.tenvb a.mo::after{content:"↗";font-size:11.4px;margin-left:5px;color:var(--nhan2);
  vertical-align:super;opacity:.75}
.tep{display:flex;flex-wrap:wrap;gap:5px;align-items:center}
.tep a{display:inline-block;font-size:11.8px;font-weight:800;letter-spacing:.04em;
  padding:3px 8px;border-radius:6px;text-decoration:none;white-space:nowrap;line-height:1.5}
.tep a.w{background:var(--nen3);color:var(--muc)}
.tep a.w:hover{background:var(--muc);color:#fff}
:root[data-theme="dark"] .tep a.w:hover{color:#0D2044}
.tep a.p{background:var(--do-nen);color:var(--do)}
.tep a.p:hover{background:var(--do);color:#fff}
.tep .ghi{font-size:11.4px;color:var(--chu2);white-space:nowrap}
"""


def _lk(x, lop, nhan):
    mb = x['byte'] / 1048576
    kt = ('%.1f MB' % mb) if mb >= 1 else ('%.0f KB' % (x['byte'] / 1024))
    return '<a class="%s" href="%s" title="%s · %s" target="_blank" rel="noopener">%s</a>' % (
        lop, html.escape(x['duong_dan']), html.escape(nhan), kt, html.escape(nhan))


def o_tep(d):
    """O cot Dinh dang: cac nut bam mo tep."""
    w, p = d['tep']['word'], d['tep']['pdf']
    ra = []
    if len(w) == 1:
        ra.append(_lk(w[0], 'w', w[0]['duoi'].upper()))
    elif len(w) > 1:
        ra += [_lk(x, 'w', 'W%d' % (i + 1)) for i, x in enumerate(w)]
    if len(p) == 1:
        ra.append(_lk(p[0], 'p', 'PDF'))
    elif len(p) > 1:
        ra += [_lk(x, 'p', 'P%d' % (i + 1)) for i, x in enumerate(p)]
    if not ra:
        return '<span class="ghi">—</span>'
    ghi = ''
    if len(w) > 1 or len(p) > 1:
        ghi = '<span class="ghi">%d phần</span>' % max(len(w), len(p))
    return '<div class="tep">%s%s</div>' % (''.join(ra), ghi)


def trang_van_ban():
    LOP = {'Luật & Nghị quyết QH': 'tl-luat', 'Nghị định': 'tl-nd',
           'Thông tư': 'tl-tt', 'Văn bản khác': 'tl-khac'}
    hang = []
    for d in sorted(VB, key=lambda x: (x['ngan'], x['hien'])):
        tt = ('<span class="the-loc" style="background:var(--do-nen);color:var(--do)">Hết hiệu lực</span>'
              if d['hethieuluc'] else
              '<span class="the-loc" style="background:var(--ngoc-nen);color:var(--ngoc)">Còn hiệu lực</span>')
        hn = ' <span class="the-loc tl-tt">Hợp nhất</span>' if d['hopnhat'] else ''
        phu = ('<span class="phu">%s</span>' % html.escape(d['diaban'])
               if d['diaban'] != 'Toàn quốc' else '')
        ten = html.escape(d.get('ten_dep') or d['ten_ngan'] or d['hien'])
        # ten bam duoc: uu tien Word, khong co thi PDF
        uu = (d['tep']['word'] or d['tep']['pdf'])
        if uu:
            ten = ('<a class="mo" href="%s" target="_blank" rel="noopener" '
                   'title="Mở văn bản">%s</a>' % (html.escape(uu[0]['duong_dan']), ten))
        hang.append(
            '<tr data-ngan="%s" data-dia="%s" data-nam="%s" data-tt="%s" data-tim="%s">'
            '<td><span class="the-loc %s">%s</span></td>'
            '<td class="sohieu">%s</td>'
            '<td class="tenvb">%s%s%s</td>'
            '<td>%s</td><td>%s</td><td>%s</td></tr>'
            % (html.escape(d['ngan']), html.escape(d['diaban']), d['nam'],
               'het' if d['hethieuluc'] else 'con',
               html.escape(P2.bo_dau(d['hien'] + ' ' + d.get('ten_dep', '') + ' '
                                     + d['diaban'] + ' ' + d.get('sohieu', ''))),
               LOP[d['ngan']], html.escape(d['ngan'].replace(' & Nghị quyết QH', '')),
               html.escape(d.get('sohieu') or '—'),
               ten, hn, phu,
               d['nam'] or '—', tt, o_tep(d)))

    than, ld = V3.trang_van_ban()
    bang_moi = """<div class="bang-boc">
    <table id="bang">
      <thead><tr><th style="width:104px">Cấp</th><th style="width:142px">Số hiệu</th>
      <th>Tên văn bản</th><th style="width:62px">Năm</th>
      <th style="width:114px">Hiệu lực</th><th style="width:130px">Mở tệp</th></tr></thead>
      <tbody>%s</tbody>
    </table>
  </div>""" % '\n'.join(hang)
    than = re.sub(r'<div class="bang-boc">\s*<table id="bang">.*?</table>\s*</div>',
                  bang_moi, than, count=1, flags=re.S)

    # doi khoi huong dan cho khop
    than = than.replace(
        """<div class="b"><b>Đọc cột Định dạng</b>
      <span>DOC hoặc DOCX là bản Word chỉnh sửa, trích dẫn được. Chỉ có PDF nghĩa là nguồn chính thức
      không phát hành bản Word.</span></div>""",
        """<div class="b"><b>Bấm vào tên là mở văn bản</b>
      <span>Bấm tên văn bản để mở bản Word; văn bản nào không có bản Word thì mở bản PDF.
      Cột <b>Mở tệp</b> cho chọn từng định dạng.</span></div>""")
    than = than.replace(
        """<div class="b"><b>Lọc chồng nhiều điều kiện</b>""",
        """<div class="b"><b>Văn bản dài chia nhiều phần</b>
      <span>Công báo đăng văn bản dài thành nhiều kỳ. Những văn bản đó hiện <b>W1 W2…</b> hoặc
      <b>P1 P2…</b> — phải mở hết các phần mới đủ nội dung.</span></div>
    <div class="b"><b>Lọc chồng nhiều điều kiện</b>""")
    return than, ld


# ---------------------------------------------------------------- ghi
TRANG = [(s, l, td, mt, (trang_van_ban if s == 'van-ban' else fn), tang)
         for s, l, td, mt, fn, tang in V7.TRANG]


def ghi():
    V7.TRANG = TRANG
    V7.ghi()


if __name__ == '__main__':
    ghi()
