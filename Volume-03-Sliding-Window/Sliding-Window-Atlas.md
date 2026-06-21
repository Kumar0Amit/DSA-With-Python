# Sliding_Window_Atlas.md

> **Purpose:** This atlas is a rapid revision guide for the entire Sliding Window chapter. It is designed to help you recall the correct variation, maintained state, validity condition, pointer responsibilities, and representative problems in a few minutes.

---

# Sliding Window Pattern Evolution

```text
Brute Force
      │
      ▼
Repeated Work
      │
      ▼
Maintain Information
      │
      ▼
Sliding Window
      │
      ├──────────────► Fixed Window
      │                     │
      │                     ▼
      │              Known Window Size
      │
      └──────────────► Variable Window
                            │
                            ▼
                  Unknown Window Size
                  + Maintain Validity
```

---

# Fixed Window vs Variable Window

| Feature          | Fixed Window                                 | Variable Window                                |
| ---------------- | -------------------------------------------- | ---------------------------------------------- |
| Window Size      | Known before starting                        | Unknown, discovered during traversal           |
| Window Movement  | Left and Right move together                 | Left and Right move independently              |
| Goal             | Process every fixed-size window              | Discover the optimal window                    |
| Main Question    | How do I update the next window efficiently? | When should I expand? When should I shrink?    |
| Maintained State | Running information about the current window | Running information + validity condition       |
| Typical Keywords | Window of size K, Fixed length               | Smallest, Longest, At Most, At Least, Contains |

---

# Pattern Recognition Decision Tree

```text
Is the data contiguous?

        │
        ▼

      YES

        │
        ▼

Can I determine the window size before starting?

        │
   ┌────┴────┐
   │         │
 YES         NO
   │         │
   ▼         ▼

Fixed      Variable
Window     Window
```

---

# Fixed Window Atlas

| Problem                      | Maintained State | Window Validity              | Goal                | Representative |
| ---------------------------- | ---------------- | ---------------------------- | ------------------- | -------------- |
| Maximum Sum of K Elements    | Running Sum      | Fixed Size                   | Maximum Sum         | ⭐              |
| Count Even Numbers in Window | Even Count       | Fixed Size                   | Count Evens         | ⭐              |
| Permutation in String        | Frequency Map    | Fixed Size + Frequency Match | Check Existence     | ⭐              |
| Find All Anagrams            | Frequency Map    | Fixed Size + Frequency Match | Collect All Indices | ⭐⭐             |

---

# Variable Window Atlas

| Problem                                        | Maintained State                  | Validity Condition              | Goal            | Representative |
| ---------------------------------------------- | --------------------------------- | ------------------------------- | --------------- | -------------- |
| Minimum Size Subarray Sum                      | Running Sum                       | Running Sum ≥ Target            | Smallest Window | ⭐              |
| Longest Substring Without Repeating Characters | Frequency Map                     | Every Frequency ≤ 1             | Longest Window  | ⭐              |
| Character Replacement                          | Frequency Map + Maximum Frequency | Window Size − Max Frequency ≤ k | Longest Window  | ⭐              |
| Longest Substring with At Most K Distinct      | Frequency Map + Distinct Count    | Distinct Count ≤ k              | Longest Window  | ⭐⭐             |
| Fruits Into Baskets                            | Frequency Map + Distinct Count    | Distinct Count ≤ 2              | Longest Window  | ⭐⭐             |
| Minimum Window Substring                       | Two Frequency Maps + Need/Have    | Have == Need                    | Smallest Window | ⭐              |

---

# Maintained State Evolution

```text
Running Sum
      │
      ▼
Frequency Map
      │
      ▼
Frequency Map
+
Maximum Frequency
      │
      ▼
Frequency Map
+
Distinct Count
      │
      ▼
Two Frequency Maps
+
Need / Have
```

---

# Validity Evolution

```text
Fixed Window

Always Valid
(Because size never changes)

────────────────────────────

Variable Window

Running Sum >= Target

↓

No Duplicate Characters

↓

Window Length - Max Frequency <= k

↓

Distinct Count <= k

↓

Have == Need
```

---

# Pointer Responsibilities

## Fixed Window

### Right Pointer

* Introduces one new element.

### Left Pointer

* Removes one old element.

Both pointers move together because the window size never changes.

---

## Variable Window

