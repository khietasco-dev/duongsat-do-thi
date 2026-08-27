# -*- coding: utf-8 -*-
"""Ban TIENG DUC: trang QUY TRINH (Ablauf) va KIEM TOAN QT (Schlussabrechnungsprüfung).

Ten van ban phap luat GIU NGUYEN so hieu tieng Viet — do la ten chinh thuc.
Phan dien giai la cach doc cua ASCO, khong phai ban dich chinh thuc.

🔴🔴 BAY DON VI TIEN NGUY HIEM NHAT CUA TIENG DUC — DOC KY TRUOC KHI VIET SO:

  **"Billion" trong tieng Duc = 10^12**, KHONG phai 10^9 nhu tieng Anh.
  Viet "1 Billion VND" cho "1 ty dong" la **SAI 1.000 LAN**.

  | Viet          | Duc                  | KHONG duoc viet     |
  |---------------|----------------------|---------------------|
  | 1 ty dong     | 1 Milliarde VND      | ~~1 Billion VND~~   |
  | 5 ty dong     | 5 Milliarden VND     | ~~5 Billion VND~~   |
  | 120 ty dong   | 120 Milliarden VND   |                     |
  | 1.000 ty dong | 1 Billion VND        | ~~1 Trillion VND~~  |
  | 10.000 ty     | 10 Billionen VND     |                     |

  Bay nay cung ho voi 亿 cua tieng Trung (= 100 trieu) va 億 cua tieng Nhat.
  Ban tieng Anh dung "Billion VND" nghia la TY — dich thang sang Duc la sai 1.000 lan.

Dau thap phan tieng Duc la DAU PHAY: 0,3375%. Phan cach nghin la DAU CHAM: 445.500.000.
toLocaleString('de-DE') tu lam dung.
"""

# =================================================================== QUY TRINH
QT = dict(
    td='Ablauf eines städtischen Schienenbahnvorhabens — neun Phasen',
    mt='Die neun Phasen eines Metrovorhabens in Vietnam: was geschieht, wer entscheidet, '
       'welche Vorschriften gelten und wo die Unterlagen scheitern.',
    duong='Ablauf',
    h1='Die neun Phasen eines städtischen Schienenbahnvorhabens',
    lede='Diese Seite verfolgt eine Linie von dem Moment an, in dem sie in die Landesplanung '
         'aufgenommen wird, bis zu dem Tag, an dem ihre Schlussabrechnung genehmigt wird. '
         'Zu jeder Phase: die Arbeit selbst, wer entscheidungsbefugt ist, die maßgeblichen '
         'Vorschriften, die entstehenden Unterlagen und die Stelle, an der Unterlagen am '
         'häufigsten scheitern. Die Reihenfolge ist von der Schlussabrechnung her rückwärts '
         'gedacht — denn was eine Phase nicht festhält, ist genau das, was sich Jahre später '
         'nicht abrechnen lässt.',
    h_gd='Die neun Phasen',
    l_viec='Was geschieht', l_tq='Wer entscheidet', l_cc='Maßgebliche Vorschriften',
    l_kq='Was entsteht', l_bay='Wo es üblicherweise scheitert',
    h_ngan='Vier Rechtsstränge — den richtigen lesen',
    ngan_lede='Ein Schienenbahnvorhaben unterliegt nicht einem einzigen Regelwerk. '
              'Welcher Strang gilt, entscheidet darüber, welche Verfahrensschritte verkürzt '
              'werden dürfen und welche nicht. Wer sich hier zu Beginn irrt, zahlt später teuer.',
    l_pv='Anwendungsbereich', l_vb='Vorschriften',
    h_ho='Drei Stellen, an denen der Mechanismus noch offen ist',
    ho_lede='Das sind keine Lücken unserer Recherche. Es sind Bestimmungen, die auf ein weiteres '
            'Dokument verweisen, das noch nicht erlassen wurde. Solange es fehlt, lässt sich die '
            'Sache nicht beziffern — und ein Vorhaben, das etwas anderes unterstellt, baut auf Sand.',
    h_ke='Wo die Prüfung ansetzt',
    ke='In den Phasen sechs bis neun sollte die Prüferin oder der Prüfer bereits vor Ort sein '
       'und nicht am Ende warten. Warum das so ist und wie sich die Arbeit aufteilt, steht '
       'unter %s.',
    ke_lk='Schlussabrechnungsprüfung',
)

