"""
===============================================================================
Problem: Longest Repeating Character Replacement
Pattern: Variable Sliding Window
Representative Problem of the Variable Window Variation
===============================================================================

Problem Statement
-----------------

You are given a string

s

consisting of uppercase English letters

and an integer

k.

You may replace

at most

k

characters.

Return the length of the longest substring that can be converted into a
substring containing only one repeating character.

-------------------------------------------------------------------------------

Example

Input

s = "ABAB"

k = 2

Output

4

Explanation

Replace the two

B

characters with

A.

Result

AAAA

Length

4

-------------------------------------------------------------------------------

Example

Input

s = "AABABBA"

k = 1

Output

4

Explanation

One optimal window is

AABA

Replace

B

with

A.

Result

AAAA

Length

4

-------------------------------------------------------------------------------

Why is this problem important?

This is the third representative problem of the

Variable Sliding Window

pattern.

The previous representative problem,

Longest Substring Without Repeating Characters,

introduced

Frequency Map

as the maintained state.

This problem introduces something even more interesting.

We still maintain

a Frequency Map,

but now we also maintain

Maximum Frequency.

Even more importantly,

we learn that

Maximum Frequency

does not always need to be perfectly accurate.

This is the first Sliding Window problem where

maintaining slightly stale information

is still sufficient to produce the correct answer.

That idea appears in many advanced algorithms.

"""

"""
===============================================================================
Brute Force
===============================================================================

Suppose we know nothing about Sliding Window.

How would we naturally solve this problem?

Generate every possible substring.

For every substring,

count the frequency of every character.

Find

the most frequent character.

Compute

Replacement Needed

Window Length

-

Maximum Frequency

If the replacements required are

less than or equal to

k,

the substring is valid.

Update the answer.

Repeat for every possible substring.

-------------------------------------------------------------------------------

Example

Window

AABA

Frequency

A : 3

B : 1

Maximum Frequency

3

Window Length

4

Replacement Needed

4 - 3 = 1

Valid

-------------------------------------------------------------------------------

Window

AABAB

Frequency

A : 3

B : 2

Maximum Frequency

3

Window Length

5

Replacement Needed

5 - 3 = 2

If

k = 1

Invalid

-------------------------------------------------------------------------------

This brute-force algorithm is correct.

However,

it repeatedly rebuilds the frequency map

and repeatedly searches for

the maximum frequency

for every possible substring.

That repeated work is what we want to eliminate.

"""

"""
===============================================================================
Observation
===============================================================================

Suppose the current window is

AABA

Frequency

A : 3

B : 1

To make every character the same,

which character should we keep?

Always keep

the character that already appears

the most.

Changing

three

A

characters into

B

would require

3

replacements.

Changing

one

B

into

A

requires only

1

replacement.

Therefore,

the optimal strategy is always

to keep the majority character

and replace everything else.

This gives us an important formula.

Replacement Needed

=

Window Length

-

Maximum Frequency

If

Replacement Needed <= k

the window is valid.

Otherwise,

the window is invalid.

This formula becomes the validity condition for the entire algorithm.

"""

"""
===============================================================================
Optimization Journey
===============================================================================

Stage 1

Generate every substring.

↓

Build a new frequency map.

↓

Find the maximum frequency.

↓

Compute replacements.

↓

Repeated work.

-------------------------------------------------------------------------------

Stage 2

Notice that neighboring windows overlap.

Instead of rebuilding,

maintain

the frequency map

of the current window.

-------------------------------------------------------------------------------

Stage 3

Maintain

Maximum Frequency

along with

the frequency map.

Now,

the replacement count can be computed instantly.

-------------------------------------------------------------------------------

Stage 4

Expand the window.

Update

the frequency

of the entering character.

Update

Maximum Frequency

if necessary.

-------------------------------------------------------------------------------

Stage 5

Check the validity condition.

Replacement Needed

=

Window Length

-

Maximum Frequency

-------------------------------------------------------------------------------

If the window becomes invalid,

shrink it

until it becomes valid again.

-------------------------------------------------------------------------------

Notice that the framework has not changed.

Only

the maintained state

and

the validity condition

have become richer.

"""

