"""
===============================================================================
Problem: Permutation in String
Pattern: Fixed Sliding Window
Representative Problem of the Fixed Window Variation
===============================================================================

Problem Statement
-----------------

You are given two strings.

s1

and

s2

Return

True

if any substring of

s2

is a permutation of

s1.

Otherwise,

return

False.

-------------------------------------------------------------------------------

Example

Input

s1 = "ab"

s2 = "eidbaooo"

Output

True

Explanation

The substring

"ba"

is a permutation of

"ab"

-------------------------------------------------------------------------------

Example

Input

s1 = "ab"

s2 = "eidboaoo"

Output

False

-------------------------------------------------------------------------------

Why is this problem important?

This is the first Fixed Window problem where

the maintained state is no longer

a single number.

Instead,

we maintain

an entire frequency map.

This teaches one of the biggest lessons of the Sliding Window pattern.

The algorithm does not depend on

what

you maintain.

It only depends on

whether

you can update that information locally.

"""

"""
===============================================================================
Brute Force
===============================================================================

Suppose we know nothing about Sliding Window.

How would we solve the problem?

Generate every substring of

s2

having length

len(s1).

For each substring,

count the frequency of every character.

Compare it with the frequency of

s1.

If they match,

return

True.

Otherwise,

continue.

-------------------------------------------------------------------------------

Example

s1

ab

Target Frequency

a : 1

b : 1

------------------------------------------------------------

Substring

ei

Frequency

e : 1

i : 1

No Match

------------------------------------------------------------

Substring

id

Frequency

i : 1

d : 1

No Match

------------------------------------------------------------

Substring

db

Frequency

d : 1

b : 1

No Match

------------------------------------------------------------

Substring

ba

Frequency

b : 1

a : 1

Match

Return

True

-------------------------------------------------------------------------------

This algorithm is correct.

However,

it rebuilds a new frequency map

for every substring.

That repeated work is expensive.

"""

"""
===============================================================================
Observation
===============================================================================

Compare two neighboring windows.

Window

ei

↓

Window

id

What actually changed?

Only two characters.

The character

e

left.

The character

d

entered.

The character

i

was already counted.

Why count it again?

Nothing about

i

changed.

The same observation applies to every pair of neighboring windows.

Only

one character leaves

and

one character enters.

Everything else remains identical.

This is exactly the same observation we discovered in

Maximum Sum

and

Count Even Numbers.

Only the maintained state has become richer.

"""

"""
===============================================================================
Optimization Journey
===============================================================================

Stage 1

Build a completely new frequency map

for every substring.

↓

Repeated Work

------------------------------------------------------------

Stage 2

Notice that neighboring windows overlap.

Only one character leaves.

Only one character enters.

------------------------------------------------------------

Stage 3

Instead of rebuilding the frequency map,

maintain

the frequency map

of the current window.

------------------------------------------------------------

Stage 4

Whenever the window moves,

decrease the frequency

of the leaving character.

Increase the frequency

of the entering character.

------------------------------------------------------------

Stage 5

Compare

the maintained frequency map

with

the target frequency map.

If they match,

a permutation has been found.

Return

True.

-------------------------------------------------------------------------------

Notice something remarkable.

The Sliding Window algorithm has not changed.

Only the maintained state has evolved.

"""

"""
===============================================================================
Repeated Work Being Eliminated
===============================================================================

Suppose

Current Window

ei

Frequency

e : 1

i : 1

The next window becomes

id

The brute-force algorithm

creates a brand new frequency map.

It counts

i

again,

even though

i

was already counted

in the previous window.

This is repeated work.

Instead,

we simply

remove

e

from the maintained map

and

add

d

to it.

Everything else remains valid.

Nothing else should be rebuilt.

"""

"""
===============================================================================
Maintained State
===============================================================================

Previous representative problems maintained

Running Sum

or

Running Even Count.

Those were both

single variables.

This problem requires more information.

We now maintain

Window Frequency Map

This map always stores

the frequency of every character

inside

the current window.

We also maintain

Target Frequency Map

Unlike the window frequency,

this map never changes.

It represents

what we are trying to match.

Notice that the maintained state has become richer,

but the Sliding Window algorithm itself remains unchanged.

"""

"""
===============================================================================
Core Invariant
===============================================================================

Throughout the entire algorithm,

the window frequency map

must always represent

exactly

the characters

inside

the current window.

Similarly,

the target frequency map

must always represent

the frequency of

s1.

Whenever the window moves,

the window frequency map

must immediately be updated

so that it once again describes

the current window

and nothing else.

If both frequency maps become identical,

the current window is a permutation of

s1.

"""

