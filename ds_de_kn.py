# -*- coding: utf-8 -*-
"""Ban TIENG DUC: trang KINH NGHIEM (Erfahrungen) va VUONG MAC (Häufige Probleme).

Ten van ban phap luat GIU NGUYEN so hieu tieng Viet.

🔴 Nhac lai bay don vi tien: "Billion" tieng Duc = 10^12, "Milliarde" = 10^9.
   "Vorhaben uber mehrere Billionen VND" = du an nhieu NGHIN TY dong. Dung.
   Xem ds_de_qt.py phan dau file.
"""

# =================================================================== KINH NGHIEM
KN = dict(
    td='Zwölf Lehren aus der Steuerung von Metrovorhaben',
    mt='Zwölf Praktiken, die darüber entscheiden, ob Abrechnungsunterlagen bestehen, drei teure '
       'Irrtümer und eine Checkliste an fünf Punkten des Vorhabens.',
    duong='Erfahrung',
    h1='Zwölf Lehren aus der Vorhabensteuerung',
    lede='Keine davon ist schwierig. Jede ist im richtigen Moment billig und später teuer zu '
         'reparieren. Sie sind für eine Projektleitung geschrieben, die möchte, dass ihre '
         'Abrechnungsunterlagen bestehen — bei einer Linie, die acht bis fünfzehn Jahre laufen wird.',
    h_bh='Zwölf Lehren',
    h_sl='Drei teure Irrtümer',
    h_kt='Eine Checkliste an fünf Punkten',
    kt_lede='Kein Formular zur Regeltreue. Es ist die kurze Liste dessen, was sich, wenn es in '
            'diesem Moment fehlt, später nicht mehr beschaffen lässt.',
    h_bt='Das auf Ihr eigenes Vorhaben anwenden',
    bt='Möchten Sie daraus Verfahren und Formulare für Ihre Stelle machen, ist das eine der '
       'Leistungen, die wir erbringen — siehe %s.',
    bt_lk='Abrechnungsunterlagen vom ersten Tag an führen',
)

