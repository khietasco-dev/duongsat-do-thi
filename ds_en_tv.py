# -*- coding: utf-8 -*-
"""Ban TIENG ANH: trang TU VAN (request advice) va LIEN HE (contact)."""

# =================================================================== TU VAN
TV = dict(
    td='Request advice on an urban railway project',
    mt='Describe what your project is stuck on. We read it, classify it and reply within 24 working '
       'hours — three kinds of request, each with its own turnaround.',
    duong='Advice',
    h1='Request advice',
    lede='Describe what the project is stuck on. We read it, classify it and reply within 24 working '
         'hours.',
    h_ba='Three kinds of request we take',
    ba=[
        ('Quick answer', 'A single specific question',
         'One clear question about a legal basis, a procedural sequence, or how to treat a '
         'particular cost. This kind is usually answered in the first reply.',
         'Turnaround: <b>within 24 working hours</b> · No charge'),
        ('Needs the file', 'A problem with several strands',
         'A situation touching several instruments, several dates, or requiring the contract and '
         'acceptance records to be read together. We give a preliminary answer first, then arrange '
         'a discussion if needed.',
         'Turnaround: <b>2 to 3 working days</b> · A confidentiality undertaking may be required'),
        ('Becomes an engagement', 'Reviewing the whole project file',
         'Reviewing the complete file before it goes for settlement, or reconstructing the map of '
         'which instruments applied when, for a project that has run many years. This has its own '
         'scope and timetable.',
         'Turnaround: <b>as agreed</b> · Under a service contract'),
    ],
    h_dv='Nine services we can take on',
    dv_lede='Beyond answering questions, we take on nine pieces of work around the financial and '
            'governance side of an urban railway project. Each card explains what we do, on what '
            'basis, and what you receive.',
    dv_ghi='All nine fall under Clause 2, Article 40 of the Law on Independent Audit and must pass '
           'an independence check before signing — the detail is on the %s page.',
    dv_lk='Services',
    h_mau='The form',
    f_ten='Full name', f_cv='Position', f_dv='Organisation', f_dt='Telephone', f_em='Email',
    f_db='Project location', f_gd='Which stage is the project at', f_nh='Type of problem',
    f_loai='Kind of request', f_mo='Describe the situation',
    f_chon='— Select —',
    f_mo_gy='What the project is stuck on · what has been tried · what help is needed · whether '
            'there is a deadline to meet',
    f_gui='Send request',
    f_bb='required',
    db=['Hanoi', 'Ho Chi Minh City', 'Elsewhere'],
    gd=['Route planning', 'Investment policy', 'Preparation, appraisal and approval',
        'Site clearance', 'Contractor selection', 'Construction', 'Acceptance and trial running',
        'Handover and asset recognition', 'Settlement of investment capital'],
    nh=['Investment procedure', 'Site clearance', 'Contract and payment',
        'Acceptance and as-built records', 'Settlement of investment capital',
        'TOD and land exploitation', 'Underground space', 'Training and technology transfer',
        'Other'],
    loai=['A single specific question', 'A problem with several strands',
          'Reviewing the whole project file'],
    h_nen='What to include in the description',
    nen=[
        'Where the project is — Hanoi and Ho Chi Minh City have their own mechanism; elsewhere does '
        'not',
        'The funding source: public investment, ODA or PPP',
        'The date of the matter in question — instruments apply according to when the event arose',
        'Whether any decision of a competent authority already exists on the point',
        'Whether there is a deadline to meet, for example a verification submission date',
    ],
    h_bm='What happens to what you send',
    bm='We treat everything you send as confidential. We do not name your project or your '
       'organisation in any public material. Where a question becomes a general lesson worth '
       'publishing, we rewrite it so that no project can be identified.',
    h_kh='What we cannot answer',
    kh='We do not give a legal opinion — an audit firm may not provide legal services. We do not '
       'comment on the work of another auditor or consultant on a project we have not examined. And '
       'we do not give an opinion on a question that turns on documents we have not read.',
)

