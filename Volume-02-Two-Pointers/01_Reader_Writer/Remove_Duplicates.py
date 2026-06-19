"""
===============================================================================
Problem: Remove Duplicates from Sorted Array
LeetCode: 26
Pattern: Two Pointers -> Reader / Writer
Difficulty: Easy
===============================================================================

PROBLEM DESCRIPTION
-------------------

You are given a sorted integer array.

Example:

    nums = [1,1,2,2,3,4,4,5]

The array is already sorted.

Your task is to remove duplicate values IN-PLACE.

Important:

1. You CANNOT create another array.
2. Relative order of unique elements must remain the same.
3. Return the number of unique elements.

Example:

Input:

    [1,1,2,2,3,4,4,5]

After modification:

    [1,2,3,4,5, ?, ?, ?]

Return:

    5

Notice that values after the returned length don't matter.

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

What should the final array look like?

Answer

Only unique elements should appear at the beginning.

----------------------------------------------------

Question 2

Can we build this unique portion gradually?

Yes.

Instead of creating another array,
we can overwrite duplicates.

----------------------------------------------------

Question 3

Who should scan?

Reader.

----------------------------------------------------

Question 4

Who should remember where the next unique value belongs?

Writer.

----------------------------------------------------

Invariant

Everything from

index 0

to

Writer

contains ONLY unique values.

This invariant must never break.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Reader

- Scan every element.
- Detect whether current element is new.
- Never decide final position.

Writer

- Always point to the LAST unique element.
- Extend the finished portion.
- Never scan ahead.

===============================================================================
"""


def remove_duplicates(nums):

    # Edge case
    if len(nums) == 0:
        return 0

    # First element is always unique.
    writer = 0

    # Reader starts from second element.
    reader = 1

    while reader < len(nums):

        # Found a new unique value.
        if nums[reader] != nums[writer]:

            nums[writer + 1] = nums[reader]

            writer = writer + 1

        # Reader always continues scanning.
        reader = reader + 1

    return writer + 1


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    nums = [1, 1, 2, 2, 3, 4, 4, 5]

    length = remove_duplicates(nums)

    print("Unique Length :", length)
    print("Modified Array:", nums[:length])

"""
===============================================================================
DRY RUN
===============================================================================

Initial

Array

[1,1,2,2,3,4,4,5]

Writer = 0

Reader = 1

Finished Portion

[1]

------------------------------------------------------------

Reader = 1

nums[reader] == nums[writer]

1 == 1

Duplicate

Move Reader

Writer = 0

Reader = 2

Finished Portion

[1]

------------------------------------------------------------

Reader = 2

nums[reader] = 2

nums[writer] = 1

Different

Write

nums[writer+1] = nums[reader]

Array

[1,2,2,2,3,4,4,5]

Move Writer

Writer = 1

Move Reader

Reader = 3

Finished Portion

[1,2]

------------------------------------------------------------

Reader = 3

2 == 2

Duplicate

Reader++

------------------------------------------------------------

Reader = 4

3 != 2

Write

Array

[1,2,3,2,3,4,4,5]

Writer = 2

Reader = 5

Finished Portion

[1,2,3]

------------------------------------------------------------

Reader = 5

4 != 3

Write

Array

[1,2,3,4,3,4,4,5]

Writer = 3

Reader = 6

Finished Portion

[1,2,3,4]

------------------------------------------------------------

Reader = 6

Duplicate

Reader++

------------------------------------------------------------

Reader = 7

5 != 4

Write

Array

[1,2,3,4,5,4,4,5]

Writer = 4

Reader = 8

Loop Ends

Return

Writer + 1

5

===============================================================================
WHY DOES THIS WORK?
===============================================================================

Every element is visited exactly once.

Every unique element is written exactly once.

Duplicates are ignored.

Writer always points to the last unique value.

The invariant

"Everything before Writer is unique"

never breaks.

===============================================================================
TIME COMPLEXITY
===============================================================================

Reader visits every element once.

Writer only moves forward.

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

Comparing

nums[reader]

with

nums[reader-1]

instead of Writer.

Although this works for THIS problem,
it doesn't generalize to the entire Reader/Writer family.

Think in terms of Writer's responsibility.

------------------------------------------------------------

2.

Moving Writer for duplicates.

Wrong.

Writer moves ONLY after discovering a new unique value.

------------------------------------------------------------

3.

Returning Writer

instead of

Writer + 1

Writer stores an index.

The answer is the count.

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1. Remove Element
   (LeetCode 27)

2. Merge Strings Alternately
   (LeetCode 1768)

Medium

3. Sort Array By Parity
   (LeetCode 905)
   Think in-place partitioning.

4. Duplicate Zeros
   (LeetCode 1089)

Hard

5. First Missing Positive
   (LeetCode 41)

(Contains an advanced form of in-place index placement and is a good
next step after mastering Reader/Writer.)

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

Reader discovers.

Writer commits.

Finished portion always remains correct.

===============================================================================

"""