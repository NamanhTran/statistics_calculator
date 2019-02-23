# Personal Statistics Calculator

Statistics Calculator that runs in python's IDLE

**Currently contains formulas for:**

```
Mean: mean([Array Containing Numbers to Sum])
Quartiles: quartiles([Array Containing Numbers to Find Quartiles])
IRQ: irq(q3, q1)
Z-Score: z_score(x, mew, std_div)
Combinations (ex: 10 choose 2): choose(a, b)
Binomial Probability: binom_prob(k, n, p)
```

### Prerequisites

You will need

```
Python 3.6 (or later versions)
Ability to run python's IDLE
```

### Using it

To run this after installing Python 3.6 (or later) on your computer and cloning this to a directory.
1) Go to directory
2) Type in your terminal

```
python3
```
This will put you in python's IDLE

3) Import the stats module
```
import stats
```
4) Done!

Just remember when you want to use a stats function prefix it with stats.*Function_Name*

### Example

```
import stats
stats.quartiles([2,4,5,5,5,5,6,6,7,8,10,11,12,13,16,17,19,19,24,25,32,38,49,53])
Q0: 2
Q1: 5.5
Q2: 11.5
Q3: 21.5
Q4: 53
```