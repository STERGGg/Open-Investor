# Introduction

On Sunday 25 October 2026 Brazil elected Luiz Inácio Lula da Silva president for a fourth time. He turns 81 the day after this report is published and will start his new term in January [LULA1, RT3]. He beat Flávio Bolsonaro, the eldest son of the former president Jair Bolsonaro, by 51.79% to 48.21%, a margin of about 4.4 million votes out of more than 124 million [RT2]. Three weeks earlier Flávio had won the first round, and the final polls had him ahead [RT3]. Within hours dollar futures traded about 10% higher against the real in thin overnight trading [RT4].

The story I kept reading alongside the election was about debt. Not the government's debt this time, although that matters too, but the debt of ordinary families. Eight in ten Brazilian households are in debt, a record [RT1]. Almost 84 million people are in default on at least one bill [RT5]. People pay for their weekly food shop in instalments and for takeaway orders on a payment plan [EMS1, EM1]. And in the nine days before the first round the government banned online betting and launched a scheme to buy up old household debts at a discount of at least 90% [RT5].

So this report tries to answer three questions. Who are the people Brazil was choosing between, and what did the last few governments actually deliver? How bad is the household debt problem, and why is credit so expensive? And what has Lula promised for his fourth term, can the budget pay for it, and what can Donald Trump, who backed the Bolsonaros, actually do about it? As with my reports on France, the AI build out and Elon Musk, the answers rest on my own Python models, nine this time, built mostly on official data from the Banco Central do Brasil, the IMF and Nasdaq.

# Key terms

**Selic** is the Brazilian central bank's policy interest rate, the equivalent of Bank Rate in the UK. It is currently 13.65% a year.

**Real (R$)** is Brazil's currency. On 23 October one US dollar bought about R$4.97.

**Revolving credit (rotativo)** is what happens when you pay less than the full credit card bill. The rest rolls over to next month and is charged interest.

**Parcelamento** is the Brazilian habit of splitting a purchase into monthly instalments on a credit card, often without interest if the shop offers it.

**Payroll loan (consignado)** is a loan repaid straight out of a worker's salary or pension, which makes it much safer for the bank and therefore much cheaper.

**Delinquency** means a loan more than 90 days behind on payments.

**Debt service ratio** is the share of a household's monthly income that goes on interest and loan repayments.

**Primary balance** is the government's budget balance before interest payments. A primary deficit means it is borrowing even before paying interest on its existing debt.

# Chapter 1  A country split down the middle

## The result

The first round on 4 October looked like the end of an era. Flávio Bolsonaro took 47.03% of the valid votes against 45.16% for Lula, with the other four main candidates sharing less than 8% between them (Model 01) [TSE1, RT6]. Flávio led in 15 states to Lula's 12, and the map split almost perfectly in two, with Lula winning all nine states of the poorer Northeast and Flávio winning every state in the South, Southeast and Centre West [RT6]. Flávio called it the "end of the PT era" [RT2].

[FIG fig01_election.png]

Three weeks later the result flipped. Lula won the runoff with 64,256,232 votes, the largest number ever cast for a single candidate in Brazil, against 59,826,041 for Flávio [RT2]. The average of 45 runoff polls had Flávio winning by 51% to 49%, so the polls were wrong by almost three points on Lula's share (Model 01) [RT3]. The margin was still small. Lula's 3.6 point lead is only twice as wide as his 1.8 point win over Jair Bolsonaro in 2022, and Flávio's Liberal Party won 121 of the 513 seats in the lower house, more than any other party and up from 99 four years ago [RT3]. Lula will take office on 5 January 2027 facing a Congress in which his opponent's party is the largest [RT3].

> Q: How did Lula win after losing the first round?
> A: Nobody can say for certain yet, and I would be wary of anyone who claims they can. Turnout rose from about 79% in the first round to 80.8% in the runoff, and most of the 8% who had voted for the smaller candidates had to choose one of the two [RT2, RT6]. What I can say is that the debt relief and the betting ban were announced nine days before the first round, and that the campaign was fought over exactly the household debt problem the rest of this report is about [RT5].

# Chapter 2  The old president, the comeback and the heir

## Jair Bolsonaro