"""
===============================================================================
Pointer / Variable Responsibilities
===============================================================================

Left Side Responsibility

Remove the contribution

of the leaving character

from the maintained frequency map.

If its frequency becomes

zero,

remove the key entirely.

------------------------------------------------------------

Right Side Responsibility

Introduce

the entering character

into the maintained frequency map.

Increase its frequency.

------------------------------------------------------------

Window Frequency Responsibility

Always represent

exactly

the current window.

------------------------------------------------------------

Target Frequency Responsibility

Never changes.

It is the reference

against which every window

is compared.

------------------------------------------------------------

Answer Responsibility

The first time

both maps become identical,

return

True.

No further searching is necessary.

"""

"""
===============================================================================
Algorithm (Reasoning Only)
===============================================================================

Step 1

Build

the target frequency map

using

s1.

------------------------------------------------------------

Step 2

Build the first window

having size

len(s1).

Create

its frequency map.

------------------------------------------------------------

Step 3

Compare

both maps.

If they match,

return

True.

------------------------------------------------------------

Step 4

Slide the window.

------------------------------------------------------------

Step 5

Decrease

the leaving character's frequency.

------------------------------------------------------------

Step 6

Increase

the entering character's frequency.

------------------------------------------------------------

Step 7

Compare

both maps again.

If they match,

return

True.

------------------------------------------------------------

Step 8

If every window has been processed

without finding a match,

return

False.

-------------------------------------------------------------------------------

Notice the evolution.

Maximum Sum

↓

Running Sum

Count Even Numbers

↓

Running Count

Permutation in String

↓

Running Frequency Map

The maintained state changed.

The Fixed Window pattern did not.
"""
"""
===============================================================================
Runnable Python Code
===============================================================================

The implementation below follows exactly the reasoning developed earlier.

Notice that the Sliding Window mechanics are identical to the previous
Fixed Window problems.

The only thing that changed is the maintained state.

Instead of maintaining

Running Sum

or

Running Even Count,

we now maintain

Window Frequency Map.

The window size is fixed because every permutation of s1 must have exactly
len(s1) characters.
"""


def permutation_in_string(s1, s2):

    # -------------------------------------------------------------------------
    # Edge Case
    # -------------------------------------------------------------------------

    if len(s1) > len(s2):
        return False

    # -------------------------------------------------------------------------
    # Build the target frequency map
    # -------------------------------------------------------------------------

    target_frequency = {}

    for character in s1:

        if character in target_frequency:
            target_frequency[character] = target_frequency[character] + 1
        else:
            target_frequency[character] = 1

    # -------------------------------------------------------------------------
    # Build the first window frequency map
    # -------------------------------------------------------------------------

    window_frequency = {}

    window_size = len(s1)

    for index in range(window_size):

        character = s2[index]

        if character in window_frequency:
            window_frequency[character] = window_frequency[character] + 1
        else:
            window_frequency[character] = 1

    # -------------------------------------------------------------------------
    # Compare the first window
    # -------------------------------------------------------------------------

    if window_frequency == target_frequency:
        return True

    # -------------------------------------------------------------------------
    # Slide the window
    # -------------------------------------------------------------------------

    for right in range(window_size, len(s2)):

        left = right - window_size

        leaving_character = s2[left]

        window_frequency[leaving_character] = (
            window_frequency[leaving_character] - 1
        )

        if window_frequency[leaving_character] == 0:
            del window_frequency[leaving_character]

        entering_character = s2[right]

        if entering_character in window_frequency:
            window_frequency[entering_character] = (
                window_frequency[entering_character] + 1
            )
        else:
            window_frequency[entering_character] = 1

        if window_frequency == target_frequency:
            return True

    return False


"""
===============================================================================
Example Run
===============================================================================

Input

s1 = "ab"

s2 = "eidbaooo"

-------------------------------------------------------------------------------

Target Frequency

a : 1

b : 1

-------------------------------------------------------------------------------

Windows

ei

↓

id

↓

db

↓

ba

↓

ao

↓

oo

↓

oo

-------------------------------------------------------------------------------

The window

ba

has exactly the same frequency as

ab.

Therefore

Output

True
"""


