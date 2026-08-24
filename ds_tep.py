# -*- coding: utf-8 -*-
"""Chep 110 tep van ban vao trang va lap ban do so hieu -> tep.

Chay mot lan. Sau do ds_v8 dung ban do nay de tao lien ket bam mo duoc.
"""
import io, os, re, json, shutil, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

KHO_VB = (r'C:\Users\Public\BO NAO\BO NAO THANH KHIET\NGUYỄN THANH KHIẾT - BRAIN TRI THỨC'
          r'\📚 KHO TRI THỨC\📥 HỘP NẠP\07 - Đọc & Học 📖\111 VBPL\VBPL theo chu de'
          r'\VBPL Duong sat do thi')
SITE = r'C:\Users\Public\BO NAO\duongsat-do-thi'
DICH = os.path.join(SITE, 'van-ban', 'tep')
TM = os.path.dirname(os.path.abspath(__file__))

NGAN = {'01 - Luat': 'luat', '02 - Nghi dinh': 'nghi-dinh',
        '03 - Thong tu': 'thong-tu', '04 - Van ban khac': 'khac'}


def dai(p):
    """Duong dan dai qua 260 ky tu tren Windows."""
    p = os.path.abspath(p)
    return '\\\\?\\' + p if not p.startswith('\\\\?\\') else p


def gon(s):
    """Ten tep an toan cho URL: bo dau, thay khoang trang."""
    s = s.replace('đ', 'd').replace('Đ', 'D')
    s = ''.join(c for c in unicodedata.normalize('NFD', s)
                if unicodedata.category(c) != 'Mn')
    s = re.sub(r'[^A-Za-z0-9._-]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')


def goc_ten(b):
    """Bo hau to '- Phan N' de gom cac phan cua cung mot van ban."""
    return re.sub(r'\s*-\s*[Pp]han\s*\d+\s*$', '', b).strip()


def main():
    vb = json.load(io.open(os.path.join(TM, 'vb_phanloai.json'), encoding='utf-8'))
    # ban do: ten goc (nhu trong vb['hien'] truoc khi lam dep) -> danh sach tep
    theo_ten = {}
    tong_byte = 0
    for ngan_goc, ngan_moi in NGAN.items():
        src = os.path.join(KHO_VB, ngan_goc)
        dst = os.path.join(DICH, ngan_moi)
        os.makedirs(dai(dst), exist_ok=True)
        for f in sorted(os.listdir(dai(src))):
            if f.lower().endswith('.md'):
                continue
            b, e = os.path.splitext(f)
            ten_moi = gon(b) + e.lower()
            p_src, p_dst = os.path.join(src, f), os.path.join(dst, ten_moi)
            if not os.path.exists(dai(p_dst)):
                shutil.copy2(dai(p_src), dai(p_dst))
            kb = os.path.getsize(dai(p_dst))
            tong_byte += kb
            theo_ten.setdefault(goc_ten(b), []).append({
                'duong_dan': 'tep/%s/%s' % (ngan_moi, ten_moi),
                'duoi': e.lower().lstrip('.'),
                'byte': kb,
                'phan': b[len(goc_ten(b)):].strip(' -') or '',
            })

    # gan vao tung van ban
    thieu = []
    for d in vb:
        ds = theo_ten.get(goc_ten(d['ten']))
        if not ds:
            # thu doi chieu bang ten hien
            ds = theo_ten.get(goc_ten(d['hien']))
        if ds:
            # uu tien Word truoc, roi PDF; trong moi nhom giu thu tu phan
            w = sorted([x for x in ds if x['duoi'] in ('doc', 'docx')], key=lambda x: x['phan'])
            p = sorted([x for x in ds if x['duoi'] == 'pdf'], key=lambda x: x['phan'])
            d['tep'] = {'word': w, 'pdf': p}
        else:
            d['tep'] = {'word': [], 'pdf': []}
            thieu.append(d['sohieu'])

    io.open(os.path.join(TM, 'vb_phanloai.json'), 'w', encoding='utf-8').write(
        json.dumps(vb, ensure_ascii=False, indent=1))

    co_word = sum(1 for d in vb if d['tep']['word'])
    co_pdf = sum(1 for d in vb if d['tep']['pdf'])
    nhieu_phan = [(d['sohieu'], len(d['tep']['pdf']) or len(d['tep']['word']))
                  for d in vb if max(len(d['tep']['pdf']), len(d['tep']['word'])) > 1]
    print('Da chep %d tep, %.0f MB' % (
        sum(len(v) for v in theo_ten.values()), tong_byte / 1048576))
    print('Van ban co ban Word : %d/%d' % (co_word, len(vb)))
    print('Van ban co ban PDF  : %d/%d' % (co_pdf, len(vb)))
    print('Khong khop tep      :', thieu if thieu else 'khong co')
    print('Van ban nhieu phan  :', nhieu_phan)


if __name__ == '__main__':
    main()
