# -*- coding: utf-8 -*-
"""Ban TIENG ANH: trang VAN BAN (document lookup) va THU VIEN RUI RO (risk library).

TEN VAN BAN GIU NGUYEN TIENG VIET — do la ten chinh thuc, dich ra thi khong tra cuu duoc.
"""

# =================================================================== VAN BAN
VB = dict(
    td='Urban railway documents — lookup',
    mt='Fifty-one legal instruments on urban railway and TOD projects in Vietnam, filterable by '
       'level, locality, year and status, with the Word or PDF file attached.',
    duong='Documents',
    h1='Document lookup',
    lede='Fifty-one instruments governing urban railway and TOD projects, each with its Word or PDF '
         'file attached. Document titles stay in Vietnamese — those are the official titles, and '
         'they are what you need in order to cite or search for them elsewhere.',
    h_cach='How to use this page',
    cach=[
        ('Accents optional in the search box',
         'File names in the store carry no accents, but the search box strips accents on both '
         'sides. “đường sắt” and “duong sat” return the same result.'),
        ('Search by document number',
         'If you remember the number, type the number: “188”, “62/2026”, “15/2025”. Faster than '
         'recalling the full title.'),
        ('Filters stack',
         'The four filters add to each other and to the search box. For example Thông tư + Hanoi + '
         'in force.'),
        ('Click the title to open the document',
         'Clicking a title opens the Word version; where no Word version exists it opens the PDF. '
         'The <b>Open file</b> column lets you choose the format.'),
        ('Long documents come in several parts',
         'The Official Gazette publishes long instruments in several issues. Those show as '
         '<b>W1 W2…</b> or <b>P1 P2…</b> — you need all the parts to have the full text.'),
    ],
    h_co='What the store holds',
    tk=['Instruments', 'Word and PDF files', 'Both Word and PDF', 'PDF only',
        'Consolidated texts', 'Local instruments'],
    h_cap='Four levels — which order to read them in',
    cap=[
        ('Laws and National Assembly resolutions',
         'The legal foundation. For urban railway, read the consolidated Law on Railways first, then '
         'Nghị quyết 188/2025 on the special mechanism — that is the instrument that actually changes '
         'the procedural sequence.'),
        ('Decrees',
         'Detailed implementing rules. The consolidated text VBHN 34/VBHN-BXD, with 143 articles on '
         'overall technical design and the special mechanism, is the one to read.'),
        ('Circulars and technical regulations',
         'Norms, unit prices, forms and technical requirements. This is the layer that changes most '
         'often — always check which version was in force at the time.'),
        ('Local instruments',
         'Resolutions of the provincial People’s Council. These decide the money: TOD revenue, '
         'underground space charges, compensation policy. Applicable only within that province.'),
    ],
    h_luu='Two things to watch',
    luu=[
        ('An instrument applies according to when the event arose',
         'A cost incurred in 2022 is governed by what was in force in 2022, not by what is in force '
         'today. This is the single most common basis error in settlement files.'),
        ('“Expired” does not mean “irrelevant”',
         'An expired instrument still governs everything that happened while it was in force. We '
         'keep expired instruments in the store for exactly that reason, marked as expired.'),
    ],
    l_cap='Level', l_so='Number', l_ten='Title', l_nam='Year', l_hl='Status', l_tep='Open file',
    hl_con='In force', hl_het='Expired', hn='Consolidated',
    loc_tim='Search', loc_cap='Level', loc_dia='Locality', loc_nam='Year', loc_tt='Status',
    loc_tatca='All',
    tim_gy='Title, number, or keyword',
    dem='%d of %d instruments',
)

