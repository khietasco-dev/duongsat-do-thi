# -*- coding: utf-8 -*-
"""Ban TIENG ANH: trang QUY TRINH (project process) va KIEM TOAN QT (settlement audit).

Ten van ban phap luat GIU NGUYEN so hieu tieng Viet — do la ten chinh thuc.
Phan dien giai la cach doc cua ASCO, khong phai ban dich chinh thuc.
"""

# =================================================================== QUY TRINH
QT = dict(
    td='Urban railway project process — nine stages',
    mt='The nine stages of an urban railway project in Vietnam: what happens, who decides, '
       'which law applies, what comes out, and where files usually go wrong.',
    duong='Process',
    h1='The nine stages of an urban railway project',
    lede='This page follows a metro line from the moment it enters a provincial plan to the day its '
         'settlement is approved. For each stage: the work itself, who has authority, the governing '
         'instruments, the documents produced, and the point where files most often fail. The '
         'sequence is written from the settlement backwards — because what a stage fails to record '
         'is exactly what cannot be settled years later.',
    h_gd='The nine stages',
    l_viec='What happens', l_tq='Who decides', l_cc='Governing instruments',
    l_kq='What comes out', l_bay='Where it usually goes wrong',
    h_ngan='Four legal tracks — read the right one',
    ngan_lede='A metro project does not sit under one single set of rules. Which track applies '
              'decides which procedures may be shortened and which may not. Getting this wrong at '
              'the start is expensive to unwind.',
    l_pv='Scope', l_vb='Instruments',
    h_ho='Three places where the mechanism is still open',
    ho_lede='These are not oversights on our part. They are provisions that delegate a further '
            'document which has not yet been issued. Until it is, the matter cannot be quantified — '
            'and a project that assumes otherwise is building on air.',
    h_ke='Where the audit fits',
    ke='Stages 6 to 9 are where an auditor should already be present, not waiting at the end. '
       'See %s for why, and how the work divides.',
    ke_lk='Settlement audit',
)