"""
===============================================================================
Repeated Work Being Eliminated
===============================================================================

Suppose

Current Window

AABA

Frequency

A : 3

B : 1

Now

one new character

B

enters.

The brute-force solution would

rebuild

the entire frequency map

and

recalculate

the maximum frequency.

Instead,

we simply

increase

B's frequency.

Frequency

A : 3

B : 2

Maximum Frequency

remains

3.

Every update is local.

Nothing is rebuilt.

The maintained state evolves

together with the window.

"""

"""
===============================================================================
Maintained State
===============================================================================

This problem maintains

two

pieces of information.

-------------------------------------------------------------------------------

1.

Frequency Map

Stores

how many times

each character appears

inside the current window.

-------------------------------------------------------------------------------

2.

Maximum Frequency

Stores

the highest frequency

of any character

seen inside the current window.

-------------------------------------------------------------------------------

These two maintained states

allow us to compute

Replacement Needed

without scanning

the frequency map

every time.

This transforms

a repeated computation

into

a constant-time calculation.

"""

"""
===============================================================================
Core Invariant
===============================================================================

Throughout the algorithm,

the frequency map

must always represent

exactly

the current window.

The value

Maximum Frequency

must always be

at least

the true maximum frequency

currently inside the window.

Notice something unusual.

Unlike previous problems,

Maximum Frequency

is allowed to become

slightly stale.

We will later prove

why this does

not

affect correctness.

This is the defining idea of this problem.

"""

"""
===============================================================================
Pointer Responsibilities
===============================================================================

Right Pointer

Expands the window.

Updates

the frequency map.

Updates

Maximum Frequency

when a new higher frequency is discovered.

-------------------------------------------------------------------------------

Left Pointer

Shrinks the window

whenever

the replacement requirement

exceeds

k.

While shrinking,

the frequency map

is updated.

Notice that

Maximum Frequency

is intentionally

not decreased.

We will later prove

why this optimization is safe.

-------------------------------------------------------------------------------

Frequency Map

Always represents

the exact frequencies

inside the current window.

-------------------------------------------------------------------------------

Maximum Frequency

Stores

the largest frequency

observed while expanding.

It may become stale,

but it never becomes

smaller

than the true maximum.

-------------------------------------------------------------------------------

Longest Length

Stores

the largest valid window

found so far.

"""

"""
===============================================================================
Algorithm (Reasoning Only)
===============================================================================

Step 1

Begin with an empty window.

-------------------------------------------------------------------------------

Step 2

Expand the window.

Increase

the frequency

of the new character.

Update

Maximum Frequency

if necessary.

-------------------------------------------------------------------------------

Step 3

Compute

Replacement Needed

Window Length

-

Maximum Frequency

-------------------------------------------------------------------------------

If

Replacement Needed <= k

The window is considered valid.

Update

the longest length.

Continue expanding.

-------------------------------------------------------------------------------

If

Replacement Needed > k

Shrink the window.

Decrease

the frequency

of the leaving character.

Do

not

decrease

Maximum Frequency.

Continue shrinking

until

the window becomes valid again.

-------------------------------------------------------------------------------

Repeat until

the right pointer

reaches the end of the string.

Notice something new.

This is the first Variable Window problem

where

one maintained variable

is intentionally

allowed to become stale.

The proof of why this works

is the most important lesson of this representative problem.

"""

"""
===============================================================================
Runnable Python Code
===============================================================================

The implementation below follows exactly the reasoning developed earlier.

This is the first Sliding Window algorithm where one maintained variable

maximum_frequency

is intentionally allowed to become stale.

Notice that

we increase it,

but we never decrease it.

That is not a mistake.

It is an optimization whose correctness will be proved later.
"""


def longest_repeating_character_replacement(s, k):

    # -------------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------------

    left = 0

    longest_length = 0

    frequency = {}

    maximum_frequency = 0

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
        # Update the largest frequency seen so far.
        # ---------------------------------------------------------------------

        if frequency[current_character] > maximum_frequency:
            maximum_frequency = frequency[current_character]

        # ---------------------------------------------------------------------
        # Check whether the current window requires
        # more than k replacements.
        # ---------------------------------------------------------------------

        current_window_length = right - left + 1

        while (
            current_window_length - maximum_frequency
        ) > k:

            leaving_character = s[left]

            frequency[leaving_character] = (
                frequency[leaving_character] - 1
            )

            if frequency[leaving_character] == 0:
                del frequency[leaving_character]

            left = left + 1

            current_window_length = right - left + 1

        # ---------------------------------------------------------------------
        # The window is considered valid.
        # ---------------------------------------------------------------------

        if current_window_length > longest_length:
            longest_length = current_window_length

    return longest_length


