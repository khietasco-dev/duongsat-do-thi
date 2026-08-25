# -*- coding: utf-8 -*-
"""Ban TIENG ANH cua 9 trang dich vu cap 2.

Nguyen tac: dich VAN CUA CHINH MINH. Phan "Legal basis" la dien giai cua ASCO,
KHONG phai ban dich chinh thuc cua dieu luat — moi trang deu ghi ro dieu do va
tro nguoi doc ve ban goc tieng Viet trong muc Tra cuu van ban.
"""

# --------------------------------------------------------------- khung trang
KHUNG = dict(
    duong_nha='Home', duong_dv='Services',
    h_vande='Common problems',
    h_cancu='Legal basis',
    cancu_nhac='The wording below is <b>our reading</b> of each provision, not an official '
               'translation. Only the Vietnamese text is authoritative — you can open every '
               'document in the %s section.',
    cancu_lk='Document lookup',
    h_lamgi='What we do',
    h_daura='What you receive',
    h_khinao='When to call us',
    luu_h='Two conditions, stated before anything else.',
    luu='First, this is a service under Clause 2, Article 40 of the Law on Independent Audit — '
        'an audit firm must register it with the Ministry of Finance before providing it. '
        'Second, if we audit your organisation, or expect to, this engagement must pass an '
        'independence check under Article 30 of the same law before signing. We run that check '
        'first, and if it fails we say so plainly and decline.',
    bt_h='Next step',
    bt='Describe your situation on the %s page, or call <b>0825092007</b>. We read it, classify '
       'it and reply within 24 working hours — including when the answer is that the work falls '
       'outside what we are permitted to do.',
    bt_lk='Request advice',
    bt_ve='← See all nine services',
)

