"""
===============================================================================
Problem: Move Zeroes
LeetCode: 283
Pattern: Two Pointers -> Reader / Writer
Difficulty: Easy
===============================================================================

PROBLEM DESCRIPTION
-------------------

You are given an integer array.

Move all the zeroes to the end of the array while preserving the
relative order of all non-zero elements.

IMPORTANT

1. Do it IN-PLACE.
2. Do NOT create another array.
3. Relative order of non-zero elements must remain unchanged.

Example

Input

[0,1,0,3,12]

Output

[1,3,12,0,0]

Notice

We are NOT sorting.

We are NOT removing zeroes.

We are only moving them.

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

What should the final array look like?

Answer

Non-zero elements first.

Zeroes at the end.

Like this

----------------------------

Non-Zero Portion | Zero Portion

----------------------------

Question 2

Can we build the non-zero portion while scanning the array?

Yes.

Question 3

Who discovers non-zero values?

Reader.

Question 4

Who remembers where the next non-zero should go?

Writer.

Question 5

What if Reader finds a zero?

Nothing belongs in the finished portion.

Only Reader moves.

Question 6

What if Reader finds a non-zero?

It belongs inside the finished portion.

Swap it with Writer.

Move both pointers.

===============================================================================
INVARIANT
===============================================================================

Everything from

0

to

Writer - 1

contains ONLY non-zero values in their ORIGINAL ORDER.

This must remain true throughout the algorithm.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Reader

- Scan every element.
- Find non-zero values.

Writer

- Point to the next position where a non-zero belongs.

Reader discovers.

Writer commits.

===============================================================================
"""


def move_zeroes(nums):

    writer = 0
    reader = 0

    while reader < len(nums):

        if nums[reader] != 0:

            if writer != reader:
                nums[writer], nums[reader] = nums[reader], nums[writer]

            writer = writer + 1

        reader = reader + 1


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    nums = [0, 1, 0, 3, 12]

    move_zeroes(nums)

    print(nums)


"""
===============================================================================
DRY RUN
===============================================================================

Initial

[0,1,0,3,12]

W = 0

R = 0

----------------------------------

Reader sees

0

Does it belong in finished portion?

No

Reader++

----------------------------------

W = 0

R = 1

Reader sees

1

Belongs in finished portion.

Swap

Array

[1,0,0,3,12]

Writer++

Reader++

----------------------------------

W = 1

R = 2

Reader sees

0

Skip

Reader++

----------------------------------

W = 1

R = 3

Reader sees

3

Swap

Array

[1,3,0,0,12]

Writer++

Reader++

----------------------------------

W = 2

R = 4

Reader sees

12

Swap

Array

[1,3,12,0,0]

Writer++

Reader++

----------------------------------

Reader finishes.

Invariant never broke.

Finished portion

[1,3,12]

===============================================================================
WHY DOES THIS WORK?
===============================================================================

Every non-zero element is moved exactly once.

Every zero naturally gets pushed towards the end.

Relative order of non-zero elements never changes.

Reader scans.

Writer builds.

===============================================================================
TIME COMPLEXITY
===============================================================================

O(n)

===============================================================================
SPACE COMPLEXITY
===============================================================================

O(1)

===============================================================================
COMMON MISTAKES
===============================================================================

1.

Moving Writer when Reader finds zero.

Invariant breaks.

----------------------------------------------------

2.

Using overwrite instead of swap.

Zeroes disappear.

You then need another pass to recreate them.

----------------------------------------------------

3.

Always swapping.

It works.

But

if writer == reader

the swap is unnecessary.

Avoid it.

----------------------------------------------------

4.

Thinking Writer points to the last non-zero.

Wrong.

Here

Writer points to the NEXT POSITION

where a non-zero should be placed.

This is different from Remove Duplicates.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why is swapping required instead of rewriting?

------------------------------------------

2.

Why doesn't Writer move on zero?

------------------------------------------

3.

What invariant is maintained?

------------------------------------------

4.

Why is the relative order preserved?

------------------------------------------

5.

Why is

if writer != reader

only an optimization?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Apply Operations to an Array
(LeetCode 2460)

2.

Replace Elements with Greatest Element on Right Side
(LeetCode 1299)

Medium

3.

Sort Colors
(LeetCode 75)

4.

Partition Array According to Given Pivot
(LeetCode 2161)

Hard

5.

Candy Crush
(LeetCode 723)

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

Reader finds.

Writer packs.

Zeroes naturally drift to the end.

===============================================================================

"""