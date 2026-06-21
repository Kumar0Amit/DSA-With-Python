# Variable Window

## Part 2 — Maintained State, Window Validity, Pointer Responsibilities, and the Expand–Shrink Cycle

---

# The Biggest Difference from Fixed Window

In the Fixed Window variation, every window automatically satisfied one requirement.

Its size.

If the problem said

```text
Window Size = 5
```

then every window you processed already met that condition.

There was nothing to verify.

The algorithm only needed to maintain information efficiently.

---

Variable Window is fundamentally different.

Now, every window belongs to one of two categories.

```text
Valid

or

Invalid
```

The entire algorithm revolves around moving between these two states.

---

# Maintained State Has a New Purpose

Fixed Window asked

> "What information should I carry forward?"

Variable Window asks two questions.

> "What information should I carry forward?"

and

> "Can that information tell me whether my current window is valid?"

The maintained state is no longer just for computing an answer.

It also becomes the tool used to decide

whether to expand

or

whether to shrink.

---

# Examples of Maintained State

Different problems require different information.

| Problem                   | Maintained State                   |
| ------------------------- | ---------------------------------- |
| Minimum Size Subarray Sum | Running Sum                        |
| Longest Unique Substring  | Frequency Map                      |
| Character Replacement     | Frequency Map + Maximum Frequency  |
| At Most Two Distinct      | Frequency Map + Distinct Count     |
| Minimum Window Substring  | Frequency Map + Need/Have Counters |

Notice something.

These maintained states look familiar.

Many of them already appeared in Fixed Window.

The maintained state itself is not new.

What is new

is

how we use it.

---

# Window Validity

Every Variable Window problem has a condition that separates

valid windows

from

invalid windows.

Examples

```text
Running Sum >= Target
```

```text
No Character Repeats
```

```text
Distinct Count <= 2
```

```text
Window Length - Maximum Frequency <= k
```

The algorithm continuously asks one question.

> **"Is my current window valid?"**

Everything else follows from this answer.

---

# The Core Invariant

Every Sliding Window family has an invariant.

For Variable Window,

the invariant is more subtle than in Fixed Window.

Instead of simply representing the current window,

the maintained state must also correctly determine whether the window is valid.

Think of it this way.

At every moment,

the maintained state must describe

exactly

the current window.

Only then can we correctly answer

> "Is this window valid?"

If the maintained state becomes incorrect,

our validity check also becomes incorrect,

and every future decision becomes unreliable.

---

# Two Phases of Every Variable Window Algorithm

Every Variable Window algorithm alternates between two phases.

## Phase 1 — Expansion

The window is currently invalid.

Our only goal is to make it valid.

The right pointer moves.

New information enters.

The maintained state grows.

Eventually,

the validity condition becomes true.

Only then does the algorithm enter the next phase.

---

## Phase 2 — Contraction

The window is already valid.

Now the objective changes completely.

The algorithm asks

> "Can I still satisfy the condition with a smaller window?"

The left pointer begins removing information.

After every removal,

the validity condition is checked again.

Eventually,

one more removal breaks the condition.

The window becomes invalid again.

Now shrinking must stop.

The algorithm returns to expansion.

---

# Why Does the Right Pointer Move?

This question has a very different answer from Fixed Window.

The right pointer does **not** move because the window has a fixed size.

It moves because

the current window is not yet sufficient.

It is trying to collect enough information

to satisfy the problem's condition.

Examples

```text
Running Sum

is still too small.
```

```text
A required character

has not appeared yet.
```

```text
The current substring

is still unique,

so we can safely make it larger.
```

The right pointer is always searching for enough information.

---

# Why Doesn't the Left Pointer Move Immediately?

Imagine the window is still invalid.

Suppose

Running Sum

is only

8

while the target is

15.

Would removing elements help?

No.

Removing information can never transform

an invalid window

into

a valid one

for this kind of problem.

Instead,

it moves you even farther away.

Therefore,

the left pointer waits.

It has nothing useful to do until the window first becomes valid.

---

# Why Does the Left Pointer Move?

Once the window becomes valid,

the objective changes.

We no longer want

just any valid window.

We usually want

* the smallest valid window,

or

* the longest valid window that still satisfies a rule.

This is where the left pointer becomes active.

Its responsibility is

to remove information

while trying to preserve validity.

Every movement asks

> "Can I throw away this information and still remain valid?"

If yes,

the window was larger than necessary.

If no,

the removed information was essential.

---

# Pointer Responsibilities

Notice how the responsibilities have evolved from Fixed Window.

## Right Pointer

Responsible for

gathering information.

It expands the search space.

It attempts to satisfy the validity condition.

---

## Left Pointer

Responsible for

discarding unnecessary information.

It minimizes or restores validity,

depending on the problem.

---

The important observation is this.

The pointers no longer move together.

Each pointer moves independently,

depending entirely on the validity condition.

---

# The Expand–Shrink Cycle

Every Variable Window algorithm follows the same rhythm.

```text
Window Invalid

↓

Expand

↓

Update Maintained State

↓

Check Validity

↓

Still Invalid?

↓

Expand Again

↓

Becomes Valid

↓

Record Candidate Answer

↓

Shrink

↓

Update Maintained State

↓

Still Valid?

↓

Shrink Again

↓

Becomes Invalid

↓

Expand Again
```

This cycle repeats until the right pointer reaches the end of the input.

Notice something.

There is no mention of

* arrays,
* strings,
* sums,
* frequencies,
* or Python.

The cycle is completely independent of the problem.

Only the maintained state

and

the validity condition

change.

---

# The General Thinking Template

Whenever you see a Variable Window problem,

train yourself to ask these questions.

1.

What information do I need to maintain?

---

2.

How do I know whether my current window is valid?

---

3.

If the window is invalid,

what information is missing?

---

4.

Should I expand or shrink?

---

5.

If the window is valid,

can I make it even better by shrinking?

---

6.

What movement would destroy the validity condition?

---

If you can answer these questions,

the algorithm almost writes itself.

---

# Memory Hook for Part 2

> **The right pointer searches for validity.**
>
> **The left pointer searches for optimality.**
>
> **Together, they maintain the smallest or largest valid window required by the problem.**
