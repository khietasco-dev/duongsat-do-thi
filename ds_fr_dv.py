# -*- coding: utf-8 -*-
"""Ban TIENG PHAP: 9 trang dich vu cap 2 — /fr/dich-vu/<slug>/.

Ten van ban phap luat GIU NGUYEN so hieu tieng Viet.
Phan "Fondements juridiques" ghi ro la CACH DOC CUA ASCO, khong phai ban dich chinh thuc.

🔴 Nhac lai bay don vi tien: "billion" tieng Phap = 10^12. Ty = "milliard".
   Xem ds_fr_qt.py phan dau file.

⚠ Nguong SEO: title <= 60, mo ta <= 160 ky tu. Tieng Phap dai — da rut gon san.
"""

KHUNG = dict(
    duong_nha='Accueil', duong_dv='Prestations',
    h_vande='Difficultés fréquentes',
    h_cancu='Fondements juridiques',
    cancu_nhac='Le texte ci-dessous est <b>notre lecture</b> de chaque disposition, non une '
               'traduction officielle. Seul le texte vietnamien fait foi — chaque document '
               's’ouvre depuis la rubrique %s.',
    cancu_lk='Recherche de textes',
    h_lamgi='Ce que nous faisons',
    h_daura='Ce que vous recevez',
    h_khinao='Quand nous solliciter',
    luu_h='Deux conditions, que nous énonçons d’emblée.',
    luu='Premièrement, il s’agit d’une prestation relevant de l’article 40, alinéa 2, de la '
        'Luật Kiểm toán độc lập — une société d’audit doit l’enregistrer auprès du ministère des '
        'Finances avant de la fournir. Deuxièmement, si nous auditons votre organisme, ou si cela '
        'est prévisible, cette mission doit passer un contrôle d’indépendance au titre de '
        'l’article 30 de la même loi avant signature. Nous procédons d’abord à ce contrôle et, '
        's’il n’est pas concluant, nous le disons franchement et déclinons.',
    bt_h='L’étape suivante',
    bt='Décrivez votre situation sur la page %s ou appelez le <b>0825092007</b>. Nous lisons, '
       'qualifions et répondons sous 24 heures ouvrées — y compris lorsque la réponse est que le '
       'travail sort de ce qui nous est permis.',
    bt_lk='Demander conseil',
    bt_ve='← Voir les neuf prestations',
)

