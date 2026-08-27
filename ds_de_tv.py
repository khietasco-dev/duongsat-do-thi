# -*- coding: utf-8 -*-
"""Ban TIENG DUC: trang TU VAN (Beratung) va LIEN HE (Kontakt) + CHAN TRANG.

⚠ MUC FAQ "tra loi bang ngon ngu nao" — viet THAN TRONG y nhu ban tieng Nhat:
  ASCO chua co bo cong cu ngon ngu Duc, nen chi hua tra loi CHINH THUC bang
  TIENG VIET hoac TIENG ANH; tieng Duc thi nhan cau hoi.
  Dung nang loi hua len khi chua co nguoi bao dam chat luong.
"""

# =================================================================== TU VAN
TV = dict(
    td='Beratung zu einem städtischen Schienenbahnvorhaben anfragen',
    mt='Schildern Sie, woran Ihr Vorhaben hängt. Wir antworten innerhalb von '
       '24 Arbeitsstunden — drei Arten von Anfragen mit eigener Frist.',
    duong='Beratung',
    h1='Beratung anfragen',
    lede='Schildern Sie, woran das Vorhaben hängt. Wir lesen es, ordnen es ein und antworten '
         'innerhalb von 24 Arbeitsstunden.',
    h_ba='Drei Arten von Anfragen, die wir annehmen',
    ba=[
        ('Kurze Antwort', 'Eine einzelne konkrete Frage',
         'Eine klare Frage zu einer Rechtsgrundlage, einer Verfahrensreihenfolge oder der '
         'Behandlung einer bestimmten Kostenposition. Diese Art ist meist mit der ersten '
         'Antwort erledigt.',
         'Frist: <b>innerhalb von 24 Arbeitsstunden</b> · kostenfrei'),
        ('Unterlagen erforderlich', 'Ein Problem mit mehreren Strängen',
         'Eine Lage, die mehrere Vorschriften oder mehrere Zeitpunkte berührt oder bei der '
         'Vertrag und Abnahmeprotokolle zusammen gelesen werden müssen. Wir geben zunächst eine '
         'vorläufige Antwort und vereinbaren bei Bedarf ein Gespräch.',
         'Frist: <b>2 bis 3 Arbeitstage</b> · eine Vertraulichkeitsvereinbarung kann '
         'erforderlich sein'),
        ('Wird zum Mandat', 'Durchsicht der gesamten Vorhabenakte',
         'Durchsicht der vollständigen Unterlagen vor der Schlussabrechnung oder Rekonstruktion '
         'der Übersicht, welche Vorschriften wann galten, bei einem über viele Jahre laufenden '
         'Vorhaben. Dies hat eigenen Umfang und eigenen Zeitplan.',
         'Frist: <b>nach Vereinbarung</b> · auf Grundlage eines Dienstleistungsvertrags'),
    ],
    h_dv='Neun Leistungen, die wir übernehmen können',
    dv_lede='Über die Beantwortung von Fragen hinaus übernehmen wir neun Arbeitspakete rund um '
            'die finanzielle und steuernde Seite eines städtischen Schienenbahnvorhabens. Jede '
            'Karte erklärt, was wir tun, worauf wir uns stützen und was Sie erhalten.',
    dv_ghi='Alle neun fallen unter Artikel 40 Absatz 2 des Luật Kiểm toán độc lập und müssen vor '
           'Vertragsschluss eine Unabhängigkeitsprüfung durchlaufen — Einzelheiten auf der Seite %s.',
    dv_lk='Leistungen',
    h_mau='Das Formular',
    f_ten='Name', f_cv='Funktion', f_dv='Organisation', f_dt='Telefon', f_em='E-Mail',
    f_db='Ort des Vorhabens', f_gd='In welcher Phase befindet sich das Vorhaben',
    f_nh='Art des Problems',
    f_loai='Art der Anfrage', f_mo='Schildern Sie die Lage',
    f_chon='— Bitte wählen —',
    f_mo_gy='Woran das Vorhaben hängt · was bereits versucht wurde · welche Unterstützung '
            'gebraucht wird · ob eine Frist einzuhalten ist',
    f_gui='Anfrage senden',
    f_bb='Pflichtfeld',
    db=['Hanoi', 'Ho-Chi-Minh-Stadt', 'Anderswo'],
    gd=['Trassenplanung', 'Investitionsleitlinie', 'Vorbereitung, Prüfung und Genehmigung',
        'Grunderwerb', 'Auftragnehmerauswahl', 'Bauausführung', 'Abnahme und Probebetrieb',
        'Übergabe und Aktivierung', 'Schlussabrechnung des Investitionskapitals'],
    nh=['Investitionsverfahren', 'Grunderwerb', 'Vertrag und Zahlung',
        'Abnahme und Bestandsunterlagen', 'Schlussabrechnung des Investitionskapitals',
        'TOD und Flächenverwertung', 'Unterirdischer Raum', 'Schulung und Technologietransfer',
        'Sonstiges'],
    loai=['Eine einzelne konkrete Frage', 'Ein Problem mit mehreren Strängen',
          'Durchsicht der gesamten Vorhabenakte'],
    h_nen='Was in die Schilderung gehört',
    nen=[
        'Wo das Vorhaben liegt — Hanoi und Ho-Chi-Minh-Stadt haben einen eigenen Mechanismus, '
        'andere Orte nicht',
        'Die Finanzierungsquelle: öffentliche Investition, ODA oder PPP',
        'Das Datum des fraglichen Vorgangs — Vorschriften gelten nach dem Zeitpunkt des Ereignisses',
        'Ob zu diesem Punkt bereits eine Entscheidung einer zuständigen Stelle vorliegt',
        'Ob eine Frist einzuhalten ist, etwa ein Abgabetermin für die Nachprüfung',
    ],
    h_bm='Was mit Ihren Angaben geschieht',
    bm='Wir behandeln alles, was Sie uns senden, vertraulich. Wir nennen weder Ihr Vorhaben noch '
       'Ihre Organisation in öffentlichem Material. Wird aus einer Frage eine allgemeine Lehre, '
       'die veröffentlicht zu werden verdient, schreiben wir sie so um, dass sich kein Vorhaben '
       'mehr identifizieren lässt.',
    h_kh='Was wir nicht beantworten können',
    kh='Wir erteilen keine Rechtsberatung — einer Prüfungsgesellschaft ist das Erbringen von '
       'Rechtsdienstleistungen nicht gestattet. Wir bewerten nicht die Arbeit anderer Prüfender '
       'oder Beratender bei einem Vorhaben, das wir nicht untersucht haben. Und wir äußern uns '
       'nicht zu einer Frage, deren Antwort von Unterlagen abhängt, die wir nicht gelesen haben.',
)

