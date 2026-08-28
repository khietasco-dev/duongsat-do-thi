# -*- coding: utf-8 -*-
"""Ban TIENG PHAP: trang KINH NGHIEM (Enseignements) va VUONG MAC (Difficultés fréquentes).

Ten van ban phap luat GIU NGUYEN so hieu tieng Viet.

🔴 Nhac lai bay don vi tien: "billion" tieng Phap = 10^12. Ty = "milliard".
   "plusieurs milliers de milliards de VND" = nhieu NGHIN TY dong. Dung.
"""

# =================================================================== KINH NGHIEM
KN = dict(
    td='Douze enseignements de la gestion de projets de métro',
    mt='Douze pratiques qui décident si un dossier de décompte tient, trois idées fausses '
       'coûteuses et une liste de contrôle à cinq moments du projet.',
    duong='Enseignements',
    h1='Douze enseignements tirés de la gestion de projet',
    lede='Aucun n’est difficile. Chacun est peu coûteux au bon moment et cher à réparer plus tard. '
         'Ils s’adressent à une unité de gestion qui entend voir son dossier de décompte tenir, '
         'sur une ligne qui courra huit à quinze ans.',
    h_bh='Douze enseignements',
    h_sl='Trois idées fausses coûteuses',
    h_kt='Une liste de contrôle à cinq moments',
    kt_lede='Ce n’est pas un formulaire de conformité. C’est la courte liste de ce qui, s’il '
            'manque à ce moment-là, ne se récupère plus ensuite.',
    h_bt='Appliquer cela à votre propre projet',
    bt='Si vous souhaitez en faire des procédures et des formulaires pour votre unité, c’est l’une '
       'des prestations que nous assurons — voir %s.',
    bt_lk='la gestion des pièces de décompte dès le premier jour',
)

