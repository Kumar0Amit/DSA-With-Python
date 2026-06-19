# Elimination Pattern

# 1. What is the Elimination Pattern?

The Elimination pattern is a Two Pointer technique where we **systematically discard impossible candidates** while searching for the answer.

Unlike Reader / Writer, we are **not building** a finished portion.

Unlike Symmetric Converging, we are **not processing mirror pairs**.

Instead, every pointer movement is backed by a **proof** that certain candidates can never lead to the optimal solution.

The search space becomes smaller after every iteration.

---

# 2. When Should This Pattern Come To Mind?

This pattern usually appears when you see:

* sorted array
* pair sum
* maximize
* minimize
* closest
* target
* area
* search space reduction

Immediately ask yourself:

> **"Can I mathematically prove that one entire side is impossible?"**

If the answer is yes,

think **Elimination**.

---

# 3. Mental Model

Imagine searching for a hidden treasure inside a long hallway.

You have two guards.

One starts from the left.

One starts from the right.

After checking a possibility,

you don't randomly move.

Instead,

you permanently lock one section of the hallway because you have proof that the treasure cannot be there.

Every movement shrinks the search space.

That is the Elimination pattern.

---

# 4. Thought Process

Suppose the problem asks:

> Find two numbers whose sum equals a target.

The array is sorted.

Don't think about code.

Ask yourself:

### Question 1

Can sorting help me predict what happens if I move left or right?

Yes.

Because the array is monotonic.

---

### Question 2

If the current sum is too small,

which pointer should move?

The left pointer.

Moving the right pointer left would only decrease the sum even further.

Those pairs become impossible.

---

### Question 3

If the current sum is too large,

which pointer should move?

The right pointer.

Moving the left pointer right would only increase the sum further.

Again,

an entire group of pairs becomes impossible.

---

### Question 4

Can I prove that I never need to revisit discarded pairs?

Yes.

That proof is the heart of this variation.

---

# 5. Brute Force

A beginner solution is:

For every element,

check every remaining element.

Time Complexity

```text
O(n²)
```

Most comparisons are unnecessary.

---

# 6. Optimization Journey

Brute Force

↓

Compare every pair.

↓

Observation

The array is sorted.

↓

Question

Can sorting predict future comparisons?

↓

Yes.

↓

Current comparison tells us
which entire side can never succeed.

↓

Discard it forever.

↓

Continue with a smaller search space.

---

# 7. Repeated Work Being Eliminated

Without Elimination:

* Same impossible pairs are considered again.
* Search space never shrinks.

With Elimination:

Every pointer movement permanently removes impossible candidates.

No discarded pair is ever checked again.

---

# 8. Core Invariant

This is the most important idea.

At every step:

```text
Everything outside the two pointers
has already been proven impossible.
```

Notice the difference.

Reader / Writer

Finished.

Symmetric

Processed.

Elimination

Impossible.

---

# 9. Pointer Responsibilities

## Left Pointer

Represents the smallest remaining candidate.

Moves only when increasing the current value may improve the answer.

---

## Right Pointer

Represents the largest remaining candidate.

Moves only when decreasing the current value may improve the answer.

Neither pointer moves randomly.

Every movement requires a proof.

---

# 10. Why Doesn't the Other Pointer Move?

Suppose

Current Sum

```text
5
```

Target

```text
8
```

The sum is too small.

Should we move Right?

No.

Moving Right left decreases the sum even more.

Every pair using the current Left with a smaller Right is guaranteed to fail.

Only moving Left has any chance of reaching the target.

This is elimination by proof.

---

# 11. Representative Problem — Container With Most Water

## Problem Statement

You are given heights of vertical lines.

Choose two lines that hold the maximum amount of water.

Return the maximum area.

Example

```text
[1,8,6,2,5,4,8,3,7]
```

---

## Step 1 — Brute Force

Check every pair.

Calculate area.

Keep the maximum.

Time

```text
O(n²)
```

---

## Step 2 — Observation

Area depends on

```text
width × shorter height
```

The taller wall never limits the water.

The shorter wall always does.

---

## Step 3 — Important Question

Suppose

Left

```text
3
```

Right

```text
8
```

Width

```text
10
```

Area

```text
3 × 10
```

Which pointer should move?

Not the taller one.

Why?

Width decreases.

The limiting height stays

```text
3
```

Area can never improve.

Those containers are impossible.

Eliminate them.

---

## Step 4 — The Key Proof

Move the shorter wall.

Two possibilities exist.

### Case 1

The next wall is shorter.

Area decreases.

---

### Case 2

The next wall is taller.

The limiting height increases.

Area might increase.

Only this movement has potential.

Therefore,

move the shorter pointer.

---

## Step 5 — What Gets Eliminated?

Every container using the current shorter wall.

They have all been mathematically proven suboptimal.

The search space becomes smaller.

---

# 12. Pattern Recognition Tricks

Whenever you read:

* sorted array
* maximize
* minimize
* pair
* area
* closest
* target

Ask:

> **"Can I prove one side is impossible?"**

If yes,

think Elimination.

---

# 13. Common Mistakes

### Mistake 1

Moving pointers randomly.

Every movement needs proof.

---

### Mistake 2

Thinking both pointers should move.

Usually only one side can be eliminated.

---

### Mistake 3

Moving the taller wall in Container With Most Water.

The shorter wall still limits the area.

The proof breaks.

---

### Mistake 4

Ignoring why the array is sorted.

Sorting provides predictability.

Without predictability,

elimination is impossible.

---

# 14. Edge Cases

Target found immediately.

---

No valid pair.

---

Duplicate values.

---

Equal heights.

Both pointer movements are valid,

but moving one is sufficient.

---

# 15. Complexity Proof

Each pointer only moves inward.

Neither pointer revisits an index.

Each movement removes part of the search space.

Therefore,

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# 16. Relation With Other Two Pointer Variations

Reader / Writer

Build a finished portion.

---

Symmetric Converging

Process mirror pairs.

---

Elimination

Discard impossible candidates.

---

Composition

Reduce to another solved problem.

---

Finalization

Process the side whose answer is already fixed.

---

# 17. Quick Revision

Purpose

Shrink the search space.

Invariant

Everything outside the pointers
has already been proven impossible.

Recognition

* Sorted
* Target
* Maximize
* Minimize
* Pair
* Area

Optimization

Discard impossible work.

Time

```text
O(n)
```

Space

```text
O(1)
```

Memory Hook

> **Never move a pointer without a proof. Every move must eliminate something forever.**
