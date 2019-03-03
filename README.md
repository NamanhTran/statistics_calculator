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
Terminal Access
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

Just remember when you want to use a stats function prefix it with ```stats.```*Function_Name* or even better instead of typing ```import stats```, type ```from stats import all``` to use the function without prefixing the library

### Example

```
>>> import stats
>>> stats.quartiles([77,289,128,59,19,148,157,203,126,118,104,141,290,48,3,2,372,140,438,56,44,274,479,211,179,1,68,386,2631,90,30,57,89,116,225,700,40,73,75,51,148,9,115,19,76,138,178,76,67,102,35,80,143,951,106,55,4,54,137,367,277,201,52,9,700,182,73,199,325,75,103,64,121,11,9,88,1148,2,465,25])

Q0: 1
Q1: 54.5
Q2: 103.5
Q3: 200.0
Q4: 2631
IRQ: 145.5
IRQ x 1.5: 218.25
Lower Fence: -163.75
Upper Fence: 418.25
```