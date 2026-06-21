"""
===============================================================================
Problem: Longest Substring Without Repeating Characters
Pattern: Variable Sliding Window
Representative Problem of the Variable Window Variation
===============================================================================

Problem Statement
-----------------

Given a string

s,

return the length of the longest substring that contains

no repeated characters.

A substring must consist of contiguous characters.

-------------------------------------------------------------------------------

Example

Input

s = "abcabcbb"

Output

3

Explanation

The longest substring without repeating characters is

"abc"

whose length is

3.

-------------------------------------------------------------------------------

Example

Input

s = "bbbbb"

Output

1

Explanation

The longest substring without repeating characters is

"b".

-------------------------------------------------------------------------------

Example

Input

s = "pwwkew"

Output

3

Explanation

The longest substring without repeating characters is

"wke"

The substring

"pwke"

is not valid because it is not contiguous.

-------------------------------------------------------------------------------

Why is this problem important?

This is the second representative problem of the

Variable Sliding Window

pattern.

The previous representative problem,

Minimum Size Subarray Sum,

used

Running Sum

as its maintained state.

This problem introduces something completely different.

Instead of maintaining a number,

we maintain

a Frequency Map.

Even more importantly,

the validity condition changes.

Earlier

Validity

↓

Running Sum >= Target

Now

Validity

↓

Every character appears at most once.

The algorithmic framework remains identical.

Only the maintained state

and

the validity condition

have evolved.

"""

"""
===============================================================================
Brute Force
===============================================================================

Suppose we know nothing about Sliding Window.

How would we naturally solve this problem?

Start from every possible character.

Extend the substring one character at a time.

For every new substring,

check whether it contains duplicate characters.

If it does not,

update the best answer.

Repeat for every starting position.

-------------------------------------------------------------------------------

Example

String

abcabcbb

Start from

a

a

Valid

Length = 1

------------------------------------------------------------

ab

Valid

Length = 2

------------------------------------------------------------

abc

Valid

Length = 3

------------------------------------------------------------

abca

Contains duplicate

Stop.

-------------------------------------------------------------------------------

Now restart

from

b

Repeat everything again.

-------------------------------------------------------------------------------

Although this algorithm is correct,

it repeatedly checks

the same characters

and

rebuilds duplicate information

for heavily overlapping substrings.

That repeated work is what we want to eliminate.

"""

"""
===============================================================================
Observation
===============================================================================

Consider the current window

abc

Now a new character

a

arrives.

The window becomes

abca

Immediately,

the validity condition breaks.

Why?

Because

a

now appears twice.

Ask yourself

"What caused the window to become invalid?"

Only

one character.

The newly added

a.

Everything else

b

and

c

was already valid.

This is an important realization.

We do not need to rebuild the entire window.

We only need to restore validity.

How?

By removing characters

from the left

until the duplicate disappears.

This is the first Variable Window problem where

the shrink phase is driven by

duplicates,

not

by a running sum.

"""

"""
===============================================================================
Optimization Journey
===============================================================================

Stage 1

Build every substring independently.

↓

Repeated duplicate checking.

↓

O(n²)

or worse,

depending on implementation.

-------------------------------------------------------------------------------

Stage 2

Notice that neighboring substrings overlap heavily.

Instead of rebuilding,

maintain information about the current window.

-------------------------------------------------------------------------------

Stage 3

Maintain

a frequency map

for the current window.

This map tells us

how many times each character appears.

-------------------------------------------------------------------------------

Stage 4

Expand the window

by adding one new character.

Update its frequency.

-------------------------------------------------------------------------------

Stage 5

If the newly added character now appears

more than once,

the window becomes invalid.

-------------------------------------------------------------------------------

Stage 6

Shrink the window.

Remove characters from the left

until

every character appears at most once.

-------------------------------------------------------------------------------

Stage 7

The window is valid again.

Update the answer.

Continue expanding.

-------------------------------------------------------------------------------

Notice something beautiful.

The overall framework is identical to

Minimum Size Subarray Sum.

Only

the maintained state

and

the validity condition

changed.

"""

"""
===============================================================================
Repeated Work Being Eliminated
===============================================================================

Suppose

Current Window

abc

Frequency Map

a : 1

b : 1

c : 1

Now a new character

a

enters.

The brute-force solution would

rebuild

the entire frequency information

for

abca.

Instead,

we simply update

one entry.

a

becomes

2.

Immediately,

the frequency map tells us

the window is invalid.

There is no need to recount

b

or

c.

They have not changed.

After shrinking,

we only update

the frequencies of the characters

that leave the window.

Every update remains local.

"""