### Right Pointer

* Expands the window.
* Collects more information.
* Attempts to satisfy the validity condition.

### Left Pointer

* Shrinks the window.
* Removes unnecessary information.
* Restores or optimizes validity.

The pointers move independently.

---

# Expand–Shrink Framework

Every Variable Window problem follows the same framework.

```text
Expand

↓

Update Maintained State

↓

Window Valid?

      │
 ┌────┴────┐
 │         │
NO        YES
 │         │
 ▼         ▼

Expand   Record Answer

            │
            ▼

         Shrink

            │
            ▼

      Still Valid?

            │
      ┌─────┴─────┐
      │           │
     YES         NO
      │           │
      ▼           ▼

  Shrink Again   Expand
```

---

# Recognition Keywords

## Fixed Window

* Size K
* Every Window
* Fixed Length
* Consecutive K
* Sliding Sum
* Window of Length K

---

## Variable Window

* Longest
* Smallest
* Minimum
* Maximum
* At Least
* At Most
* Contains
* Distinct
* Unique
* Replace
* Valid Window

---

# Common Maintained States

| Maintained State                  | Used In                                 |
| --------------------------------- | --------------------------------------- |
| Running Sum                       | Maximum Sum, Minimum Size Subarray Sum  |
| Running Count                     | Count Even Numbers                      |
| Frequency Map                     | Permutation, Longest Unique             |
| Frequency Map + Maximum Frequency | Character Replacement                   |
| Frequency Map + Distinct Count    | At Most K Distinct, Fruits Into Baskets |
| Two Frequency Maps + Need/Have    | Minimum Window Substring                |

---

# Common Validity Conditions

| Problem               | Validity                        |
| --------------------- | ------------------------------- |
| Maximum Sum of K      | Fixed Size                      |
| Count Even            | Fixed Size                      |
| Permutation           | Frequency Maps Equal            |
| Minimum Size Subarray | Running Sum ≥ Target            |
| Longest Unique        | No Frequency > 1                |
| Character Replacement | Window Size − Max Frequency ≤ k |
| At Most K Distinct    | Distinct Count ≤ k              |
| Fruits Into Baskets   | Distinct Count ≤ 2              |
| Minimum Window        | Have == Need                    |

---

# Complexity Cheat Sheet

| Pattern                        | Time | Space               |
| ------------------------------ | ---- | ------------------- |
| Running Sum                    | O(n) | O(1)                |
| Running Count                  | O(n) | O(1)                |
| Frequency Map                  | O(n) | O(alphabet) or O(n) |
| Frequency Map + Max Frequency  | O(n) | O(alphabet)         |
| Frequency Map + Distinct Count | O(n) | O(alphabet)         |
| Need / Have                    | O(n) | O(alphabet)         |

---

# Pattern Evolution

```text
Hashing

↓

Maintain Information

↓

Two Pointers

↓

Assign Pointer Responsibilities

↓

Sliding Window

↓

Fixed Window

↓

Maintain Window State

↓

Variable Window

↓

Maintain Window Validity

↓

Advanced Variable Window

↓

Need / Have
Multiple Maintained States
```

---

# One-Minute Revision

## Fixed Window

* Window size is known.
* Maintain the current window efficiently.
* Left and right move together.

---

## Variable Window

* Window size is unknown.
* Maintain information that determines validity.
* Expand until valid.
* Shrink while valid.
* Repeat until traversal completes.

---

# Sliding Window Memory Hook

> **Fixed Window asks:**
> *"How do I efficiently process every fixed-size window?"*

> **Variable Window asks:**
> *"How do I discover the optimal window while continuously maintaining validity?"*

---

# Representative Problems Roadmap

```text
Sliding Window

│
├── Fixed Window
│      │
│      ├── Maximum Sum of K
│      ├── Count Even Numbers
│      ├── Permutation in String
│      └── Find All Anagrams
│
└── Variable Window
       │
       ├── Minimum Size Subarray Sum
       ├── Longest Unique Substring
       ├── Character Replacement
       ├── Longest Substring with At Most K Distinct
       ├── Fruits Into Baskets
       └── Minimum Window Substring
```

---

# Final Memory Hook

> **Maintain the right information.**
>
> **Let the validity condition decide which pointer moves.**
>
> **The code changes from problem to problem, but the framework stays the same.**
