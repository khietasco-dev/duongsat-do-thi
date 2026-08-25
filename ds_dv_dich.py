# -*- coding: utf-8 -*-
"""Ban dich trang TONG DICH VU sang 5 thu tieng.

Chi dich VAN CUA CHINH MINH — khong dich ten van ban phap luat, khong dich
trich dan dieu khoan. Ten dieu luat giu nguyen so hieu tieng Viet kem chu giai.
"""

# tieu de + doan mo
TRANG = {
    'en': dict(
        td='Advisory services for urban railway projects',
        mt='Nine advisory services for metro projects in Vietnam: TOD capital recovery, '
           'financial planning, investment norms, internal control, tax and training.',
        duong='Home', ten='Services',
        h1='Nine advisory services for urban railway projects',
        lede='Beyond auditing the final settlement report of a completed project, we take on nine '
             'more pieces of work around the financial and governance side of a metro line. All of '
             'them sit inside what Vietnamese law allows an audit firm to do — and we set out that '
             'boundary right here.',
        vs_h='Why an audit firm does this work',
        vs_1='Because all nine are <b>financial problems</b>, not civil engineering problems. '
             'Recovering capital from TOD land is a cash-flow model. Converting foreign investment '
             'norms is a price-level conversion. Internal control is designing checkpoints in the '
             'flow of money. This is our trade.',
        vs_2='Conversely, we <b>do not take on</b> project management consultancy, construction '
             'supervision, design or design appraisal. Not because of any licence problem — but '
             'because we have no team of civil engineers, and because if we did that work we would '
             'later be auditing ourselves.',
        rg_h='The legal boundary, stated up front',
        duoc_h='What we are allowed to do',
        duoc_1='Article 40 of the Law on Independent Audit lists the services an audit firm may '
               'provide. <b>Clause 1</b> covers audit, review and other assurance services — '
               'available immediately. <b>Clause 2</b> covers economic, financial and tax advisory; '
               'advisory on management, conversion and corporate restructuring; IT advisory; '
               'accounting services; valuation; and training in finance, accounting and auditing — '
               'these <b>require registration with the Ministry of Finance</b>.',
        duoc_2='All nine services on this page fall under Clause 2.',
        khong_h='What we are not allowed to do',
        khong_1='The list in Article 40 is a <b>closed list</b>. Anything not named in it, an audit '
                'firm may not sell — <b>including legal services</b>. When you need a genuine legal '
                'opinion, we say so plainly and refer you to a licensed law practice rather than '
                'taking the work and improvising.',
        khong_2='And under Article 30, we may not provide services that impair our independence '
                'towards an entity we audit. The independence check always runs before any '
                'discussion of price.',
        bd_h='Where to start',
        bd_1='If you are not sure which service your problem belongs to, just describe the situation '
             'on the %s page. We will classify it for you — and if it falls outside what we are '
             'permitted to do, we will say so immediately.',
        bd_lk='Request advice',
        bd_2='Contact: <b>0825092007</b> (Zalo available) · ASCO Building, No. 2, Lane 308, '
             'Le Trong Tan Street, Phuong Liet Ward, Hanoi.',
        xem='View details →',
    ),
    'zh': dict(
        td='越南城市轨道交通项目咨询服务',
        mt='面向越南地铁项目的九项咨询服务：TOD 土地资金回收、财务方案、投资定额换算、内部控制、税务与培训。',
        duong='首页', ten='服务项目',
        h1='城市轨道交通项目的九项咨询服务',
        lede='除竣工决算报告审计外，我们还承接地铁线路在财务与治理方面的九项工作。'
             '这些工作都在越南法律允许审计企业从事的范围之内——我们在此把界限说清楚。',
        vs_h='审计企业为何做这些工作',
        vs_1='因为这九项都是<b>财务问题</b>，不是土木工程问题。TOD 土地资金回收是一个现金流模型；'
             '境外投资定额换算是价格水平的换算；内部控制是在资金流程中设置卡口。这正是我们的本行。',
        vs_2='反过来，我们<b>不承接</b>项目管理咨询、施工监理、设计和设计审查。'
             '不是因为资质问题，而是因为我们没有土木工程师团队；而且做了这些工作，'
             '日后就等于审计自己。',
        rg_h='法律界限，先说清楚',
        duoc_h='我们可以做什么',
        duoc_1='《独立审计法》第 40 条列举了审计企业可以提供的服务。<b>第 1 款</b>为审计、审阅'
               '及其他鉴证服务，可直接开展。<b>第 2 款</b>为经济、财务、税务咨询；管理、转制'
               '与企业重组咨询；信息技术咨询；会计服务；资产评估；财务、会计、审计知识培训——'
               '这些<b>须向财政部登记</b>后方可开展。',
        duoc_2='本页九项服务均属第 2 款。',
        khong_h='我们不能做什么',
        khong_1='第 40 条的清单是<b>封闭清单</b>。清单之外的业务，审计企业不得提供——'
                '<b>包括法律服务</b>。当贵方需要真正的法律意见时，我们会直言相告并推荐持牌律师'
                '事务所，而不是接下来自行摸索。',
        khong_2='并且根据第 30 条，我们不得向自己审计的单位提供影响独立性的服务。'
                '独立性核查始终先于价格洽谈。',
        bd_h='从哪里开始',
        bd_1='若不确定所遇问题属于哪一项服务，请直接在%s页面描述情况。'
             '我们会替贵方分类；若超出我们获准从事的范围，会立即说明。',
        bd_lk='咨询申请',
        bd_2='联系方式：<b>0825092007</b>（可加 Zalo）· 河内市芳列坊黎仲晋街 308 巷 2 号 ASCO 大楼。',
        xem='查看详情 →',
    ),
    'ja': dict(
        td='ベトナム都市鉄道事業の コンサルティング',
        mt='ベトナムの地下鉄事業向け九つのコンサルティング：TOD用地からの資金回収、財務計画、'
           '投資原単位換算、内部統制、税務、研修。',
        duong='ホーム', ten='サービス',
        h1='都市鉄道事業のための九つのコンサルティング',
        lede='完成事業の決算報告書監査に加えて、地下鉄路線の財務・統治の面で九つの業務をお引き受け'
              'します。いずれもベトナム法が監査法人に認めた範囲の内にあります。その境界を、'
             'ここではっきり示します。',
        vs_h='なぜ監査法人がこの業務を行うのか',
        vs_1='九つとも<b>財務の問題</b>であって、土木工学の問題ではないからです。TOD用地からの'
             '資金回収はキャッシュフロー・モデル、海外の投資原単位の換算は価格水準の換算、'
             '内部統制は資金の流れに関所を設ける設計です。これが私たちの本業です。',
        vs_2='逆に、事業管理コンサルティング、施工監理、設計、設計審査は<b>お引き受けしません</b>。'
             '資格の問題ではなく、土木技術者の陣容を持たないため、そして引き受ければ後日'
             '自分の仕事を自分で監査することになるためです。',
        rg_h='法的な境界を先に申し上げます',
        duoc_h='行えること',
        duoc_1='独立監査法第40条は、監査法人が提供できる業務を列挙しています。<b>第1項</b>は'
               '監査・レビュー・その他の保証業務で、直ちに実施できます。<b>第2項</b>は'
               '経済・財務・税務の助言、経営・転換・企業再編の助言、情報技術の助言、会計業務、'
               '資産評価、財務会計監査の知識研修で、<b>財政省への登録</b>が必要です。',
        duoc_2='本ページの九業務はすべて第2項に属します。',
        khong_h='行えないこと',
        khong_1='第40条の一覧は<b>限定列挙</b>です。そこに名のない業務は監査法人が販売できません'
                '——<b>法務サービスを含みます</b>。真に法的な意見が必要な場合は率直に申し上げ、'
                '弁護士事務所をご紹介します。引き受けて我流で処理することはしません。',
        khong_2='また第30条により、監査対象の独立性を損なう業務は提供できません。'
                '独立性の確認は、価格の話より必ず先に行います。',
        bd_h='はじめに',
        bd_1='どの業務に当たるか判然としない場合は、%sのページで状況をご記入ください。'
             '当方で分類いたします。認められた範囲を超える場合は、その場で申し上げます。',
        bd_lk='相談の依頼',
        bd_2='窓口：<b>0825092007</b>（Zalo可）· ハノイ市フオンリエット坊レチョンタン通り308番地'
             '2号 ASCOビル。',
        xem='詳細を見る →',
    ),
    'fr': dict(
        td='Conseil pour les projets de métro au Vietnam',
        mt='Neuf services de conseil pour les projets de métro : foncier TOD, plan financier, '
           'normes de coût, contrôle interne, fiscalité et formation.',
        duong='Accueil', ten='Services',
        h1='Neuf services de conseil pour les projets de métro',
        lede='Au-delà de l’audit du décompte final d’un projet achevé, nous prenons en charge neuf '
             'autres missions touchant au volet financier et à la gouvernance d’une ligne de métro. '
             'Toutes se situent dans le périmètre que la loi vietnamienne reconnaît à une société '
             'd’audit — et nous posons cette limite dès maintenant.',
        vs_h='Pourquoi une société d’audit fait ce travail',
        vs_1='Parce que les neuf missions sont des <b>problèmes financiers</b>, et non des problèmes '
             'de génie civil. Récupérer le capital par le foncier TOD est un modèle de flux de '
             'trésorerie. Convertir des ratios de coût étrangers est une conversion de niveau de '
             'prix. Le contrôle interne consiste à placer des verrous dans le circuit de l’argent. '
             'C’est notre métier.',
        vs_2='À l’inverse, nous <b>n’acceptons pas</b> le conseil en gestion de projet, la '
             'supervision de chantier, la conception ni la vérification de la conception. Non par '
             'défaut d’agrément, mais parce que nous n’avons pas d’équipe d’ingénieurs, et parce '
             'qu’en le faisant nous auditerions ensuite notre propre travail.',
        rg_h='La limite juridique, énoncée d’emblée',
        duoc_h='Ce que nous pouvons faire',
        duoc_1='L’article 40 de la loi sur l’audit indépendant énumère les services qu’une société '
               'd’audit peut fournir. Le <b>paragraphe 1</b> couvre l’audit, l’examen limité et les '
               'autres missions d’assurance — disponibles immédiatement. Le <b>paragraphe 2</b> '
               'couvre le conseil économique, financier et fiscal ; le conseil en gestion, '
               'transformation et restructuration ; le conseil informatique ; les services '
               'comptables ; l’évaluation ; et la formation en finance, comptabilité et audit — '
               'ceux-ci <b>exigent un enregistrement auprès du ministère des Finances</b>.',
        duoc_2='Les neuf services de cette page relèvent du paragraphe 2.',
        khong_h='Ce que nous ne pouvons pas faire',
        khong_1='La liste de l’article 40 est une <b>liste fermée</b>. Ce qui n’y figure pas, une '
                'société d’audit ne peut le vendre — <b>y compris les services juridiques</b>. '
                'Lorsqu’un avis juridique véritable est nécessaire, nous le disons franchement et '
                'orientons vers un cabinet d’avocats, plutôt que d’accepter la mission et '
                'd’improviser.',
        khong_2='Et selon l’article 30, nous ne pouvons fournir de services portant atteinte à notre '
                'indépendance envers une entité que nous auditons. La vérification de '
                'l’indépendance précède toujours la discussion du prix.',
        bd_h='Par où commencer',
        bd_1='Si vous ne savez pas de quel service relève votre difficulté, décrivez simplement la '
             'situation sur la page %s. Nous la classons pour vous — et si elle sort de ce que nous '
             'sommes autorisés à faire, nous le disons aussitôt.',
        bd_lk='Demande de conseil',
        bd_2='Contact : <b>0825092007</b> (Zalo) · Immeuble ASCO, n° 2, ruelle 308, rue Le Trong Tan, '
             'quartier Phuong Liet, Hanoï.',
        xem='Voir le détail →',
    ),
    'de': dict(
        td='Beratung für U-Bahn-Vorhaben in Vietnam',
        mt='Neun Beratungsleistungen für U-Bahn-Vorhaben: TOD-Flächen, Finanzierungsplan, '
           'Investitionskennwerte, interne Kontrolle, Steuern und Schulung.',
        duong='Startseite', ten='Leistungen',
        h1='Neun Beratungsleistungen für U-Bahn-Vorhaben',
        lede='Über die Prüfung der Schlussabrechnung eines fertiggestellten Vorhabens hinaus '
             'übernehmen wir neun weitere Aufgaben rund um Finanzen und Steuerung einer U-Bahn-Linie. '
             'Alle liegen innerhalb dessen, was das vietnamesische Recht einer Prüfungsgesellschaft '
             'erlaubt — und diese Grenze benennen wir hier.',
        vs_h='Warum eine Prüfungsgesellschaft das übernimmt',
        vs_1='Weil alle neun <b>finanzielle Fragen</b> sind und keine bautechnischen. Der Rückfluss '
             'über TOD-Flächen ist ein Zahlungsstrommodell. Die Umrechnung ausländischer '
             'Kostenkennwerte ist eine Umrechnung des Preisniveaus. Interne Kontrolle heißt, im '
             'Geldfluss Kontrollpunkte zu setzen. Das ist unser Handwerk.',
        vs_2='Umgekehrt übernehmen wir <b>keine</b> Projektsteuerung, keine Bauüberwachung, keine '
             'Planung und keine Planprüfung. Nicht wegen fehlender Zulassung, sondern weil uns ein '
             'Team von Bauingenieuren fehlt — und weil wir sonst später unsere eigene Arbeit prüfen '
             'würden.',
        rg_h='Die rechtliche Grenze, vorab benannt',
        duoc_h='Was wir tun dürfen',
        duoc_1='Artikel 40 des Gesetzes über die unabhängige Abschlussprüfung zählt auf, welche '
               'Leistungen eine Prüfungsgesellschaft erbringen darf. <b>Absatz 1</b> umfasst '
               'Prüfung, prüferische Durchsicht und sonstige betriebswirtschaftliche Prüfungen — '
               'sofort möglich. <b>Absatz 2</b> umfasst Wirtschafts-, Finanz- und Steuerberatung, '
               'Beratung zu Führung, Umwandlung und Restrukturierung, IT-Beratung, '
               'Buchführungsleistungen, Bewertung sowie Schulungen in Finanzen, Rechnungswesen und '
               'Prüfung — diese <b>erfordern eine Registrierung beim Finanzministerium</b>.',
        duoc_2='Alle neun Leistungen dieser Seite fallen unter Absatz 2.',
        khong_h='Was wir nicht tun dürfen',
        khong_1='Die Liste in Artikel 40 ist eine <b>abschließende Liste</b>. Was dort nicht steht, '
                'darf eine Prüfungsgesellschaft nicht anbieten — <b>auch keine Rechtsdienstleistungen'
                '</b>. Wenn eine echte rechtliche Einschätzung nötig ist, sagen wir das offen und '
                'verweisen an eine Anwaltskanzlei, statt den Auftrag anzunehmen und zu '
                'improvisieren.',
        khong_2='Und nach Artikel 30 dürfen wir keine Leistungen erbringen, die unsere Unabhängigkeit '
                'gegenüber einem geprüften Unternehmen beeinträchtigen. Die Prüfung der '
                'Unabhängigkeit läuft stets vor jedem Preisgespräch.',
        bd_h='Wo anfangen',
        bd_1='Wenn unklar ist, zu welcher Leistung Ihr Anliegen gehört, schildern Sie die Lage '
             'einfach auf der Seite %s. Wir ordnen sie ein — und falls sie außerhalb des uns '
             'Erlaubten liegt, sagen wir es sofort.',
        bd_lk='Beratung anfragen',
        bd_2='Kontakt: <b>0825092007</b> (Zalo) · ASCO-Gebäude, Nr. 2, Gasse 308, Le-Trong-Tan-Straße, '
             'Bezirk Phuong Liet, Hanoi.',
        xem='Details ansehen →',
    ),
}