# =================================================================== THU VIEN RUI RO
RR = dict(
    td='Risk library for settlement audit of railway projects',
    mt='Thirty-three risks in eight groups for the settlement audit of an urban railway project: '
       'what the signal looks like and how to test it.',
    duong='Risk library',
    h1='Risk library for the settlement audit',
    lede='Thirty-three risks, grouped into eight. For each: what the signal looks like, and how to '
         'test it. Use it as a checklist when planning an audit, or as a self-check before a '
         'settlement file goes for verification.',
    h_ng='Where this comes from, and what it is not',
    ng='This library is compiled from professional experience and publicly available material. It '
       'is <b>general reference</b>. Nothing in it is drawn from the file of any particular entity, '
       'and no item describes any actual project. Read it as a list of things worth testing — not '
       'as an allegation about anyone.',
    h_ds='The eight groups',
    l_dh='What the signal looks like', l_kt='How to test it',
    muc=dict(cao='High', trung='Medium', thap='Low'),
    l_muc='Attention',
    h_dung='How to use it',
    dung=[
        'When planning, run down the list and mark which items apply to this project. Items you rule '
        'out, write down why — that is evidence of judgement, not of laziness.',
        'When testing, the “how to test it” column is a starting point, not a substitute for the '
        'audit programme.',
        'Before a file goes for verification, an investor can run the same list as a self-check. '
        'Most items are things that can still be corrected if they are found in time.',
    ],
    h_bt='If you would like this applied to your own project',
    bt='Send the details through the %s page. We will say which groups matter most for the stage '
       'your project is at.',
    bt_lk='Advice',
)

