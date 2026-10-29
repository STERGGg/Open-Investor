# Introduction

Within five days in October 2026 three of the biggest employers in tech and banking made announcements that all seemed to point the same way. On 22 October Barclays said it would cut about 5,000 jobs by the end of the year, roughly 5% of its staff, as technology makes the bank more efficient [ITV1]. On 26 October Microsoft offered voluntary buyouts to about 60,000 employees, a quarter of its workforce [KUOW1]. On the same morning Meta launched a share sale of a size rarely seen, with $37.5 billion of new stock and preferred shares and a plan for $60 billion more, to pay for artificial intelligence [FF1, RAL1].

Put next to each other, the story writes itself. Companies are clearing out people to make room for machines. I started with that story too, but two things about it bothered me. The first is that these announcements are not all the same thing, and one of them is not about employees at all. The second is that we have heard this before. When ChatGPT arrived at the end of 2022, firms cut staff in the name of efficiency and then quietly hired many of them back. So the real question is whether this is a genuine shift or another round of over firing that will be reversed.

This report tries to answer it with numbers. It looks at what each company actually announced, whether the job cuts come anywhere close to paying for the AI spending, what happened the last time, what the companies that fired people for AI say it cost them, and what the official US jobs data shows. As in my earlier reports, the answers rest on my own Python models, eight this time, built on company filings, Nasdaq prices, the US Bureau of Labor Statistics and the Challenger, Gray and Christmas job cut reports.

# Key terms

**Capex (capital expenditure)** is money spent on long lived assets. For these companies it is mostly data centres, chips and the power to run them.

**Free cash flow** is the cash a business generates from its operations minus its capex. When it turns negative, the company has to use savings or raise money.

**Forward sale** means the company agrees the price for new shares now but issues them, and receives the cash, later on dates it chooses.

**Mandatory convertible preferred** is a share that pays a fixed dividend and must turn into ordinary shares on a set date, in Meta's case around August 2029.

**At the market programme** lets a company drip new shares into the market over time at whatever the price happens to be.

**Dilution** is the fall in each existing shareholder's slice of the company when new shares are created.

**Voluntary buyout** is an offer to pay staff to leave of their own accord, usually on severance terms, instead of choosing who to lay off.

**Headcount** is the number of people a company employs at a given date.

# Chapter 1  What actually happened

## Meta is selling shares, not handing them out

Meta's offering is not a bankroll for its employees, and it is worth being precise about this because the headlines made it easy to mix up. Meta is selling newly created shares to investors to raise money. It priced $25 billion of ordinary shares at $625 each through forward sales with Morgan Stanley and Goldman Sachs, and $12.5 billion of mandatory convertible preferred shares [RAL1, FF1]. It also set up a $60 billion at the market programme that is not expected to start before the first quarter of 2027 [FF1]. In total that is about $97.5 billion, and the filing says Nvidia, AMD and Broadcom, which also sell Meta its chips, have indicated they may buy up to $5 billion of the new shares between them [FF1]. The money is for AI. Meta raised its 2026 capex guidance to between $135 billion and $145 billion, and its free cash flow was negative $2.1 billion in the third quarter [META1].

The shares were already falling before the offering. Meta closed at $762.50 in the middle of October, fell 7% on 22 October after its results showed costs up 68% and operating margin halved to 20%, partly because of a $9.9 billion legal charge, and finished on 26 October at $630.56 [META1, DATA1]. Figure 1 shows that Microsoft, the company actually paying people to leave, is up 10% this year (Model 01).

[FIG fig01_the_week.png]

## Microsoft is paying people to go

Microsoft's offer is closer to what most people mean by a bankroll, but it is a severance deal, not a reward. Employees at vice president level and below in the US, Canada, the UK and India can choose to leave with a package comparable to Microsoft's standard severance, which usually means pay based on tenure, some stock vesting and health cover [KUOW1]. Each division chose who is eligible, and sales and some engineering teams are excluded [KUOW1]. Staff have until early December to decide and leave at the end of the year [AX1]. Earlier this year Microsoft made a smaller voluntary retirement offer that about 30% of those eligible accepted, and it expects fewer to take this one [KUOW1].

