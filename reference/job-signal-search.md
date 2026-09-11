# Job-post signal search — the A1 sourcing spec

*The metadata that builds the prospect pool for A1 personalised cold outreach. Load this
before running a jobs search. Channel method stays in `outbound-engine.md`; this file only
decides who enters the pool.*

`last_reviewed: 2026-09-11`

## The signal

An agency posting a job is telling us three things it would never tell us in an email: it
has more inbound volume than the people it has, it has decided the fix is a person, and it
has a budget line open right now.

Two posts carry the signal most sharply, and they are not the same post.

**Hiring a licensed agent** means the book is growing past the owner's capacity. That is
ICP-1 stage 1, "we're missing calls we can't afford to miss", with a date on it.

**Hiring a front desk, client services or seasonal AEP role** is the stronger of the two.
They are hiring a human to answer the phone and field plan questions. That is the job our
front line does, priced against a salary rather than against a competitor.

It is also the one we can only partly reach. This signal is sourceable only where the
title itself carries Medicare, because the bare versions of those titles return the whole
labour market. Treat what the search returns as a floor on how often it occurs.

A third signal sits on top of both and costs nothing to capture: a role reposted two or
three times, or open more than 45 days. They tried to hire the human and could not. That
is the agency to run the Gap Report on first.

## Structure: one pass, and the title carries the whole filter

The two-pass design this file used to carry is withdrawn. Pass B paired generic titles
with a Medicare description keyword, on the assumption that the keyword would gate the
title. It does not. Generic titles return the entire labour market, and "Customer Service
Representative" returns U-Haul and Stripe before it returns a single agency.

The correction is a rule, not a tuning:

**Every title in the include list must be one that a non-insurance employer could not
post.** If a logistics company or a payments company could plausibly use the title, it is
out, whatever the description field says. There is no keyword that repairs a title with no
ICP signal in it.

The description field is the second half of that failure. A large employer's posting
mentions Medicare in benefits and eligibility boilerplate, so the keyword matches
companies that have nothing to do with the market. Leave it empty.

The cost is real and it is the right trade. The answer-the-phone cluster, the front desk
and client services roles that were the highest-intent signal in the previous version, do
not survive at the title level. They come back only where the title also carries Medicare
or insurance, and the bare versions are gone.

## Job titles to include — Medicare in the title

The core list. No non-insurance employer posts any of these.

```
Medicare Agent, Medicare Sales Agent, Licensed Medicare Agent, Medicare Insurance Agent,
Medicare Sales Representative, Medicare Advisor, Medicare Insurance Advisor, Medicare
Broker, Medicare Insurance Broker, Medicare Specialist, Medicare Sales Specialist,
Medicare Benefits Advisor, Medicare Sales Consultant, Medicare Consultant, Medicare
Account Executive, Medicare Producer, Medicare Enrollment Specialist, Medicare Enrollment
Advisor, Medicare Customer Service Representative, Medicare Client Services
Representative, Medicare Account Manager, Medicare Sales Manager, Medicare Agency Manager,
Medicare Advantage Agent, Medicare Advantage Sales Agent, Medicare Advantage Sales
Representative, Medicare Supplement Agent, Medigap Agent, Medicare Part D Agent
```

Two of these carry provider-side drift rather than employer-side drift. Health systems and
clinics use "Medicare Specialist" and "Medicare Enrollment Specialist" for patient
eligibility work. The exclusion list below removes them by the second word in the title.

## Job titles to include — senior market

The segment's own language for the same roles, for agencies that do not put Medicare in
the title.

```
Senior Market Agent, Senior Market Advisor, Senior Market Sales Agent, Senior Market
Specialist, Senior Products Agent, Senior Benefits Agent
```

Only titles where "senior" cannot be read as seniority belong here. "Senior Benefits
Advisor", "Senior Insurance Advisor" and "Senior Health Insurance Agent" are all common
corporate titles about experience level, and each one reopens exactly the drift this
version removes. They stay out.

