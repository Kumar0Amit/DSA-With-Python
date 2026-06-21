# Sliding Window

> **"Sliding Window is not an algorithm. It is a way of carrying forward information instead of rebuilding it."**

---

# Welcome

Welcome to the **Sliding Window** chapter of **The Algorithm Engineer Handbook**.

This chapter is not a collection of interview solutions.

It is a collection of **algorithmic ideas**.

The goal is **not** to memorize patterns such as:

* Fixed Window
* Variable Window
* At Most K
* Minimum Window

Instead, the goal is to understand **why** Sliding Window exists, **when** it naturally appears, and **how** to derive it from first principles.

By the end of this chapter, you should be able to:

* Recognize Sliding Window problems during interviews.
* Derive the algorithm from brute force.
* Explain every optimization mathematically.
* Implement every variation confidently from scratch.

---

# Why Does Sliding Window Exist?

Every algorithmic optimization starts with one question:

> **"What repeated work am I performing?"**

Sliding Window exists because many brute-force solutions repeatedly process **almost identical contiguous regions** of an array or string.

Instead of rebuilding information for every region, we carry forward information from the previous region.

The optimization is **not** moving two pointers.

The optimization is **maintaining state**.

---

# The Optimization Journey

Imagine the following problem.

> Find the maximum sum of every 3 consecutive elements.

### Brute Force

```
Window 1

2 1 5

Compute sum.


Window 2

1 5 1

Compute sum again.


Window 3

5 1 3

Compute sum again.
```

Every new window recomputes almost everything.

Most of the previous work is thrown away.

---

## Observation

When the window moves by one position,

only **two things change**.

```
Old Window

2 1 5

↓

New Window

1 5 1
```

Only

* `2` leaves
* `1` enters

Everything else remains unchanged.

Instead of rebuilding the sum,

we update it.

```
Old Sum

↓

Subtract Leaving Element

↓

Add Entering Element

↓

New Sum
```

This single observation gives birth to the Sliding Window technique.

---

# Sliding Window Is About Maintaining State

Many beginners believe Sliding Window is about moving pointers.

It is not.

The pointers simply tell us **what information expires** and **what information becomes available**.

The real focus is the **maintained state**.

Examples of maintained state include:

* Running Sum
* Running Count
* Frequency Map
* Character Inventory
* Historical Maximum
* Running Minimum
* Average
* Presence Information

Different problems maintain different information.

The algorithm changes very little.

The maintained state changes.

---

# The Core Question

Whenever you encounter a new problem, ask:

> **What information am I rebuilding again and again?**

If that information can be updated locally when the window moves,

Sliding Window is a strong candidate.

---

# Evolution From Previous Patterns

Sliding Window is not an isolated technique.

It naturally evolves from patterns learned earlier.

## Hashing taught us

Maintain useful information.

Examples:

* Frequency
* Mapping
* Presence
* Counts

---

## Two Pointers taught us

Maintain pointer invariants.

Instead of asking

> Which pointer moves?

we ask

> What responsibility does each pointer currently have?

---

## Sliding Window combines both ideas

Now we maintain

> **the state of an entire moving window.**

Pointers simply update that maintained state.

---

# Two Major Families

Sliding Window is best understood as two independent variations.

---

## 1. Fixed Window

The problem itself determines the window size.

Examples

* Maximum Sum of K Consecutive Elements
* Count Even Numbers in a Window
* Permutation in String
* Find All Anagrams in a String

The main question becomes

> **How can I efficiently update the maintained state while the fixed window moves?**

---

## 2. Variable Window

The problem determines a **condition**, not the size.

Examples

* Minimum Size Subarray Sum
* Longest Substring Without Repeating Characters
* Longest Substring with At Most K Distinct Characters
* Longest Repeating Character Replacement
* Minimum Window Substring

The main question becomes

> **How large should the window become before I shrink it?**

---

# Fixed Window vs Variable Window

