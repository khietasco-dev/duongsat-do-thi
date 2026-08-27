# -*- coding: utf-8 -*-
"""Ban TIENG DUC: 9 trang dich vu cap 2 — /de/dich-vu/<slug>/.

Ten van ban phap luat GIU NGUYEN so hieu tieng Viet.
Phan "Rechtsgrundlagen" ghi ro la CACH DOC CUA ASCO, khong phai ban dich chinh thuc
(KHUNG['cancu_nhac']) — cau nay bat buoc phai co o moi thu tieng.

🔴 Nhac lai bay don vi tien: "Billion" tieng Duc = 10^12.
   1 ty dong = 1 Milliarde VND. Xem ds_de_qt.py phan dau file.
"""

KHUNG = dict(
    duong_nha='Start', duong_dv='Leistungen',
    h_vande='Häufige Probleme',
    h_cancu='Rechtsgrundlagen',
    cancu_nhac='Der nachstehende Wortlaut ist <b>unsere Lesart</b> der jeweiligen Bestimmung und '
               'keine amtliche Übersetzung. Rechtsverbindlich ist allein der vietnamesische Text '
               '— jedes Dokument lässt sich im Bereich %s öffnen.',
    cancu_lk='Vorschriften suchen',
    h_lamgi='Was wir tun',
    h_daura='Was Sie erhalten',
    h_khinao='Wann Sie uns ansprechen sollten',
    luu_h='Zwei Bedingungen, die wir vorweg nennen.',
    luu='Erstens ist dies eine Leistung nach Artikel 40 Absatz 2 des Luật Kiểm toán độc lập — '
        'eine Prüfungsgesellschaft muss sie vor der Erbringung beim Finanzministerium anmelden. '
        'Zweitens muss dieses Mandat, falls wir Ihre Organisation prüfen oder dies zu erwarten '
        'ist, vor Vertragsschluss eine Unabhängigkeitsprüfung nach Artikel 30 desselben Gesetzes '
        'durchlaufen. Diese Prüfung führen wir zuerst durch, und fällt sie negativ aus, sagen wir '
        'es offen und lehnen ab.',
    bt_h='Der nächste Schritt',
    bt='Schildern Sie Ihre Lage auf der Seite %s oder rufen Sie <b>0825092007</b> an. Wir lesen '
       'es, ordnen es ein und antworten innerhalb von 24 Arbeitsstunden — auch dann, wenn die '
       'Antwort lautet, dass die Arbeit außerhalb dessen liegt, was uns gestattet ist.',
    bt_lk='Beratung anfragen',
    bt_ve='← Alle neun Leistungen ansehen',
)

