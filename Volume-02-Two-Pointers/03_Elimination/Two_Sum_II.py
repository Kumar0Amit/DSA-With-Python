"""
===============================================================================
Problem: Two Sum II - Input Array Is Sorted
LeetCode: 167
Pattern: Two Pointers -> Elimination
Difficulty: Medium
===============================================================================

PROBLEM DESCRIPTION
-------------------

You are given a 1-indexed integer array 'numbers'.

The array is already sorted in non-decreasing order.

Find two numbers such that

numbers[i] + numbers[j] == target

Return their 1-based indices.

Exactly one solution exists.

You cannot use the same element twice.

------------------------------------------------------------

Example

Input

numbers = [2,7,11,15]
target = 9

Output

[1,2]

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

Can brute force solve it?

Yes.

Try every pair.

Time

O(n²)

------------------------------------------------------------

Question 2

What special property does this problem have?

The array is SORTED.

This immediately gives predictability.

------------------------------------------------------------

Question 3

Suppose

Current Sum

is smaller than target.

Can moving Right help?

No.

Moving Right to the left only decreases the sum.

Those pairs become impossible forever.

Only moving Left has the possibility of increasing the sum.

------------------------------------------------------------

Question 4

Suppose

Current Sum

is larger than target.

Can moving Left help?

No.

Moving Left to the right only increases the sum.

Those pairs become impossible forever.

Only moving Right has the possibility of decreasing the sum.

------------------------------------------------------------

Every pointer movement removes
an entire group of impossible pairs.

===============================================================================
INVARIANT
===============================================================================

Everything OUTSIDE the pointers
has already been mathematically proven
to never produce the target.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Left Pointer

- Represents the smallest remaining value.
- Move only when increasing the sum is required.

------------------------------------------------------------

Right Pointer

- Represents the largest remaining value.
- Move only when decreasing the sum is required.

Neither pointer moves randomly.

Every move has proof.

===============================================================================
"""


def two_sum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:

        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left = left + 1

        else:
            right = right - 1

    return []


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    numbers = [2, 7, 11, 15]
    target = 9

    print(two_sum(numbers, target))


"""
===============================================================================
DRY RUN
===============================================================================

numbers

[2,7,11,15]

target

9

------------------------------------------------------------

Left = 0

Right = 3

Current Sum

2 + 15 = 17

17 > 9

Can moving Left help?

No.

It only increases the sum.

Move Right.

------------------------------------------------------------

Left = 0

Right = 2

Current Sum

2 + 11 = 13

13 > 9

Still too large.

Move Right.

------------------------------------------------------------

Left = 0

Right = 1

Current Sum

2 + 7 = 9

Target found.

Return

[1,2]

===============================================================================
WHY DOES THIS WORK?
===============================================================================

When

Current Sum < Target

Every pair using the current Left
with a smaller Right

will produce an even smaller sum.

Impossible.

Eliminate them.

------------------------------------------------------------

When

Current Sum > Target

Every pair using the current Right
with a larger Left

will produce an even larger sum.

Impossible.

Eliminate them.

Every movement permanently shrinks
the search space.

===============================================================================
PATTERN EVOLUTION
===============================================================================

Brute Force

↓

Check every pair

↓

Notice array is sorted

↓

Sorted gives predictability

↓

Predictability gives elimination

↓

O(n)

===============================================================================
TIME COMPLEXITY
===============================================================================

Each pointer moves at most n times.

Time

O(n)

===============================================================================
SPACE COMPLEXITY
===============================================================================

Only two pointers.

O(1)

===============================================================================
COMMON MISTAKES
===============================================================================

1.

Moving Left when

Current Sum > Target

Wrong.

Sum becomes even larger.

------------------------------------------------------------

2.

Moving Right when

Current Sum < Target

Wrong.

Sum becomes even smaller.

------------------------------------------------------------

3.

Ignoring that the array is sorted.

Without sorting,

this elimination proof disappears.

------------------------------------------------------------

4.

Thinking pointers move because of intuition.

No.

They move because of proof.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why does sorting make this algorithm possible?

------------------------------------------------------------

2.

Why can't moving Right help when
the sum is too small?

------------------------------------------------------------

3.

What invariant is maintained?

------------------------------------------------------------

4.

What exactly gets eliminated after
every pointer movement?

------------------------------------------------------------

5.

How would the solution change
if the array were unsorted?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Squares of a Sorted Array
(LeetCode 977)

2.

Count Binary Substrings
(LeetCode 696)

------------------------------------------------------------

Medium

3.

3Sum
(LeetCode 15)

4.

3Sum Closest
(LeetCode 16)

------------------------------------------------------------

Hard

5.

4Sum
(LeetCode 18)

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

If the move cannot improve the answer,

eliminate it forever.

===============================================================================

"""