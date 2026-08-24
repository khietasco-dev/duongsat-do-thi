# -*- coding: utf-8 -*-
"""Ban 7 — ba trang ngoai ngu moi: Nhat, Phap, Duc + ghi toan bo site."""
import io, os, sys
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

N = V6.N


def _bang(hang):
    return ''.join('<tr><td><b>%d</b></td><td><b>%s</b></td><td>%s</td></tr>' % (i + 1, a, b)
                   for i, (a, b) in enumerate(hang))


# ================================================================ TIENG NHAT
def trang_ja():
    gd = _bang([
        ("路線計画", "省級計画および都市総合計画への路線の組み込み、線形・駅・車両基地の位置決定、TOD区域の暫定設定。"),
        ("投資方針の決定", "事前実行可能性調査、資金源の審査、権限機関による投資方針の決定。"),
        ("事業の審査・承認", "実行可能性調査と基本設計、または特別メカニズムに基づく全体技術設計、審査、承認。承認された総投資額はその後の決算費用すべての法的上限となる。"),
        ("用地取得と再定住", "土地収用、補償、支援、再定住、区間ごとの用地引渡し。"),
        ("請負者の選定", "入札計画、入札図書、評価、承認、契約締結。"),
        ("施工と原価管理", "詳細設計、積算の作成と承認、施工、段階ごとの出来高検収、支払、変更処理。"),
        ("検査・試運転・システム安全認証", "静的および動的試験、全系統連動試運転、第三者によるシステム安全評価、国家検収、営業許可。"),
        ("引渡しと資産計上", "運営主体への引渡し、公有財産としての所有権確立、資産台帳、減価償却、運賃と補助の方針。"),
        ("竣工決算", "決算報告書の作成、決算報告書の独立監査、審査、承認、債権債務と余剰資材の処理。"),
    ])
    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">ベトナム語版</a> · 日本語</div>
  <h1>ベトナムの都市鉄道事業：法制度と監査</h1>
  <p>ベトナムの地下鉄およびTOD事業に携わる事業管理機関、発注者、コンサルタント、請負者のための参考資料です。</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="nn-bao">
    <b>本ページについて。</b>本サイトの主要部分はベトナム語です。根拠となる法令の正文がベトナム語のみで
    存在するためです。本ページはサイトの内容と、外国企業が見落としやすい点を要約しています。
    <a href="../index.html">ベトナム語版を開く →</a>
  </div>

  <h2 style="margin-bottom:12px">外国企業が見落としやすい三点</h2>
  <div class="luoi g3">
    <div class="the" style="border-top:3px solid var(--do)">
      <h3>失効した法令の引用</h3>
      <p>ベトナムの法令は改正が頻繁です。鉄道法には2017年版と2025年版が併存し、首都法は2026年に
      新法へ置き換えられました。十年に及ぶ事業は二〜三世代の施行細則をまたぎます。</p>
    </div>
    <div class="the" style="border-top:3px solid var(--hoacuc)">
      <h3>特別メカニズムの適用範囲の誤解</h3>
      <p>国会決議は都市鉄道事業について手続の簡素化を認めていますが、<b>ハノイ市とホーチミン市に限られます</b>。
      他の地方には及びません。</p>
    </div>
    <div class="the" style="border-top:3px solid var(--ngoc)">
      <h3>数量内訳のないEPC契約</h3>
      <p>国際的な一括請負契約は数量リスクを請負者に移転しますが、ベトナムの竣工決算は施工数量の
      立証を求めます。契約締結前に価格内訳書を契約附属書として確定してください。</p>
    </div>
  </div>

  <h2 style="margin:30px 0 12px">事業の九段階</h2>
  <div class="bang-boc">
    <table><thead><tr><th style="width:56px">段階</th><th style="width:24%%">名称</th><th>内容</th></tr></thead>
    <tbody>%s</tbody></table>
  </div>

  <h2 style="margin:30px 0 12px">監査は事業と並行して行う</h2>
  <p>地下鉄路線の建設期間は通常八年から十五年に及びます。竣工後に決算報告書の監査を始めると、
  初期の証憑は劣化し、署名者は異動し、下請は解散しており、そして何より<b>地下構造物はもはや
  検査できません</b>。</p>
  <p>そのため大規模事業では、監査を<b>事業の実施と並行して</b>、施工段階または工区ごとに分けて行い、
  最終回で竣工決算報告書監査報告書としてとりまとめます。並行監査は最終報告書に取って代わるものでは
  なく、最終報告書を可能にするものです。</p>

  <h2 style="margin:30px 0 12px">本サイトの内容</h2>
  <div class="luoi g2">
    <div class="the"><h3>法令目録</h3><p>都市鉄道とTODを現に規律する%d件の法令。法律、国会決議、
      政府議定、省令、技術規準、ハノイ市・ホーチミン市人民評議会決議。階層・地域・年・効力状態で
      絞り込めます。</p></div>
    <div class="the"><h3>手続の全体図</h3><p>路線計画から竣工決算までの九段階。各段階の決定機関、
      適用法令、成果物、頻出する問題を示します。</p></div>
    <div class="the"><h3>竣工決算報告書の監査</h3><p>十三の監査区分、二つの必須照合式、
      大規模事業で並行監査を採る理由。</p></div>
    <div class="the"><h3>リスク集</h3><p>監査上の頻出リスクを八分類し、それぞれに兆候と対応手続を
      付しています。一般的な専門経験と公開資料に基づくもので、特定の組織の事例ではありません。</p></div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>連絡先</h3>
    <p style="margin-top:8px">電話・Zalo：<a href="tel:0825092007"><b>+84 82 509 2007</b></a><br>
    ハノイ市フォンリエット坊レチョンタン通り308路地2番地 ASCOビル</p>
    <p class="small" style="margin-top:10px">日本語でのご連絡も承ります。監査報告書、評価証明書などの
    正式成果物はベトナム語で発行し、契約上必要な場合は訳文を添付します。</p>
  </div>

  <p class="small" style="margin-top:22px">本ページは一般的な情報であり、個別事業に関する助言ではなく、
  法的根拠でもありません。ベトナムの法令は頻繁に改正されます。依拠する前に必ず官報の正文をご確認ください。</p>

