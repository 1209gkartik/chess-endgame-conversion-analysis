# Chess Endgame Conversion Under Time Pressure

Research question: how does remaining clock time relate to winning from a material advantage, within rating and advantage bands?

Run `python analysis.py` (Python 3.9+, no dependencies). It generates results.csv using 5,000 seeded synthetic observations. These are NOT real chess games. The simulation deliberately makes clock, rating and advantage affect win probability; results demonstrate the pipeline, not a discovery about chess.

Use `python analysis.py --csv observations.csv` for real observations with columns rating,clock (seconds),advantage (1–3 pawns of net material),win (1 for win, 0 otherwise). Define one observation per game: first position with no queens and at most two non-pawn pieces per side, positive material advantage of 1–3 pawns for the focal player, and recorded clock. Use standard material weights P=1,N=B=3,R=5. Exclude missing clocks and nonstandard games. Draws count as non-wins. Obtain PGNs from https://database.lichess.org/ and extract these fields separately; extraction is not implemented here.

Method: stratify by 400-point rating bands and material advantage, then compare win rates below 30 seconds versus at least 30 seconds. Report sample sizes alongside rates. Small groups are noisy. Material is not engine evaluation; opponent strength, increment, position difficulty and selection bias remain confounders. No causal claim.

Interview: explain grouping, binary outcomes, logistic simulation, reproducibility, and why real data is necessary. Next step: PGN extraction and regression controlling for opponent rating and time control.