# 9 giai doan: (ten, viec, tham quyen, can cu, ket qua, cai bay)
QT_GD = [
    ('Planung und Trassenkonzept',
     'Aufnahme der Linie in die Landesplanung und den Flächennutzungsplan; Festlegung der '
     'Trasse sowie der Standorte von Stationen und Betriebshof; Erstellung der Trassenvariante; '
     'vorläufige Abgrenzung des TOD-Bereichs.',
     'Der Volksausschuss der Provinz legt vor; der Volksrat der Provinz beschließt, soweit es '
     'in seine Zuständigkeit fällt',
     'Luật Quy hoạch đô thị và nông thôn 47/2024/QH15 · Luật Quy hoạch 112/2025/QH15 · '
     'Hanoi: NQ 64/2026/NQ-HĐND zur Planung des unterirdischen Raums',
     'Genehmigte Trassenplanung · Trassenvariante · vorläufige Grenze des TOD-Bereichs',
     'Die Trasse wird auf dem Plan gezeichnet, aber nicht im Gelände abgesteckt; der '
     'Grunderwerb fällt später versetzt aus. Eine Planung des unterirdischen Raums existiert '
     'noch nicht, sodass sich die vertikale Grenze unterirdischer Stationen nicht festlegen lässt.'),
    ('Entscheidung über die Investitionsleitlinie',
     'Erstellung des Vorschlags zur Investitionsleitlinie oder der Vorstudie; Prüfung der '
     'Finanzierungsquelle und der Fähigkeit zum Kapitalausgleich; Entscheidung über die '
     'Investitionsleitlinie.',
     'Die Nationalversammlung bei Vorhaben von nationaler Bedeutung · der Premierminister · '
     'der Volksrat der Provinz',
     'Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (geändert durch NĐ 275/2025) · '
     'NĐ 19/2026 zur Prüfung von Vorhaben nationaler Bedeutung',
     'Beschluss oder Entscheidung über die Investitionsleitlinie · vorläufige '
     'Gesamtinvestitionssumme · Finanzierungsstruktur',
     'Die vorläufige Gesamtinvestitionssumme beruht auf dünnen Erkundungsdaten; bei der '
     'eigentlichen Vorhabenvorbereitung klafft die Lücke weit auf. Wo der Sondermechanismus '
     'diesen Schritt entfallen lässt, fehlt in den Abrechnungsunterlagen ein Glied, das man '
     'dort erwartet — bereiten Sie den Ersatznachweis rechtzeitig vor.'),
    ('Vorbereitung, Prüfung und Genehmigung des Vorhabens',
     'Baugrunderkundung; Machbarkeitsstudie und Grundlagenplanung oder technische '
     'Gesamtplanung nach dem Sondermechanismus; Prüfung durch die zuständige Fachbehörde; '
     'Brandschutzfreigabe und Umweltprüfung.',
     'Die investitionsentscheidende Stelle nach Übertragung; bei Vorhaben nach NQ 188 ist die '
     'Zuständigkeit weitgehend auf die Provinz verlagert',
     'Luật Xây dựng 135/2025/QH15 · NĐ 209/2026 und NĐ 210/2026 · NĐ 206/2026 zur '
     'Kostensteuerung · VBHN 34/VBHN-BXD zur technischen Gesamtplanung',
     'Genehmigungsentscheidung · genehmigte Gesamtinvestitionssumme — sie ist die rechtliche '
     'Obergrenze für jede später abzurechnende Kostenposition',
     'Bei den unterirdischen Mengen weichen Planung und tatsächlicher Baugrund am stärksten '
     'voneinander ab. Vorhaben, die vor dem 30. Juli 2026 vorbereitet wurden, hatten keine '
     'eigene Metro-Norm und mussten auf ausländische zurückgreifen.'),
    ('Grunderwerb und Umsiedlung',
     'Mitteilung über die Landrücknahme; Bestandsaufnahme; Aufstellung, Auslegung und '
     'Genehmigung des Entschädigungs-, Unterstützungs- und Umsiedlungsplans; Auszahlung; '
     'Übergabe des Baufeldes in Teilen. Läuft parallel zu Phase 3.',
     'Der Volksausschuss, der für Landrücknahme und Genehmigung des Plans zuständig ist',
     'Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · '
     'Hanoi, in TOD-Bereichen: NQ 66/2026/NQ-HĐND',
     'Landrücknahmeentscheidung je Flurstück · genehmigter Entschädigungsplan · '
     'Übergabeprotokolle des Baufeldes',
     'Das Baufeld wird stückweise übergeben, sodass die Baufirma keinen durchgehenden Ablauf '
     'organisieren kann und Stillstandskosten geltend macht. Auszahlungsnachweisen fehlen '
     'Unterschriften, was erst bei der Schlussabrechnung auffällt — dann sind die Empfänger '
     'längst weggezogen.'),
    ('Auftragnehmerauswahl und Vertragsschluss',
     'Aufstellung und Genehmigung des Auswahlplans; Herausgabe der Vergabeunterlagen; '
     'Wertung; Prüfung und Genehmigung des Ergebnisses; Verhandlung und Vertragsschluss.',
     'Die zuständige Stelle und der Vorhabenträger nach dem Vergaberecht',
     'Luật Đấu thầu 22/2023/QH15 (geändert durch Luật 57/2024 und Luật 90/2025) · NĐ 214/2025 · '
     'bei PPP: TT 98/2025/TT-BTC und TT 142/2025/TT-BTC',
     'Entscheidung über das Auswahlergebnis · Vertrag mit der darin bezeichneten Form des '
     'Vertragspreises',
     'Die im Vertrag festgeschriebene Form des Vertragspreises stimmt nicht damit überein, wie '
     'die Parteien tatsächlich abrechnen — ein Pauschalvertrag wird nach Aufmaß abgerechnet oder '
     'umgekehrt. Daraus entsteht der größte Teil der Streitigkeiten bei der Schlussabrechnung.'),
    ('Bauausführung, Kostensteuerung und Änderungen',
     'Nachfolgende Planungsstufen; Aufstellung, Prüfung und Genehmigung der '
     'Kostenberechnungen; Bauausführung; Mengenabnahme nach Bauabschnitten; Zahlung; '
     'Behandlung von Änderungen und Anpassungen.',
     'Der Vorhabenträger für Kostenberechnungen innerhalb des genehmigten Rahmens; die '
     'investitionsentscheidende Stelle für Vorhabenänderungen',
     'NĐ 206/2026 zur Kostensteuerung · NĐ 207/2026 zur Qualitätssteuerung · '
     'TT 36/2026, TT 37/2026, TT 38/2026 zu Normen und Kosten',
     'Genehmigte Kostenberechnungen je Leistungsposition · Protokolle der Mengenabnahme · '
     'Bestandspläne · Zahlungsunterlagen je Tranche',
     'Bei den Normen wird am leichtesten gefehlt — dieselbe Leistungsposition trägt in '
     'verschiedenen Zeiträumen verschiedene Normen, und maßgeblich ist die zum Zeitpunkt der '
     'Kostenberechnung geltende. Für Sonderleistungen wie Tunnelvortrieb und Signaltechnik gibt '
     'es überhaupt keine inländische Norm.'),
    ('Abnahme, Probebetrieb und Systemsicherheitsnachweis',
     'Abnahme fertiggestellter Teile; statische und dynamische Erprobung; integrierter '
     'Probebetrieb des Gesamtsystems; Systemsicherheitsbewertung und -zertifizierung; '
     'staatliche Abnahme; Betriebsgenehmigung.',
     'Der Vorhabenträger führt die Abnahme durch; die Fachbehörde überprüft die Abnahme; '
     'die Aufsichtsbehörde erteilt die Betriebsgenehmigung',
     'Luật Đường sắt 95/2025/QH15 (konsolidierte Fassung 75/VBHN-VPQH) · NĐ 16/2026 · '
     'TT 62/2026/TT-BXD Metro-Norm · VBHN 13/VBHN-BXD zur Verknüpfung mit der Staatsbahn',
     'Abnahmeprotokolle · Unterlagen zum Probebetrieb · Systemsicherheitszertifikat · '
     'Entscheidung über die Inbetriebnahme',
     'Diese Phase überschreitet den Terminplan am häufigsten. Strom, Betriebspersonal und '
     'Versicherung fallen an, während die Anlagen noch nicht übergeben sind und keine Erlöse '
     'bringen. Ob dies Investitions- oder Betriebskosten sind, muss vorher schriftlich geklärt '
     'werden.'),
    ('Übergabe, Aktivierung und Betriebsaufnahme',
     'Übergabe der Anlagen und Unterlagen an den Betreiber; Feststellung des Eigentums und '
     'Zuweisung der Verwaltung der Infrastrukturvermögenswerte; Anlagenverzeichnis, Anmeldung '
     'und Abschreibung; Aufbau des Tarif- und Zuschussmodells.',
     'Die Stelle, die die Verwaltung der Infrastrukturvermögenswerte zuweist; Volksausschuss '
     'und Volksrat der Provinz für Tarif und Zuschuss',
     'NĐ 15/2025 zu Eisenbahninfrastrukturvermögen · TT 75/2025/TT-BTC zur Abschreibung · '
     'TT 34/2025 und TT 33/2025/TT-BXD · Luật Quản lý, sử dụng tài sản công 15/2017/QH14',
     'Übergabeprotokolle je übernehmender Stelle · Verzeichnis und Wert der durch die '
     'Investition entstandenen Vermögenswerte',
     'Erst übergeben, dann bewerten — die Züge fahren, während die Vermögenswerte noch nicht '
     'endgültig bewertet sind; der Betreiber bucht vorläufige Zahlen, und nach Abschluss der '
     'Schlussabrechnung muss alles berichtigt werden.'),
    ('Schlussabrechnung des Investitionskapitals',
     'Abschluss und Abstimmung des ausgezahlten Kapitals; Erstellung des '
     'Schlussabrechnungsberichts; unabhängige Prüfung dieses Berichts; behördliche Nachprüfung; '
     'Genehmigung der Schlussabrechnung; Abwicklung von Forderungen, Verbindlichkeiten sowie '
     'überzähligem Material und Gerät.',
     'Die nach Übertragung genehmigende Stelle; die Finanzbehörde führt die Nachprüfung',
     'NĐ 254/2025 (ersetzt NĐ 99/2021) · TT 147/2025/TT-BTC · TT 73/2026/TT-BTC zum '
     'Formularwesen · Prüfung nach VSA 1000',
     'Schlussabrechnungsbericht · unabhängiger Prüfungsbericht · Nachprüfungsbericht · '
     'Genehmigungsentscheidung',
     'Die Unterlagen haben mehrere Generationen von Verordnungen durchlaufen; wer sie erstellt '
     'hat, ist nicht mehr da; frühe Belege sind verloren. Kosten, die nicht dem Anlagewert '
     'zuzurechnen sind, bleiben in der Schwebe, solange die zuständige Stelle sie nicht '
     'schriftlich zugelassen hat.'),
]

