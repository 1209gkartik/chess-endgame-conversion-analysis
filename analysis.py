import csv, random, math
from collections import defaultdict
from pathlib import Path
import argparse

def simulate(n=5000):
    rng=random.Random(42)
    for _ in range(n):
        rating=rng.randint(1000,2400); clock=rng.randint(5,180); advantage=rng.choice([1,2,3])
        p=1/(1+math.exp(-(-2+0.001*(rating-1500)+0.012*clock+0.65*advantage)))
        yield dict(rating=rating,clock=clock,advantage=advantage,win=int(rng.random()<p))

def summarize(rows):
    groups=defaultdict(list)
    for r in rows:
        clock=float(r['clock']); rating=int(r['rating']); advantage=int(r['advantage']); win=int(r['win'])
        if clock<0 or win not in (0,1) or advantage not in (1,2,3): raise ValueError('Invalid observation')
        groups[(rating//400*400,advantage,'under 30s' if clock<30 else '30s or more')].append(win)
    return [(rating,adv,clock,len(v),sum(v)/len(v)) for (rating,adv,clock),v in sorted(groups.items())]

def main():
    p=argparse.ArgumentParser(); p.add_argument('--csv'); args=p.parse_args()
    if args.csv:
        with open(args.csv,newline='') as f: rows=list(csv.DictReader(f))
    else: rows=list(simulate())
    out=Path('results.csv')
    with out.open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['rating_band_start','pawn_advantage','clock_group','n','win_rate']); w.writerows(summarize(rows))
    print('Saved',out,'from',len(rows),'observations;', 'user CSV' if args.csv else 'SIMULATED data')
if __name__=='__main__': main()
