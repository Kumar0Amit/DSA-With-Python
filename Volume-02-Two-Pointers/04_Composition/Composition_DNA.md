# Composition — Pattern DNA

## Pattern Name

**Composition**

---

## Goal

Solve a harder problem by **reducing it into a problem you already know**.

Instead of inventing a completely new algorithm,

reuse an existing one.

---

## Core Idea

Break a larger problem into two parts.

1. Fix one part.
2. Solve the remaining smaller problem.

Example

```text
3Sum

↓

Fix one number

↓

2Sum
```

The difficult problem becomes one you already know how to solve.

---

## Core Invariant

Every unique fixed value is processed exactly once.

Every unique value combination is generated exactly once.

Duplicate work is never repeated.

---

## Pointer Responsibilities

### Fixed Pointer

* Chooses one element.
* Reduces the original problem.
* Skips duplicate fixed values.

---

### Left Pointer

* Solves the reduced problem.
* Uses the Elimination pattern.

---

### Right Pointer

* Solves the reduced problem.
* Uses the Elimination pattern.

Composition **reuses** another pattern instead of replacing it.

---

## Pointer Movement

### Before Two Sum

Move the **Fixed Pointer**

to the next unique value.

---

### During Two Sum

Use normal Elimination rules.

* Sum too small → Left++
* Sum too large → Right--

---

### After Finding a Valid Combination

Store the answer.

Skip duplicate Left values.

Skip duplicate Right values.

Continue searching.

---

## Recognition Keywords

If the problem contains:

* triplets
* quadruplets
* k numbers
* unique combinations
* all possible combinations
* sum equals target

Ask yourself:

> **"Can I fix one value and reduce the rest to a smaller problem?"**

If yes,

think **Composition**.

---

## Representative Problems

### Medium

* 3Sum

### Medium

* 3Sum Closest

### Hard

* 4Sum

---

## Common Mistakes

❌ Forgetting to sort first.

Sorting enables both:

* Elimination
* Duplicate skipping

---

❌ Processing duplicate fixed values.

Produces duplicate answers.

---

❌ Skipping duplicates before storing a valid answer.

Always store first.

Then skip duplicates.

---

❌ Thinking Composition is a new algorithm.

It is a combination of:

* Sorting
* Elimination
* Duplicate handling

---

## Pattern Evolution

```text
2Sum

↓

3Sum

↓

4Sum

↓

k-Sum
```

The same idea scales naturally.

---

## Complexity

Sorting

```text
O(n log n)
```

Outer Loop

```text
O(n)
```

Inner Two Sum

```text
O(n)
```

Overall

```text
O(n²)
```

Space

```text
O(1)
```

(ignoring the output list)

---

## Memory Hook

> **Fix one. Reduce the problem. Reuse the solution. Skip duplicates.**