# 4 ngan phap ly: (ma, ten, pham vi, van ban, mau)
QT_NGAN = [
    ('A', 'Metro in Hanoi / Ho-Chi-Minh-Stadt, öffentliche Investition',
     'Gelegen in Hanoi oder Ho-Chi-Minh-Stadt',
     'NQ 188/2025/QH15 · Luật Đường sắt 95/2025/QH15 · VBHN 34/VBHN-BXD', 'ngoc'),
    ('B', 'Metro andernorts, öffentliche Investition',
     'Außerhalb von Hanoi und Ho-Chi-Minh-Stadt',
     'Luật Đường sắt 95/2025/QH15 · Luật Đầu tư công 58/2024/QH15 · Luật Xây dựng. '
     'NQ 188 kann nicht herangezogen werden', 'do'),
    ('C', 'Metro im Rahmen einer PPP',
     'Durchführung auf Grundlage eines PPP-Vertrags',
     'Luật PPP 64/2020/QH14 (konsolidierte Fassung 81/VBHN-VPQH) · NĐ 243/2025 · NĐ 312/2025',
     'nhan'),
    ('D', 'TOD-Bereich zur Linie',
     'Die Zone um Stationen und Betriebshöfe',
     'Luật Thủ đô 02/2026/QH16 · Beschlüsse des Volksrats der Provinz '
     '(Hanoi: NQ 71/2025, 66/2026, 67/2026 — Ho-Chi-Minh-Stadt: NQ 21/2026)', 'muc'),
]

