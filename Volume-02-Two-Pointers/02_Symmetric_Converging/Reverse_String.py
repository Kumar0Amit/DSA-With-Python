"""
===============================================================================
Problem: Reverse String
LeetCode: 344
Pattern: Two Pointers -> Symmetric Converging
Difficulty: Easy
===============================================================================

PROBLEM DESCRIPTION
-------------------

You are given an array of characters.

Reverse the array IN-PLACE.

You are NOT allowed to create another array.

Example

Input

['h','e','l','l','o']

Output

['o','l','l','e','h']

------------------------------------------------------------

Notice

We are not sorting.

We are not creating another array.

We simply need to reverse the existing array.

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

What should the final array look like?

Answer

First character should become last.

Second should become second last.

Third should become third last.

Every position has exactly one mirror position.

------------------------------------------------------------

Question 2

Do we really need another array?

No.

Once we swap two mirror positions,
both become permanently correct.

------------------------------------------------------------

Question 3

Who should process the left side?

Left Pointer.

------------------------------------------------------------

Question 4

Who should process the right side?

Right Pointer.

------------------------------------------------------------

Question 5

After swapping one pair,
do we ever need those positions again?

No.

Both positions are finished forever.

Move both pointers inward.

===============================================================================
INVARIANT
===============================================================================

Everything OUTSIDE the two pointers
has already been reversed correctly.

Nothing outside the pointers
will ever need to be touched again.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Left Pointer

- Points to the next unprocessed character
  from the left.

------------------------------------------------------------

Right Pointer

- Points to the next unprocessed character
  from the right.

------------------------------------------------------------

Both pointers perform the SAME job.

Neither is a Reader.

Neither is a Writer.

===============================================================================
"""


def reverse_string(s):

    left = 0
    right = len(s) - 1

    while left < right:

        s[left], s[right] = s[right], s[left]

        left = left + 1
        right = right - 1


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    chars = ['h', 'e', 'l', 'l', 'o']

    reverse_string(chars)

    print(chars)


"""
===============================================================================
DRY RUN
===============================================================================

Initial

['h','e','l','l','o']

L                     R

------------------------------------------------------------

Swap

h <-> o

Array

['o','e','l','l','h']

Move

L++

R--

------------------------------------------------------------

Now

['o','e','l','l','h']

    L             R

Swap

e <-> l

Array

['o','l','l','e','h']

Move

L++

R--

------------------------------------------------------------

Now

['o','l','l','e','h']

        L
        R

Left is no longer less than Right.

Loop ends.

Array is completely reversed.

===============================================================================
WHY DOES THIS WORK?
===============================================================================

Each swap permanently fixes TWO positions.

The left position gets its correct value.

The right position gets its correct value.

Those positions never need to be visited again.

Therefore,

after every swap,

the processed portion grows from both ends.

The invariant remains true.

===============================================================================
TIME COMPLEXITY
===============================================================================

Each character participates in at most one swap.

Time

O(n)

===============================================================================
SPACE COMPLEXITY
===============================================================================

Only two pointers are used.

O(1)

===============================================================================
COMMON MISTAKES
===============================================================================

1.

Using another array.

Correct,

but violates the in-place requirement.

------------------------------------------------------------

2.

Moving only one pointer.

Then one side keeps getting processed.

Invariant breaks.

------------------------------------------------------------

3.

Using

while left <= right

without understanding why.

The middle element of an odd-length array
does not need swapping.

Using

while left < right

is enough.

------------------------------------------------------------

4.

Forgetting to move pointers after swapping.

Infinite loop.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why do both pointers move after a swap?

------------------------------------------------------------

2.

What invariant is maintained?

------------------------------------------------------------

3.

Why don't we revisit swapped positions?

------------------------------------------------------------

4.

Why is

while left < right

sufficient?

------------------------------------------------------------

5.

How is this different from Reader / Writer?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Reverse Prefix of Word
(LeetCode 2000)

2.

Reverse String II
(LeetCode 541)

------------------------------------------------------------

Medium

3.

Reverse Words in a String
(LeetCode 151)

4.

Reverse Words in a String III
(LeetCode 557)

------------------------------------------------------------

Hard

5.

Reverse Nodes in k-Group
(LeetCode 25)

(Extends the same reversing idea to Linked Lists.)

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

Swap one mirror pair.

Move inward.

Repeat.

===============================================================================

"""