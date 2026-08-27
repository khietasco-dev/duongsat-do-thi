# -*- coding: utf-8 -*-
"""Ban TIENG DUC: trang VAN BAN (Vorschriften suchen) va THU VIEN RUI RO (Risikokatalog).

TEN VAN BAN GIU NGUYEN TIENG VIET — do la ten chinh thuc, dich ra thi khong tra cuu duoc.

⚠ Trang /de/van-ban/ nam o thu muc khac voi kho tep /van-ban/tep/ nen phai di qua
  _tep_lang() doi duong dan thanh @/van-ban/tep/... — ban 17 da vap 161 lien ket hong.
"""

# =================================================================== VAN BAN
VB = dict(
    td='Vorschriften zur städtischen Schienenbahn — Suche',
    mt='51 Rechtsvorschriften zu Schienenbahn- und TOD-Vorhaben in Vietnam, filterbar nach '
       'Ebene, Gebiet, Jahr und Geltung, mit Word- oder PDF-Datei.',
    duong='Vorschriften',
    h1='Vorschriften suchen',
    lede='Einundfünfzig Vorschriften, die städtische Schienenbahn- und TOD-Vorhaben regeln, jede '
         'mit ihrer Word- oder PDF-Datei. Die Titel bleiben auf Vietnamesisch — das sind die '
         'amtlichen Bezeichnungen, und genau sie brauchen Sie, um anderswo zu zitieren oder zu '
         'suchen.',
    h_cach='So nutzen Sie diese Seite',
    cach=[
        ('Diakritika im Suchfeld sind optional',
         'Die Dateinamen im Bestand tragen keine Diakritika, doch das Suchfeld entfernt sie auf '
         'beiden Seiten. „đường sắt“ und „duong sat“ liefern dasselbe Ergebnis.'),
        ('Nach Aktenzeichen suchen',
         'Wenn Sie die Nummer erinnern, geben Sie die Nummer ein: „188“, „62/2026“, „15/2025“. '
         'Das geht schneller, als sich den vollen Titel ins Gedächtnis zu rufen.'),
        ('Die Filter greifen zusammen',
         'Die vier Filter wirken miteinander und mit dem Suchfeld. Zum Beispiel Thông tư + Hanoi '
         '+ in Kraft.'),
        ('Auf den Titel klicken öffnet das Dokument',
         'Ein Klick auf den Titel öffnet die Word-Fassung; fehlt sie, öffnet die PDF-Fassung. '
         'In der Spalte <b>Datei öffnen</b> wählen Sie das Format selbst.'),
        ('Lange Vorschriften erscheinen in mehreren Teilen',
         'Das Amtsblatt veröffentlicht lange Vorschriften in mehreren Ausgaben. Diese erscheinen '
         'als <b>W1 W2…</b> oder <b>P1 P2…</b> — für den vollständigen Text brauchen Sie alle '
         'Teile.'),
    ],
    h_co='Was der Bestand enthält',
    tk=['Vorschriften', 'Word- und PDF-Dateien', 'Word und PDF', 'nur PDF',
        'Konsolidierte Fassungen', 'Örtliche Vorschriften'],
    h_cap='Vier Ebenen — in welcher Reihenfolge zu lesen',
    cap=[
        ('Gesetze und Beschlüsse der Nationalversammlung',
         'Das rechtliche Fundament. Für die städtische Schienenbahn zuerst die konsolidierte '
         'Fassung des Luật Đường sắt lesen, dann Nghị quyết 188/2025 zum Sondermechanismus — das '
         'ist die Vorschrift, die den Verfahrensablauf tatsächlich verändert.'),
        ('Verordnungen',
         'Die Durchführungsbestimmungen im Einzelnen. Zu lesen ist die konsolidierte Fassung '
         'VBHN 34/VBHN-BXD mit 143 Artikeln zur technischen Gesamtplanung und zum '
         'Sondermechanismus.'),
        ('Rundschreiben und technische Normen',
         'Normen, Einheitspreise, Formulare und technische Anforderungen. Diese Ebene ändert sich '
         'am häufigsten — prüfen Sie stets, welche Fassung seinerzeit galt.'),
        ('Örtliche Vorschriften',
         'Beschlüsse des Volksrats der Provinz. Sie entscheiden über das Geld: TOD-Einnahmen, '
         'Entgelte für den unterirdischen Raum, Entschädigungspolitik. Sie gelten nur innerhalb '
         'dieser Provinz.'),
    ],
    h_luu='Zwei Punkte zur Beachtung',
    luu=[
        ('Eine Vorschrift gilt nach dem Zeitpunkt des Ereignisses',
         'Eine 2022 entstandene Kostenposition richtet sich nach dem, was 2022 galt, nicht nach '
         'dem heute Geltenden. Dies ist der häufigste Grundlagenfehler in '
         'Schlussabrechnungsunterlagen.'),
        ('„Außer Kraft“ heißt nicht „unerheblich“',
         'Eine außer Kraft getretene Vorschrift regelt weiterhin alles, was während ihrer Geltung '
         'geschehen ist. Genau deshalb behalten wir außer Kraft getretene Vorschriften im Bestand '
         '— entsprechend gekennzeichnet.'),
    ],
    l_cap='Ebene', l_so='Aktenzeichen', l_ten='Titel', l_nam='Jahr', l_hl='Geltung',
    l_tep='Datei öffnen',
    hl_con='In Kraft', hl_het='Außer Kraft', hn='Konsolidiert',
    loc_tim='Suche', loc_cap='Ebene', loc_dia='Gebiet', loc_nam='Jahr', loc_tt='Geltung',
    loc_tatca='Alle',
    tim_gy='Titel, Aktenzeichen oder Stichwort',
    dem='%d von %d Vorschriften',
)

