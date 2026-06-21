# Variable Window

> **"Fixed Window maintains the state of a known-size window. Variable Window maintains the validity of an unknown-size window."**

---

# Part 1 — Foundations of the Variable Window Pattern

---

# What Is the Variable Window Variation?

Not every problem tells us the correct window size.

Sometimes the problem only tells us a **condition**.

Examples:

* Find the **smallest** subarray whose sum is at least `k`.
* Find the **longest** substring without repeating characters.
* Find the **longest** substring that can be made of one character after at most `k` replacements.
* Find the **smallest** window containing all required characters.

Notice something different from Fixed Window.

The problem never says:

> "Use a window of size 5."

Instead, it says things like:

* At least
* At most
* No duplicates
* Contains all characters
* Valid
* Invalid

The algorithm must discover the correct window size while scanning the input.

That is why this variation is called **Variable Window**.

---

# Why Does This Variation Exist?

Suppose someone asks:

> Find the smallest subarray whose sum is at least 15.

Can you choose the window size before starting?

No.

Maybe the answer has length 3.

Maybe it has length 7.

Maybe it has length 20.

You simply do not know.

Unlike Fixed Window, where the problem determines the size, here the algorithm must **discover** it.

---

# Why Fixed Window Is Not Enough

Imagine trying to solve

> Smallest subarray with sum ≥ 15

using Fixed Window.

You choose a window size of 3.

You process every window of size 3.

What if no window satisfies the condition?

Should you conclude that no answer exists?

No.

There might be a valid window of size 4.

Or 5.

Or 10.

Now suppose you restart with size 4.

Then size 5.

Then size 6.

Eventually you realize you are solving the same problem repeatedly.

Fixed Window breaks down because **the correct size is unknown**.

---

# The Real Question Changes

In Fixed Window, the main question was:

> **"How do I maintain the state of every window?"**

In Variable Window, the question becomes:

> **"How large should the current window be?"**

That single change completely changes the algorithm.

---

# A New Optimization Journey

Let's revisit the problem:

> Smallest subarray with sum ≥ 15

A brute-force solution might examine every possible subarray.

That works.

But it repeatedly computes information for overlapping regions.

Just like Fixed Window, there is repeated work.

However, there is now an additional challenge.

You do not even know how large the answer is.

So the optimization journey becomes:

```text
Brute Force

↓

Repeated Work

↓

Unknown Window Size

↓

Maintain a Growing Window

↓

Check Validity

↓

Shrink When Possible

↓

Discover the Optimal Window
```

Notice that "window size" is no longer an input.

It becomes part of the search.

---

# The Biggest Mental Shift

This is the most important idea in the entire Variable Window chapter.

In Fixed Window, the window moved because its size was fixed.

In Variable Window, the window moves because its **validity changes**.

The algorithm is no longer thinking about size.

It is thinking about **whether the current window satisfies the required condition**.

---

# Introducing Window Validity

This is a completely new concept.

Every Variable Window problem has a rule that determines whether the current window is acceptable.

Examples:

| Problem                                        | Valid Window                      |
| ---------------------------------------------- | --------------------------------- |
| Minimum Size Subarray Sum                      | Sum ≥ Target                      |
| Longest Substring Without Repeating Characters | No duplicate characters           |
| Character Replacement                          | Replacements Needed ≤ k           |
| At Most Two Distinct Characters                | Distinct Count ≤ 2                |
| Minimum Window Substring                       | Contains every required character |

These conditions are called the **window validity condition**.

Unlike Fixed Window, where every window automatically had the correct size, here **some windows are valid and others are not**.

The algorithm constantly moves between these two states.

---

# Mental Model

Imagine filling a bucket with water.

Your goal is to collect **at least** 10 liters.

You start with an empty bucket.

You keep pouring water.

```text
2 L

↓

5 L

↓

8 L

↓

11 L
```

Now you finally have enough.

Should you stop?

No.

The problem asks for the **smallest** bucket that still contains at least 10 liters.

So you begin removing water from the front.

```text
11 L

↓

10 L

↓

9 L
```

The moment the bucket drops below 10 liters,

it is no longer valid.

Now you must start filling it again.

This cycle repeats until the entire array has been processed.

That is exactly how Variable Window works.

---

# Expand First, Shrink Later

Every Variable Window algorithm follows the same rhythm.

First,

expand the window.

Keep collecting information.

Eventually,

the window becomes valid.

Only then

does shrinking become meaningful.

Why?

Because shrinking an invalid window cannot magically make it satisfy the condition.

It only moves you farther away.

Therefore,

the algorithm always follows this cycle:

```text
Expand

↓

Become Valid

↓

Shrink

↓

Become Invalid

↓

Expand Again
```

This rhythm is the heartbeat of every Variable Window problem.

---

# Core Philosophy

Fixed Window taught us:

> Preserve useful information.

Variable Window adds another layer:

> Preserve a **valid** window whenever possible.

The maintained state is still important.

But now it serves a new purpose.

It helps us determine whether the current window is valid.

Everything else in this chapter will build on that single idea.

---

# Memory Hook for Part 1

> **Fixed Window asks:** "How do I process every window efficiently?"
>
> **Variable Window asks:** "How do I discover the correct window while keeping it valid?"