The old president is in prison. Jair Bolsonaro, a former army captain who governed from 2019 to 2022, was barred from running for office until 2030 by the electoral court in June 2023 for abusing his position, and on 11 September 2025 the Supreme Court sentenced him to 27 years for his part in a plot to stay in power after losing the 2022 election [WIKI1]. He could not run in 2026, so he endorsed his son.

His record in office is more mixed than either side admits. Figure 2 compares the last four governments on official data (Model 02). Under Bolsonaro the economy grew by an average of 1.4% a year, including the Covid crash of 2020, unemployment averaged 12.1%, and gross government debt actually fell by 3.6 points of GDP over his term, helped by the high inflation of 2021 and 2022 that shrank the debt relative to the size of the economy. But the dollar rose 40% against the real while he was president, and inflation averaged 6.1% [DATA1].

[FIG fig02_presidents.png]

## Lula, the comeback

Lula is the most extraordinary comeback story in modern politics. He was a metalworker and union leader before he became president, served two terms from 2003 to 2010 and left office with an approval rating of about 80%, largely thanks to a commodity boom and the Bolsa Família cash transfer programme [LULA1]. In 2018 he was jailed for corruption and spent 580 days in prison before the Supreme Court annulled his convictions in 2021, which let him run and narrowly beat Bolsonaro in 2022 [LULA1].

His third term has been good for jobs and bad for the public finances. Growth has averaged 2.8% a year, the best of the four governments, and unemployment has fallen to between 5% and 6%, the lowest since the current survey began in 2012, and stood at 5.3% in August (Model 02) [DATA1]. But gross government debt has risen by 11.2 points of GDP, the Selic has averaged 13.1%, and as Chapter 3 shows, households have never been more indebted. The real is almost exactly where it was when he took office.

## Flávio, the heir

Flávio Bolsonaro is a senator for Rio de Janeiro who announced he would run in December 2025, after his father was jailed and after the governor of São Paulo, Tarcísio de Freitas, who many on the right had wanted as their candidate, decided to run for governor again instead [WIKI1]. He ran as the continuation of his father's movement, promising his own debt relief plan, SOS Brasil, with discounts of up to 90% through the state bank Caixa [RT5].

He also ran under a cloud. In September the Supreme Court revealed that it had opened an investigation into whether Flávio was involved in corruption, money laundering and tax evasion linked to Daniel Vorcaro, the former head of the collapsed lender Banco Master, whose fraud police say touched about 800,000 clients and was worth about $2.3 billion [AJ1]. Police say Vorcaro sent about $12 million to a US fund linked to Flávio's brother Eduardo to finance a film about their father. Flávio denies any wrongdoing and says he was only looking for private investment in the film [AJ1].

> Q: So who was the fan favourite?
> A: On the first round, Flávio. He won more votes and more states than Lula, and polls had him winning the runoff. But Brazil is so evenly split that the "favourite" depends almost entirely on who turns out, and in the end Lula won by about 4.4 million votes. I would not call either of them a fan favourite. Lula is the most successful vote winner in Brazil's history, and the Bolsonaro name still gets nearly half the country to vote for a son with no executive experience who is under investigation.

# Chapter 3  A country living on the card

## How indebted are Brazilians?

The household debt numbers explain why debt dominated the campaign. According to the central bank, Brazilian households owe the banks the equivalent of 49.9% of a year's income, close to the record of 49.9% set in January, and they now spend 28.7% of their monthly income on interest and repayments, the highest share since the series began in 2011 (Model 03) [DATA1]. The CNC's monthly survey of about 18,000 households found that 82% of families were in debt in July, the sixth record in a row, and that 29.8% were behind on their payments [RT1].

[FIG fig03_household_debt.png]

What makes Brazil different from Britain or Europe is not the amount of debt, which at half a year's income is lower than in many rich countries, but its price. The right hand side of Figure 3 shows that 8.0% of household loans from banks' own funds were more than 90 days late in August, the highest since the series began in 2011, and that this happened while the Selic was at its highest level in almost twenty years [DATA1]. When interest rates are this high, even a modest amount of debt swallows a large share of income.

## What credit costs