KN_BH = [
    ('Eine Übersicht bauen, welche Vorschriften wann galten — und sie aktuell halten',
     'Sobald das Vorhaben genehmigt ist, eine Tabelle anlegen: jeder Meilenstein gegen die in '
     'diesem Moment geltenden Vorschriften. Bei jeder neuen Verordnung oder jedem neuen '
     'Rundschreiben, das Altes ablöst, eine Zeile ergänzen. Die Tabelle kostet etwa zwei Tage '
     'Aufbau und zehn Minuten Pflege. Ohne sie bedeutet die Schlussabrechnung, sie über Monate aus '
     'dem Gedächtnis derjenigen zu rekonstruieren, die noch da sind.'),
    ('Die Form des Vertragspreises in den Vergabeunterlagen festschreiben',
     'Eine Preisform je Vergabepaket. Mischt ein Paket mehrere Leistungsarten, den Preisanhang '
     'nach Teilen aufteilen. Am wichtigsten: Die tatsächliche Zahlungsweise muss der '
     'festgeschriebenen Preisform entsprechen. Dies ist die teuerste Lehre hier — der größte Teil '
     'des Streits bei der Nachprüfung hängt genau an diesem Punkt.'),
    ('Unterlagen laufend erstellen, nicht am Periodenende',
     'Abnahmeprotokolle am Tag der Abnahme unterzeichnen. Bestandspläne erstellen, sobald die '
     'Position fertig ist. Bautagebuch täglich führen. Es klingt selbstverständlich und ist die am '
     'häufigsten gebrochene Regel — und die unmittelbare Ursache der meisten bei der '
     'Schlussabrechnung aberkannten Beträge.'),
    ('Fotografieren und aufmessen, was verdeckt wird, solange es sichtbar ist',
     'Bei einer Metro macht die unterirdische Leistung einen sehr großen Kostenanteil aus und '
     'lässt sich nach Fertigstellung nicht erneut aufmessen. Bewehrung vor dem Betonieren, '
     'Tunnelausbau vor der Innenschale — beides braucht Fotos mit Zeit und Ort sowie ein von den '
     'Beteiligten unterzeichnetes Protokoll. Ein Foto ohne Zeit und Ort beweist so gut wie nichts.'),
    ('Das ausgezahlte Kapital jährlich mit der auszahlenden Stelle abstimmen',
     'Der am häufigsten übersprungene Schritt — und der, der die meisten Differenzen findet. '
     'Jährlich durchführen, mit beidseitig unterzeichnetem Protokoll. Eine im laufenden Jahr '
     'gefundene Differenz lässt sich klären; nach acht Jahren bedeutet sie, die gesamte Belegkette '
     'nachzuverfolgen.'),
    ('Normen für Sonderleistungen vor der Ausführung genehmigen lassen',
     'Maschineller Tunnelvortrieb, Montage der Signaltechnik, Oberleitung, integrierte Erprobung — '
     'nichts davon steht im allgemeinen Baunormensystem. Eine neue Norm muss erstellt und vor der '
     'Ausführung genehmigt werden. Wer zuerst baut und später um Genehmigung nachsucht, wird diese '
     'Kosten in der Schwebe finden.'),
    ('Die Behandlung der Kosten des Probebetriebs vorab entscheiden',
     'Vor Beginn des Probebetriebs die Genehmigung eines Dokuments einholen, das Umfang, Dauer, '
     'Kostenliste und Finanzierungsquelle festlegt. In der Buchhaltung eine eigene Kennung '
     'einrichten. Das kostet eine Woche und spart Monate bei der Schlussabrechnung.'),
    ('Projektsteuerungskosten nach einem Grundsatz verteilen, nicht nach Gefühl',
     'Einer Position unmittelbar zurechenbare Kosten gehen vollständig auf diese Position; '
     'Gemeinkosten werden im Verhältnis zum Kapital verteilt. Die Verteilungsaufstellung früh '
     'anlegen und pflegen, statt sich bei der Schlussabrechnung ans Aufteilen zu setzen — '
     'besonders dann, wenn Vermögenswerte an mehrere verschiedene Stellen gehen.'),
    ('Die zu erwartenden Vermögenswerte schon ab der Genehmigung auflisten',
     'Nicht bis zur Übergabe warten, um zu überlegen, wer was erhält. Die Tabelle früh anlegen: '
     'Position — Art des Vermögenswerts — erwartete übernehmende Stelle — Rechtsgrundlage der '
     'Übertragung. Sie wird oft überarbeitet, doch wer sie von Beginn an hat, dem fällt jede '
     'Überarbeitung leicht.'),
    ('Feststellungen von Inspektionen und Rechnungshof sofort abarbeiten und den Weg dokumentieren',
     'Ein langes, großes Vorhaben durchläuft in seinem Leben mit hoher Wahrscheinlichkeit '
     'mindestens eine Inspektion oder Prüfung. Zu jeder Feststellung: das Dokument aufbewahren, '
     'jeden Punkt in einer Übersicht verfolgen, festhalten, was getan wurde und wo der Nachweis '
     'liegt. Bei der Schlussabrechnung wird nach dieser Übersicht als Erstes gefragt.'),
    ('Die Menschen halten, die die Unterlagen kennen — und wo das nicht geht, dokumentiert übergeben',
     'Eine Lebensdauer von zehn bis fünfzehn Jahren ist länger als die übliche Verweildauer einer '
     'Sachbearbeiterin oder eines Sachbearbeiters. Bei jedem Wechsel der zuständigen Person gegen '
     'ein Dokumentenverzeichnis übergeben, nicht allgemein. Das Verzeichnis gehört der '
     'Organisation, nicht der Person.'),
    ('Früh digitalisieren und nach einer einzigen Regel benennen',
     'Papierbelege der frühen Jahre verblassen, gehen verloren, ziehen Feuchtigkeit. Laufend '
     'scannen und nach einer Regel benennen — Vergabepaket, Dokumentenart, Datum, Nummer. Der '
     'Aufwand dafür ist verschwindend gegenüber der Suche nach einem Abnahmeprotokoll aus Jahr zwei '
     'im Jahr elf.'),
]

