# -*- coding: utf-8 -*-
"""Ban TIENG ANH: trang KINH NGHIEM (lessons) va VUONG MAC (common problems) + CHAN TRANG."""

# =================================================================== KINH NGHIEM
KN = dict(
    td='Twelve lessons from managing urban railway projects',
    mt='Twelve practices that decide whether a settlement file survives, three costly '
       'misconceptions, and a checklist at five points in the project.',
    duong='Experience',
    h1='Twelve lessons from project management',
    lede='None of these is difficult. Every one is cheap to do at the right moment and expensive to '
         'repair later. They are written for a project management unit that intends its settlement '
         'file to survive, on a line that will run eight to fifteen years.',
    h_bh='Twelve lessons',
    h_sl='Three costly misconceptions',
    h_kt='A checklist at five points',
    kt_lede='Not a compliance form. It is the short list of things that, if missing at that moment, '
            'cannot be recovered afterwards.',
    h_bt='Applying this to your own project',
    bt='If you would like these turned into procedures and forms for your unit, that is one of the '
       'services we provide — see %s.',
    bt_lk='settlement records management from day one',
)

KN_BH = [
    ('Build a map of which instruments applied when — and keep it current',
     'As soon as the project is approved, build a table: each project milestone against the '
     'instruments in force at that moment. Add a row every time a new decree or circular replaces '
     'an old one. The table takes about two days to build and ten minutes to update. Without it, '
     'settlement means spending months reconstructing it from the memory of whoever is still there.'),
    ('Lock the form of contract price in the bidding documents',
     'One form of price per package. Where a package mixes several kinds of work, split the price '
     'annex by part. Most important: the way payment actually happens must match the form of price '
     'written down. This is the most expensive lesson here — most of the argument at verification '
     'sits precisely on this point.'),
    ('Create records as the work happens, not at the end of the period',
     'Acceptance records signed on the day of acceptance. As-built drawings prepared as soon as the '
     'item is finished. Site diary written daily. It sounds obvious, and it is the rule most often '
     'broken — and the direct cause of most amounts disallowed at settlement.'),
    ('Photograph and measure what will be covered up, while it can still be seen',
     'On a metro, underground work is a very large share of cost and cannot be measured again after '
     'completion. Reinforcement before the pour, tunnel support before the lining — each needs '
     'photographs carrying time and location, with a record signed by the parties. A photograph '
     'without time and location proves almost nothing.'),
    ('Reconcile capital paid with the paying authority every year',
     'The step most often skipped, and the one that finds the most differences. Do it annually, with '
     'a record signed by both sides. A difference found within the year can be dealt with; found '
     'after eight years it means tracing the whole chain of vouchers.'),
    ('Get norms approved for specialised work before it is carried out',
     'Machine tunnelling, signalling installation, overhead power, integrated testing — none of '
     'these appears in the general construction norm system. A new norm has to be prepared and '
     'approved before the work is done. Do the work first and seek approval later, and that cost '
     'will be suspended.'),
    ('Decide the treatment of trial-running costs in advance',
     'Before trial running starts, obtain approval of a document setting out the scope, the '
     'duration, the list of costs and the funding source. Open a separate tracking code in the '
     'accounts. It takes a week and saves months at settlement.'),
    ('Allocate project management cost on a principle, not by feel',
     'Cost directly attributable to an item goes wholly to that item; common cost is allocated in '
     'proportion to capital. Build the allocation schedule early and maintain it, rather than '
     'sitting down to divide it up at settlement — particularly where assets will go to several '
     'different receiving entities.'),
    ('List the assets you expect to create, from the approval stage',
     'Do not wait until handover to think about who receives what. Build the table early: item — '
     'asset type — expected receiving entity — legal basis for the transfer. It will be revised '
     'many times, but having it from the start makes every revision light.'),
    ('Deal with inspection and State Audit findings at once, and keep the trail',
     'A long, large project will almost certainly face at least one inspection or audit in its life. '
     'For each finding: keep the document, track each point in a schedule, record what was done '
     'about it and where the evidence sits. At settlement, this schedule is the first thing asked '
     'for.'),
    ('Keep the people who know the file — and where you cannot, hand over on the record',
     'A ten to fifteen year life is longer than the average tenure of a project officer. Every time '
     'the responsible officer changes, hand over against a document schedule, not in general terms. '
     'The document schedule belongs to the organisation, not to the individual.'),
    ('Digitise early, and name files to one convention',
     'Paper vouchers from the early years will fade, go missing, absorb damp. Scan and name them to '
     'a convention as they arise — package, document type, date, number. The cost of doing this is '
     'trivial beside the cost of hunting for a year-two acceptance record in year eleven.'),
]