Figure 4 shows why. In August the average Brazilian paying interest on a credit card balance was charged 445% a year. A card instalment loan cost 192%, an overdraft 136%, and a personal loan not tied to a salary 110% (Model 04) [DATA1]. The central bank's own rate was 13.65%, so the revolving card rate is 33 times the policy rate. Only payroll loans, which are repaid straight out of a salary or pension, come anywhere near normal at 29%.

[FIG fig04_price_of_credit.png]

To make that concrete I took a R$100 food shop left on a credit card. At 445% a year the monthly rate is 15.2%, so without any limit the R$100 would grow to R$545 after a year. Since January 2024 a law has capped the interest and charges on revolving card debt at 100% of the original amount [MM1], so the most anyone can now owe on that shop is R$200, a limit the debt hits after five months (Model 04). The cap is a real protection, but doubling the cost of your groceries is still a terrible deal, and two thirds of all revolving card balances, 66%, are already more than 90 days late [DATA1].

## Can you really take out a loan for fruit?

Not quite, and I think the way the story gets told abroad is a bit misleading. Brazil does not have a special loan product for fruit, and this is not microfinance in the usual sense of small business loans to the poor. What Brazil has is a near universal habit of paying in instalments on a credit card, called parcelamento, which is offered for almost everything. According to the card industry association, 42.7% of credit card purchases in the third quarter of 2025 were split into instalments [EMS1]. Supermarkets have offered food in instalments since 2024, as long as the bill is above a minimum amount [EM1], and more than 1.3 million iFood takeaway orders were paid in instalments in December and January alone, more than double the year before [EMS1]. Of the families in debt, 85% owe money on a credit card [RT1].

The instalments themselves are often interest free, which is why people use them. The danger is what they do to the next few months. A family that pays this week's food in six instalments has already spent part of the next six months' income, and when an emergency arrives the gap is filled with the revolving card or the overdraft at 136% to 445% a year. That is how a fruit purchase becomes a debt problem.

> Q: Why are Brazilian interest rates so high?
> A: Partly because the Selic itself is high, at 13.65%, to keep inflation down in a country with a long history of it. But the much bigger reason is the spread banks add on top for lending to people with no collateral, in a country where recovering bad debts through the courts is slow and two thirds of revolving card debt goes bad. High defaults justify high rates, which cause more defaults, and that circle is very hard to break.

# Chapter 4  Who owes, and what the government is doing about it

## The poorest owe the most

The debt is concentrated where it hurts most. Among families earning up to three minimum wages, about R$4,860 a month, 84.9% are in debt and 38.5% are behind on payments, compared with 72% and 15.1% among families earning more than ten (Model 05) [RT1]. Serasa, the credit bureau, counted 83.98 million people in default in August, about two in five Brazilians including children, with R$586.4 billion of overdue debts on its records [RT5].

Online betting made it worse. Betting was legalised in 2018 but only properly regulated at the end of 2023, and Brazilian households lost about R$62 billion to it in 2025 alone, around R$4.7 billion a month [AB1]. A survey of secondary school students found that one in five had placed an online bet in the past year [AB1]. On 25 September the government banned online betting outright [AB1, RT5].

[FIG fig05_relief.png]

## The pre election rescue

On the same day, nine days before the first round, Lula signed a provisional measure creating Desenrola 3.0. The state will buy household debts that are between two and four and a half years overdue and worth less than R$10,000 each, at a discount of at least 90% to their face value, clear the debtors' credit records and let them repay a reduced amount [RT5]. The target is R$150 billion of face value out of an eligible R$300 billion, at a cost of about R$15 billion, and the first auction is planned for November, after the vote [RT5]. Together with a 15% rise in Bolsa Família worth R$22 billion and the R$5.3 billion of tax lost from the betting ban, the three measures cost up to R$42.3 billion, none of which is in the 2027 budget sent to Congress in August [RT5].

The track record of these schemes is not encouraging. The first Desenrola, launched in 2023, renegotiated about R$53 billion of debt for around 15 million people, and a second round renegotiated R$28.37 billion this year, yet household debt kept rising, and O Globo found that 30.34% of the second round's repayment deals were already behind in September [RT5]. The central bank governor, Gabriel Galípolo, has said he is worried by "aggressive and predatory" credit offers [RT5]. Flávio called the betting ban "hypocritical, electioneering and populist", while promising a debt relief plan of his own [RT5].