# 3 cho ho: (ten, giai thich)
QT_HO = [
    ('TOD-Vorteilskoeffizient in Hanoi — noch nicht erlassen',
     'NQ 67/2026/NQ-HĐND Artikel 8 beauftragt den Volksausschuss, den TOD-Vorteilskoeffizienten '
     'und die Prozentsätze dem Volksrat vorzulegen, sobald die Planung des TOD-Bereichs '
     'genehmigt ist. Dieser Beschluss ist nicht ergangen. Ohne ihn lassen sich die vier '
     'TOD-Einnahmearten nicht in Geld umrechnen.'),
    ('Anschlussentgelt für den unterirdischen Raum in Hanoi — noch nicht erlassen',
     'NQ 65/2026/NQ-HĐND Artikel 3 Absatz 2 sieht die Vorlage des Anschlussentgelts vor, sobald '
     'die Planung des unterirdischen Raums genehmigt ist. Solange dieses Dokument fehlt, lässt '
     'sich die Anschlusspflicht benachbarter Gebäude an eine unterirdische Station nicht '
     'bestimmen.'),
    ('Durchführungsverordnung zu Luật Thủ đô 02/2026 — nicht auffindbar',
     'QĐ 762/QĐ-TTg ist der Umsetzungsplan zu Luật Thủ đô 39/2024 und erging, bevor das neue '
     'Gesetz existierte. Eine Ersatzentscheidung zu Luật 02/2026 und eine '
     'Durchführungsverordnung haben wir nicht gefunden.'),
]