# =================================================================== LIEN HE
LH = dict(
    td='Contact ASCO — urban railway projects',
    mt='Three ways to reach us: the advice form, a phone call, or a scheduled discussion. Each suits '
       'a different kind of matter.',
    duong='Contact',
    h1='Contact',
    lede='Three ways to reach us, each suited to a different kind of matter. Choosing the right one '
         'gets you a faster answer.',
    h_ba='Three ways to reach us',
    ba=[
        ('Best for most', 'Send the advice form',
         'This gives us enough context to answer properly, so the reply is usually usable straight '
         'away instead of starting a chain of questions.',
         'Reply: <b>within 24 working hours</b>', 'Open the advice form →'),
        ('Urgent', 'Call us',
         'Suits a matter with a deadline in the next few days, or a quick point you need settled '
         'before deciding.',
         'Office hours: <b>Monday to Friday, 08:00 – 17:30</b>', None),
        ('Complex', 'Schedule a discussion',
         'For a project stuck in several places at once, one conversation usually achieves more than '
         'a long exchange of letters. Online or at your own offices.',
         'Length: <b>60 to 90 minutes</b>', None),
    ],
    dt_ghi='This number also works on <b>Zalo</b> — message outside office hours and we read it '
           'first thing in the morning.',
    dl_ghi='To schedule, either message <b>Zalo 08 2509 2007</b> or complete the %s and choose the '
           'request type <b>“A problem with several strands”</b>.',
    dl_lk='advice form',
    h_ts='Head office',
    ts_ten='ASCO Auditing and Valuation Firm',
    ts='ASCO Building, No. 2, Lane 308, Le Trong Tan Street, Phuong Liet Ward, Hanoi<br>'
       'Telephone and Zalo: <b>08 2509 2007</b>',
    h_tt='Online works too',
    tt='For organisations outside Hanoi, most discussions are held online — it is quicker and nobody '
       'has to travel. We send the meeting link once the time is fixed. If you would rather meet at '
       'your own offices, say so when scheduling and we will arrange for someone to come.',
    h_chon='Which way for which matter',
    chon_cot=('Your matter', 'Use', 'Why'),
    chon=[
        ('A single question about a legal basis', 'The form',
         'A written answer citing document numbers, which you can keep'),
        ('A verification deadline is close and you need an answer now', 'Call',
         'No waiting on an exchange of letters'),
        ('The project is stuck in several places and you do not know where to start', 'Schedule',
         'It needs an overall view; correspondence will not get there'),
        ('You want the whole file reviewed before settlement', 'The form, third option',
         'This has its own scope and needs to be agreed first'),
        ('Feedback on the content of this site', 'The form',
         'We correct it and record where the correction came from'),
    ],
    h_fa='Questions people ask before getting in touch',
    fa=[
        ('Is there a charge?',
         'Not for answering a specific point. Reading a file, or reviewing a whole project file, is '
         'work with its own scope and timetable, agreed between us before it starts.'),
        ('I am not with a project management unit — can I still ask?',
         'Yes. This site serves project management unit staff, investors, consultants and '
         'contractors. Please say what your role on the project is so we answer from the right '
         'angle.'),
        ('My project is not an urban railway — does that matter?',
         'Much of the content applies to any public investment project, particularly on settlement. '
         'Say what kind of project it is and we will tell you which parts carry over and which do '
         'not.'),
        ('Which language do you reply in?',
         'Vietnamese or English. Where the answer turns on the wording of a legal instrument we give '
         'the Vietnamese text as well, because only that text is authoritative.'),
    ],
    h_bm='Confidentiality',
    bm='We treat what you send as confidential and do not name your project or organisation in '
       'public material. Where a question becomes a general lesson worth publishing, we rewrite it '
       'so that no project can be identified.',
)
