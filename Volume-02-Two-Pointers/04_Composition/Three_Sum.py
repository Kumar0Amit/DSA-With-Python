"""
===============================================================================
Problem: 3Sum
LeetCode: 15
Pattern: Two Pointers -> Composition
Difficulty: Medium
===============================================================================

PROBLEM DESCRIPTION
-------------------

Given an integer array nums,

return ALL UNIQUE triplets

[a,b,c]

such that

a + b + c = 0

Notice

1. Triplets must be unique.
2. Order inside a triplet doesn't matter.
3. Order of triplets doesn't matter.

------------------------------------------------------------

Example

Input

[-1,0,1,2,-1,-4]

Output

[
 [-1,-1,2],
 [-1,0,1]
]

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

Can brute force solve it?

Yes.

Three nested loops.

Choose

i

j

k

Check every triplet.

Time

O(n³)

------------------------------------------------------------

Question 2

Do we already know how to solve
a smaller version of this problem?

Yes.

We already know

Two Sum II.

------------------------------------------------------------

Question 3

Can we somehow convert

3Sum

into

2Sum?

Yes.

Fix one number.

Suppose

a

is fixed.

Then

a + b + c = 0

becomes

b + c = -a

Now we only need to solve

Two Sum.

------------------------------------------------------------

Question 4

Why must we sort?

Sorting gives us

1.

Monotonicity

↓

Two Pointer Elimination

2.

Duplicate Detection

↓

Unique Triplets

------------------------------------------------------------

Question 5

Why skip duplicate fixed values?

Suppose

[-2,-2,0,2]

Fix first

-2

Need

2

Two Sum gives

(0,2)

Now fix second

-2

Need

2

Two Sum again gives

(0,2)

Same triplet.

Repeated work.

Skip duplicates.

===============================================================================
INVARIANT
===============================================================================

Every unique fixed value

is processed exactly once.

Every unique triplet

is generated exactly once.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Fixed Pointer

- Chooses one value.
- Reduces 3Sum into 2Sum.
- Skips duplicate fixed values.

------------------------------------------------------------

Left Pointer

- Finds smaller remaining value.
- Uses Elimination.

------------------------------------------------------------

Right Pointer

- Finds larger remaining value.
- Uses Elimination.

===============================================================================
"""


def three_sum(nums):

    nums.sort()

    answer = []

    n = len(nums)

    for fixed in range(n - 2):

        if fixed > 0 and nums[fixed] == nums[fixed - 1]:
            continue

        left = fixed + 1
        right = n - 1

        target = -nums[fixed]

        while left < right:

            current_sum = nums[left] + nums[right]

            if current_sum < target:

                left += 1

            elif current_sum > target:

                right -= 1

            else:

                answer.append(
                    [nums[fixed], nums[left], nums[right]]
                )

                left += 1
                right -= 1

                while (
                    left < right
                    and nums[left] == nums[left - 1]
                ):
                    left += 1

                while (
                    left < right
                    and nums[right] == nums[right + 1]
                ):
                    right -= 1

    return answer


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    nums = [-1, 0, 1, 2, -1, -4]

    print(three_sum(nums))


"""
===============================================================================
DRY RUN
===============================================================================

Initial

[-1,0,1,2,-1,-4]

------------------------------------------------------------

Sort

[-4,-1,-1,0,1,2]

------------------------------------------------------------

Fixed = -4

Need

4

Run Two Sum

No answer.

------------------------------------------------------------

Fixed = -1

Need

1

Left = -1

Right = 2

Sum

1

Target found

Triplet

[-1,-1,2]

Store it.

Move both pointers.

Skip duplicates.

------------------------------------------------------------

Continue.

Left = 0

Right = 1

Need

1

Found

[-1,0,1]

Store.

------------------------------------------------------------

Next Fixed

Second

-1

Duplicate.

Skip.

------------------------------------------------------------

Algorithm finishes.

Return

[
 [-1,-1,2],
 [-1,0,1]
]

===============================================================================
WHY DOES THIS WORK?
===============================================================================

The fixed pointer reduces

3Sum

↓

2Sum

The inner loop is exactly

Two Sum II.

Duplicate skipping guarantees

every triplet appears exactly once.

===============================================================================
PATTERN EVOLUTION
===============================================================================

Brute Force

↓

Three Nested Loops

↓

Already Know Two Sum

↓

Fix One Number

↓

Remaining Problem

↓

Two Sum

↓

Reuse Existing Pattern

↓

O(n²)

===============================================================================
COMPOSITION PROOF
===============================================================================

Original Problem

a + b + c = target

------------------------------------------------------------

Fix

a

------------------------------------------------------------

Now

b + c = target - a

------------------------------------------------------------

This is exactly

Two Sum.

We didn't invent a new algorithm.

We reused an existing one.

That is

Composition.

===============================================================================
TIME COMPLEXITY
===============================================================================

Sorting

O(n log n)

Outer Loop

O(n)

Inner Two Sum

O(n)

Overall

O(n²)

===============================================================================
SPACE COMPLEXITY
===============================================================================

Ignoring output list

O(1)

===============================================================================
COMMON MISTAKES
===============================================================================

1.

Forgetting to sort.

Then

Two Pointer Elimination

doesn't work.

------------------------------------------------------------

2.

Not skipping duplicate fixed values.

Duplicate triplets appear.

------------------------------------------------------------

3.

Skipping duplicates BEFORE storing.

Wrong.

Store first.

Then skip duplicates.

------------------------------------------------------------

4.

Thinking this is a completely
different algorithm.

It is simply

2Sum

inside another loop.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why must the array be sorted?

------------------------------------------------------------

2.

Why does fixing one number
reduce the problem?

------------------------------------------------------------

3.

Why skip duplicate fixed values?

------------------------------------------------------------

4.

Why skip duplicate left/right values
after finding an answer?

------------------------------------------------------------

5.

How would this idea extend to

4Sum

or

k-Sum?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Two Sum II
(LeetCode 167)

2.

Intersection of Two Arrays
(LeetCode 349)

------------------------------------------------------------

Medium

3.

3Sum Closest
(LeetCode 16)

4.

4Sum
(LeetCode 18)

------------------------------------------------------------

Hard

5.

k-Sum (Generalized)

Implement a recursive solution that
reduces

kSum

↓

(k-1)Sum

↓

...

↓

2Sum

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

Fix one.

Reduce the problem.

Reuse Two Sum.

Skip duplicates.

===============================================================================

"""