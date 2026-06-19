# Elimination — Pattern DNA

## Pattern Name

**Elimination**

---

## Goal

Reduce the search space by **permanently discarding impossible candidates**.

---

## Core Idea

Every pointer movement must have a mathematical proof.

If moving a pointer cannot improve the answer, eliminate that entire side forever.

---

## Core Invariant

Everything **outside** the two pointers has already been proven impossible.

Those candidates will never become part of the final answer.

---

## Pointer Responsibilities

### Left Pointer

* Represents the smallest remaining candidate.
* Moves only when increasing the value may improve the answer.

### Right Pointer

* Represents the largest remaining candidate.
* Moves only when decreasing the value may improve the answer.

Neither pointer moves randomly.

Every movement is justified by proof.

---

## Pointer Movement

### Sum is Too Small

```text
Move Left →
```

Reason:

Increasing the smaller value is the only way to increase the sum.

---

### Sum is Too Large

```text
← Move Right
```

Reason:

Decreasing the larger value is the only way to decrease the sum.

---

### Container With Most Water

Move the **shorter wall**.

Reason:

The shorter wall limits the water level.

Moving the taller wall cannot increase the area because:

* Width decreases.
* Limiting height remains unchanged.

---

## Recognition Keywords

If the problem mentions:

* sorted array
* target
* pair
* maximize
* minimize
* closest
* area
* optimize

Ask yourself:

> **"Can I eliminate one entire side with proof?"**

If yes,

think **Elimination**.

---

## Representative Problems

### Easy

* Two Sum II

### Medium

* Container With Most Water

---

## Common Mistakes

❌ Moving a pointer without justification.

---

❌ Moving both pointers when only one side has been proven impossible.

---

❌ Ignoring the importance of a sorted array.

Without monotonicity,

elimination usually isn't possible.

---

❌ Moving the taller wall in Container With Most Water.

The limiting height never changes.

Area cannot improve.

---

## Pattern Evolution

```text
Two Sum II
        │
        ▼
Container With Most Water
        │
        ▼
3Sum (after fixing one element)
        │
        ▼
4Sum
        │
        ▼
k-Sum
```

---

## Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

## Memory Hook

> **Never move a pointer unless you can prove what you're eliminating.**
