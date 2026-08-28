# -*- coding: utf-8 -*-
"""Ban TIENG PHAP: trang QUY TRINH (Déroulement) va KIEM TOAN QT (Audit du décompte final).

Ten van ban phap luat GIU NGUYEN so hieu tieng Viet — do la ten chinh thuc.
Phan dien giai la cach doc cua ASCO, khong phai ban dich chinh thuc.

🔴 BAY DON VI TIEN — tieng Phap dung THANG DAI giong tieng Duc:
  **"billion" tieng Phap = 10^12**, KHONG phai ty. Ty = **milliard**.

  | Viet          | Phap                      | KHONG duoc viet        |
  |---------------|---------------------------|------------------------|
  | 1 ty dong     | 1 milliard de VND         | ~~1 billion de VND~~   |
  | 5 ty dong     | 5 milliards de VND        |                        |
  | 120 ty dong   | 120 milliards de VND      |                        |
  | 1.000 ty dong | 1 000 milliards de VND    | ~~1 billion~~          |
  | 10.000 ty     | 10 000 milliards de VND   |                        |

  Ban tieng Anh dung "Billion VND" nghia la TY — dich thang sang Phap la sai 1.000 lan.
  Cung ho bay voi 亿 (Trung), 億 (Nhat), Billion (Duc).

⚠ Cach viet so tieng Phap:
  - Dau thap phan la DAU PHAY: 0,3375 %
  - Phan cach nghin la KHOANG TRANG: 445 500 000
  - Co KHOANG TRANG truoc dau % va dau hai cham: "0,96 %" · "Note :"
  toLocaleString('fr-FR') tu lam dung hai cai dau.
"""

# =================================================================== QUY TRINH
QT = dict(
    td='Déroulement d’un projet ferroviaire urbain — neuf phases',
    mt='Les neuf phases d’un projet ferroviaire urbain au Vietnam : ce qui se passe, qui décide, '
       'quels textes s’appliquent et où les dossiers achoppent.',
    duong='Déroulement',
    h1='Les neuf phases d’un projet ferroviaire urbain',
    lede='Cette page suit une ligne depuis son inscription au schéma provincial jusqu’au jour où '
         'son décompte final est approuvé. Pour chaque phase : le travail lui-même, qui détient '
         'le pouvoir de décision, les textes applicables, les pièces produites et l’endroit où '
         'les dossiers achoppent le plus souvent. L’ordre est pensé à rebours, depuis le décompte '
         'final — car ce qu’une phase omet de consigner est précisément ce qui ne pourra pas être '
         'liquidé des années plus tard.',
    h_gd='Les neuf phases',
    l_viec='Ce qui se passe', l_tq='Qui décide', l_cc='Textes applicables',
    l_kq='Ce qui est produit', l_bay='Où cela achoppe habituellement',
    h_ngan='Quatre régimes juridiques — lire le bon',
    ngan_lede='Un projet ferroviaire urbain ne relève pas d’un corpus unique. Le régime applicable '
              'détermine quelles étapes peuvent être abrégées et lesquelles ne le peuvent pas. '
              'Se tromper au départ coûte cher à défaire.',
    l_pv='Champ d’application', l_vb='Textes',
    h_ho='Trois points où le mécanisme reste ouvert',
    ho_lede='Ce ne sont pas des lacunes de notre recherche. Ce sont des dispositions qui renvoient '
            'à un texte ultérieur qui n’a pas encore été pris. Tant qu’il manque, la question ne '
            'peut pas être chiffrée — et un projet qui suppose le contraire bâtit sur du sable.',
    h_ke='Où intervient l’audit',
    ke='Des phases six à neuf, l’auditeur devrait déjà être présent plutôt que d’attendre la fin. '
       'Le pourquoi et la répartition du travail figurent sous %s.',
    ke_lk='Audit du décompte final',
)

