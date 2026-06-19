"""
===============================================================================
Problem: Container With Most Water
LeetCode: 11
Pattern: Two Pointers -> Elimination
Difficulty: Medium
===============================================================================

PROBLEM DESCRIPTION
-------------------

You are given an array where each element represents the height of
a vertical line.

Choose two lines that, together with the x-axis,
can hold the maximum amount of water.

Return the maximum area.

------------------------------------------------------------

Example

Input

height = [1,8,6,2,5,4,8,3,7]

Output

49

Explanation

Choose

Height = 8

Height = 7

Width = 7

Area = 7 × 7 = 49

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

Can brute force solve it?

Yes.

Check every pair.

Compute every area.

Keep the largest.

Time

O(n²)

------------------------------------------------------------

Question 2

What determines the area?

Area

=

Width × Minimum(Left Height, Right Height)

Notice

The smaller wall decides
how much water can actually stay.

The taller wall cannot hold
more water than the shorter wall.

------------------------------------------------------------

Question 3

Suppose we move the taller wall.

Will the limiting height change?

No.

The shorter wall still limits the water.

Width also decreases.

Area can never improve.

------------------------------------------------------------

Question 4

Suppose we move the shorter wall.

Two possibilities exist.

Case 1

Next wall is shorter.

Area decreases.

------------------------------------------------------------

Case 2

Next wall is taller.

The limiting height increases.

Area MAY increase.

Only this movement has potential.

Therefore,

move the shorter wall.

===============================================================================
INVARIANT
===============================================================================

Every container using the discarded
shorter wall has already been proven
incapable of producing a better answer.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Left Pointer

Represents the current left wall.

------------------------------------------------------------

Right Pointer

Represents the current right wall.

------------------------------------------------------------

Every iteration

1.

Compute area.

2.

Update maximum.

3.

Move ONLY the shorter wall.

===============================================================================
"""


def max_area(height):

    left = 0
    right = len(height) - 1

    maximum_area = 0

    while left < right:

        width = right - left

        current_height = min(height[left], height[right])

        current_area = width * current_height

        if current_area > maximum_area:
            maximum_area = current_area

        if height[left] < height[right]:

            left = left + 1

        else:

            right = right - 1

    return maximum_area


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    height = [1,8,6,2,5,4,8,3,7]

    print(max_area(height))


"""
===============================================================================
DRY RUN
===============================================================================

height

[1,8,6,2,5,4,8,3,7]

------------------------------------------------------------

L = 0

R = 8

Width

8

Height

min(1,7)

=

1

Area

8 × 1 = 8

Maximum

8

Smaller wall

Left

Move Left.

------------------------------------------------------------

L = 1

R = 8

Width

7

Height

min(8,7)

=

7

Area

49

Maximum

49

Smaller wall

Right

Move Right.

------------------------------------------------------------

L = 1

R = 7

Width

6

Height

3

Area

18

Maximum remains

49

Smaller wall

Right

Move Right.

------------------------------------------------------------

Continue until

Left >= Right.

Return

49

===============================================================================
ELIMINATION PROOF
===============================================================================

Suppose

Left Height

=

5

Right Height

=

100

Area

=

5 × Width

------------------------------------------------------------

Move Right.

Width decreases.

Left Height remains

5.

New Area

=

5 × Smaller Width

Always smaller.

Impossible to improve.

------------------------------------------------------------

Move Left.

Width decreases.

BUT

New Left Height

may become

6

8

20

100

The limiting height may increase.

Area MAY increase.

Therefore,

moving the shorter wall is the ONLY
movement worth exploring.

===============================================================================
WHY DOES THIS WORK?
===============================================================================

Every iteration permanently removes
one impossible boundary.

Those containers are never checked again.

Search space keeps shrinking.

Eventually,

every possible useful container
has been considered.

===============================================================================
PATTERN EVOLUTION
===============================================================================

Brute Force

↓

Check every pair

↓

Area depends on

Width × Smaller Height

↓

Smaller wall limits water

↓

Move shorter wall

↓

Search space shrinks

↓

O(n)

===============================================================================
TIME COMPLEXITY
===============================================================================

Each pointer moves inward only once.

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

Moving the taller wall.

Wrong.

Limiting height never changes.

------------------------------------------------------------

2.

Thinking wider width
always gives larger area.

Height also matters.

------------------------------------------------------------

3.

Thinking taller wall
determines water.

Wrong.

Shorter wall always limits the water.

------------------------------------------------------------

4.

Moving both pointers.

Unnecessary.

Only one side has been proven impossible.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why does the shorter wall
determine the water level?

------------------------------------------------------------

2.

Why can't moving the taller wall
improve the answer?

------------------------------------------------------------

3.

What invariant is maintained?

------------------------------------------------------------

4.

Exactly what search space
gets eliminated?

------------------------------------------------------------

5.

If both heights are equal,

why is moving either pointer correct?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Two Sum II
(LeetCode 167)

2.

Valid Palindrome
(LeetCode 125)

------------------------------------------------------------

Medium

3.

Boats to Save People
(LeetCode 881)

4.

3Sum Closest
(LeetCode 16)

------------------------------------------------------------

Hard

5.

Trapping Rain Water
(LeetCode 42)

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

The shorter wall limits the water.

Move the limiter.

Never the supporter.

===============================================================================

"""