"""
===============================================================================
Step-by-Step Dry Run
===============================================================================

Input

s1 = "ab"

s2 = "eidbaooo"

-------------------------------------------------------------------------------

Step 1

Build Target Frequency

Target

a : 1

b : 1

-------------------------------------------------------------------------------

Step 2

Build First Window

Window

ei

Window Frequency

e : 1

i : 1

Compare

Target

≠

Window

Continue.

-------------------------------------------------------------------------------

Step 3

Slide Window

Old Window

ei

↓

New Window

id

Leaving Character

e

Remove

e : 1

↓

Delete key because frequency becomes zero.

Window Frequency

i : 1

Entering Character

d

Window Frequency

i : 1

d : 1

Compare

Target

≠

Window

Continue.

-------------------------------------------------------------------------------

Step 4

Slide Again

Old Window

id

↓

New Window

db

Leaving Character

i

Remove

i

Entering Character

b

Window Frequency

d : 1

b : 1

Compare

Target

≠

Window

Continue.

-------------------------------------------------------------------------------

Step 5

Slide Again

Old Window

db

↓

New Window

ba

Leaving Character

d

Remove

d

Entering Character

a

Window Frequency

b : 1

a : 1

Compare

Window Frequency

==

Target Frequency

Permutation Found

Return

True

-------------------------------------------------------------------------------

Notice something important.

We never rebuilt the frequency map.

We only updated it.

Exactly one character left.

Exactly one character entered.

Everything else was carried forward.

This is precisely the same optimization philosophy used in every Fixed
Window problem.
"""


"""
===============================================================================
Why This Algorithm Works
===============================================================================

The algorithm works because of a fundamental property of permutations.

Two strings are permutations of one another

if and only if

their character frequencies are identical.

The order of characters does not matter.

Only the frequency matters.

-------------------------------------------------------------------------------

The target frequency map represents

exactly

what we are looking for.

Every window frequency map represents

exactly

what we currently have.

Whenever both maps become equal,

the current window contains exactly the same characters as s1.

Therefore,

the current window must be a permutation of s1.

-------------------------------------------------------------------------------

Why don't we rebuild the frequency map?

Neighboring windows overlap heavily.

When the window moves,

only one character leaves

and

one character enters.

Every other character remains unchanged.

Therefore,

rebuilding the entire map would repeat unnecessary work.

Instead,

we simply update the maintained frequency map.

-------------------------------------------------------------------------------

Think about the maintained state.

Maximum Sum maintained

Running Sum.

Count Even Numbers maintained

Running Even Count.

This problem maintains

Window Frequency.

The maintained state became richer,

but the Sliding Window algorithm itself remained almost identical.
"""