# =================================================================== KIEM TOAN QT
KT = dict(
    td='Schlussabrechnungsprüfung abgeschlossener Vorhaben',
    mt='Dreizehn Arbeitsfelder, zwei Abstimmgleichungen und der Grund, warum ein großes '
       'Metrovorhaben baubegleitend statt erst am Ende geprüft werden sollte.',
    duong='Schlussabrechnungsprüfung',
    h1='Den Schlussabrechnungsbericht eines abgeschlossenen Vorhabens prüfen',
    lede='Bei einer Metrolinie sollte die Prüfung nicht bis zur Eröffnung warten. Eine Linie '
         'braucht acht bis fünfzehn Jahre; Nachweise, die man nicht in dem Moment sieht, in dem '
         'sie existieren, lassen sich später nicht wiederherstellen. Diese Seite zeigt, was die '
         'Prüfung umfasst und warum die Arbeit bei einem Vorhaben dieser Größe parallel zum Bau '
         'läuft.',
    h_sh='Was baubegleitende Prüfung bedeutet',
    sh='Baubegleitend prüfen heißt, dass die Prüferin oder der Prüfer während der Bauzeit in '
       'Abschnitten hinzukommt statt einmal am Ende. Jeder Abschnitt schließt eine Phase oder ein '
       'Vergabepaket ab; der letzte Abschnitt führt zusammen. Es ist kein anderer Prüfungsmaßstab '
       '— es ist dieselbe Arbeit, nur dort ausgeführt, wo die Nachweise noch vorhanden sind.',
    h_vs='Fünf Gründe, warum ein großes Vorhaben baubegleitend geprüft werden muss',
    h_ss='Die beiden Vorgehensweisen im Vergleich',
    ss_cot=('', 'Prüfung nach Fertigstellung', 'Baubegleitende Prüfung'),
    h_ph='Dreizehn Arbeitsfelder',
    ph_lede='Die Gliederung folgt der VACPA-Musterarbeitsakte für Schlussabrechnungsberichte '
            'abgeschlossener Vorhaben (QĐ 314-2016/QĐ-VACPA). Die Nummerierung ist die '
            'Aktengliederung, nicht die Arbeitsreihenfolge.',
    h_cd='Zwei Abstimmungen vor der Erteilung',
    cd_lede='Beide laufen über denselben Zahlenbestand. Stimmen sie nicht, wird der Bericht '
            'nicht erteilt.',
    h_kl='Drei Dinge, die eine Prüferin oder ein Prüfer nicht tut',
    h_phi='Prüfungshonorar — hier berechnen',
    phi_1='Nach <b>Nghị định 193/2026/NĐ-CP, Artikel 20</b>, in Kraft seit dem 1. Juli 2026. '
          'Geben Sie den Prüfungsgegenstand ein, und das Honorar erscheint.',
    phi_2='Diese Sätze sind gegenüber Nghị định 254/2025/NĐ-CP Artikel 45 <b>unverändert</b> — '
          'wir haben jede Zahl abgeglichen. Die neue Verordnung nummeriert den Artikel lediglich um.',
    l_gt='Prüfungsgegenstand (Wert)',
    l_gt_phu='Der zur Abrechnung vorgesehene Betrag; liegt noch keiner vor, die '
             'Gesamtinvestitionssumme',
    l_dv='Einheit',
    # 🔴 l_ty = TY DONG. Tieng Duc phai la "Milliarden", KHONG phai "Billion" (= 10^12).
    l_ty='Milliarden VND', l_tr='Millionen VND', l_d='VND',
    l_vat='Umsatzsteuer', l_kvat='Nicht anwendbar',
    tick_tb='<b>Geräteanteil beträgt 50 % oder mehr</b> — Artikel 20 Absatz 1 Buchstabe d: '
            'das Honorar beträgt <b>70 %</b> des Regelbetrags',
    tick_bt='<b>Es handelt sich um Entschädigungs-, Unterstützungs- und Umsiedlungskosten</b> — '
            'Buchstabe đ: das Honorar beträgt <b>50 %</b> des Regelbetrags',
    tick_kt='<b>Bereits unabhängig, durch den Staatlichen Rechnungshof oder eine Inspektion '
            'geprüft</b> — Buchstabe e: allein die <b>Nachprüfungs</b>gebühr beträgt <b>50 %</b>',
    kq_gt='Bemessungsgrundlage', kq_ty='Angewandter Satz', kq_hs='Anpassungsfaktor',
    kq_truoc='Prüfungshonorar ohne Steuer', kq_vat='Umsatzsteuer',
    kq_nhan='Höchstbetrag des Prüfungshonorars', kq_phu='einschließlich Umsatzsteuer',
    kq_tt='Gebühr für Nachprüfung und Genehmigung der Schlussabrechnung',
    kq_tt_ghi='Diese Gebühr erhebt die nachprüfende Behörde — sie ist kein an die Prüferin oder '
              'den Prüfer zu zahlendes Honorar, und Umsatzsteuer wird darauf nicht erhoben.',
    kq_loi='Bitte geben Sie einen Wert größer als null ein.',
    kq_toi='* Der Mindestbetrag von 1 Million VND nach Artikel 20 Absatz 1 Buchstabe b wurde '
           'angewandt.',
    h_bang='Die Satztabelle',
    bang_gt='Wert (Milliarden VND)', bang_kt='Unabhängige Prüfung (%)', bang_tt='Nachprüfung (%)',
    bang_ghi='Ein Wert zwischen zwei Schwellen wird nach Artikel 20 Absatz 1 Buchstabe a linear '
             'interpoliert: <code>Ki = Kb − (Kb − Ka) × (Gi − Gb) ÷ (Ga − Gb)</code>. '
             'Der Rechner oben tut dies bereits.',
    h_nho='Vier Dinge, die zu diesem Betrag zu merken sind',
    nho='<b>Erstens —</b> es handelt sich um einen <b>Höchstbetrag</b>, nicht um den Preis, den '
        'Sie zahlen müssen. Ein Angebotspreis kann darunter liegen und liegt es im Wettbewerb '
        'meist auch.<br><br>'
        '<b>Zweitens —</b> das Mindesthonorar der Prüfung beträgt <b>1 Million VND</b> zuzüglich '
        'Steuer; die Mindestgebühr der Nachprüfung <b>500 Tausend VND</b>.<br><br>'
        '<b>Drittens —</b> auf das Prüfungshonorar wird <b>Umsatzsteuer erhoben</b>, auf die '
        'Nachprüfungsgebühr nicht.<br><br>'
        '<b>Viertens —</b> dieser Betrag ist eine <b>Grundlage zur Schätzung eines Auftrags</b>. '
        'Das Honorar im konkreten Mandat hängt zusätzlich vom Umfang der Unterlagen, der Zahl '
        'der Vergabepakete, dem Ort und der verfügbaren Zeit ab.',
    h_sh2='Wie es sich bei baubegleitender Prüfung verhält',
    sh2='Der Satz gilt für den <b>Prüfungsgegenstand des Vorhabens insgesamt</b>, nicht für die '
        'Summe der Abschnitte. Die Aufteilung in Abschnitte ist eine Frage der Organisation, '
        'kein Weg, das Honorar zu vervielfachen.',
    sh3='In der Praxis liegen die Gesamtkosten eines baubegleitenden Mandats über dem Satz für '
        'ein einmaliges Mandat, weil die Arbeit tatsächlich größer ist — mehr Ortstermine, mehr '
        'Arbeitsstunden. Diese Differenz wird im Vertrag vereinbart und bedarf der Zustimmung der '
        'zuständigen Stelle.',
    h_bt='Wenn Sie das Vorgehen für Ihr eigenes Vorhaben abwägen',
    bt='Ob nach Fertigstellung oder baubegleitend geprüft wird, hängt von Größe, Dauer und Zahl '
       'der Vergabepakete ab. Schildern Sie uns die Einzelheiten über die Seite %s, und wir sagen '
       'Ihnen unsere Einschätzung zum Vorgehen und zum voraussichtlichen Arbeitsumfang.',
    bt_lk='Beratung',
)