</div></div>
""" % (gd, N)
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "inLanguage": "ja",
           "name": "ベトナムの都市鉄道事業：法制度と監査",
           "description": "ベトナムの都市鉄道・TOD事業の参考資料。事業の九段階、ハノイ市とホーチミン市の特別メカニズム、竣工決算報告書の監査。"}]
    return than, ld


# ================================================================ TIENG PHAP
def trang_fr():
    gd = _bang([
        ("Planification du tracé", "Inscription de la ligne aux schémas provinciaux et urbains ; tracé, emplacement des stations et du dépôt ; périmètre TOD préliminaire."),
        ("Décision de principe d'investissement", "Étude de préfaisabilité, examen des sources de financement, décision de principe par l'autorité compétente."),
        ("Instruction et approbation du projet", "Étude de faisabilité et avant-projet, ou études d'ingénierie préliminaire dans le cadre du mécanisme spécial ; instruction ; approbation. Le montant total approuvé constitue le plafond juridique de tous les coûts admis ultérieurement au décompte."),
        ("Libération des emprises et relogement", "Récupération foncière, indemnisation, aides, relogement ; remise du terrain par tronçons."),
        ("Sélection des entreprises", "Plan de passation, dossier de consultation, évaluation, approbation, signature du marché."),
        ("Travaux et maîtrise des coûts", "Études d'exécution, devis, travaux, réception échelonnée des quantités, paiements, traitement des avenants."),
        ("Essais, marche à blanc et certification de sécurité", "Essais statiques et dynamiques, marche à blanc du système intégré, évaluation indépendante de la sécurité, réception par l'État, autorisation d'exploitation."),
        ("Remise et comptabilisation des actifs", "Remise à l'exploitant, constitution de la propriété publique, inventaire des actifs, amortissement, politique tarifaire et de subvention."),
        ("Décompte final", "Rapport de décompte, audit indépendant du rapport, instruction, approbation, traitement des créances et des matériels excédentaires."),
    ])
    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Version vietnamienne</a> · Français</div>
  <h1>Projets de métro au Vietnam : cadre juridique et audit</h1>
  <p>Ressource destinée aux unités de gestion de projet, maîtres d'ouvrage, bureaux d'études et
  entreprises intervenant sur les projets de métro et de développement orienté transport au Vietnam.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="nn-bao">
    <b>À propos de cette page.</b> L'essentiel du site est en vietnamien, car il porte sur des textes
    juridiques dont la version officielle n'existe qu'en vietnamien. Cette page résume le contenu du site
    et les points qui surprennent le plus souvent les intervenants étrangers.
    <a href="../index.html">Ouvrir la version vietnamienne →</a>
  </div>

  <h2 style="margin-bottom:12px">Trois erreurs fréquentes chez les intervenants étrangers</h2>
  <div class="luoi g3">
    <div class="the" style="border-top:3px solid var(--do)">
      <h3>Invoquer un texte abrogé</h3>
      <p>Le droit vietnamien évolue rapidement. La loi ferroviaire existe en version 2017 et en version
      2025 ; la loi sur la Capitale a été remplacée en 2026. Un projet de dix ans traverse deux à trois
      générations de décrets d'application.</p>
    </div>
    <div class="the" style="border-top:3px solid var(--hoacuc)">
      <h3>Croire le mécanisme spécial applicable partout</h3>
      <p>Une résolution de l'Assemblée nationale autorise une procédure allégée pour les projets de métro,
      mais <b>uniquement à Hanoï et à Hô Chi Minh-Ville</b>. Elle ne s'étend pas aux autres localités.</p>
    </div>
    <div class="the" style="border-top:3px solid var(--ngoc)">
      <h3>Marché EPC sans détail quantitatif</h3>
      <p>Les marchés internationaux à forfait transfèrent le risque de quantités à l'entreprise ;
      le décompte vietnamien exige pourtant la preuve des quantités exécutées. Faites annexer au marché
      la décomposition du prix avant signature.</p>
    </div>
  </div>

  <h2 style="margin:30px 0 12px">Les neuf phases du projet</h2>
  <div class="bang-boc">
    <table><thead><tr><th style="width:56px">Phase</th><th style="width:26%%">Intitulé</th><th>Contenu</th></tr></thead>
    <tbody>%s</tbody></table>
  </div>

  <h2 style="margin:30px 0 12px">L'audit se déroule en parallèle, pas seulement à la fin</h2>
  <p>La construction d'une ligne de métro s'étend habituellement sur huit à quinze ans. Attendre
  l'achèvement pour engager l'audit du rapport de décompte, c'est trouver des pièces dégradées,
  des signataires mutés, des sous-traitants dissous et — surtout — <b>des ouvrages souterrains
  devenus inspectables</b>.</p>
  <p>Pour les grands projets, l'audit est donc conduit <b>en parallèle de l'exécution</b>, par phases
  calées sur les étapes de travaux ou sur les lots, la dernière consolidant l'ensemble dans le rapport
  d'audit du décompte final. L'audit parallèle ne remplace pas le rapport final : il le rend possible.</p>

  <h2 style="margin:30px 0 12px">Contenu du site</h2>
  <div class="luoi g2">
    <div class="the"><h3>Répertoire des textes</h3><p>%d textes régissant actuellement le métro et le TOD :
      lois, résolutions de l'Assemblée nationale, décrets, circulaires ministérielles, règlements techniques
      et résolutions des Conseils populaires de Hanoï et de Hô Chi Minh-Ville. Filtrables par niveau,
      localité, année et validité.</p></div>
    <div class="the"><h3>Carte des procédures</h3><p>Neuf phases, de la planification du tracé au décompte
      final, avec pour chacune l'autorité décisionnaire, les textes applicables, le livrable et les
      difficultés les plus fréquentes.</p></div>
    <div class="the"><h3>Audit du rapport de décompte</h3><p>Treize sections d'audit, deux équations de
      contrôle obligatoires, et la logique de l'audit parallèle pour les grands projets.</p></div>
    <div class="the"><h3>Bibliothèque de risques</h3><p>Risques d'audit courants classés en huit familles,
      chacun avec ses indices et la procédure d'audit correspondante. Compilée à partir de l'expérience
      professionnelle générale et de sources publiques, et non de cas propres à un organisme.</p></div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>Contact</h3>
    <p style="margin-top:8px">Téléphone et Zalo : <a href="tel:0825092007"><b>+84 82 509 2007</b></a><br>
    Immeuble ASCO, n° 2, ruelle 308, rue Le Trong Tan, quartier Phuong Liet, Hanoï</p>
    <p class="small" style="margin-top:10px">La correspondance en français est possible. Les livrables
    officiels — rapports d'audit, certificats d'évaluation — sont émis en vietnamien, avec traduction
    lorsque la mission l'exige.</p>
  </div>

  <p class="small" style="margin-top:22px">Cette page fournit une information générale ; elle ne constitue
  ni un conseil sur un projet déterminé ni une source de droit. La législation vietnamienne change
  fréquemment : vérifiez toujours le texte au journal officiel avant de vous en prévaloir.</p>

</div></div>
""" % (gd, N)
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "inLanguage": "fr",
           "name": "Projets de métro au Vietnam : cadre juridique et audit",
           "description": "Ressource sur les projets de métro et de TOD au Vietnam : les neuf phases, le mécanisme spécial de Hanoï et Hô Chi Minh-Ville, et l'audit du décompte final."}]
    return than, ld