# 9 giai doan: (ten, viec, tham quyen, can cu, ket qua, cai bay)
QT_GD = [
    ('Planification et conception du tracé',
     'Inscription de la ligne au schéma provincial et au plan directeur d’urbanisme ; fixation du '
     'tracé, de l’emplacement des stations et du dépôt ; élaboration de la variante de tracé ; '
     'délimitation provisoire du périmètre TOD.',
     'Le Comité populaire provincial soumet ; le Conseil populaire provincial approuve ce qui '
     'relève de sa compétence',
     'Luật Quy hoạch đô thị và nông thôn 47/2024/QH15 · Luật Quy hoạch 112/2025/QH15 · '
     'Hanoï : NQ 64/2026/NQ-HĐND sur la planification du sous-sol',
     'Plan de tracé approuvé · variante de tracé · limite provisoire du périmètre TOD',
     'Le tracé est dessiné sur le plan mais non implanté sur le terrain ; les acquisitions '
     'foncières se révèlent ensuite décalées. La planification du sous-sol n’existe pas encore, '
     'de sorte que la limite verticale des stations souterraines ne peut être arrêtée.'),
    ('Décision sur l’orientation d’investissement',
     'Élaboration de la proposition d’orientation d’investissement ou de l’étude préalable ; '
     'examen de la source de financement et de la capacité d’équilibre ; décision sur '
     'l’orientation d’investissement.',
     'L’Assemblée nationale pour les projets d’importance nationale · le Premier ministre · '
     'le Conseil populaire provincial',
     'Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (modifié par NĐ 275/2025) · '
     'NĐ 19/2026 sur l’examen des projets d’importance nationale',
     'Résolution ou décision d’orientation · montant total d’investissement provisoire · '
     'structure de financement',
     'Le montant provisoire repose sur des données de reconnaissance minces ; l’écart se creuse '
     'lors de la préparation effective. Là où le mécanisme spécial supprime cette étape, il manque '
     'au dossier de décompte un maillon que l’on s’attend à y trouver — préparez la pièce de '
     'substitution à l’avance.'),
    ('Préparation, examen et approbation du projet',
     'Reconnaissance des sols ; étude de faisabilité et avant-projet, ou conception technique '
     'd’ensemble au titre du mécanisme spécial ; examen par l’autorité technique compétente ; '
     'avis de sécurité incendie et évaluation environnementale.',
     'L’autorité décisionnaire par délégation ; pour les projets relevant de NQ 188, la compétence '
     'est largement transférée à la province',
     'Luật Xây dựng 135/2025/QH15 · NĐ 209/2026 et NĐ 210/2026 · NĐ 206/2026 sur la maîtrise des '
     'coûts · VBHN 34/VBHN-BXD sur la conception technique d’ensemble',
     'Décision d’approbation · montant total d’investissement approuvé — c’est le plafond '
     'juridique de toute dépense qui sera liquidée par la suite',
     'C’est sur les quantités en souterrain que la conception et les conditions réelles de terrain '
     'divergent le plus. Les projets préparés avant le 30 juillet 2026 ne disposaient d’aucune '
     'norme métro propre et ont dû emprunter des normes étrangères.'),
    ('Acquisitions foncières et réinstallation',
     'Notification de reprise des terrains ; état des lieux ; élaboration, affichage et '
     'approbation du plan d’indemnisation, d’aide et de réinstallation ; paiement ; remise des '
     'emprises par tranches. Se déroule en parallèle de la phase 3.',
     'Le Comité populaire compétent pour la reprise des terrains et l’approbation du plan',
     'Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · '
     'Hanoï, en périmètre TOD : NQ 66/2026/NQ-HĐND',
     'Décision de reprise par parcelle · plan d’indemnisation approuvé · procès-verbaux de remise '
     'des emprises',
     'Les emprises sont remises par morceaux, si bien que l’entreprise ne peut organiser une '
     'chaîne de production et réclame des frais d’immobilisation. Des signatures manquent aux '
     'pièces de paiement, et cela n’apparaît qu’au décompte — les bénéficiaires ont alors déménagé.'),
    ('Sélection des entreprises et conclusion des marchés',
     'Élaboration et approbation du plan de passation ; publication du dossier de consultation ; '
     'évaluation ; examen et approbation du résultat ; négociation et signature.',
     'L’autorité compétente et le maître d’ouvrage au titre du droit de la commande publique',
     'Luật Đấu thầu 22/2023/QH15 (modifiée par Luật 57/2024 et Luật 90/2025) · NĐ 214/2025 · '
     'pour les PPP : TT 98/2025/TT-BTC et TT 142/2025/TT-BTC',
     'Décision d’approbation du résultat · marché, avec la forme de prix qui y est stipulée',
     'La forme de prix inscrite au marché ne correspond pas à la manière dont les parties règlent '
     'effectivement — un marché à prix forfaitaire liquidé sur métré, ou l’inverse. C’est de là que '
     'naît la plus grande part des litiges au décompte.'),
    ('Exécution, maîtrise des coûts et modifications',
     'Étapes de conception ultérieures ; élaboration, examen et approbation des estimations ; '
     'exécution ; réception des quantités par phase ; paiement ; traitement des modifications et '
     'des révisions.',
     'Le maître d’ouvrage pour les estimations dans le périmètre approuvé ; l’autorité '
     'décisionnaire pour les modifications du projet',
     'NĐ 206/2026 sur la maîtrise des coûts · NĐ 207/2026 sur la qualité · '
     'TT 36/2026, TT 37/2026, TT 38/2026 sur les normes et les coûts',
     'Estimations approuvées par ouvrage · procès-verbaux de réception des quantités · plans de '
     'récolement · dossiers de paiement par tranche',
     'Les normes sont ce que l’on se trompe le plus facilement — un même ouvrage relève de normes '
     'différentes selon la période, et c’est celle en vigueur à la date de l’estimation qui '
     's’applique. Les ouvrages spécialisés comme le creusement de tunnel et la signalisation ne '
     'disposent d’aucune norme nationale.'),
    ('Réception, marche à blanc et certification de sécurité du système',
     'Réception des ouvrages achevés ; essais statiques et dynamiques ; marche à blanc intégrée de '
     'l’ensemble du système ; évaluation et certification de la sécurité du système ; réception '
     'par l’État ; autorisation d’exploitation.',
     'Le maître d’ouvrage procède à la réception ; l’autorité technique contrôle cette réception ; '
     'le régulateur sectoriel délivre l’autorisation d’exploitation',
     'Luật Đường sắt 95/2025/QH15 (texte consolidé 75/VBHN-VPQH) · NĐ 16/2026 · '
     'TT 62/2026/TT-BXD norme métro · VBHN 13/VBHN-BXD sur le raccordement au réseau national',
     'Procès-verbaux de réception · dossier de marche à blanc · certificat de sécurité du système '
     '· décision de mise en service',
     'C’est la phase qui dépasse le plus souvent les délais. L’électricité, le personnel '
     'd’exploitation et les assurances sont engagés alors que les ouvrages ne sont pas remis et ne '
     'produisent aucune recette. Savoir si ce sont des dépenses d’investissement ou '
     'd’exploitation doit être tranché par écrit au préalable.'),
    ('Remise, comptabilisation des actifs et mise en exploitation',
     'Remise des ouvrages et des dossiers à l’exploitant ; établissement de la propriété et '
     'désignation du gestionnaire des actifs d’infrastructure ; inventaire, déclaration et '
     'amortissement ; construction du dispositif tarifaire et de subvention.',
     'L’autorité qui désigne le gestionnaire des actifs d’infrastructure ; le Comité et le Conseil '
     'populaires provinciaux pour les tarifs et la subvention',
     'NĐ 15/2025 sur les actifs d’infrastructure ferroviaire · TT 75/2025/TT-BTC sur '
     'l’amortissement · TT 34/2025 et TT 33/2025/TT-BXD · '
     'Luật Quản lý, sử dụng tài sản công 15/2017/QH14',
     'Procès-verbaux de remise par entité réceptrice · liste et valeur des actifs constitués par '
     'l’investissement',
     'On remet d’abord, on évalue ensuite — les rames circulent alors que la valeur des actifs '
     'n’est pas arrêtée, l’exploitant comptabilise des montants provisoires, et tout doit être '
     'repris une fois le décompte clos.'),
    ('Décompte final du capital investi',
     'Clôture et rapprochement du capital versé ; établissement du rapport de décompte final ; '
     'audit indépendant de ce rapport ; contrôle administratif ; approbation du décompte ; '
     'apurement des créances, des dettes et des matériels excédentaires.',
     'L’autorité approbatrice par délégation ; l’autorité financière conduit le contrôle',
     'NĐ 254/2025 (remplaçant NĐ 99/2021) · TT 147/2025/TT-BTC · TT 73/2026/TT-BTC sur les '
     'formulaires · audit selon VSA 1000',
     'Rapport de décompte final · rapport d’audit indépendant · rapport de contrôle · décision '
     'd’approbation',
     'Le dossier a traversé plusieurs générations de décrets ; ceux qui l’ont constitué sont '
     'partis ; les pièces des premières années ont disparu. Les dépenses non imputables à la '
     'valeur des actifs restent en suspens tant que l’autorité compétente ne les a pas admises '
     'par écrit.'),
]