"""
===============================================================================
Maintained State
===============================================================================

The maintained state is now

Window Frequency Map.

Unlike the previous representative problem,

we no longer care about

a running sum.

Instead,

we care about

how many times

each character appears.

The maintained state serves two purposes.

Purpose 1

Describe the current window.

Purpose 2

Determine whether

the current window is valid.

If any character has

frequency greater than

1,

the window is invalid.

"""

"""
===============================================================================
Core Invariant
===============================================================================

Throughout the algorithm,

the frequency map

must always represent

exactly

the characters inside the current window.

Furthermore,

after the shrinking phase completes,

every character in the window

must have

frequency equal to

1.

This means

the current window is valid.

The invariant is restored

every time

the shrinking process finishes.

"""

"""
===============================================================================
Pointer Responsibilities
===============================================================================

Right Pointer

Responsible for

expanding the window.

It introduces

one new character

into the frequency map.

Sometimes,

that new character breaks the validity condition.

-------------------------------------------------------------------------------

Left Pointer

Responsible for

restoring validity.

Whenever a duplicate appears,

the left pointer removes characters

until

the duplicate disappears.

-------------------------------------------------------------------------------

Frequency Map

Always represents

the current window.

Its frequencies determine

whether the window is valid.

-------------------------------------------------------------------------------

Longest Length

Stores

the largest valid window

found so far.

Unlike

the previous representative problem,

we now want

the largest

valid window,

not

the smallest.

This changes

when

we update the answer,

but not

the overall Sliding Window framework.

"""

"""
===============================================================================
Algorithm (Reasoning Only)
===============================================================================

Step 1

Begin with an empty window.

-------------------------------------------------------------------------------

Step 2

Expand the window

by adding the next character.

Update

its frequency.

-------------------------------------------------------------------------------

Step 3

Check the validity condition.

Does any character now appear

more than once?

-------------------------------------------------------------------------------

If No

The window is valid.

Update

the longest length.

Continue expanding.

-------------------------------------------------------------------------------

If Yes

The window is invalid.

Begin shrinking.

-------------------------------------------------------------------------------

Step 4

Remove characters

from the left.

Decrease their frequencies.

Continue shrinking

until

every character appears

only once.

-------------------------------------------------------------------------------

Step 5

The window is valid again.

Update

the longest length.

Continue expanding.

-------------------------------------------------------------------------------

Repeat until

the right pointer

has processed every character.

Notice something.

In the previous representative problem,

the validity condition depended on

a number.

Now,

the validity condition depends on

the structure

of the frequency map.

The framework remains identical.

Only the definition of

"valid"

has changed.

"""

"""
===============================================================================
Runnable Python Code
===============================================================================

The implementation below follows exactly the reasoning developed earlier.

Notice that the overall Variable Sliding Window framework has not changed.

Expand

↓

Check Validity

↓

Shrink Until Valid

↓

Update Answer

The only difference from the previous representative problem is

how validity is determined.

Previously,

Running Sum >= Target

Now,

No character should have a frequency greater than 1.
"""


def longest_substring_without_repeating_characters(s):

    # -------------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------------

    left = 0

    longest_length = 0

    frequency = {}

    # -------------------------------------------------------------------------
    # Expand the window
    # -------------------------------------------------------------------------

    for right in range(len(s)):

        current_character = s[right]

        if current_character in frequency:
            frequency[current_character] = (
                frequency[current_character] + 1
            )
        else:
            frequency[current_character] = 1

        # ---------------------------------------------------------------------
        # Window became invalid.
        # Restore validity by shrinking.
        # ---------------------------------------------------------------------

        while frequency[current_character] > 1:

            leaving_character = s[left]

            frequency[leaving_character] = (
                frequency[leaving_character] - 1
            )

            if frequency[leaving_character] == 0:
                del frequency[leaving_character]

            left = left + 1

        # ---------------------------------------------------------------------
        # Window is valid.
        # Update the answer.
        # ---------------------------------------------------------------------

        current_window_length = right - left + 1

        if current_window_length > longest_length:
            longest_length = current_window_length

    return longest_length


"""
===============================================================================
Example Run
===============================================================================

Input

s = "abcabcbb"

-------------------------------------------------------------------------------

Output

3

-------------------------------------------------------------------------------

Explanation

The longest valid substring is

"abc"

whose length is

3.

-------------------------------------------------------------------------------

Example

print(longest_substring_without_repeating_characters("abcabcbb"))

Output

3
"""


