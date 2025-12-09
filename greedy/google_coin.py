def min_total_coins(denoms, n):
    denoms.sort()
    reachable = 0  # we can form all values 1..reachable
    count = 0      # total coins needed
    i = 0          # pointer into denoms

    while reachable < n:
        # Case 1: we have a coin denom <= reachable+1
        if i < len(denoms) and denoms[i] <= reachable + 1:
            reachable += denoms[i]
            count += 1
            i += 1
        else:
            # Case 2: must create a coin of value reachable+1
            reachable += reachable + 1
            count += 1

    return count


# Examples
print(min_total_coins([1, 3], 10))        # -> 4
print(min_total_coins([1, 2, 4], 7))      # -> 3
print(min_total_coins([], 20))            # -> 5 (coins: 1,2,4,8,16)

'''
Nice — here’s a clear, rigorous proof that the greedy procedure you used is **optimal** (it produces the minimum possible number of coins needed to be able to form every integer from `1` to `n`).

I'll give two complementary arguments: an **invariant / “stays ahead” proof** and a short **exchange / contradiction** argument. Either one is enough; together they make the idea obvious and watertight.

---

## Setup / notation

* `denoms` = given sorted unique denominations (you may also be allowed to add new coin values).
* The algorithm maintains `reachable` = the largest value `R` such that **every** integer in `[1..R]` can be formed with coins chosen so far.
* At each step the algorithm:

  * If the smallest unused denomination `c ≤ R+1`, **take** it (use it), set `R ← R + c`.
  * Otherwise (no available `c ≤ R+1`), **create** a coin of value `R+1` and set `R ← R + (R+1)`.
* Stop when `R ≥ n`. Let `G` be the number of coins the greedy algorithm used.

We must prove no other selection of coins (from the given denoms plus any added ones) can use fewer than `G` coins to reach coverage `≥ n`.

---

## Invariant / “Greedy Stays Ahead” proof

Claim: after `t` coins have been chosen by the greedy algorithm, its `reachable` value (R_g(t)) is **at least** the `reachable` value (R^*(t)) of **any** other solution that uses `t` coins.

Proof by induction on `t`:

* **Base (t = 0):** both reachability values are 0. So (R_g(0)=R^*(0)=0).

* **Inductive step:** assume (R_g(t) \ge R^*(t)) for some `t ≥ 0`. Consider the (t+1)-th coin chosen by greedy and by an arbitrary optimal solution that has picked `t+1` coins in some way.

  * Let greedy’s current reachable be (R_g(t)). Greedy picks the largest extension possible without creating a gap: if there is a denomination (c \le R_g(t)+1) it takes the (smallest unused) such `c` and extends reach to (R_g(t+1)=R_g(t)+c); otherwise it creates coin (R_g(t)+1) and extends reach to (R_g(t+1)=2R_g(t)+1).
  * Now consider any other solution’s (t+1)-th coin choice. That solution must have been able to form every value up to (R^*(t)) before the (t+1)-th coin; hence to avoid a gap it must pick a coin value (c') with (c' \le R^*(t) + 1). Because (R_g(t) \ge R^*(t)) (inductive hypothesis), we have (c' \le R_g(t)+1). Greedy, by rule, picks a coin value that is at least as large an extender as any allowed (c' \le R_g(t)+1) — either it picks such a `c` from the available denominations or (if none exists among denominations) it creates the exact `R_g(t)+1`, which is the **largest** possible reachable-extending coin that does not create a gap at this step.
  * Therefore (R_g(t+1) \ge R^*(t+1)).

By induction, for every `t` we have (R_g(t) \ge R^*(t)).

Consequence: if some other solution reaches `R ≥ n` using `t` coins, then greedy reaches at least `R` with `t` coins as well. Thus greedy never needs more coins than any optimal solution — i.e., greedy uses the minimum number of coins. QED.

---

## Exchange / Contradiction argument (short)

Assume for contradiction there is an optimal solution `OPT` that uses fewer coins than greedy to reach coverage `≥ n`. Consider the first step where `OPT` and greedy differ in the coin they choose (both start with reachable `0`).

* Let greedy’s first coin be `g1` and `OPT`’s first coin be `o1`.
* Because `OPT` must cover `1`, `o1 ≤ 1`. Greedy chooses the best coin available that does not leave a gap, so either `g1 = o1`, or greedy chose a coin at least as large as `o1` while still not creating a gap.
* Replace `o1` in `OPT` with `g1`. Doing so cannot create a gap (because `g1 ≤ reachable_greedy_before + 1` and initial reachable is 0) and can only increase `OPT`’s coverage after the first step. Repeating this swap for the first differing coin step by step, we transform `OPT` into a solution that matches greedy for more prefix coins and uses no more coins than `OPT`. Eventually we end up with a valid solution that uses no more coins than `OPT` but whose prefix matches greedy; continuing the argument shows greedy’s solution is at least as good as `OPT`. This contradicts the assumption that `OPT` used fewer coins. Hence greedy is optimal.

---

## Intuition / Why "≤ reachable+1" matters

* If you currently can make all amounts up to `R`, the **next amount you must make is `R+1`**.
* If you add a coin bigger than `R+1`, you **leave `R+1` unreachable**, so that choice is invalid (unless you later add a coin ≤ `R+1`).
* Therefore the only useful new coins are those `≤ R+1`. Among those, the greedy choice (taking the largest possible extension available without making a gap — i.e., the largest coin ≤ `R+1`) maximizes new coverage immediately and therefore helps you reach `n` with as few further coins as possible. The “stays ahead” proof formalizes that.

---

## Quick example to build intuition

`denoms = [1,3], n = 10`:

* Greedy picks `1` → reach `1`.
* Next denom is `3 > 2` so greedy creates coin `2` → reach `3`.
* Greedy can then use `3` → reach `6`.
* No more denoms, greedy creates `7` → reach `13` and stops. Total coins = 4.
  Any other plan must also provide a coin ≤2 before reaching 2, so it cannot beat this count.

---

## Summary

* The greedy algorithm preserves the invariant “we can form 1..R” and always picks a coin that maximally extends `R` without creating gaps.
* By induction (stays-ahead) or by exchange, greedy’s reach after `t` coins is never worse than any other `t`-coin solution.
* Therefore greedy achieves the **minimum number of coins** required to cover `1..n`.

If you want, I can:

* produce a short formal write-up with symbols only, or
* show a small script that prints the greedy steps and compares with all possible selections for tiny inputs to empirically verify optimality. Which would you prefer?
'''