# ================================================================ TIENG DUC
def trang_de():
    gd = _bang([
        ("Trassenplanung", "Aufnahme der Linie in Provinz- und Stadtentwicklungspläne; Linienführung, Lage der Stationen und des Betriebshofs; vorläufiges TOD-Gebiet."),
        ("Investitionsgrundsatzentscheidung", "Vorstudie, Prüfung der Finanzierungsquellen, Grundsatzentscheidung durch die zuständige Stelle."),
        ("Prüfung und Genehmigung des Vorhabens", "Machbarkeitsstudie und Vorentwurf oder Basic Engineering nach dem Sondermechanismus; Prüfung; Genehmigung. Die genehmigte Gesamtinvestition bildet die rechtliche Obergrenze aller später abrechenbaren Kosten."),
        ("Grunderwerb und Umsiedlung", "Landrücknahme, Entschädigung, Beihilfen, Umsiedlung; abschnittsweise Übergabe der Baufelder."),
        ("Auftragnehmerauswahl", "Vergabeplan, Vergabeunterlagen, Wertung, Genehmigung, Vertragsabschluss."),
        ("Bauausführung und Kostensteuerung", "Ausführungsplanung, Kostenanschläge, Bauausführung, abschnittsweise Abnahme der Mengen, Zahlungen, Behandlung von Nachträgen."),
        ("Prüfung, Probebetrieb und Systemsicherheitsnachweis", "Statische und dynamische Prüfungen, integrierter Probebetrieb, unabhängige Systemsicherheitsbewertung, staatliche Abnahme, Betriebsgenehmigung."),
        ("Übergabe und Aktivierung", "Übergabe an den Betreiber, Begründung des öffentlichen Eigentums, Anlagenverzeichnis, Abschreibung, Tarif- und Zuschusskonzept."),
        ("Schlussabrechnung", "Abrechnungsbericht, unabhängige Prüfung des Abrechnungsberichts, Prüfung, Genehmigung, Behandlung von Forderungen und Restmaterial."),
    ])
    than = """
<div class="banner"><div class="wrap">
  <div class="duong"><a href="../index.html">Vietnamesische Fassung</a> · Deutsch</div>
  <h1>U-Bahn-Projekte in Vietnam: Rechtsrahmen und Prüfung</h1>
  <p>Nachschlagewerk für Projektträger, Bauherren, Planungsbüros und Auftragnehmer bei U-Bahn- und
  TOD-Vorhaben in Vietnam.</p>
</div></div>

<div class="than"><div class="wrap">

  <div class="nn-bao">
    <b>Zu dieser Seite.</b> Der Hauptteil der Website ist auf Vietnamesisch, weil er auf Rechtstexte
    gestützt ist, die amtlich nur auf Vietnamesisch vorliegen. Diese Seite fasst den Inhalt zusammen
    und nennt die Punkte, die ausländische Beteiligte am häufigsten übersehen.
    <a href="../index.html">Vietnamesische Fassung öffnen →</a>
  </div>

  <h2 style="margin-bottom:12px">Drei häufige Fehler ausländischer Beteiligter</h2>
  <div class="luoi g3">
    <div class="the" style="border-top:3px solid var(--do)">
      <h3>Berufung auf aufgehobene Vorschriften</h3>
      <p>Das vietnamesische Recht ändert sich häufig. Das Eisenbahngesetz besteht in einer Fassung von
      2017 und einer von 2025; das Hauptstadtgesetz wurde 2026 ersetzt. Ein zehnjähriges Vorhaben
      durchläuft zwei bis drei Generationen von Durchführungsverordnungen.</p>
    </div>
    <div class="the" style="border-top:3px solid var(--hoacuc)">
      <h3>Annahme, der Sondermechanismus gelte überall</h3>
      <p>Ein Beschluss der Nationalversammlung erlaubt ein verkürztes Verfahren für U-Bahn-Vorhaben,
      jedoch <b>nur in Hanoi und Ho-Chi-Minh-Stadt</b>. Auf andere Gebietskörperschaften erstreckt er
      sich nicht.</p>
    </div>
    <div class="the" style="border-top:3px solid var(--ngoc)">
      <h3>EPC-Vertrag ohne Mengengerüst</h3>
      <p>Internationale Pauschalverträge verlagern das Mengenrisiko auf den Auftragnehmer; die
      vietnamesische Schlussabrechnung verlangt jedoch den Nachweis der ausgeführten Mengen.
      Vereinbaren Sie die Preisaufgliederung vor Vertragsschluss als Anlage.</p>
    </div>
  </div>

  <h2 style="margin:30px 0 12px">Die neun Projektphasen</h2>
  <div class="bang-boc">
    <table><thead><tr><th style="width:56px">Phase</th><th style="width:26%%">Bezeichnung</th><th>Inhalt</th></tr></thead>
    <tbody>%s</tbody></table>
  </div>

  <h2 style="margin:30px 0 12px">Die Prüfung läuft parallel, nicht erst am Ende</h2>
  <p>Der Bau einer U-Bahn-Linie dauert in der Regel acht bis fünfzehn Jahre. Wer mit der Prüfung des
  Abrechnungsberichts bis zur Fertigstellung wartet, findet beschädigte Belege vor, versetzte
  Unterzeichner, aufgelöste Nachunternehmer und — vor allem — <b>unterirdische Bauwerke, die sich
  nicht mehr prüfen lassen</b>.</p>
  <p>Bei Großvorhaben wird die Prüfung deshalb <b>parallel zur Projektdurchführung</b> vorgenommen,
  in Abschnitten nach Bauphasen oder Losen; der letzte Abschnitt fasst alles im Prüfungsbericht zur
  Schlussabrechnung zusammen. Die parallele Prüfung ersetzt den Schlussbericht nicht — sie macht ihn
  erst möglich.</p>

  <h2 style="margin:30px 0 12px">Inhalt der Website</h2>
  <div class="luoi g2">
    <div class="the"><h3>Verzeichnis der Rechtstexte</h3><p>%d derzeit geltende Rechtstexte zu U-Bahn und
      TOD: Gesetze, Beschlüsse der Nationalversammlung, Regierungsverordnungen, Ministerialrundschreiben,
      technische Regelwerke sowie Beschlüsse der Volksräte von Hanoi und Ho-Chi-Minh-Stadt. Filterbar nach
      Ebene, Gebiet, Jahr und Gültigkeit.</p></div>
    <div class="the"><h3>Verfahrensübersicht</h3><p>Neun Phasen von der Trassenplanung bis zur
      Schlussabrechnung, jeweils mit entscheidender Stelle, anwendbaren Vorschriften, Ergebnis und den
      häufigsten Schwierigkeiten.</p></div>
    <div class="the"><h3>Prüfung des Abrechnungsberichts</h3><p>Dreizehn Prüfungsabschnitte, zwei
      verbindliche Abstimmungsgleichungen und die Begründung der parallelen Prüfung bei Großvorhaben.</p></div>
    <div class="the"><h3>Risikobibliothek</h3><p>Häufige Prüfungsrisiken in acht Gruppen, jeweils mit
      Anzeichen und zugehöriger Prüfungshandlung. Zusammengestellt aus allgemeiner Berufserfahrung und
      öffentlichen Quellen, nicht aus Fällen einer bestimmten Organisation.</p></div>
  </div>

  <div class="the" style="border-left:3px solid var(--muc3);margin-top:24px">
    <h3>Kontakt</h3>
    <p style="margin-top:8px">Telefon und Zalo: <a href="tel:0825092007"><b>+84 82 509 2007</b></a><br>
    ASCO-Gebäude, Nr. 2, Gasse 308, Le-Trong-Tan-Straße, Bezirk Phuong Liet, Hanoi</p>
    <p class="small" style="margin-top:10px">Korrespondenz auf Deutsch ist möglich. Förmliche Ergebnisse —
    Prüfungsberichte, Wertgutachten — werden auf Vietnamesisch erstellt, bei Bedarf mit Übersetzung.</p>
  </div>

  <p class="small" style="margin-top:22px">Diese Seite enthält allgemeine Informationen; sie ist weder
  Beratung zu einem bestimmten Vorhaben noch eine Rechtsquelle. Das vietnamesische Recht ändert sich
  häufig — prüfen Sie vor jeder Berufung den amtlichen Text im Gesetzblatt.</p>

</div></div>
""" % (gd, N)
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "inLanguage": "de",
           "name": "U-Bahn-Projekte in Vietnam: Rechtsrahmen und Prüfung",
           "description": "Nachschlagewerk zu U-Bahn- und TOD-Vorhaben in Vietnam: die neun Projektphasen, der Sondermechanismus für Hanoi und Ho-Chi-Minh-Stadt und die Prüfung der Schlussabrechnung."}]
    return than, ld