# 4 ngan phap ly: (ma, ten, pham vi, van ban, mau)
QT_NGAN = [
    ('A', 'Métro de Hanoï / Hô-Chi-Minh-Ville, investissement public',
     'Situé à Hanoï ou à Hô-Chi-Minh-Ville',
     'NQ 188/2025/QH15 · Luật Đường sắt 95/2025/QH15 · VBHN 34/VBHN-BXD', 'ngoc'),
    ('B', 'Métro ailleurs, investissement public',
     'Hors Hanoï et Hô-Chi-Minh-Ville',
     'Luật Đường sắt 95/2025/QH15 · Luật Đầu tư công 58/2024/QH15 · Luật Xây dựng. '
     'NQ 188 ne peut être invoquée', 'do'),
    ('C', 'Métro en PPP',
     'Réalisé au titre d’un contrat de partenariat public-privé',
     'Luật PPP 64/2020/QH14 (texte consolidé 81/VBHN-VPQH) · NĐ 243/2025 · NĐ 312/2025', 'nhan'),
    ('D', 'Périmètre TOD attaché à la ligne',
     'La zone autour des stations et du dépôt',
     'Luật Thủ đô 02/2026/QH16 · résolutions du Conseil populaire provincial '
     '(Hanoï : NQ 71/2025, 66/2026, 67/2026 — Hô-Chi-Minh-Ville : NQ 21/2026)', 'muc'),
]