KN_SL = [
    ('Treating settlement as the accountant’s job',
     'Settlement of investment capital is work for the whole project management unit: the technical '
     'department holds quantities and acceptance records, the contracts department holds the price '
     'terms, the planning department holds total investment, the accounts department holds the '
     'vouchers. Hand it wholly to accounting and accounting can only consolidate what it is given — '
     'and whatever is not given becomes a gap in the file.'),
    ('Applying today’s instruments to work done years ago',
     'A cost arising in 2022 is governed by what was in force in 2022, not by a 2026 instrument. A '
     'work item accepted in 2023 takes the norm in force in 2023. This is a basis error, and the '
     'verifying authority is entitled to reject it.'),
    ('Invoking the special mechanism without proving it applies',
     'The special mechanism shortens a number of steps — but only where the project falls within '
     'its scope and within its period of effect. The file must contain the proof: that the project '
     'is within the scope of NQ 188/2025, which part of the work arose after the resolution took '
     'effect, which step was shortened under which provision. A general reference to “the special '
     'mechanism” without citing a provision is not enough.'),
]

KN_KT = [
    ('As soon as the project is approved', [
        'A map of which instruments applied when — built, with someone named to keep it current',
        'Which of the four legal tracks the project sits in, with the document proving it',
        'A schedule of total investment by period — opened even before any adjustment',
        'The list of assets expected to be created and their expected receiving entities',
        'A file naming convention and electronic folder structure — issued in writing',
    ]),
    ('Before issuing the bidding documents for each package', [
        'The form of contract price settled, one form per part of the work',
        'Bidders required to submit a price analysis and a base bill of quantities as contract annexes',
        'A technology transfer schedule with acceptance criteria and the value attached to each item',
        'Training obligations tied to acceptance milestones, not paid as a lump sum in advance',
        'Contract language, responsibility for translation, and the conversion rate for foreign '
        'contractors',
    ]),
    ('Throughout construction', [
        'A site handover register by chainage and by date, signed by three parties',
        'Norms for specialised work approved before the work is carried out',
        'Photographs and measurements of what will be covered up — with time, location and a record',
        'Annual reconciliation of capital paid with the paying authority',
        'Allocation schedules for project management and consultancy cost — updated regularly',
        'Every extension of time recorded in a contract addendum, not in correspondence',
    ]),
    ('Before trial running', [
        'A document approving the scope, duration, cost list and funding source',
        'A separate tracking code for trial-running cost in the accounting system',
        'System safety assessment and certification — with its own estimate and its own contract',
        'As-built records for the equipment, with a Vietnamese version',
    ]),
    ('Before handover', [
        'The list and value of assets to be handed over, by receiving entity',
        'Assets classified as long-term or short-term',
        'The project management unit’s own assets: ledger reconciled to physical count, residual '
        'value established',
        'Surplus materials and equipment: ledger reconciled to physical count, with a disposal plan',
        'Receivables and payables attributed to the correct parties, with recommended treatment',
    ]),
]

# =================================================================== VUONG MAC
VM = dict(
    td='Ten recurring problems on urban railway projects',
    mt='Ten problems that recur on urban railway projects in Vietnam: what happens, why it happens, '
       'which instruments govern it, and what to do about it.',
    duong='Common problems',
    h1='Ten recurring problems',
    lede='Each of these is set out the same way: what actually happens, why it happens, which '
         'instruments govern it, and what can be done. They are recurring patterns, not the file of '
         'any particular project.',
    l_ht='What happens', l_ng='Why it happens', l_cc='Governing instruments', l_xl='What to do',
    h_bt='If your project is stuck on one of these',
    bt='Describe the situation on the %s page. Say where the project is, what the funding source is, '
       'and the date of the matter — instruments apply according to when the event arose.',
    bt_lk='advice',
)