# mo ta ngan cua tung dich vu, hien tren the
MO_TA = {
    'thu-hoi-von-tod': dict(
        en='A cash-flow model for TOD land under Article 25 of the Law on Railways: collection '
           'schedule, the share the province keeps, and sensitivity to land prices and timing.',
        zh='依据《铁路法》第 25 条建立 TOD 土地现金流模型：收入时序、地方留成比例，'
           '以及地价与进度变动的敏感性分析。',
        ja='鉄道法第25条に基づくTOD用地のキャッシュフロー・モデル。収入時期、地方の留保割合、'
           '地価と進度の変動に対する感応度。',
        fr='Un modèle de flux de trésorerie du foncier TOD selon l’article 25 de la loi ferroviaire : '
           'calendrier des recettes, part conservée par la province, sensibilité aux prix et délais.',
        de='Ein Zahlungsstrommodell für TOD-Flächen nach Artikel 25 des Eisenbahngesetzes: '
           'Einnahmeverlauf, Anteil der Provinz, Empfindlichkeit gegenüber Bodenpreis und Zeitplan.'),
    'phuong-an-tai-chinh': dict(
        en='A whole-life financial plan for the line: capital cost, operating subsidy, TOD revenue, '
           'the provincial budget it requires each year, and sensitivity analysis.',
        zh='线路全生命周期财务方案：投资额、运营补贴、TOD 收入、每年所需地方财政以及敏感性分析。',
        ja='路線の全期間の財務計画：投資額、運営補助、TOD収入、毎年必要となる地方予算、感応度分析。',
        fr='Un plan financier sur toute la durée de vie : investissement, subvention d’exploitation, '
           'recettes TOD, budget provincial annuel requis et analyse de sensibilité.',
        de='Ein Finanzierungsplan über die gesamte Lebensdauer: Investition, Betriebszuschuss, '
           'TOD-Einnahmen, jährlicher Bedarf im Provinzhaushalt und Sensitivitätsanalyse.'),
    'co-cau-nguon-von': dict(
        en='Comparing and combining funding sources for the line — budget, ODA, private capital and '
           'PPP: who carries which risk, and what each source really costs.',
        zh='比较并组合线路资金来源——财政、ODA、社会资本与 PPP：各方承担何种风险，每种来源的真实成本。',
        ja='路線の資金源の比較と組み合わせ——予算、ODA、民間資本、PPP。誰がどのリスクを負い、'
           '各資金源の実質コストはいくらか。',
        fr='Comparer et combiner les sources de financement — budget, APD, capitaux privés et PPP : '
           'qui porte quel risque et ce que chaque source coûte réellement.',
        de='Finanzierungsquellen vergleichen und kombinieren — Haushalt, ODA, privates Kapital und '
           'ÖPP: wer welches Risiko trägt und was jede Quelle wirklich kostet.'),
    'suat-von-dau-tu': dict(
        en='Selecting comparable projects and converting foreign investment rates and norms to the '
           'valuation date under Article 32, with the reasoning needed to defend the file.',
        zh='选取可比项目，依《铁路法》第 32 条将境外投资单价与定额换算至计算时点，'
           '并附可供审查的论证。',
        ja='類似事業を選び、鉄道法第32条により海外の投資原単位と歩掛を算定時点へ換算し、'
           '審査に耐える論拠を添える。',
        fr='Choisir des projets comparables et convertir ratios et normes étrangers à la date de '
           'calcul selon l’article 32, avec l’argumentaire permettant de défendre le dossier.',
        de='Vergleichbare Vorhaben auswählen und ausländische Kennwerte und Normen nach Artikel 32 '
           'auf den Berechnungszeitpunkt umrechnen — mit belastbarer Begründung für die Prüfung.'),
    'kiem-soat-noi-bo': dict(
        en='Spending rules, separation of duties and checkpoints between measurement and payment for '
           'the project management unit, designed backwards from what settlement will demand.',
        zh='为项目管理单位设计支出制度、职责分离以及计量与付款之间的卡口，'
           '从竣工决算的要求倒推而成。',
        ja='事業管理組織の支出規程、職務分離、出来高と支払の間の関所を、'
           '決算で求められるものから逆算して設計する。',
        fr='Règles de dépense, séparation des tâches et points de contrôle entre constat et paiement '
           'pour l’unité de gestion, conçus à rebours des exigences du décompte final.',
        de='Ausgaberegeln, Funktionstrennung und Kontrollpunkte zwischen Aufmaß und Zahlung für die '
           'Projektleitung — rückwärts entwickelt aus dem, was die Abrechnung verlangt.'),
    'ho-so-quyet-toan': dict(
        en='Rules for creating, coding, storing and handing over settlement records from the very '
           'first contract package — for a project that runs eight to twelve years.',
        zh='从第一个标段起，制定竣工决算档案的形成、编码、保管与移交规则——'
           '适用于历时八至十二年的项目。',
        ja='最初の工区から決算書類の作成・付番・保管・引継ぎの規則を定める。'
           '八年から十二年続く事業のために。',
        fr='Règles de création, codification, conservation et remise des dossiers de décompte dès le '
           'premier lot — pour un projet qui dure de huit à douze ans.',
        de='Regeln für Erstellung, Kennzeichnung, Aufbewahrung und Übergabe der '
           'Abrechnungsunterlagen ab dem ersten Los — für ein Vorhaben über acht bis zwölf Jahre.'),
    'tai-co-cau-doanh-nghiep': dict(
        en='Reorganising when the line moves from construction to operation: asset handover, the '
           'operating company’s structure, and the subsidy formula.',
        zh='线路由建设转入运营时的重组：资产移交、运营单位的组织架构以及补贴计算公式。',
        ja='路線が建設から運営へ移る際の再編：資産の引継ぎ、運営組織の体制、補助金の算定式。',
        fr='Réorganisation au passage de la construction à l’exploitation : remise des actifs, '
           'structure de la société d’exploitation et formule de subvention.',
        de='Umbau beim Übergang von Bau zu Betrieb: Vermögensübergabe, Aufbau der '
           'Betriebsgesellschaft und Formel für den Zuschuss.'),
    'thue-du-an': dict(
        en='Foreign contractor tax on rolling stock and signalling, VAT treatment under ODA, and the '
           'investment incentives the Law on Railways already provides.',
        zh='车辆与信号系统的外国承包商税、ODA 资金的增值税处理，以及《铁路法》已给予的投资优惠。',
        ja='車両と信号システムに係る外国契約者税、ODA資金の付加価値税の取扱い、'
           'および鉄道法が既に定める投資優遇。',
        fr='Retenue sur les contractants étrangers pour matériel roulant et signalisation, TVA sur '
           'financement APD, et les incitations que la loi ferroviaire prévoit déjà.',
        de='Quellensteuer für ausländische Auftragnehmer bei Fahrzeugen und Signaltechnik, '
           'Umsatzsteuer bei ODA sowie die im Eisenbahngesetz bereits vorgesehenen Anreize.'),
    'boi-duong-can-bo': dict(
        en='Training built from the unit’s own files, not a ready-made syllabus: settlement, cost '
           'control, payment documentation and preparing for an audit.',
        zh='以本单位真实档案为教材、而非现成讲义的培训：竣工决算、成本控制、'
           '付款单据与迎接审计的准备。',
        ja='既製の教材ではなく当該組織の実際の書類から組み立てる研修：決算、原価管理、'
           '支払書類、監査への備え。',
        fr='Formation bâtie sur les dossiers réels de l’unité, non sur un programme tout fait : '
           'décompte, contrôle des coûts, pièces de paiement et préparation à l’audit.',
        de='Schulung aus den echten Unterlagen der Einheit statt aus fertigem Lehrstoff: '
           'Abrechnung, Kostenkontrolle, Zahlungsbelege und Vorbereitung auf die Prüfung.'),
}