KN_SL = [
    ('Die Schlussabrechnung für Sache der Buchhaltung zu halten',
     'Die Schlussabrechnung des Investitionskapitals ist Arbeit der gesamten Projektleitung: die '
     'technische Abteilung hält Mengen und Abnahmeprotokolle, die Vertragsabteilung die '
     'Preisklauseln, die Planungsabteilung die Gesamtinvestitionssumme, die Buchhaltung die Belege. '
     'Übergibt man alles der Buchhaltung, kann sie nur zusammenführen, was sie bekommt — und was '
     'sie nicht bekommt, wird zur Lücke in den Unterlagen.'),
    ('Heutige Vorschriften auf Jahre zurückliegende Leistungen anzuwenden',
     'Eine 2022 entstandene Kostenposition richtet sich nach dem 2022 Geltenden, nicht nach einer '
     'Vorschrift von 2026. Eine 2023 abgenommene Position nimmt die 2023 geltende Norm. Das ist ein '
     'Grundlagenfehler, und die nachprüfende Behörde darf ihn zurückweisen.'),
    ('Den Sondermechanismus anzuführen, ohne seine Anwendbarkeit zu belegen',
     'Der Sondermechanismus verkürzt einige Schritte — aber nur dort, wo das Vorhaben in seinen '
     'Anwendungsbereich und in seinen Geltungszeitraum fällt. Die Unterlagen müssen den Nachweis '
     'enthalten: dass das Vorhaben in den Anwendungsbereich von NQ 188/2025 fällt, welcher Teil der '
     'Leistung nach Inkrafttreten des Beschlusses entstand, welcher Schritt nach welcher Bestimmung '
     'verkürzt wurde. Ein allgemeiner Verweis auf „den Sondermechanismus“ ohne Angabe der '
     'Bestimmung genügt nicht.'),
]

KN_KT = [
    ('Sobald das Vorhaben genehmigt ist', [
        'Eine Übersicht, welche Vorschriften wann galten — erstellt, mit benannter Person für die '
        'Pflege',
        'In welchem der vier Rechtsstränge das Vorhaben liegt, mit dem belegenden Dokument',
        'Eine Aufstellung der Gesamtinvestitionssumme nach Zeiträumen — angelegt noch vor jeder '
        'Anpassung',
        'Die Liste der zu erwartenden Vermögenswerte und ihrer voraussichtlichen übernehmenden '
        'Stellen',
        'Eine Dateibenennungsregel und eine elektronische Ordnerstruktur — schriftlich in Kraft '
        'gesetzt',
    ]),
    ('Vor Herausgabe der Vergabeunterlagen je Paket', [
        'Die Form des Vertragspreises festgelegt, eine Form je Leistungsteil',
        'Bietende verpflichtet, Preisanalyse und Basisleistungsverzeichnis als Vertragsanhänge '
        'vorzulegen',
        'Ein Zeitplan für den Technologietransfer mit Abnahmekriterien und je Position '
        'zugeordnetem Wert',
        'Schulungspflichten an Abnahmemeilensteine gebunden, nicht als Pauschale vorab bezahlt',
        'Vertragssprache, Verantwortung für die Übersetzung und Umrechnungskurs für ausländische '
        'Auftragnehmer',
    ]),
    ('Während der gesamten Bauzeit', [
        'Ein Übergaberegister des Baufeldes nach Stationierung und Datum, dreiseitig unterzeichnet',
        'Normen für Sonderleistungen vor der Ausführung genehmigt',
        'Fotos und Aufmaß dessen, was verdeckt wird — mit Zeit, Ort und Protokoll',
        'Jährliche Abstimmung des ausgezahlten Kapitals mit der auszahlenden Stelle',
        'Verteilungsaufstellungen für Projektsteuerungs- und Beratungskosten — regelmäßig '
        'fortgeschrieben',
        'Jede Fristverlängerung in einem Vertragsnachtrag festgehalten, nicht im Schriftwechsel',
    ]),
    ('Vor dem Probebetrieb', [
        'Ein Dokument, das Umfang, Dauer, Kostenliste und Finanzierungsquelle genehmigt',
        'Eine eigene Kennung für die Kosten des Probebetriebs im Buchhaltungssystem',
        'Systemsicherheitsbewertung und -zertifizierung — mit eigener Kostenberechnung und eigenem '
        'Vertrag',
        'Bestandsunterlagen zu den Geräten, mit vietnamesischer Fassung',
    ]),
    ('Vor der Übergabe', [
        'Verzeichnis und Wert der zu übergebenden Vermögenswerte, je übernehmender Stelle',
        'Vermögenswerte als lang- oder kurzfristig eingeordnet',
        'Die eigenen Vermögenswerte der Projektleitung: Buchbestand gegen körperliche Aufnahme '
        'abgestimmt, Restwert festgestellt',
        'Überzähliges Material und Gerät: Buchbestand gegen körperliche Aufnahme abgestimmt, mit '
        'Verwertungsplan',
        'Forderungen und Verbindlichkeiten den richtigen Parteien zugeordnet, mit '
        'Behandlungsvorschlag',
    ]),
]

