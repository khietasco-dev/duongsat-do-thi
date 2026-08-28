# -*- coding: utf-8 -*-
"""Ban TIENG PHAP: trang TU VAN (Conseil) va LIEN HE (Contact) + CHAN TRANG.

⚠ MUC FAQ "tra loi bang ngon ngu nao" — viet THAN TRONG y nhu ban Nhat va Duc:
  ASCO chua co bo cong cu ngon ngu Phap, nen chi hua tra loi CHINH THUC bang
  TIENG VIET hoac TIENG ANH; tieng Phap thi nhan cau hoi.
"""

# =================================================================== TU VAN
TV = dict(
    td='Demander conseil sur un projet ferroviaire urbain',
    mt='Décrivez ce qui bloque votre projet. Nous lisons, qualifions et répondons sous '
       '24 heures ouvrées — trois types de demandes, chacun avec son délai.',
    duong='Conseil',
    h1='Demander conseil',
    lede='Décrivez ce qui bloque le projet. Nous lisons, qualifions et répondons sous 24 heures '
         'ouvrées.',
    h_ba='Trois types de demandes que nous acceptons',
    ba=[
        ('Réponse rapide', 'Une question précise et unique',
         'Une question claire sur un fondement juridique, un ordre de procédure ou le traitement '
         'd’une dépense donnée. Ce type se règle en général dès la première réponse.',
         'Délai : <b>sous 24 heures ouvrées</b> · sans frais'),
        ('Pièces nécessaires', 'Un problème à plusieurs volets',
         'Une situation qui touche plusieurs textes, plusieurs dates, ou qui exige de lire '
         'ensemble le marché et les procès-verbaux de réception. Nous donnons d’abord une réponse '
         'provisoire, puis convenons d’un échange si nécessaire.',
         'Délai : <b>2 à 3 jours ouvrés</b> · un engagement de confidentialité peut être demandé'),
        ('Devient une mission', 'Revue de l’ensemble du dossier',
         'Revue du dossier complet avant présentation au décompte, ou reconstitution de la carte '
         'des textes applicables dans le temps pour un projet mené sur de longues années. Cela a '
         'son propre périmètre et son propre calendrier.',
         'Délai : <b>selon convention</b> · sur la base d’un contrat de prestation'),
    ],
    h_dv='Neuf prestations que nous pouvons prendre en charge',
    dv_lede='Au-delà des réponses aux questions, nous prenons en charge neuf chantiers autour du '
            'volet financier et de la gouvernance d’un projet ferroviaire urbain. Chaque fiche '
            'précise ce que nous faisons, sur quel fondement, et ce que vous recevez.',
    dv_ghi='Les neuf relèvent de l’article 40, alinéa 2, de la Luật Kiểm toán độc lập et doivent '
           'passer un contrôle d’indépendance avant signature — le détail figure sur la page %s.',
    dv_lk='Prestations',
    h_mau='Le formulaire',
    f_ten='Nom', f_cv='Fonction', f_dv='Organisme', f_dt='Téléphone', f_em='Courriel',
    f_db='Lieu du projet', f_gd='À quelle phase se trouve le projet',
    f_nh='Nature du problème',
    f_loai='Type de demande', f_mo='Décrivez la situation',
    f_chon='— Sélectionner —',
    f_mo_gy='Ce qui bloque le projet · ce qui a déjà été tenté · l’aide attendue · s’il y a un '
            'délai à tenir',
    f_gui='Envoyer la demande',
    f_bb='obligatoire',
    db=['Hanoï', 'Hô-Chi-Minh-Ville', 'Ailleurs'],
    gd=['Planification du tracé', 'Orientation d’investissement',
        'Préparation, examen et approbation', 'Acquisitions foncières',
        'Sélection des entreprises', 'Exécution des travaux', 'Réception et marche à blanc',
        'Remise et comptabilisation des actifs', 'Décompte final du capital investi'],
    nh=['Procédure d’investissement', 'Acquisitions foncières', 'Marché et paiement',
        'Réception et dossier de récolement', 'Décompte final du capital investi',
        'TOD et valorisation foncière', 'Sous-sol', 'Formation et transfert de technologie',
        'Autre'],
    loai=['Une question précise et unique', 'Un problème à plusieurs volets',
          'Revue de l’ensemble du dossier'],
    h_nen='Ce qu’il faut indiquer dans la description',
    nen=[
        'Où se situe le projet — Hanoï et Hô-Chi-Minh-Ville disposent d’un mécanisme propre, pas '
        'les autres territoires',
        'La source de financement : investissement public, ODA ou PPP',
        'La date du fait en cause — les textes s’appliquent selon la date de survenance',
        'S’il existe déjà une décision d’une autorité compétente sur ce point',
        'S’il y a un délai à tenir, par exemple une date de dépôt pour le contrôle',
    ],
    h_bm='Ce que deviennent vos informations',
    bm='Nous traitons comme confidentiel tout ce que vous nous adressez. Nous ne citons ni votre '
       'projet ni votre organisme dans aucun document public. Lorsqu’une question devient un '
       'enseignement général qui mérite publication, nous la réécrivons de sorte qu’aucun projet '
       'ne puisse être identifié.',
    h_kh='Ce à quoi nous ne pouvons pas répondre',
    kh='Nous ne délivrons pas de consultation juridique — une société d’audit n’est pas autorisée '
       'à fournir des prestations juridiques. Nous ne commentons pas le travail d’un autre '
       'auditeur ou conseil sur un projet que nous n’avons pas examiné. Et nous ne nous prononçons '
       'pas sur une question dont la réponse dépend de pièces que nous n’avons pas lues.',
)