## Job description keywords

**Leave empty.** On both lists above the title has already done the qualifying, and any
keyword added here only subtracts from a pool that is already precise.

## Job titles to include — volume extension, off by default

Turn this on only if the core lists come back too thin to work, and understand what it
gives up.

```
Licensed Insurance Agent, Licensed Insurance Sales Agent, Insurance Sales Agent, Insurance
Agent, Insurance Producer, Insurance Broker, Health Insurance Agent, Licensed Health
Insurance Agent, Life and Health Insurance Agent, Health Insurance Advisor, Insurance
Customer Service Representative, Insurance Account Manager
```

These are insurance-exclusive, so they do not return the labour market at large. They also
do not prove Medicare. The agency in the result may sell property and casualty, life, or
group benefits, and the list reopens the 1099 recruiting volume that the final expense and
mortgage protection operations generate.

Run it as a separate search with its own table, never merged into the core pool, so the
two can be measured against each other before anything is sent.

## Job titles to exclude

With Medicare-bounded titles the drift is no longer U-Haul. It is the wrong side of this
same market: providers, payers and back office. That makes the list shorter and sharper
than the previous version.

```
Patient, Clinical, Nurse, Registered Nurse, RN, LPN, LVN, Case Manager, Care Manager, Care
Coordinator, Care Navigator, Social Worker, Home Health, Hospice, Pharmacy, Pharmacist,
Billing, Biller, Coder, Coding, Revenue Cycle, Claims, Utilization Review, Utilization
Management, Prior Authorization, Credentialing, Provider Relations, Provider Network,
Network Development, Underwriter, Underwriting, Actuary, Actuarial, Risk Adjustment,
HEDIS, Stars, Auditor, Data Analyst, Business Analyst, Software Engineer, Developer,
Recruiter, Talent Acquisition, Trainer, Intern, Internship
```

Add this second block only when the volume extension above is running. On the core lists
it is inert, because nothing matching "Medicare Agent" also matches "Real Estate Agent".

```
Real Estate, Leasing, Travel Agent, Freight, Booking Agent, Reservation, Ramp Agent, Gate
Agent, Dispatcher, Auto, Property, Casualty, Personal Lines, Commercial Lines, Workers
Compensation, Mortgage, Loan Officer, Financial Advisor, Financial Planner, Wealth,
Final Expense, Mortgage Protection, Annuity
```

## What no keyword can do

The title lists above return Medicare roles at Medicare organisations. They do not return
only agencies, and no string in this panel can, because the organisations that are not
agencies use the same titles.

Carriers post "Medicare Sales Agent". So do national call centres, Field Marketing
Organisations recruiting downline, and staffing firms. They are inside the vertical, they
use the vertical's vocabulary, and they post at a volume that buries the real pool.

That separation is a company-level filter, and it is unavoidable. What it does not have to
be is a recurring cost. Set it once, as described below, and every later run inherits it.

## Location

**Cities, states, or countries to include:** `United States`

**Cities, states, or countries to exclude:** leave empty.

Do not filter to the dense states. ICP-1 is densest in FL, TX, AZ, CA, PA, OH, NC and MI,
but that is a ranking input, not a boundary, and eight states would cut the pool by more
than half for no gain in fit. Carry the state as a column and sort on it.

## Has recruiter — leave it off

The toggle filters to posts where a recruiter or hiring contact has been identified and
attached. Confirm that reading on one run before relying on it, because the label is the
only evidence of what it does.

Off is right for A1, and the reason is the ICP rather than the pool size.

An ICP-1 agency has 3 to 10 licensed agents and 1 to 2 admin, no marketing hire and no ops
hire. There is no recruiter in the building. The owner writes the post, and the owner is
also the top producer and the person who signs. So a recruiter attached to a Medicare job
post is a size signal, and it points the wrong way: a talent function exists, which means
the company is a carrier, a national call centre, a Field Marketing Organisation or a
staffing firm. That is the exclusion list, not the pool.