"""
===============================================================================
Pattern Evolution
===============================================================================

Maximum Sum of K Elements

↓

Maintained State

Running Sum

------------------------------------------------------------

Count Even Numbers

↓

Maintained State

Running Even Count

------------------------------------------------------------

Permutation in String

↓

Maintained State

Window Frequency Map

+

Target Frequency Map

------------------------------------------------------------

Notice the progression.

The Sliding Window framework never changed.

Only the information being maintained evolved.

This is exactly how algorithmic thinking develops.

You stop memorizing solutions.

You start recognizing

"What information should I maintain?"
"""
"""
===============================================================================
Correctness Proof
===============================================================================

A correct algorithm should not only produce the right answer.

It should also be possible to explain why it works for every valid input.

For this problem, the proof is based on maintaining two frequency maps.

-------------------------------------------------------------------------------

Claim

At every stage of the algorithm,

window_frequency

represents exactly the frequency of the characters inside the current window.

-------------------------------------------------------------------------------

Base Case

Before the sliding process begins,

we build the first complete window.

Every character inside that window is counted exactly once.

Therefore,

window_frequency

correctly represents the first window.

Hence,

the invariant is true before the sliding process starts.

-------------------------------------------------------------------------------

Induction Step

Assume that before sliding,

window_frequency

correctly represents the current window.

Now the window moves by one position.

Exactly one character leaves.

Exactly one character enters.

The algorithm performs two operations.

1.

Decrease the frequency of the leaving character.

If its frequency becomes zero,

remove it from the dictionary.

2.

Increase the frequency of the entering character.

No other character changes.

Therefore,

after these two updates,

window_frequency

again represents exactly the new window.

Hence,

the invariant remains true.

-------------------------------------------------------------------------------

Why does comparing the two maps work?

A permutation does not require the characters to appear in the same order.

It only requires

the same characters

with

the same frequencies.

Therefore,

if

window_frequency == target_frequency

then

the current window contains exactly the same multiset of characters as

s1.

Hence,

the current window is a permutation of

s1.

-------------------------------------------------------------------------------

Conclusion

The invariant is true initially.

It remains true after every slide.

Every possible window is examined exactly once.

Therefore,

if a permutation exists,

the algorithm will find it.

If no permutation exists,

the algorithm correctly returns

False.

===============================================================================
Time Complexity
===============================================================================

Let

m = len(s1)

n = len(s2)

-------------------------------------------------------------------------------

Building the target frequency map

requires

O(m)

-------------------------------------------------------------------------------

Building the first window

requires

O(m)

-------------------------------------------------------------------------------

Sliding the window

The window moves

n - m

times.

Each movement performs

• One decrement

• One increment

• One dictionary comparison

-------------------------------------------------------------------------------

Dictionary Comparison

In Python,

checking

window_frequency == target_frequency

compares the stored keys and values.

If the alphabet size is fixed (for example, lowercase English letters),

the number of distinct keys is bounded.

Therefore,

this comparison behaves like constant time.

For the more general case where the alphabet is unbounded,

the comparison depends on the number of distinct characters currently stored.

-------------------------------------------------------------------------------

Overall Time Complexity

Interview Assumption (bounded alphabet)

O(n + m)

General Case

O((n + m) × d)

where

d

is the number of distinct characters that may appear in the maps.

===============================================================================
Space Complexity
===============================================================================

Target Frequency Map

stores at most

the distinct characters in

s1.

Window Frequency Map

stores at most

the distinct characters in

the current window.

Therefore

General Space Complexity

O(d)

where

d

is the number of distinct characters.

Under the common interview assumption of a fixed alphabet,

the extra space is effectively constant.

===============================================================================
Common Mistakes
===============================================================================

Mistake 1

Building a new frequency map

for every window.

Why it is wrong

This repeats the same counting work again and again.

The maintained frequency map should evolve continuously.

-------------------------------------------------------------------------------

Mistake 2

Forgetting to decrease the frequency

of the leaving character.

The maintained state would now represent

Current Window

+

Expired Information.

The invariant immediately breaks.

-------------------------------------------------------------------------------

Mistake 3

Forgetting to delete keys

whose frequency becomes zero.

Example

Window Frequency

a : 1

b : 0

Target Frequency

a : 1

The dictionaries are not equal,

even though logically

b

is no longer present.

Always remove zero-frequency keys.

-------------------------------------------------------------------------------

Mistake 4

Using the wrong window size.

The window size must always equal

len(s1).

A permutation cannot have more or fewer characters.

-------------------------------------------------------------------------------

Mistake 5

Comparing the strings directly

instead of comparing their frequencies.

Permutations preserve

frequency,

not

order.

===============================================================================
Interview Questions
===============================================================================

Question 1

Why does comparing frequency maps correctly detect permutations?

-------------------------------------------------------------------------------

Question 2

Why must the window size always equal

len(s1)?

-------------------------------------------------------------------------------

Question 3

Why do we delete keys whose frequency becomes zero?

-------------------------------------------------------------------------------

Question 4

How is this problem different from

Maximum Sum of K Elements?

Expected Answer

The Sliding Window framework is identical.

Only the maintained state changes.

-------------------------------------------------------------------------------

Question 5

Suppose the problem asks for

all permutations

instead of just checking whether one exists.

How would the algorithm change?

Expected Answer

Instead of returning immediately,

store the starting index of every matching window and continue sliding.

===============================================================================
Revision Problems
===============================================================================

Easy

1.

Check if two strings are anagrams.

(Maintained State

Frequency Map)

------------------------------------------------------------

2.

Find all anagrams in a string.

(Same algorithm.

Different output.)

-------------------------------------------------------------------------------

Medium

1.

Permutation in String

(Implement from memory.)

------------------------------------------------------------

2.

Group Anagrams

(Uses the same frequency idea,

but not Sliding Window.)

-------------------------------------------------------------------------------

Hard (Relative to This Variation)

1.

Minimum Window Substring

Notice the evolution.

Instead of matching

a fixed-size window,

you must discover

the smallest valid window.

This leads naturally into

Variable Sliding Window.

===============================================================================
Pattern Evolution
===============================================================================

Maximum Sum of K Elements

↓

Maintained State

Running Sum

↓

Count Even Numbers

↓

Maintained State

Running Even Count

↓

Permutation in String

↓

Maintained State

Target Frequency Map

+

Window Frequency Map

↓

Find All Anagrams

↓

Same Maintained State

Different Output

-------------------------------------------------------------------------------

Notice the evolution.

The complexity of the maintained state increases.

The Sliding Window framework remains unchanged.

This is the hallmark of mastering patterns instead of memorizing problems.

===============================================================================
One-Line Memory Hook
===============================================================================

"A permutation is defined by frequency, not order.
Maintain the window's frequency map, compare it with the target, and slide
without rebuilding."
"""

