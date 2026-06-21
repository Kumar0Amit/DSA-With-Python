# Fixed Window

> **"A Fixed Window algorithm is not about moving a window of size `k`. It is about maintaining the state of a fixed-size region while avoiding repeated work."**

---

# Part 1 — Foundations of the Fixed Window Pattern

---

# What Is the Fixed Window Variation?

Sliding Window is not a single algorithm.

It is a family of optimization techniques.

The first and simplest member of this family is the **Fixed Window** variation.

In this variation, the problem itself tells us **exactly how large the window must be**.

Examples include:

* Find the maximum sum of every **3** consecutive elements.
* Count even numbers in every window of size **5**.
* Find a permutation of a string of length **m**.
* Find all anagrams of a pattern of length **m**.

Notice something common among all these problems.

The size of the region we are interested in is already known before the algorithm starts.

We never have to discover the correct window size.

The problem has already done that for us.

Our only responsibility is to process every window **efficiently**.

---

# Why Does This Pattern Exist?

Every optimization begins with frustration.

Imagine you are solving this problem.

> Find the maximum sum of every 3 consecutive elements.

Consider the array:

```text
2 1 5 1 3 2
```

The brute-force solution is straightforward.

Compute:

```text
Window 1

2 + 1 + 5 = 8
```

Then

```text
Window 2

1 + 5 + 1 = 7
```

Then

```text
Window 3

5 + 1 + 3 = 9
```

Then

```text
Window 4

1 + 3 + 2 = 6
```

Nothing appears wrong.

The algorithm is correct.

But correctness alone does not make an algorithm efficient.

The real question is:

> **How much unnecessary work is being repeated?**

---

# Looking Beyond the Numbers

Most beginners look at the sums.

An algorithm designer looks at the windows.

Compare these two windows.

```text
Window 1

2 1 5
```

```text
Window 2

1 5 1
```

Instead of asking

> "What is the new sum?"

ask

> **"What actually changed?"**

Only two things.

```text
2 disappeared.

1 appeared.
```

Everything else remained exactly the same.

That means almost all the work performed for the first window is still useful for the second window.

Yet the brute-force algorithm throws all of it away and starts from scratch.

This is the repeated work we want to eliminate.

---

# The Real Optimization

The optimization is often misunderstood.

People say:

> "Slide the window."

But moving the window is not the optimization.

The optimization is realizing that the new window is **almost identical** to the previous one.

Instead of rebuilding the answer,

we update it.

Think about the previous example.

Suppose we already know

```text
Window

2 1 5

Sum = 8
```

The next window is

```text
1 5 1
```

Should we add everything again?

No.

We already know most of the answer.

The previous sum contains useful information.

Only one value expired.

Only one value became available.

So instead of computing

```text
1 + 5 + 1
```

again,

we simply update the old answer.

```text
Old Sum

↓

Remove expired contribution

↓

Add new contribution

↓

New Sum
```

This idea is the heart of the Fixed Window pattern.

---

# The Window Is Not the Important Part

This is one of the biggest misconceptions about Sliding Window.

Many explanations focus entirely on the window.

They draw boxes around arrays.

They animate two pointers moving.

But the window itself is not what makes the algorithm efficient.

The important part is the **information** associated with the window.

Imagine carrying a notebook while walking through the array.

The notebook contains everything you currently know about the active window.

For example, it might store:

* the current sum,
* the current frequency map,
* the number of even elements,
* the number of vowels,
* the maximum frequency,
* or any other information required by the problem.

When the window moves,

you do not throw away the notebook.

You simply erase information that has expired and write down the new information that has become available.

The notebook stays with you throughout the entire algorithm.

The notebook is what we call the **maintained state**.

The window merely determines **which information should leave** and **which information should enter**.

---

# Mental Model

Forget arrays for a moment.

Imagine a train.

Each compartment represents one element of the current window.

The train always has exactly **k compartments**.

When the train moves forward by one station:

* the last compartment remains,
* the middle compartments remain,
* only the front compartment leaves,
* and one new compartment is attached at the back.

Would you rebuild the entire train?

Of course not.

You only replace the parts that changed.

The Fixed Window algorithm follows exactly the same philosophy.

The algorithm never rebuilds information that is still valid.

It only updates what changed.

---

# The Optimization Journey

Every Fixed Window problem follows the same evolution.

## Stage 1 — Brute Force

Treat every window independently.

Recompute everything.

```text
Window 1

Compute

↓

Window 2

Compute again

↓

Window 3

Compute again
```

Simple.

Correct.

Slow.

---

## Stage 2 — Observation

Notice that consecutive windows overlap heavily.

Only one element leaves.

Only one element enters.

Everything else remains unchanged.

---

## Stage 3 — Ask the Right Question

Instead of asking

> "How do I compute the next answer?"

ask

> **"How can I update the previous answer?"**

This single question changes the entire algorithm.

---

## Stage 4 — Maintain Information

Carry useful information forward.

When the window moves:

* remove expired information,
* add new information,
* preserve everything else.

The maintained information now evolves together with the window.

---

## Stage 5 — Linear-Time Solution

Each movement performs only local updates.

The algorithm no longer rebuilds answers.

Instead, it continuously maintains them.

This reduces the complexity from repeatedly processing the entire window to updating only the changes.

The optimization did not come from moving pointers.

It came from **preserving knowledge**.

---

# The Core Philosophy of Fixed Window

If you remember only one idea from this chapter, remember this:

> **A Fixed Window algorithm does not repeatedly solve many independent problems.**

It solves **one continuously evolving problem**.

Each new window is simply the previous window after one piece of information has expired and one new piece of information has arrived.

Once you begin thinking this way, many interview problems that initially appear different suddenly become instances of the same underlying pattern.

The algorithm changes very little.

Only the maintained state changes.

That idea will become the foundation for every Fixed Window problem you solve in the future.