# =================================================================== LIEN HE
LH = dict(
    td='Contacter ASCO — projets ferroviaires urbains',
    mt='Trois voies pour nous joindre : le formulaire de conseil, un appel ou un échange '
       'programmé. Chacune convient à un type de sujet.',
    duong='Contact',
    h1='Contact',
    lede='Trois voies pour nous joindre, chacune adaptée à un type de sujet. Choisir la bonne vous '
         'vaut une réponse plus rapide.',
    h_ba='Trois voies pour nous joindre',
    ba=[
        ('Convient à la plupart', 'Envoyer le formulaire de conseil',
         'Il nous donne assez de contexte pour répondre correctement ; la réponse est donc '
         'généralement utilisable telle quelle, au lieu d’ouvrir une série de questions.',
         'Réponse : <b>sous 24 heures ouvrées</b>', 'Ouvrir le formulaire de conseil →'),
        ('Urgent', 'Appelez-nous',
         'Convient à un sujet dont l’échéance tombe dans les prochains jours, ou à un point bref à '
         'trancher avant de décider.',
         'Horaires : <b>du lundi au vendredi, 8 h 00 – 17 h 30</b>', None),
        ('Complexe', 'Convenir d’un échange',
         'Lorsqu’un projet bute sur plusieurs points à la fois, un échange fait généralement plus '
         'qu’une longue correspondance. En visioconférence ou dans vos propres locaux.',
         'Durée : <b>60 à 90 minutes</b>', None),
    ],
    dt_ghi='Ce numéro fonctionne aussi sur <b>Zalo</b> — écrivez en dehors des horaires et nous le '
           'lisons dès le lendemain matin.',
    dl_ghi='Pour convenir d’une date, écrivez au <b>Zalo 08 2509 2007</b> ou remplissez le %s en '
           'choisissant comme type de demande <b>« Un problème à plusieurs volets »</b>.',
    dl_lk='formulaire de conseil',
    h_ts='Siège',
    ts_ten='ASCO — Société d’audit et d’évaluation',
    ts='Immeuble ASCO, n° 2, ruelle 308, rue Le Trong Tan, quartier Phuong Liet, Hanoï<br>'
       'Téléphone et Zalo : <b>08 2509 2007</b>',
    h_tt='La visioconférence convient aussi',
    tt='Avec les organismes hors de Hanoï, nous tenons la plupart des échanges à distance — c’est '
       'plus rapide et personne n’a à se déplacer. Nous envoyons le lien une fois la date fixée. '
       'Si vous préférez nous recevoir dans vos locaux, dites-le au moment de convenir de la date '
       'et nous organisons le déplacement.',
    h_chon='Quelle voie pour quel sujet',
    chon_cot=('Votre sujet', 'Voie', 'Pourquoi'),
    chon=[
        ('Une question unique sur un fondement juridique', 'Formulaire',
         'Une réponse écrite citant les références, que vous pouvez conserver'),
        ('La date de dépôt du contrôle approche et il faut trancher maintenant', 'Appel',
         'Pas d’attente liée à un échange de courriers'),
        ('Le projet bute sur plusieurs points et vous ne savez par où commencer', 'Rendez-vous',
         'Il faut une vue d’ensemble ; la correspondance n’y suffit pas'),
        ('Vous souhaitez une revue de tout le dossier avant le décompte',
         'Formulaire, troisième option',
         'Cela a son propre périmètre et doit être convenu au préalable'),
        ('Un retour sur le contenu de ce site', 'Formulaire',
         'Nous corrigeons et consignons l’origine de la remarque'),
    ],
    h_fa='Questions fréquentes avant de nous contacter',
    fa=[
        ('Y a-t-il des frais ?',
         'Non pour la réponse à un point précis. La lecture de pièces, ou la revue d’un dossier '
         'complet, est un travail au périmètre et au calendrier définis, que nous convenons '
         'ensemble avant de commencer.'),
        ('Je n’appartiens pas à une unité de gestion de projet — puis-je tout de même vous '
         'interroger ?',
         'Oui. Ce site s’adresse aux agents des unités de gestion, aux maîtres d’ouvrage, aux '
         'bureaux d’études et aux entreprises. Précisez votre rôle dans le projet afin que nous '
         'répondions sous le bon angle.'),
        ('Mon projet n’est pas ferroviaire urbain — est-ce gênant ?',
         'Une grande partie du contenu vaut pour tout projet d’investissement public, en '
         'particulier sur le décompte. Indiquez la nature du projet et nous vous dirons ce qui se '
         'transpose et ce qui ne se transpose pas.'),
        ('Dans quelle langue répondez-vous ?',
         'La réponse formelle est rendue en <b>vietnamien ou en anglais</b>. Nous acceptons les '
         'demandes en français, mais nous ne pouvons répondre du contenu que pour les versions '
         'vietnamienne et anglaise. Lorsque la réponse tient à la lettre d’un texte, nous joignons '
         'l’original vietnamien, seul à faire foi.'),
    ],
    h_bm='Confidentialité',
    bm='Nous traitons vos informations comme confidentielles et ne citons ni votre projet ni votre '
       'organisme dans aucun document public. Lorsqu’une question devient un enseignement général '
       'qui mérite publication, nous la réécrivons de sorte qu’aucun projet ne puisse être '
       'identifié.',
)

# =================================================================== CHAN TRANG
CHAN_FR = dict(
    gt='Un site de référence sur l’investissement, la gouvernance et le décompte final des projets '
       'ferroviaires urbains au Vietnam.',
    c1='Consulter', c2='Nous joindre', c3='À noter',
    m1=[('van-ban', 'Recherche de textes'), ('quy-trinh', 'Déroulement du projet'),
        ('kinh-nghiem', 'Enseignements de gestion')],
    m2=[('vuong-mac', 'Difficultés fréquentes'), ('tu-van', 'Demander conseil'),
        ('lien-he', 'Contact')],
    luu='Le contenu de ce site est indicatif et ne remplace pas un conseil sur un projet précis. '
        'Les textes changent souvent — vérifiez toujours sur l’original.',
    bq='Droits réservés — ASCO, Société d’audit et d’évaluation, Vietnam · Compilé à partir de '
       'notre fonds documentaire interne.',
    ngay='Textes à jour au %s.',
)