KT_VS = [
    ('Die frühen Unterlagen sind nicht mehr vollständig vorhanden',
     'Eine Metrolinie läuft acht bis fünfzehn Jahre. Wartet man bis zur Fertigstellung, sind die '
     'Belege der ersten Jahre verblasst, die Unterzeichnenden versetzt, Nachunternehmen '
     'liquidiert. Die Prüferin oder der Prüfer findet keine Nachweise — und ohne Nachweise gibt '
     'es kein Urteil.'),
    ('Unterirdische Mengen sind bereits verdeckt',
     'Die Bewehrung vor dem Betonieren, der Tunnelausbau vor der Innenschale — beides lässt sich '
     'genau einmal sehen, im Augenblick der Ausführung. Danach kann niemand mehr nachmessen, so '
     'sehr er es auch wollte. Wer später hinzukommt, hat nur noch die Akte.'),
    ('Ein spät entdeckter Fehler lässt sich nicht mehr heilen',
     'Eine Kostenposition ohne Entscheidung der zuständigen Stelle lässt sich heilen, wenn sie im '
     'Entstehungsjahr auffällt. Sieben Jahre später ist die damals zuständige Person im Ruhestand, '
     'und die Nachfolge unterschreibt nichts, was sie nicht selbst begleitet hat.'),
    ('Alles ans Ende zu schieben zieht die Schlussabrechnung in die Länge',
     'Ein Vorhaben über mehrere Billionen VND umfasst Zehntausende Belege. Wirft man sie alle in '
     'eine einzige Schlussprüfung, vergehen allein für das Ordnen Monate, bevor überhaupt geprüft '
     'wird. Nach Phasen aufgeteilt bleibt jeder Abschnitt handhabbar, und spätere Abschnitte bauen '
     'auf früheren auf.'),
    ('Der Vorhabenträger erfährt rechtzeitig, wo er falsch liegt',
     'Das ist der größte Nutzen. Baubegleitende Prüfung dient nicht nur dem Aufdecken; sie soll '
     'dem Vorhabenträger ermöglichen, die Art der Unterlagenerstellung schon beim nächsten '
     'Vergabepaket zu ändern. Ein Hinweis im zweiten Jahr spart Monate im zehnten.'),
]