> Q: Will Desenrola 3.0 fix the problem?
> A: I doubt it. It will help millions of people clean their credit records, which matters, but it treats the symptom and not the cause. As long as a credit card costs 445% a year and two thirds of revolving balances go bad, new debts will replace the ones the state buys, which is exactly what happened after the last two rounds. It also teaches people that if they wait long enough, someone may buy their debt for ten cents on the real, which is unfair on the people who paid.

# Chapter 5  The state's own debt

## Public debt is climbing again

The government has the same problem as the households it is trying to help. Gross government debt on Brazil's own definition is 82.9% of GDP, up from a low of 71.4% in 2022, and the IMF, which uses a wider definition, expects it to rise from 97% this year to 105% by 2031 (Model 06) [DATA1, DATA2].

[FIG fig06_state_debt.png]

The right hand side of Figure 6 shows why. Before interest the budget is roughly balanced, with a primary deficit of only 0.3% of GDP this year, but the government pays about 7.8% of GDP in interest, so almost the entire deficit is interest [DATA2]. That is the mirror image of the household problem. The Selic at 13.65% keeps inflation down, but it also makes the government's own borrowing very expensive.

I did the same debt test I used for France. With an average interest rate of about 8.3% on the debt and nominal growth of about 6.2% next year, Brazil needs a primary surplus of about 2% of GDP just to stop the debt ratio rising (Model 06). The 2027 budget targets 0.5% [RT3], before the R$42.3 billion of election promises that are not in it. So the debt is likely to keep rising unless interest rates fall a long way or the government tightens much harder than it has said it will.

> Q: Is Brazil heading for a debt crisis like Greece?
> A: Not in the same way. Almost all of Brazil's debt is in its own currency, held mostly by its own banks and funds, and it has large foreign reserves, so it cannot run out of reais the way Greece ran out of euros. The risk is slower. A rising debt keeps interest rates high, high rates keep households in debt, and the economy grows more slowly than it could. That is less dramatic than a default, but over a decade it costs a lot.

# Chapter 6  What the markets were betting on

Investors had clearly bet on a Bolsonaro win. The iShares MSCI Brazil fund, one of the main ways to own Brazilian shares from abroad, rose 87.5% between the start of 2025 and 23 October, and jumped 12.5% the day after Flávio won the first round (Model 07) [DATA3]. The real had recovered from about R$6.10 to the dollar at the end of 2024 to R$4.97 on the Friday before the runoff [DATA1, RT3].

[FIG fig07_markets.png]

The reaction to Lula's win came overnight. Dollar futures in Chicago rose about 10% against the real on Sunday evening and a Tokyo listed fund that tracks Brazilian shares fell more than 11% when it opened [RT4]. Those markets are thin on a Sunday night and often overshoot, and Brazilian markets reopen this morning, so the real test of how much investors care is what happens over the next few weeks, and above all who Lula picks as his finance minister [RT3, RT4].

> Q: Why do markets prefer the Bolsonaros?
> A: Mainly because of the public finances. Investors worry that a fourth Lula term means more spending, a bigger deficit and therefore interest rates that stay high for longer, while they expected a Flávio government to cut spending. Whether that would have happened is another question, since Jair Bolsonaro also spent heavily before the 2022 election. Brazil also faces a 25% US tariff on some of its exports since July, which adds to the pressure on the real whoever is president [RT3].

# Chapter 7  Lula's fourth term, the plan and the odds

## What he has promised

Lula's programme for a fourth term, registered with the electoral court in August, is long on ambitions and short on numbers [EX1]. The headline promise is to end the "6x1" working week, in which many Brazilians work six days for one day off, and cut the legal week to 40 hours without any cut in pay. Alongside it he promises to keep the income tax exemption for people earning up to R$5,000 a month, which became law in January and is paid for by a new minimum tax of up to 10% on incomes above R$600,000 a year, to finish the consumption tax reform with a zero rate on basic food and cashback for poorer families, and to expand housing, health, education and pharmacy programmes [EX1, EX2]. He also promises a separate ministry for public security, an end to illegal deforestation by 2030 and a return of Petrobras to fuel distribution [EX1]. Ten days before the runoff he added free public transport at weekends in every city with buses, which a PT deputy estimates would cost up to R$16 billion a year [GP1].

