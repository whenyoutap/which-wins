# Which Wins? No. 5: O(1) vs O(2ⁿ)

**Same 60 numbers, five algorithms: how many steps does each take?**

## Run it yourself

```
python3 bigo_race.py
```

Python 3, standard library only.

## Our result

Counted steps, not timed: you should get exactly these numbers on any machine. The O(2ⁿ) lane is run for real on 10, 16 and 20 numbers to show it is exactly 2ⁿ; 60 is calculated.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | O(1), O(log n), O(n), O(n²) on 60 numbers | 1, 5, 60 and 1,770 steps | O(1) |
| 2 | O(2ⁿ): try every subset of the 60 | 2⁶⁰ subsets: about 36.5 years at a billion a second | Nobody |

## The rule

The O tells you how the work grows: one more number doubles O(2ⁿ), adds about 120 steps to O(n²), and changes nothing for O(1).

## In an interview

**Two numbers that add up to a target: how do you beat O(n²)?**
Remember the numbers you have seen in a dict and check for target minus x: one pass, O(n).

[Watch the reel](https://www.instagram.com/reel/DfeucPTj9xj/)