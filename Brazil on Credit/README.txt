BRAZIL ON CREDIT
October 2026

Brazil on Credit.docx / .pdf   The finished article (also in 01 Report)

02 Python Models   (run "python3 run_all.py" from inside this folder; needs pandas, numpy, matplotlib)
   common.py                        Shared paths, data loaders and chart style
   model_01_election.py             First round and runoff results, 2022 against 2026, polls (Figure 1)
   model_02_presidents.py           Dilma, Temer, Bolsonaro and Lula compared on official data (Figure 2)
   model_03_household_debt.py       Household debt, debt service and defaults since 2011 (Figure 3)
   model_04_price_of_credit.py      Interest rates by product and a R$100 food shop on the card (Figure 4)
   model_05_relief.py               Who is in debt, and what the election promises cost (Figure 5)
   model_06_state_debt.py           Government debt, interest bill and the debt stabilising surplus (Figure 6)
   model_07_markets.py              Brazilian shares (EWZ) and the real into the vote (Figure 7)
   model_08_fourth_term.py          Debt paths for Lula's fourth term and a 20,000 path simulation (Figure 8)
   model_09_trade.py                Brazil's exports by destination and US tariffs (Figure 9)
   run_all.py                       Runs every model

03 Data
   bcb_monthly.csv                  25 monthly series from the Banco Central do Brasil (SGS), 2011 to 2026
   bcb_series_list.csv              The SGS code and official title of every series
   imf_weo_bra_*.csv                IMF World Economic Outlook: growth, debt, overall and primary balance
   imf_weo_bra_nominal.csv          IMF nominal GDP in reais and inflation, 2024 to 2031
   imf_imts_brazil_exports_usd_bn.csv  IMF exports by destination, 2015 to 2025
   ewz_daily_close.csv              iShares MSCI Brazil ETF, Nasdaq via OpenBB
   hand_collected_sources.csv       Every figure taken from an article, with source and URL
   raw/                             Original downloads as JSON

04 Outputs
   charts/   fig01 to fig09
   tables/   csv results for every model

05 Report Build Files
   report_text.md, references.txt, build_report.py   Rebuilds the Word document