On also costs coverage on top of fit. Any "has X" toggle drops every post the provider
could not enrich, and enrichment on small local employers is thin. The pool gets cut
twice, once for company size and once for data coverage, and both cuts land on the ICP.

### The contact it returns is the wrong contact

This holds separately from the size argument, and it holds even where the enrichment is
good.

A1 goes to the owner. In ICP-2 the true buyer is the Director of Operations and the
principal signs. A recruiter is neither, in either track. Their incentive also runs
against ours specifically: they are paid to fill the seat, and our argument is that the
seat costs more than the coverage does. Of everyone in that building, the recruiter is the
one person whose job our product argues against.

### Two ways to use it without filtering on it

Keep it as a column rather than a gate.

**Harvest the exclusion list with it on.** Run one pass with the toggle on and nothing else
changed. The companies that come back are close to the company-exclusion list below, built
from live data in twenty minutes instead of from memory. Then turn it off.

**Route on it.** Recruiter present is a rough ICP-1 and ICP-2 splitter. Agent recruiting is
a core Field Marketing Organisation function, so an FMO or General Agency post usually
carries a recruiter and a four-agent agency in Ocala never does. Hits go to B1, misses go
to A1.

### The test that decides which of those applies

On a small agency post the attached hiring contact is sometimes the owner rather than a
recruiter, and that changes the answer. Run the toggle on over one sample and read the
titles that come back.

| What the titles say | What the field is | What to do with it |
|---|---|---|
| Recruiter, Talent Acquisition, HR | A company-size proxy | Keep it off, use it inverted as above |
| Owner, Principal, Agency Manager | Decision-maker enrichment on ICP-sized companies | Keep it off, but carry the contact as a column into the outreach step |

Neither outcome makes it a filter. In the second case the posts it misses are not
disqualified, they are just missing a contact we can find another way.

## What the panel cannot do, and what has to happen after import

The search returns jobs. The ICP is a company, so three filters have to run on the
imported table before a single Gap Report is spent.

**Headcount band.** ICP-1 is 3 to 10 licensed agents plus 1 to 2 admin. Filter company
headcount to 2 to 50, and treat 3 to 25 as the core. Small agencies undercount themselves
on every data source, so a hard ceiling at 10 throws away real prospects.

**Company exclusions by name.** Paid once, inherited by every run afterwards. This is the
filter the title lists cannot be, and the four groups it removes are all inside the
vertical.

Carriers and their captive sales arms:

```
UnitedHealthcare, UnitedHealth Group, Optum, Humana, Aetna, CVS Health, Elevance Health,
Anthem, Wellpoint, Centene, WellCare, Cigna, Kaiser Permanente, Molina Healthcare, Devoted
Health, Clover Health, Alignment Healthcare, SCAN Health Plan, Highmark, Health Care
Service Corporation, Blue Cross, Blue Shield, BCBS, CareSource, Priority Health,
Healthfirst, EmblemHealth
```

National direct-to-consumer call centres and lead aggregators:

```
eHealth, GoHealth, SelectQuote, Assurance IQ, HealthMarkets, Spring Venture Group,
TogetherHealth, TZ Insurance Solutions, HealthPlanOne, Connie Health, Chapter
```

Field Marketing Organisations and General Agencies. These are routed rather than binned,
per the note below:

```
Integrity Marketing Group, AmeriLife, Senior Market Sales, Ritter Insurance Marketing,
Agent Pipeline, Berwick Insurance, Pinnacle Financial Services, Precision Senior Marketing,
The Brokerage Inc
```

Captive networks and the 1099 recruiting operations:

```
State Farm, Allstate, Farmers Insurance, Goosehead Insurance, Freeway Insurance, Family
First Life, Symmetry Financial Group, Globe Life, American Income Life, Primerica, Bankers
Life, New York Life, Combined Insurance, Aflac, Colonial Life, Robert Half, Aerotek,
Randstad, Adecco, Kelly Services
```