# 3 cho ho: (ten, giai thich)
QT_HO = [
    ('Coefficient d’avantage TOD de Hanoï — non encore pris',
     'L’article 8 de NQ 67/2026/NQ-HĐND charge le Comité populaire de soumettre au Conseil '
     'populaire le coefficient d’avantage TOD et les taux, une fois le plan du périmètre TOD '
     'approuvé. Cette résolution n’est pas intervenue. Sans elle, les quatre recettes TOD ne '
     'peuvent être converties en argent.'),
    ('Redevance de raccordement au sous-sol à Hanoï — non encore prise',
     'L’article 3, alinéa 2, de NQ 65/2026/NQ-HĐND prévoit de soumettre la redevance de '
     'raccordement une fois le plan du sous-sol approuvé. Tant que ce texte n’existe pas, '
     'l’obligation de raccordement des immeubles voisins à une station souterraine ne peut être '
     'déterminée.'),
    ('Décret d’application de Luật Thủ đô 02/2026 — introuvable',
     'QĐ 762/QĐ-TTg est le plan de mise en œuvre de Luật Thủ đô 39/2024, pris avant l’existence '
     'de la nouvelle loi. Nous n’avons trouvé ni décision de remplacement pour Luật 02/2026, ni '
     'décret d’application.'),
]

