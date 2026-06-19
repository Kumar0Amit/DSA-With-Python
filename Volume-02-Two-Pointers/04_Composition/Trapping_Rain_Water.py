"""
===============================================================================
Problem: Trapping Rain Water
LeetCode: 42
Pattern: Two Pointers -> Finalization
Difficulty: Hard
===============================================================================

PROBLEM DESCRIPTION
-------------------

You are given an array where each element represents the height
of a building.

After rain falls,

water becomes trapped between buildings.

Return the TOTAL amount of trapped water.

------------------------------------------------------------

Example

Input

height =

[0,1,0,2,1,0,1,3,2,1,2,1]

Output

6

------------------------------------------------------------

Water above a building depends upon

1.

Tallest building on its left.

2.

Tallest building on its right.

The smaller of these two decides
the water level.

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

Can brute force solve it?

Yes.

For every building,

search

Tallest Left

Tallest Right

Compute

Water

Time

O(n²)

------------------------------------------------------------

Question 2

Can we precompute?

Yes.

Store

Left Max

Right Max

Then compute water.

Time

O(n)

Space

O(n)

------------------------------------------------------------

Question 3

Can we avoid extra space?

Yes.

Notice

We only need to know

which side is already finalized.

------------------------------------------------------------

Question 4

Which side becomes finalized?

The side with the SMALLER maximum.

Why?

Because

Water =

Minimum(Left Max, Right Max)

If

Left Max

is already smaller,

then regardless of how large

Right Max

becomes later,

Left Max

will still determine the answer.

Therefore

the current left position
can be finalized immediately.

===============================================================================
INVARIANT
===============================================================================

The pointer on the side having
the smaller maximum

already has enough information
to compute its water.

Its answer can never change again.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Left Pointer

Moves through the left side.

Maintains

Left Max.

------------------------------------------------------------

Right Pointer

Moves through the right side.

Maintains

Right Max.

------------------------------------------------------------

At every step

Compare

Left Max

Right Max

Process ONLY the smaller side.

===============================================================================
"""


def trap(height):

    if len(height) == 0:
        return 0

    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    water = 0

    while left < right:

        if left_max <= right_max:

            if height[left] >= left_max:

                left_max = height[left]

            else:

                water += left_max - height[left]

            left += 1

        else:

            if height[right] >= right_max:

                right_max = height[right]

            else:

                water += right_max - height[right]

            right -= 1

    return water


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    print(trap(height))


"""
===============================================================================
DRY RUN
===============================================================================

Initial

L = 0

R = 11

Left Max = 0

Right Max = 0

------------------------------------------------------------

Update

Left Max

0

Move Left

------------------------------------------------------------

Left Max = 1

Right Max = 0

Right side smaller.

Process Right.

------------------------------------------------------------

Continue.

Whenever

Left Max <= Right Max

Process Left.

------------------------------------------------------------

Whenever

Right Max < Left Max

Process Right.

------------------------------------------------------------

Each processed building

adds

Current Max

-

Current Height

to the answer.

Eventually

Pointers meet.

Total Water

6

===============================================================================
FINALIZATION PROOF
===============================================================================

Suppose

Left Max = 5

Right Max = 8

Current Building

Height = 2

------------------------------------------------------------

Water depends on

Minimum(5,8)

=

5

------------------------------------------------------------

Even if

Right Max

later becomes

20

Minimum

remains

5

------------------------------------------------------------

Therefore

The answer for this left building
is already fixed.

We do NOT need any more information.

Process it immediately.

------------------------------------------------------------

Exactly the same logic works
symmetrically for the right side.

===============================================================================
WHY DOES THIS WORK?
===============================================================================

Every building is processed
exactly once.

Each building waits until
its limiting boundary
is completely known.

Once finalized,

its answer never changes.

===============================================================================
PATTERN EVOLUTION
===============================================================================

Brute Force

↓

Find Left Max

Find Right Max

for every building

↓

Repeated searching

↓

Store arrays

↓

Left Max Array

Right Max Array

↓

Needless extra space

↓

Observe

Smaller maximum
already determines the answer

↓

Finalize one side

↓

O(n)

Space O(1)

===============================================================================
TIME COMPLEXITY
===============================================================================

Each pointer moves only once.

Time

O(n)

===============================================================================
SPACE COMPLEXITY
===============================================================================

Only two pointers
and two variables.

O(1)

===============================================================================
COMMON MISTAKES
===============================================================================

1.

Comparing

height[left]

with

height[right]

instead of

Left Max

and

Right Max.

Wrong reasoning.

------------------------------------------------------------

2.

Thinking larger boundary
determines water.

Wrong.

Smaller boundary always limits it.

------------------------------------------------------------

3.

Using current heights
instead of running maximums.

Water depends upon

Tallest Seen So Far.

------------------------------------------------------------

4.

Thinking this is
Container With Most Water.

Different proof.

Container

↓

Elimination.

Rain Water

↓

Finalization.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why do we compare

Left Max

and

Right Max

instead of

current heights?

------------------------------------------------------------

2.

Why is the smaller maximum
already finalized?

------------------------------------------------------------

3.

What invariant is maintained?

------------------------------------------------------------

4.

How does this improve over
the prefix/suffix array solution?

------------------------------------------------------------

5.

How is this different from
Container With Most Water?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Container With Most Water
(Review the proof difference.)

2.

Squares of a Sorted Array
(Review pointer movement.)

------------------------------------------------------------

Medium

3.

Product of Array Except Self
(Compare prefix/suffix thinking.)

4.

Maximum Score of a Good Subarray
(LeetCode 1793)

------------------------------------------------------------

Hard

5.

Trapping Rain Water II
(LeetCode 407)

(Extends the same idea to 2D
using a priority queue.)

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

Don't process the side
that might change.

Process the side
whose answer is already final.

===============================================================================

"""