KT_SS = [
    ('Zeitpunkt des Beginns', 'Nach Fertigstellung der Anlagen',
     'Ab der Bauphase, in Abschnitten'),
    ('Aufteilung der Arbeit', 'Ein Durchgang über das gesamte Vorhaben',
     'Mehrere Abschnitte nach Phase oder Vergabepaket, mit zusammenführendem Schlussabschnitt'),
    ('Prüfungsnachweise', 'Nur Unterlagen; verdeckte Leistungen nicht prüfbar',
     'Unmittelbare Inaugenscheinnahme vor dem Verdecken sowie Bestandsaufnahmen vor Ort'),
    ('Wenn ein Fehler auffällt', 'Meist zu spät, um die Unterlagen noch zu vervollständigen',
     'Es bleibt Zeit, ihn zu heilen oder eine Entscheidung einzuholen'),
    ('Dauer der Schlussabrechnung', 'Lang, weil Unterlagen aus Vorjahren rekonstruiert werden '
                                    'müssen',
     'Kürzer, weil das meiste bereits geprüft und abgestimmt ist'),
    ('Prüfungskosten', 'Als Einzelmandat günstiger, aber höheres Risiko, dass Unterlagen in der '
                       'Schwebe bleiben',
     'In der Summe höher, dafür geringeres Risiko und kürzere Schlussabrechnung'),
    ('Geeignet für', 'Kleine Vorhaben unter zwei Jahren',
     'Vorhaben der Gruppe A, Vorhaben nationaler Bedeutung, Vorhaben mit vielen Vergabepaketen, '
     'ODA-Vorhaben'),
]

KT_PH = [
    ('1000', 'Prüfungsplanung',
     'Mandatsannahme und Beurteilung des Auftragsrisikos · Verständnis des Vorhabens und seines '
     'internen Kontrollsystems · vorläufige Analyse des Schlussabrechnungsberichts · Festlegung '
     'der Wesentlichkeit und des Stichprobenverfahrens · Gesamtprüfungsplan.',
     'Wer die Wesentlichkeit falsch ansetzt, zieht jeden nachfolgenden Stichprobenumfang mit '
     'ins Falsche.'),
    ('3000', 'Rechtliche Vorhabenunterlagen',
     'Abgleich der rechtlichen Unterlagen mit den Anforderungen · Prüfung der '
     'Genehmigungszuständigkeit · Beurteilung der Einhaltung des Investitions- und '
     'Bauablaufs, des Auswahlverfahrens und des Vertragsschlusses.',
     'Wird ein Sondermechanismus angewandt, muss zuerst nachgewiesen werden, dass das Vorhaben in '
     'dessen Anwendungsbereich fällt, bevor ein verkürzter Schritt akzeptiert wird.'),
    ('4000', 'Quellen des Investitionskapitals',
     'Prüfung von Beständen und Bewegungen je Quelle · Abstimmung des ausgezahlten Kapitals '
     'zwischen Vorhabenträger und auszahlender Stelle · Prüfung von Zu- und Abgängen sowie ihrer '
     'Verbuchung.',
     'Hier treten Differenzen am häufigsten auf — und hier lässt sich am leichtesten sauber '
     'bleiben, wenn jährlich abgestimmt wird.'),
    ('5100', 'Entschädigungs-, Unterstützungs- und Umsiedlungskosten',
     'Abgleich mit dem genehmigten Entschädigungsplan · Prüfung bis zur Entschädigungsentscheidung '
     'der zuständigen Stelle · Auszahlungsübersicht · Zahlungsbelege und Empfangsbestätigungen.',
     'Ein Auszahlungsnachweis ohne Unterschrift lässt sich kaum noch vervollständigen, weil die '
     'empfangende Person weggezogen ist.'),
    ('5200', 'Baukosten',
     'Abgleich der A–B-Abrechnung mit dem Schlussabrechnungsbericht · Prüfung von Mengen und '
     'Einheitspreisen entsprechend der tatsächlichen Form des Vertragspreises · Abgleich von '
     'Abnahmeprotokollen und Qualitätsunterlagen · Prüfung der Abrechnung von Änderungen.',
     'Das größte Arbeitsfeld. Die Prüfmethode einer Vertragspreisform auf eine andere anzuwenden '
     'ist der häufigste Fehler überhaupt.'),
    ('5300', 'Gerätekosten',
     'Abgleich der Vertragsabrechnung · Prüfung von Verzeichnis, Typ, Herkunft, Qualität und '
     'Konfiguration der Geräte gegen Kostenberechnung und Vertrag · Prüfung der Abrechnung von '
     'Änderungen.',
     'Bei einer Metro ist der Geräteanteil sehr groß und überwiegend importiert — auch der '
     'Umrechnungskurs ist zu prüfen.'),
    ('5400', 'Vom Vorhabenträger beigestelltes Material und Gerät',
     'Zusammenführung von Zugang, Abgang und Bestand · Prüfung des Zugangs nach Menge, Herkunfts- '
     'und Qualitätsnachweisen sowie Einheitspreisen · Prüfung der Abgänge zur Montage an die '
     'einzelnen Auftragnehmer.',
     'Eine ungeklärte Lücke zwischen Zugang, Abgang und Bestand ist das Signal, den Prüfungsumfang '
     'auszuweiten.'),
    ('5500', 'Projektsteuerungs-, Beratungs- und sonstige Kosten',
     'Abgleich mit der genehmigten Gesamtkostenberechnung · Prüfung der vom Vorhabenträger selbst '
     'erbrachten Kosten einschließlich Beschaffung und Personalkosten der Projektleitung · Prüfung '
     'der von Beratenden erbrachten Kosten.',
     'Sie sind mit den seinerzeit geltenden Normen neu zu berechnen, nicht mit den heutigen.'),
    ('6000', 'Nicht dem Anlagewert zuzurechnende Kosten',
     'Zwei Gruppen: Schäden aus höherer Gewalt, die herausgenommen werden dürfen, und Kosten, die '
     'keinen Vermögenswert schaffen. Art und Höhe des Schadens sind gegen die Entscheidung der '
     'zuständigen Stelle zu prüfen, ebenso deren Zuständigkeit.',
     'Ohne zulassende Entscheidung bleibt der Betrag in der Schwebe und ist nicht abrechenbar.'),
    ('7000', 'Wert der durch die Investition entstandenen Vermögenswerte',
     'Zusammenführung lang- und kurzfristiger Vermögenswerte · Grundsatz der Verteilung von '
     'Gemeinkosten · Gliederung nach Finanzierungsquelle und Nutzer · Übertragungsentscheidungen '
     'und Übergabeprotokolle · Restwert der eigenen Vermögenswerte der Projektleitung.',
     'Bei einer Metro gehen die Vermögenswerte an mehrere verschiedene übernehmende Stellen; die '
     'Aufstellung muss daher von Anfang an klar getrennt sein.'),
    ('8000', 'Forderungen, Verbindlichkeiten und überzähliges Material',
     'Prüfung der Salden je Auftragnehmer · Saldenbestätigung durch von der Prüferin oder dem '
     'Prüfer gesteuerte Anfragen · Prüfung von Kassen- und Bankbeständen · Prüfung von Zugang, '
     'Abgang und Bestand überzähligen Materials und Geräts.',
     'Versand und Empfang der Bestätigungen muss die Prüferin oder der Prüfer selbst steuern — '
     'niemals dem Vorhabenträger überlassen.'),
    ('9000', 'Regeltreue des Vorhabenträgers',
     'Durchsicht der Einhaltung des Investitions- und Baurechts · Einhaltung der Rechnungslegungs- '
     'und Abrechnungsvorgaben · sowie Umsetzung der Feststellungen von Inspektionen und des '
     'Staatlichen Rechnungshofs.',
     'Ein großes Vorhaben hat mit hoher Wahrscheinlichkeit mindestens eine Inspektion durchlaufen '
     '— wer das überspringt, erhält einen Bericht, der den Feststellungen einer staatlichen Stelle '
     'widerspricht.'),
    ('2000', 'Zusammenführung, Durchsicht und Erteilung',
     'Zusammenführung der Ergebnisse und Prüfung der Abstimmung · Zusammenführung der '
     'Korrekturvorschläge · Auflistung nicht einvernehmlicher Punkte · Vollständigkeitserklärung '
     'des Vorhabenträgers · Protokoll der Schlussbesprechung · Durchsicht auf jeder Stufe · '
     'Freigabe zur Erteilung.',
     'Die Abstimmgleichungen müssen vor der Erteilung aufgehen — gehen sie nicht auf, wird der '
     'Bericht nicht erteilt.'),
]