| Fixed Window                          | Variable Window                             |
| ------------------------------------- | ------------------------------------------- |
| Window size is predetermined          | Window size is discovered during execution  |
| Left and right pointers move together | Left and right pointers move independently  |
| State changes once per slide          | State changes while expanding and shrinking |
| Goal is efficient updates             | Goal is maintaining validity                |

---

# Recognition Checklist

Whenever you read a problem, ask yourself the following questions.

### Question 1

Am I processing **contiguous** elements?

Keywords include:

* Subarray
* Substring
* Consecutive
* Continuous

---

### Question 2

Does brute force repeatedly process overlapping regions?

If the answer is yes,

there is repeated work.

---

### Question 3

Can information from the previous region be reused?

If yes,

there is likely a maintained state.

---

### Question 4

Can I update that maintained state by only processing:

* the leaving element
* the entering element

instead of rebuilding everything?

If yes,

Sliding Window is a strong candidate.

---

# Pattern Decision Tree

```
Problem mentions

Exactly K
Exactly Length K
Every K Consecutive Elements

↓

Think Fixed Window
```

---

```
Problem mentions

At Most K

↓

Think Variable Window
```

---

```
Problem mentions

Minimum

↓

Expand

↓

Shrink
```

---

```
Problem mentions

Longest

↓

Maintain validity

↓

Expand as much as possible
```

---

```
Problem mentions

Substring
Subarray
Continuous
Consecutive

↓

Think Sliding Window
```

---

# General Thinking Process

Never memorize templates.

Instead ask the following questions.

```
What information do I need?

↓

What repeated work exists?

↓

Can I maintain that information?

↓

What should my maintained state be?

↓

What invariant must always remain true?

↓

Which pointer currently has unfinished work?

↓

Can I update the maintained state locally?

↓

Derive the algorithm.
```

---

# Folder Structure

```
Sliding_Window/

│── README.md

├── Fixed_Window/
│     │── Fixed_Window.md
│     │── Fixed_Window_DNA.md
│     │── Maximum_Sum_of_K.py
│     │── Count_Even_In_Window.py
│     │── Permutation_in_String.py
│     │── Find_All_Anagrams.py
│
├── Variable_Window/
│     │── Variable_Window.md
│     │── Variable_Window_DNA.md
│     │── Minimum_Size_Subarray_Sum.py
│     │── Longest_Substring_Without_Repeating.py
│     │── Longest_Substring_At_Most_2_Distinct.py
│     │── Character_Replacement.py
```

Each variation contains:

* A complete handbook
* A one-minute DNA revision sheet
* Fully documented Python implementations
* Dry runs
* Mathematical proofs
* Interview notes
* Practice roadmap

---

# How This Handbook Is Organized

Every variation follows the same learning path.

```
Brute Force

↓

Observation

↓

Repeated Work

↓

Maintained State

↓

Invariant

↓

Pointer Responsibilities

↓

Optimized Algorithm

↓

General Template

↓

Representative Problems

↓

Practice
```

This order is intentional.

Algorithms should be **discovered**, not memorized.

---

# Learning Philosophy

Throughout this handbook, every algorithm is derived from first principles.

For every problem we answer:

* Why does this optimization exist?
* What repeated work is being eliminated?
* What maintained state is chosen?
* Why is that state sufficient?
* What invariant guarantees correctness?
* Why does each pointer move?
* Why does the other pointer not move?
* Why is the optimization mathematically correct?

Only after answering these questions do we implement the algorithm.

---

# What You Should Gain From This Chapter

After completing this chapter, you should be able to:

* Recognize Sliding Window problems without memorizing keywords.
* Identify repeated work immediately.
* Choose the correct maintained state.
* Derive the invariant naturally.
* Explain pointer responsibilities confidently.
* Write the algorithm from scratch.
* Defend its correctness in an interview.

---

# Memory Hook

> **Sliding Window is not about moving pointers.**
>
> **Sliding Window is about carrying forward information instead of rebuilding it.**