On the public finances the programme says only that it will keep the existing fiscal framework and balance the books through growth, efficiency and taxing the rich, without a single number for the deficit, the debt or growth [EX1].

## Can he pay for it?

To answer that I built a simple debt model on the IMF's forecasts for the four years of the new term (Model 08). On the IMF's own baseline, gross debt rises from 97% of GDP this year to 104.5% in 2030. Adding the election promises that are not in the budget, the Bolsa Família rise and the tax lost from the betting ban every year, Desenrola once in 2027 and free weekend transport from 2028, costs about 0.3% of GDP a year and takes debt to about 106%. The promises themselves are not what breaks the budget. The problem is that the baseline was already rising before any of them were made.

[FIG fig08_fourth_term.png]

A single line hides how uncertain this is, so I simulated the term 20,000 times for two scenarios, using exactly the same random shocks in both so that the only difference is policy (Model 08). Growth shocks have fat tails sized from Brazil's own record, so deep recessions like 2015 and 2016 turn up more often than a normal curve would allow. Interest rates drift and tend to rise in bad growth years, and in any given year there is an 8% chance of a confidence crisis like those of 2002 and 2015, which lifts interest rates by 2.5 points for the rest of the term. On Lula's current promises the median path takes debt to about 108% of GDP in 2030. Debt ends the term lower than it is today in only 7% of paths, and it passes 110% of GDP in 39% of them and 120% in 10%.

The green paths show what a serious fix would do. In that scenario the government aims for a primary surplus of 2% of GDP by 2029, which is what Chapter 5 shows is needed, and the credibility lets interest rates fall by up to one and a half points. Because governments rarely deliver all of what they announce, each path also draws how much of the plan is actually carried out, two thirds on average. Even then the median only flattens to about 101% of GDP, debt falls below today's level in 29% of paths, and the chance of passing 110% drops from 39% to 16%. A fix helps a great deal with the worst outcomes, but it needs around 2% of GDP, about R$300 billion a year, from spending cuts or new taxes, which nothing in the programme points to.

> Q: So can Lula actually pull it off?
> A: It depends which part. The income tax cut and the tax reform are already law, so those will happen. The social programmes are cheap enough to fund by squeezing other spending. The two flagship promises that need the constitution changed, ending the 6x1 week and free transport, need three fifths of both houses, which means 308 of the 513 deputies, and the right already holds about 276 seats [RT3, GP1]. And on the evidence of my simulation, stabilising the debt during this term is very unlikely without a change of direction he has not promised, since even a serious fix that is two thirds delivered only gets debt below today's level in about three paths out of ten. My rough scorecard is that he delivers most of what is already law, some of the social expansion, perhaps a watered down version of the working week, and very little of the fiscal repair.

## Will Trump do anything about it?

Trump has already made clear what he thinks. On election night he compared Lula's win to his own defeat by Joe Biden in 2020 and said "communists" do not give up power once they win it, without offering any evidence of fraud [RT7]. The State Department had not said whether it recognised the result [RT7].

The relationship was already hostile. In July 2025 Trump raised tariffs on Brazil to 50%, explicitly linking it to the prosecution of his ally Jair Bolsonaro, with exemptions for aircraft, oil, iron ore and orange juice, and the US revoked the visas of eight Supreme Court justices [WIKI2]. Washington then presented Brazil with 21 demands for lifting the tariff, cut them to 14 in January, and saw both lists rejected [WIKI2]. In July 2026 the trade representative added a 25% tariff on certain Brazilian goods under Section 301, citing digital payments, ethanol, intellectual property, illegal deforestation and anti corruption enforcement, while saying the US remained "open to continuing negotiations" [USTR1].

[FIG fig09_trade.png]

What limits Trump is trade arithmetic (Model 09). The US bought $38.1 billion of Brazilian goods in 2025, 10.9% of Brazil's exports and about 1.7% of its GDP, and that figure fell 7% last year as the tariffs bit [DATA4]. China bought $99.9 billion, 28.7% of the total and 2.6 times as much as the US. When the US raised tariffs on coffee in 2025, China approved 183 Brazilian companies to export coffee to China [WIKI2]. Tariffs can hurt particular industries, coffee, beef and steel among them, but they cannot sink the Brazilian economy, and every new round pushes Brazil closer to Beijing.