What makes it striking is the context. Microsoft laid off about 15,000 people in 2025 and 4,800 more in July 2026 [TR1, AX1]. Its headcount fell by 5,000 to 223,000 in the year to June, the first drop in a decade [TT1]. In the same year it spent $116 billion on capex, 80% more than the year before, and its AI business reached an annual revenue run rate of $37 billion [DATA2, CFO1]. Microsoft's spokesperson says AI is not driving the buyouts [KUOW1].

## Barclays says AI is the icing, not the cake

Barclays' cuts are real job losses. About 1,000 roles went in the first half and the rest will go by the end of the year, mostly in operations and support functions in the UK retail bank, including software developers [ITV1, RT1]. The bank booked about £600 million of structural cost actions in 2026, double what it planned, while its third quarter pre tax profit rose 12% to £2.3 billion [ITV1]. But the chief executive, C.S. Venkatakrishnan, was careful about the credit. He said the savings came from years of investment in modernising and simplifying systems, and called AI "the icing on the cake" [ITV1]. Barclays also cut about 5,000 jobs in 2023, before generative AI was in any bank's workflow [EUN1]. Cutting 5% of staff is something Barclays does.

> Q: So is Meta paying its staff in stock?
> A: No. Meta, like every big tech company, already pays a large part of its staff in shares, but this offering has nothing to do with that. It is new stock sold to outside investors because the company's AI spending is now bigger than the cash its business produces. The thing that hits Meta's employees is the 8,000 job cuts and 6,000 cancelled vacancies announced in April [SIL1].

# Chapter 2  Why Meta needs the money

## The data centres eat the cash

Figure 2 shows why a company this profitable is selling shares (Model 02). In 2022 Meta spent 62 cents of every dollar its operations generated on capex. In 2026, on the midpoint of guidance and my estimate of fourth quarter cash flow, it will spend about $1.04 [DATA2, META1]. Free cash flow goes from $54 billion in 2024 to roughly minus $6 billion this year. In 2024 Meta spent a net $30 billion buying back its own shares and in 2025 another $26 billion. In 2026 it has bought back none, has added about $22 billion of long term debt, and is now issuing $37.5 billion of equity [DATA2, META1].

[FIG fig02_meta_cash.png]

Meta is not running out of money. It still had $82 billion of cash and securities at the end of September [META1]. It is choosing to sell shares now, while the price is high, rather than run that cash down or borrow much more. The dilution from the shares launched so far is small, 40 million new ordinary shares or about 1.6% of the company, and about 6% if the whole $97.5 billion is eventually sold at today's price (Model 02).

The harder question is next year, which Figure 3 tries to answer (Model 03). Meta has not given 2027 capex guidance. If capex stays flat and operating cash grows by 15%, Meta would still burn about $4 billion in 2027 once the remaining legal payments are counted. If capex grows 30%, a pace well below this year's doubling, the gap is about $46 billion, more than the $37.5 billion already raised. In half of the scenarios in the grid the money launched in October does not cover 2027 alone, which is why the extra $60 billion programme exists.

[FIG fig03_meta_2027.png]

# Chapter 3  Do the job cuts pay for the AI?

## People versus graphics chips

This is the part of the story that I think gets the economics backwards. Figure 4 compares the cuts with the spending (Model 04). At Meta, capex per employee has gone from about $360,000 in 2022 to about $2.1 million in 2026. At Microsoft it has gone from $127,000 to $520,000.

[FIG fig04_people_vs_gpus.png]

Now take the cuts. Meta's median employee earned $388,200 in 2025 including stock [MPROXY1]. Cutting 8,000 people at that cost saves about $3.1 billion a year, which is 2.2% of this year's capex, or about eight days of data centre spending. If 30% of Microsoft's 60,000 eligible staff take the buyout, as happened with its last offer, the saving at the median pay of $200,972 is about $3.6 billion a year, 3.1% of its capex in the year to June [MSPROXY1]. Even if the people leaving earn 50% more than the median, the savings stay under 5% of capex. At Barclays, 5,000 jobs at the average 2025 compensation of about £99,500 per employee save roughly £500 million a year, close to the £600 million of cost actions the bank announced and 4.7% of its staff costs [BCS1, ITV1].