# 9 giai doan: (ten, viec, tham quyen, can cu, ket qua, cai bay)
QT_GD = [
    ('Planning and route conception',
     'Bringing the line into the provincial plan and the urban master plan; fixing the alignment, '
     'station and depot locations; preparing the route option; provisionally delineating the TOD area.',
     'Provincial People’s Committee submits; Provincial People’s Council approves what falls within '
     'its authority',
     'Luật Quy hoạch đô thị và nông thôn 47/2024/QH15 · Luật Quy hoạch 112/2025/QH15 · '
     'Hanoi: NQ 64/2026/NQ-HĐND on underground space planning',
     'Approved route plan · route option · provisional TOD area boundary',
     'The alignment is drawn on a map but not staked on the ground, so site clearance later comes '
     'out misaligned. Underground space planning does not yet exist, so the vertical boundary of '
     'underground stations cannot be fixed.'),
    ('Investment policy decision',
     'Preparing the investment policy proposal or pre-feasibility study; appraising the funding '
     'source and the ability to balance capital; deciding the investment policy.',
     'National Assembly for projects of national importance · Prime Minister · Provincial People’s '
     'Council',
     'Luật Đầu tư công 58/2024/QH15 · NĐ 85/2025 (amended by NĐ 275/2025) · NĐ 19/2026 on appraising '
     'projects of national importance',
     'Resolution or decision on investment policy · preliminary total investment · funding structure',
     'Preliminary total investment is built on thin survey data, so the gap is wide when the project '
     'is actually prepared. Where the special mechanism waives this step, the settlement file is '
     'missing a link people expect to find — prepare the substitute evidence in advance.'),
    ('Project preparation, appraisal and approval',
     'Construction survey; feasibility study and basic design, or overall technical design under the '
     'special mechanism; appraisal by the competent technical authority; fire safety approval and '
     'environmental assessment.',
     'The investment decider under delegation; for projects under NQ 188 authority is strongly '
     'devolved to the province',
     'Luật Xây dựng 135/2025/QH15 · NĐ 209/2026 and NĐ 210/2026 · NĐ 206/2026 on cost management · '
     'VBHN 34/VBHN-BXD on overall technical design',
     'Project approval decision · approved total investment — this is the legal ceiling for every '
     'cost that will later be settled',
     'Underground quantities are where design and actual ground conditions diverge most. Projects '
     'prepared before 30 July 2026 had no dedicated metro standard and had to borrow foreign ones.'),
    ('Site clearance and resettlement',
     'Land recovery notice; inventory; preparing, posting and approving the compensation, support '
     'and resettlement plan; payment; handing over the site in tranches. Runs in parallel with '
     'stage 3.',
     'The People’s Committee with authority to recover land and approve the plan',
     'Luật Đất đai 31/2024/QH15 · NĐ 88/2024 · NĐ 102/2024 · NĐ 103/2024 · Hanoi, in TOD areas: '
     'NQ 66/2026/NQ-HĐND',
     'Land recovery decision for each parcel · approved compensation plan · site handover records',
     'The site is handed over in patches, so the contractor cannot organise a production line and '
     'claims standing-time costs. Payment records are missing signatures, and it only surfaces at '
     'settlement — by which time the recipients have moved away.'),
    ('Contractor selection and contract signing',
     'Preparing and approving the contractor selection plan; issuing bidding documents; evaluation; '
     'appraisal and approval of the result; negotiation and contract signing.',
     'The competent person and the investor under the Law on Bidding',
     'Luật Đấu thầu 22/2023/QH15 (amended by Luật 57/2024 and Luật 90/2025) · NĐ 214/2025 · '
     'for PPP: TT 98/2025/TT-BTC and TT 142/2025/TT-BTC',
     'Decision approving the selection result · contract, with its stated form of contract price',
     'The form of contract price written into the contract does not match how the parties actually '
     'pay — a lump-sum contract settled on measured quantities, or the reverse. This is the origin '
     'of most disputes at settlement.'),
    ('Construction, cost management and adjustment',
     'Subsequent design steps; preparing, appraising and approving estimates; construction; '
     'acceptance of quantities by stage; payment; handling variations and adjustments.',
     'The investor for estimates within the approved scope; the investment decider for project '
     'adjustments',
     'NĐ 206/2026 on cost management · NĐ 207/2026 on quality management · TT 36/2026, TT 37/2026, '
     'TT 38/2026 on norms and costs',
     'Approved estimates by work item · quantity acceptance records · as-built drawings · payment '
     'files by tranche',
     'Norms are the easiest thing to get wrong — the same work item carries different norms in '
     'different periods, and you must use the one in force when the estimate was prepared. '
     'Specialised work such as tunnelling and signalling has no domestic norm at all.'),
    ('Acceptance, trial running and system safety certification',
     'Acceptance of completed items; static and dynamic testing; integrated trial running of the '
     'whole system; system safety assessment and certification; State acceptance; operating licence.',
     'The investor carries out acceptance; the technical authority inspects the acceptance work; '
     'the sector regulator issues the operating licence',
     'Luật Đường sắt 95/2025/QH15 (consolidated text 75/VBHN-VPQH) · NĐ 16/2026 · '
     'TT 62/2026/TT-BXD metro technical regulation · VBHN 13/VBHN-BXD on connection to the national '
     'railway',
     'Completion acceptance records · trial running file · system safety certificate · decision to '
     'bring into operation',
     'This is the stage that overruns most often. Electricity, operating staff and insurance costs '
     'arise while the works are not yet handed over and earn no revenue — whether these are '
     'investment cost or operating cost is a question that must be settled in writing beforehand.'),
    ('Handover, asset recognition and entry into operation',
     'Handing the works and records to the operator; establishing ownership and assigning management '
     'of infrastructure assets; preparing asset records, declaration and depreciation; building the '
     'fare and subsidy plan.',
     'The authority assigning management of infrastructure assets; the provincial People’s Committee '
     'and Council for fares and subsidy',
     'NĐ 15/2025 on railway infrastructure assets · TT 75/2025/TT-BTC on depreciation · TT 34/2025 '
     'and TT 33/2025/TT-BXD · Luật Quản lý, sử dụng tài sản công 15/2017/QH14',
     'Handover records by receiving entity · list and value of assets formed through investment',
     'Handover first, valuation later — trains are running while asset values are not final, the '
     'operator books provisional figures, and everything has to be restated once settlement closes.'),
    ('Settlement of investment capital',
     'Closing and reconciling capital paid; preparing the settlement report; independent audit of '
     'the settlement report; verification; approval of settlement; resolving debts and surplus '
     'materials and equipment.',
     'The authority approving settlement under delegation; the finance authority leads verification',
     'NĐ 254/2025 (replacing NĐ 99/2021) · TT 147/2025/TT-BTC · TT 73/2026/TT-BTC on the system of '
     'forms · audit under VSA 1000',
     'Settlement report · independent audit report · verification report · settlement approval '
     'decision',
     'The file has passed through several generations of decrees; the people who prepared it have '
     'left; early-stage vouchers are lost. Costs not chargeable to asset value are suspended unless '
     'the competent authority has permitted them in writing.'),
]

