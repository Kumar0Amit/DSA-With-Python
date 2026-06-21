# Fixed Window DNA

> **One-Minute Revision Sheet**

---

# Pattern Name

**Fixed Sliding Window**

---

# Goal

Efficiently process **every contiguous window of a predetermined size** without rebuilding information from scratch.

---

# Core Idea

Consecutive windows overlap heavily.

Instead of recomputing the entire answer for every window,

carry forward information from the previous window.

Update only what changed.

---

# Optimization Journey

```text
Brute Force

↓

Repeated Work

↓

Observation

↓

Only one element leaves.

Only one element enters.

↓

Maintain State

↓

Update Locally

↓

O(n)
```

---

# Core Invariant

> **The maintained state always represents exactly the current window.**

---

# Maintained State

Depends entirely on the problem.

Examples:

| Problem        | Maintained State        |
| -------------- | ----------------------- |
| Maximum Sum    | Running Sum             |
| Average        | Running Sum             |
| Count Evens    | Running Count           |
| Count Odds     | Running Count           |
| Permutation    | Frequency Map           |
| Anagrams       | Frequency Map           |
| Distinct Count | Frequency Map + Counter |

---

# Pointer Responsibilities

### Left Pointer

Remove expired information.

---

### Right Pointer

Add newly available information.

---

# Movement Rules

```text
Window Moves

↓

Remove Left Contribution

↓

Add Right Contribution

↓

Update Answer
```

---

# Recognition Keywords

* Exactly K
* Window Size K
* Every K Consecutive
* Fixed Length
* Subarray
* Substring
* Continuous
* Consecutive

---

# Recognition Questions

Ask yourself:

* Is the data contiguous?
* Is the window size predetermined?
* Am I rebuilding almost identical information?
* Can I update the previous answer instead of recomputing it?

If the answer is **yes**, think **Fixed Window**.

---

# General Thinking Process

```text
What information do I need?

↓

What repeated work exists?

↓

Can I maintain that information?

↓

What leaves?

↓

What enters?

↓

Update State

↓

Update Answer
```

---

# Representative Problems

* Maximum Sum of K Consecutive Elements
* Count Even Numbers in a Window
* Permutation in String
* Find All Anagrams in a String

---

# Common Mistakes

* Recomputing every window
* Rebuilding the maintained state
* Forgetting to remove expired information
* Forgetting to add new information
* Breaking synchronization between the maintained state and the current window

---

# Complexity

### Time

```text
O(n)
```

Each slide performs constant work.

---

### Space

Depends on the maintained state.

Examples:

* Running Sum → **O(1)**
* Running Count → **O(1)**
* Frequency Map → **O(k)** in the general case (or bounded by the alphabet size for fixed-character problems)

---

# Pattern Evolution

```text
Hashing

↓

Maintain Information

↓

Two Pointers

↓

Maintain Pointer Responsibilities

↓

Fixed Window

↓

Maintain Window State
```

---

# Memory Hook

> **Fixed Window is not about moving a window.**
>
> **It is about carrying forward information instead of rebuilding it.**