> Q: What will Trump most likely do?
> A: My guess is more pressure rather than a break. The easiest levers are the ones he has already used, more tariffs, visa bans and sanctions on individual judges and officials, and refusing to say the election was fair keeps Flávio Bolsonaro's challenge alive. What he probably cannot do is change the result, and the market reaction suggests investors are far more worried about Brazil's budget than about Washington. Note too that Brazil is not "nearby" in any practical sense, since Brasília is about 7,000 kilometres from Washington, and that the US is only Brazil's second biggest customer among single countries, far behind China.

## The most likely path

Putting it together, the path I think is most likely for the next four years looks like this. The income tax cut and the tax reform roll out on schedule, and the social programmes grow at the margin. Congress, where Flávio's party is the largest, blocks or waters down the constitutional changes, so the 6x1 week is phased in slowly at best and free transport is limited to a few cities. The government meets its fiscal rules only on paper, debt drifts up towards 105% of GDP as the IMF expects, and the central bank cuts the Selic slowly, to about 12% by the end of 2027 on the market's own forecasts [RT1]. Growth stays around 1.5% to 2% a year [RT1, DATA2], household debt eases a little as rates fall but stays near record levels, and relations with Washington stay cold, with tariffs that hurt some exporters but not the economy as a whole.

The upside case is that a credible finance minister commits to a real primary surplus, interest rates fall faster than expected and the cheaper credit finally reaches households. The downside case is a fight over the result, a weaker real, higher inflation and a central bank forced to keep rates high for longer, which would make every problem in this report worse.

## What I will be watching

Three things will tell me which path Brazil is on. The first is the finance minister Lula picks, and whether that person commits to a number for the primary surplus. The second is the Selic. If the central bank can start cutting early next year, both the government and households get breathing room, and if it cannot, the debt dynamics in Figure 8 get worse. The third is whether Flávio Bolsonaro and Washington accept the result, because a long fight over legitimacy would raise the risk premium on everything Brazilian.

## My view

My view is that Brazil has a credit problem that no election can fix. Households are not in trouble because they borrowed recklessly, at half a year's income they owe less than British families do, but because borrowing costs between 110% and 445% a year on the products poor families actually use. That comes from a high Selic, which comes in turn from a government that runs large deficits, and from a system where bad debts are so hard to recover that lenders charge everyone for the people who do not pay. Desenrola and the betting ban treat symptoms. The cure is lower interest rates, which need a government that borrows less, and cheaper ways to recover debts, which need legal reform. Lula has the mandate to try, but his programme promises more spending, contains no fiscal numbers and depends on constitutional changes he does not have the votes for. My central expectation is a fourth term that is good for the people who already benefit from his tax cuts and transfers, and that leaves the debt, the interest rate and the household credit trap roughly where it found them.

# Conclusion

Brazil chose Lula again by 51.79% to 48.21%, a few weeks after it had put Flávio Bolsonaro first, and the margin and the map show a country split almost exactly in half between the poorer Northeast and the richer South. The old president, Jair Bolsonaro, is in prison, the comeback president will be 81, and the heir lost narrowly while under investigation.

The debt story is real but often told the wrong way. Brazilians are not taking out special loans for fruit. They are paying for food in instalments on credit cards, and when money runs short they fall onto revolving credit at 445% a year and overdrafts at 136%. As a result 82% of families are in debt, 28.7% of income goes on repayments, and household defaults are at a record. The government's answer before the vote was to ban betting and buy up old debts at a 90% discount, which will help millions of people but did not stop debts rising after the last two rounds.

The deeper problem is that the state is caught in the same trap as its citizens, paying about 7.8% of GDP in interest on a debt that the IMF expects to keep rising. Lula's plan for a fourth term does not change that. My simulation puts the chance that debt is lower in 2030 than today at about 7% on current plans and a 39% chance that it passes 110% of GDP, his flagship promises need constitutional votes he does not have, and Trump can hurt Brazilian exporters but not the economy, because China buys almost three times as much. Until the government borrows less and interest rates can fall, every Brazilian with a credit card will keep paying for it.

