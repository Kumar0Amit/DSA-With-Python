# Fixed Window

## Part 3 — Pattern Recognition, Decision Making, Common Mistakes, Complexity, and Pattern Evolution

---

# Recognizing a Fixed Window Problem

One of the biggest mistakes beginners make is trying to memorize problem names.

For example:

* "Maximum Sum of K Elements"
* "Find All Anagrams"
* "Permutation in String"

These are **not** the pattern.

They are merely different applications of the same idea.

Instead of memorizing problems, train yourself to recognize the **characteristics** of the problem.

---

## Recognition Question 1

> **Am I processing contiguous data?**

Sliding Window only works when the data must remain together.

Common words include:

* Subarray
* Substring
* Consecutive
* Continuous

If the problem allows arbitrary elements from anywhere in the array, Sliding Window is usually **not** the correct pattern.

---

## Recognition Question 2

> **Is the window size already known?**

Examples:

```text id="hvgdqu"
Exactly K elements

Every K elements

Window of size K

Substring of length M
```

Notice something.

The problem has already fixed the size.

You do **not** need to discover it.

This is one of the strongest indicators of the Fixed Window variation.

---

## Recognition Question 3

> **Am I rebuilding almost identical information?**

Suppose two consecutive windows are

```text id="s5x7gq"
2 1 5

↓

1 5 1
```

Ask yourself

> "Am I recomputing something that I already knew?"

If the answer is yes,

there is repeated work waiting to be eliminated.

---

## Recognition Question 4

> **Can I update the answer locally?**

Instead of asking

> "Can I compute the next answer?"

ask

> **"Can I update the previous answer?"**

If you can express the next state as

```text id="8j7xrk"
Old State

↓

Remove Leaving Contribution

↓

Add Entering Contribution

↓

New State
```

then you are almost certainly looking at a Fixed Window problem.

---

# Fixed Window Recognition Checklist

Before thinking about code, mentally walk through this checklist.

```text id="brt4bk"
□ Contiguous data?

□ Fixed window size?

□ Overlapping windows?

□ Repeated work?

□ State can be updated locally?

□ Only one element leaves?

□ Only one element enters?
```

If most of these are true,

Fixed Window should immediately come to mind.

---

# Decision Tree

Whenever you encounter a new interview problem, use the following reasoning process.

```text id="xpw8zy"
Does the problem involve

Subarray
Substring
Consecutive
Continuous

↓

YES

↓

Does the problem specify

Exactly K?

Window Size K?

Length M?

↓

YES

↓

Think Fixed Window

↓

What information must be maintained?

↓

How can I update it locally?
```

This decision tree is much more useful than memorizing problem names.

---

# General Thinking Template

Every Fixed Window problem can be discovered using the same reasoning process.

```text id="ty8g97"
Problem

↓

Brute Force

↓

Repeated Work

↓

Observation

↓

Maintained State

↓

Core Invariant

↓

Remove Leaving Contribution

↓

Add Entering Contribution

↓

Update Answer
```

Notice something interesting.

There is no mention of

* arrays,
* strings,
* pointers,
* or Python.

This is because the thinking process is independent of the programming language.

---

# Common Maintained States

Different problems require different information.

The Sliding Window pattern itself does not care what information you maintain.

Below are some of the most common maintained states.

| Problem Requirement | Maintained State                                   |
| ------------------- | -------------------------------------------------- |
| Maximum Sum         | Running Sum                                        |
| Average             | Running Sum                                        |
| Product             | Running Product *(only when mathematically valid)* |
| Count Evens         | Running Count                                      |
| Count Odds          | Running Count                                      |
| Character Frequency | Frequency Map                                      |
| Inventory           | Frequency Map                                      |
| Presence            | Set                                                |
| Distinct Count      | Frequency Map + Distinct Counter                   |

Notice that all of these follow the same update rule.

```text id="apxsvl"
Remove old contribution

↓

Add new contribution
```

Only the information being maintained changes.

---

# Common Mistakes

One of the fastest ways to improve at algorithms is to understand why solutions fail.