KT_CD = [
    ('Quellen gegen Kosten',
     'Gesamtes Investitionskapital (4000) ≈ Gesamte zur Abrechnung vorgelegte Investitionskosten '
     '(5000)',
     'Eine Differenz bedeutet: entweder ist Kapital nicht erfasst, oder eine Kostenposition hat '
     'keine Quelle hinter sich.'),
    ('Kosten gegen Anlagewert',
     'Investitionskosten (5000) − nicht dem Anlagewert zuzurechnen (6000) − überzähliges Material '
     'und Gerät (8200) = Wert der entstandenen Vermögenswerte (7000)',
     'Das ist die letzte Abstimmung vor der Erteilung. Auch eine Differenz von einem Dong ist '
     'nachzuverfolgen.'),
]

KT_KL = [
    ('Wir prüfen nicht, während wir dasselbe Vorhaben beraten',
     'Unterlagen zu erstellen und anschließend die selbst erstellten Unterlagen zu prüfen '
     'zerstört die Unabhängigkeit. Das ist ein Verbot; keine Schutzmaßnahme heilt es.'),
    ('Wir erstellen die Unterlagen nicht anstelle des Vorhabenträgers',
     'Die Prüferin oder der Prüfer weist darauf hin, was fehlt; erstellen und unterzeichnen muss '
     'der Vorhabenträger. Tut man es für ihn, verwischt die Verantwortungsgrenze.'),
    ('Wir urteilen nicht ohne ausreichende Nachweise',
     'Fehlen Nachweise, sagen wir das und benennen die Auswirkung, statt eine Zahl herzuleiten, '
     'damit der Bericht vollständig aussieht.'),
]
