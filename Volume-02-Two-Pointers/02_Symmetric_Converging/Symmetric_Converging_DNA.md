# Symmetric Converging — Pattern DNA

## Pattern Name

**Symmetric Converging**

---

## Goal

Process two symmetric positions of a sequence by moving from opposite ends toward the center.

---

## Core Idea

Instead of comparing every possible pair, compare only the elements that are mirror images of each other.

Process one symmetric pair.

Move inward.

Repeat.

---

## Core Invariant

Everything **outside** the two pointers has already been correctly processed.

Depending on the problem, "processed" may mean:

* already swapped
* already compared
* already verified

The invariant must remain true after every pointer movement.

---

## Pointer Responsibilities

### Left Pointer

* Starts from the left end.
* Processes the next unprocessed element on the left.

### Right Pointer

* Starts from the right end.
* Processes the next unprocessed element on the right.

Both pointers work as a team.

Neither pointer has a "writer" role.

---

## Pointer Movement

### Normal Case

After processing one pair:

```text
left  += 1
right -= 1
```

Both move toward the center.

---

### Special Case

Some problems require temporarily moving only one pointer.

Example:

* Skip spaces
* Skip punctuation
* Skip invalid characters

Once a valid pair is found, both pointers continue converging.

---

## Recognition Keywords

If the problem contains words like:

* reverse
* palindrome
* mirror
* symmetry
* opposite ends
* compare both sides

Think:

> **Symmetric Converging**

---

## Representative Problems

### Easy

* Reverse String

### Easy / Medium

* Valid Palindrome

---

## Common Mistakes

❌ Moving only one pointer after processing a valid pair.

---

❌ Forgetting to skip invalid characters before comparison.

---

❌ Using `while left <= right` when the middle element should not be processed twice.

---

❌ Thinking the pointers have different jobs.

In this variation, both pointers perform the same type of work.

---

## Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

## Memory Hook

> **Meet in the middle. One symmetric pair at a time.**