VM_DS = [
    ('Site clearance and resettlement',
     'The site is handed over in short disconnected stretches. The contractor receives section A '
     'while section B is unfinished, plant and labour stand idle, and a claim for standing time and '
     'an extension of time follows.',
     'A metro runs through established urban areas with dense population and utilities. The '
     'compensation plan is built on cadastral records while the actual situation on the ground has '
     'moved on. Costs approved at one date are paid out over several years.',
     'Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · NĐ 226/2025 · '
     'Hanoi, in TOD areas: NQ 66/2026/NQ-HĐND Article 11',
     'Keep a site handover register by chainage and by date, signed by three parties — this is the '
     'primary evidence that decides whether standing-time cost can be settled at all. Record every '
     'extension in a contract addendum, not in correspondence. Reconcile the payment list against '
     'actual vouchers quarterly.'),
    ('Total investment adjusted several times',
     'Total investment is approved at one figure; a few years on, actual cost is far above it. While '
     'the adjustment awaits approval, construction and payment continue. At settlement, part of the '
     'work turns out to exceed the total investment that was in force when it was done.',
     'Four causes usually compound: preliminary total investment built on thin survey data; '
     'escalation across an eight to fifteen year life; design changes because underground conditions '
     'differ from expectation; and site clearance cost rising with land prices.',
     'Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (amended by NĐ 275/2025) · NĐ 206/2026 on cost '
     'management · NĐ 19/2026 on appraisal and investment supervision',
     'Cost proposed for settlement must fall within the approved total investment — the excess, '
     'absent an approved adjustment, has no basis for inclusion in the settled value, even where the '
     'work is built and accepted. Keep a schedule of total investment by period; obtain the '
     'adjustment before carrying out the excess.'),
    ('EPC contracts and foreign contractors',
     'An EPC package is signed on an international form, lump sum in foreign currency, paid against '
     'milestones. At settlement the investor has no detailed bill of quantities to check against; '
     'the verifying authority asks for a breakdown and the contractor refuses, the contract being '
     'lump sum.',
     'International contracting and domestic settlement law rest on two different logics. The '
     'international form treats lump sum as transferring quantity risk to the contractor; a State '
     'capital settlement file demands evidence of quantities executed.',
     'NĐ 37/2015 amended by NĐ 50/2021 (consolidated text 07/VBHN-BXD) · Luật Xây dựng 135/2025/QH15 '
     '· Luật Đấu thầu 22/2023/QH15 · VBHN 34/VBHN-BXD · NĐ 04/2026 on the railway industry',
     'Lock the form of price in the bidding documents; where an EPC package mixes kinds of work, '
     'split the price annex by part. Require a price analysis and a base bill of quantities as '
     'contract annexes even on a lump sum. State the contract language, who is responsible for '
     'translation, and the conversion rate.'),
    ('Trial-running costs before commercial operation',
     'Trial running lasts months, sometimes more than a year. Traction electricity, operating '
     'payroll, insurance and foreign specialists all arise. The works are not handed over and earn '
     'no revenue. Is this investment cost or operating cost?',
     'On a metro the boundary between the end of investment and the start of operation is not a '
     'point but an interval. Trial running is both an acceptance step and an operating activity. '
     'Construction law and public asset law do not join up at precisely this place.',
     'NĐ 207/2026 and TT 32/2026/TT-BXD · TT 62/2026/TT-BXD metro technical regulation · NĐ 16/2026 '
     '· NĐ 15/2025 on infrastructure assets · TT 79/2026/TT-BTC',
     'Decide before trial running, not after: obtain approval of a document fixing the scope, the '
     'duration, the list of costs and the funding source. Open a separate tracking code in the '
     'accounts. Treat the system safety certification file as a standalone contract item with its '
     'own estimate.'),
    ('Applying foreign standards and technical regulations',
     'Design and equipment follow the standards of the country supplying the technology. At '
     'acceptance and settlement the domestic authority asks for a comparison against Vietnamese '
     'technical regulations, and many parameters either do not exist or are measured differently.',
     'Vietnam has had a dedicated technical regulation for metro-type urban railway only since '
     'TT 62/2026/TT-BXD of 30 July 2026. Lines started before that date had to borrow foreign '
     'standards, and each line uses the technology of a different country.',
     'Hanoi: NQ 40/2025/NQ-HĐND — note that Article 1.2 states expressly that urban railway follows '
     'its own route and does NOT follow the general sequence in that resolution · TT 62/2026/TT-BXD '
     '· TT 44/2025/TT-BXD',
     'Prepare a standards comparison table at design stage and have it approved, rather than leaving '
     'it as an internal consultant document. For Hanoi projects, do not cite NQ 40/2025 as authority '
     'for urban railway — that resolution excludes it; cite Luật Thủ đô 02/2026/QH16 and '
     'NQ 188/2025/QH15.'),
    ('Settlement of a project that ran for many years',
     'The project has passed through several generations of decrees on cost management, project '
     'management and settlement, and several rounds of amendment to the norm circulars. The people '
     'who prepared the file have left; early vouchers are in storage and some have faded.',
     'This is simply the nature of a project with an eight to fifteen year life. There is no way to '
     'avoid it, only ways to manage it.',
     'The chains to know — project management: NĐ 59/2015 → NĐ 15/2021 → NĐ 175/2024 → NĐ 209/2026 '
     'and NĐ 210/2026. Cost management: NĐ 32/2015 → NĐ 68/2019 → NĐ 10/2021 → NĐ 206/2026. '
     'Settlement: TT 09/2016 → TT 10/2020 → NĐ 99/2021 → NĐ 254/2025',
     'The first task is to build the project’s own map of which instruments applied when, assigning '
     'each milestone to a generation. A conclusion that cannot cite the document number of the right '
     'period will not stand. Reconcile capital paid with the paying authority annually rather than '
     'waiting for the end.'),
    ('TOD and capturing the increase in land value',
     'Policy allows the city to capture part of the increase in land value around stations to offset '
     'the cost of the line. In practice, the implementing body cannot work out how much is to be '
     'collected.',
     'The mechanism is complete at the level of the law and the People’s Council resolution, but the '
     'document that quantifies it is missing at the bottom layer. There is a second mismatch: the '
     'TOD plan must be approved first, yet the TOD plan depends on a fixed alignment and station '
     'locations — while the line is still being redesigned.',
     'Luật Thủ đô 02/2026/QH16 Article 12 · NQ 188/2025/QH15 · Hanoi: NQ 71/2025, NQ 66/2026, '
     'NQ 67/2026 · HCMC: NQ 21/2026 (replacing NQ 38/2025 from 19 June 2026), NQ 90/2025',
     'Draw the accounting boundary between the line project and the TOD project from the outset. For '
     'Hanoi, watch the Official Gazette for the resolution on the TOD advantage coefficient the '
     'moment it is issued — until it exists, every TOD revenue figure is an internal estimate and '
     'does not belong in a formal financial plan.'),
    ('Underground space',
     'Underground stations and tunnel sections sit beneath land held by many different users. To '
     'what depth is land recovered, how is the subsurface compensated, what is the land rent for an '
     'underground structure, and how far may the commercial area within an underground station be '
     'exploited?',
     'Traditional land law manages by surface parcel. Underground space is a new layer of '
     'administration, only just laid down in Luật Thủ đô and the 2026 resolutions of the Hanoi '
     'People’s Council.',
     'Luật Thủ đô 02/2026/QH16 Article 11 · Hanoi: NQ 64/2026 (underground space planning), '
     'NQ 65/2026 (charges), NQ 62/2026 (investment incentives)',
     'Establish and record the underside level of each station and each tunnel section in the design '
     'and as-built files — the fifteen-metre threshold decides the financial obligation directly. '
     'Separate the underground floor area used for operations from the area exploited commercially, '
     'because the two carry different financial regimes.'),
    ('Training the operating workforce',
     'The cost of training drivers, controllers and maintenance staff is included in total '
     'investment. At settlement the question arises: does this create an asset? If not, how is it '
     'treated?',
     'Training is investment cost in economic terms but forms no fixed asset in accounting terms. '
     'Those trained may leave before the line opens, which raises a question about the effectiveness '
     'of the capital.',
     'NQ 188/2025/QH15, the group of mechanisms on technology transfer and workforce training · '
     'QĐ 2230/QĐ-TTg, the railway workforce plan to 2035 · NĐ 254/2025',
     'Settle it at project preparation stage: which cost heading training belongs to, and whether it '
     'is chargeable to asset value. If it is not, permission from the competent authority is '
     'required — that is a separate procedure, not something the investor can decide alone. Keep '
     'full evidence, because this is a cost with no physical product.'),
    ('Technology transfer and localisation',
     'The contract contains a technology transfer clause but describes it in general terms, with no '
     'specific schedule, no acceptance criteria and no separate payment milestone. At settlement '
     'nobody can establish whether the obligation was performed, or what share of the contract price '
     'it represents.',
     'Technology transfer is an obligation that is hard to quantify. The seller has an incentive to '
     'retain the core. The buyer often lacks the technical capacity to define precisely what it '
     'needs to receive at the moment of signing.',
     'NQ 188/2025/QH15 · NĐ 04/2026 on assigning and ordering railway industry work · '
     'QĐ 498/QĐ-TTg on restructuring Vietnam Railways · Luật Chuyển giao công nghệ 07/2017/QH14',
     'Set out the transfer schedule as a table in the bidding documents: content — form — acceptance '
     'criteria — date — corresponding value. Without a value column it cannot be settled. Make it a '
     'separate payment item and retain the final percentage until the whole schedule is accepted.'),
]

# =================================================================== CHAN TRANG
CHAN = dict(
    en=dict(
        gt='A professional reference site on the investment, management and settlement of urban '
           'railway projects in Vietnam.',
        c1='Reference', c2='Get in touch', c3='Please note',
        m1=[('van-ban', 'Document lookup'), ('quy-trinh', 'Project process'),
            ('kinh-nghiem', 'Project management experience')],
        m2=[('vuong-mac', 'Common problems'), ('tu-van', 'Request advice'), ('lien-he', 'Contact')],
        luu='Content on this site is for reference and does not replace advice on a specific '
            'project. Legal instruments change often — always check against the original.',
        bq='Copyright of ASCO Auditing and Valuation Firm · Compiled from our internal store of '
           'legal instruments.',
        ngay='Documents updated to %s.',
    ),
)
