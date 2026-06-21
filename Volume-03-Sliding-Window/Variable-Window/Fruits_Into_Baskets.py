"""
===============================================================================
Problem: Fruits Into Baskets
Pattern: Variable Sliding Window
Reinforcement Problem
===============================================================================

Problem Statement
-----------------

You are given an array

fruits,

where each number represents a fruit type.

You have

two baskets.

Each basket can store only

one

type of fruit,

but it can hold an unlimited quantity of that type.

Return the maximum number of fruits you can collect by picking fruits from a
contiguous subarray.

You must stop as soon as a third fruit type appears.

-------------------------------------------------------------------------------

Example

Input

fruits = [1, 2, 1]

Output

3

Explanation

Both baskets are sufficient.

Basket 1

Fruit Type 1

Basket 2

Fruit Type 2

-------------------------------------------------------------------------------

Example

Input

fruits = [0, 1, 2, 2]

Output

3

Explanation

Collect

[1, 2, 2]

-------------------------------------------------------------------------------

Example

Input

fruits = [1, 2, 3, 2, 2]

Output

4

Explanation

Collect

[2, 3, 2, 2]

===============================================================================
Why This Reinforcement Problem Exists
===============================================================================

This problem exists to teach one of the most important lessons in interviews.

Different stories

do not necessarily require

different algorithms.

At first glance,

this problem appears completely different from

Longest Substring with At Most K Distinct Characters.

One talks about

characters.

The other talks about

fruit baskets.

However,

after removing the story,

both problems become identical.

===============================================================================
Relationship with Previous Problem
===============================================================================

Longest Substring with At Most K Distinct Characters

↓

Characters

↓

Distinct Count <= k

-------------------------------------------------------------------------------

Fruits Into Baskets

↓

Fruit Types

↓

Distinct Count <= 2

-------------------------------------------------------------------------------

The only difference is

that

k

is permanently fixed as

2.

Everything else remains identical.

===============================================================================
What Changed?
===============================================================================

Absolutely nothing

about the algorithm.

Previous Problem

Validity

Distinct Count <= k

-------------------------------------------------------------------------------

Current Problem

Validity

Distinct Count <= 2

-------------------------------------------------------------------------------

Frequency Map

↓

Same

-------------------------------------------------------------------------------

Expand

↓

Same

-------------------------------------------------------------------------------

Shrink

↓

Same

-------------------------------------------------------------------------------

Update Answer

↓

Same

Only one number changed.

k

became

2.

===============================================================================
Runnable Python Code
===============================================================================
"""


def fruits_into_baskets(fruits):

    left = 0

    longest_length = 0

    frequency = {}

    distinct_count = 0

    for right in range(len(fruits)):

        fruit = fruits[right]

        if fruit in frequency:
            frequency[fruit] = frequency[fruit] + 1
        else:
            frequency[fruit] = 1
            distinct_count = distinct_count + 1

        while distinct_count > 2:

            leaving_fruit = fruits[left]

            frequency[leaving_fruit] = (
                frequency[leaving_fruit] - 1
            )

            if frequency[leaving_fruit] == 0:

                del frequency[leaving_fruit]

                distinct_count = distinct_count - 1

            left = left + 1

        current_window_length = right - left + 1

        if current_window_length > longest_length:
            longest_length = current_window_length

    return longest_length


"""
===============================================================================
Key Insight
===============================================================================

This is

not

a new algorithm.

It is exactly the previous algorithm

wearing a different story.

Characters

↓

Fruit Types

Distinct Count <= k

↓

Distinct Count <= 2

Frequency Map

↓

Frequency Map

Expand

↓

Expand

Shrink

↓

Shrink

Update Answer

↓

Update Answer

Nothing changed.

Recognizing this quickly

is a hallmark of strong pattern recognition.

===============================================================================
Complexity
===============================================================================

Time Complexity

O(n)

Each fruit enters

and

leaves

the window

at most once.

-------------------------------------------------------------------------------

Space Complexity

General Case

O(n)

If the number of possible fruit types is bounded,

the auxiliary space behaves like

O(1).

===============================================================================
Interview Question
===============================================================================

Suppose I already know how to solve

Longest Substring with At Most K Distinct Characters.

How would I solve

Fruits Into Baskets?

Expected Answer

Replace

k

with

2.

Everything else remains exactly the same.

===============================================================================
Memory Hook
===============================================================================

"Ignore the story.

Fruit types are just characters.

Two baskets simply mean

at most two distinct values."
```
"""