# 8 nhom, moi rui ro: (ten, dau hieu, kiem the nao, muc)
RR_NHOM = [
    ('Legal file', [
        ('The investment sequence is out of order or a step is missing',
         'A contract signed before the project approval decision; work started before the '
         'construction permit.',
         'Compare the signing date of every document along a timeline — not merely whether the '
         'document exists.', 'cao'),
        ('Approval given at the wrong level',
         'The person signing the decision does not hold authority for that project class or that '
         'value band.',
         'Match the signatory’s position against the delegation rules in force on the signing date.',
         'cao'),
        ('The special mechanism applied outside its scope',
         'Shortened procedures used for a project or a locality that is not within the pilot scope.',
         'Ask the investor to produce the document showing the project falls within the scope.',
         'cao'),
        ('Documents drawn up later and back-dated',
         'Records and decisions prepared late but bearing the date they ought to have carried.',
         'Compare paper stock and layout across the same file; cross-check against the site diary '
         'and payment vouchers of the same period.', 'trung'),
    ]),
    ('Funding and payment', [
        ('The investor’s ledger differs from the paying authority',
         'Capital paid per the accounting records differs from the figure held by the Treasury or '
         'the servicing bank.',
         'Require a signed reconciliation for each year; trace the cause of every difference — do '
         'not accept a netted total.', 'cao'),
        ('Payment exceeds the contract value',
         'The sum of all payment tranches exceeds the contract price plus valid addenda.',
         'Add up every tranche and compare against the contract price as adjusted.', 'cao'),
        ('Advances not fully recovered',
         'A contractual advance has not been fully offset although the works are complete.',
         'Keep an advance and recovery schedule per contract, reconciled against the advance '
         'guarantee.', 'trung'),
        ('Costs incurred with no capital allocated',
         'Quantities executed but no capital allocated in the public investment plan.',
         'Reconcile costs proposed for settlement against the annual capital allocation.', 'trung'),
    ]),
    ('Quantities and unit rates', [
        ('Settled quantity exceeds accepted quantity',
         'The settlement schedule records more than the corresponding acceptance record.',
         'Reconcile three ways: settlement schedule — acceptance record — as-built drawing.', 'cao'),
        ('The same quantity counted in two packages',
         'One work item counted in two different packages, usually where two packages meet.',
         'Search for duplicates by unit-rate code and by chainage; pay particular attention to '
         'package boundaries.', 'cao'),
        ('The wrong period’s norm applied',
         'Current norms used for quantities accepted years earlier.',
         'Fix the date each work item applies to, then look up the norm in force on that date.',
         'cao'),
        ('Specialised work with no approved norm',
         'Tunnelling, signalling installation, integrated testing — not present in the general norm '
         'system.',
         'Require the decision approving a new norm; without it the item lacks a basis for '
         'settlement.', 'cao'),
        ('Price adjustment inconsistent with the form of contract price',
         'Escalation paid on a lump-sum contract or a fixed unit-rate contract.',
         'Establish the form of contract price stated in the contract first, then consider whether '
         'the adjustment is permitted at all.', 'cao'),
        ('The wrong price index used',
         'An index for a different province, a different type of works, or a different period.',
         'Match the index source against the contract terms and against the publication of the '
         'competent authority.', 'trung'),
    ]),
    ('Contracts', [
        ('The form of contract price differs from how the parties actually pay',
         'A lump-sum contract settled on measured quantities, or the reverse.',
         'Read the price clause and the payment clause before checking a single figure.', 'cao'),
        ('An addendum signed after the work was finished',
         'An addendum adjusting quantities or price signed after that part was accepted.',
         'Compare the addendum signing date against the acceptance date for the same work.', 'cao'),
        ('An EPC contract with no detailed bill of quantities',
         'An international-form contract defining scope by output, with no bill of quantities to '
         'check against.',
         'Require the price analysis and the base bill of quantities; if neither exists, state the '
         'scope limitation clearly.', 'cao'),
        ('The adjusted price exceeds the approved package price',
         'Contract price plus addenda exceeds the package price in the contractor selection plan.',
         'Add them up and compare against the decision approving the contractor selection plan.',
         'trung'),
    ]),
    ('Project management, consultancy and other costs', [
        ('Project management cost above the norm',
         'Actual cost exceeds the amount derived from the percentage norm on construction and '
         'equipment cost.',
         'Recompute using the norm interpolated between the two size thresholds and compare against '
         'the amount claimed.', 'trung'),
        ('Items already inside the norm charged separately',
         'Stationery, electricity and water of the project management unit charged on top of the '
         'norm.',
         'Compare the list of costs already covered by the norm against actual spending.', 'trung'),
        ('Consultancy cost above the contract',
         'Settled value of a consultancy contract exceeds the contract price plus addenda.',
         'Reconcile each consultancy contract and check that the deliverables were in fact '
         'delivered.', 'trung'),
    ]),
    ('Assets and handover', [
        ('Asset value does not balance against investment cost',
         'The balance equation does not hold: cost, less amounts not chargeable to assets, less '
         'surplus stock, does not equal asset value.',
         'Run the balance equation on a single set of figures; trace every difference before '
         'issuing.', 'cao'),
        ('Common costs allocated without a principle',
         'Common costs split across items by feel rather than in proportion to capital.',
         'Check the allocation schedule and match the allocation basis against the approved policy.',
         'trung'),
        ('Assets missing or duplicated across receiving entities',
         'The same item appears in two handover records, or in none.',
         'Reconcile the total asset schedule against the sum of all handover records.', 'trung'),
        ('Costs excluded from asset value without permission',
         'Losses, or costs of a cancelled item, with no decision of the competent authority.',
         'Require the decision permitting it; without one the amount must stay suspended and cannot '
         'be transferred.', 'cao'),
    ]),
    ('Debts and surplus stock', [
        ('Debts recorded against the wrong party',
         'Balances recorded by package name rather than by contractor legal entity, or several '
         'contractors merged.',
         'Reconcile balances by legal entity; circularise under the auditor’s control.', 'trung'),
        ('Confirmations sent and received by the investor',
         'The auditor does not control despatch and receipt, so the evidence loses reliability.',
         'The auditor controls the despatch address and receives the replies directly.', 'cao'),
        ('Surplus materials and equipment with no disposal plan',
         'Materials still in store after completion with no decision on what happens to them.',
         'Count physically against the records; recommend a disposal route in the report.', 'thap'),
    ]),
    ('Risks particular to urban railway projects', [
        ('Trial-running costs classified wrongly',
         'Electricity, operating payroll and insurance during trial running charged to investment '
         'cost with no basis for doing so.',
         'Require the document approving the scope and funding source for trial running, prepared '
         'before trial running began.', 'cao'),
        ('System safety assessment cost missing from total investment',
         'An item carried out by an independent foreign body, commonly omitted when the project was '
         'prepared.',
         'Reconcile the safety assessment contract against the approved total investment.', 'trung'),
        ('Exchange differences on loans and imported equipment',
         'Rates applied to different transaction types inconsistently, or at the wrong date.',
         'Test exchange differences separately; match the rates applied against the contract terms.',
         'cao'),
        ('Unclear whether training and technology transfer create an asset',
         'Large amounts that form no fixed asset, easily suspended at settlement.',
         'Require a decision of the competent authority on whether they are chargeable to asset '
         'value.', 'trung'),
        ('No clear cost boundary between the line and the TOD area',
         'Cash flows and assets of the two are mixed, and cannot be separated at handover.',
         'Check whether a cost separation policy was established at project preparation stage.',
         'trung'),
    ]),
]