KN_BH = [
    ('Construire la carte des textes applicables dans le temps — et la tenir à jour',
     'Dès l’approbation du projet, dresser un tableau : chaque jalon face aux textes en vigueur à '
     'ce moment-là. Ajouter une ligne chaque fois qu’un décret ou une circulaire en remplace un '
     'autre. Le tableau demande environ deux jours de constitution et dix minutes d’entretien. '
     'Sans lui, le décompte revient à le reconstituer pendant des mois à partir de la mémoire de '
     'ceux qui sont encore là.'),
    ('Verrouiller la forme de prix dès le dossier de consultation',
     'Une forme de prix par marché. Si un marché mêle plusieurs natures d’ouvrages, scinder '
     'l’annexe de prix par partie. Le plus important : la manière dont le règlement s’opère '
     'réellement doit correspondre à la forme de prix écrite. C’est l’enseignement le plus coûteux '
     'de cette liste — l’essentiel des discussions au contrôle porte précisément sur ce point.'),
    ('Établir les pièces au fil de l’eau, non en fin de période',
     'Signer les procès-verbaux de réception le jour de la réception. Dresser les plans de '
     'récolement dès l’ouvrage achevé. Tenir le journal de chantier chaque jour. Cela paraît '
     'évident et c’est la règle la plus souvent enfreinte — cause directe de la plupart des '
     'montants rejetés au décompte.'),
    ('Photographier et mesurer ce qui sera recouvert, tant que cela se voit',
     'Sur un métro, les ouvrages souterrains pèsent très lourd dans le coût et ne se mesurent plus '
     'après achèvement. Le ferraillage avant coulage, le soutènement avant revêtement — l’un et '
     'l’autre exigent des photographies horodatées et localisées, accompagnées d’un procès-verbal '
     'signé des parties. Une photographie sans heure ni lieu ne prouve à peu près rien.'),
    ('Rapprocher chaque année le capital versé avec l’organisme payeur',
     'L’étape la plus souvent omise — et celle qui révèle le plus d’écarts. La faire chaque année, '
     'avec un procès-verbal signé des deux parties. Un écart trouvé dans l’année se traite ; '
     'trouvé au bout de huit ans, il impose de remonter toute la chaîne des pièces.'),
    ('Faire approuver les normes des ouvrages spécialisés avant leur exécution',
     'Creusement mécanisé, montage de la signalisation, caténaire, essais intégrés — rien de tout '
     'cela ne figure au système général de normes de construction. Une norme nouvelle doit être '
     'établie et approuvée avant exécution. Exécuter d’abord et solliciter l’approbation ensuite, '
     'c’est retrouver cette dépense en suspens.'),
    ('Trancher à l’avance le traitement des coûts de marche à blanc',
     'Avant que la marche à blanc ne commence, obtenir l’approbation d’une pièce fixant le '
     'périmètre, la durée, la liste des coûts et la source de financement. Ouvrir un code de suivi '
     'distinct en comptabilité. Cela prend une semaine et épargne des mois au décompte.'),
    ('Répartir les frais de gestion de projet selon un principe, non au jugé',
     'Les coûts directement rattachables à un ouvrage lui sont affectés en totalité ; les charges '
     'communes se répartissent au prorata du capital. Établir l’état de répartition tôt et le '
     'tenir, plutôt que de s’asseoir pour ventiler au moment du décompte — surtout lorsque les '
     'actifs iront à plusieurs entités réceptrices.'),
    ('Recenser dès l’approbation les actifs que l’on compte constituer',
     'Ne pas attendre la remise pour réfléchir à qui reçoit quoi. Dresser le tableau tôt : '
     'ouvrage — nature de l’actif — entité réceptrice prévue — fondement juridique du transfert. '
     'Il sera révisé bien des fois, mais l’avoir dès le départ rend chaque révision légère.'),
    ('Traiter aussitôt les constats des inspections et de la Cour des comptes, et garder la trace',
     'Un projet long et important connaîtra presque certainement au moins une inspection ou un '
     'audit. Pour chaque constat : conserver la pièce, suivre chaque point dans un état, consigner '
     'ce qui a été fait et où se trouve la preuve. Au décompte, c’est cet état que l’on demande en '
     'premier.'),
    ('Garder ceux qui connaissent le dossier — et, à défaut, transmettre sur pièces',
     'Une durée de vie de dix à quinze ans excède la durée moyenne d’affectation d’un agent. À '
     'chaque changement de responsable, transmettre contre un bordereau de pièces, non en termes '
     'généraux. Le bordereau appartient à l’organisation, non à la personne.'),
    ('Numériser tôt et nommer selon une règle unique',
     'Les pièces papier des premières années pâlissent, se perdent, prennent l’humidité. Les '
     'numériser au fil de l’eau et les nommer selon une règle — marché, nature de pièce, date, '
     'numéro. Le coût de cette pratique est dérisoire au regard de celui d’une recherche, la '
     'onzième année, d’un procès-verbal de réception de la deuxième.'),
]

KN_SL = [
    ('Tenir le décompte pour l’affaire du comptable',
     'Le décompte final du capital investi est l’affaire de toute l’unité de gestion : le service '
     'technique détient les quantités et les procès-verbaux de réception, le service des marchés '
     'les clauses de prix, le service de la planification le montant total, la comptabilité les '
     'pièces. Tout confier à la comptabilité, c’est la réduire à consolider ce qu’on lui remet — '
     'et ce qu’on ne lui remet pas devient une lacune du dossier.'),
    ('Appliquer les textes d’aujourd’hui à des travaux exécutés il y a des années',
     'Une dépense née en 2022 relève de ce qui valait en 2022, non d’un texte de 2026. Un ouvrage '
     'réceptionné en 2023 prend la norme en vigueur en 2023. C’est une erreur de fondement, et '
     'l’autorité de contrôle est fondée à la rejeter.'),
    ('Invoquer le mécanisme spécial sans établir qu’il s’applique',
     'Le mécanisme spécial abrège certaines étapes — mais seulement là où le projet entre dans son '
     'champ et dans sa période d’effet. Le dossier doit en porter la preuve : que le projet relève '
     'du champ de NQ 188/2025, quelle part des travaux est née après l’entrée en vigueur de la '
     'résolution, quelle étape a été abrégée au titre de quelle disposition. Un renvoi général au '
     '« mécanisme spécial » sans citer de disposition ne suffit pas.'),
]

