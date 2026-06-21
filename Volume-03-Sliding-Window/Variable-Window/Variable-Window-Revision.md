# Variable Window DNA

> **One-Minute Revision Sheet**

---

# Pattern Name

**Variable Sliding Window**

---

# Goal

Discover the **optimal window size** while continuously maintaining a **valid window**.

---

# Core Idea

Unlike Fixed Window,

the window size is **not known beforehand**.

The algorithm must grow and shrink the window while preserving a validity condition.

---

# Optimization Journey

```text
Brute Force

↓

Repeated Work

↓

Unknown Window Size

↓

Maintain State

↓

Maintain Validity

↓

Expand

↓

Become Valid

↓

Shrink

↓

Become Invalid

↓

Expand Again

↓

Optimal Answer
```

---

# Core Invariant

> **The maintained state always represents exactly the current window and correctly determines whether the window is valid.**

---

# Maintained State

Depends on the problem.

Examples

| Problem                   | Maintained State                  |
| ------------------------- | --------------------------------- |
| Minimum Size Subarray Sum | Running Sum                       |
| Longest Unique Substring  | Frequency Map                     |
| Character Replacement     | Frequency Map + Maximum Frequency |
| At Most K Distinct        | Frequency Map + Distinct Count    |
| Minimum Window Substring  | Need / Have + Frequency Maps      |

---

# Validity Condition

Every Variable Window problem has a condition.

Examples

* Running Sum ≥ Target
* Distinct Count ≤ K
* No Duplicate Characters
* Window Size − Max Frequency ≤ K
* Have == Need

---

# Pointer Responsibilities

### Right Pointer

* Expand the window.
* Gather more information.
* Try to satisfy the validity condition.

---

### Left Pointer

* Shrink the window.
* Remove unnecessary information.
* Keep the window optimal while preserving validity.

---

# Movement Rules

```text
Window Invalid

↓

Expand

↓

Update State

↓

Window Valid?

↓

NO

↓

Expand Again

-------------------------

YES

↓

Record Answer

↓

Shrink

↓

Still Valid?

↓

YES

↓

Shrink Again

↓

NO

↓

Expand Again
```

---

# Recognition Keywords

* Smallest
* Longest
* Minimum
* Maximum
* At Least
* At Most
* Contains
* Without Repeating
* Distinct
* Valid Window

---

# Recognition Questions

Ask yourself

* Is the data contiguous?
* Is the window size unknown?
* Does the problem define a validity condition?
* Can I maintain that validity efficiently?
* Should I expand or shrink?

If the answer is **yes**, think **Variable Window**.

---

# General Thinking Process

```text
What information do I need?

↓

How do I know if the window is valid?

↓

Expand

↓

Become Valid

↓

Can I improve the answer?

↓

Shrink

↓

Lose Validity

↓

Expand Again
```

---

# Representative Problems

* Minimum Size Subarray Sum
* Longest Substring Without Repeating Characters
* Longest Repeating Character Replacement

---

# Reinforcement Problems

* Longest Substring with At Most K Distinct Characters
* Fruits Into Baskets

---

# Advanced Representative Problem

* Minimum Window Substring

---

# Common Mistakes

* Thinking about pointers before validity.
* Shrinking an invalid window.
* Continuing to expand after becoming valid.
* Forgetting to update the maintained state.
* Confusing window size with validity.

---

# Complexity

### Time

**O(n)**

Each pointer moves forward at most once.

---

### Space

Depends on the maintained state.

Examples

* Running Sum → **O(1)**
* Frequency Map → **O(d)** where *d* is the number of distinct elements (or constant for a fixed alphabet).

---

# Pattern Evolution

```text
Hashing

↓

Maintain Information

↓

Two Pointers

↓

Pointer Responsibilities

↓

Fixed Window

↓

Maintain Window State

↓

Variable Window

↓

Maintain Window Validity
```

---

# Memory Hook

> **Expand until valid.**
>
> **Shrink while valid.**
>
> **The maintained state tells you when to switch between the two.**