# 4 ngan phap ly: (ma, ten, pham vi, van ban, mau)
QT_NGAN = [
    ('A', 'Hanoi / HCMC metro, public investment',
     'Located in Hanoi or Ho Chi Minh City',
     'NQ 188/2025/QH15 · Luật Đường sắt 95/2025/QH15 · VBHN 34/VBHN-BXD', 'ngoc'),
    ('B', 'Metro elsewhere, public investment',
     'Outside Hanoi and Ho Chi Minh City',
     'Luật Đường sắt 95/2025/QH15 · Luật Đầu tư công 58/2024/QH15 · Luật Xây dựng. '
     'NQ 188 may not be invoked', 'do'),
    ('C', 'Metro under a PPP',
     'Carried out under a PPP contract',
     'Luật PPP 64/2020/QH14 (consolidated text 81/VBHN-VPQH) · NĐ 243/2025 · NĐ 312/2025', 'nhan'),
    ('D', 'TOD area attached to the line',
     'The zone around stations and depots',
     'Luật Thủ đô 02/2026/QH16 · resolutions of the provincial People’s Council '
     '(Hanoi: NQ 71/2025, 66/2026, 67/2026 — HCMC: NQ 21/2026)', 'muc'),
]

# 3 cho ho: (ten, giai thich)
QT_HO = [
    ('Hanoi’s TOD advantage coefficient — not yet issued',
     'NQ 67/2026/NQ-HĐND Article 8 assigns the People’s Committee to submit the TOD advantage '
     'coefficient and the percentage rates to the People’s Council, once the TOD area plan is '
     'approved. That resolution has not been issued. Without it, the four TOD revenue streams '
     'cannot be converted into money.'),
    ('Hanoi’s underground connection fee — not yet issued',
     'NQ 65/2026/NQ-HĐND Article 3.2 assigns submission of the underground connection fee once the '
     'underground space plan is approved. Until that document exists, the connection obligation of '
     'neighbouring buildings tying into an underground station cannot be determined.'),
    ('Decree detailing Luật Thủ đô 02/2026 — not found',
     'QĐ 762/QĐ-TTg is the implementation plan for Luật Thủ đô 39/2024, issued before the new law '
     'existed. We have found no replacement decision for Luật 02/2026, and no detailing decree.'),
]