KN_KT = [
    ('Dès l’approbation du projet', [
        'La carte des textes applicables dans le temps — établie, avec une personne nommément '
        'chargée de la tenir',
        'Lequel des quatre régimes juridiques s’applique, avec la pièce qui l’établit',
        'Un état du montant total d’investissement par période — ouvert avant toute révision',
        'La liste des actifs que l’on compte constituer et de leurs entités réceptrices prévues',
        'Une règle de nommage des fichiers et une arborescence électronique — publiées par écrit',
    ]),
    ('Avant publication du dossier de consultation de chaque marché', [
        'La forme de prix arrêtée, une forme par nature d’ouvrage',
        'Les candidats tenus de produire une analyse de prix et un détail quantitatif de base en '
        'annexes au marché',
        'Un calendrier de transfert de technologie avec critères de réception et valeur affectée à '
        'chaque poste',
        'Les obligations de formation adossées aux jalons de réception, non payées d’avance au '
        'forfait',
        'La langue du marché, la responsabilité de la traduction et le taux de conversion pour les '
        'contractants étrangers',
    ]),
    ('Tout au long du chantier', [
        'Un registre de remise des emprises par point kilométrique et par date, signé des trois '
        'parties',
        'Les normes des ouvrages spécialisés approuvées avant exécution',
        'Photographies et métrés de ce qui sera recouvert — avec heure, lieu et procès-verbal',
        'Rapprochement annuel du capital versé avec l’organisme payeur',
        'Les états de répartition des frais de gestion et d’ingénierie — tenus régulièrement',
        'Toute prolongation de délai consignée dans un avenant, non dans la correspondance',
    ]),
    ('Avant la marche à blanc', [
        'Une pièce approuvant le périmètre, la durée, la liste des coûts et la source de '
        'financement',
        'Un code de suivi distinct pour les coûts de marche à blanc dans le système comptable',
        'Évaluation et certification de la sécurité du système — avec son estimation et son marché '
        'propres',
        'Le dossier de récolement des équipements, avec une version vietnamienne',
    ]),
    ('Avant la remise', [
        'La liste et la valeur des actifs à remettre, par entité réceptrice',
        'Les actifs classés en long ou court terme',
        'Les biens propres de l’unité de gestion : écritures rapprochées de l’inventaire physique, '
        'valeur résiduelle arrêtée',
        'Matériels excédentaires : écritures rapprochées de l’inventaire physique, avec un plan '
        'd’écoulement',
        'Créances et dettes imputées aux bonnes parties, avec une proposition de traitement',
    ]),
]

# =================================================================== VUONG MAC
VM = dict(
    td='Dix difficultés récurrentes des projets de métro',
    mt='Dix difficultés qui reviennent sur les projets ferroviaires urbains au Vietnam : ce qui se '
       'passe, pourquoi, quels textes s’appliquent et que faire.',
    duong='Difficultés fréquentes',
    h1='Dix difficultés récurrentes',
    lede='Chacune est présentée de la même façon : ce qui se passe réellement, pourquoi cela se '
         'produit, quels textes s’appliquent et ce que l’on peut faire. Ce sont des schémas '
         'récurrents, non le dossier d’un projet déterminé.',
    l_ht='Ce qui se passe', l_ng='Pourquoi cela se produit',
    l_cc='Textes applicables', l_xl='Que faire',
    h_bt='Si votre projet bute sur l’une d’elles',
    bt='Décrivez la situation sur la page %s. Indiquez où se situe le projet, sa source de '
       'financement et la date du fait — les textes s’appliquent selon la date de survenance.',
    bt_lk='conseil',
)