CAP_DE = {'Luật & Nghị quyết QH': 'Gesetz / NV-Beschluss', 'Nghị định': 'Verordnung',
          'Thông tư': 'Rundschreiben', 'Văn bản khác': 'Sonstiges'}
DIA_DE = {'Toàn quốc': 'Landesweit', 'Hà Nội': 'Hanoi', 'TP. Hồ Chí Minh': 'Ho-Chi-Minh-Stadt'}

# =================================================================== THU VIEN RUI RO
RR = dict(
    td='Risikokatalog der Schlussabrechnungsprüfung',
    mt='Dreiunddreißig Risiken in acht Gruppen für die Schlussabrechnungsprüfung eines '
       'städtischen Schienenbahnvorhabens: woran man sie erkennt und wie man sie prüft.',
    duong='Risikokatalog',
    h1='Risikokatalog für die Schlussabrechnungsprüfung',
    lede='Dreiunddreißig Risiken in acht Gruppen. Zu jedem: woran man es erkennt und wie man es '
         'prüft. Nutzen Sie den Katalog als Checkliste bei der Prüfungsplanung oder als '
         'Selbstprüfung, bevor Abrechnungsunterlagen zur Nachprüfung gehen.',
    h_ng='Woher dieser Katalog stammt und was er nicht ist',
    ng='Dieser Katalog ist aus Berufserfahrung und öffentlich zugänglichem Material '
       'zusammengestellt. Er ist eine <b>allgemeine Orientierung</b>. Nichts darin stammt aus den '
       'Unterlagen einer bestimmten Stelle, und kein Eintrag beschreibt ein tatsächliches '
       'Vorhaben. Lesen Sie ihn als Liste prüfenswerter Punkte — nicht als Vorwurf gegen '
       'irgendjemanden.',
    h_ds='Die acht Gruppen',
    l_dh='Woran man es erkennt', l_kt='Wie man es prüft',
    muc=dict(cao='Hoch', trung='Mittel', thap='Gering'),
    l_muc='Aufmerksamkeit',
    h_dung='So nutzen Sie ihn',
    dung=[
        'Gehen Sie ihn bei der Planung durch und markieren Sie, welche Punkte auf dieses Vorhaben '
        'zutreffen. Ausgeschlossene Punkte begründen Sie schriftlich — das ist ein Nachweis von '
        'Urteilsbildung, nicht von Bequemlichkeit.',
        'Bei der Durchführung ist die Spalte „Wie man es prüft“ ein Ausgangspunkt und kein Ersatz '
        'für das Prüfungsprogramm.',
        'Bevor Unterlagen zur Nachprüfung gehen, kann auch der Vorhabenträger dieselbe Liste zur '
        'Selbstprüfung nutzen. Die meisten Punkte lassen sich noch beheben, wenn sie rechtzeitig '
        'auffallen.',
    ],
    h_bt='Wenn Sie dies auf Ihr eigenes Vorhaben angewandt haben möchten',
    bt='Senden Sie uns die Einzelheiten über die Seite %s. Wir sagen Ihnen, welche Gruppen für '
       'die Phase, in der Ihr Vorhaben steht, am wichtigsten sind.',
    bt_lk='Beratung',
)

