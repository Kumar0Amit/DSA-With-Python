# Composition Pattern

# 1. What is the Composition Pattern?

The Composition pattern is a Two Pointer technique where we solve a difficult problem by **reducing it into a problem we already know how to solve**.

Instead of inventing a completely new algorithm, we compose existing patterns together.

For example,

Instead of solving **3Sum** directly,

we transform it into

```text
3Sum

↓

Fix one element

↓

2Sum
```

The difficult problem becomes a simpler one.

This idea extends further.

```text
4Sum

↓

3Sum

↓

2Sum
```

Eventually,

most **k-Sum** problems become repeated applications of the same idea.

---

# 2. When Should This Pattern Come To Mind?

This pattern usually appears when you see:

* triplets
* quadruplets
* k elements
* unique combinations
* combinations that sum to target
* exactly three numbers
* exactly four numbers

Immediately ask yourself:

> **"Can I fix one part of the answer and reduce the remaining problem?"**

If yes,

think **Composition**.

---

# 3. Mental Model

Imagine solving a three-person puzzle.

Instead of solving for all three people simultaneously,

you choose one person first.

Now the remaining problem only involves two people.

A difficult problem suddenly becomes one you've already solved.

That is the Composition pattern.

---

# 4. Thought Process

Suppose the problem asks:

> Find all unique triplets whose sum is zero.

Don't think about code.

Ask yourself:

### Question 1

Can brute force solve it?

Yes.

Choose every possible triplet.

Time

```text
O(n³)
```

Very expensive.

---

### Question 2

Do I already know how to find two numbers whose sum equals a target?

Yes.

Two Sum II.

---

### Question 3

Can I somehow transform 3Sum into 2Sum?

Yes.

Fix one element.

Now instead of finding

```text
a + b + c = target
```

we only need

```text
b + c = target - a
```

The problem has become Two Sum.

---

### Question 4

Why do we sort first?

Sorting restores monotonicity.

Without sorting,

Two Sum elimination cannot be applied.

Sorting also makes duplicate handling easy.

---

# 5. Brute Force

Choose

First element

↓

Second element

↓

Third element

↓

Check sum.

Time

```text
O(n³)
```

Most combinations repeat the same work.

---

# 6. Optimization Journey

Brute Force

↓

Three nested loops.

↓

Observation

Already know Two Sum.

↓

Fix one element.

↓

Remaining problem becomes Two Sum.

↓

Sort the array.

↓

Use Elimination pattern.

↓

Handle duplicates.

↓

Time

```text
O(n²)
```

---

# 7. Repeated Work Being Eliminated

Without Composition

The same value combinations are explored repeatedly.

With Composition

* Fix one element once.
* Solve the remaining problem once.
* Skip duplicate fixed values.
* Skip duplicate left values.
* Skip duplicate right values.

Repeated value combinations disappear.

---

# 8. Core Invariant

At every iteration,

```text
Every fixed value has been processed exactly once.

Every value combination is generated exactly once.
```

The invariant is about **uniqueness**.

Not about the array.

Not about pointers.

---

# 9. Pointer Responsibilities

## Fixed Pointer

Represents the first chosen element.

Never revisits duplicate values.

Each unique value starts exactly one Two Sum search.

---

## Left Pointer

Find the smaller remaining value.

Move according to Two Sum elimination.

---

## Right Pointer

Find the larger remaining value.

Move according to Two Sum elimination.

Notice

Composition reuses the Elimination pattern.

---

# 10. Why Do We Skip Duplicates?

Suppose

```text
[-2,-2,0,2]
```

Fix the first

```text
-2
```

Target becomes

```text
2
```

Two Sum finds

```text
(0,2)
```

Now suppose we fix the second

```text
-2
```

Target is still

```text
2
```

Two Sum produces

```text
(0,2)
```

again.

The triplet is identical.

The second fixed value creates only repeated work.

Therefore,

skip duplicate fixed values.

The same logic applies to the Left and Right pointers after finding a valid triplet.

---

# 11. Representative Problem — 3Sum

## Problem Statement

Find every unique triplet whose sum equals zero.

Example

```text
[-1,0,1,2,-1,-4]
```

Answer

```text
[-1,-1,2]

[-1,0,1]
```

---

## Step 1 — Brute Force

Three nested loops.

Try every triplet.

Time

```text
O(n³)
```

---

## Step 2 — Observation

Already know Two Sum.

Instead of solving three numbers together,

fix one.

Reduce to Two Sum.

---

## Step 3 — Sort

```text
[-4,-1,-1,0,1,2]
```

Sorting enables

* elimination
* duplicate detection

---

## Step 4 — Reduce

Fix

```text
-1
```

Need

```text
1
```

Now solve

Two Sum

for

```text
1
```

using Left and Right pointers.

---

## Step 5 — Handle Duplicates

Skip

* duplicate fixed values
* duplicate Left values
* duplicate Right values

Every value combination appears exactly once.

---

# 12. Pattern Recognition Tricks

Whenever you read:

* three numbers
* four numbers
* k numbers
* unique combinations
* triplets

Ask:

> **"Can I fix one element and solve the rest as a smaller problem?"**

If yes,

think **Composition**.

---

# 13. Common Mistakes

### Mistake 1

Trying to solve all three numbers simultaneously.

Composition is about reduction.

---

### Mistake 2

Not sorting first.

Without sorting,

Two Sum elimination cannot work.

---

### Mistake 3

Not skipping duplicate fixed values.

Duplicate triplets appear.

---

### Mistake 4

Skipping duplicates before storing the answer.

Always store first.

Skip afterwards.

---

### Mistake 5

Thinking Composition is a completely new algorithm.

It is simply a combination of previously learned patterns.

---

# 14. Edge Cases

Less than three elements.

---

All positive.

---

All negative.

---

Multiple duplicate values.

---

Already sorted.

---

# 15. Complexity Proof

Outer loop

```text
O(n)
```

Inner Two Sum

```text
O(n)
```

Total

```text
O(n²)
```

Sorting

```text
O(n log n)
```

Overall

```text
O(n²)
```

Space

```text
O(1)
```

(ignoring output list)

---

# 16. Relation With Other Two Pointer Variations

Reader / Writer

Build finished portion.

---

Symmetric Converging

Process mirror pairs.

---

Elimination

Discard impossible candidates.

---

Composition

Reduce a harder problem into a solved one.

---

Finalization

Process only the side whose answer is already fixed.

---

# 17. Quick Revision

Purpose

Reduce a difficult problem into a smaller solved problem.

Invariant

Every value combination is processed exactly once.

Recognition

* Triplets
* Quadruplets
* k-Sum
* Unique combinations

Optimization

Reduce

3Sum

↓

2Sum

Time

```text
O(n²)
```

Space

```text
O(1)
```

Memory Hook

> **Fix one. Solve the rest. Skip duplicates. Repeat.**