Treat that as a starting list to verify rather than a finished one. Extend it after the
first run from the top 50 companies by post count, because post volume identifies the
wrong companies in this market almost perfectly: an agency with six agents posts one job,
and everything posting forty is out of profile.

The cheapest way to build the extension is the recruiter toggle above. Run one pass with
it on, take the company names, add them here, turn it off.

**Route rather than discard.** A Field Marketing Organisation or General Agency hit is not
noise, it is ICP-2. Send it to the B1 LinkedIn track and title-verify it there. The two
tracks never merge, so it must not enter the A1 sequence.

## Who to contact inside the company

The job search returns a company. The Gap Report goes to a person, and in ICP-1 that is
one person.

**The owner, on the first touch, and nobody else.** ICP-1 has no committee. The owner
decides, is usually also the top producer, and is the person who answers the hard plan
questions personally. There is nobody to route around and no consensus to build.

The consultative framing makes that sharper rather than softer. The Gap Report is a finding
about a licensed entity: their line, in their agency's name, failing a question a
beneficiary asked. Everyone in that building can read it. One person owns the exposure in
it, and that is the principal broker.

### Titles to include — primary

```
Owner, Agency Owner, Owner and Agent, Founder, Co-Founder, President, Principal, Principal
Broker, Broker Owner, Managing Broker, Managing Partner, Partner, Agency Principal,
Managing Director, Chief Executive Officer, CEO, Proprietor
```

### Titles to include — verify before sending

At this company size the owner often describes themselves by what they do rather than by
what they own.

```
Independent Insurance Agent, Independent Insurance Broker, Independent Broker, Independent
Medicare Broker, Insurance Broker, Medicare Broker, Licensed Insurance Broker
```

Every one of these is also what an employee at the same agency is called. They qualify only
once one of the owner tests below passes. Sending to an unverified one puts the offer in
front of Level 1, which is the worst available outcome and the subject of the next list.

### Titles to exclude on the first touch

```
Licensed Insurance Agent, Medicare Agent, Medicare Sales Agent, Sales Agent, Producer,
Sales Representative, Account Executive, Customer Service Representative, Client Services
Representative, Enrollment Specialist, Receptionist, Administrative Assistant, Marketing
Coordinator, Marketing Manager, Recruiter, Talent Acquisition, Intern
```

These are Level 1 of the buying committee. They hold no formal influence and a real veto,
and the documented reason they block is fear of replacement.

An audit of the phone line they personally answer reads to them as a business case for
removing their job. It hands the one person who can quietly kill the deal a motive to. This
list is the most important one in this section.

### The fallback tier, and when it applies

```
Agency Manager, Operations Manager, Director of Operations, Office Manager, General
Manager, Operations Lead, Business Manager
```

Two cases only: no owner is identifiable after the tests below, or the agency sits at the 8
to 10 agent end where a real operations hire exists. This is Level 2, which shapes the
shortlist and runs the trial. A good second best and a poor default.

### One contact per company

Not two. In a five-person agency the owner and the office manager sit in the same room and
compare notes, so two near-identical approaches in one week reads as a sequence rather than
as a person. It also costs the sending domain for no gain.

### Finding the owner when the title does not say so

Titles at this size are unreliable in both directions. Six tests, cheapest first.

| Test | What it catches |
|---|---|
| Seniority filter set to owner, founder, partner or C-suite | The straightforward majority |
| Surname appears in the company name | High precision at this size. Smith Insurance Group, and a John Smith |
| The contact attached to the job post | At a four-agent agency the person hiring is the person who signs |
| Only profile at the company without an agent or service title | Works where the team page is thin |
| Start date matches the company founding year | Separates the founder from a long-tenured producer |
| Named as principal or broker of record on the agency website | Slowest, and the only one that also confirms the licence |

The second test is the one that pays. Independent agencies are named after their owners far
more often than software companies are.

### What raises reply odds inside the owner tier