# =================================================================== KIEM TOAN QT
KT = dict(
    td='Audit du décompte final d’une opération achevée',
    mt='Treize domaines de travaux, deux équations de rapprochement et pourquoi un grand projet '
       'de métro doit être audité en continu plutôt qu’à la fin.',
    duong='Audit du décompte final',
    h1='Auditer le rapport de décompte final d’une opération achevée',
    lede='Sur une ligne de métro, l’audit ne devrait pas attendre l’inauguration. Une ligne prend '
         'huit à quinze ans ; les éléments probants que l’on ne voit pas au moment où ils '
         'existent ne se récupèrent pas ensuite. Cette page expose ce que couvre l’audit et '
         'pourquoi, sur un projet de cette taille, le travail se déroule en parallèle du chantier.',
    h_sh='Ce qu’est un audit en continu',
    sh='Auditer en continu, c’est intervenir pendant le chantier, par tranches, plutôt qu’une '
       'seule fois à la fin. Chaque tranche clôt une phase ou un marché ; la dernière consolide. '
       'Ce n’est pas un autre niveau d’exigence — c’est le même travail, placé là où les éléments '
       'probants existent encore.',
    h_vs='Cinq raisons pour lesquelles un grand projet doit être audité en continu',
    h_ss='Les deux approches, côte à côte',
    ss_cot=('', 'Audit après achèvement', 'Audit en continu'),
    h_ph='Treize domaines de travaux',
    ph_lede='L’indexation suit le dossier d’audit type de la VACPA pour les rapports de décompte '
            'final d’opérations achevées (QĐ 314-2016/QĐ-VACPA). La numérotation est celle du '
            'dossier, non l’ordre d’exécution.',
    h_cd='Deux rapprochements avant émission',
    cd_lede='Les deux portent sur le même jeu de chiffres. S’ils ne s’équilibrent pas, le rapport '
            'n’est pas émis.',
    h_kl='Trois choses qu’un auditeur ne fait pas',
    h_phi='Honoraires d’audit — calculez-les ici',
    phi_1='Au titre du <b>Nghị định 193/2026/NĐ-CP, article 20</b>, en vigueur depuis le '
          '1<sup>er</sup> juillet 2026. Saisissez le montant à auditer et les honoraires '
          's’affichent.',
    phi_2='Ces taux sont <b>inchangés</b> par rapport à l’article 45 du Nghị định 254/2025/NĐ-CP — '
          'nous avons vérifié chaque chiffre. Le nouveau décret ne fait que renuméroter l’article.',
    l_gt='Montant à auditer',
    l_gt_phu='Le montant proposé au décompte ; à défaut, le montant total d’investissement',
    l_dv='Unité',
    # 🔴 l_ty = TY DONG. Tieng Phap phai la "milliards", KHONG phai "billions" (= 10^12).
    l_ty='Milliards de VND', l_tr='Millions de VND', l_d='VND',
    l_vat='TVA', l_kvat='Non applicable',
    tick_tb='<b>La part des équipements atteint 50 % ou plus</b> — article 20, alinéa 1, point d : '
            'les honoraires s’élèvent à <b>70 %</b> du montant normal',
    tick_bt='<b>Il s’agit de dépenses d’indemnisation, d’aide et de réinstallation</b> — point đ : '
            'les honoraires s’élèvent à <b>50 %</b> du montant normal',
    tick_kt='<b>Déjà audité de façon indépendante, par la Cour des comptes ou par une '
            'inspection</b> — point e : seuls les frais de <b>contrôle</b> sont à <b>50 %</b>',
    kq_gt='Assiette de calcul', kq_ty='Taux appliqué', kq_hs='Coefficient d’ajustement',
    kq_truoc='Honoraires hors taxe', kq_vat='TVA',
    kq_nhan='Plafond des honoraires d’audit', kq_phu='TVA comprise',
    kq_tt='Frais de contrôle et d’approbation du décompte',
    kq_tt_ghi='Ces frais sont perçus par l’autorité de contrôle — ce ne sont pas des honoraires '
              'versés à l’auditeur, et la TVA ne s’y ajoute pas.',
    kq_loi='Veuillez saisir une valeur supérieure à zéro.',
    kq_toi='* Le minimum d’un million de VND prévu à l’article 20, alinéa 1, point b, a été '
           'appliqué.',
    h_bang='Le barème',
    bang_gt='Montant (milliards de VND)', bang_kt='Audit indépendant (%)', bang_tt='Contrôle (%)',
    bang_ghi='Un montant compris entre deux seuils fait l’objet d’une interpolation linéaire au '
             'titre de l’article 20, alinéa 1, point a : '
             '<code>Ki = Kb − (Kb − Ka) × (Gi − Gb) ÷ (Ga − Gb)</code>. '
             'Le calculateur ci-dessus le fait déjà.',
    h_nho='Quatre points à retenir sur ce montant',
    nho='<b>Premièrement —</b> il s’agit d’un <b>plafond</b>, non du prix que vous devez payer. '
        'Un prix de marché peut être inférieur, et l’est généralement en concurrence.<br><br>'
        '<b>Deuxièmement —</b> les honoraires d’audit minimaux sont d’<b>un million de VND</b> '
        'hors taxe ; les frais de contrôle minimaux, de <b>cinq cent mille VND</b>.<br><br>'
        '<b>Troisièmement —</b> les honoraires d’audit <b>sont soumis à la TVA</b> ; les frais de '
        'contrôle ne le sont pas.<br><br>'
        '<b>Quatrièmement —</b> ce montant sert à <b>estimer un marché</b>. Les honoraires d’une '
        'mission réelle dépendent aussi du volume des pièces, du nombre de marchés, du lieu et du '
        'temps disponible.',
    h_sh2='Ce qu’il en est sur un projet audité en continu',
    sh2='Le taux s’applique au <b>montant à auditer du projet dans son ensemble</b>, non à la '
        'somme des tranches. Découper le travail en tranches relève de l’organisation, non d’un '
        'moyen de multiplier les honoraires.',
    sh3='En pratique, le coût total d’une mission en continu dépasse le taux d’une mission unique, '
        'car le travail est réellement plus important — davantage de visites sur site, davantage '
        'd’heures. Cet écart se convient au contrat et doit être admis par l’autorité compétente.',
    h_bt='Si vous arbitrez l’approche pour votre propre projet',
    bt='Auditer après achèvement ou en continu dépend de la taille du projet, de sa durée et du '
       'nombre de marchés. Transmettez-nous les éléments via la page %s et nous vous donnerons '
       'notre avis sur l’approche et le volume de travail prévisible.',
    bt_lk='Conseil',
)

