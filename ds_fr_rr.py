# -*- coding: utf-8 -*-
"""Ban TIENG PHAP: trang VAN BAN (Recherche de textes) va THU VIEN RUI RO (Catalogue de risques).

TEN VAN BAN GIU NGUYEN TIENG VIET — do la ten chinh thuc, dich ra thi khong tra cuu duoc.

⚠ Trang /fr/van-ban/ nam o thu muc khac voi kho tep /van-ban/tep/ nen phai di qua
  _tep_lang() doi duong dan thanh @/van-ban/tep/... — ban 17 da vap 161 lien ket hong.
"""

# =================================================================== VAN BAN
VB = dict(
    td='Textes sur le ferroviaire urbain — recherche',
    mt='51 textes régissant les projets ferroviaires urbains et TOD au Vietnam, filtrables par '
       'niveau, territoire, année et validité, avec le fichier Word ou PDF.',
    duong='Textes',
    h1='Recherche de textes',
    lede='Cinquante et un textes régissant les projets ferroviaires urbains et TOD, chacun '
         'accompagné de son fichier Word ou PDF. Les intitulés restent en vietnamien — ce sont les '
         'dénominations officielles, et ce sont elles qu’il vous faut pour citer ou rechercher '
         'ailleurs.',
    h_cach='Comment utiliser cette page',
    cach=[
        ('Les signes diacritiques sont facultatifs dans la recherche',
         'Les noms de fichiers du fonds ne portent pas de diacritiques, mais le champ de recherche '
         'les retire des deux côtés. « đường sắt » et « duong sat » donnent le même résultat.'),
        ('Rechercher par référence',
         'Si vous vous souvenez du numéro, saisissez le numéro : « 188 », « 62/2026 », '
         '« 15/2025 ». C’est plus rapide que de retrouver l’intitulé complet.'),
        ('Les filtres se cumulent',
         'Les quatre filtres se combinent entre eux et avec le champ de recherche. Par exemple '
         'Thông tư + Hanoï + en vigueur.'),
        ('Cliquer sur l’intitulé ouvre le document',
         'Un clic sur l’intitulé ouvre la version Word ; à défaut, la version PDF. La colonne '
         '<b>Ouvrir le fichier</b> vous laisse choisir le format.'),
        ('Les textes longs paraissent en plusieurs parties',
         'Le Journal officiel publie les textes longs en plusieurs numéros. Ils apparaissent alors '
         'sous la forme <b>W1 W2…</b> ou <b>P1 P2…</b> — il faut toutes les parties pour disposer '
         'du texte intégral.'),
    ],
    h_co='Ce que contient le fonds',
    tk=['Textes', 'Fichiers Word et PDF', 'Word et PDF', 'PDF seulement',
        'Textes consolidés', 'Textes locaux'],
    h_cap='Quatre niveaux — dans quel ordre les lire',
    cap=[
        ('Lois et résolutions de l’Assemblée nationale',
         'Le socle juridique. Pour le ferroviaire urbain, lire d’abord le texte consolidé de la '
         'Luật Đường sắt, puis la Nghị quyết 188/2025 sur le mécanisme spécial — c’est elle qui '
         'modifie effectivement l’ordre des procédures.'),
        ('Décrets',
         'Les modalités d’application. Le texte à lire est la version consolidée '
         'VBHN 34/VBHN-BXD, forte de 143 articles sur la conception technique d’ensemble et le '
         'mécanisme spécial.'),
        ('Circulaires et normes techniques',
         'Normes, prix unitaires, formulaires et exigences techniques. C’est le niveau qui change '
         'le plus souvent — vérifiez toujours quelle version était en vigueur à l’époque.'),
        ('Textes locaux',
         'Résolutions du Conseil populaire provincial. Ce sont elles qui décident de l’argent : '
         'recettes TOD, redevances du sous-sol, politique d’indemnisation. Elles ne valent que '
         'dans cette province.'),
    ],
    h_luu='Deux points de vigilance',
    luu=[
        ('Un texte s’applique selon la date de survenance du fait',
         'Une dépense née en 2022 relève de ce qui était en vigueur en 2022, non de ce qui l’est '
         'aujourd’hui. C’est l’erreur de fondement la plus fréquente dans les dossiers de '
         'décompte.'),
        ('« Abrogé » ne veut pas dire « sans objet »',
         'Un texte abrogé continue de régir tout ce qui s’est produit pendant sa validité. C’est '
         'précisément pour cela que nous conservons les textes abrogés dans le fonds, signalés '
         'comme tels.'),
    ],
    l_cap='Niveau', l_so='Référence', l_ten='Intitulé', l_nam='Année', l_hl='Validité',
    l_tep='Ouvrir le fichier',
    hl_con='En vigueur', hl_het='Abrogé', hn='Consolidé',
    loc_tim='Recherche', loc_cap='Niveau', loc_dia='Territoire', loc_nam='Année',
    loc_tt='Validité',
    loc_tatca='Tous',
    tim_gy='Intitulé, référence ou mot-clé',
    dem='%d textes sur %d',
)

