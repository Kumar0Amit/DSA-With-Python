# Reader / Writer Pattern

# 1. What is the Reader / Writer Pattern?

Reader / Writer is an in-place Two Pointer technique used when we want to **build a correct portion of an array while scanning it only once**.

Instead of repeatedly shifting elements or creating another array, we assign two different responsibilities to two pointers.

* **Reader** explores the array.
* **Writer** builds the final answer.

The writer never explores.

The reader never decides where the next element should permanently stay.

Because their jobs are separated, the algorithm becomes simple and runs in **O(n)** time with **O(1)** extra space.

---

# 2. When Should This Pattern Come To Mind?

If a problem contains phrases like:

* remove duplicates
* remove element
* move all X to one side
* compress array
* filter elements
* in-place modification
* preserve relative order
* stable partition
* rewrite the array

Immediately ask yourself:

> "Can I scan the array once while building the finished portion?"

If the answer is yes, Reader / Writer is a strong candidate.

---

# 3. Mental Model

Imagine you are packing books into a shelf.

You have two people.

### Reader

Walks through every book.

For every book, Reader asks:

> "Does this belong in the final shelf?"

Reader never arranges books.

Reader only discovers them.

---

### Writer

Writer stands at the next empty position in the shelf.

Whenever Reader finds a valid book,

Writer places it into the next available position.

Writer never searches.

Writer only commits.

Think of it as:

```
Reader discovers.

Writer commits.
```

---

# 4. Thought Process

Suppose the problem asks:

> Remove duplicates from a sorted array.

Don't think about code.

Ask yourself:

### Question 1

What should the finished array look like?

Answer:

```
Only unique elements.
```

---

### Question 2

Can I build this finished array from left to right?

Yes.

---

### Question 3

Can one pointer scan while another pointer remembers where the next valid element belongs?

Yes.

Now the pattern naturally appears.

---

# 5. Brute Force

A beginner might think:

* create another array
* check each element
* append only valid elements
* copy back into original array

Works.

But:

Extra Space = O(n)

The problem usually asks:

> Do it in-place.

So we need another approach.

---

# 6. Optimization Journey

Brute Force

↓

Extra array

↓

Observation

The original array itself has enough space.

↓

Question

Can I overwrite unnecessary values?

↓

Yes.

↓

Need one pointer to scan.

↓

Need one pointer to write.

↓

Reader / Writer Pattern.

---

# 7. Repeated Work Being Eliminated

Without Reader / Writer:

* shifting elements repeatedly
* creating temporary arrays
* copying values multiple times

Reader / Writer eliminates all of that.

Every element is examined once.

Every valid element is written once.

---

# 8. Core Invariant

This is the heart of the pattern.

At every moment during the algorithm:

```
Everything from index

0

to

writer

is already correct.
```

Nothing before Writer will ever need to be revisited.

This is the invariant.

Every pointer movement must preserve this property.

---

# 9. Pointer Responsibilities

## Reader

Responsibilities

* Scan the entire array.
* Inspect every element exactly once.
* Decide whether the current element belongs in the final answer.

Reader never modifies completed work.

---

## Writer

Responsibilities

* Point to the last completed position (or next insertion position depending on implementation).
* Extend the finished portion.
* Never scan ahead.

Writer only moves when Reader discovers a valid element.

---

# 10. Why Doesn't Writer Move Every Time?

Suppose Reader encounters an invalid element.

Example:

Move Zeroes

```
0
```

Does this belong in the finished non-zero portion?

No.

Then Writer should not move.

Otherwise the invariant breaks.

The finished portion would contain invalid elements.

---

# 11. Why Doesn't Reader Stop Early?

Reader's only job is:

```
Inspect everything.
```

Even if the finished portion already looks correct,

Reader cannot stop,

because a future element may still belong inside it.

Reader must scan the entire array.

---

# 12. Representative Problem

## Remove Duplicates From Sorted Array

Problem

```
[1,1,1,2,2,3]
```

Need

```
[1,2,3]
```

without extra space.

---

### Thinking Process

Question

Do we already know where unique elements should go?

Yes.

At the beginning of the array.

---

Question

Who finds unique elements?

Reader.

---

Question

Who stores them?

Writer.

---

Question

What invariant should always remain true?

```
Everything before Writer is unique.
```

---

### Discovery

When Reader finds

```
same value
```

Nothing changes.

Only Reader moves.

---

When Reader finds

```
new value
```

Writer extends the finished portion.

Invariant preserved.

---

Final complexity

```
Time

O(n)

Space

O(1)
```

---

# 12. Representative Problem — Remove Duplicates From Sorted Array

## Problem Statement

You are given a **sorted** array.

Your task is to remove duplicates **in-place** such that every unique element appears exactly once.

You cannot create another array.

You must return the number of unique elements.

Example

```text
Input

[1,1,2,2,3,4,4,5]

Output

Length = 5

Array

[1,2,3,4,5,...]
```

---

# Step 1 — Understand The Final Goal

Before writing any algorithm, imagine the desired array.

Current array

```text
1 1 2 2 3 4 4 5
```

Desired array

```text
1 2 3 4 5
```

Notice something.

The unique elements are already in the correct relative order.

We don't need to sort anything.

We only need to **compress** them.

---

# Step 2 — Brute Force Thinking

A beginner might think:

* Create another list.
* Traverse the array.
* If the current value hasn't been added yet, append it.
* Copy the new list back.

This works.

But it uses

```text
O(n)
```

extra space.

The problem specifically asks for an **in-place** solution.

So we need another idea.