# ================================================================ GHI TOAN BO
TRANG = list(V5.TRANG)
# thay trang van ban bang ban co cot So hieu
TRANG = [(s, l, td, mt, (V6.trang_van_ban if s == 'van-ban' else fn), tang)
         for s, l, td, mt, fn, tang in TRANG]
TRANG += [
    ('ja', 'ja', 'ベトナムの都市鉄道事業：法制度と監査',
     'ベトナムの都市鉄道・TOD事業の参考資料。事業の九段階、ハノイ市とホーチミン市の特別メカニズム、竣工決算報告書の監査。',
     trang_ja, 'trong'),
    ('fr', 'fr', 'Métro au Vietnam : cadre juridique et audit',
     'Projets de métro et de TOD au Vietnam : les neuf phases, le mécanisme spécial de Hanoï et Hô Chi Minh-Ville, et l\'audit du décompte final.',
     trang_fr, 'trong'),
    ('de', 'de', 'U-Bahn in Vietnam: Rechtsrahmen und Prüfung',
     'U-Bahn- und TOD-Vorhaben in Vietnam: die neun Projektphasen, der Sondermechanismus für Hanoi und Ho-Chi-Minh-Stadt und die Prüfung der Schlussabrechnung.',
     trang_de, 'trong'),
]


def ghi():
    os.makedirs(B.KHO, exist_ok=True)
    qua = []
    for slug, lang, td, mt, fn, tang in TRANG:
        than, ld = fn()
        h = B.khung(slug, td, mt, than, ld, tang, lang)
        d = os.path.join(B.KHO, slug) if slug else B.KHO
        os.makedirs(d, exist_ok=True)
        io.open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h)
        print('  %-18s %-3s %7d byte   title %2d   desc %3d' % (slug or '.', lang, len(h), len(td), len(mt)))
        if len(td) > 60 or len(mt) > 160:
            qua.append((slug or '.', len(td), len(mt)))

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for slug, lang, td, mt, fn, tang in TRANG:
        u = B.GOC + '/' + (slug + '/' if slug else '')
        sm.append('  <url><loc>%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>'
                  % (u, 'weekly' if slug == 'van-ban' else 'monthly', '1.0' if not slug else '0.8'))
    sm.append('</urlset>')
    io.open(os.path.join(B.KHO, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
    io.open(os.path.join(B.KHO, 'robots.txt'), 'w', encoding='utf-8').write(
        'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % B.GOC)
    print('\nDa ghi %d trang + sitemap.xml + robots.txt' % len(TRANG))
    print('Vuot nguong SEO:', qua if qua else 'khong co')


if __name__ == '__main__':
    ghi()