VM_DS = [
    ('Acquisitions foncières et réinstallation',
     'Les emprises sont remises par tronçons courts et discontinus. L’entreprise reçoit le tronçon '
     'A tandis que le B reste inachevé, matériel et personnel sont immobilisés, et suit une '
     'réclamation pour frais d’immobilisation et prolongation de délai.',
     'Un métro traverse des quartiers constitués, densément peuplés et densément équipés en '
     'réseaux. Le plan d’indemnisation repose sur le cadastre alors que la situation réelle du '
     'terrain a évolué. Des coûts approuvés à une date sont versés sur plusieurs années.',
     'Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · NĐ 226/2025 · '
     'Hanoï, en périmètre TOD : NQ 66/2026/NQ-HĐND article 11',
     'Tenez un registre de remise des emprises par point kilométrique et par date, signé des trois '
     'parties — c’est l’élément probant principal qui décide si les frais d’immobilisation sont '
     'seulement liquidables. Consignez chaque prolongation dans un avenant, non dans la '
     'correspondance. Rapprochez trimestriellement l’état des paiements des pièces réelles.'),
    ('Montant total d’investissement révisé à plusieurs reprises',
     'Le montant total est approuvé à un certain niveau ; quelques années plus tard, le coût réel '
     'le dépasse largement. Pendant que la révision attend son approbation, chantier et paiements '
     'se poursuivent. Au décompte, une part des travaux se révèle avoir dépassé le montant en '
     'vigueur au moment de leur exécution.',
     'Quatre causes se cumulent en général : un montant provisoire bâti sur des données de '
     'reconnaissance minces ; l’actualisation sur huit à quinze ans ; des modifications de '
     'conception, le sous-sol différant des prévisions ; et le coût des acquisitions foncières qui '
     'progresse avec les prix.',
     'Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (modifié par NĐ 275/2025) · NĐ 206/2026 sur la '
     'maîtrise des coûts · NĐ 19/2026 sur l’examen et le suivi des investissements',
     'Les dépenses proposées au décompte doivent tenir dans le montant total approuvé — le '
     'dépassement, faute de révision approuvée, est dépourvu de fondement pour figurer dans la '
     'valeur liquidée, même si les ouvrages sont construits et réceptionnés. Tenez un état du '
     'montant total par période et obtenez la révision avant d’exécuter le dépassement.'),
    ('Marchés EPC et contractants étrangers',
     'Un marché EPC est conclu selon une forme internationale, au forfait en devises, payable à '
     'jalons. Au décompte, le maître d’ouvrage ne dispose d’aucun détail quantitatif à confronter ; '
     'l’autorité de contrôle réclame une décomposition et l’entreprise la refuse, le marché étant '
     'forfaitaire.',
     'Pratique contractuelle internationale et droit national du décompte reposent sur deux '
     'logiques distinctes. Dans la forme internationale, le forfait transfère le risque de '
     'quantité à l’entreprise ; un dossier de décompte de fonds publics exige, lui, la preuve des '
     'quantités exécutées.',
     'NĐ 37/2015 modifié par NĐ 50/2021 (texte consolidé 07/VBHN-BXD) · '
     'Luật Xây dựng 135/2025/QH15 · Luật Đấu thầu 22/2023/QH15 · VBHN 34/VBHN-BXD · '
     'NĐ 04/2026 sur l’industrie ferroviaire',
     'Verrouillez la forme de prix dans le dossier de consultation ; si un marché EPC mêle '
     'plusieurs natures d’ouvrages, scindez l’annexe de prix par partie. Exigez l’analyse de prix '
     'et le détail quantitatif de base en annexes, même au forfait. Fixez la langue du marché, la '
     'responsabilité de la traduction et le taux de conversion.'),
    ('Coûts de marche à blanc avant l’exploitation commerciale',
     'La marche à blanc dure des mois, parfois plus d’un an. Électricité de traction, masse '
     'salariale d’exploitation, assurances et spécialistes étrangers sont engagés. Les ouvrages ne '
     'sont pas remis et ne produisent aucune recette. Est-ce de l’investissement ou de '
     'l’exploitation ?',
     'Sur un métro, la frontière entre la fin de l’investissement et le début de l’exploitation '
     'n’est pas un point mais un intervalle. La marche à blanc est à la fois une étape de '
     'réception et une activité d’exploitation. Le droit de la construction et celui des biens '
     'publics ne se raccordent pas précisément à cet endroit.',
     'NĐ 207/2026 et TT 32/2026/TT-BXD · TT 62/2026/TT-BXD norme métro · NĐ 16/2026 · '
     'NĐ 15/2025 sur les actifs d’infrastructure · TT 79/2026/TT-BTC',
     'Tranchez avant la marche à blanc, non après : obtenez l’approbation d’une pièce fixant le '
     'périmètre, la durée, la liste des coûts et la source de financement. Ouvrez un code de suivi '
     'distinct en comptabilité. Traitez le dossier de certification de sécurité comme un poste '
     'contractuel autonome, doté de sa propre estimation.'),
    ('Application de normes et référentiels techniques étrangers',
     'Conception et équipements suivent les normes du pays fournisseur de la technologie. À la '
     'réception et au décompte, l’autorité nationale réclame une comparaison avec les normes '
     'techniques vietnamiennes, et beaucoup de paramètres soit n’existent pas, soit se mesurent '
     'autrement.',
     'Le Vietnam ne dispose d’un référentiel technique propre au ferroviaire urbain de type métro '
     'que depuis TT 62/2026/TT-BXD du 30 juillet 2026. Les lignes engagées avant cette date ont dû '
     'emprunter des normes étrangères, et chaque ligne emploie la technologie d’un pays différent.',
     'Hanoï : NQ 40/2025/NQ-HĐND — noter que l’article 1, alinéa 2, énonce expressément que le '
     'ferroviaire urbain suit sa propre voie et NE suit PAS la procédure générale de cette '
     'résolution · TT 62/2026/TT-BXD · TT 44/2025/TT-BXD',
     'Établissez un tableau de correspondance des normes dès la conception et faites-le approuver, '
     'plutôt que de le laisser à l’état de document interne du bureau d’études. Pour les projets '
     'de Hanoï, n’invoquez pas NQ 40/2025 comme fondement pour le ferroviaire urbain — cette '
     'résolution l’exclut ; invoquez Luật Thủ đô 02/2026/QH16 et NQ 188/2025/QH15.'),
    ('Décompte d’un projet mené sur de longues années',
     'Le projet a traversé plusieurs générations de décrets sur la maîtrise des coûts, la gestion '
     'de projet et le décompte, ainsi que plusieurs séries de modifications des circulaires de '
     'normes. Ceux qui ont constitué le dossier sont partis ; les pièces anciennes sont en archive '
     'et certaines ont pâli.',
     'C’est simplement la nature d’un projet dont la durée de vie atteint huit à quinze ans. On ne '
     'peut l’éviter, seulement le gérer.',
     'Les filiations à connaître — gestion de projet : NĐ 59/2015 → NĐ 15/2021 → NĐ 175/2024 → '
     'NĐ 209/2026 et NĐ 210/2026. Maîtrise des coûts : NĐ 32/2015 → NĐ 68/2019 → NĐ 10/2021 → '
     'NĐ 206/2026. Décompte : TT 09/2016 → TT 10/2020 → NĐ 99/2021 → NĐ 254/2025',
     'La première tâche est de construire, pour ce projet, sa propre carte des textes applicables '
     'dans le temps, en rattachant chaque jalon à une génération. Une conclusion incapable de '
     'citer la référence de la bonne période ne tiendra pas. Rapprochez chaque année le capital '
     'versé avec l’organisme payeur, plutôt que d’attendre la fin.'),
    ('TOD et captation de la plus-value foncière',
     'La politique permet à la ville de capter une part de la hausse de valeur des terrains autour '
     'des stations pour compenser le coût de la ligne. En pratique, l’organisme chargé de la mise '
     'en œuvre ne parvient pas à établir combien doit être perçu.',
     'Le mécanisme est complet au niveau de la loi et de la résolution du Conseil populaire, mais '
     'le texte qui le chiffre manque au dernier étage. S’y ajoute un second décalage : le plan TOD '
     'doit être approuvé d’abord, or il suppose un tracé et des emplacements de stations arrêtés — '
     'alors que la ligne est encore en cours de reconception.',
     'Luật Thủ đô 02/2026/QH16 article 12 · NQ 188/2025/QH15 · Hanoï : NQ 71/2025, NQ 66/2026, '
     'NQ 67/2026 · Hô-Chi-Minh-Ville : NQ 21/2026 (remplaçant NQ 38/2025 à compter du 19 juin '
     '2026), NQ 90/2025',
     'Tracez dès le départ la frontière comptable entre le projet de ligne et le projet TOD. Pour '
     'Hanoï, surveillez le Journal officiel afin de saisir la résolution sur le coefficient '
     'd’avantage TOD dès sa parution — jusque-là, tout montant de recette TOD est une estimation '
     'interne et n’a pas sa place dans un plan de financement formel.'),
    ('Sous-sol',
     'Stations souterraines et sections en tunnel se trouvent sous des terrains détenus par de '
     'nombreux occupants différents. Jusqu’à quelle profondeur le terrain est-il repris, comment '
     'le tréfonds est-il indemnisé, quel est le loyer foncier d’un ouvrage souterrain, et dans '
     'quelle mesure la surface commerciale d’une station souterraine peut-elle être valorisée ?',
     'Le droit foncier traditionnel gère à la parcelle de surface. Le sous-sol constitue une '
     'nouvelle strate administrative, à peine posée par la Luật Thủ đô et les résolutions de 2026 '
     'du Conseil populaire de Hanoï.',
     'Luật Thủ đô 02/2026/QH16 article 11 · Hanoï : NQ 64/2026 (planification du sous-sol), '
     'NQ 65/2026 (redevances), NQ 62/2026 (incitations à l’investissement)',
     'Fixez et consignez la cote inférieure de chaque station et de chaque section de tunnel dans '
     'les dossiers de conception et de récolement — le seuil de quinze mètres commande directement '
     'l’obligation financière. Séparez la surface souterraine affectée à l’exploitation de celle '
     'valorisée commercialement : les deux relèvent de régimes financiers distincts.'),
    ('Formation du personnel d’exploitation',
     'Le coût de formation des conducteurs, des régulateurs et du personnel de maintenance entre '
     'dans le montant total d’investissement. Au décompte, la question se pose : cela crée-t-il un '
     'actif ? Sinon, comment le traiter ?',
     'La formation est économiquement un investissement, mais elle ne constitue comptablement '
     'aucune immobilisation. Les personnes formées peuvent partir avant l’ouverture, ce qui '
     'soulève la question de l’efficacité du capital engagé.',
     'NQ 188/2025/QH15, le groupe de mécanismes sur le transfert de technologie et la formation '
     'des personnels · QĐ 2230/QĐ-TTg, le plan des personnels ferroviaires à l’horizon 2035 · '
     'NĐ 254/2025',
     'Tranchez dès la phase de préparation : à quelle nature de dépense la formation se rattache, '
     'et si elle est imputable à la valeur des actifs. Si elle ne l’est pas, l’autorisation de '
     'l’autorité compétente est nécessaire — c’est une procédure distincte, que le maître '
     'd’ouvrage ne peut décider seul. Conservez les preuves au complet, car c’est une dépense sans '
     'produit matériel.'),
    ('Transfert de technologie et localisation',
     'Le marché comporte une clause de transfert de technologie, mais la décrit en termes '
     'généraux, sans calendrier précis, sans critères de réception et sans jalon de paiement '
     'distinct. Au décompte, nul ne peut établir si l’obligation a été exécutée, ni quelle part du '
     'prix elle représente.',
     'Le transfert de technologie est une obligation difficile à chiffrer. Le vendeur a intérêt à '
     'conserver le cœur. L’acheteur manque souvent, à la signature, de la capacité technique de '
     'définir précisément ce qu’il doit recevoir.',
     'NQ 188/2025/QH15 · NĐ 04/2026 sur la commande de prestations à l’industrie ferroviaire · '
     'QĐ 498/QĐ-TTg sur la réorganisation des Chemins de fer vietnamiens · '
     'Luật Chuyển giao công nghệ 07/2017/QH14',
     'Portez le calendrier de transfert en tableau dans le dossier de consultation : contenu — '
     'forme — critère de réception — échéance — valeur correspondante. Sans colonne de valeur, il '
     'ne peut être liquidé. Faites-en un poste de paiement distinct et retenez le dernier '
     'pourcentage jusqu’à réception de l’ensemble du calendrier.'),
]
