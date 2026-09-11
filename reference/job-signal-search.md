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

A third signal sits on top of both and costs nothing to capture: a role reposted two or
three times, or open more than 45 days. They tried to hire the human and could not. That
is the agency to run the Gap Report on first.

## Structure: two passes, one pool

Run the search twice and union the results. One pass cannot be both broad and clean.

**Pass A, titles carry Medicare.** No description keyword at all. Title precision does the
qualifying, so nothing is filtered away.

**Pass B, titles are generic, description carries Medicare.** This is where the pool
actually grows. A four-agent agency in Ocala posts "Licensed Insurance Agent" and never
puts Medicare in the title, but the description says "Medicare Advantage" in the second
line. Pass A cannot see that agency. Pass B is most of the addressable pool.

Point the **Exclude jobs** table at the previous run so each pass only returns posts that
are new. Run weekly during the posting season, because repost frequency is itself a
scoring input and only a weekly cadence measures it.

**Verify the boolean before trusting the counts.** Run Pass B with titles only and note
the result count, then add one description keyword and note it again. If the count drops,
the panel ANDs the keyword block against the title block, and Pass B must use a single
keyword rather than the full set. Everything below assumes it does AND.

## Pass A — job titles to include

Medicare in the title. Paste as-is.

```
Medicare Agent, Medicare Sales Agent, Licensed Medicare Agent, Medicare Insurance Agent,
Medicare Sales Representative, Medicare Advisor, Medicare Insurance Advisor, Medicare
Broker, Medicare Specialist, Medicare Sales Specialist, Medicare Enrollment Specialist,
Medicare Benefits Advisor, Medicare Sales Consultant, Medicare Consultant, Medicare
Account Executive, Medicare Producer, Medicare Customer Service Representative, Medicare
Client Services Representative, Senior Benefits Advisor, Senior Market Agent, Senior
Health Advisor, Senior Insurance Advisor
```

If the panel matches on substring rather than whole phrase, the single entry `Medicare`
replaces the first eighteen of these and returns strictly more. Test it on one run before
switching, because a substring match also pulls in every payer and provider title, and the
exclusion list below then has to carry the whole load.

The four senior-market entries are the one soft spot in Pass A. "Senior" reads as
seniority as often as it reads as the over-65 market, so send those four straight to the
scoring step rather than to outreach.

**Job description keywords: leave empty.** Any keyword here only subtracts.

## Pass B — job titles to include

Generic titles. The description keyword does the qualifying.

```
Insurance Agent, Licensed Insurance Agent, Insurance Sales Agent, Licensed Sales Agent,
Licensed Agent, Insurance Advisor, Insurance Broker, Insurance Producer, Sales Producer,
Benefits Advisor, Benefits Consultant, Health Insurance Agent, Health Insurance Advisor,
Life and Health Agent, Licensed Sales Representative, Insurance Sales Representative,
Enrollment Specialist, Enrollment Advisor, Enrollment Counselor, Client Services
Representative, Client Service Specialist, Customer Service Representative, Insurance
Customer Service Representative, Account Manager, Service Agent, Receptionist, Front Desk
Receptionist, Office Administrator, Office Manager, Administrative Assistant, Agency
Assistant, Licensed Assistant, Inside Sales Representative, Appointment Setter, Call
Center Representative, Sales Assistant, Agency Manager, Sales Manager, Director of Sales,
Seasonal Licensed Agent, Seasonal Insurance Agent, AEP Agent, Open Enrollment Agent,
Bilingual Insurance Agent, Bilingual Customer Service Representative
```

The back half of that list, from `Client Services Representative` down, is the
answer-the-phone cluster. It is the highest-intent half and the one a title-only search
misses entirely.

## Pass B — job description keywords

```
Medicare, Medicare Advantage, Medicare Supplement, Medigap, Part D, AHIP, Annual
Enrollment Period
```

If the panel ORs these, use all seven. If it ANDs them, use `Medicare` alone and nothing
else. Every term after the first is a long-tail cut, and `Medicare` appears in the
description of essentially every post the other six would have found.

## Job titles to exclude — both passes