# 8 nhom, moi rui ro: (ten, dau hieu, kiem the nao, muc)
RR_NHOM = [
    ('Rechtliche Unterlagen', [
        ('Der Investitionsablauf ist vertauscht oder ein Schritt fehlt',
         'Ein Vertrag vor der Genehmigungsentscheidung geschlossen; Baubeginn vor der '
         'Baugenehmigung.',
         'Das Unterzeichnungsdatum jedes Dokuments auf einem Zeitstrahl abgleichen — nicht nur, '
         'ob das Dokument vorliegt.', 'cao'),
        ('Genehmigung auf der falschen Ebene erteilt',
         'Die unterzeichnende Person ist für diese Vorhabenklasse oder Wertspanne nicht zuständig.',
         'Die Funktion der unterzeichnenden Person gegen die am Unterzeichnungstag geltende '
         'Zuständigkeitsregelung stellen.', 'cao'),
        ('Sondermechanismus außerhalb seines Anwendungsbereichs angewandt',
         'Verkürzte Verfahren bei einem Vorhaben oder Gebiet, das nicht zum Erprobungsbereich '
         'gehört.',
         'Vom Vorhabenträger das Dokument verlangen, das die Zugehörigkeit zum Anwendungsbereich '
         'belegt.', 'cao'),
        ('Unterlagen nachträglich erstellt und rückdatiert',
         'Protokolle und Entscheidungen spät erstellt, tragen aber das Datum, das sie hätten '
         'tragen sollen.',
         'Papier und Layout innerhalb derselben Akte vergleichen; gegen Bautagebuch und '
         'Zahlungsbelege desselben Zeitraums abgleichen.', 'trung'),
    ]),
    ('Finanzierung und Zahlung', [
        ('Das Buchwerk des Vorhabenträgers weicht von der auszahlenden Stelle ab',
         'Das ausgezahlte Kapital laut Buchhaltung weicht von der Zahl der Staatskasse oder der '
         'abwickelnden Bank ab.',
         'Für jedes Jahr eine unterzeichnete Abstimmung verlangen; jede Differenz einzeln bis zur '
         'Ursache verfolgen — keine saldierte Summe akzeptieren.', 'cao'),
        ('Zahlungen übersteigen den Vertragswert',
         'Die Summe aller Zahlungstranchen übersteigt den Vertragspreis zuzüglich wirksamer '
         'Nachträge.',
         'Alle Tranchen aufaddieren und gegen den angepassten Vertragspreis stellen.', 'cao'),
        ('Vorauszahlungen nicht vollständig verrechnet',
         'Eine vertragliche Vorauszahlung ist trotz fertiggestellter Leistung nicht vollständig '
         'verrechnet.',
         'Je Vertrag ein Verzeichnis über Vorauszahlung und Verrechnung führen und gegen die '
         'Vorauszahlungsbürgschaft abgleichen.', 'trung'),
        ('Kosten entstanden ohne zugewiesene Mittel',
         'Mengen ausgeführt, ohne dass im öffentlichen Investitionsplan Mittel zugewiesen sind.',
         'Die zur Abrechnung vorgelegten Kosten gegen die jährliche Mittelzuweisung abgleichen.',
         'trung'),
    ]),
    ('Mengen und Einheitspreise', [
        ('Abgerechnete Menge übersteigt die abgenommene Menge',
         'Die Abrechnungsaufstellung weist mehr aus als das zugehörige Abnahmeprotokoll.',
         'Dreifach abgleichen: Abrechnungsaufstellung — Abnahmeprotokoll — Bestandsplan.', 'cao'),
        ('Dieselbe Menge in zwei Vergabepaketen gezählt',
         'Eine Leistungsposition in zwei Paketen gezählt, meist an der Nahtstelle zweier Pakete.',
         'Doppelungen nach Preiskennziffer und Stationierung suchen; auf Paketgrenzen besonders '
         'achten.', 'cao'),
        ('Norm des falschen Zeitraums angewandt',
         'Heutige Normen auf Mengen angewandt, die Jahre zuvor abgenommen wurden.',
         'Zuerst den maßgeblichen Zeitpunkt jeder Position festlegen, dann die zu diesem Zeitpunkt '
         'geltende Norm heranziehen.', 'cao'),
        ('Sonderleistung ohne genehmigte Norm',
         'Tunnelvortrieb, Montage der Signaltechnik, integrierte Erprobung — im allgemeinen '
         'Normensystem nicht enthalten.',
         'Die Entscheidung über die Genehmigung einer neuen Norm verlangen; ohne sie fehlt der '
         'Position die Abrechnungsgrundlage.', 'cao'),
        ('Preisanpassung passt nicht zur Form des Vertragspreises',
         'Preissteigerung auf einen Pauschalvertrag oder einen Vertrag mit festen Einheitspreisen '
         'gezahlt.',
         'Zuerst die im Vertrag bezeichnete Preisform bestimmen, dann prüfen, ob die Anpassung '
         'überhaupt zulässig ist.', 'cao'),
        ('Falscher Preisindex verwendet',
         'Ein Index einer anderen Provinz, einer anderen Bauart oder eines anderen Zeitraums.',
         'Die Indexquelle gegen die Vertragsbedingungen und die Veröffentlichung der zuständigen '
         'Stelle abgleichen.', 'trung'),
    ]),
    ('Verträge', [
        ('Die Form des Vertragspreises weicht von der tatsächlichen Abrechnung ab',
         'Ein Pauschalvertrag wird nach Aufmaß abgerechnet oder umgekehrt.',
         'Preisklausel und Zahlungsklausel lesen, bevor eine einzige Zahl geprüft wird.', 'cao'),
        ('Nachtrag nach Fertigstellung der Leistung unterzeichnet',
         'Ein Nachtrag zu Mengen oder Preis, unterzeichnet nach der Abnahme dieses Teils.',
         'Das Unterzeichnungsdatum des Nachtrags gegen das Abnahmedatum derselben Leistung stellen.',
         'cao'),
        ('EPC-Vertrag ohne detailliertes Leistungsverzeichnis',
         'Ein Vertrag internationaler Form beschreibt den Umfang über das Ergebnis, ohne '
         'Leistungsverzeichnis zum Abgleich.',
         'Preisanalyse und Basisleistungsverzeichnis verlangen; fehlen beide, die Beschränkung des '
         'Prüfungsumfangs ausdrücklich benennen.', 'cao'),
        ('Der angepasste Preis übersteigt den genehmigten Paketpreis',
         'Vertragspreis zuzüglich Nachträge übersteigt den Paketpreis im Auswahlplan.',
         'Aufaddieren und gegen die Genehmigungsentscheidung zum Auswahlplan stellen.', 'trung'),
    ]),
    ('Projektsteuerungs-, Beratungs- und sonstige Kosten', [
        ('Projektsteuerungskosten über der Norm',
         'Die tatsächlichen Kosten übersteigen den Betrag, der sich aus dem Prozentsatz auf Bau- '
         'und Gerätekosten ergibt.',
         'Mit der zwischen den beiden Größenschwellen interpolierten Norm neu berechnen und gegen '
         'den geltend gemachten Betrag stellen.', 'trung'),
        ('Bereits in der Norm enthaltene Posten zusätzlich abgerechnet',
         'Büromaterial sowie Strom und Wasser der Projektleitung zusätzlich zur Norm abgerechnet.',
         'Die Liste der von der Norm bereits abgedeckten Kosten gegen die tatsächlichen Ausgaben '
         'stellen.', 'trung'),
        ('Beratungskosten über dem Vertrag',
         'Der abgerechnete Wert eines Beratungsvertrags übersteigt den Vertragspreis zuzüglich '
         'Nachträge.',
         'Jeden Beratungsvertrag einzeln abgleichen und prüfen, ob die Leistungen tatsächlich '
         'erbracht wurden.', 'trung'),
    ]),
    ('Vermögenswerte und Übergabe', [
        ('Der Anlagewert stimmt nicht mit den Investitionskosten überein',
         'Die Abstimmgleichung geht nicht auf: Kosten abzüglich nicht dem Anlagewert zuzurechnender '
         'Beträge und abzüglich überzähligen Bestands ergibt nicht den Anlagewert.',
         'Die Abstimmgleichung über einen einzigen Zahlenbestand laufen lassen; jede Differenz vor '
         'der Erteilung nachverfolgen.', 'cao'),
        ('Gemeinkosten ohne Grundsatz verteilt',
         'Gemeinkosten nach Gefühl auf die Positionen verteilt statt im Verhältnis zum Kapital.',
         'Die Verteilungsaufstellung prüfen und den Verteilungsmaßstab gegen den genehmigten '
         'Grundsatz stellen.', 'trung'),
        ('Vermögenswerte fehlen oder doppeln sich zwischen den übernehmenden Stellen',
         'Dieselbe Position erscheint in zwei Übergabeprotokollen oder in keinem.',
         'Die Gesamtaufstellung der Vermögenswerte gegen die Summe aller Übergabeprotokolle '
         'abgleichen.', 'trung'),
        ('Kosten ohne Zulassung vom Anlagewert ausgenommen',
         'Schäden oder Kosten einer aufgehobenen Position ohne Entscheidung der zuständigen Stelle.',
         'Die zulassende Entscheidung verlangen; ohne sie muss der Betrag in der Schwebe bleiben '
         'und darf nicht übertragen werden.', 'cao'),
    ]),
    ('Forderungen, Verbindlichkeiten und überzähliger Bestand', [
        ('Schulden der falschen Partei zugeordnet',
         'Salden nach Paketbezeichnung statt nach Rechtsträger des Auftragnehmers erfasst oder '
         'mehrere Auftragnehmer zusammengefasst.',
         'Salden je Rechtsträger abgleichen; Bestätigungsanfragen unter Steuerung der Prüferin '
         'oder des Prüfers versenden.', 'trung'),
        ('Bestätigungen vom Vorhabenträger versandt und empfangen',
         'Die Prüferin oder der Prüfer steuert Versand und Empfang nicht, wodurch der Nachweis '
         'seine Verlässlichkeit verliert.',
         'Die Prüferin oder der Prüfer steuert die Versandanschrift und empfängt die Antworten '
         'unmittelbar.', 'cao'),
        ('Überzähliges Material und Gerät ohne Verwertungsplan',
         'Nach Fertigstellung liegt Material im Lager, ohne dass über seinen Verbleib entschieden '
         'ist.',
         'Körperlich aufnehmen und gegen die Bücher abgleichen; im Bericht einen Verwertungsweg '
         'empfehlen.', 'thap'),
    ]),
    ('Risiken, die für städtische Schienenbahnvorhaben eigentümlich sind', [
        ('Kosten des Probebetriebs falsch zugeordnet',
         'Strom, Betriebspersonal und Versicherung während des Probebetriebs ohne Grundlage den '
         'Investitionskosten zugeordnet.',
         'Das vor Beginn des Probebetriebs erstellte Dokument verlangen, das Umfang und '
         'Finanzierungsquelle genehmigt.', 'cao'),
        ('Kosten der Systemsicherheitsbewertung fehlen in der Gesamtinvestitionssumme',
         'Eine von einer unabhängigen ausländischen Stelle erbrachte Position, bei der '
         'Vorhabenvorbereitung häufig übersehen.',
         'Den Vertrag zur Sicherheitsbewertung gegen die genehmigte Gesamtinvestitionssumme '
         'abgleichen.', 'trung'),
        ('Kursdifferenzen bei Darlehen und eingeführten Geräten',
         'Auf verschiedene Geschäftsarten uneinheitlich angewandte Kurse oder Kurse des falschen '
         'Stichtags.',
         'Kursdifferenzen gesondert prüfen; die angewandten Kurse gegen die Vertragsbedingungen '
         'stellen.', 'cao'),
        ('Unklar, ob Schulung und Technologietransfer einen Vermögenswert schaffen',
         'Große Beträge, die kein Anlagevermögen bilden und bei der Schlussabrechnung leicht in '
         'der Schwebe bleiben.',
         'Eine Entscheidung der zuständigen Stelle darüber verlangen, ob sie dem Anlagewert '
         'zuzurechnen sind.', 'trung'),
        ('Keine klare Kostengrenze zwischen Linie und TOD-Bereich',
         'Zahlungsströme und Vermögenswerte beider vermischen sich und lassen sich bei der Übergabe '
         'nicht mehr trennen.',
         'Prüfen, ob ein Grundsatz zur Kostentrennung bereits in der Vorbereitungsphase festgelegt '
         'wurde.', 'trung'),
    ]),
]