---

# Step 3 — Observe The Array

The array is sorted.

```text
1 1 2 2 3 4 4 5
```

What advantage does sorting give us?

It groups duplicates together.

Instead of searching the whole array for duplicates,

Reader only needs to compare with the **last unique value**.

That observation removes a huge amount of unnecessary work.

---

# Step 4 — Invent The Two Pointers

We now give two different responsibilities.

## Reader

Job:

Scan every element.

Ask:

> "Is this a new unique value?"

Reader never decides where to store it.

---

## Writer

Job:

Remember where the latest unique value has been stored.

Writer never scans.

Writer only extends the finished portion.

---

# Step 5 — Define The Invariant

This is the most important sentence.

At every moment,

```text
Everything from index 0 to Writer
contains only unique elements.
```

Every movement must preserve this.

---

# Step 6 — Dry Run

Array

```text
1 1 2 2 3 4 4 5
```

Initial state

```text
W
R

1 1 2 2 3 4 4 5
```

Writer = 0

Reader = 1

Finished portion

```text
[1]
```

Invariant holds.

---

### Reader sees another 1

```text
W
  R

1 1 2 2 3 4 4 5
```

Question:

Is this a new unique value?

No.

Action:

Move Reader only.

Writer waits.

Finished portion remains

```text
[1]
```

Invariant preserved.

---

### Reader reaches 2

```text
W
    R

1 1 2 2 3 4 4 5
```

Question:

Is this a new value?

Yes.

Where should it go?

Immediately after the finished portion.

So write

```text
nums[writer + 1] = nums[reader]
```

Array becomes

```text
1 2 2 2 3 4 4 5
```

Move both pointers.

```text
  W
      R

1 2 2 2 3 4 4 5
```

Finished portion

```text
[1 2]
```

Invariant preserved.

---

### Reader sees another 2

Duplicate.

Move Reader only.

```text
  W
        R

1 2 2 2 3 4 4 5
```

---

### Reader reaches 3

Unique.

Write it after Writer.

```text
1 2 3 2 3 4 4 5
```

Move both.

Finished portion

```text
1 2 3
```

---

### Reader reaches 4

Unique.

Write.

Move both.

Finished portion

```text
1 2 3 4
```

---

### Reader reaches another 4

Duplicate.

Reader only.

---

### Reader reaches 5

Unique.

Write.

Move both.

Finished portion

```text
1 2 3 4 5
```

Reader finishes.

---

# Step 7 — Why This Works

Notice what happened.

Every unique element was written **exactly once**.

Every duplicate was ignored **exactly once**.

No element was shifted repeatedly.

No extra array was created.

Reader scanned the array once.

Writer extended the finished portion only when it was safe.

The invariant never broke.

---

# Step 8 — Generalize The Pattern

Now forget this problem.

Remember the idea instead.

Whenever a problem says:

* remove
* compress
* filter
* keep only
* preserve order
* in-place

Ask yourself:

> "Can one pointer discover valid elements while another pointer builds the finished answer?"

If yes,

you've probably found a Reader / Writer problem.


# 13. Pattern Recognition Tricks

Whenever you read:

* remove
* compress
* keep only
* stable
* preserve order
* in-place
* move all X

Immediately ask:

```
Can I build the final answer from left to right?
```

If yes,

think Reader / Writer.

---

# 14. Common Mistakes

### Mistake 1

Moving Writer even when Reader finds an invalid element.

Result

Invariant breaks.

---

### Mistake 2

Treating Reader as the Writer.

Reader should never decide final positions.

Reader only explores.

---

### Mistake 3

Forgetting what Writer represents.

Always define it first.

Examples

Remove Duplicates

```
Writer points to last unique element.
```

Move Zeroes

```
Writer points to next position where a non-zero belongs.
```

Different problem.

Different invariant.

---

### Mistake 4

Thinking the Writer always writes.

Sometimes Writer simply waits.

Waiting is part of its responsibility.

---

# 15. Edge Cases

Single element

```
[5]
```

Already finished.

---

All valid

```
[1,2,3]
```

Writer moves together with Reader.

---

All invalid

```
[0,0,0]
```

Writer may never move.

Still correct.

---

Empty array

Always check whether special handling is needed.

---

# 16. Complexity Proof

Reader moves only forward.

Writer moves only forward.

Neither pointer ever moves backward.

Neither pointer revisits an index.

Therefore

```
Reader

O(n)

Writer

At most O(n)
```

Total

```
O(n)
```

Extra memory

```
O(1)
```

---

# 17. How To Recognize This Pattern

Ask these questions.

```
Need in-place?

↓

Yes

Need preserve order?

↓

Yes

Need remove/filter/compress?

↓

Yes

Need build a finished portion?

↓

Yes

Think

Reader / Writer
```

---

# 18. Relation With Other Two Pointer Variations

Reader / Writer

Goal

Build a finished portion.

---

Symmetric Converging

Goal

Compare or swap opposite ends.

---

Elimination

Goal

Discard impossible search space.

---

Composition

Goal

Reduce a harder problem into a simpler one.

---

Finalization

Goal

Process only the side whose answer is already determined.

---

# 19. Quick Revision

Purpose

Build a finished portion.

Reader

Scans.

Writer

Commits.

Invariant

Everything before Writer is already correct.

Recognition

* Remove
* Compress
* Stable
* Preserve order
* In-place

Optimization

Avoid repeated shifting and extra arrays.

Time

```
O(n)
```

Space

```
O(1)
```

Memory Hook

> **Reader discovers. Writer commits.**