"""
===============================================================================
Step-by-Step Dry Run
===============================================================================

Input

abcabcbb

-------------------------------------------------------------------------------

Initial State

Left = 0

Right = 0

Frequency = {}

Longest Length = 0

-------------------------------------------------------------------------------

Expand

Add

a

Frequency

a : 1

Window

a

Valid?

Yes

Current Length

1

Longest Length

1

-------------------------------------------------------------------------------

Expand

Add

b

Frequency

a : 1

b : 1

Window

ab

Valid?

Yes

Current Length

2

Longest Length

2

-------------------------------------------------------------------------------

Expand

Add

c

Frequency

a : 1

b : 1

c : 1

Window

abc

Valid?

Yes

Current Length

3

Longest Length

3

-------------------------------------------------------------------------------

Expand

Add

a

Frequency

a : 2

b : 1

c : 1

Window

abca

Valid?

No

Duplicate

a

appeared.

Begin shrinking.

-------------------------------------------------------------------------------

Shrink

Remove

a

from the left.

Frequency

a : 1

b : 1

c : 1

Left moves forward.

Window

bca

Valid?

Yes

Current Length

3

Longest Length

Still

3

-------------------------------------------------------------------------------

Expand

Add

b

Window

bcab

Frequency

b : 2

Duplicate found.

Shrink again.

Remove

b

from the left.

Window

cab

Frequency

b : 1

c : 1

a : 1

Window becomes valid again.

Length

3

Longest Length

Still

3

-------------------------------------------------------------------------------

The algorithm continues using the same rhythm.

Expand

↓

Duplicate Appears

↓

Shrink Until Duplicate Disappears

↓

Expand Again

Eventually,

the right pointer reaches the end.

Return

3.

"""


"""
===============================================================================
Why This Algorithm Works
===============================================================================

The algorithm works because the only way a valid window can become invalid
is when the newly added character creates a duplicate.

Suppose the current window is valid.

Every character appears exactly once.

Now we add one new character.

Only two situations are possible.

-------------------------------------------------------------------------------

Situation 1

The new character has never appeared inside the current window.

The window remains valid.

We simply continue expanding.

-------------------------------------------------------------------------------

Situation 2

The new character already exists inside the current window.

Now exactly one duplicate has been created.

Notice something important.

No other character suddenly became invalid.

Only the newly added character caused the problem.

Therefore,

we only need to remove characters from the left

until

that duplicate disappears.

-------------------------------------------------------------------------------

Why do we stop shrinking?

The moment

frequency[current_character]

becomes

1,

the duplicate has been removed.

Every character now appears at most once.

The window is valid again.

Shrinking further would only make the window smaller,

which cannot help us find the

longest

valid substring.

Therefore,

we stop immediately after validity is restored.

-------------------------------------------------------------------------------

Think about the maintained state.

The frequency map is not used to calculate the answer.

Instead,

it tells us

whether the current window satisfies the required property.

The maintained state has become

a validity checker.

"""

"""
===============================================================================
Pattern Evolution
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

Notice what changed.

The Variable Sliding Window framework stayed exactly the same.

Only

the maintained state

and

the definition of validity

changed.

This is the central lesson of the Variable Window pattern.
"""