CAP_FR = {'Luật & Nghị quyết QH': 'Loi / résolution AN', 'Nghị định': 'Décret',
          'Thông tư': 'Circulaire', 'Văn bản khác': 'Autre'}
DIA_FR = {'Toàn quốc': 'National', 'Hà Nội': 'Hanoï', 'TP. Hồ Chí Minh': 'Hô-Chi-Minh-Ville'}

# =================================================================== THU VIEN RUI RO
RR = dict(
    td='Catalogue de risques de l’audit du décompte final',
    mt='Trente-trois risques en huit groupes pour l’audit du décompte final d’un projet '
       'ferroviaire urbain : le signe et la manière de le vérifier.',
    duong='Catalogue de risques',
    h1='Catalogue de risques pour l’audit du décompte final',
    lede='Trente-trois risques répartis en huit groupes. Pour chacun : à quoi le signe ressemble '
         'et comment le vérifier. Utilisez-le comme liste de contrôle au moment de planifier un '
         'audit, ou comme auto-contrôle avant qu’un dossier de décompte ne parte au contrôle.',
    h_ng='D’où vient ce catalogue et ce qu’il n’est pas',
    ng='Ce catalogue est établi à partir de l’expérience professionnelle et de sources publiques. '
       'Il constitue une <b>référence générale</b>. Rien n’y provient du dossier d’un organisme '
       'déterminé, et aucune entrée ne décrit un projet réel. Lisez-le comme une liste de points '
       'qu’il vaut la peine de vérifier — non comme une accusation visant quiconque.',
    h_ds='Les huit groupes',
    l_dh='À quoi le signe ressemble', l_kt='Comment le vérifier',
    muc=dict(cao='Élevée', trung='Moyenne', thap='Faible'),
    l_muc='Attention',
    h_dung='Comment l’utiliser',
    dung=[
        'À la planification, parcourez-le et cochez les points applicables à ce projet. Les points '
        'écartés, motivez-les par écrit — c’est la preuve d’un jugement exercé, non d’une '
        'facilité.',
        'À l’exécution, la colonne « comment le vérifier » est un point de départ et ne remplace '
        'pas le programme de travail.',
        'Avant qu’un dossier ne parte au contrôle, le maître d’ouvrage peut passer la même liste '
        'en auto-contrôle. La plupart des points se corrigent encore s’ils sont vus à temps.',
    ],
    h_bt='Si vous souhaitez l’appliquer à votre propre projet',
    bt='Adressez-nous les éléments via la page %s. Nous vous dirons quels groupes comptent le plus '
       'compte tenu de la phase où se trouve votre projet.',
    bt_lk='Conseil',
)

