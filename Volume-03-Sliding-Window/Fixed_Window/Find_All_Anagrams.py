"""
===============================================================================
Problem: Find All Anagrams in a String
Pattern: Fixed Sliding Window
Representative Reinforcement Problem
===============================================================================

Problem Statement
-----------------

You are given two strings

s

and

p.

Return the starting indices of every substring in

s

that is an anagram of

p.

-------------------------------------------------------------------------------

Example

Input

s = "cbaebabacd"

p = "abc"

Output

[0, 6]

Explanation

Window

cba

is an anagram of

abc.

Window

bac

is also an anagram of

abc.

Therefore,

their starting indices

0

and

6

are returned.

===============================================================================
Why This Representative Problem Exists
===============================================================================

This problem is intentionally placed immediately after

Permutation in String.

Its purpose is not to introduce a new algorithm.

Its purpose is to teach an important lesson.

Changing the required output

does not necessarily require changing the algorithm.

Many interview questions are simply different ways of asking for the same
information.

Strong algorithmic thinking means recognizing

that the maintained state,

the invariant,

and the window mechanics

are identical.

Only the required output changes.

===============================================================================
Relationship with the Previous Problem
===============================================================================

Compare the two problems.

Permutation in String

↓

Question

"Does at least one valid window exist?"

Output

True / False

------------------------------------------------------------

Find All Anagrams

↓

Question

"Where are all the valid windows?"

Output

List of Starting Indices

------------------------------------------------------------

Everything else remains identical.

Same window size.

Same maintained state.

Same target frequency map.

Same window frequency map.

Same invariant.

Same sliding process.

The only difference is

what we do

after finding a valid window.

===============================================================================
Algorithm Difference
===============================================================================

Permutation in String

When

window_frequency == target_frequency

↓

Return

True

immediately.

------------------------------------------------------------

Find All Anagrams

When

window_frequency == target_frequency

↓

Store

the starting index

↓

Continue Sliding

No other part of the algorithm changes.

===============================================================================
Runnable Python Code
===============================================================================
"""


def find_all_anagrams(s, p):

    if len(p) > len(s):
        return []

    target_frequency = {}

    for character in p:

        if character in target_frequency:
            target_frequency[character] = (
                target_frequency[character] + 1
            )
        else:
            target_frequency[character] = 1

    window_frequency = {}

    window_size = len(p)

    for index in range(window_size):

        character = s[index]

        if character in window_frequency:
            window_frequency[character] = (
                window_frequency[character] + 1
            )
        else:
            window_frequency[character] = 1

    result = []

    if window_frequency == target_frequency:
        result.append(0)

    for right in range(window_size, len(s)):

        left = right - window_size

        leaving_character = s[left]

        window_frequency[leaving_character] = (
            window_frequency[leaving_character] - 1
        )

        if window_frequency[leaving_character] == 0:
            del window_frequency[leaving_character]

        entering_character = s[right]

        if entering_character in window_frequency:
            window_frequency[entering_character] = (
                window_frequency[entering_character] + 1
            )
        else:
            window_frequency[entering_character] = 1

        if window_frequency == target_frequency:

            start_index = right - window_size + 1

            result.append(start_index)

    return result


"""
===============================================================================
Key Insight
===============================================================================

Notice how little changed.

Earlier

Match

↓

Return True

Now

Match

↓

Store Index

↓

Continue

This is one of the most important habits of an algorithm engineer.

Never ask

"Is this a new problem?"

Instead ask

"What actually changed?"

If the maintained state,

the invariant,

and the window mechanics remain unchanged,

then you are probably looking at the same algorithm with a different output.

===============================================================================
Complexity
===============================================================================

Time Complexity

Same as

Permutation in String.

Space Complexity

Same as

Permutation in String.

===============================================================================
Interview Question
===============================================================================

Suppose I already know how to solve

Permutation in String.

How can I modify that solution to solve

Find All Anagrams?

Expected Answer

Replace

return True

with

append the current starting index

and continue processing the remaining windows.

===============================================================================
Memory Hook
===============================================================================

"Same algorithm.

Same maintained state.

Same invariant.

Different output."

"""