Rank the owners, do not just collect them. Three things move the reply rate, and all three
come from work already done in this file.

An owner whose agency has two or more roles open is scaling past their systems. An owner
named directly on the job post has already put their name to the capacity problem. An owner
whose own line failed the Gap test on a plan they actively sell is the one who cannot put
the finding down.

### The sanity gate: people found should approximate companies in

A people search is scoped by company, not by job. It returns every person at each company
who matches the filters, so one large employer in the input contributes thousands of rows
on its own and the count stops being a count of prospects.

**The target is one person per company.** Eighty-one companies should return something near
eighty-one people, and realistically fewer once coverage gaps are allowed for. A result
that is a multiple of the company count is not a large pool, it is a broken input, and the
multiple names the problem.

| People returned against companies in | What it means |
|---|---|
| Roughly one to one | Working as intended |
| Two or three times | Several owners per agency, or the per-company cap is unset |
| Hundreds of times | Enterprises in the company table. Stop and fix the table |

Cap results per company at one where the panel offers it. Where it does not, deduplicate on
company in the table and keep the highest-ranking owner-tier title.

The failure is always upstream. The people search inherits whatever the company table holds
and multiplies it, so an enterprise that survived the job-layer filters does not add one bad
row here, it adds several thousand. Apply the company exclusion list and the headcount
ceiling to the jobs table before it feeds a people search, never after.

A headcount ceiling of 50 is the single filter that enforces this structurally. No carrier,
health system or platform company survives it, and no ICP-1 agency is excluded by it.

One cost that is not measured in rows: an outreach asset built for a 5-agent agency,
arriving at a health plan chief executive or a former regulator, is read by exactly the
people whose opinion this market takes seriously.

### The ICP-2 branch

If the company routing step sent the account to ICP-2, this entire section is void. The B1
target is the Director of Operations first and the principal second, and the two tracks
never merge. An ICP-2 prospect reached with an ICP-1 approach is a prospect spent.

## Scoring columns, built from the job text

These rank the pool. None of them belongs in the search filter, because each one used as a
filter would cut the pool for a fraction of the gain it gives as a sort.

| Column | Why it ranks | Source |
|---|---|---|
| Days open, and repost count | They failed to hire the human. Sharpest signal in the set | Post date across weekly runs |
| Bilingual or Spanish required | We ship Spanish. They are staffing for it | Description text |
| After-hours, evening or weekend coverage | The exact gap, stated in their own words | Description text |
| Inbound call volume named | They have measured the problem already | Description text |
| Seasonal or AEP-specific | A capacity spike they have to solve twice a year | Title and description |
| Number of open roles at the company | Two or more open roles is an agency scaling past its systems | Company grouping |
| Own inbound number on the website | Hard ICP-1 qualifier, and the Gap Report has nothing to run against without it | Website enrichment |
| Named Medicare Advantage carriers | Confirms they sell MA rather than only supplement | Website enrichment |
| State in the dense eight | Ranking only | Location field |

The first row is the one to sort on. An agency on its third repost of a client services
role in August has already priced the problem, failed to solve it with headcount, and is
eight weeks from AEP.

## The calendar, which decides when this runs rather than whether

Sourcing and outreach come apart here, and the seasonal rule in `outbound-engine.md` binds
the second one only.

Job posting peaks from July to mid-September, because agencies staff for an enrolment
period that starts 15 October. So the pool is at its richest now and thinnest in February,
which is the exact inverse of the outreach window.

Harvest on the posting calendar. Send on the outreach calendar. Cold outreach runs to
mid-September and then stops until January. The one asset that still goes out during AEP
is the Gap Report, unaccompanied by an ask, so a September pool stays workable through
15 October to 7 December on that basis alone.

Nothing here changes the qualification rule in `outbound-engine.md`. Verify against the
ICP-1 definition, 3 to 10 agents, own inbound number, sells MA, before spending a report
on anyone. A job post proves hiring. It does not prove profile.