# =================================================================== LIEN HE
LH = dict(
    td='ASCO kontaktieren — städtische Schienenbahnvorhaben',
    mt='Drei Wege zu uns: das Beratungsformular, ein Anruf oder ein vereinbartes Gespräch. '
       'Jeder passt zu einer anderen Art von Anliegen.',
    duong='Kontakt',
    h1='Kontakt',
    lede='Drei Wege zu uns, jeder für eine andere Art von Anliegen. Der passende Weg bringt Ihnen '
         'die schnellere Antwort.',
    h_ba='Drei Wege zu uns',
    ba=[
        ('Für die meisten Fälle', 'Das Beratungsformular senden',
         'So erhalten wir genug Zusammenhang, um sachgerecht zu antworten; die Antwort ist daher '
         'meist unmittelbar verwendbar, statt eine Kette von Rückfragen auszulösen.',
         'Antwort: <b>innerhalb von 24 Arbeitsstunden</b>', 'Beratungsformular öffnen →'),
        ('Eilig', 'Rufen Sie uns an',
         'Passend für ein Anliegen mit Frist in den nächsten Tagen oder einen kurzen Punkt, den '
         'Sie vor einer Entscheidung geklärt haben müssen.',
         'Bürozeiten: <b>Montag bis Freitag, 8:00 – 17:30 Uhr</b>', None),
        ('Komplex', 'Ein Gespräch vereinbaren',
         'Hängt ein Vorhaben an mehreren Stellen zugleich, bringt ein Gespräch meist mehr als ein '
         'langer Schriftwechsel. Online oder in Ihren eigenen Räumen.',
         'Dauer: <b>60 bis 90 Minuten</b>', None),
    ],
    dt_ghi='Diese Nummer funktioniert auch über <b>Zalo</b> — schreiben Sie außerhalb der '
           'Bürozeiten, und wir lesen es am nächsten Morgen als Erstes.',
    dl_ghi='Für einen Termin schreiben Sie entweder an <b>Zalo 08 2509 2007</b> oder füllen Sie '
           'das %s aus und wählen als Art der Anfrage <b>„Ein Problem mit mehreren Strängen“</b>.',
    dl_lk='Beratungsformular',
    h_ts='Hauptsitz',
    ts_ten='ASCO Prüfungs- und Bewertungsgesellschaft',
    ts='ASCO-Gebäude, Nr. 2, Gasse 308, Le-Trong-Tan-Straße, Bezirk Phuong Liet, Hanoi<br>'
       'Telefon und Zalo: <b>08 2509 2007</b>',
    h_tt='Online geht ebenso',
    tt='Mit Organisationen außerhalb Hanois führen wir die meisten Gespräche online — das geht '
       'schneller, und niemand muss reisen. Den Zugangslink senden wir, sobald der Termin steht. '
       'Möchten Sie lieber in Ihren eigenen Räumen zusammenkommen, sagen Sie es bei der '
       'Terminvereinbarung, und wir richten es ein.',
    h_chon='Welcher Weg für welches Anliegen',
    chon_cot=('Ihr Anliegen', 'Weg', 'Warum'),
    chon=[
        ('Eine einzelne Frage zu einer Rechtsgrundlage', 'Formular',
         'Eine schriftliche Antwort mit Aktenzeichen, die Sie behalten können'),
        ('Der Abgabetermin der Nachprüfung ist nah und Sie brauchen jetzt eine Antwort', 'Anruf',
         'Kein Warten auf einen Schriftwechsel'),
        ('Das Vorhaben hängt an mehreren Stellen und Sie wissen nicht, wo anfangen', 'Termin',
         'Es braucht den Blick aufs Ganze; Schriftverkehr reicht dafür nicht'),
        ('Sie möchten die gesamte Akte vor der Schlussabrechnung durchgesehen haben',
         'Formular, dritte Option',
         'Das hat eigenen Umfang und muss zuvor vereinbart werden'),
        ('Rückmeldung zum Inhalt dieser Website', 'Formular',
         'Wir berichtigen ihn und halten fest, woher der Hinweis kam'),
    ],
    h_fa='Fragen, die vor der Kontaktaufnahme häufig gestellt werden',
    fa=[
        ('Entstehen Kosten?',
         'Für die Beantwortung eines konkreten Punktes nicht. Das Durchsehen von Unterlagen oder '
         'einer gesamten Vorhabenakte ist Arbeit mit eigenem Umfang und Zeitplan, die wir vor '
         'Beginn miteinander vereinbaren.'),
        ('Ich gehöre keiner Projektleitung an — darf ich trotzdem fragen?',
         'Ja. Diese Website richtet sich an Mitarbeitende von Projektleitungen, Vorhabenträger, '
         'Beratende und Auftragnehmer. Bitte nennen Sie Ihre Rolle im Vorhaben, damit wir aus dem '
         'richtigen Blickwinkel antworten.'),
        ('Mein Vorhaben ist keine städtische Schienenbahn — spielt das eine Rolle?',
         'Vieles auf dieser Website gilt für jedes öffentlich finanzierte Vorhaben, besonders zur '
         'Schlussabrechnung. Nennen Sie die Art des Vorhabens, und wir sagen Ihnen, was sich '
         'übertragen lässt und was nicht.'),
        ('In welcher Sprache antworten Sie?',
         'Die förmliche Antwort erteilen wir auf <b>Vietnamesisch oder Englisch</b>. Anfragen auf '
         'Deutsch nehmen wir entgegen; inhaltlich einstehen können wir jedoch für den '
         'vietnamesischen und den englischen Wortlaut. Hängt die Antwort am Wortlaut einer '
         'Vorschrift, fügen wir den vietnamesischen Originaltext bei, denn nur dieser ist '
         'rechtsverbindlich.'),
    ],
    h_bm='Vertraulichkeit',
    bm='Wir behandeln Ihre Angaben vertraulich und nennen weder Ihr Vorhaben noch Ihre '
       'Organisation in öffentlichem Material. Wird aus einer Frage eine allgemeine Lehre, die '
       'veröffentlicht zu werden verdient, schreiben wir sie so um, dass sich kein Vorhaben mehr '
       'identifizieren lässt.',
)

# =================================================================== CHAN TRANG
CHAN_DE = dict(
    gt='Ein Fachportal zu Investition, Steuerung und Schlussabrechnung städtischer '
       'Schienenbahnvorhaben in Vietnam.',
    c1='Nachschlagen', c2='Kontakt aufnehmen', c3='Bitte beachten',
    m1=[('van-ban', 'Vorschriften suchen'), ('quy-trinh', 'Ablauf des Vorhabens'),
        ('kinh-nghiem', 'Erfahrungen aus der Steuerung')],
    m2=[('vuong-mac', 'Häufige Probleme'), ('tu-van', 'Beratung anfragen'), ('lien-he', 'Kontakt')],
    luu='Die Inhalte dieser Website dienen der Orientierung und ersetzen keine Beratung zu einem '
        'konkreten Vorhaben. Vorschriften ändern sich häufig — bitte stets gegen das Original '
        'prüfen.',
    bq='Urheberrecht der ASCO Prüfungs- und Bewertungsgesellschaft, Vietnam · Zusammengestellt '
       'aus unserem internen Vorschriftenbestand.',
    ngay='Vorschriften aktualisiert bis %s.',
)