DE = {
    'thu-hoi-von-tod': dict(
        td='Rückfluss über TOD-Flächen — Beratung',
        mt='Zahlungsstrommodell für TOD-Flächen nach Artikel 25 Luật Đường sắt: Zeitpunkt '
           'der Einnahmen, verbleibender Anteil der Provinz, Sensitivitäten.',
        ten='Beratung zum Rückfluss über TOD-Flächen',
        lede='Eine städtische Schienenbahn trägt sich fast nie aus Fahrgeldeinnahmen. Die '
             'eigentliche Rückflussquelle ist der Wertzuwachs der Flächen um die Stationen — und '
             'das Gesetz eröffnet der Provinz nun einen Weg, diesen Wert einzubehalten. Schwierig '
             'ist es, aus einem gesetzlichen Mechanismus einen Zahlungsstrom zu machen, den man in '
             'einen Finanzierungsplan einstellen und vor der prüfenden Behörde vertreten kann.',
        van_de=[
            'Der Mechanismus zur Schaffung von Versteigerungsflächen besteht, doch niemand hat '
            'beziffert, wie viel er einbringt und wann.',
            'Versteigerungserlöse fließen später; der Grunderwerb muss zuerst bezahlt werden. '
            'Diese Lücke wird selten modelliert.',
            'Der Finanzierungsplan der Linie und der Plan zur Flächenverwertung stammen von zwei '
            'verschiedenen Stellen, und die Zahlen passen nicht zusammen.',
            'Die unterstellten Bodenpreise sind optimistisch. Wenn die tatsächliche Versteigerung '
            'dahinter zurückbleibt, hat sich das Vorhaben längst auf einen Terminplan festgelegt.',
        ],
        can_cu=[
            ('Luật Đường sắt (konsolidierte Fassung 75/VBHN-VPQH) — Artikel 25 Absatz 2',
             'Der Volksrat der Provinz kann beschließen, Mittel des örtlichen Haushalts für ein '
             'eigenständiges öffentliches Investitionsvorhaben einzusetzen, das Entschädigung, '
             'Unterstützung und Umsiedlung nach der Planung des TOD-Bereichs durchführt, um '
             'Flächen für die Versteigerung zu schaffen.'),
            ('Luật Đường sắt — Artikel 25 Absatz 3',
             'Von den Erlösen aus der Verwertung von Flächen im TOD-Bereich verbleiben bei der '
             'Staatsbahn nach Abzug der Entschädigungs- und Nebenkosten 50 % bei der Provinz, '
             '50 % fließen an den Zentralhaushalt. Bei örtlichen Bahnen verbleiben 100 % bei der '
             'Provinz.'),
            ('Luật Đường sắt — Artikel 3 Absätze 6 und 7',
             'Begriffsbestimmungen des TOD-Bereichs und des örtlichen Schienenbahnvorhabens nach '
             'dem TOD-Modell. Die richtige Einordnung entscheidet darüber, welcher Anteil gilt.'),
        ],
        lam_gi=[
            ('Vorhabenart und verbleibenden Anteil bestimmen',
             'Staatsbahn oder örtliche Bahn entscheidet, ob der Anteil 50 % oder 100 % beträgt. '
             'Das ist die erste Frage, denn sie verändert jede nachfolgende Zahl.'),
            ('Flächenaufstellung je TOD-Bereich erstellen',
             'Fläche, Bestand, Planungskennwerte nach Anpassung sowie der erwartete Zeitpunkt, zu '
             'dem jedes Flurstück versteigerungsfähig wird.'),
            ('Den Zahlungsstrom in beide Richtungen modellieren',
             'Abfluss: Entschädigung, Unterstützung, Umsiedlung und die Kosten ihrer Durchführung. '
             'Zufluss: Versteigerungserlöse nach Tranchen. Die Lücke dazwischen muss der örtliche '
             'Haushalt zwischenzeitlich tragen.'),
            ('Sensitivitäten rechnen',
             'Bodenpreise 10–30 % niedriger, Versteigerungstermine ein bis drei Jahre später, ein '
             'geringerer Anteil verkaufter Flurstücke. Das Ergebnis zeigt, wie viel der Plan '
             'verkraftet.'),
            ('Die Begründung schreiben',
             'In der Sprache einer Vorlage, mit genauer Angabe der Bestimmungen, sodass die '
             'prüfende Stelle jede Zahl nachvollziehen kann.'),
        ],
        dau_ra=[
            'Eine TOD-Flächenaufstellung je Bereich mit erwarteten Zeitpunkten',
            'Ein Zahlungsstrommodell zu den Flächen, das Sie öffnen und bearbeiten können — keine '
            'Blackbox',
            'Sensitivitätstabellen zu Bodenpreis und Zeitpunkt',
            'Eine Begründung zum Kapitalrückfluss mit vollständigen Fundstellen',
        ],
        khi_nao='Bei Erstellung der Vor- oder Machbarkeitsstudie einer Linie mit TOD-Anteil; wenn '
                'der Volksrat der Provinz über den Einsatz örtlicher Haushaltsmittel zur Schaffung '
                'von Versteigerungsflächen beschließen will; oder wenn ein bestehender '
                'Finanzierungsplan zurückgegeben wurde, weil die Rückflussseite nicht überzeugt.',
    ),
    'phuong-an-tai-chinh': dict(
        td='Finanzierungsplan einer städtischen Schienenbahnlinie',
        mt='Finanzierungsplan über die gesamte Lebensdauer: Investitionskosten, '
           'Betriebszuschuss, TOD-Erlöse, Belastung des Provinzhaushalts, Sensitivitäten.',
        ten='Beratung zum Lebensdauer-Finanzierungsplan der Linie und ihres TOD-Vorhabens',
        lede='Eine städtische Schienenbahnlinie endet nicht am Tag der Eröffnung. Danach folgen '
             'zwei bis drei Jahrzehnte Betrieb, Instandhaltung, Geräteerneuerung und Zuschuss. Ein '
             'Finanzierungsplan, der mit der Fertigstellung endet, lässt die Hälfte der '
             'Lebensdauer aus.',
        van_de=[
            'Die Investitionskosten werden sorgfältig ermittelt, die Betriebs- und '
            'Instandhaltungskosten über die Lebensdauer dagegen grob geschätzt.',
            'Der Zuschuss für den öffentlichen Personenverkehr geht nicht in den langfristigen '
            'Ausgleich des Provinzhaushalts ein.',
            'Die große Geräteerneuerung in den Jahren 15 bis 20 taucht in den Unterlagen nirgends '
            'auf.',
            'Erlöse außerhalb des Fahrgelds — Werbung, Einzelhandel in Stationen, '
            'Flächenverwertung — fehlen im Modell.',
        ],
        can_cu=[
            ('Luật Đường sắt — Artikel 5 Absätze 1 und 2',
             'Der Staat weist Haushaltsmittel für Investition, Ertüchtigung und Instandhaltung '
             'vorrangig zu und bezuschusst den öffentlichen Personenverkehr auf städtischen '
             'Schienenbahnen.'),
            ('Luật Đường sắt — Artikel 32 Absätze 3 und 4',
             'Fehlt ein inländisches System von Normen und Einheitspreisen für Betrieb und '
             'Instandhaltung oder passt es nicht, dürfen von in- oder ausländischen Stellen '
             'veröffentlichte Normen verwendet werden. Kosten für Probebetrieb, Schulung und '
             'Technologietransfer gehören zur Gesamtinvestitionssumme.'),
            ('Nghị định 206/2026/NĐ-CP',
             'Steuerung der Bauinvestitionskosten — Gesamtinvestitionssumme, Kostenberechnungen, '
             'Paketkosten sowie Betriebs- und Instandhaltungskosten.'),
        ],
        lam_gi=[
            ('Den Zahlungsstromrahmen über die Lebensdauer setzen',
             'Investitionsphase, eingeschwungener Betrieb und die Meilensteine großer Erneuerungen.'),
            ('Die Erlösarten trennen',
             'Fahrgeldeinnahmen, Zuschuss, Erlöse außerhalb des Fahrgelds sowie, soweit '
             'einschlägig, TOD-Flächenerlöse.'),
            ('Betriebs- und Instandhaltungskosten festlegen',
             'Inländische Normen, soweit vorhanden; sonst Normen einer vergleichbaren Linie, '
             'umgerechnet auf den Bewertungsstichtag nach Artikel 32.'),
            ('Gegen den Provinzhaushalt prüfen',
             'Zeigen, was der Haushalt Jahr für Jahr bereitstellen muss und welchen Anteil das an '
             'den örtlichen Investitionsausgaben ausmacht.'),
            ('Sensitivitäten rechnen und die Bruchstellen finden',
             'Nachfrage unter der Prognose, steigende Strompreise, Wechselkursbewegungen bei '
             'Fremdwährungsverträgen.'),
        ],
        dau_ra=[
            'Ein Lebensdauer-Finanzmodell mit Annahmen in einem eigenen Tabellenblatt',
            'Eine Jahr-für-Jahr-Darstellung der Belastung des Provinzhaushalts',
            'Sensitivitätsanalyse und die Bruchstellen des Plans',
            'Eine Begründung, gegliedert für die Vorlage',
        ],
        khi_nao='Bei Erstellung oder Prüfung einer Vor- oder Machbarkeitsstudie; bei Anpassung der '
                'Investitionsleitlinie; oder wenn eine Linie sich dem Betrieb nähert und die '
                'Provinz wissen muss, was sie jährlich einplanen muss.',
    ),
    'co-cau-nguon-von': dict(
        td='Finanzierungsstruktur eines Schienenbahnvorhabens',
        mt='Haushalt, ODA, privates Kapital und PPP für eine Metrolinie vergleichen und '
           'kombinieren: wer welches Risiko trägt und was jede Quelle wirklich kostet.',
        ten='Beratung zur Finanzierungsstruktur eines städtischen Schienenbahnvorhabens',
        lede='Jede Finanzierungsquelle bringt eigene Bindungen mit — beim Verfahren, beim '
             'Mittelabfluss, bei der Herkunft der Güter, bei der Frage, wer das Währungsrisiko '
             'trägt. Wählt man die falsche Struktur, geht dem Vorhaben nicht das Geld aus; es '
             'kommt schlicht nicht mehr voran.',
        van_de=[
            'ODA sieht auf dem Zinssatz günstig aus, doch Bedingungen zu Auftragnehmern und '
            'Geräteherkunft treiben die tatsächlichen Kosten.',
            'Das Währungsrisiko eines über zwanzig oder dreißig Jahre laufenden '
            'Fremdwährungsdarlehens ist nicht beziffert.',
            'Die inländischen Eigenmittel stehen nicht rechtzeitig bereit, was den Abfluss des '
            'Darlehens selbst blockiert.',
            'Es ist unklar, welche Teile sich für private Investoren eignen und welche der Staat '
            'behalten muss.',
        ],
        can_cu=[
            ('Luật Đường sắt — Artikel 24',
             'Bei Schienenbahnvorhaben nach dem Investitionsrecht oder dem PPP-Recht garantiert '
             'der Staat die gesamten Kosten für Entschädigung, Unterstützung und Umsiedlung aus '
             'dem Staatshaushalt; diese Arbeit wird als eigenes Vorhaben abgetrennt.'),
            ('Luật Đường sắt — Artikel 23',
             'Ein Teilvorhaben für Entschädigung, Unterstützung und Umsiedlung wird als '
             'eigenständiges Vorhaben geführt und muss die sonst im Baurecht geforderte '
             'eigenständige Betriebsfähigkeit nicht erfüllen.'),
            ('Luật Đường sắt — Artikel 5 Absätze 2 und 4',
             'Weiterleitung von Darlehen und Förderkredite; sowie die Einordnung von '
             'Schieneninfrastrukturbetrieb, Schienenverkehr, Schienenindustrie und Ausbildung von '
             'Eisenbahnpersonal als investitionsbegünstigte Bereiche.'),
        ],
        lam_gi=[
            ('Verfügbare Quellen und ihre Anforderungen auflisten',
             'Je Quelle: Zins, Laufzeit, tilgungsfreie Zeit, Beschaffungsbedingungen, '
             'Abflussverfahren.'),
            ('Auf eine gemeinsame Vergleichsgrundlage bringen',
             'Die tatsächlichen Kapitalkosten nach Beschaffungsbedingungen und Verfahrensaufwand '
             'berechnen — nicht den Nominalzins.'),
            ('Die Risiken zuordnen',
             'Währung, Mittelabfluss, Terminplan des Grunderwerbs — wer trägt was und über welchen '
             'vertraglichen Mechanismus.'),
            ('Eine Struktur mit Rückfalloption vorschlagen',
             'Einschließlich des Auslösers: Verzögert sich Quelle A um mehr als einen bestimmten '
             'Zeitraum, welcher Weg übernimmt dann.'),
        ],
        dau_ra=[
            'Ein Vergleich der Finanzierungsquellen auf einer Grundlage',
            'Eine Risikozuordnung zwischen den Beteiligten',
            'Ein Vorschlag zur Finanzierungsstruktur mit Rückfallszenarien',
        ],
        khi_nao='Bei Erstellung der Unterlagen zur Investitionsleitlinie; wenn erwogen wird, einen '
                'Teil der Linie in eine PPP zu überführen; oder wenn die derzeitige Quelle beim '
                'Mittelabfluss stockt.',
    ),
    'suat-von-dau-tu': dict(
        td='Investitionskennwerte und Umrechnung ausländischer Normen',
        mt='Vergleichsvorhaben auswählen und ausländische Kennwerte nach Artikel 32 auf den '
           'Bewertungsstichtag umrechnen — mit tragfähiger Begründung.',
        ten='Beratung zu Investitionskennwerten und zur Umrechnung ausländischer Normen',
        lede='Vietnams System der Baunormen deckt noch nicht jedes Element einer städtischen '
             'Schienenbahn ab. Das Gesetz erlaubt bereits die Verwendung ausländischer Normen und '
             'Investitionskennwerte. Erlaubt zu sein ist das eine; die eigene Wahl vor der '
             'prüfenden Behörde zu belegen das andere — und genau hier werden Unterlagen am '
             'häufigsten zurückgegeben.',
        van_de=[
            'Für Tunnelvortrieb, Fahrzeuge, Signaltechnik und Zugsicherung gibt es keine '
            'inländischen Normen.',
            'Zahlen werden aus einem ausländischen Vorhaben übernommen, ohne zu begründen, warum '
            'dieses Vorhaben „vergleichbar“ ist.',
            'Die Umrechnung auf den Bewertungsstichtag erfolgt grob, ohne Preissteigerung, '
            'Wechselkurs und Unterschiede der Bauumstände zu trennen.',
            'Bei jeder Anpassung beginnt die Arbeit von vorn, weil die Ausgangsdaten nicht '
            'aufbewahrt wurden.',
        ],
        can_cu=[
            ('Luật Đường sắt — Artikel 32 Absatz 1',
             'Für Positionen, die nicht passen oder im amtlichen System der Normen, Baupreise und '
             'Investitionskennwerte nicht vorkommen, darf ein Schienenbahnvorhaben Systeme '
             'verwenden, die in- oder ausländische Stellen für vergleichbare Positionen oder '
             'vergleichbare Schienenbahnvorhaben veröffentlicht haben, umgerechnet auf den '
             'Bewertungsstichtag.'),
            ('Luật Đường sắt — Artikel 32 Absätze 2 und 5',
             'Ist auch das nicht möglich, dürfen Investitionskennwerte eines vergleichbaren '
             'Vorhabens anderswo auf der Welt herangezogen werden. Kostenpositionen, für die das '
             'vietnamesische Recht noch nichts vorsieht, dürfen einem vergleichbaren '
             'ausländischen Schienenbahnvorhaben folgen.'),
            ('Nghị định 206/2026/NĐ-CP — Artikel 16',
             'Prüfung und Nachprüfung von Kostenberechnungen — worauf die prüfende Stelle sieht.'),
        ],
        lam_gi=[
            ('Feststellen, für welche Positionen inländische Normen fehlen',
             'Die Leistungsgliederung des Vorhabens gegen das geltende Normensystem stellen und '
             'die Lücken auflisten.'),
            ('Vergleichsvorhaben auswählen und die Vergleichbarkeit belegen',
             'Nach Spurweite, Linienart, Anteil unterirdischer und aufgeständerter Abschnitte, '
             'Baugrundverhältnissen und Automatisierungsgrad. Diese Begründung wiegt so schwer wie '
             'die Zahlen selbst.'),
            ('Auf den Bewertungsstichtag umrechnen',
             'In drei Schichten getrennt: Preissteigerung über die Zeit, Preisniveauunterschied '
             'zwischen den beiden Ländern sowie Unterschiede der Bauumstände und der geltenden '
             'Normen.'),
            ('Die Ausgangsdaten aufbewahren',
             'Herausgeber, Veröffentlichungsdatum, verwendeter Wechselkurs, verwendeter Preisindex '
             '— damit die nächste Anpassung nicht bei null beginnt.'),
            ('Den Methodenvermerk schreiben',
             'Ausführlich genug, dass die prüfende Stelle jeden Rechenschritt nachvollziehen kann.'),
        ],
        dau_ra=[
            'Eine Liste der Positionen ohne inländische Norm',
            'Die Auswahlunterlage der Vergleichsvorhaben mit Begründung',
            'Eine dreischichtige Umrechnungstabelle auf den Bewertungsstichtag',
            'Der aufbewahrte Ausgangsdatenbestand für künftige Anpassungen',
        ],
        khi_nao='Bei Erstellung oder Anpassung der Gesamtinvestitionssumme; bei Kostenberechnungen '
                'für Vergabepakete mit Sonderleistungen; oder wenn die prüfende Behörde eine '
                'Begründung Ihrer Einheitspreise verlangt hat.',
    ),
    'kiem-soat-noi-bo': dict(
        td='Interne Kontrolle einer Projektleitung im Schienenbahnbau',
        mt='Ausgaberegeln, Funktionstrennung und Kontrollpunkte zwischen Aufmaß und Zahlung — '
           'entworfen von dem her, was die Schlussabrechnung später verlangen wird.',
        ten='Beratung zur internen Kontrolle der Projektleitung',
        lede='Die meisten Fehler, die bei der Schlussabrechnung auffallen, sind nicht absichtlich '
             'entstanden. Sie sind da, weil über Jahre der Ausführung niemandem die Aufgabe des '
             'Prüfens zugewiesen war. Eine von Anfang an richtig gebaute interne Kontrolle ist weit '
             'billiger, als acht Jahre später die Folgen zu tragen.',
        van_de=[
            'Dieselbe Person bescheinigt Mengen und genehmigt die Zahlung, ohne Kontrolle dazwischen.',
            'Interne Ausgaberegeln bestehen, wurden aber nie gegen das Recht der '
            'Bauinvestitionskosten abgeglichen.',
            'Änderungen werden zuerst mündlich freigegeben und später dokumentiert, sodass bei der '
            'Schlussabrechnung die Grundlage fehlt.',
            'Das Personal wechselt über mehrere Amtszeiten, jede arbeitet anders, ein gemeinsamer '
            'Maßstab fehlt.',
        ],
        can_cu=[
            ('Nghị định 206/2026/NĐ-CP',
             'Steuerung der Bauinvestitionskosten: Zuständigkeit für die Genehmigung von '
             'Kostenberechnungen, Paketkosten und Anpassungen — Grundlage für die Festlegung von '
             'Genehmigungsstufen in den internen Regeln.'),
            ('Nghị định 207/2026/NĐ-CP',
             'Steuerung von Bauqualität und Instandhaltung — Grundlage für die Kontrollpunkte der '
             'Abnahme.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Schlussabrechnung des Investitionskapitals. Zu wissen, was die Schlussabrechnung '
             'verlangen wird, erlaubt es, die Kontrollen von Anfang an passend zu entwerfen.'),
        ],
        lam_gi=[
            ('Den heutigen Ablauf abbilden',
             'Von der Zahlungsanforderung bis zum Abgang aus der Staatskasse: über wen er läuft, '
             'wer was unterschreibt.'),
            ('Die Lücken bestimmen',
             'Wo eine Person zwei Rollen hält; wo niemand abstimmt; wo Unterlagen dem Geld '
             'nachfolgen, statt ihm vorauszugehen.'),
            ('Die Kontrollpunkte neu entwerfen',
             'Bescheinigung und Zahlungsfreigabe trennen; Genehmigungsgrenzen je Stufe festlegen; '
             'die Mindestunterlagen je Ausgabeart bestimmen.'),
            ('Regeln und Formulare entwerfen',
             'Interne Ausgaberegeln, das Kontrollverfahren von der Mengenermittlung bis zur '
             'Zahlung und die dazugehörigen Formulare.'),
            ('Schulen und erproben',
             'An mehreren echten Vorgängen durchspielen, korrigieren, was nicht trägt, und dann '
             'förmlich in Kraft setzen.'),
        ],
        dau_ra=[
            'Heutiger und vorgeschlagener Ablauf, einander gegenübergestellt',
            'Eine Liste der Kontrolllücken mit Risikoeinstufung',
            'Entwurf interner Ausgaberegeln und des Kontrollverfahrens',
            'Ein sofort einsetzbarer Formularsatz',
        ],
        khi_nao='Wenn eine Projektleitung neu eingerichtet wird; wenn eine Linie mit großem '
                'Zahlungsvolumen in die Bauphase eintritt; oder nachdem eine Inspektion oder '
                'Prüfung Feststellungen zur Kontrolle getroffen hat.',
    ),
    'ho-so-quyet-toan': dict(
        td='Abrechnungsunterlagen vom ersten Tag an führen',
        mt='Regeln für Erstellung, Kennzeichnung, Aufbewahrung und Übergabe der '
           'Abrechnungsunterlagen ab dem ersten Vergabepaket.',
        ten='Beratung zur Führung der Abrechnungsunterlagen ab dem ersten Vorhabentag',
        lede='Eine Metrolinie läuft acht bis zwölf Jahre. Das Unternehmen des ersten '
             'Vergabepakets kann liquidiert sein, bevor die Linie den ersten Fahrgast befördert. '
             'Die Ingenieurin, die im zweiten Jahr ein Abnahmeprotokoll unterschrieben hat, kann '
             'im Ruhestand sein. Unterlagen, die nicht im richtigen Moment eingesammelt werden, '
             'lassen sich später nicht einsammeln — nicht weil jemand sie verbirgt, sondern weil '
             'es sie nicht mehr gibt.',
        van_de=[
            'Unterlagen zu unterirdischen und verdeckten Leistungen sind überbaut; anders lassen '
            'sie sich nachträglich nicht belegen.',
            'Frühe Auftragnehmer werden aufgelöst oder wechseln den Inhaber, sodass niemand mehr '
            'Mengen bestätigen kann.',
            'Unterlagen liegen in mehreren Abteilungen ohne gemeinsames Ordnungsmerkmal, und die '
            'Lücken zeigen sich erst beim Entwurf des Schlussabrechnungsberichts.',
            'Bestandspläne und Abnahmeprotokolle stimmen nicht überein, und das fällt viel zu spät '
            'für eine Korrektur auf.',
        ],
        can_cu=[
            ('Nghị định 193/2026/NĐ-CP',
             'Schlussabrechnung des Investitionskapitals — das Verzeichnis der Unterlagen und der '
             'Inhalt des Berichts. Wer das Ziel kennt, kann den Weg entwerfen.'),
            ('Nghị định 207/2026/NĐ-CP',
             'Steuerung von Bauqualität und Instandhaltung — Abnahmeprotokolle und '
             'Fertigstellungsunterlagen.'),
            ('Luật Đường sắt — Artikel 23',
             'Teilvorhaben werden je für sich als eigenständige Vorhaben geführt; die Unterlagen '
             'müssen sich daher ebenfalls teilvorhabenweise abschließen lassen.'),
        ],
        lam_gi=[
            ('Das Zielverzeichnis der Unterlagen aufstellen',
             'Rückwärts von dem her, was der Schlussabrechnungsbericht verlangt: welche Phase '
             'welches Dokument hervorbringen muss.'),
            ('Ein gemeinsames Kennzeichnungssystem festlegen',
             'Ein Ordnungsmerkmal je Teilvorhaben, Vergabepaket und Leistungsposition, damit alle '
             'Abteilungen denselben Namen verwenden.'),
            ('Verbindliche Erfassungspunkte setzen',
             'Gebunden an Abnahme- und Zahlungsmeilensteine, damit Unterlagen dem Geld nie '
             'nachfolgen — besonders bei unterirdischen und verdeckten Leistungen.'),
            ('Aufbewahrung und Sicherung entwerfen',
             'Papier und elektronisch, wo sie liegen, wer sie hält, wo gesichert wird und wie lange.'),
            ('Vierteljährliche Selbstprüfung ansetzen',
             'Jedes Quartal durchsehen, was fehlt, und es einfordern, solange es noch zu bekommen '
             'ist.'),
        ],
        dau_ra=[
            'Ein Verzeichnis der Abrechnungsunterlagen nach Vorhabenphase',
            'Eine gemeinsame Kennzeichnungs- und Benennungsregel',
            'Verfahren für Erfassung, Aufbewahrung, Sicherung und Übergabe',
            'Ein vierteljährliches Selbstprüfungsblatt',
        ],
        khi_nao='Idealerweise vor Abschluss des ersten Vergabepakets. Später ist es weiterhin '
                'machbar, muss dann aber mit einer rückwärtsgerichteten Durchsicht einhergehen, '
                'um bereits Verlorenes zu rekonstruieren.',
    ),
    'tai-co-cau-doanh-nghiep': dict(
        td='Umstrukturierung von Vorhaben- und Betriebsgesellschaft',
        mt='Beratung zur Reorganisation beim Übergang einer Linie vom Bau zum Betrieb: '
           'Vermögensübergabe, Aufbau der Betriebsgesellschaft und Zuschussmechanismus.',
        ten='Beratung zur Umstrukturierung von Vorhabengesellschaft und Betreiber',
        lede='Der Tag, an dem eine Linie den ersten Fahrgast befördert, ist der Tag, an dem eine '
             'Organisation ihr Wesen ändern muss: von einer Stelle, die Investitionen steuert, zu '
             'einer Stelle, die eine Bahn betreibt. Beide brauchen andere Menschen, andere '
             'Verfahren und einen anderen Finanzmechanismus. Erfolgt der Wechsel zu spät, fährt die '
             'Linie, während die Bücher es nicht tun.',
        van_de=[
            'Die durch die Investition entstandenen Vermögenswerte sind vor der Übergabe an den '
            'Betreiber nicht vollständig und richtig erfasst.',
            'Es ist unklar, auf welcher Grundlage der Betreiber die Vermögenswerte erhält und wie '
            'sie zu verbuchen sind.',
            'Der Zuschussmechanismus hat keine feste Formel und wird jedes Jahr neu verhandelt.',
            'Die Projektleitung hat noch Abrechnungsarbeit offen, während ihr Personal bereits in '
            'den Betrieb gewechselt ist.',
        ],
        can_cu=[
            ('Luật Đường sắt — Artikel 5 Absatz 2 Buchstabe c',
             'Der Staat bezuschusst den öffentlichen Personenverkehr auf städtischen Schienenbahnen.'),
            ('Luật Kiểm toán độc lập — Artikel 40 Absatz 2 Buchstabe b',
             'Eine Prüfungsgesellschaft darf Beratungsleistungen zu Management, Umwandlung und '
             'Unternehmensumstrukturierung anmelden und erbringen.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Der Wert der durch die Investition entstandenen Vermögenswerte und ihre Übergabe — '
             'dies muss vor dem Übergang auf die Betriebsgesellschaft abgeschlossen sein.'),
        ],
        lam_gi=[
            ('Vermögen und Verbindlichkeiten vor dem Übergang durchsehen',
             'Ob die Nachweise vollständig sind, wie viel offene Verbindlichkeiten gegenüber '
             'Auftragnehmern bleiben und wer sie weiterträgt.'),
            ('Die Betriebsgesellschaft entwerfen',
             'Aufgaben, Aufbau, Personalstärke und die Abrechnungsarbeit, die bei der '
             'Projektleitung verbleibt.'),
            ('Den Finanzmechanismus des Betriebs aufbauen',
             'Zuschussformel, Anpassungsmechanismus und Kennzahlen zur Beurteilung der '
             'Betriebsleistung.'),
            ('Einen Übergangsfahrplan nach Meilensteinen setzen',
             'Was vor Aufnahme des kommerziellen Betriebs fertig sein muss und was danach folgen '
             'darf.'),
        ],
        dau_ra=[
            'Ein Durchsichtsbericht zu Vermögen und Verbindlichkeiten vor dem Übergang',
            'Ein Aufbauvorschlag für die Betriebsgesellschaft',
            'Ein Vorschlag für Finanzmechanismus und Zuschussformel',
            'Ein Übergangsfahrplan mit Terminen',
        ],
        khi_nao='Zwölf bis achtzehn Monate vor dem geplanten Beginn des kommerziellen Betriebs; '
                'oder wenn die Provinz ihren Betreiber für die städtische Schienenbahn einrichten '
                'oder neu ordnen will.',
    ),
    'thue-du-an': dict(
        td='Steuerberatung für städtische Schienenbahnvorhaben',
        mt='Quellensteuer für ausländische Auftragnehmer, umsatzsteuerliche Behandlung bei '
           'ODA und die Investitionsbegünstigungen des Luật Đường sắt.',
        ten='Steuerberatung für ein städtisches Schienenbahnvorhaben',
        lede='Eine städtische Schienenbahn führt nahezu ihre gesamte Kerntechnik ein: Fahrzeuge, '
             'Signaltechnik, Zugsicherung, dazu die ausländischen Fachleute, die damit kommen. '
             'Jeder solche Vertrag wirft eine Frage zur Quellensteuer für ausländische '
             'Auftragnehmer auf, und Fehler zeigen sich meist erst bei einer Betriebsprüfung — '
             'wenn das Geld längst gezahlt ist.',
        van_de=[
            'Ein Gesamtvertrag über Geräte, Montage, Schulung und Technologietransfer trennt die '
            'Werte der Bestandteile nicht, sodass der falsche Quellensteuersatz angewandt wird.',
            'Es ist nicht geklärt, welche Partei die Quellensteuer trägt, und die Differenz '
            'erscheint bei der Schlussabrechnung.',
            'Die umsatzsteuerliche Behandlung des ODA-finanzierten Teils wird über die Vergabepakete '
            'hinweg uneinheitlich angewandt.',
            'Investitionsbegünstigungen, die das Gesetz dem Schienensektor bereits gewährt, werden '
            'nicht ausgeschöpft.',
        ],
        can_cu=[
            ('Luật Đường sắt — Artikel 5 Absatz 4',
             'Schieneninfrastrukturbetrieb, Schienenverkehr, Schienenindustrie und die Ausbildung '
             'von Eisenbahnpersonal sind investitionsbegünstigte Bereiche.'),
            ('Luật Đường sắt — Artikel 32 Absatz 4',
             'Kosten für Probebetrieb, Schulung und Technologietransfer gehören zur '
             'Gesamtinvestitionssumme — wie sie getrennt werden, wirkt unmittelbar auf die '
             'steuerliche Beurteilung.'),
            ('Luật Kiểm toán độc lập — Artikel 40 Absatz 2 Buchstabe a',
             'Eine Prüfungsgesellschaft darf Beratungsleistungen in Wirtschafts-, Finanz- und '
             'Steuerfragen anmelden und erbringen.'),
        ],
        lam_gi=[
            ('Den Vertrag vor Abschluss durchsehen',
             'Den Wert jedes Bestandteils trennen, seine steuerliche Behandlung bestimmen und '
             'klarstellen, welche Partei die Steuer trägt.'),
            ('Die Quellensteuerlage bestimmen',
             'Nach Tätigkeit: Lieferung von Gütern, Montageleistungen, Schulung, '
             'Technologietransfer.'),
            ('Die umsatzsteuerliche Behandlung je Finanzierungsquelle festlegen',
             'Einheitlich angewandt über alle Vergabepakete des Vorhabens hinweg.'),
            ('Investitionsbegünstigungen durchsehen',
             'Gegen die Voraussetzungen und die zu ihrer Inanspruchnahme nötigen Nachweise.'),
            ('Die Begründungsunterlage vorbereiten',
             'Vorab bereitgelegt für den Fall, dass die Steuerbehörde die Beurteilung überprüft.'),
        ],
        dau_ra=[
            'Eine Durchsicht der Steuerklauseln des Vertrags mit Änderungsvorschlägen',
            'Eine Aufstellung der Quellensteuer je Bestandteil',
            'Einheitliche umsatzsteuerliche Vorgaben für das gesamte Vorhaben',
            'Eine Begründungsunterlage für die Steuerbehörde',
        ],
        khi_nao='Vor Abschluss mit einem ausländischen Auftragnehmer — nur dann lassen sich die '
                'Klauseln noch ändern. Nach der Unterschrift lassen sich lediglich die Folgen '
                'gestalten.',
    ),
    'boi-duong-can-bo': dict(
        td='Schulung für Mitarbeitende der Projektleitung',
        mt='Eine Schulung, aufgebaut aus den eigenen Unterlagen der Stelle: Schlussabrechnung, '
           'Kostenkontrolle, Zahlungsunterlagen und Vorbereitung auf eine Prüfung.',
        ten='Schulung in Finanzwesen, Rechnungslegung und Prüfung für Mitarbeitende der '
            'Projektleitung',
        lede='Die meisten Mitarbeitenden einer Projektleitung kommen aus der Technik. Sie lesen '
             'Pläne besser als Abrechnungsvorschriften. Diese Lücke steckt hinter sehr vielen '
             'Unterlagen, die neu erstellt werden müssen — und sie lässt sich mit der richtigen '
             'Schulung schließen, ohne dass jemand noch einmal studieren muss.',
        van_de=[
            'Zahlungsunterlagen werden wegen fehlender Bestandteile wiederholt zurückgegeben und '
            'kosten beide Seiten Zeit.',
            'Die Mitarbeitenden wissen nicht im Voraus, wonach eine Prüfung fragen wird, und '
            'bereiten sich daher reaktiv vor.',
            'Jede und jeder arbeitet anders, weil der Stelle ein gemeinsamer Maßstab fehlt.',
            'Neue Mitarbeitende haben kein Material zum Lernen und eignen es sich mündlich an.',
        ],
        can_cu=[
            ('Luật Kiểm toán độc lập — Artikel 40 Absatz 2 Buchstabe e',
             'Eine Prüfungsgesellschaft darf Schulungen in Finanzwesen, Rechnungslegung und '
             'Prüfung anmelden und erbringen. Unser Programm bleibt streng in diesen drei '
             'Bereichen.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Schlussabrechnung des Investitionskapitals — der Kern des Programms.'),
            ('Nghị định 206/2026/NĐ-CP', 'Steuerung der Bauinvestitionskosten.'),
        ],
        lam_gi=[
            ('Zuerst den Bedarf erheben',
             'Die tatsächlichen Unterlagen der Stelle ansehen, um zu erkennen, wo es hakt, und '
             'erst dann die Inhalte entwerfen. Wir kommen nicht mit einem fertigen Lehrplan.'),
            ('Nach Zielgruppe entwerfen',
             'Technisches Personal, Rechnungswesen und Leitung brauchen drei verschiedene Niveaus.'),
            ('An echten Unterlagen unterrichten',
             'Mit den anonymisierten Unterlagen des Vorhabens selbst statt mit erfundenen '
             'Beispielen.'),
            ('Übungsaufgaben stellen und bewerten',
             'Die Teilnehmenden sollen es danach können, nicht bloß gehört haben.'),
            ('Das Selbstlernpaket übergeben',
             'Damit auch später hinzukommende Mitarbeitende es nutzen können.'),
        ],
        dau_ra=[
            'Ein Bericht zur Bedarfserhebung',
            'Programm und Unterrichtsmaterial, an die Stelle übergeben',
            'Bewertungsergebnisse je Teilnehmerin und Teilnehmer',
            'Ein Selbstlernpaket für neue Mitarbeitende',
        ],
        khi_nao='Vor der Hochphase der Schlussabrechnung; wenn die Stelle mehrere neue '
                'Mitarbeitende aufnimmt; oder nachdem eine Prüfung oder Inspektion wiederholt '
                'dieselben Feststellungen getroffen hat.',
    ),
}