# =================================================================== KIEM TOAN QT
KT = dict(
    td='Audit of the settlement report of a completed project',
    mt='Thirteen workstreams, two balance checks and why a large metro project should be audited '
       'in parallel with construction rather than only at the end.',
    duong='Settlement audit',
    h1='Auditing the settlement report of a completed project',
    lede='On a metro line the audit should not wait for the ribbon-cutting. A line takes eight to '
         'fifteen years; evidence that is not seen at the moment it exists cannot be recovered '
         'afterwards. This page sets out what the audit covers, and why on a project of this size '
         'the work runs alongside construction.',
    h_sh='Parallel auditing — what it means',
    sh='Auditing in parallel means the auditor comes in during construction, in tranches, rather '
       'than once at the end. Each tranche closes a stage or a package; the final tranche '
       'consolidates. It is not a different standard of audit — it is the same work, placed where '
       'the evidence still exists.',
    h_vs='Five reasons a large project has to be audited in parallel',
    h_ss='The two approaches, side by side',
    ss_cot=('', 'Audit after completion', 'Audit in parallel'),
    h_ph='Thirteen workstreams',
    ph_lede='The index follows the VACPA model audit file for settlement reports of completed '
            'projects (QĐ 314-2016/QĐ-VACPA). The numbering is the file index, not the working '
            'order.',
    h_cd='Two balance checks before issuing',
    cd_lede='These two checks run on the same set of figures. If they do not balance, the report is '
            'not issued.',
    h_kl='Three things an auditor does not do',
    h_phi='Audit fee — calculate it now',
    phi_1='Under <b>Nghị định 193/2026/NĐ-CP, Article 20</b>, in force from 1 July 2026. Enter the '
          'value to be audited and the fee appears.',
    phi_2='These rates are <b>unchanged</b> from Nghị định 254/2025/NĐ-CP Article 45 — we checked '
          'every figure. The new decree only renumbers the article.',
    l_gt='Value to be audited',
    l_gt_phu='The value proposed for settlement, or total investment where no settlement figure '
             'exists yet',
    l_dv='Unit', l_ty='Billion VND', l_tr='Million VND', l_d='VND',
    l_vat='Value added tax', l_kvat='Not applied',
    tick_tb='<b>Equipment cost is 50% or more</b> — point d, clause 1, Article 20: the fee is '
            '<b>70%</b> of the normal level',
    tick_bt='<b>This is compensation, support and resettlement cost</b> — point đ: the fee is '
            '<b>50%</b> of the normal level',
    tick_kt='<b>Already audited independently, or by the State Audit or an inspection</b> — point e: '
            'the <b>verification</b> fee alone is <b>50%</b>',
    kq_gt='Value used for the fee', kq_ty='Rate applied', kq_hs='Adjustment factor',
    kq_truoc='Audit fee before tax', kq_vat='Value added tax',
    kq_nhan='Maximum audit fee', kq_phu='Value added tax included',
    kq_tt='Settlement verification and approval fee',
    kq_tt_ghi='This charge is collected by the verifying authority — it is not a fee paid to the '
              'auditor, and no value added tax is added to it.',
    kq_loi='Please enter a value greater than zero.',
    kq_toi='* The minimum of 1 million VND under point b, clause 1, Article 20 has been applied.',
    h_bang='The rate table',
    bang_gt='Value (billion VND)', bang_kt='Independent audit (%)', bang_tt='Verification (%)',
    bang_ghi='A value between two thresholds is interpolated linearly under point a, clause 1, '
             'Article 20: <code>Ki = Kb − (Kb − Ka) × (Gi − Gb) ÷ (Ga − Gb)</code>. '
             'The calculator above already does this.',
    h_nho='Four things to remember about this figure',
    nho='<b>One —</b> this is a <b>maximum</b>, not the price you must pay. A package price may be '
        'lower, and in competitive tendering usually is.<br><br>'
        '<b>Two —</b> the minimum audit fee is <b>1 million VND</b> plus tax; the minimum '
        'verification fee is <b>500 thousand VND</b>.<br><br>'
        '<b>Three —</b> the audit fee <b>carries value added tax</b>; the verification fee does not.'
        '<br><br>'
        '<b>Four —</b> this figure is a <b>basis for estimating a package</b>. The fee on an actual '
        'engagement also depends on the volume of records, the number of packages, the location and '
        'the time available.',
    h_sh2='How it works on a project audited in parallel',
    sh2='The rate applies to the <b>value to be audited for the project as a whole</b>, not to the '
        'sum of the tranches. Splitting the work into tranches is a way of organising it, not a way '
        'of multiplying the fee.',
    sh3='In practice the total cost of a parallel engagement is higher than a single-tranche rate, '
        'because the work genuinely is greater — more site visits, more working minutes. That '
        'difference is agreed in the contract and must be accepted by the competent authority.',
    h_bt='If you are weighing up the approach for your own project',
    bt='Whether to audit after completion or in parallel depends on the size of the project, its '
       'duration and the number of packages. Send the details through the %s page and we will give '
       'our view on the approach and the likely volume of work.',
    bt_lk='Advice',
)

