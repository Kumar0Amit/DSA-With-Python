# Variable Window

## Part 3 — Pattern Recognition, Decision Tree, Common Mistakes, Complexity, Pattern Evolution, and Memory Hooks

---

# Recognizing a Variable Window Problem

One of the biggest reasons people struggle with Sliding Window is that they try to memorize problem names.

Examples:

* Minimum Size Subarray Sum
* Longest Substring Without Repeating Characters
* Character Replacement
* Fruits Into Baskets
* Minimum Window Substring

These all look different.

But an algorithm engineer ignores the story.

Instead, they ask:

> **"What property do all these problems share?"**

The answer is:

> **The correct window size is unknown and must be discovered while maintaining a validity condition.**

That is the real pattern.

---

# Recognition Question 1

> **Is the data contiguous?**

Look for words such as

* Subarray
* Substring
* Continuous
* Consecutive

Variable Window only works on contiguous regions.

If elements can be chosen from arbitrary positions,

Sliding Window is usually not the correct pattern.

---

# Recognition Question 2

> **Is the window size unknown?**

Ask yourself

"Can I determine the window size before I start?"

If the answer is

"No"

then Variable Window becomes a strong candidate.

Examples

```text
Smallest subarray

Longest substring

Minimum window

At least

At most

Contains

Without repeating
```

These phrases usually indicate that the algorithm must discover the window size.

---

# Recognition Question 3

> **Does the problem define a validity condition?**

Every Variable Window problem revolves around one rule.

Examples

```text
Sum >= Target
```

```text
Distinct Characters <= 2
```

```text
No Duplicate Characters
```

```text
Window Contains Every Required Character
```

Instead of thinking

"What should my answer be?"

first identify

"What makes a window valid?"

Everything else depends on this answer.

---

# Recognition Question 4

> **Can I update the information locally?**

Suppose the window grows by one element.

Can you update the maintained state

without recomputing everything?

Examples

* Running Sum
* Frequency Map
* Distinct Count
* Maximum Frequency

If yes,

Sliding Window is probably applicable.

---

# Variable Window Recognition Checklist

Before writing code,

walk through this checklist.

```text
□ Contiguous data?

□ Unknown window size?

□ Window validity exists?

□ Can I maintain that validity efficiently?

□ Does expanding add useful information?

□ Does shrinking remove unnecessary information?

□ Can both pointers move independently?
```

If most of these answers are

Yes,

think

Variable Window.

---

# Decision Tree

Use this reasoning process whenever you see a new interview problem.

```text
Contiguous Data?

↓

YES

↓

Window Size Known?

↓

YES

↓

Fixed Window

-----------------------------------------

NO

↓

Window Validity Exists?

↓

YES

↓

Variable Window

↓

What information determines validity?

↓

Maintain that information

↓

Expand

↓

Become Valid

↓

Shrink

↓

Repeat
```

Notice that the decision is made

before

thinking about Python,

before

thinking about pointers,

and

before

thinking about code.

---

# General Thinking Framework

Every Variable Window problem can be derived using the same reasoning process.

```text
Problem

↓

Brute Force

↓

Repeated Work

↓

Unknown Window Size

↓

Maintained State

↓

Validity Condition

↓

Expand

↓

Become Valid

↓

Shrink

↓

Lose Validity

↓

Expand Again

↓

Optimal Solution
```

Notice that

"Expand"

and

"Shrink"

are consequences.

The real driver is

the validity condition.

---

# Common Maintained States

Different problems require different maintained information.

| Problem                   | Maintained State                  |
| ------------------------- | --------------------------------- |
| Minimum Size Subarray Sum | Running Sum                       |
| Longest Unique Substring  | Frequency Map                     |
| Character Replacement     | Frequency Map + Maximum Frequency |
| At Most K Distinct        | Frequency Map + Distinct Counter  |
| Fruits Into Baskets       | Frequency Map + Distinct Counter  |
| Minimum Window Substring  | Need / Have + Frequency Maps      |

The maintained state changes.

The framework remains identical.

---

# Common Validity Conditions

This is one of the most important tables in the entire chapter.

| Problem                   | Validity Condition              |
| ------------------------- | ------------------------------- |
| Minimum Size Subarray Sum | Running Sum ≥ Target            |
| Longest Unique Substring  | No Character Frequency > 1      |
| Character Replacement     | Window Size − Max Frequency ≤ k |
| At Most K Distinct        | Distinct Count ≤ k              |
| Fruits Into Baskets       | Distinct Count ≤ 2              |
| Minimum Window Substring  | Have == Need                    |

When you solve a new Variable Window problem,

your first task is to discover

this table entry.

---

# Common Mistakes

## Mistake 1

Thinking about pointers first.

Wrong question

> Which pointer should move?

Correct question

> What is my current validity condition?

The pointer movement follows from the validity.

---

## Mistake 2

Shrinking an invalid window.

Suppose

Running Sum

is still below the target.

Removing elements cannot help.

Expand instead.

---

## Mistake 3

Continuing to expand after the window is already valid.

Many optimization problems ask for

the smallest

valid window.

Once the window becomes valid,

you should immediately ask

"Can I make it smaller?"

---

## Mistake 4

Breaking synchronization.

The maintained state must always describe

the current window.

If the maintained state lags behind,

the validity check becomes incorrect.

---

## Mistake 5

Confusing

window size

with

validity.

The size changes naturally.

Validity determines

when

the pointers should move.

---

# Complexity Proof

Many learners assume

two pointers moving

must mean

O(2n).

That is incorrect.

Think carefully.

The right pointer

starts at the beginning

and reaches the end

exactly once.

The left pointer

also starts at the beginning

and reaches the end

at most once.

Neither pointer ever moves backward.

Therefore,

each element enters the window once

and leaves the window once.

No element is processed repeatedly.

Hence,

the total work is linear.

```text
Time Complexity

O(n)
```

This reasoning applies to almost every Variable Window algorithm.

---

# Relation to Fixed Window

Fixed Window

↓

Known window size

↓

Maintain state

↓

Slide together

---

Variable Window

↓

Unknown window size

↓

Maintain state

*

Maintain validity

↓

Expand and shrink independently

The Variable Window pattern is not a completely new algorithm.

It is an evolution of Fixed Window.

---

# Pattern Evolution

Your learning journey now looks like this.

```text
Hashing

↓

Maintain Information

↓

Two Pointers

↓

Assign Responsibilities

↓

Fixed Window

↓

Maintain Window State

↓

Variable Window

↓

Maintain Window Validity

↓

Advanced Sliding Window

↓

Maintain Multiple States
and
Complex Invariants
```

Every pattern builds upon the previous one.

Nothing appears suddenly.

Algorithmic thinking evolves gradually.

---

# Quick Revision

If you have only one minute before an interview,

remember these ideas.

* The window size is unknown.
* The maintained state determines validity.
* Expand until the window becomes valid.
* Shrink while it remains valid.
* The right pointer searches for validity.
* The left pointer searches for optimality.
* Every element enters once and leaves once.

---

# Memory Hook

> **Fixed Window maintains information.**
>
> **Variable Window maintains information to preserve validity.**
>
> **Expand to satisfy the condition. Shrink to optimize the answer. Repeat until the search is complete.**