"""
===============================================================================
Example Run
===============================================================================

Input

s = "AABABBA"

k = 1

-------------------------------------------------------------------------------

Output

4

-------------------------------------------------------------------------------

Explanation

One optimal window is

AABA

Frequency

A : 3

B : 1

Replacement Needed

4 - 3 = 1

Therefore,

the answer is

4.

-------------------------------------------------------------------------------

Example

print(longest_repeating_character_replacement("AABABBA", 1))

Output

4
"""


"""
===============================================================================
Step-by-Step Dry Run
===============================================================================

Input

String

AABABBA

k = 1

-------------------------------------------------------------------------------

Initial State

Left = 0

Right = 0

Frequency = {}

Maximum Frequency = 0

Longest Length = 0

-------------------------------------------------------------------------------

Expand

Add

A

Frequency

A : 1

Maximum Frequency

1

Window

A

Length

1

Replacement Needed

1 - 1 = 0

Valid

Longest Length

1

-------------------------------------------------------------------------------

Expand

Add

A

Frequency

A : 2

Maximum Frequency

2

Window

AA

Length

2

Replacement Needed

2 - 2 = 0

Valid

Longest Length

2

-------------------------------------------------------------------------------

Expand

Add

B

Frequency

A : 2

B : 1

Maximum Frequency

2

Window

AAB

Length

3

Replacement Needed

3 - 2 = 1

Valid

Longest Length

3

-------------------------------------------------------------------------------

Expand

Add

A

Frequency

A : 3

B : 1

Maximum Frequency

3

Window

AABA

Length

4

Replacement Needed

4 - 3 = 1

Valid

Longest Length

4

-------------------------------------------------------------------------------

Expand

Add

B

Frequency

A : 3

B : 2

Maximum Frequency

3

Window

AABAB

Length

5

Replacement Needed

5 - 3 = 2

Invalid

Begin shrinking.

-------------------------------------------------------------------------------

Shrink

Remove

A

Frequency

A : 2

B : 2

Left moves forward.

Window

ABAB

Length

4

Maximum Frequency

Still

3

(Stale Value)

Replacement Needed

4 - 3 = 1

Window is now considered valid.

Longest Length

Still

4

-------------------------------------------------------------------------------

Expand

Add

B

Frequency

A : 2

B : 3

Maximum Frequency

3

Window

ABABB

Length

5

Replacement Needed

5 - 3 = 2

Invalid

Shrink Again.

-------------------------------------------------------------------------------

Shrink

Remove

A

Frequency

A : 1

B : 3

Window

BABB

Length

4

Replacement Needed

4 - 3 = 1

Valid

Longest Length

Still

4

-------------------------------------------------------------------------------

The algorithm continues until

the right pointer reaches the end.

Return

4.

-------------------------------------------------------------------------------

Notice something interesting.

When we removed

A,

its frequency decreased.

However,

maximum_frequency

did not decrease.

It remained

3.

This is called

a stale value.

Surprisingly,

the algorithm still produces the correct answer.

The proof of this optimization

is the key idea of this problem.

"""