KT_VS = [
    ('Les pièces des premières années ne subsistent pas intactes',
     'Une ligne de métro court sur huit à quinze ans. Attendez l’achèvement et les pièces des '
     'premières années auront pâli, les signataires auront changé de poste, les sous-traitants '
     'auront été liquidés. L’auditeur ne trouve pas d’éléments probants — et sans éléments '
     'probants, pas d’opinion.'),
    ('Les quantités en souterrain ont été recouvertes',
     'Le ferraillage avant coulage, le soutènement avant le revêtement — cela ne se voit qu’une '
     'fois, au moment de l’exécution. Ensuite, plus personne ne peut mesurer à nouveau, quelle que '
     'soit sa volonté. L’auditeur qui arrive après n’a plus que le dossier.'),
    ('Une erreur découverte tard ne se corrige plus',
     'Une dépense dépourvue de décision de l’autorité compétente peut être régularisée si elle est '
     'décelée dans l’année où elle naît. Sept ans plus tard, la personne qui détenait cette '
     'compétence est à la retraite, et son successeur ne signera pas pour ce qu’il n’a pas suivi.'),
    ('Tout reporter à la fin allonge le décompte',
     'Un projet de plusieurs milliers de milliards de VND compte des dizaines de milliers de '
     'pièces. Les verser toutes dans un audit final unique, c’est passer des mois à trier avant '
     'même de contrôler. Découpé par phase, chaque tranche reste maniable et les suivantes '
     'héritent des précédentes.'),
    ('Le maître d’ouvrage apprend où il se trompe alors qu’il est encore temps',
     'C’est la plus grande valeur. L’audit en continu ne sert pas qu’à détecter ; il permet au '
     'maître d’ouvrage de changer sa façon de constituer les dossiers dès le marché suivant. Une '
     'observation formulée la deuxième année épargne des mois la dixième.'),
]