# --------------------------------------------------------------- 9 dich vu
EN = {
    'thu-hoi-von-tod': dict(
        td='Capital recovery from TOD land — advisory',
        mt='A cash-flow model for TOD land under Article 25 of the Law on Railways: collection '
           'timing, the share the province keeps, and sensitivity testing.',
        ten='Advising on capital recovery from TOD land',
        lede='An urban railway almost never pays for itself out of fare revenue. The real source of '
             'recovery is the rise in land value around the stations — and the law now opens a route '
             'for the province to keep that value. The difficulty is turning a statutory mechanism '
             'into a cash flow you can put into a financial plan and defend before the appraising '
             'authority.',
        van_de=[
            'The mechanism for creating auction land exists, but nobody has quantified how much it '
            'brings in, or when.',
            'Auction proceeds arrive later; site clearance has to be paid for first. That gap is '
            'rarely modelled.',
            'The financial plan for the line and the land exploitation plan are drawn up by two '
            'different departments, and the numbers do not reconcile.',
            'Assumed land prices are optimistic. By the time the real auction falls short, the '
            'project has already committed to a schedule.',
        ],
        can_cu=[
            ('Law on Railways (consolidated text 75/VBHN-VPQH) — Article 25.2',
             'The provincial People’s Council may decide to use the local budget for a separate '
             'public investment project carrying out compensation, support and resettlement under '
             'the TOD area plan, in order to create land for auction.'),
            ('Law on Railways — Article 25.3',
             'Proceeds from exploiting land in a TOD area: for national railways, after deducting '
             'compensation and related costs, the province keeps 50% and remits 50% to the central '
             'budget. For local railways, the province keeps 100%.'),
            ('Law on Railways — Article 3.6 and 3.7',
             'Definitions of a TOD area and of a local railway project following the TOD model. '
             'Classifying the project correctly is what decides which share applies.'),
        ],
        lam_gi=[
            ('Establish the project type and the retained share',
             'National railway or local railway decides whether the share is 50% or 100%. This is '
             'the first question, because it changes every figure that follows.'),
            ('Build the land schedule for each TOD area',
             'Area, current status, planning indicators after adjustment, and the expected date each '
             'parcel becomes eligible for auction.'),
            ('Model the cash flow in both directions',
             'Outflow: compensation, support, resettlement and the cost of carrying them out. '
             'Inflow: auction proceeds by tranche. The gap between the two is what the local budget '
             'must carry in the meantime.'),
            ('Run the sensitivities',
             'Land price down 10–30%, auction schedule slipping one to three years, a lower share of '
             'parcels selling. The result shows how much the plan can absorb.'),
            ('Write the explanatory statement',
             'In the language of a submission file, citing the provisions precisely, so the '
             'appraiser can verify every figure.'),
        ],
        dau_ra=[
            'A TOD land schedule by area, with expected dates',
            'A land cash-flow model you can open and edit — not a black box',
            'Sensitivity tables for land price and timing',
            'An explanatory statement on capital recovery with full citations',
        ],
        khi_nao='When preparing the pre-feasibility or feasibility study for a line with a TOD '
                'component; when the provincial People’s Council is about to resolve on using '
                'the local budget to create auction land; or when an existing financial plan has '
                'been sent back because the recovery side is not convincing.',
    ),
    'phuong-an-tai-chinh': dict(
        td='Financial plan for an urban railway line',
        mt='A whole-life financial plan: capital cost, operating subsidy, TOD revenue, the annual '
           'call on the provincial budget, and sensitivity analysis.',
        ten='Advising on the whole-life financial plan for a line and its TOD project',
        lede='An urban railway line does not end on the day the ribbon is cut. After that come two '
             'or three decades of operation, maintenance, equipment renewal and subsidy. A financial '
             'plan that stops at completion of construction is a plan missing half its life.',
        van_de=[
            'Capital cost is worked out carefully, while whole-life operating and maintenance cost '
            'is estimated loosely.',
            'The subsidy for public passenger transport is not carried into the long-term provincial '
            'budget balance.',
            'Major equipment renewal in years 15 to 20 appears nowhere in the file.',
            'Non-fare revenue — advertising, retail at stations, land exploitation — is left out of '
            'the model.',
        ],
        can_cu=[
            ('Law on Railways — Article 5.1 and 5.2',
             'The State prioritises budget allocation for investment, upgrading and maintenance, and '
             'subsidises public passenger transport by urban railway.'),
            ('Law on Railways — Article 32.3 and 32.4',
             'Where the domestic system of norms and unit prices for operation and maintenance does '
             'not exist or does not fit, norms published by domestic or foreign organisations may be '
             'used. Trial running, training and technology transfer costs are included in total '
             'investment.'),
            ('Decree 206/2026/ND-CP',
             'Management of construction investment cost — total investment, construction estimates, '
             'package estimates, and operation and maintenance cost.'),
        ],
        lam_gi=[
            ('Set the whole-life cash-flow frame',
             'Investment phase, steady-state operation, and the major renewal milestones.'),
            ('Separate the revenue lines',
             'Fare revenue, subsidy, non-fare revenue, and TOD land proceeds where they apply.'),
            ('Establish operating and maintenance cost',
             'Domestic norms where they exist; otherwise norms from a comparable line, converted to '
             'the valuation date under Article 32.'),
            ('Test it against the provincial budget',
             'Show what the budget must provide each year, and what share that is of local '
             'development investment spending.'),
            ('Run sensitivities and find the breaking points',
             'Ridership below forecast, electricity prices rising, exchange-rate movement on '
             'foreign-currency contracts.'),
        ],
        dau_ra=[
            'A whole-life financial model with assumptions held in a separate sheet',
            'A year-by-year statement of the call on the provincial budget',
            'Sensitivity analysis and the plan’s breaking points',
            'An explanatory statement structured for the submission file',
        ],
        khi_nao='When preparing or appraising a pre-feasibility or feasibility study; when adjusting '
                'the investment policy decision; or when a line is approaching operation and the '
                'province needs to know what it must budget each year.',
    ),
    'co-cau-nguon-von': dict(
        td='Funding structure for an urban railway project',
        mt='Comparing and combining budget, ODA, private capital and PPP for a metro line: who '
           'carries which risk, and what each source really costs.',
        ten='Advising on the funding structure of an urban railway project',
        lede='Every funding source carries its own constraints — on procedure, on disbursement pace, '
             'on the origin of goods, on who bears currency risk. Choose the wrong structure and the '
             'project does not run short of money; it simply stops moving.',
        van_de=[
            'ODA looks cheap on the coupon, but conditions on contractors and equipment origin raise '
            'the real cost.',
            'Currency risk on a foreign-currency loan running twenty or thirty years is not '
            'quantified.',
            'Domestic counterpart funds are not provided on time, which stalls disbursement of the '
            'loan itself.',
            'It is unclear which parts are suitable for a private investor and which the State must '
            'keep.',
        ],
        can_cu=[
            ('Law on Railways — Article 24',
             'For railway projects under the investment law or the public-private partnership law, '
             'the State guarantees the entire cost of compensation, support and resettlement from '
             'the State budget, and that work is separated into its own project.'),
            ('Law on Railways — Article 23',
             'A compensation, support and resettlement component project is managed as an '
             'independent project and need not meet the requirement of independent operation that '
             'construction law otherwise imposes.'),
            ('Law on Railways — Article 5.2 and 5.4',
             'On-lending and preferential credit support; and the treatment of railway '
             'infrastructure business, railway transport, railway industry and railway workforce '
             'training as investment-incentivised sectors.'),
        ],
        lam_gi=[
            ('List the available sources and what each requires',
             'For each: interest, tenor, grace period, procurement conditions, disbursement '
             'procedure.'),
            ('Bring them onto one basis of comparison',
             'Compute the true cost of capital after procurement conditions and procedural cost — '
             'not the headline rate.'),
            ('Map the risks',
             'Currency, disbursement, site clearance schedule — who carries each, and through which '
             'contractual mechanism.'),
            ('Propose a structure with a fallback',
             'Including the trigger: if source A slips by more than a stated period, which route '
             'takes over.'),
        ],
        dau_ra=[
            'A comparison of funding sources on a single basis',
            'A risk allocation map across the parties',
            'A proposed funding structure with fallback scenarios',
        ],
        khi_nao='When preparing the investment policy file; when considering moving part of a line '
                'to a public-private partnership; or when the current source has run into '
                'disbursement difficulties.',
    ),
    'suat-von-dau-tu': dict(
        td='Investment rates and conversion of foreign norms',
        mt='Selecting comparable projects and converting foreign investment rates and norms to '
           'the valuation date under Article 32, with reasoning that defends the file.',
        ten='Advising on investment rates and the conversion of foreign norms',
        lede='Vietnam’s system of construction norms does not yet cover every element of an '
             'urban railway. The law already permits the use of foreign norms and investment rates. '
             'But permission is one thing; proving your choice to the appraising authority is '
             'another — and this is where files are most often sent back.',
        van_de=[
            'There are no domestic norms for tunnelling, rolling stock, signalling or train control '
            'systems.',
            'Figures are taken from a foreign project without any argument for why that project is '
            '"comparable".',
            'Conversion to the valuation date is done loosely, without separating escalation, '
            'exchange rate and differences in construction conditions.',
            'Each time the project is adjusted the work starts again, because the source data was '
            'never kept.',
        ],
        can_cu=[
            ('Law on Railways — Article 32.1',
             'For items that do not fit, or do not appear in, the official system of norms, '
             'construction prices and investment rates, a railway project may use systems published '
             'by domestic or foreign organisations for comparable items or comparable railway '
             'projects, converted to the valuation date.'),
            ('Law on Railways — Article 32.2 and 32.5',
             'Where that is still not possible, investment rates from a comparable project elsewhere '
             'in the world may be used. Cost items not yet provided for in Vietnamese law may follow '
             'a comparable railway project abroad.'),
            ('Decree 206/2026/ND-CP — Article 16',
             'Appraisal and verification of construction estimates — what the appraiser will '
             'examine.'),
        ],
        lam_gi=[
            ('Identify which items lack domestic norms',
             'Compare the project’s work breakdown against the current norm system and list the '
             'gaps.'),
            ('Select comparable projects and prove comparability',
             'By gauge, line type, share of underground and elevated sections, ground conditions and '
             'level of automation. This argument matters as much as the numbers.'),
            ('Convert to the valuation date',
             'Separating three layers: escalation over time, the price-level difference between the '
             'two countries, and differences in construction conditions and applicable standards.'),
            ('Keep the source data',
             'Publisher, publication date, exchange rate used, price index used — so the next '
             'adjustment does not start from zero.'),
            ('Write the methodology note',
             'Detailed enough for the appraiser to follow each step of the calculation.'),
        ],
        dau_ra=[
            'A list of items with no domestic norm',
            'The comparable-project selection file with its reasoning',
            'A three-layer conversion table to the valuation date',
            'The retained source data set for future adjustments',
        ],
        khi_nao='When preparing or adjusting total investment; when preparing package estimates for '
                'specialised items; or when the appraising authority has asked you to justify the '
                'basis of your unit prices.',
    ),
    'kiem-soat-noi-bo': dict(
        td='Internal control for a railway project management unit',
        mt='Spending rules, separation of duties and checkpoints between measurement and payment, '
           'designed backwards from what settlement will demand.',
        ten='Advising on internal control for the project management unit',
        lede='Most of the errors found at settlement were not put there deliberately. They are there '
             'because, through years of execution, nobody was given the job of checking. Internal '
             'control built correctly at the outset is far cheaper than dealing with the consequences '
             'eight years later.',
        van_de=[
            'One person both certifies quantities and approves payment, with no check in between.',
            'Internal spending rules exist but were never reconciled against construction cost '
            'management regulations.',
            'Variations are approved verbally first and documented afterwards, leaving insufficient '
            'basis at settlement.',
            'Staff change over several terms, each working differently, with no common standard.',
        ],
        can_cu=[
            ('Decree 206/2026/ND-CP',
             'Management of construction investment cost: authority to approve estimates, package '
             'estimates and adjustments — the basis for setting approval levels in internal rules.'),
            ('Decree 207/2026/ND-CP',
             'Management of construction quality and maintenance — the basis for acceptance '
             'checkpoints.'),
            ('Decree 193/2026/ND-CP',
             'Settlement of investment capital. Knowing what settlement will demand is what lets you '
             'design the controls to match from the start.'),
        ],
        lam_gi=[
            ('Map the current flow',
             'From payment request to money leaving the treasury: who it passes through, who signs '
             'what.'),
            ('Identify the gaps',
             'Where one person holds two roles; where nobody reconciles; where documents follow the '
             'money instead of preceding it.'),
            ('Redesign the checkpoints',
             'Separate certification from payment approval; set approval limits by level; define the '
             'minimum documentation for each type of spending.'),
            ('Draft the rules and forms',
             'Internal spending rules, the measurement-to-payment control procedure, and the forms '
             'that go with them.'),
            ('Train and pilot',
             'Run it on several real files, correct what does not work, then issue it formally.'),
        ],
        dau_ra=[
            'Current flow and proposed flow, set side by side',
            'A list of control gaps with risk ratings',
            'Draft internal spending rules and control procedure',
            'A set of forms ready for immediate use',
        ],
        khi_nao='When a project management unit is newly established; when a line enters the '
                'construction phase with large payment volumes; or after an inspection or audit has '
                'raised findings on control.',
    ),
    'ho-so-quyet-toan': dict(
        td='Settlement records management from day one',
        mt='Rules for creating, coding, storing and handing over settlement records from the first '
           'contract package, for a project that runs eight to twelve years.',
        ten='Advising on settlement records management from the first day of the project',
        lede='A metro line runs eight to twelve years. The contractor on the first package may have '
             'been wound up before the line carries its first passenger. The engineer who signed an '
             'acceptance record in year two may have retired. Documents not collected at the right '
             'moment cannot be collected later — not because anyone is hiding them, but because they '
             'no longer exist.',
        van_de=[
            'Records for underground and concealed works are buried; there is no other way to verify '
            'them afterwards.',
            'Early-stage contractors are dissolved or change hands, leaving nobody to confirm '
            'quantities.',
            'Records sit across several departments with no common reference, and the gaps only '
            'appear when the settlement report is drafted.',
            'As-built drawings and acceptance records do not match, and it is discovered far too late '
            'to correct.',
        ],
        can_cu=[
            ('Decree 193/2026/ND-CP',
             'Settlement of investment capital — the list of records and the content of the '
             'settlement report. Knowing the destination is what lets you design the route.'),
            ('Decree 207/2026/ND-CP',
             'Management of construction quality and maintenance — acceptance records and completion '
             'documentation.'),
            ('Law on Railways — Article 23',
             'Component projects are each managed as an independent project, so the records must also '
             'be capable of being closed component by component.'),
        ],
        lam_gi=[
            ('Build the target record list',
             'Working backwards from what the settlement report requires: which stage must produce '
             'which document.'),
            ('Set a shared coding system',
             'One reference per component project, package and work item, so every department uses '
             'the same name.'),
            ('Fix mandatory collection points',
             'Tied to acceptance and payment milestones, so records never follow the money — '
             'especially for underground and concealed works.'),
            ('Design storage and backup',
             'Paper and electronic, where it is held, who holds it, where it is backed up, and for '
             'how long.'),
            ('Schedule quarterly self-checks',
             'Review each quarter what is missing, and demand it while it can still be obtained.'),
        ],
        dau_ra=[
            'A settlement record list by project stage',
            'A shared coding and naming convention',
            'Procedures for collection, storage, backup and handover',
            'A quarterly self-check sheet',
        ],
        khi_nao='Ideally before the first package is signed. Later is still workable, but it must '
                'come with a backward review to reconstruct what has already been lost.',
    ),
    'tai-co-cau-doanh-nghiep': dict(
        td='Restructuring the project and operating companies',
        mt='Advisory on reorganisation as a line moves from construction to operation: asset '
           'handover, the operating company structure, and the subsidy mechanism.',
        ten='Advising on restructuring the project company and the operating entity',
        lede='The day a line carries its first passenger is the day an organisation has to change '
             'its nature: from a body that manages investment to a body that runs a railway. The two '
             'need different people, different procedures and a different financial mechanism. Make '
             'the change too late and the line runs while the books do not.',
        van_de=[
            'Assets formed through investment are not fully and correctly recognised before handover '
            'to the operator.',
            'It is unclear on what basis the operator receives the assets, or how they are recorded.',
            'The subsidy mechanism has no settled formula and is renegotiated every year.',
            'The project management unit still has settlement work outstanding while its staff have '
            'already moved to operations.',
        ],
        can_cu=[
            ('Law on Railways — Article 5.2(c)',
             'The State subsidises public passenger transport by urban railway.'),
            ('Law on Independent Audit — Article 40.2(b)',
             'An audit firm may register to provide advisory services on management, conversion and '
             'corporate restructuring.'),
            ('Decree 193/2026/ND-CP',
             'The value of assets formed through investment and their handover — this must be closed '
             'before transfer to the operating entity.'),
        ],
        lam_gi=[
            ('Review assets and liabilities before transfer',
             'Whether asset documentation is complete, how much contractor debt remains outstanding, '
             'and who carries it onward.'),
            ('Design the operating entity',
             'Functions, structure, headcount, and the settlement work the project management unit '
             'retains.'),
            ('Build the operating financial mechanism',
             'Subsidy formula, adjustment mechanism, and indicators for assessing operating '
             'performance.'),
            ('Set a milestone-based transfer roadmap',
             'What must be finished before commercial operation begins, and what may follow after.'),
        ],
        dau_ra=[
            'A review report on assets and liabilities before transfer',
            'A structural plan for the operating entity',
            'A proposed financial mechanism and subsidy formula',
            'A transfer roadmap against dates',
        ],
        khi_nao='Twelve to eighteen months before the planned start of commercial operation; or when '
                'the province is preparing to establish or reorganise its urban railway operator.',
    ),
    'thue-du-an': dict(
        td='Tax advisory for urban railway projects',
        mt='Foreign contractor tax on rolling stock and signalling, VAT treatment under ODA, and the '
           'investment incentives the Law on Railways already provides.',
        ten='Tax advisory for an urban railway project',
        lede='An urban railway imports almost all of its core technology: rolling stock, signalling, '
             'train control, together with the foreign specialists who come with it. Every such '
             'contract carries a foreign contractor tax question, and mistakes usually surface only '
             'at a tax inspection — by which time the money has already been paid to the contractor.',
        van_de=[
            'A turnkey contract covering equipment, installation, training and technology transfer '
            'does not separate the value of each part, so the wrong withholding rate is applied.',
            'It is not settled which party bears foreign contractor tax, and the shortfall appears at '
            'settlement.',
            'VAT treatment of the ODA-funded portion is applied inconsistently across packages.',
            'Investment incentives the law already grants to the railway sector are not fully used.',
        ],
        can_cu=[
            ('Law on Railways — Article 5.4',
             'Railway infrastructure business, railway transport, railway industry and railway '
             'workforce training are investment-incentivised sectors.'),
            ('Law on Railways — Article 32.4',
             'Trial running, training and technology transfer costs are included in total investment '
             '— how these are separated bears directly on the tax position.'),
            ('Law on Independent Audit — Article 40.2(a)',
             'An audit firm may register to provide economic, financial and tax advisory services.'),
        ],
        lam_gi=[
            ('Review the contract before signing',
             'Separate the value of each component, establish the tax treatment of each, and make '
             'clear which party bears the tax.'),
            ('Determine the foreign contractor tax position',
             'By activity: supply of goods, installation services, training, technology transfer.'),
            ('Settle VAT treatment by funding source',
             'Applied consistently across all packages within the project.'),
            ('Review investment incentives',
             'Against the qualifying conditions and the documentation needed to claim them.'),
            ('Prepare the explanatory file',
             'Ready in advance for when the tax authority examines the position.'),
        ],
        dau_ra=[
            'A review of the tax clauses in the contract, with proposed amendments',
            'A schedule of foreign contractor tax by component',
            'Consistent VAT guidance for the whole project',
            'An explanatory file for the tax authority',
        ],
        khi_nao='Before signing with a foreign contractor — that is the point at which the clauses '
                'can still be changed. After signature, only the consequences can be managed.',
    ),
    'boi-duong-can-bo': dict(
        td='Training for project management unit staff',
        mt='Training built from the unit’s own files: settlement, cost control, payment '
           'documentation and preparing for an audit.',
        ten='Training in finance, accounting and auditing for project management unit staff',
        lede='Most project management unit staff come from an engineering background. They read '
             'drawings better than they read settlement regulations. That gap is behind a great many '
             'files that have to be redone — and it can be closed with the right training, without '
             'anyone going back for another degree.',
        van_de=[
            'Payment files are returned repeatedly for missing components, costing both sides time.',
            'Staff do not know in advance what an audit will ask, so they prepare reactively.',
            'Everyone works differently because the unit has no common standard.',
            'New staff have no material to learn from and pick it up by word of mouth.',
        ],
        can_cu=[
            ('Law on Independent Audit — Article 40.2(e)',
             'An audit firm may register to provide training in finance, accounting and auditing. '
             'Our programme is kept strictly within those three fields.'),
            ('Decree 193/2026/ND-CP',
             'Settlement of investment capital — the core of the programme.'),
            ('Decree 206/2026/ND-CP', 'Management of construction investment cost.'),
        ],
        lam_gi=[
            ('Survey the need first',
             'Look at the unit’s actual files to see where the difficulty lies, then design the '
             'content. We do not arrive with a ready-made syllabus.'),
            ('Design by audience',
             'Engineering staff, accounting staff and unit leadership need three different levels.'),
            ('Teach on real files',
             'Using the project’s own documents, anonymised, instead of invented examples.'),
            ('Set and mark applied exercises',
             'Participants should be able to do the work afterwards, not merely to have heard it.'),
            ('Hand over the self-study pack',
             'So that staff joining later can still use it.'),
        ],
        dau_ra=[
            'A training needs assessment report',
            'The programme and teaching materials, handed over to the unit',
            'Assessment results for each participant',
            'A self-study pack for new staff',
        ],
        khi_nao='Ahead of the settlement season; when the unit takes on a number of new staff; or '
                'after an audit or inspection has raised the same findings repeatedly.',
    ),
}

assert len(EN) == 9