FR = {
    'thu-hoi-von-tod': dict(
        td='Retour sur investissement par le foncier TOD',
        mt='Un modèle de flux pour le foncier TOD au titre de l’article 25 : calendrier des '
           'recettes, part conservée par la province et tests de sensibilité.',
        ten='Conseil sur le retour sur investissement par le foncier TOD',
        lede='Un transport ferroviaire urbain ne s’autofinance presque jamais par les recettes '
             'tarifaires. La véritable source de retour est la hausse de valeur des terrains '
             'autour des stations — et la loi ouvre désormais à la province une voie pour '
             'conserver cette valeur. La difficulté est de transformer un mécanisme légal en un '
             'flux de trésorerie que l’on puisse inscrire dans un plan de financement et défendre '
             'devant l’autorité d’examen.',
        van_de=[
            'Le mécanisme de constitution de terrains à mettre aux enchères existe, mais personne '
            'n’a chiffré ce qu’il rapporte, ni quand.',
            'Les produits des enchères arrivent plus tard ; les acquisitions foncières doivent '
            'être payées d’abord. Cet écart est rarement modélisé.',
            'Le plan de financement de la ligne et le plan de valorisation foncière sont établis '
            'par deux services différents, et les chiffres ne se recoupent pas.',
            'Les prix fonciers retenus sont optimistes. Quand l’enchère réelle se révèle en deçà, '
            'le projet s’est déjà engagé sur un calendrier.',
        ],
        can_cu=[
            ('Luật Đường sắt (texte consolidé 75/VBHN-VPQH) — article 25, alinéa 2',
             'Le Conseil populaire provincial peut décider d’affecter des crédits du budget local '
             'à un projet d’investissement public distinct réalisant l’indemnisation, l’aide et la '
             'réinstallation prévues au plan du périmètre TOD, afin de constituer des terrains à '
             'mettre aux enchères.'),
            ('Luật Đường sắt — article 25, alinéa 3',
             'Sur les produits de la valorisation du foncier en périmètre TOD : pour le réseau '
             'national, après déduction des frais d’indemnisation et frais annexes, la province '
             'conserve 50 % et reverse 50 % au budget central. Pour les lignes locales, la '
             'province conserve 100 %.'),
            ('Luật Đường sắt — article 3, alinéas 6 et 7',
             'Définitions du périmètre TOD et du projet ferroviaire local suivant le modèle TOD. '
             'C’est le classement correct qui détermine la part applicable.'),
        ],
        lam_gi=[
            ('Déterminer le type de projet et la part conservée',
             'Réseau national ou ligne locale détermine si la part est de 50 % ou de 100 %. C’est '
             'la première question, car elle change tous les chiffres suivants.'),
            ('Établir l’état du foncier par périmètre TOD',
             'Surface, situation actuelle, indices d’urbanisme après ajustement, et date prévue à '
             'laquelle chaque parcelle devient cessible aux enchères.'),
            ('Modéliser les flux dans les deux sens',
             'Sorties : indemnisation, aide, réinstallation et coût de leur mise en œuvre. '
             'Entrées : produits des enchères par tranche. L’écart entre les deux est ce que le '
             'budget local doit porter entre-temps.'),
            ('Passer les sensibilités',
             'Prix fonciers en baisse de 10 à 30 %, calendrier d’enchères décalé d’un à trois ans, '
             'part de parcelles vendues plus faible. Le résultat montre ce que le plan peut '
             'absorber.'),
            ('Rédiger la note explicative',
             'Dans la langue d’un dossier de présentation, en citant précisément les dispositions, '
             'afin que l’examinateur puisse vérifier chaque chiffre.'),
        ],
        dau_ra=[
            'Un état du foncier TOD par périmètre, avec les dates prévues',
            'Un modèle de flux fonciers que vous pouvez ouvrir et modifier — pas une boîte noire',
            'Des tableaux de sensibilité au prix foncier et au calendrier',
            'Une note explicative sur le retour de capital, entièrement référencée',
        ],
        khi_nao='Lors de l’élaboration de l’étude préalable ou de faisabilité d’une ligne '
                'comportant un volet TOD ; lorsque le Conseil populaire provincial s’apprête à '
                'délibérer sur l’emploi de crédits locaux pour constituer des terrains à mettre '
                'aux enchères ; ou lorsqu’un plan de financement a été renvoyé faute d’un volet '
                'retour convaincant.',
    ),
    'phuong-an-tai-chinh': dict(
        td='Plan de financement d’une ligne ferroviaire urbaine',
        mt='Un plan de financement sur toute la durée de vie : investissement, subvention '
           'd’exploitation, recettes TOD, charge annuelle du budget provincial.',
        ten='Conseil sur le plan de financement de la ligne et de son projet TOD sur toute sa '
            'durée de vie',
        lede='Une ligne ferroviaire urbaine ne s’arrête pas le jour de l’inauguration. Suivent '
             'deux à trois décennies d’exploitation, d’entretien, de renouvellement des '
             'équipements et de subvention. Un plan de financement qui s’arrête à l’achèvement des '
             'travaux laisse de côté la moitié de la durée de vie.',
        van_de=[
            'L’investissement est chiffré avec soin, tandis que les coûts d’exploitation et '
            'd’entretien sur la durée de vie sont estimés grossièrement.',
            'La subvention au transport public de voyageurs n’est pas reportée dans l’équilibre '
            'budgétaire provincial à long terme.',
            'Le renouvellement lourd des équipements entre les années 15 et 20 n’apparaît nulle '
            'part au dossier.',
            'Les recettes hors billettique — publicité, commerces en station, valorisation '
            'foncière — sont absentes du modèle.',
        ],
        can_cu=[
            ('Luật Đường sắt — article 5, alinéas 1 et 2',
             'L’État accorde la priorité aux crédits d’investissement, de modernisation et '
             'd’entretien, et subventionne le transport public de voyageurs par voie ferrée '
             'urbaine.'),
            ('Luật Đường sắt — article 32, alinéas 3 et 4',
             'À défaut de système national de normes et de prix unitaires pour l’exploitation et '
             'l’entretien, ou s’il ne convient pas, des normes publiées par des organismes '
             'nationaux ou étrangers peuvent être employées. Les coûts de marche à blanc, de '
             'formation et de transfert de technologie entrent dans le montant total '
             'd’investissement.'),
            ('Nghị định 206/2026/NĐ-CP',
             'Maîtrise des coûts d’investissement — montant total, estimations, coûts par marché, '
             'et coûts d’exploitation et d’entretien.'),
        ],
        lam_gi=[
            ('Poser le cadre des flux sur la durée de vie',
             'Phase d’investissement, exploitation en régime établi et jalons de renouvellement '
             'lourd.'),
            ('Séparer les natures de recettes',
             'Recettes tarifaires, subvention, recettes hors billettique et, le cas échéant, '
             'produits fonciers TOD.'),
            ('Arrêter les coûts d’exploitation et d’entretien',
             'Normes nationales lorsqu’elles existent ; à défaut, normes d’une ligne comparable, '
             'converties à la date d’évaluation au titre de l’article 32.'),
            ('Confronter au budget provincial',
             'Montrer ce que le budget doit fournir chaque année et quelle part cela représente '
             'dans les dépenses locales d’investissement.'),
            ('Passer les sensibilités et trouver les points de rupture',
             'Fréquentation inférieure aux prévisions, hausse du prix de l’électricité, variation '
             'de change sur les marchés en devises.'),
        ],
        dau_ra=[
            'Un modèle financier sur la durée de vie, hypothèses isolées dans un onglet distinct',
            'Un état année par année de la charge pesant sur le budget provincial',
            'Une analyse de sensibilité et les points de rupture du plan',
            'Une note explicative structurée pour le dossier de présentation',
        ],
        khi_nao='Lors de l’élaboration ou de l’examen d’une étude préalable ou de faisabilité ; '
                'lors de la révision de l’orientation d’investissement ; ou lorsqu’une ligne '
                'approche de la mise en service et que la province doit savoir ce qu’il lui faudra '
                'inscrire chaque année.',
    ),
    'co-cau-nguon-von': dict(
        td='Structure de financement d’un projet ferroviaire',
        mt='Comparer et combiner budget, ODA, capitaux privés et PPP : qui porte quel risque et ce '
           'que chaque source coûte réellement.',
        ten='Conseil sur la structure de financement d’un projet ferroviaire urbain',
        lede='Chaque source de financement porte ses propres contraintes — de procédure, de rythme '
             'de décaissement, d’origine des fournitures, de partage du risque de change. Un '
             'mauvais montage ne prive pas le projet d’argent ; il l’immobilise simplement.',
        van_de=[
            'L’ODA paraît bon marché au taux affiché, mais les conditions sur les entreprises et '
            'l’origine des équipements en relèvent le coût réel.',
            'Le risque de change d’un prêt en devises courant sur vingt ou trente ans n’est pas '
            'chiffré.',
            'La contrepartie nationale n’est pas mise en place à temps, ce qui bloque le '
            'décaissement du prêt lui-même.',
            'On ne sait pas quelles parties conviennent à un investisseur privé et lesquelles '
            'l’État doit conserver.',
        ],
        can_cu=[
            ('Luật Đường sắt — article 24',
             'Pour les projets ferroviaires relevant du droit de l’investissement ou du droit des '
             'PPP, l’État garantit sur le budget public la totalité des coûts d’indemnisation, '
             'd’aide et de réinstallation, et ce travail est isolé en un projet distinct.'),
            ('Luật Đường sắt — article 23',
             'Un projet composant d’indemnisation, d’aide et de réinstallation est géré comme un '
             'projet autonome et n’a pas à satisfaire l’exigence d’exploitation indépendante que '
             'le droit de la construction impose par ailleurs.'),
            ('Luật Đường sắt — article 5, alinéas 2 et 4',
             'Rétrocession de prêts et crédits préférentiels ; ainsi que le classement de '
             'l’exploitation d’infrastructures ferroviaires, du transport ferroviaire, de '
             'l’industrie ferroviaire et de la formation des personnels parmi les secteurs '
             'bénéficiant d’incitations à l’investissement.'),
        ],
        lam_gi=[
            ('Recenser les sources disponibles et leurs exigences',
             'Pour chacune : taux, durée, différé, conditions de passation, procédure de '
             'décaissement.'),
            ('Les ramener à une base de comparaison unique',
             'Calculer le coût réel du capital une fois intégrées les conditions de passation et '
             'le coût de procédure — non le taux affiché.'),
            ('Cartographier les risques',
             'Change, décaissement, calendrier de libération des emprises — qui porte quoi, et par '
             'quel mécanisme contractuel.'),
            ('Proposer un montage assorti d’une solution de repli',
             'Y compris le déclencheur : si la source A prend plus d’un certain retard, quelle '
             'voie prend le relais.'),
        ],
        dau_ra=[
            'Une comparaison des sources de financement sur une base unique',
            'Une cartographie de la répartition des risques entre les parties',
            'Une proposition de structure assortie de scénarios de repli',
        ],
        khi_nao='Lors de la constitution du dossier d’orientation d’investissement ; lorsqu’il est '
                'envisagé de basculer une partie de la ligne en PPP ; ou lorsque la source '
                'actuelle rencontre des difficultés de décaissement.',
    ),
    'suat-von-dau-tu': dict(
        td='Ratios d’investissement et conversion de normes étrangères',
        mt='Choisir des projets comparables et convertir ratios et normes étrangers à la date '
           'd’évaluation, avec une justification qui tient devant l’examinateur.',
        ten='Conseil sur les ratios d’investissement et la conversion de normes étrangères',
        lede='Le système vietnamien de normes de construction ne couvre pas encore tous les '
             'éléments d’un transport ferroviaire urbain. La loi autorise déjà le recours à des '
             'normes et ratios étrangers. Mais être autorisé est une chose ; justifier son choix '
             'devant l’autorité d’examen en est une autre — et c’est là que les dossiers sont le '
             'plus souvent renvoyés.',
        van_de=[
            'Il n’existe aucune norme nationale pour le creusement de tunnel, le matériel roulant, '
            'la signalisation ou le contrôle des trains.',
            'Des chiffres sont repris d’un projet étranger sans aucun raisonnement expliquant en '
            'quoi ce projet est « comparable ».',
            'La conversion à la date d’évaluation est faite grossièrement, sans distinguer '
            'l’actualisation, le change et les différences de conditions d’exécution.',
            'À chaque révision du projet, le travail recommence, faute d’avoir conservé les '
            'données sources.',
        ],
        can_cu=[
            ('Luật Đường sắt — article 32, alinéa 1',
             'Pour les postes qui ne conviennent pas, ou ne figurent pas, dans le système officiel '
             'de normes, de prix de construction et de ratios d’investissement, un projet '
             'ferroviaire peut employer des systèmes publiés par des organismes nationaux ou '
             'étrangers pour des postes ou des projets ferroviaires comparables, convertis à la '
             'date d’évaluation.'),
            ('Luật Đường sắt — article 32, alinéas 2 et 5',
             'Si cela demeure impossible, les ratios d’investissement d’un projet comparable '
             'ailleurs dans le monde peuvent être retenus. Les postes de coût que le droit '
             'vietnamien ne prévoit pas encore peuvent suivre un projet ferroviaire étranger '
             'comparable.'),
            ('Nghị định 206/2026/NĐ-CP — article 16',
             'Examen et contrôle des estimations — ce que l’examinateur regardera.'),
        ],
        lam_gi=[
            ('Repérer les postes dépourvus de norme nationale',
             'Confronter la décomposition des ouvrages au système de normes en vigueur et lister '
             'les manques.'),
            ('Choisir les projets comparables et établir la comparabilité',
             'Par écartement, type de ligne, part de souterrain et d’aérien, conditions de sol et '
             'degré d’automatisation. Ce raisonnement compte autant que les chiffres.'),
            ('Convertir à la date d’évaluation',
             'En séparant trois couches : l’actualisation dans le temps, l’écart de niveau de prix '
             'entre les deux pays, et les différences de conditions d’exécution et de normes '
             'applicables.'),
            ('Conserver les données sources',
             'Éditeur, date de publication, taux de change retenu, indice de prix retenu — pour '
             'que la révision suivante ne reparte pas de zéro.'),
            ('Rédiger la note de méthode',
             'Assez détaillée pour que l’examinateur suive chaque étape du calcul.'),
        ],
        dau_ra=[
            'Une liste des postes sans norme nationale',
            'Le dossier de choix des projets comparables et son raisonnement',
            'Un tableau de conversion à trois couches vers la date d’évaluation',
            'Le jeu de données sources conservé pour les révisions futures',
        ],
        khi_nao='Lors de l’établissement ou de la révision du montant total d’investissement ; '
                'lors de l’estimation de marchés portant sur des ouvrages spécialisés ; ou '
                'lorsque l’autorité d’examen vous a demandé de justifier vos prix unitaires.',
    ),
    'kiem-soat-noi-bo': dict(
        td='Contrôle interne d’une unité de gestion de projet',
        mt='Règles de dépense, séparation des tâches et points de contrôle entre métré et '
           'paiement, conçus à rebours de ce que le décompte exigera.',
        ten='Conseil sur le contrôle interne de l’unité de gestion de projet',
        lede='La plupart des erreurs relevées au décompte n’y ont pas été mises volontairement. '
             'Elles s’y trouvent parce que, au fil d’années d’exécution, personne n’a été chargé '
             'de vérifier. Un contrôle interne bien bâti au départ coûte bien moins cher que d’en '
             'assumer les conséquences huit ans plus tard.',
        van_de=[
            'La même personne atteste les quantités et approuve le paiement, sans contrôle '
            'intermédiaire.',
            'Des règles de dépense internes existent, mais n’ont jamais été confrontées au droit '
            'de la maîtrise des coûts.',
            'Les modifications sont approuvées oralement d’abord et documentées ensuite, laissant '
            'un fondement insuffisant au décompte.',
            'Les agents se succèdent sur plusieurs mandats, chacun travaillant à sa façon, sans '
            'référentiel commun.',
        ],
        can_cu=[
            ('Nghị định 206/2026/NĐ-CP',
             'Maîtrise des coûts d’investissement : compétence d’approbation des estimations, des '
             'coûts par marché et des révisions — fondement pour fixer les seuils d’approbation '
             'dans les règles internes.'),
            ('Nghị định 207/2026/NĐ-CP',
             'Maîtrise de la qualité et de l’entretien — fondement des points de contrôle à la '
             'réception.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Décompte final du capital investi. Savoir ce que le décompte exigera est ce qui '
             'permet de concevoir les contrôles en conséquence dès le départ.'),
        ],
        lam_gi=[
            ('Cartographier le circuit actuel',
             'De la demande de paiement à la sortie des fonds du Trésor : par qui elle passe, qui '
             'signe quoi.'),
            ('Identifier les manques',
             'Là où une personne cumule deux rôles ; là où personne ne rapproche ; là où les '
             'pièces suivent l’argent au lieu de le précéder.'),
            ('Redéfinir les points de contrôle',
             'Séparer l’attestation de l’autorisation de paiement ; fixer des seuils par niveau ; '
             'définir les pièces minimales par nature de dépense.'),
            ('Rédiger les règles et les formulaires',
             'Règles de dépense internes, procédure de contrôle du métré au paiement, et les '
             'formulaires correspondants.'),
            ('Former et expérimenter',
             'Passer plusieurs dossiers réels, corriger ce qui ne tient pas, puis publier '
             'formellement.'),
        ],
        dau_ra=[
            'Le circuit actuel et le circuit proposé, mis en regard',
            'Une liste des failles de contrôle assortie d’une cotation du risque',
            'Un projet de règles de dépense internes et de procédure de contrôle',
            'Un jeu de formulaires immédiatement utilisable',
        ],
        khi_nao='Lorsqu’une unité de gestion vient d’être créée ; lorsqu’une ligne entre en phase '
                'de chantier avec de gros volumes de paiement ; ou après qu’une inspection ou un '
                'audit a formulé des constats sur le contrôle.',
    ),
    'ho-so-quyet-toan': dict(
        td='Gestion des pièces de décompte dès le premier jour',
        mt='Règles de production, de codification, de conservation et de remise des pièces dès le '
           'premier marché, pour un projet de huit à douze ans.',
        ten='Conseil sur la gestion des pièces de décompte dès le premier jour du projet',
        lede='Une ligne de métro court sur huit à douze ans. L’entreprise du premier marché peut '
             'avoir été liquidée avant que la ligne ne transporte son premier voyageur. '
             'L’ingénieur qui a signé un procès-verbal de réception la deuxième année peut être à '
             'la retraite. Les pièces que l’on ne recueille pas au bon moment ne se recueillent '
             'pas plus tard — non parce que quelqu’un les dissimule, mais parce qu’elles n’existent '
             'plus.',
        van_de=[
            'Les pièces relatives aux ouvrages souterrains et cachés sont recouvertes ; rien '
            'd’autre ne permet de les vérifier après coup.',
            'Les entreprises des premières années sont dissoutes ou changent de mains, et plus '
            'personne ne peut confirmer les quantités.',
            'Les pièces sont dispersées entre plusieurs services sans référence commune, et les '
            'manques n’apparaissent qu’à la rédaction du rapport de décompte.',
            'Plans de récolement et procès-verbaux de réception ne concordent pas, et on s’en '
            'aperçoit bien trop tard pour corriger.',
        ],
        can_cu=[
            ('Nghị định 193/2026/NĐ-CP',
             'Décompte final du capital investi — liste des pièces et contenu du rapport. '
             'Connaître la destination permet de tracer le chemin.'),
            ('Nghị định 207/2026/NĐ-CP',
             'Maîtrise de la qualité et de l’entretien — procès-verbaux de réception et dossier '
             'des ouvrages exécutés.'),
            ('Luật Đường sắt — article 23',
             'Les projets composants sont gérés chacun comme un projet autonome ; les pièces '
             'doivent donc pouvoir être closes composant par composant.'),
        ],
        lam_gi=[
            ('Établir la liste cible des pièces',
             'À rebours de ce qu’exige le rapport de décompte : quelle phase doit produire quel '
             'document.'),
            ('Fixer une codification commune',
             'Une référence par projet composant, par marché et par ouvrage, afin que tous les '
             'services emploient le même nom.'),
            ('Arrêter des points de collecte obligatoires',
             'Adossés aux jalons de réception et de paiement, pour que les pièces ne suivent '
             'jamais l’argent — en particulier pour les ouvrages souterrains et cachés.'),
            ('Concevoir la conservation et la sauvegarde',
             'Papier et électronique, où elles se trouvent, qui les détient, où elles sont '
             'sauvegardées et pour combien de temps.'),
            ('Programmer un auto-contrôle trimestriel',
             'Passer en revue chaque trimestre ce qui manque, et l’exiger tant qu’il est encore '
             'possible de l’obtenir.'),
        ],
        dau_ra=[
            'Une liste des pièces de décompte par phase du projet',
            'Une règle commune de codification et de nommage',
            'Des procédures de collecte, de conservation, de sauvegarde et de remise',
            'Une fiche d’auto-contrôle trimestriel',
        ],
        khi_nao='Idéalement avant la signature du premier marché. Plus tard reste faisable, mais '
                'doit s’accompagner d’une revue rétrospective pour reconstituer ce qui est déjà '
                'perdu.',
    ),
    'tai-co-cau-doanh-nghiep': dict(
        td='Réorganisation des sociétés de projet et d’exploitation',
        mt='Conseil sur la réorganisation au passage du chantier à l’exploitation : remise des '
           'actifs, structure de l’exploitant et mécanisme de subvention.',
        ten='Conseil sur la réorganisation de la société de projet et de l’exploitant',
        lede='Le jour où une ligne transporte son premier voyageur est le jour où une organisation '
             'doit changer de nature : d’un organisme qui pilote un investissement à un organisme '
             'qui exploite un chemin de fer. Les deux exigent des personnes, des procédures et un '
             'mécanisme financier différents. Un changement trop tardif, et la ligne roule pendant '
             'que les comptes ne suivent pas.',
        van_de=[
            'Les actifs constitués par l’investissement ne sont pas comptabilisés complètement et '
            'correctement avant la remise à l’exploitant.',
            'On ignore sur quel fondement l’exploitant reçoit les actifs et comment il les '
            'enregistre.',
            'Le mécanisme de subvention n’a pas de formule arrêtée et se renégocie chaque année.',
            'L’unité de gestion a encore des travaux de décompte en cours alors que ses agents '
            'sont déjà passés à l’exploitation.',
        ],
        can_cu=[
            ('Luật Đường sắt — article 5, alinéa 2, point c',
             'L’État subventionne le transport public de voyageurs par voie ferrée urbaine.'),
            ('Luật Kiểm toán độc lập — article 40, alinéa 2, point b',
             'Une société d’audit peut enregistrer et fournir des prestations de conseil en '
             'gestion, en transformation et en restructuration d’entreprise.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Valeur des actifs constitués par l’investissement et leur remise — cela doit être '
             'clos avant le transfert à l’exploitant.'),
        ],
        lam_gi=[
            ('Examiner l’actif et le passif avant transfert',
             'Si les pièces relatives aux actifs sont complètes, quelles dettes subsistent envers '
             'les entreprises, et qui les reprend.'),
            ('Concevoir l’exploitant',
             'Missions, organisation, effectifs, et les travaux de décompte qui restent à l’unité '
             'de gestion.'),
            ('Bâtir le mécanisme financier de l’exploitation',
             'Formule de subvention, mécanisme de révision et indicateurs d’appréciation de la '
             'performance.'),
            ('Fixer une feuille de route de transfert par jalons',
             'Ce qui doit être achevé avant le début de l’exploitation commerciale et ce qui peut '
             'suivre.'),
        ],
        dau_ra=[
            'Un rapport d’examen de l’actif et du passif avant transfert',
            'Un projet d’organisation de l’exploitant',
            'Une proposition de mécanisme financier et de formule de subvention',
            'Une feuille de route de transfert assortie de dates',
        ],
        khi_nao='Douze à dix-huit mois avant le début prévu de l’exploitation commerciale ; ou '
                'lorsque la province s’apprête à créer ou réorganiser son exploitant ferroviaire '
                'urbain.',
    ),
    'thue-du-an': dict(
        td='Conseil fiscal pour un projet ferroviaire urbain',
        mt='Retenue à la source sur les contractants étrangers, traitement TVA des parts ODA et '
           'incitations que la Luật Đường sắt accorde déjà.',
        ten='Conseil fiscal pour un projet ferroviaire urbain',
        lede='Un transport ferroviaire urbain importe la quasi-totalité de sa technologie de '
             'cœur : matériel roulant, signalisation, contrôle des trains, ainsi que les '
             'spécialistes étrangers qui les accompagnent. Chacun de ces marchés soulève une '
             'question de retenue à la source sur les contractants étrangers, et les erreurs ne '
             'se révèlent en général qu’au contrôle fiscal — quand l’argent est déjà versé.',
        van_de=[
            'Un marché global couvrant équipements, montage, formation et transfert de technologie '
            'ne sépare pas la valeur de chaque part, si bien qu’un mauvais taux de retenue est '
            'appliqué.',
            'La partie qui supporte la retenue n’est pas arrêtée, et le manque apparaît au '
            'décompte.',
            'Le traitement TVA de la part financée par ODA est appliqué de façon inégale d’un '
            'marché à l’autre.',
            'Les incitations à l’investissement que la loi accorde déjà au secteur ferroviaire ne '
            'sont pas pleinement utilisées.',
        ],
        can_cu=[
            ('Luật Đường sắt — article 5, alinéa 4',
             'L’exploitation d’infrastructures ferroviaires, le transport ferroviaire, l’industrie '
             'ferroviaire et la formation des personnels ferroviaires sont des secteurs '
             'bénéficiant d’incitations à l’investissement.'),
            ('Luật Đường sắt — article 32, alinéa 4',
             'Les coûts de marche à blanc, de formation et de transfert de technologie entrent '
             'dans le montant total d’investissement — la manière de les séparer touche '
             'directement à la position fiscale.'),
            ('Luật Kiểm toán độc lập — article 40, alinéa 2, point a',
             'Une société d’audit peut enregistrer et fournir des prestations de conseil '
             'économique, financier et fiscal.'),
        ],
        lam_gi=[
            ('Examiner le marché avant signature',
             'Séparer la valeur de chaque composante, arrêter son traitement fiscal et préciser '
             'quelle partie supporte l’impôt.'),
            ('Arrêter la position de retenue à la source',
             'Par activité : fourniture de biens, prestations de montage, formation, transfert de '
             'technologie.'),
            ('Fixer le traitement TVA par source de financement',
             'Appliqué de façon homogène à tous les marchés du projet.'),
            ('Passer en revue les incitations',
             'Au regard des conditions d’éligibilité et des pièces nécessaires pour les faire '
             'valoir.'),
            ('Préparer le dossier explicatif',
             'Constitué à l’avance pour le moment où l’administration fiscale examinera la '
             'position.'),
        ],
        dau_ra=[
            'Un examen des clauses fiscales du marché, assorti de propositions de modification',
            'Un état de la retenue à la source par composante',
            'Des consignes TVA homogènes pour tout le projet',
            'Un dossier explicatif à destination de l’administration fiscale',
        ],
        khi_nao='Avant de signer avec un contractant étranger — c’est le seul moment où les '
                'clauses peuvent encore être modifiées. Après signature, on ne peut plus que gérer '
                'les conséquences.',
    ),
    'boi-duong-can-bo': dict(
        td='Formation des agents d’une unité de gestion de projet',
        mt='Une formation bâtie sur les propres dossiers de l’unité : décompte, maîtrise des '
           'coûts, pièces de paiement et préparation à un audit.',
        ten='Formation en finance, comptabilité et audit pour les agents de l’unité de gestion',
        lede='La plupart des agents d’une unité de gestion viennent de la technique. Ils lisent '
             'mieux les plans que les textes sur le décompte. Cet écart explique une bonne part '
             'des dossiers à refaire — et il se comble par une formation adaptée, sans que '
             'personne ait à reprendre des études.',
        van_de=[
            'Les dossiers de paiement sont renvoyés à répétition pour pièces manquantes, au prix '
            'du temps des deux parties.',
            'Les agents ignorent à l’avance ce qu’un audit demandera et se préparent donc en '
            'réaction.',
            'Chacun travaille à sa façon, faute de référentiel commun dans l’unité.',
            'Les nouveaux arrivants n’ont aucun support et apprennent de bouche à oreille.',
        ],
        can_cu=[
            ('Luật Kiểm toán độc lập — article 40, alinéa 2, point e',
             'Une société d’audit peut enregistrer et dispenser des formations en finance, '
             'comptabilité et audit. Notre programme se tient strictement dans ces trois '
             'domaines.'),
            ('Nghị định 193/2026/NĐ-CP',
             'Décompte final du capital investi — le cœur du programme.'),
            ('Nghị định 206/2026/NĐ-CP', 'Maîtrise des coûts d’investissement.'),
        ],
        lam_gi=[
            ('Analyser d’abord le besoin',
             'Examiner les dossiers réels de l’unité pour voir où se situe la difficulté, puis '
             'concevoir le contenu. Nous n’arrivons pas avec un programme tout fait.'),
            ('Concevoir par public',
             'Agents techniques, agents comptables et encadrement demandent trois niveaux '
             'différents.'),
            ('Enseigner sur pièces réelles',
             'À partir des documents du projet lui-même, anonymisés, plutôt que d’exemples '
             'inventés.'),
            ('Donner et corriger des exercices d’application',
             'Les participants doivent savoir faire ensuite, non seulement avoir entendu.'),
            ('Remettre le kit d’auto-formation',
             'Afin que les agents arrivant plus tard puissent s’en servir.'),
        ],
        dau_ra=[
            'Un rapport d’analyse des besoins',
            'Le programme et les supports pédagogiques, remis à l’unité',
            'Les résultats d’évaluation de chaque participant',
            'Un kit d’auto-formation pour les nouveaux arrivants',
        ],
        khi_nao='Avant la période de pointe du décompte ; lorsque l’unité accueille plusieurs '
                'nouveaux agents ; ou après qu’un audit ou une inspection a formulé les mêmes '
                'constats à répétition.',
    ),
}
