# Symmetric Converging Pattern

# 1. What is the Symmetric Converging Pattern?

Symmetric Converging is a Two Pointer technique where two pointers start from **opposite ends** of a sequence and move **towards each other**.

Unlike the Reader / Writer variation, both pointers perform the **same type of work**. They inspect, compare, or swap a **pair of symmetric positions** before moving inward.

The goal is to process one symmetric pair at a time until every required pair has been handled.

---

# 2. When Should This Pattern Come To Mind?

If a problem contains words like:

* reverse
* palindrome
* mirror
* symmetry
* opposite ends
* compare first and last
* swap from both sides

Immediately ask yourself:

> **"Can I solve this by processing one pair from the outside and moving inward?"**

If the answer is yes, think **Symmetric Converging**.

---

# 3. Mental Model

Imagine two people painting a fence.

One starts from the left.

One starts from the right.

After both finish painting one plank each, they move one step toward the center.

They never repaint the same plank.

Eventually, they meet in the middle.

Every plank outside them is already finished.

That is exactly how Symmetric Converging works.

---

# 4. Thought Process

Suppose the problem asks:

> Reverse a string in-place.

Don't think about code.

Ask yourself:

### Question 1

What should the final string look like?

Answer

The first character should become the last.

The second should become the second last.

The third should become the third last.

Every position has a mirror position.

---

### Question 2

Can I directly exchange each mirror pair?

Yes.

---

### Question 3

Do I need another array?

No.

After swapping one pair,

those positions are already finished forever.

---

### Question 4

Can I process every pair exactly once?

Yes.

That naturally creates two pointers.

---

# 5. Brute Force

A beginner might think:

* Create another array.
* Copy the string in reverse order.
* Copy it back.

This works.

But it needs extra space.

Instead,

we can simply swap mirror positions.

---

# 6. Optimization Journey

Brute Force

↓

Extra array

↓

Observation

Every character already has a mirror position.

↓

Question

Can I directly exchange both positions?

↓

Yes.

↓

Need one pointer on each end.

↓

Process one pair.

↓

Move inward.

↓

Repeat.

---

# 7. Repeated Work Being Eliminated

Without this pattern:

* creating another array
* copying values twice
* revisiting already processed positions

Symmetric Converging removes all repeated work.

Every pair is processed exactly once.

---

# 8. Core Invariant

This is the heart of the pattern.

At every moment:

```text
Everything outside the two pointers
has already been correctly processed.
```

Depending on the problem, "processed" may mean:

* swapped
* compared
* verified

The invariant must never break.

---

# 9. Pointer Responsibilities

## Left Pointer

* Point to the next unprocessed element from the left.
* Participate in one symmetric operation.

---

## Right Pointer

* Point to the next unprocessed element from the right.
* Participate in one symmetric operation.

Unlike Reader / Writer,

both pointers have equal responsibility.

---

# 10. Why Do Both Pointers Usually Move?

Suppose we swap

```text
A          Z
```

Those two positions are finished forever.

There is no reason to revisit them.

So both pointers move inward.

---

# 11. Why Does Only One Pointer Sometimes Move?

Some problems introduce **invalid characters**.

Example:

```text
A man, a plan, a canal: Panama
```

We only care about letters and digits.

If the left pointer is currently on:

```text
,
```

there is no valid comparison yet.

The left pointer must keep moving until it reaches a valid character.

The right pointer waits.

Only after both pointers point to valid characters can we compare them.

The invariant still holds because no valid pair has been skipped.

---

# 12. Representative Problem — Reverse String

## Problem Statement

Given a character array,

reverse it **in-place**.

Example

```text
Input

['h','e','l','l','o']

Output

['o','l','l','e','h']
```

---

## Step 1 — Understand The Goal

The first character must become the last.

The last must become the first.

Second ↔ Second Last

Third ↔ Third Last

Every character has one mirror position.

---

## Step 2 — Brute Force

Create another array.

Traverse from the end.

Copy values.

Works.

Extra Space:

```text
O(n)
```

---

## Step 3 — Observation

Do we really need another array?

No.

If we exchange both mirror characters,

both positions become correct immediately.

---

## Step 4 — Invent The Two Pointers

Left starts from

```text
0
```

Right starts from

```text
n-1
```

Each iteration:

* Swap
* Move Left
* Move Right

Repeat until they meet.

---

## Step 5 — Dry Run

Initial

```text
h e l l o
L       R
```

Swap

```text
o e l l h
  L   R
```

Swap

```text
o l l e h
    L R
```

Pointers meet.

Done.

Notice something.

Every swap permanently finished two positions.

Nothing outside the pointers needed to be touched again.

---

# 13. Pattern Recognition Tricks

Whenever you read:

* reverse
* palindrome
* mirror
* compare ends
* symmetric

Ask:

> **"Does every position have one mirror partner?"**

If yes,

Symmetric Converging is a strong candidate.

---

# 14. Common Mistakes

### Mistake 1

Moving only one pointer after processing a valid pair.

Result

One side gets processed repeatedly.

The invariant breaks.

---

### Mistake 2

Using

```text
left <= right
```

without understanding why.

Some problems don't need to process the middle element.

Always understand the stopping condition.

---

### Mistake 3

Comparing invalid characters.

Problems like Valid Palindrome require skipping punctuation and spaces first.

---

### Mistake 4

Thinking both pointers always move together.

Not always.

Sometimes one pointer waits while the other skips invalid elements.

---

# 15. Edge Cases

Single character

Already reversed.

---

Empty string

Return immediately.

---

Even length

Pointers cross.

---

Odd length

Pointers meet at the middle.

Middle character never needs swapping.

---

All punctuation (Palindrome)

Pointers keep skipping until finished.

---

# 16. Complexity Proof

Each pointer moves only toward the center.

Neither pointer moves backward.

Neither pointer revisits an index.

Therefore:

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# 17. Relation With Other Two Pointer Variations

Reader / Writer

Goal

Build a finished portion.

---

Symmetric Converging

Goal

Process one symmetric pair.

---

Elimination

Goal

Discard impossible search space.

---

Composition

Goal

Reduce a larger problem into a solved one.

---

Finalization

Goal

Process only the side whose answer is already fixed.

---

# 18. Quick Revision

Purpose

Process symmetric pairs.

Invariant

Everything outside the pointers is already correct.

Pointer Movement

Usually both.

Sometimes one waits while the other skips invalid characters.

Recognition

* Reverse
* Palindrome
* Mirror
* Symmetry

Optimization

Avoid extra arrays.

Avoid revisiting processed pairs.

Time

```text
O(n)
```

Space

```text
O(1)
```

Memory Hook

> **Process one mirror pair. Move inward. Repeat.**