So the job cuts do not fund the AI build out. At Meta and Microsoft they are a rounding error next to it. What they do is protect profit margins while depreciation from the new data centres starts to hit the income statement, and send a message to investors that costs are under control. At Barclays the cuts are the main event, and the bank itself credits system modernisation more than AI. In none of the three cases is it accurate to say that machines have already taken these jobs.

> Q: Then why do companies keep saying AI?
> A: Because it is a better story. A company that says it is cutting because growth has slowed or because it hired too many people looks weak. A company that says it is cutting because AI made it more productive looks like it is ahead. Mark Zuckerberg said in January that projects which used to need big teams can now be done by one very talented person [SIL1]. That may well become true, but Chapter 5 shows that employers now blame AI for a far larger share of cuts than the official jobs data can explain.

# Chapter 4  Have we been here before?

## Meta's last round of efficiency

It is true that this has happened before, although the reason last time was not really AI. Figure 5 shows Meta's headcount (Model 05). It peaked at 87,314 in September 2022. Meta then cut 11,000 jobs in November 2022 and 10,000 more, plus 5,000 open roles, in March 2023, in what Zuckerberg called the "Year of Efficiency" [SEM1]. By the end of 2023 headcount was 67,317, down 23%. Then it climbed back to 78,450 by September 2025, so more than half of the people removed were effectively hired back within 21 months. Now it is cutting again, to 66,775 in September 2026, down 15% in a year [META1, META2].

[FIG fig05_cut_and_rehire.png]

That first wave was mostly about hiring too many people during the pandemic and then facing higher interest rates, and ChatGPT arrived in the middle of it. Microsoft shows a similar pattern in a different way. Its headcount has hardly moved since 2022, at 221,000 then and 223,000 now, despite tens of thousands of announced cuts [TT1]. In the year to June 2026, which included about 9,000 layoffs in July 2025, headcount fell by only 5,000, so Microsoft hired at least 4,000 more people than it lost through normal leaving [TR1, TT1]. These companies are swapping people, moving money from sales, gaming and middle management towards AI engineers, as much as they are shrinking.

## The companies that fired for AI and changed their minds

The cases where AI really was the reason are smaller but clearer. Klarna stopped hiring in 2023, said its chatbot did the work of 700 customer service agents, and let headcount fall 22% to about 3,500. By May 2025 its chief executive admitted the AI approach gave "lower quality" service and the company started recruiting people again [ENT1]. In July 2025 Commonwealth Bank of Australia cut 45 customer service roles to make way for a voice bot, then reversed the decision weeks later, apologised and said the roles had not been redundant after all, as call volumes were rising [ACS1].

Surveys suggest these are not one offs. In a Careerminds survey of 600 HR leaders in February 2026, two in three companies that made AI driven cuts were bringing staff back, and more than a third had rehired over half the roles [IBT1]. Forrester and Orgvue both put the share of employers who regret AI layoffs at about 55%, and Orgvue estimates that companies spend about $1.27 for every $1 they recover through workforce cuts once severance, lost output and rehiring are counted [IBT1].

## What an AI layoff really saves

To see why, I built a Monte Carlo simulation of 50,000 imaginary companies that cut jobs because AI will do the work (Model 06). Each draws its own severance bill, the yearly cost of the AI tools, whether and when it ends up rehiring, how much rehiring costs and how much damage is done while the roles sit empty. All the ranges come from the evidence above, for example a 2 in 3 chance of rehiring and a median of six months before people come back.

[FIG fig06_rehire_trap.png]

The result is sobering. Companies that never need to rehire keep a median of about 61% of the saving they promised over three years, because severance and AI tools eat the rest. Companies that do rehire keep a median of just 10%. Among those, 36% end up losing money and only 20% come out clearly ahead, which is close to what the HR leaders told Careerminds, 31% and 27% [IBT1]. Applied to Meta's 8,000 cuts, a promised $9.3 billion over three years shrinks to about $2.7 billion at the median of all companies, before you count anything that cannot be measured, like the people who stay and spend their time worrying about the next round.

# Chapter 5  What the jobs data says

## AI is now the most popular reason to fire people

Figure 7 uses the Challenger, Gray and Christmas reports, which count job cuts announced by US employers and the reasons they give (Model 07). From January to September 2026 employers announced 573,195 cuts, 39% fewer than in the same months of 2025, and planned 3% more hires [CHAL1]. But they blamed AI for 120,136 of those cuts, 21% of the total, making it the most cited reason this year, up from about 4.5% in 2025 [CHAL1, IBT1]. Technology sector cuts are up 54% while financial sector cuts are down 49% [CHAL1].