KT_SS = [
    ('Point de départ', 'Après achèvement des ouvrages',
     'Dès la phase de chantier, par tranches'),
    ('Découpage du travail', 'Un passage unique sur l’ensemble du projet',
     'Plusieurs tranches par phase ou par marché, avec une tranche finale de consolidation'),
    ('Éléments probants', 'Pièces écrites seulement ; les ouvrages cachés ne sont pas vérifiables',
     'Constat direct des ouvrages sur le point d’être recouverts, et inventaires physiques sur site'),
    ('Lorsqu’une erreur est décelée', 'Souvent trop tard pour compléter le dossier',
     'Il reste du temps pour régulariser ou solliciter une décision'),
    ('Durée du décompte', 'Longue, car il faut reconstituer des pièces de plusieurs années',
     'Plus courte, l’essentiel étant déjà contrôlé et arrêté'),
    ('Coût de l’audit', 'Moindre en mission unique, mais risque élevé de dossier en suspens',
     'Plus élevé au total, en échange d’un risque moindre et d’un décompte plus rapide'),
    ('Convient à', 'Petits projets de moins de deux ans',
     'Projets du groupe A, projets d’importance nationale, projets à marchés multiples, projets ODA'),
]

KT_PH = [
    ('1000', 'Planification de l’audit',
     'Acceptation de la mission et appréciation du risque · compréhension du projet et de son '
     'contrôle interne · analyse préliminaire du rapport de décompte · fixation du seuil de '
     'signification et de la méthode de sondage · plan d’audit général.',
     'Un seuil de signification mal fixé entraîne dans l’erreur tous les échantillons qui suivent.'),
    ('3000', 'Dossier juridique du projet',
     'Rapprochement du dossier juridique avec les exigences réglementaires · vérification de la '
     'compétence d’approbation · appréciation du respect de la procédure d’investissement, de la '
     'procédure de passation et de la conclusion des marchés.',
     'Lorsqu’un mécanisme spécial est appliqué, il faut d’abord établir que le projet entre dans '
     'son champ avant d’admettre une étape abrégée.'),
    ('4000', 'Sources du capital investi',
     'Vérification des soldes et mouvements de chaque source · rapprochement du capital versé '
     'entre le maître d’ouvrage et l’organisme payeur · vérification des augmentations, '
     'diminutions et de leur comptabilisation.',
     'C’est là que les écarts apparaissent le plus souvent — et c’est aussi le plus facile à '
     'tenir propre si le rapprochement est fait chaque année.'),
    ('5100', 'Dépenses d’indemnisation, d’aide et de réinstallation',
     'Rapprochement avec le plan d’indemnisation approuvé · vérification jusqu’à la décision '
     'd’indemnisation de l’autorité compétente · état récapitulatif des paiements · pièces de '
     'paiement et attestations des bénéficiaires.',
     'Une pièce de paiement sans signature est presque impossible à compléter, le bénéficiaire '
     'ayant déménagé.'),
    ('5200', 'Dépenses de travaux',
     'Rapprochement du décompte A-B avec le rapport de décompte · vérification des quantités et '
     'des prix unitaires selon la forme de prix réellement appliquée · rapprochement des '
     'procès-verbaux de réception et des pièces qualité · vérification du décompte des '
     'modifications.',
     'Le domaine le plus important. Appliquer la méthode de contrôle d’une forme de prix à une '
     'autre est l’erreur la plus fréquente de toutes.'),
    ('5300', 'Dépenses d’équipements',
     'Rapprochement du décompte du marché · vérification de la liste, du type, de l’origine, de la '
     'qualité et de la configuration des équipements au regard de l’estimation et du marché · '
     'vérification du décompte des modifications.',
     'Sur un métro, la part des équipements est très importante et majoritairement importée — le '
     'taux de conversion doit aussi être vérifié.'),
    ('5400', 'Matériels et équipements fournis par le maître d’ouvrage',
     'Consolidation des entrées, sorties et stocks · vérification des entrées quant aux quantités, '
     'certificats d’origine et de qualité, et prix unitaires · vérification des sorties destinées '
     'au montage par chaque entreprise.',
     'Un écart inexpliqué entre entrées, sorties et stocks est le signal qu’il faut élargir '
     'l’étendue des contrôles.'),
    ('5500', 'Frais de gestion de projet, d’ingénierie et autres',
     'Rapprochement avec l’estimation générale approuvée · vérification des dépenses réalisées par '
     'le maître d’ouvrage lui-même, achats et masse salariale de l’unité de gestion compris · '
     'vérification des dépenses engagées par les prestataires.',
     'Elles doivent être recalculées selon les normes en vigueur à l’époque considérée, non selon '
     'les normes actuelles.'),
    ('6000', 'Dépenses non imputables à la valeur des actifs',
     'Deux catégories : les pertes de force majeure dont l’exclusion est admise, et les dépenses '
     'ne créant aucun actif. On vérifie la nature et le montant de la perte au regard de la '
     'décision de l’autorité compétente, ainsi que la compétence de celle-ci.',
     'Sans décision l’admettant, le montant reste en suspens et ne peut être liquidé.'),
    ('7000', 'Valeur des actifs constitués par l’investissement',
     'Consolidation des actifs à long et court terme · politique de répartition des charges '
     'communes · classement par source de financement et par utilisateur · décisions de transfert '
     'et procès-verbaux de remise · valeur résiduelle des biens propres de l’unité de gestion.',
     'Sur un métro, les actifs reviennent à plusieurs entités réceptrices différentes ; le détail '
     'doit donc être séparé clairement dès le départ.'),
    ('8000', 'Créances, dettes et matériels excédentaires',
     'Vérification des soldes par entreprise · confirmation des soldes par circularisation sous le '
     'contrôle de l’auditeur · vérification des soldes de caisse et de banque · vérification des '
     'entrées, sorties et stocks de matériels excédentaires.',
     'L’auditeur doit maîtriser l’envoi comme la réception des demandes de confirmation — ne '
     'jamais s’en remettre au maître d’ouvrage.'),
    ('9000', 'Respect des obligations par le maître d’ouvrage',
     'Examen du respect du droit de l’investissement et de la construction · respect des '
     'obligations comptables et de décompte · et mise en œuvre des conclusions des inspections et '
     'de la Cour des comptes.',
     'Un grand projet a presque certainement subi au moins une inspection — omettre ce point '
     'produit un rapport qui contredit les constats d’un organe de l’État.'),
    ('2000', 'Consolidation, revue et émission',
     'Consolidation des résultats et vérification de l’équilibre des chiffres · consolidation des '
     'propositions de correction · liste des points non arrêtés · lettre d’affirmation du maître '
     'd’ouvrage · procès-verbal de la réunion de clôture · revue à chaque niveau · autorisation '
     'd’émission.',
     'Les équations de rapprochement doivent être passées avant émission — si elles ne '
     's’équilibrent pas, le rapport n’est pas émis.'),
]