# =================================================================== VUONG MAC
VM = dict(
    td='Zehn wiederkehrende Probleme bei Metrovorhaben',
    mt='Zehn wiederkehrende Probleme bei Metrovorhaben in Vietnam: was geschieht, warum, '
       'welche Vorschriften gelten und was zu tun ist.',
    duong='Häufige Probleme',
    h1='Zehn wiederkehrende Probleme',
    lede='Jedes ist gleich aufgebaut: was tatsächlich geschieht, warum es geschieht, welche '
         'Vorschriften gelten und was sich tun lässt. Es sind wiederkehrende Muster, nicht die '
         'Akte eines bestimmten Vorhabens.',
    l_ht='Was geschieht', l_ng='Warum es geschieht',
    l_cc='Maßgebliche Vorschriften', l_xl='Was zu tun ist',
    h_bt='Wenn Ihr Vorhaben an einem dieser Punkte hängt',
    bt='Schildern Sie die Lage auf der Seite %s. Nennen Sie, wo das Vorhaben liegt, wie es '
       'finanziert ist und das Datum des Vorgangs — Vorschriften gelten nach dem Zeitpunkt des '
       'Ereignisses.',
    bt_lk='Beratung',
)

VM_DS = [
    ('Grunderwerb und Umsiedlung',
     'Das Baufeld wird in kurzen, unzusammenhängenden Abschnitten übergeben. Die Baufirma erhält '
     'Abschnitt A, während Abschnitt B noch offen ist; Gerät und Personal stehen still, und es '
     'folgen Forderungen nach Stillstandskosten und Fristverlängerung.',
     'Eine Metro führt durch gewachsene Stadtgebiete mit dichter Bebauung und dichten Leitungen. '
     'Der Entschädigungsplan beruht auf Katasterdaten, während die tatsächliche Lage vor Ort sich '
     'weiterentwickelt hat. Zu einem Zeitpunkt genehmigte Kosten werden über mehrere Jahre '
     'ausgezahlt.',
     'Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · NĐ 226/2025 · '
     'Hanoi, in TOD-Bereichen: NQ 66/2026/NQ-HĐND Artikel 11',
     'Führen Sie ein Übergaberegister des Baufeldes nach Stationierung und Datum, dreiseitig '
     'unterzeichnet — es ist der wichtigste Nachweis dafür, ob Stillstandskosten überhaupt '
     'abrechenbar sind. Halten Sie jede Fristverlängerung in einem Vertragsnachtrag fest, nicht im '
     'Schriftwechsel. Gleichen Sie die Auszahlungsliste vierteljährlich gegen die tatsächlichen '
     'Belege ab.'),
    ('Mehrfach angepasste Gesamtinvestitionssumme',
     'Die Gesamtinvestitionssumme wird in einer Höhe genehmigt; einige Jahre später liegen die '
     'tatsächlichen Kosten weit darüber. Während die Anpassung auf Genehmigung wartet, gehen Bau '
     'und Zahlung weiter. Bei der Schlussabrechnung zeigt sich, dass ein Teil der Leistung die '
     'seinerzeit geltende Gesamtinvestitionssumme überschritten hat.',
     'Meist wirken vier Ursachen zusammen: eine auf dünnen Erkundungsdaten beruhende vorläufige '
     'Gesamtinvestitionssumme; Preissteigerung über acht bis fünfzehn Jahre; Planänderungen, weil '
     'der Baugrund anders ist als erwartet; und mit den Bodenpreisen steigende Grunderwerbskosten.',
     'Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (geändert durch NĐ 275/2025) · NĐ 206/2026 zur '
     'Kostensteuerung · NĐ 19/2026 zu Prüfung und Investitionsaufsicht',
     'Die zur Abrechnung vorgelegten Kosten müssen innerhalb der genehmigten '
     'Gesamtinvestitionssumme liegen — für den Überschuss fehlt ohne genehmigte Anpassung die '
     'Grundlage, ihn in den abgerechneten Wert aufzunehmen, selbst wenn die Leistung gebaut und '
     'abgenommen ist. Führen Sie eine Aufstellung der Gesamtinvestitionssumme nach Zeiträumen und '
     'holen Sie die Anpassung ein, bevor Sie den Überschuss ausführen.'),
    ('EPC-Verträge und ausländische Auftragnehmer',
     'Ein EPC-Paket wird nach internationalem Muster geschlossen, pauschal in Fremdwährung, zahlbar '
     'nach Meilensteinen. Bei der Schlussabrechnung hat der Vorhabenträger kein detailliertes '
     'Leistungsverzeichnis zum Abgleich; die nachprüfende Behörde verlangt eine Aufgliederung, und '
     'der Auftragnehmer verweigert sie unter Hinweis auf den Pauschalcharakter.',
     'Internationale Vertragspraxis und inländisches Abrechnungsrecht beruhen auf zwei '
     'verschiedenen Logiken. Im internationalen Muster überträgt der Pauschalpreis das '
     'Mengenrisiko auf den Auftragnehmer; Abrechnungsunterlagen für staatliches Kapital verlangen '
     'dagegen den Nachweis der ausgeführten Mengen.',
     'NĐ 37/2015, geändert durch NĐ 50/2021 (konsolidierte Fassung 07/VBHN-BXD) · '
     'Luật Xây dựng 135/2025/QH15 · Luật Đấu thầu 22/2023/QH15 · VBHN 34/VBHN-BXD · '
     'NĐ 04/2026 zur Schienenindustrie',
     'Schreiben Sie die Preisform in den Vergabeunterlagen fest; mischt ein EPC-Paket mehrere '
     'Leistungsarten, teilen Sie den Preisanhang nach Teilen auf. Verlangen Sie Preisanalyse und '
     'Basisleistungsverzeichnis als Vertragsanhänge auch bei einem Pauschalpreis. Legen Sie '
     'Vertragssprache, Verantwortung für die Übersetzung und Umrechnungskurs fest.'),
    ('Kosten des Probebetriebs vor dem kommerziellen Betrieb',
     'Der Probebetrieb dauert Monate, manchmal über ein Jahr. Fahrstrom, Betriebspersonal, '
     'Versicherung und ausländische Fachleute fallen an. Die Anlagen sind nicht übergeben und '
     'bringen keine Erlöse. Sind das Investitions- oder Betriebskosten?',
     'Bei einer Metro ist die Grenze zwischen dem Ende der Investition und dem Beginn des Betriebs '
     'kein Punkt, sondern ein Zeitraum. Der Probebetrieb ist zugleich ein Abnahmeschritt und eine '
     'Betriebstätigkeit. Baurecht und Recht des öffentlichen Vermögens greifen genau hier nicht '
     'ineinander.',
     'NĐ 207/2026 und TT 32/2026/TT-BXD · TT 62/2026/TT-BXD Metro-Norm · NĐ 16/2026 · '
     'NĐ 15/2025 zu Infrastrukturvermögen · TT 79/2026/TT-BTC',
     'Entscheiden Sie vor dem Probebetrieb, nicht danach: Holen Sie die Genehmigung eines '
     'Dokuments ein, das Umfang, Dauer, Kostenliste und Finanzierungsquelle festlegt. Richten Sie '
     'in der Buchhaltung eine eigene Kennung ein. Behandeln Sie die Unterlagen zur '
     'Systemsicherheitszertifizierung als eigenständige Vertragsposition mit eigener '
     'Kostenberechnung.'),
    ('Anwendung ausländischer Normen und technischer Regelwerke',
     'Planung und Geräte folgen den Normen des Landes, das die Technik liefert. Bei Abnahme und '
     'Schlussabrechnung verlangt die inländische Behörde einen Abgleich mit vietnamesischen '
     'technischen Normen, und viele Kennwerte existieren dort entweder nicht oder werden anders '
     'gemessen.',
     'Vietnam hat erst seit TT 62/2026/TT-BXD vom 30. Juli 2026 ein eigenes technisches Regelwerk '
     'für städtische Schienenbahnen vom Metro-Typ. Linien, die davor begonnen wurden, mussten auf '
     'ausländische Normen zurückgreifen, und jede Linie verwendet die Technik eines anderen Landes.',
     'Hanoi: NQ 40/2025/NQ-HĐND — beachten Sie, dass Artikel 1 Absatz 2 ausdrücklich bestimmt, '
     'dass die städtische Schienenbahn ihren eigenen Weg geht und dem allgemeinen Ablauf jenes '
     'Beschlusses NICHT folgt · TT 62/2026/TT-BXD · TT 44/2025/TT-BXD',
     'Erstellen Sie in der Planungsphase eine Normenvergleichstabelle und lassen Sie sie '
     'genehmigen, statt sie als internes Beratungsdokument zu belassen. Führen Sie bei '
     'Hanoi-Vorhaben NQ 40/2025 nicht als Grundlage für die städtische Schienenbahn an — jener '
     'Beschluss nimmt sie aus; führen Sie Luật Thủ đô 02/2026/QH16 und NQ 188/2025/QH15 an.'),
    ('Schlussabrechnung eines über viele Jahre laufenden Vorhabens',
     'Das Vorhaben hat mehrere Generationen von Verordnungen zu Kostensteuerung, Projektsteuerung '
     'und Abrechnung durchlaufen sowie mehrere Änderungsrunden der Normenrundschreiben. Wer die '
     'Unterlagen erstellt hat, ist fort; frühe Belege liegen im Archiv, und manche sind verblasst.',
     'Das ist schlicht die Natur eines Vorhabens mit acht bis fünfzehn Jahren Lebensdauer. Es lässt '
     'sich nicht vermeiden, nur handhaben.',
     'Die Ketten, die man kennen muss — Projektsteuerung: NĐ 59/2015 → NĐ 15/2021 → NĐ 175/2024 → '
     'NĐ 209/2026 und NĐ 210/2026. Kostensteuerung: NĐ 32/2015 → NĐ 68/2019 → NĐ 10/2021 → '
     'NĐ 206/2026. Abrechnung: TT 09/2016 → TT 10/2020 → NĐ 99/2021 → NĐ 254/2025',
     'Die erste Aufgabe ist, für das Vorhaben eine eigene Übersicht zu bauen, welche Vorschriften '
     'wann galten, und jeden Meilenstein einer Generation zuzuordnen. Eine Schlussfolgerung, die '
     'kein Aktenzeichen des richtigen Zeitraums nennen kann, hält nicht. Stimmen Sie das '
     'ausgezahlte Kapital jährlich mit der auszahlenden Stelle ab, statt bis zum Ende zu warten.'),
    ('TOD und die Abschöpfung des Bodenwertzuwachses',
     'Politisch darf die Stadt einen Teil des Bodenwertzuwachses um die Stationen abschöpfen, um '
     'die Kosten der Linie auszugleichen. In der Praxis kann die ausführende Stelle nicht '
     'ermitteln, wie viel zu erheben ist.',
     'Der Mechanismus ist auf Ebene des Gesetzes und des Volksratsbeschlusses vollständig, doch '
     'auf der untersten Ebene fehlt das Dokument, das ihn beziffert. Hinzu kommt eine zweite '
     'Unstimmigkeit: Die TOD-Planung muss zuerst genehmigt sein, doch sie setzt eine feste Trasse '
     'und feste Stationsstandorte voraus — während die Linie noch umgeplant wird.',
     'Luật Thủ đô 02/2026/QH16 Artikel 12 · NQ 188/2025/QH15 · Hanoi: NQ 71/2025, NQ 66/2026, '
     'NQ 67/2026 · Ho-Chi-Minh-Stadt: NQ 21/2026 (ersetzt NQ 38/2025 ab 19. Juni 2026), NQ 90/2025',
     'Ziehen Sie die buchhalterische Grenze zwischen Linienvorhaben und TOD-Vorhaben von Anfang '
     'an. Beobachten Sie für Hanoi das Amtsblatt auf den Beschluss zum TOD-Vorteilskoeffizienten, '
     'sobald er ergeht — bis dahin ist jede TOD-Einnahmezahl eine interne Schätzung und gehört '
     'nicht in einen förmlichen Finanzierungsplan.'),
    ('Unterirdischer Raum',
     'Unterirdische Stationen und Tunnelabschnitte liegen unter Flächen vieler verschiedener '
     'Nutzerinnen und Nutzer. Bis in welche Tiefe wird Land zurückgenommen, wie wird der '
     'Untergrund entschädigt, wie hoch ist der Bodenzins für ein unterirdisches Bauwerk, und wie '
     'weit darf die Handelsfläche innerhalb einer unterirdischen Station verwertet werden?',
     'Das herkömmliche Bodenrecht verwaltet nach Flurstücken an der Oberfläche. Der unterirdische '
     'Raum ist eine neue Verwaltungsebene, die erst im Luật Thủ đô und in den Beschlüssen des '
     'Hanoier Volksrats von 2026 angelegt wurde.',
     'Luật Thủ đô 02/2026/QH16 Artikel 11 · Hanoi: NQ 64/2026 (Planung des unterirdischen Raums), '
     'NQ 65/2026 (Entgelte), NQ 62/2026 (Investitionsbegünstigungen)',
     'Legen Sie die Unterkante jeder Station und jedes Tunnelabschnitts in Planungs- und '
     'Bestandsunterlagen fest und halten Sie sie dort fest — die Fünfzehn-Meter-Schwelle '
     'entscheidet unmittelbar über die finanzielle Verpflichtung. Trennen Sie die betrieblich '
     'genutzte von der gewerblich verwerteten unterirdischen Fläche, denn für beide gelten '
     'unterschiedliche Finanzregime.'),
    ('Schulung des Betriebspersonals',
     'Die Kosten für die Schulung von Triebfahrzeugführenden, Disponierenden und '
     'Instandhaltungspersonal gehören zur Gesamtinvestitionssumme. Bei der Schlussabrechnung stellt '
     'sich die Frage: Schafft das einen Vermögenswert? Wenn nicht, wie ist es zu behandeln?',
     'Schulung ist wirtschaftlich Investitionskosten, bildet buchhalterisch aber kein '
     'Anlagevermögen. Geschulte Personen können vor der Eröffnung ausscheiden, was die Frage nach '
     'der Wirksamkeit des eingesetzten Kapitals aufwirft.',
     'NQ 188/2025/QH15, die Gruppe der Mechanismen zu Technologietransfer und Personalausbildung · '
     'QĐ 2230/QĐ-TTg, der Plan für Eisenbahnpersonal bis 2035 · NĐ 254/2025',
     'Klären Sie es in der Vorbereitungsphase: welcher Kostenart die Schulung zugehört und ob sie '
     'dem Anlagewert zuzurechnen ist. Ist sie es nicht, bedarf es der Zulassung durch die '
     'zuständige Stelle — ein eigenes Verfahren, das der Vorhabenträger nicht allein entscheiden '
     'kann. Bewahren Sie die Nachweise vollständig auf, denn dies ist eine Kostenposition ohne '
     'körperliches Ergebnis.'),
    ('Technologietransfer und Lokalisierung',
     'Der Vertrag enthält eine Klausel zum Technologietransfer, beschreibt ihn aber allgemein, ohne '
     'konkreten Zeitplan, ohne Abnahmekriterien und ohne eigenen Zahlungsmeilenstein. Bei der '
     'Schlussabrechnung kann niemand feststellen, ob die Pflicht erfüllt wurde oder welchen Anteil '
     'am Vertragspreis sie ausmacht.',
     'Technologietransfer ist eine schwer zu beziffernde Pflicht. Die verkaufende Seite hat einen '
     'Anreiz, den Kern zurückzuhalten. Der Käuferseite fehlt zum Zeitpunkt der Unterschrift oft die '
     'technische Fähigkeit, genau zu bestimmen, was sie erhalten muss.',
     'NQ 188/2025/QH15 · NĐ 04/2026 zur Beauftragung und Bestellung von Leistungen der '
     'Schienenindustrie · QĐ 498/QĐ-TTg zur Umstrukturierung der vietnamesischen Eisenbahn · '
     'Luật Chuyển giao công nghệ 07/2017/QH14',
     'Legen Sie den Transferplan als Tabelle in die Vergabeunterlagen: Inhalt — Form — '
     'Abnahmekriterium — Termin — zugeordneter Wert. Ohne Wertspalte lässt er sich nicht '
     'abrechnen. Machen Sie ihn zu einer eigenen Zahlungsposition und behalten Sie den letzten '
     'Prozentsatz ein, bis der gesamte Plan abgenommen ist.'),
]
