"""
===============================================================================
Problem: Longest Substring with At Most K Distinct Characters
Pattern: Variable Sliding Window
Reinforcement Problem
===============================================================================

Problem Statement
-----------------

Given a string

s

and an integer

k,

return the length of the longest substring containing

at most

k

distinct characters.

-------------------------------------------------------------------------------

Example

Input

s = "eceba"

k = 2

Output

3

Explanation

The substring

"ece"

contains only

2

distinct characters.

Its length is

3.

-------------------------------------------------------------------------------

Example

Input

s = "aa"

k = 1

Output

2

Explanation

The entire string

"aa"

contains only one distinct character.

===============================================================================
Why This Reinforcement Problem Exists
===============================================================================

This problem is intentionally placed immediately after

Longest Repeating Character Replacement.

It does

not

introduce a new Sliding Window algorithm.

Instead,

it teaches another important lesson.

Different interview questions

often reuse

the exact same framework.

Only

the maintained state

or

the validity condition

changes.

Your goal is not to memorize

another solution.

Your goal is to recognize

that this is the same

Expand → Shrink

framework you already know.

===============================================================================
Relationship with Previous Representative Problems
===============================================================================

Minimum Size Subarray Sum

↓

Maintained State

Running Sum

↓

Validity

Running Sum >= Target

------------------------------------------------------------

Longest Substring Without Repeating Characters

↓

Maintained State

Frequency Map

↓

Validity

Every Character Frequency <= 1

------------------------------------------------------------

Longest Repeating Character Replacement

↓

Maintained State

Frequency Map

+

Maximum Frequency

↓

Validity

Window Length - Maximum Frequency <= k

------------------------------------------------------------

This Problem

↓

Maintained State

Frequency Map

+

Distinct Count

↓

Validity

Distinct Count <= k

-------------------------------------------------------------------------------

Notice something.

The Sliding Window framework

never changed.

Only

the maintained state

and

the validity condition

changed.

===============================================================================
What Changed?
===============================================================================

Previous Problem

Question

How many replacements are required?

Validity

Window Length

-

Maximum Frequency

<=

k

-------------------------------------------------------------------------------

Current Problem

Question

How many distinct characters are currently inside the window?

Validity

Distinct Count

<=

k

-------------------------------------------------------------------------------

When a new character enters,

its frequency increases.

If its frequency changes

from

0

to

1,

the number of distinct characters increases.

-------------------------------------------------------------------------------

When a character leaves,

its frequency decreases.

If its frequency becomes

0,

that character no longer exists

inside the current window.

Therefore,

remove it from the frequency map

and

decrease

Distinct Count.

Everything else remains identical.

===============================================================================
Runnable Python Code
===============================================================================
"""


def longest_substring_with_at_most_k_distinct(s, k):

    if k == 0:
        return 0

    left = 0

    longest_length = 0

    frequency = {}

    distinct_count = 0

    for right in range(len(s)):

        current_character = s[right]

        if current_character in frequency:
            frequency[current_character] = (
                frequency[current_character] + 1
            )
        else:
            frequency[current_character] = 1
            distinct_count = distinct_count + 1

        while distinct_count > k:

            leaving_character = s[left]

            frequency[leaving_character] = (
                frequency[leaving_character] - 1
            )

            if frequency[leaving_character] == 0:

                del frequency[leaving_character]

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

Notice how little changed.

Previous Representative Problem

Frequency Map

+

Maximum Frequency

------------------------------------------------------------

Current Problem

Frequency Map

+

Distinct Count

------------------------------------------------------------

Expand

↓

Update Maintained State

↓

Window Valid?

↓

No

↓

Shrink

↓

Become Valid

↓

Update Answer

The framework is identical.

Only the definition of

"valid"

has changed.

===============================================================================
Complexity
===============================================================================

Time Complexity

O(n)

Each character enters

and

leaves

the window at most once.

-------------------------------------------------------------------------------

Space Complexity

General Case

O(n)

Interview Assumption

If the alphabet is fixed,

the auxiliary space behaves like

O(1).

===============================================================================
Interview Question
===============================================================================

Suppose you already know how to solve

Longest Substring Without Repeating Characters.

How would you modify that solution

to solve

Longest Substring with At Most K Distinct Characters?

Expected Answer

Instead of checking

whether a character appears twice,

maintain

Distinct Count

and shrink

while

Distinct Count > k.

===============================================================================
Memory Hook
===============================================================================

"Count characters,

not duplicates.

The window is valid

as long as

the number of distinct characters

does not exceed

k."
"""