KT_CD = [
    ('Sources et dépenses',
     'Capital investi total (4000) ≈ Dépenses d’investissement proposées au décompte (5000)',
     'Un écart signifie soit qu’un capital n’est pas comptabilisé, soit qu’une dépense n’a aucune '
     'source derrière elle.'),
    ('Dépenses et valeur des actifs',
     'Dépenses d’investissement (5000) − Non imputable aux actifs (6000) − Matériels excédentaires '
     '(8200) = Valeur des actifs constitués (7000)',
     'C’est le dernier rapprochement avant émission. Un écart d’un dong doit encore être tracé.'),
]

KT_KL = [
    ('Nous n’auditons pas un projet dont nous sommes le conseil',
     'Constituer un dossier puis contrôler le dossier que l’on a soi-même constitué détruit '
     'l’indépendance. C’est une interdiction ; aucune mesure de sauvegarde n’y remédie.'),
    ('Nous ne constituons pas le dossier à la place du maître d’ouvrage',
     'L’auditeur signale ce qui manque, mais c’est au maître d’ouvrage de constituer et de signer '
     'le dossier. Le faire à sa place efface la frontière des responsabilités.'),
    ('Nous n’exprimons pas d’opinion sans éléments probants suffisants',
     'Lorsque les éléments manquent, nous le disons et en indiquons l’incidence, plutôt que de '
     'déduire un chiffre pour que le rapport paraisse complet.'),
]