KT_VS = [
    ('Early-stage records no longer survive intact',
     'A metro line runs eight to fifteen years. Wait until completion and the vouchers from the '
     'early years have faded, the signatories have moved on, subcontractors have been wound up. The '
     'auditor cannot find evidence — and without evidence there is no opinion.'),
    ('Underground quantities have been covered up',
     'Reinforcement before the concrete pour, tunnel support before the lining goes on — these can '
     'be seen exactly once, at the moment of construction. Afterwards they cannot be measured again '
     'however much anyone wants to. An auditor arriving later has nothing but the file.'),
    ('An error found late can no longer be corrected',
     'A cost lacking a decision of the competent authority can be regularised if it is found in the '
     'year it arises. Found seven years later, the person who held that authority has retired, and '
     'their successor will not sign for something they did not oversee.'),
    ('Leaving the work to the end drags the settlement out',
     'A project of several thousand billion has tens of thousands of vouchers. Put them all into one '
     'final audit and simply sorting the file takes months before any checking begins. Split by '
     'stage, each tranche is manageable and later tranches inherit the earlier work.'),
    ('The investor learns where it is going wrong while there is still time',
     'This is the greatest value. Auditing in parallel is not only about detection; it is so the '
     'investor can change how files are prepared from the very next package. A note raised in '
     'year two saves months in year ten.'),
]

KT_SS = [
    ('Starting point', 'After the works are complete',
     'From the construction stage, in tranches'),
    ('How the work divides', 'A single pass over the whole project',
     'Several tranches by stage or by package, with a consolidating final tranche'),
    ('Audit evidence', 'Paper records only; concealed work cannot be checked',
     'Direct observation of work about to be covered up, and physical counts on site'),
    ('When an error is found', 'Usually too late to complete the file',
     'Time remains for the investor to regularise it or seek a ruling'),
    ('Settlement duration', 'Long, because records from years back must be reconstructed',
     'Shorter, because most of it has already been checked and agreed'),
    ('Audit cost', 'Lower on a single engagement, but a higher risk of the file being suspended',
     'Higher in total, in exchange for less risk and a shorter settlement'),
    ('Suits', 'Small projects running under two years',
     'Group A projects, projects of national importance, multi-package projects, ODA projects'),
]