# 8 nhom, moi rui ro: (ten, dau hieu, kiem the nao, muc)
RR_NHOM = [
    ('Dossier juridique', [
        ('L’ordre des procédures est inversé ou une étape manque',
         'Un marché signé avant la décision d’approbation ; un démarrage des travaux avant le '
         'permis de construire.',
         'Confronter la date de signature de chaque pièce sur une frise chronologique — pas '
         'seulement vérifier que la pièce existe.', 'cao'),
        ('Approbation donnée au mauvais niveau',
         'Le signataire de la décision n’est pas compétent pour cette catégorie de projet ou cette '
         'tranche de montant.',
         'Confronter la fonction du signataire aux règles de délégation en vigueur à la date de '
         'signature.', 'cao'),
        ('Mécanisme spécial appliqué hors de son champ',
         'Des procédures abrégées employées pour un projet ou un territoire hors du périmètre '
         'd’expérimentation.',
         'Exiger du maître d’ouvrage la pièce établissant que le projet entre dans le champ '
         'd’application.', 'cao'),
        ('Pièces établies après coup et antidatées',
         'Procès-verbaux et décisions rédigés tardivement mais portant la date qu’ils auraient dû '
         'porter.',
         'Comparer le papier et la mise en page au sein d’un même dossier ; recouper avec le '
         'journal de chantier et les pièces de paiement de la même période.', 'trung'),
    ]),
    ('Financement et paiement', [
        ('Les écritures du maître d’ouvrage diffèrent de celles de l’organisme payeur',
         'Le capital versé selon la comptabilité diffère du chiffre du Trésor ou de la banque '
         'gestionnaire.',
         'Exiger un procès-verbal de rapprochement signé pour chaque exercice ; remonter à la '
         'cause de chaque écart — ne pas accepter un total compensé.', 'cao'),
        ('Les paiements dépassent le montant du marché',
         'La somme des acomptes dépasse le prix du marché augmenté des avenants réguliers.',
         'Additionner tous les acomptes et confronter au prix du marché tel que révisé.', 'cao'),
        ('Avances non intégralement récupérées',
         'Une avance contractuelle n’est pas entièrement apurée alors que les ouvrages sont '
         'achevés.',
         'Tenir par marché un état des avances et de leur récupération, rapproché de la garantie '
         'd’avance.', 'trung'),
        ('Dépenses engagées sans crédits ouverts',
         'Des quantités exécutées alors qu’aucun crédit n’est ouvert au plan d’investissement '
         'public.',
         'Rapprocher les dépenses proposées au décompte des crédits ouverts par exercice.',
         'trung'),
    ]),
    ('Quantités et prix unitaires', [
        ('La quantité liquidée dépasse la quantité réceptionnée',
         'L’état de décompte porte davantage que le procès-verbal de réception correspondant.',
         'Rapprocher les trois : état de décompte — procès-verbal de réception — plan de '
         'récolement.', 'cao'),
        ('Une même quantité comptée dans deux marchés',
         'Un même ouvrage compté dans deux marchés, en général à la jonction de deux lots.',
         'Rechercher les doublons par code de prix et par point kilométrique ; prêter une '
         'attention particulière aux limites de lots.', 'cao'),
        ('Norme de la mauvaise période appliquée',
         'Des normes actuelles appliquées à des quantités réceptionnées des années plus tôt.',
         'Fixer d’abord la date d’application de chaque ouvrage, puis rechercher la norme en '
         'vigueur à cette date.', 'cao'),
        ('Ouvrage spécialisé sans norme approuvée',
         'Creusement de tunnel, montage de la signalisation, essais intégrés — absents du système '
         'général de normes.',
         'Exiger la décision approuvant une norme nouvelle ; à défaut, le poste est dépourvu de '
         'fondement pour le décompte.', 'cao'),
        ('Révision de prix incompatible avec la forme de prix du marché',
         'Une actualisation payée sur un marché à prix forfaitaire ou à prix unitaires fermes.',
         'Établir d’abord la forme de prix stipulée au marché, puis examiner si la révision est '
         'seulement admissible.', 'cao'),
        ('Indice de prix inadéquat',
         'Un indice d’une autre province, d’une autre nature d’ouvrage ou d’une autre période.',
         'Confronter la source de l’indice aux stipulations du marché et à la publication de '
         'l’autorité compétente.', 'trung'),
    ]),
    ('Marchés', [
        ('La forme de prix diffère du mode de règlement effectif',
         'Un marché à prix forfaitaire liquidé sur métré, ou l’inverse.',
         'Lire la clause de prix et la clause de paiement avant de vérifier le moindre chiffre.',
         'cao'),
        ('Avenant signé après achèvement des travaux',
         'Un avenant modifiant les quantités ou le prix, signé après la réception de cette part.',
         'Confronter la date de signature de l’avenant à la date de réception des mêmes ouvrages.',
         'cao'),
        ('Marché EPC sans détail quantitatif',
         'Un marché de forme internationale définissant le périmètre par le résultat, sans détail '
         'quantitatif permettant le contrôle.',
         'Exiger l’analyse de prix et le détail quantitatif de base ; à défaut des deux, énoncer '
         'clairement la limitation d’étendue.', 'cao'),
        ('Le prix révisé dépasse le prix du lot approuvé',
         'Le prix du marché augmenté des avenants dépasse le prix du lot au plan de passation.',
         'Additionner et confronter à la décision approuvant le plan de passation.', 'trung'),
    ]),
    ('Gestion de projet, ingénierie et autres frais', [
        ('Frais de gestion de projet au-dessus de la norme',
         'Les dépenses réelles dépassent le montant résultant du taux appliqué aux coûts de '
         'travaux et d’équipements.',
         'Recalculer avec la norme interpolée entre les deux seuils de taille et confronter au '
         'montant réclamé.', 'trung'),
        ('Postes déjà couverts par la norme facturés en sus',
         'Fournitures de bureau, électricité et eau de l’unité de gestion facturées en plus de la '
         'norme.',
         'Confronter la liste des coûts déjà couverts par la norme aux dépenses réelles.', 'trung'),
        ('Frais d’ingénierie au-dessus du marché',
         'La valeur liquidée d’un marché d’ingénierie dépasse le prix du marché augmenté des '
         'avenants.',
         'Rapprocher chaque marché d’ingénierie et vérifier que les livrables ont bien été '
         'remis.', 'trung'),
    ]),
    ('Actifs et remise', [
        ('La valeur des actifs ne s’équilibre pas avec les dépenses',
         'L’équation ne tient pas : dépenses, moins montants non imputables aux actifs, moins '
         'stocks excédentaires, ne donne pas la valeur des actifs.',
         'Passer l’équation sur un jeu de chiffres unique ; tracer chaque écart avant émission.',
         'cao'),
        ('Charges communes réparties sans principe',
         'Des charges communes ventilées au jugé plutôt qu’au prorata du capital.',
         'Vérifier l’état de répartition et confronter la base de ventilation à la politique '
         'approuvée.', 'trung'),
        ('Actifs manquants ou en doublon entre entités réceptrices',
         'Un même poste figure dans deux procès-verbaux de remise, ou dans aucun.',
         'Rapprocher l’état général des actifs de la somme de tous les procès-verbaux de remise.',
         'trung'),
        ('Dépenses exclues de la valeur des actifs sans autorisation',
         'Des pertes, ou les coûts d’un ouvrage abandonné, sans décision de l’autorité compétente.',
         'Exiger la décision l’admettant ; à défaut, le montant doit rester en suspens et ne peut '
         'être transféré.', 'cao'),
    ]),
    ('Créances, dettes et stocks excédentaires', [
        ('Dettes imputées à la mauvaise partie',
         'Des soldes enregistrés par nom de lot plutôt que par personne morale, ou plusieurs '
         'entreprises confondues.',
         'Rapprocher les soldes par personne morale ; circulariser sous le contrôle de '
         'l’auditeur.', 'trung'),
        ('Confirmations envoyées et reçues par le maître d’ouvrage',
         'L’auditeur ne maîtrise ni l’envoi ni la réception, et l’élément probant perd sa '
         'fiabilité.',
         'L’auditeur maîtrise l’adresse d’envoi et reçoit directement les réponses.', 'cao'),
        ('Matériels excédentaires sans plan d’écoulement',
         'Des matériels demeurent en magasin après achèvement sans décision sur leur sort.',
         'Inventorier physiquement et rapprocher des écritures ; recommander une voie '
         'd’écoulement dans le rapport.', 'thap'),
    ]),
    ('Risques propres aux projets ferroviaires urbains', [
        ('Coûts de marche à blanc mal classés',
         'Électricité, masse salariale d’exploitation et assurances pendant la marche à blanc '
         'imputés aux dépenses d’investissement sans fondement.',
         'Exiger la pièce, établie avant le début de la marche à blanc, approuvant son périmètre '
         'et sa source de financement.', 'cao'),
        ('Coût de l’évaluation de sécurité du système absent du montant total',
         'Un poste réalisé par un organisme étranger indépendant, souvent omis lors de la '
         'préparation du projet.',
         'Rapprocher le marché d’évaluation de sécurité du montant total approuvé.', 'trung'),
        ('Écarts de change sur les prêts et les équipements importés',
         'Des taux appliqués de façon inégale selon la nature des opérations, ou à la mauvaise '
         'date.',
         'Contrôler les écarts de change séparément ; confronter les taux retenus aux stipulations '
         'des marchés.', 'cao'),
        ('Formation et transfert de technologie : création d’actif incertaine',
         'Des montants élevés qui ne constituent aucune immobilisation et restent facilement en '
         'suspens au décompte.',
         'Exiger une décision de l’autorité compétente sur leur imputation ou non à la valeur des '
         'actifs.', 'trung'),
        ('Frontière de coûts floue entre la ligne et le périmètre TOD',
         'Les flux et les actifs des deux se mêlent et ne peuvent plus être séparés à la remise.',
         'Vérifier si une politique de séparation des coûts a été arrêtée dès la phase de '
         'préparation.', 'trung'),
    ]),
]