---

## Mistake 1

### Recomputing Everything

Many beginners correctly identify the window,

but still compute everything from scratch.

Example:

```text id="3aegwb"
Compute the sum of every window independently.
```

Correct.

But inefficient.

The whole purpose of the pattern is to avoid rebuilding information.

---

## Mistake 2

### Building Every Window Again

Some implementations recreate the maintained state every time.

For example,

creating a new frequency map for every window.

This destroys the optimization completely.

The maintained state should evolve continuously.

---

## Mistake 3

### Forgetting to Remove Expired Information

Suppose an element leaves the window,

but its contribution remains.

Now the maintained state represents

```text id="rl9j2j"
Current Window

+

Expired Information
```

The invariant is broken.

---

## Mistake 4

### Forgetting to Add New Information

Now the maintained state represents

```text id="j0q3jz"
Current Window

-

Missing Information
```

Again,

the invariant breaks.

---

## Mistake 5

### Breaking Synchronization

The window and the maintained state must always describe exactly the same region.

If one changes before the other,

the algorithm temporarily becomes incorrect.

Always think:

> **Is my maintained state synchronized with my current window?**

---

# Complexity Proof

Many books simply state:

```text id="u9hyl8"
Time Complexity = O(n)
```

Let's understand why.

Suppose

```text id="0egjlwm"
Array Size = n

Window Size = k
```

The first window is built once.

After that,

every movement performs exactly two updates.

```text id="3gl6pd"
Remove one contribution.

Add one contribution.
```

Each update is constant time.

The window slides

```text id="qcv3y7"
n - k
```

times.

Therefore,

the total work grows linearly with the input size.

No element is processed repeatedly inside multiple recomputations.

The repeated work has been eliminated.

---

# Relation to Hashing

Hashing taught us an important lesson.

Instead of searching repeatedly,

maintain useful information.

Examples include:

* Frequencies
* Presence
* Mappings

Fixed Window takes the same philosophy one step further.

Instead of maintaining information about the entire input,

we maintain information about **only the current window**.

---

# Relation to Two Pointers

Two Pointers introduced another important concept.

Every pointer has a responsibility.

Instead of asking

> "Which pointer moves?"

we ask

> **"Why does this pointer move?"**

Fixed Window preserves that philosophy.

The responsibilities become:

Left Pointer

```text id="hm4hbo"
Remove expired information.
```

Right Pointer

```text id="vk02ah"
Introduce new information.
```

Pointer movement is simply a consequence of maintaining the invariant.

---

# Relation to Variable Window

Many learners confuse these two variations.

The difference is fundamental.

## Fixed Window

The problem determines the size.

Your responsibility is to maintain the state.

---

## Variable Window

The problem determines a condition.

Your responsibility is to discover the correct size while maintaining validity.

Think of it this way.

### Fixed Window asks

> **"How do I efficiently process every window?"**

### Variable Window asks

> **"How large should the current window become?"**

The optimization goals are completely different.

---

# Pattern Evolution

This chapter fits naturally into the larger journey of algorithmic thinking.

```text id="g07d6m"
Brute Force

↓

Hashing

(Maintain Information)

↓

Two Pointers

(Maintain Pointer Responsibilities)

↓

Fixed Window

(Maintain Window State)

↓

Variable Window

(Maintain Window Validity)

↓

Advanced Sliding Window

(Maintain Multiple States and Complex Invariants)
```

Notice how each pattern builds on ideas from the previous one.

Very few algorithmic ideas appear suddenly.

Most are natural evolutions of earlier concepts.

---

# Quick Revision

If you have only two minutes before an interview, remember these ideas.

* The problem already fixes the window size.
* Consecutive windows overlap heavily.
* Eliminate repeated work by maintaining state.
* The maintained state must always represent the current window.
* Left pointer removes expired information.
* Right pointer introduces new information.
* Never rebuild information that can be updated locally.

---

# One-Sentence Memory Hook

> **Fixed Window is the art of preserving knowledge. Every slide removes only what expired, adds only what arrived, and carries everything else forward.**