[FIG fig07_ai_blame.png]

Two things follow. Total firing is falling, not rising, so there is no sign yet of AI driving a wave of mass layoffs across the economy. And the share of cuts companies choose to blame on AI has jumped far faster than any plausible change in what the technology can actually do in a year, which supports the idea that "AI" has become the preferred explanation for cuts that would have happened anyway.

## Tech is shrinking, and the young feel it

Figure 8 turns to the official data from the Bureau of Labor Statistics (Model 08). Jobs in the information sector, which includes software publishers and the big internet platforms, peaked in November 2022, the month ChatGPT was released, and have fallen 12% since, a loss of 376,000 jobs [DATA3]. Computer systems design is down 5% and finance and insurance about 1%, while total US employment is up 3%. Job openings in the information sector are running at about 95,000 a month, down from about 240,000 at the 2022 peak [DATA3].

[FIG fig08_labour_market.png]

The timing is suggestive, but it is not proof, because 2022 was also when interest rates rose sharply and the pandemic hiring boom ended. The clearest evidence that AI itself is changing hiring comes from Stanford economists using payroll data, who found employment for 22 to 25 year olds in the most AI exposed jobs fell 13% relative to other groups after generative AI spread, while older workers in the same jobs were unaffected [STAN1]. In the BLS data the unemployment rate for 20 to 24 year olds has averaged 7.5% over the past year, against 4.3% for everyone, and the rate for graduates aged 25 and over has risen from 2.0% to 2.8% since late 2022 [DATA3]. That is a squeeze on entry level jobs, not a collapse.

# Chapter 6  So is it over firing?

## My answer

Partly, and in a specific way. I do not think Meta, Microsoft and Barclays are making the mistake Klarna made, because they are not really replacing whole teams with chatbots. Their cuts are mostly about margins and investor signalling at a time of enormous AI spending, and in Barclays' case about ordinary cost cutting with AI as a supporting act. Meta's equity raise is a separate thing altogether, a sign that the AI build out has outgrown even the most profitable companies' cash.

Where over firing is a real risk is in the kind of cut sold as "AI will do this now", especially in customer service and support. That is where the evidence of regret is strongest, where my simulation shows most of the saving disappears once people have to be rehired, and where Gartner expects half of the companies that cut service staff for AI to rehire for similar roles by 2027 [IBT1]. Meta's own history shows that big efficiency drives get partly reversed when the business needs people again.

The cost does not fall evenly. The cuts are small next to the AI bill, but they land on real people, and the data says they land hardest on the young, who are finding fewer entry level jobs in exactly the sectors that are building the technology.

## What I am watching

I am watching four things. The first is how many Microsoft employees take the buyout by early December, and whether forced layoffs follow if too few do. The second is Meta's 2027 capex guidance in January, because Model 03 shows that is what decides whether it needs the extra $60 billion. The third is whether Barclays' headcount actually falls in its 2026 annual report, given that it cut 5,000 people in 2023 too. The fourth is the Challenger share of cuts blamed on AI against the BLS data, because a widening gap between the two is the best sign that "AI" is an excuse rather than a cause.

# Data and method

All numbers come from public sources. Share prices and company cash flow and income statements come from Nasdaq through the OpenBB platform [DATA1, DATA2]. US employment, unemployment and job openings come from the Bureau of Labor Statistics public API [DATA3]. Headcounts, pay and the terms of each announcement come from company filings and the reports cited, and are listed in 03 Data/hand_collected_sources.csv with their links. Meta's 2026 free cash flow is my estimate using the company's own guidance. Annual capex for 2022 to 2025 from the cash flow statement excludes finance lease payments, while the 2026 guidance includes them, which slightly flatters the earlier years. The savings in Model 04 use median pay, which may differ from what the people actually leaving earn, so the sensitivity table shows a range. The Monte Carlo in Model 06 is a stylised model whose ranges I set from the survey evidence, and its comparison with the Careerminds results is a sense check, not a test. Challenger counts announced cuts and the reasons employers give, not confirmed layoffs. This report is not investment advice.