KT_PH = [
    ('1000', 'Audit planning',
     'Client acceptance and engagement risk assessment · understanding the project and its internal '
     'control · preliminary analysis of the settlement report · setting materiality and the sampling '
     'method · the overall audit plan.',
     'Set materiality wrongly and every sample size downstream is wrong with it.'),
    ('3000', 'Project legal file',
     'Reconciling the legal file against what the rules require · checking approval authority · '
     'assessing compliance with the investment and construction sequence, the contractor selection '
     'sequence and contract signing.',
     'Where a special mechanism is applied, you must first prove the project falls within its scope '
     'before accepting any shortened step.'),
    ('4000', 'Sources of investment capital',
     'Checking balances and movements of each source · reconciling capital paid between the investor '
     'and the paying authority · checking increases, decreases and how they were recorded.',
     'This is where discrepancies most often appear — and the easiest one to keep clean if it is '
     'reconciled every year.'),
    ('5100', 'Compensation, support and resettlement cost',
     'Reconciling against the approved compensation plan · checking through to the compensation '
     'decision of the competent authority · the payment summary · payment vouchers and recipients’ '
     'confirmations.',
     'A payment record missing a signature is close to impossible to complete, because the recipient '
     'has moved away.'),
    ('5200', 'Construction cost',
     'Reconciling the A–B settlement against the settlement report · checking quantities and unit '
     'rates according to the actual form of contract price · reconciling acceptance records and '
     'quality management files · checking settlement of variations.',
     'The largest workstream. Applying the checking method of one form of contract price to another '
     'is the most common error of all.'),
    ('5300', 'Equipment cost',
     'Reconciling the contract settlement · checking the list, type, origin, quality and '
     'configuration of equipment against the estimate and the contract · checking settlement of '
     'variations.',
     'On a metro, equipment is a very large share and mostly imported — the conversion rate must be '
     'checked as well.'),
    ('5400', 'Materials and equipment supplied by the investor',
     'Consolidating receipts, issues and stock · checking receipts for quantity, certificates of '
     'origin and quality, and unit rates · checking issues to each contractor for installation.',
     'An unexplained gap between receipts, issues and stock is a signal to widen the scope of '
     'testing.'),
    ('5500', 'Project management, consultancy and other costs',
     'Reconciling against the approved total estimate · checking costs the investor carried out '
     'itself, including procurement and project management unit payroll · checking costs incurred by '
     'consultants.',
     'These must be recomputed on the norms in force at the time they applied, not on current norms.'),
    ('6000', 'Costs not chargeable to asset value',
     'Two groups: losses from force majeure that may be excluded, and costs that create no asset. '
     'Checking the nature and amount of the loss against the decision of the competent authority, '
     'and that authority’s competence.',
     'Without a decision permitting it, the amount is suspended and cannot be settled.'),
    ('7000', 'Value of assets formed through investment',
     'Consolidating long-term and short-term assets · the policy for allocating common costs · '
     'classification by funding source and by user · transfer decisions and handover records · '
     'residual value of the project management unit’s own assets.',
     'On a metro the assets go to several different receiving entities, so the schedule has to be '
     'split clearly from the outset.'),
    ('8000', 'Debts and surplus materials and equipment',
     'Checking receivable and payable balances by contractor · confirming balances by circularisation '
     'controlled by the auditor · checking cash and bank balances · checking receipts, issues and '
     'stock of surplus materials and equipment.',
     'The auditor must control both the sending and the receiving of confirmations — never leave it '
     'to the investor.'),
    ('9000', 'The investor’s compliance record',
     'Reviewing compliance with investment and construction rules · compliance with accounting and '
     'settlement requirements · and implementation of the conclusions of inspections and the State '
     'Audit.',
     'A large project has almost certainly been through at least one inspection — skip this and the '
     'report will contradict the findings of a State body.'),
    ('2000', 'Consolidation, review and issue',
     'Consolidating results and checking the balance of figures · consolidating proposed adjustments '
     '· listing matters not agreed · the investor’s representation · the closing meeting record · '
     'review at each level · approval to issue.',
     'The balance equations must run before issue — if they do not balance, the report is not '
     'issued.'),
]

KT_CD = [
    ('Sources against costs',
     'Total investment capital (4000) ≈ Total investment cost proposed for settlement (5000)',
     'A difference means either capital has not been recognised, or a cost has no source behind it.'),
    ('Costs against asset value',
     'Investment cost (5000) − Not chargeable to asset value (6000) − Surplus materials and equipment '
     '(8200) = Value of assets formed (7000)',
     'This is the last check before issue. A difference of one dong still has to be traced.'),
]

KT_KL = [
    ('We do not audit while acting as consultant on the same project',
     'Preparing a file and then checking the file you prepared destroys independence. This is a '
     'prohibition; no safeguard cures it.'),
    ('We do not prepare the file on the investor’s behalf',
     'The auditor points out what is missing, but the investor must prepare and sign the file. '
     'Doing it for them erases the boundary of responsibility.'),
    ('We do not give an opinion without sufficient evidence',
     'Where evidence is lacking we say so and state the effect, rather than inferring a figure to '
     'make the report look complete.'),
]
