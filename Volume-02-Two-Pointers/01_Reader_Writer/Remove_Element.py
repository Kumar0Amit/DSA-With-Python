"""
===============================================================================
Problem: Remove Element
LeetCode: 27
Pattern: Two Pointers -> Reader / Writer
Difficulty: Easy
===============================================================================

PROBLEM DESCRIPTION
-------------------

You are given an integer array nums and an integer val.

Remove all occurrences of val IN-PLACE.

You cannot create another array.

The relative order of the remaining elements should be preserved.

Return the number of remaining elements.

Example

Input

nums = [3,2,2,3]
val  = 3

Output

Length = 2

Modified Array

[2,2]

------------------------------------------------------------

Example

Input

nums = [0,1,2,2,3,0,4,2]
val = 2

Output

Length = 5

Modified Array

[0,1,3,0,4]

Notice

We are NOT deleting elements.

We are rebuilding the valid portion of the array.

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

What should remain?

Everything except val.

------------------------------------------------------------

Question 2

Can we build the remaining portion from left to right?

Yes.

------------------------------------------------------------

Question 3

Who scans?

Reader.

------------------------------------------------------------

Question 4

Who remembers where the next valid value belongs?

Writer.

------------------------------------------------------------

Question 5

If Reader sees val?

Ignore it.

Move Reader only.

------------------------------------------------------------

Question 6

If Reader sees a valid value?

Place it at Writer.

Move both pointers.

===============================================================================
INVARIANT
===============================================================================

Everything from

index 0

to

writer - 1

contains ONLY valid elements.

Their relative order is preserved.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Reader

- Scan every element.
- Decide whether current value should stay.

Writer

- Point to the next position where a valid value belongs.
- Extend the finished portion.

Reader discovers.

Writer commits.

===============================================================================
"""


def remove_element(nums, val):

    writer = 0
    reader = 0

    while reader < len(nums):

        if nums[reader] != val:

            nums[writer] = nums[reader]

            writer = writer + 1

        reader = reader + 1

    return writer


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    length = remove_element(nums, 2)

    print("Length :", length)
    print("Modified :", nums[:length])


"""
===============================================================================
DRY RUN
===============================================================================

Initial

nums

[0,1,2,2,3,0,4,2]

Remove

2

-----------------------------------------

Writer = 0

Reader = 0

Reader sees

0

Valid

Write

nums[0] = 0

Writer++

Reader++

-----------------------------------------

Writer = 1

Reader = 1

Reader sees

1

Valid

Write

nums[1] = 1

Writer++

Reader++

-----------------------------------------

Writer = 2

Reader = 2

Reader sees

2

Target value

Skip

Reader++

-----------------------------------------

Writer = 2

Reader = 3

Reader sees

2

Skip

Reader++

-----------------------------------------

Writer = 2

Reader = 4

Reader sees

3

Write

nums[2] = 3

Array

[0,1,3,2,3,0,4,2]

Writer++

Reader++

-----------------------------------------

Writer = 3

Reader = 5

Reader sees

0

Write

nums[3] = 0

Array

[0,1,3,0,3,0,4,2]

Writer++

Reader++

-----------------------------------------

Writer = 4

Reader = 6

Reader sees

4

Write

nums[4] = 4

Array

[0,1,3,0,4,0,4,2]

Writer++

Reader++

-----------------------------------------

Reader sees

2

Skip

Reader++

Reader reaches end.

Return

Writer

5

Finished Portion

[0,1,3,0,4]

===============================================================================
WHY DOES THIS WORK?
===============================================================================

Every element is scanned exactly once.

Only valid elements are copied.

Invalid elements are ignored.

Writer always points to the next free position.

The finished portion is always correct.

===============================================================================
TIME COMPLEXITY
===============================================================================

Reader scans once.

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

Trying to delete elements.

Deletion shifts elements repeatedly.

Unnecessary work.

------------------------------------------------------------

2.

Moving Writer even after finding val.

Wrong.

Writer only moves after placing a valid element.

------------------------------------------------------------

3.

Returning

writer + 1

Wrong.

Writer here already stores

the number of valid elements.

Return

writer

------------------------------------------------------------

4.

Using swap.

Swap works.

But rewriting is simpler.

We don't care where removed values go.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why is rewriting enough?

Why don't we need swapping?

------------------------------------------------------------

2.

What invariant is maintained?

------------------------------------------------------------

3.

Why doesn't Writer move after finding val?

------------------------------------------------------------

4.

Why is preserving relative order automatic?

------------------------------------------------------------

5.

How is this different from Move Zeroes?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Remove Duplicates from Sorted Array II
(LeetCode 80)

2.

Keep Multiplying Found Values by Two
(LeetCode 2154)

Medium

3.

Compress String
(LeetCode 443)

4.

Wiggle Sort
(LeetCode 280)

Hard

5.

First Missing Positive
(LeetCode 41)

===============================================================================
READER / WRITER COMPARISON
===============================================================================

Remove Duplicates

Writer points to

Last unique element.

Operation

Rewrite.

------------------------------------------------------------

Move Zeroes

Writer points to

Next non-zero position.

Operation

Swap.

------------------------------------------------------------

Remove Element

Writer points to

Next valid position.

Operation

Rewrite.

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

Reader filters.

Writer rebuilds.

Finished portion always stays valid.

===============================================================================

"""