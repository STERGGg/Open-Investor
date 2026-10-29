FIRED FOR THE MACHINES?
October 2026

Fired for the Machines.docx / .pdf   The finished article (also in 01 Report)

02 Python Models   (run "python3 run_all.py" from inside this folder; needs pandas, numpy, matplotlib)
   common.py                        Shared paths, data loaders and chart style
   model_01_the_week.py             Meta, Microsoft, Barclays and the Nasdaq 100 around the announcements (Figure 1)
   model_02_meta_cash.py            Meta's cash flow against capex, buybacks against the new equity, dilution (Figure 2)
   model_03_meta_2027.py            Meta's 2027 free cash flow under capex and cash flow scenarios (Figure 3)
   model_04_people_vs_gpus.py       Capex per employee and what the job cuts save against the AI bill (Figure 4)
   model_05_cut_and_rehire.py       Meta's cut and rehire cycle and Microsoft's headcount (Figure 5)
   model_06_rehire_trap.py          Monte Carlo of 50,000 companies that cut jobs for AI (Figure 6)
   model_07_ai_blame.py             US announced job cuts and the share blamed on AI (Figure 7)
   model_08_labour_market.py        BLS jobs, unemployment of the young and graduates (Figure 8)
   run_all.py                       Runs every model in order (model 03 uses a table from model 02)

03 Data
   daily_close.csv                  META, MSFT, BCS and QQQ daily closes, Nasdaq via OpenBB
   nasdaq_cash_flow.csv, nasdaq_income.csv   Meta and Microsoft statements, Nasdaq via OpenBB (US$ thousand)
   bls_monthly.csv                  BLS CES, CPS and JOLTS series, 2017 to 2026
   challenger_monthly.csv           Announced US job cuts by month, 2025 and 2026
   hand_collected_sources.csv       Every figure taken from a filing or article, with source and URL
   raw/                             Original downloads as JSON

04 Outputs
   charts/   fig01 to fig08
   tables/   csv results for every model

05 Report Build Files
   report_text.md, references.txt, build_report.py   Rebuilds the Word document