# Appendix A  Methodology and models

All models are written in Python using pandas, numpy and matplotlib and sit in 02 Python Models, where run_all.py rebuilds every chart and table in 04 Outputs. Monthly data from the Banco Central do Brasil's SGS system was downloaded on 26 October 2026 and is stored in 03 Data/bcb_monthly.csv, with the code and official title of every series in 03 Data/bcb_series_list.csv. IMF World Economic Outlook data and Nasdaq prices were downloaded through the OpenBB platform. Every figure taken from an article is stored in 03 Data/hand_collected_sources.csv with its source and URL.

Model 01, The election. First round shares for the six main candidates and the 2022 and 2026 runoffs, with the 2026 runoff poll average.

Model 02, Presidents compared. Averages of unemployment, 12 month inflation, the Selic and real GDP growth over each government's term, with the change in gross government debt and in the real. Terms are Dilma Rousseff from January 2011 to August 2016, Michel Temer from September 2016 to December 2018, Jair Bolsonaro from 2019 to 2022 and Lula from January 2023 to the latest month. Unemployment starts in March 2012, 2016 growth is counted under Temer and 2026 growth is an IMF estimate.

Model 03, Household debt. Debt as a share of the last twelve months' income, with and without mortgages, the debt service ratio, the delinquency rate on household loans from free resources and the Selic.

Model 04, The price of credit. Average interest rates by product in August 2026. The R$100 example converts the annual revolving card rate to a monthly rate and compounds it for twelve months, with and without the cap that limits interest and charges on revolving card debt to 100% of the original amount.

Model 05, Who owes. The CNC survey by income group and type of debt, and the size of the pre election measures against overdue debts and betting losses.

Model 06, The state's debt. Gross debt on the central bank's definition and on the IMF's wider definition with its forecast to 2031. Interest is the IMF's overall deficit minus its primary balance. The debt stabilising primary balance is debt times (r minus g) divided by (1 plus g), with r the 2026 interest bill divided by 2025 debt, about 8.3%, and g nominal growth in 2027 from the IMF's real growth forecast and 4.25% inflation, about 6.2%.

Model 07, Markets. The iShares MSCI Brazil fund (EWZ) since January 2025 and the monthly average real against the dollar since 2018.

Model 08, The fourth term. A debt engine for 2027 to 2030 on the IMF's definition, where debt equals last year's debt times one plus the average interest rate, divided by one plus nominal growth, minus the primary balance, plus a residual that makes the IMF's own path reproduce exactly. Interest rates, growth and the primary balance come from the IMF's October 2026 forecasts. The Promises scenario subtracts the unbudgeted measures as a share of the IMF's nominal GDP. The Credible fix scenario aims for a primary surplus of 2% of GDP by 2029 with up to 1.5 points off the interest rate, scaled in each path by a delivery share drawn from a Beta(4, 2) distribution with a mean of two thirds. Both scenarios run on the same 20,000 sets of shocks. Growth shocks follow a Student t distribution with 4 degrees of freedom scaled to 2.45 points, Brazil's standard deviation from 2011 to 2025 excluding 2020. The interest rate follows a random walk with steps of 0.75 points correlated at minus 0.5 with growth, there is an 8% chance each year of a confidence crisis that adds 2.5 points to the rate for the rest of the term and takes 1.5 points off growth, and the primary balance has shocks of 0.5 points. The chart shows 300 paths per scenario, with percentile bands shaded on top.

Model 09, Trade. Brazil's goods exports by destination from the IMF's IMTS data, 2015 to 2025, and exports to the US as a share of GDP using the 2025 average exchange rate.

Limitations. The CNC, Serasa, betting and Desenrola figures come from press reports of surveys and official documents rather than the original datasets. The overnight market moves after the runoff were reported in thin trading before Brazilian markets reopened and are not in my data. The comparison of presidents uses simple averages over different economic conditions, including Covid, so it describes rather than judges each government. The debt stabilising balance and Model 08 use the IMF's debt definition, whose year to year changes include a residual of about 1.5% of GDP a year not explained by interest, growth and the primary balance, so they show the order of magnitude rather than a precise forecast. Free weekend transport is costed from a PT deputy's estimate rather than an official one.