"""
===============================================================================
Correctness Proof
===============================================================================

A correct algorithm should work for every valid input,

not only for the examples we manually tested.

For this problem,

the proof is based on maintaining a frequency map that always represents
the current window.

-------------------------------------------------------------------------------

Claim

At every stage of the algorithm,

the frequency map

correctly represents

the frequency of every character

inside the current window.

Furthermore,

after the shrinking phase finishes,

every character inside the current window appears

exactly once.

Therefore,

the current window is always valid when we update the answer.

-------------------------------------------------------------------------------

Base Case

Initially,

the window is empty.

Frequency Map

=

{}

Left = 0

No characters are present.

The frequency map correctly represents the current window.

Therefore,

the invariant is true before the algorithm begins.

-------------------------------------------------------------------------------

Induction Step

Assume

before an iteration,

the frequency map correctly represents

the current window.

There are only two possible operations.

-------------------------------------------------------------------------------

Operation 1

Expand

The right pointer adds one new character.

The algorithm increases

that character's frequency.

Now,

the frequency map again represents

the current window.

The invariant remains true.

-------------------------------------------------------------------------------

Operation 2

Shrink

Suppose the new character created a duplicate.

The left pointer removes characters

one by one.

Every removal decreases the corresponding frequency.

When a frequency becomes zero,

the key is removed.

After every removal,

the frequency map again represents

the current window.

The invariant continues to hold.

-------------------------------------------------------------------------------

Why does shrinking stop at the correct moment?

The shrinking loop continues only while

frequency[current_character] > 1

The moment

frequency[current_character]

becomes

1,

the duplicate disappears.

Now

every character appears at most once.

The window becomes valid again.

Any additional shrinking would only remove valid characters

and make the window smaller.

Since our goal is to find

the longest

valid substring,

there is no benefit in shrinking further.

-------------------------------------------------------------------------------

Why is every candidate answer correct?

The algorithm updates

longest_length

only after

the shrinking phase has finished.

At that moment,

the window is guaranteed to satisfy

the validity condition.

Therefore,

every recorded answer corresponds to

a valid substring.

-------------------------------------------------------------------------------

Conclusion

The invariant is true initially.

It remains true after every expansion

and

every contraction.

Every valid window is considered.

Therefore,

the algorithm always returns

the length of the longest substring

without repeating characters.

===============================================================================
Time Complexity
===============================================================================

Suppose

n

is the length of the string.

-------------------------------------------------------------------------------

Right Pointer

Starts at the beginning.

Moves to the end exactly once.

Maximum movements

n

-------------------------------------------------------------------------------

Left Pointer

Also starts at the beginning.

Never moves backward.

Maximum movements

n

-------------------------------------------------------------------------------

Although

a while loop

appears inside

the for loop,

every character can be removed

from the window

only once.

Therefore,

the total number of shrinking operations

over the entire algorithm

is at most

n.

-------------------------------------------------------------------------------

Overall Time Complexity

O(n)

-------------------------------------------------------------------------------

Intuition

Every character

enters the window once

and

leaves the window once.

No character is processed repeatedly.

===============================================================================
Space Complexity
===============================================================================

The frequency map stores

only the characters currently inside the window.

General Case

If every character is different,

the map may contain

O(n)

entries.

Therefore,

General Space Complexity

O(n)

-------------------------------------------------------------------------------

Interview Assumption

If the alphabet is fixed

(for example,

26 lowercase English letters

or

128 ASCII characters),

the maximum number of keys

is bounded by a constant.

Therefore,

the auxiliary space behaves like

O(1).

===============================================================================
Common Mistakes
===============================================================================

Mistake 1

Checking the answer

before restoring validity.

Wrong

Expand

↓

Update Answer

↓

Shrink

Correct

Expand

↓

Shrink Until Valid

↓

Update Answer

Always record the answer

only after

the window becomes valid.

-------------------------------------------------------------------------------

Mistake 2

Using

if

instead of

while

during shrinking.

Suppose

Window

abca

Removing only one character

may not always eliminate the duplicate

in more general problems.

The correct approach is

continue shrinking

until

the validity condition becomes true.

-------------------------------------------------------------------------------

Mistake 3

Forgetting to decrease frequencies.

The frequency map must always describe

the current window.

Otherwise,

future validity checks become incorrect.

-------------------------------------------------------------------------------

Mistake 4

Forgetting to delete

zero-frequency keys.

Although this problem checks

frequency[current_character] > 1,

developing the habit of removing zero-frequency entries

keeps the maintained state synchronized

and is essential for many later Sliding Window problems.

-------------------------------------------------------------------------------

Mistake 5

Thinking

"We found one duplicate,

so the answer is finished."

The duplicate only tells us

that the window became invalid.

Our goal is to

restore validity

and continue searching.

===============================================================================
Interview Questions
===============================================================================

Question 1

Why do we shrink

only after

a duplicate appears?

-------------------------------------------------------------------------------

Question 2

Why is

while

preferred over

if

during shrinking?

-------------------------------------------------------------------------------

Question 3

Why is the answer updated

after

the shrinking phase?

-------------------------------------------------------------------------------

Question 4

How is this problem different from

Minimum Size Subarray Sum?

Expected Answer

Both use the same

Expand → Shrink

framework.

Only the maintained state

and

the validity condition

are different.

-------------------------------------------------------------------------------

Question 5

Suppose the problem asks for

the actual substring

instead of

its length.

What additional information would you store?

Expected Answer

Store

the starting index

and

the best length,

or

the left and right boundaries

whenever a better answer is found.

===============================================================================
Revision Problems
===============================================================================

Easy

1.

Longest Substring Without Repeating Characters

(Implement from memory.)

------------------------------------------------------------

2.

Longest Substring with Unique Digits

(Same pattern,

different alphabet.)

-------------------------------------------------------------------------------

Medium

1.

Longest Repeating Character Replacement

Introduces

Frequency Map

+

Maximum Frequency.

------------------------------------------------------------

2.

Longest Substring with At Most K Distinct Characters

Introduces

Distinct Count.

-------------------------------------------------------------------------------

Hard

1.

Minimum Window Substring

The most advanced Variable Window problem.

Introduces

Need

Have

Required

Satisfied

while preserving

the same Expand–Shrink framework.

===============================================================================
Pattern Evolution
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

Character Replacement

↓

Maintained State

Frequency Map

+

Maximum Frequency

↓

Validity

Window Size − Maximum Frequency <= k

------------------------------------------------------------

Notice the progression.

The Sliding Window framework

never changes.

The maintained state becomes richer,

and the validity condition becomes more sophisticated.

===============================================================================
One-Line Memory Hook
===============================================================================

"The moment a duplicate appears,
expand stops,
shrink restores uniqueness,
and only then is the window allowed to grow again."
"""