Four families of drift. These do not cost pool size, because nothing they remove was ever
inside the ICP.

**Clinical and provider.** The word Medicare appears in thousands of care-delivery posts.

```
Nurse, Registered Nurse, RN, LPN, LVN, Nurse Practitioner, Physician, Medical Assistant,
Certified Nursing Assistant, CNA, Caregiver, Home Health Aide, Personal Care Aide,
Therapist, Physical Therapist, Occupational Therapist, Social Worker, Case Manager, Care
Manager, Care Coordinator, Care Navigator, Patient Advocate, Patient Access, Patient
Services, Clinical, Pharmacist, Pharmacy Technician, Dental Assistant, Dental Hygienist
```

**Payer and back office.** Carrier-side and revenue-cycle roles, none of which sit in an
agency.

```
Claims Adjuster, Claims Examiner, Claims Processor, Claims Specialist, Claims Analyst,
Medical Biller, Billing Specialist, Medical Coder, Coding Specialist, Revenue Cycle,
Utilization Review, Utilization Management, Prior Authorization, Credentialing, Provider
Relations, Provider Network, Network Development, Underwriter, Underwriting, Actuary,
Actuarial, Risk Adjustment, HEDIS, Stars, Quality Analyst, Data Analyst, Business Analyst,
Project Manager, Software Engineer, Developer
```

**Wrong line of business.** Property and casualty volume alone would swamp the pool.

```
Auto, Home, Property, Casualty, Property and Casualty, Personal Lines, Commercial Lines,
Commercial Insurance, Workers Compensation, Financial Advisor, Financial Planner, Wealth,
Investment, Loan Officer, Mortgage
```

**The word "agent" everywhere else.** Pure noise from the generic titles in Pass B.

```
Real Estate Agent, Leasing Agent, Travel Agent, Freight Agent, Booking Agent, Talent
Agent, Reservation Agent, Ramp Agent, Gate Agent, Customs Agent, Transfer Agent,
Dispatcher, Recruiter, Recruiting, Talent Acquisition, Staffing, Intern, Internship
```

## Reversible exclusions — your call on the trade

Each of these removes real volume, and some of what it removes is inside the ICP. Start
with them off, measure the noise, then turn on only the ones the data justifies.

| Exclusion | What it removes | What it costs |
|---|---|---|
| `Final Expense` | Mostly 1099 recruiting posts, very high volume | Medicare agencies genuinely cross-sell final expense |
| `Mortgage Protection` | Close to pure recruiting noise | Almost nothing. Turn this one on first |
| `Annuity` | Financial-services drift | Some Medicare agencies sell annuities |
| `Employee Benefits`, `Group Benefits`, `Group Health` | Group brokers | A group broker with a Medicare book is a real prospect |
| `Trainee`, `Agent Trainee` | Captive career-agency programmes | An agency training a new hire has the same capacity pain |
| `Remote` | National call centres and downline recruiting | Small agencies do hire remote licensed agents |

`Remote` is the one worth understanding rather than just setting. A fully-remote licensed
agent post is overwhelmingly a national call centre or a downline recruiting drive, and
neither has its own local inbound number, which is the thing our product answers. Capture
remote as a column and deprioritise it. Do not filter on it.

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

**Company exclusions by name.** This is the filter that decides the quality of the pool, and
none of it is doable in the title panel. Four groups:

- Carriers and their captive sales arms. They are not agencies, and they post Medicare
  sales roles in volume.
- National direct-to-consumer call centres and lead aggregators. Hundreds of agents, their
  own stack, and nothing resembling the ICP-1 buying process.
- Captive property and casualty franchise networks, which post "insurance agent" at a rate
  that dwarfs the real pool.
- The 1099 recruiting operations that post continuously and hire nobody.

Build the list from the first run's top 50 companies by post count rather than from
memory. In this market, post volume identifies the wrong companies almost perfectly: an
agency with six agents posts one job, and everything posting forty is out of profile.

**Route rather than discard.** A Field Marketing Organisation or General Agency hit is not
noise, it is ICP-2. Send it to the B1 LinkedIn track and title-verify it there. The two
tracks never merge, so it must not enter the A1 sequence.

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
