# Fixed Window

## Part 2 — Maintained State, Invariants and Pointer Responsibilities

---

# The Biggest Mental Shift

At this point, most people think they understand the Fixed Window pattern.

They usually say:

> "We move a window of size `k`."

While that statement is technically true, it completely misses the real idea.

The window is **not** the algorithm.

The maintained information is.

Imagine solving the same Fixed Window problem five different times.

The window size never changes.

Only the information you care about changes.

For example:

| Problem                   | Window Size | Information Maintained |
| ------------------------- | ----------- | ---------------------- |
| Maximum Sum of K Elements | Fixed       | Running Sum            |
| Count Even Numbers        | Fixed       | Even Count             |
| Average of K Elements     | Fixed       | Running Sum            |
| Permutation in String     | Fixed       | Frequency Map          |
| Find All Anagrams         | Fixed       | Frequency Map          |

Notice something interesting.

The **window movement is identical** in every problem.

Only the maintained information changes.

This is why the Sliding Window algorithm feels almost the same across many problems.

The pointers are following exactly the same movement.

The maintained state is what changes.

---

# What Is the Maintained State?

The maintained state is simply the information that always describes the current window.

Think back to the notebook analogy from Part 1.

Your notebook always contains everything important about the current window.

As the window moves,

you never throw away the notebook.

You only update the information inside it.

The maintained state must always answer the question:

> **"If someone stopped my algorithm right now, what information about the current window would I need?"**

That answer becomes the maintained state.

---

# Choosing the Correct Maintained State

This is one of the most important skills in algorithm design.

Never start by thinking about pointers.

Start by asking:

> **What information does this problem actually need?**

Different problems require different information.

---

## Case 1 — Need a Total

Example

```text id="6f1p5r"
Maximum Sum

Average

Total Cost
```

Information needed

```text id="3bxn4x"
Running Sum
```

---

## Case 2 — Need a Count

Example

```text id="bxfv42"
Even Numbers

Odd Numbers

Vowels

Consonants
```

Information needed

```text id="zct4s6"
Running Count
```

---

## Case 3 — Need Frequency

Example

```text id="vjlwmk"
Permutation

Anagrams

Character Inventory
```

Information needed

```text id="ik8t1e"
Frequency Map
```

---

## Case 4 — Need Presence

Sometimes you only care whether something exists.

Information needed

```text id="8v2nsq"
Set
```

---

The important observation is this:

> **The pattern never tells you what to store.**

The problem tells you.

The Sliding Window technique only tells you **how to maintain** that information efficiently.

---

# Local Updates

The reason Fixed Window works is because the maintained state can be updated locally.

Suppose your current window is

```text id="pj20c7"
2 1 5
```

The next window becomes

```text id="glldo7"
1 5 1
```

The algorithm never asks

> "How do I compute everything again?"

Instead it asks

> **"How do I update the information I already have?"**

Every maintained state should support two operations.

```text id="utvwpx"
Remove Contribution

Add Contribution
```

Everything else stays exactly the same.

---

# The Core Invariant

Every Sliding Window variation has an invariant.

For Fixed Window, the invariant is extremely simple.

> **The maintained state always represents exactly the current window.**

Nothing more.

Nothing less.

If your maintained state ever represents:

* part of the previous window,
* part of the next window,
* or a mixture of both,

the algorithm becomes incorrect.

The maintained state must always stay synchronized with the current window.

---

# Understanding the Invariant Through Examples

Suppose the current window is

```text id="uhd4md"
4 2 8
```

If your maintained state is

```text id="rbc1sa"
Running Sum = 14
```

then it correctly represents the window.

Now the window slides.

```text id="knh6lf"
2 8 5
```

Your maintained state must immediately become

```text id="d8y8za"
Running Sum = 15
```

The maintained state has changed because the window changed.

At every moment,

both must describe exactly the same region.

This synchronization is the invariant.

---

# Pointer Responsibilities

One of the biggest lessons from the Two Pointers chapter was this:

Never ask

> "Which pointer moves?"

Instead ask

> **"What responsibility does each pointer have?"**

The same philosophy applies here.

---

## Left Pointer

The left pointer is responsible for removing information that is no longer valid.

When the window moves,

the leftmost element expires.

Its contribution must be removed from the maintained state.

Think of the left pointer as the **cleanup worker**.

Its only responsibility is to erase expired information.

---

## Right Pointer

The right pointer is responsible for introducing new information.

When the window expands by one position,

a new element becomes part of the current window.

Its contribution must be added.

Think of the right pointer as the **information collector**.

Its only responsibility is to record newly available information.

---

# Why Does the Left Pointer Move?

The left pointer does **not** move because the algorithm says so.

It moves because the information it points to has expired.

Once an element is no longer inside the current window,

its contribution becomes invalid.

Keeping that contribution would violate the invariant.

Therefore,

the left pointer removes it.

---

# Why Doesn't the Left Pointer Move Earlier?

Suppose the window has not moved yet.

The leftmost element is still inside the current window.

Removing it early would produce a maintained state that no longer represents the window.

The invariant would immediately break.

Therefore,

the left pointer waits until the window actually slides.

---

# Why Does the Right Pointer Move?

The right pointer moves because new information becomes available.

Whenever the window shifts,

one new element enters.

Ignoring that element would make the maintained state incomplete.

Therefore,

the right pointer adds its contribution.

---

# Why Doesn't the Right Pointer Skip Elements?

Imagine skipping an entering element.

Now the maintained state would represent

```text id="jz6xv9"
Current Window

minus

one contribution
```

Again,

the invariant breaks.

Every element that belongs to the window must contribute exactly once.

---

# Window Movement Is Only a Consequence

Many people think

```text id="0vpd2u"
Move Window

↓

Update Information
```

The real thinking process is the opposite.

```text id="hgr8kg"
Information Expired

↓

Remove It

↓

New Information Appeared

↓

Add It

↓

Window Has Successfully Moved
```

The movement of the pointers is simply the mechanism used to keep the maintained state synchronized.

The maintained state is the real objective.

---

# General Fixed Window Lifecycle

Every Fixed Window problem follows the same lifecycle.

### Step 1

Build the first complete window.

---

### Step 2

Compute the maintained state for that first window.

---

### Step 3

Slide the window by one position.

---

### Step 4

Remove the contribution of the leaving element.

---

### Step 5

Add the contribution of the entering element.

---

### Step 6

Update the answer using the maintained state.

---

### Step 7

Repeat until every possible window has been processed.

Notice that this lifecycle never changes.

Only the maintained state changes.

---

# The General Algorithm (Reasoning Template)

Whenever you encounter a new Fixed Window problem, think through these questions in order.

1. What information does the problem require?

2. Can that information be represented as a maintained state?

3. How do I compute the first window?

4. What information expires when the window moves?

5. How do I remove that contribution?

6. What new information enters the window?

7. How do I add that contribution?

8. Does my maintained state still describe the current window exactly?

If the answer to the last question is **yes**, then your invariant is preserved, and your algorithm is ready to continue.

---

# Memory Hook for This Part

> **The window does not move because pointers move.**
>
> **The pointers move because the maintained state must remain synchronized with the current window.**