"""
===============================================================================
Why This Algorithm Works
===============================================================================

The key observation is that

the only character capable of increasing

maximum_frequency

is the

newly added character.

Whenever we expand,

we update

maximum_frequency

if necessary.

However,

when we shrink,

we deliberately do not decrease it.

Why?

Because recomputing the true maximum frequency

would require scanning

the entire frequency map

after every shrink.

That would introduce repeated work.

-------------------------------------------------------------------------------

Instead,

we allow

maximum_frequency

to become stale.

A stale value means

it may be larger than

the true maximum frequency

currently inside the window.

-------------------------------------------------------------------------------

At first,

this seems dangerous.

A stale value can make

Replacement Needed

appear smaller

than it really is.

Consequently,

the algorithm may temporarily treat

an invalid window

as valid.

Why is this still safe?

Because

longest_length

only increases

when the right pointer expands.

Eventually,

either

the window truly becomes valid,

or

future expansions recreate a window

whose real maximum frequency

matches the stale value.

Therefore,

the stale value

may delay shrinking,

but it can never cause

the algorithm to miss

the optimal answer.

The complete correctness proof

formalizes this reasoning.
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

No Duplicate Characters

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

↓

Maximum Frequency

may safely become stale.

------------------------------------------------------------

This is the first Sliding Window problem where

a maintained variable

does not always represent

the exact current window,

yet the algorithm remains correct.

Learning why this works

is more important

than memorizing the code.
"""
"""
===============================================================================
Correctness Proof
===============================================================================

This is one of the most misunderstood Sliding Window algorithms.

Many learners believe

maximum_frequency

must always represent

the exact highest frequency

inside the current window.

Surprisingly,

that is unnecessary.

The algorithm remains correct even when

maximum_frequency

becomes stale.

Understanding why is far more valuable than memorizing the code.

-------------------------------------------------------------------------------

Claim 1

The frequency map always represents

exactly

the characters inside the current window.

-------------------------------------------------------------------------------

Proof

Whenever the right pointer expands,

we increase the frequency of the entering character.

Whenever the left pointer shrinks,

we decrease the frequency of the leaving character.

If a frequency becomes zero,

the key is removed.

Therefore,

after every pointer movement,

the frequency map exactly represents

the current window.

The first invariant always holds.

-------------------------------------------------------------------------------

Claim 2

maximum_frequency

never becomes smaller

than the true maximum frequency

inside the current window.

-------------------------------------------------------------------------------

Proof

maximum_frequency

is updated only when a larger frequency is discovered.

It is never decreased.

Therefore,

it can only be

Equal to

or

Greater than

the actual maximum frequency.

It may become stale,

but it is never an underestimate.

-------------------------------------------------------------------------------

Why is a stale value safe?

Suppose

Current Window

ABAB

Frequency

A : 2

B : 2

Imagine

maximum_frequency

is still

3

from an earlier window.

Our validity check becomes

Window Length

-

3

instead of

Window Length

-

2

This makes the window appear

more valid

than it actually is.

At first,

this seems dangerous.

-------------------------------------------------------------------------------

The Important Observation

A stale value can only

delay shrinking.

It can never force the algorithm

to shrink too early.

Why?

Because the stale value

makes

Replacement Needed

smaller,

never larger.

Therefore,

if an error occurs,

it is always in the direction of

keeping the window larger.

-------------------------------------------------------------------------------

Why doesn't this produce a wrong answer?

Remember

when

longest_length

changes.

It changes only

when the right pointer expands.

Suppose a stale value temporarily allows

a larger invalid window

to survive.

Eventually,

one of two things happens.

-------------------------------------------------------------------------------

Case 1

Future characters increase

the true maximum frequency

until it matches

the stale value.

Now

the window genuinely becomes valid.

The recorded answer is correct.

-------------------------------------------------------------------------------

Case 2

The window continues expanding.

Eventually,

even the stale value

can no longer hide the violation.

The validity condition fails.

The shrinking phase begins.

The oversized window is reduced.

Again,

the algorithm continues correctly.

-------------------------------------------------------------------------------

Therefore,

a stale

maximum_frequency

may postpone shrinking,

but it can never cause the algorithm

to miss the optimal answer

or return a length larger than the true optimum.

-------------------------------------------------------------------------------

Intuition

Think of

maximum_frequency

as

an optimistic estimate.

An optimistic estimate may allow us

to keep exploring

a little longer.

If the optimism eventually becomes false,

the shrinking phase corrects it.

If it becomes true,

then the larger window was actually valid anyway.

Either way,

the final answer remains correct.

-------------------------------------------------------------------------------

Conclusion

The frequency map

always represents

the current window.

The stale

maximum_frequency

never causes premature shrinking.

Any temporary delay in shrinking

is eventually corrected.

Therefore,

the algorithm always returns

the length of the longest valid substring.

===============================================================================
Time Complexity
===============================================================================

Suppose

n

is the length of the string.

-------------------------------------------------------------------------------

Right Pointer

Moves from

left to right

exactly once.

Maximum movements

n

-------------------------------------------------------------------------------

Left Pointer

Also moves

left to right

at most once.

Maximum movements

n

-------------------------------------------------------------------------------

Frequency Map Updates

Each expansion performs

one increment.

Each contraction performs

one decrement.

Each operation takes

constant time.

-------------------------------------------------------------------------------

Overall Time Complexity

O(n)

-------------------------------------------------------------------------------

Why don't we recompute

maximum_frequency

during shrinking?

Because that would require scanning

the frequency map

after every contraction.

Allowing

maximum_frequency

to become stale

eliminates that repeated work

while preserving correctness.

===============================================================================
Space Complexity
===============================================================================

The frequency map stores

the characters currently inside the window.

General Case

O(n)

if every character is different.

-------------------------------------------------------------------------------

Interview Assumption

The input contains

only uppercase English letters.

Maximum possible keys

26

Therefore,

Auxiliary Space

O(1)

under the interview assumption.

===============================================================================
Common Mistakes
===============================================================================

Mistake 1

Recomputing

maximum_frequency

every time

the left pointer moves.

Why it is unnecessary

The stale value optimization

already guarantees correctness.

Recomputing introduces repeated work.

-------------------------------------------------------------------------------

Mistake 2

Trying to decrease

maximum_frequency

when shrinking.

Example

maximum_frequency = 5

One

A

leaves.

Many beginners immediately write

maximum_frequency = 4

This is incorrect.

Another character

might still appear

five times.

The only safe recomputation

would require scanning the entire map,

which we intentionally avoid.

-------------------------------------------------------------------------------

Mistake 3

Thinking

maximum_frequency

must always be exact.

It does not.

It only needs to be

an upper bound

on the true maximum frequency.

-------------------------------------------------------------------------------

Mistake 4

Confusing

Frequency Map

with

Maximum Frequency.

The frequency map

must always be exact.

Only

maximum_frequency

is allowed to become stale.

-------------------------------------------------------------------------------

Mistake 5

Memorizing the formula

Window Length - Maximum Frequency <= k

without understanding

why

it represents the number of replacements needed.

Always remember

we keep

the majority character

and replace

everything else.

===============================================================================
Interview Questions
===============================================================================

Question 1

Why do we subtract

maximum_frequency

from

the window length?

-------------------------------------------------------------------------------

Question 2

Why is

maximum_frequency

never decreased?

-------------------------------------------------------------------------------

Question 3

Can a stale

maximum_frequency

produce an incorrect answer?

Explain why or why not.

-------------------------------------------------------------------------------

Question 4

What repeated work is eliminated

by allowing

maximum_frequency

to become stale?

-------------------------------------------------------------------------------

Question 5

How does this problem differ from

Longest Substring Without Repeating Characters?

Expected Answer

Both use

Expand → Shrink.

Both maintain

a frequency map.

The new idea is

maintaining

maximum_frequency

and allowing it to become stale.

===============================================================================
Revision Problems
===============================================================================

Easy

1.

Implement

Longest Repeating Character Replacement

from memory.

------------------------------------------------------------

2.

Modify the solution

to return

the actual substring

instead of only its length.

-------------------------------------------------------------------------------

Medium

1.

Longest Substring with At Most K Distinct Characters

Introduces

Distinct Count

instead of

Maximum Frequency.

------------------------------------------------------------

2.

Fruits Into Baskets

Same maintained state,

different story.

-------------------------------------------------------------------------------

Hard

1.

Minimum Window Substring

The final representative problem

of the Variable Window chapter.

Introduces

Need

Have

Required

Satisfied

and combines everything learned so far.

===============================================================================
Pattern Evolution
===============================================================================

Minimum Size Subarray Sum

↓

Running Sum

↓

Validity

Running Sum >= Target

------------------------------------------------------------

Longest Unique Substring

↓

Frequency Map

↓

Validity

No Duplicate Characters

------------------------------------------------------------

Character Replacement

↓

Frequency Map

+

Maximum Frequency

↓

Validity

Window Length - Maximum Frequency <= k

↓

Stale Information

can still be correct.

------------------------------------------------------------

Each representative problem

adds exactly one new idea

while preserving

the same

Expand → Shrink

framework.

===============================================================================
One-Line Memory Hook
===============================================================================

"Keep the majority character,
replace the minority characters,
and remember:
a stale maximum frequency may delay shrinking,
but it never changes the correct answer."
"""

