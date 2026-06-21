"""
===============================================================================
Problem: Minimum Size Subarray Sum
Pattern: Variable Sliding Window
Representative Problem of the Variable Window Variation
===============================================================================

Problem Statement
-----------------

Given an array of positive integers

nums

and an integer

target,

return the length of the smallest contiguous subarray whose sum is
greater than or equal to

target.

If no such subarray exists,

return

0.

-------------------------------------------------------------------------------

Example

Input

target = 7

nums = [2, 3, 1, 2, 4, 3]

Output

2

Explanation

The subarray

[4, 3]

has a sum of

7

and is the smallest valid subarray.

-------------------------------------------------------------------------------

Why is this problem important?

This is the first representative problem of the

Variable Sliding Window

pattern.

Unlike Fixed Window,

the correct window size is unknown.

The algorithm must discover it while scanning the array.

This problem introduces

Expand

↓

Become Valid

↓

Shrink

↓

Become Invalid

↓

Expand Again

This cycle is the foundation of almost every Variable Sliding Window problem.

"""

"""
===============================================================================
Brute Force
===============================================================================

Suppose we know nothing about Sliding Window.

How would we naturally solve this problem?

Choose every possible starting position.

For every starting position,

extend the subarray one element at a time.

Compute its sum.

As soon as the sum becomes

greater than or equal to

the target,

record its length.

Repeat this process for every possible starting position.

Finally,

return the smallest length found.

-------------------------------------------------------------------------------

Example

nums

2 3 1 2 4 3

Target

7

Starting from index

0

2

↓

2 + 3

↓

2 + 3 + 1

↓

2 + 3 + 1 + 2

Now

Sum = 8

Length = 4

Store

4

-------------------------------------------------------------------------------

Start from index

1

3

↓

3 + 1

↓

3 + 1 + 2

↓

3 + 1 + 2 + 4

Length = 4

-------------------------------------------------------------------------------

Eventually

we discover

4 + 3

Length = 2

-------------------------------------------------------------------------------

This algorithm is correct.

However,

it repeatedly computes sums

for heavily overlapping subarrays.

That repeated work is what we want to eliminate.

"""

"""
===============================================================================
Observation
===============================================================================

Instead of looking at

every subarray,

look at

how neighboring subarrays are related.

Suppose our current window is

2 3 1 2

Running Sum

8

The target is

7.

The current window is already valid.

Now ask yourself

"What is the real objective?"

Not simply

to find

a valid window.

We already have one.

The real objective is

to find

the smallest

valid window.

That changes everything.

Instead of expanding further,

we should ask

"Can I remove something from the left

and still remain valid?"

If the answer is

Yes,

our previous window was larger than necessary.

This observation gives birth to the

shrink phase.

"""

"""
===============================================================================
Optimization Journey
===============================================================================

Stage 1

Treat every starting position independently.

↓

Repeatedly compute overlapping sums.

↓

O(n²)

-------------------------------------------------------------------------------

Stage 2

Notice that neighboring subarrays share almost all of their elements.

Instead of restarting,

carry the current window forward.

-------------------------------------------------------------------------------

Stage 3

Maintain

the running sum

of the current window.

-------------------------------------------------------------------------------

Stage 4

Keep expanding

until the window becomes valid.

Running Sum

>=

Target

-------------------------------------------------------------------------------

Stage 5

Once valid,

change your objective.

Instead of collecting more elements,

try removing unnecessary ones.

Shrink the window

while it remains valid.

-------------------------------------------------------------------------------

Stage 6

Eventually,

the window becomes invalid again.

Now shrinking no longer helps.

Return to expansion.

-------------------------------------------------------------------------------

This repeating

Expand

↓

Shrink

cycle

is the defining characteristic of the Variable Window pattern.

"""

"""
===============================================================================
Repeated Work Being Eliminated
===============================================================================

Consider the array

2 3 1 2 4 3

Suppose our current window is

2 3 1 2

Running Sum

8

Now compare two approaches.

-------------------------------------------------------------------------------

Brute Force

Start over.

Recompute

3 + 1 + 2

again.

-------------------------------------------------------------------------------

Sliding Window

We already know

Running Sum = 8

Simply remove

2.

New Running Sum

6

No recomputation.

-------------------------------------------------------------------------------

If the window later expands,

we simply

add

the new element.

Every update becomes local.

Instead of rebuilding

the answer,

we transform

the previous answer

into

the next answer.

"""

"""
===============================================================================
Maintained State
===============================================================================

Every Variable Window problem maintains information.

For this problem,

the maintained state is extremely simple.

Running Sum

This variable always stores

the sum

of the current window.

Nothing more.

Nothing less.

Unlike Fixed Window,

the maintained state now serves

two purposes.

Purpose 1

Represent the current window.

Purpose 2

Tell us whether

the current window is valid.

The maintained state has become

both

a description

and

a decision-making tool.

"""

"""
===============================================================================
Core Invariant
===============================================================================

Throughout the algorithm,

Running Sum

must always equal

the sum

of the current window.

This statement must remain true

after every expansion

and

after every contraction.

If this invariant breaks,

the validity check

Running Sum >= Target

also becomes incorrect.

The invariant is therefore responsible for

every future decision made by the algorithm.

"""

"""
===============================================================================
Pointer Responsibilities
===============================================================================

Right Pointer

Responsible for

collecting more information.

Every movement expands the window.

Every movement increases the amount of information available.

Its goal is

to make the current window valid.

-------------------------------------------------------------------------------

Left Pointer

Responsible for

removing unnecessary information.

Once the window is already valid,

its job is to determine

whether the same condition can still be satisfied

using a smaller window.

-------------------------------------------------------------------------------

Running Sum

Always represents

the current window.

It must immediately reflect

every expansion

and

every contraction.

-------------------------------------------------------------------------------

Best Answer

Stores

the smallest valid window

found so far.

Unlike

Running Sum,

this variable is never reset.

It only improves

whenever a smaller valid window is discovered.

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

by moving the right pointer.

Update

Running Sum.

-------------------------------------------------------------------------------

Step 3

Check the validity condition.

Is

Running Sum

greater than or equal to

Target?

-------------------------------------------------------------------------------

If No

Continue expanding.

-------------------------------------------------------------------------------

If Yes

A valid window has been found.

Record its length.

-------------------------------------------------------------------------------

Step 4

Shrink the window

by moving the left pointer.

Update

Running Sum.

-------------------------------------------------------------------------------

Step 5

Check validity again.

If the window is still valid,

record the new,

smaller length

and continue shrinking.

-------------------------------------------------------------------------------

Step 6

Eventually,

the window becomes invalid.

Stop shrinking.

Return to expansion.

-------------------------------------------------------------------------------

Repeat until

the right pointer reaches

the end of the array.

Notice the difference from Fixed Window.

There,

both pointers moved together.

Here,

each pointer moves

only when its responsibility demands it.

That independence is what allows the algorithm to discover

the optimal window size.

"""

"""
===============================================================================
Runnable Python Code
===============================================================================

The implementation below follows exactly the reasoning developed earlier.

Notice something important.

Unlike the Fixed Window variation,

the left pointer does not move every time the right pointer moves.

The right pointer expands the window until it becomes valid.

Only then does the left pointer begin shrinking the window.

The window size is therefore discovered during the algorithm instead of
being known beforehand.
"""


def minimum_size_subarray_sum(target, nums):

    # -------------------------------------------------------------------------
    # Edge Case
    # -------------------------------------------------------------------------

    if len(nums) == 0:
        return 0

    # -------------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------------

    left = 0

    current_sum = 0

    minimum_length = float("inf")

    # -------------------------------------------------------------------------
    # Expand the window
    # -------------------------------------------------------------------------

    for right in range(len(nums)):

        current_sum = current_sum + nums[right]

        # ---------------------------------------------------------------------
        # The current window is valid.
        # Try to make it smaller while preserving validity.
        # ---------------------------------------------------------------------

        while current_sum >= target:

            current_window_length = right - left + 1

            if current_window_length < minimum_length:
                minimum_length = current_window_length

            current_sum = current_sum - nums[left]

            left = left + 1

    # -------------------------------------------------------------------------
    # No valid window found
    # -------------------------------------------------------------------------

    if minimum_length == float("inf"):
        return 0

    return minimum_length


"""
===============================================================================
Example Run
===============================================================================

Input

target = 7

nums = [2, 3, 1, 2, 4, 3]

-------------------------------------------------------------------------------

Output

2

-------------------------------------------------------------------------------

Explanation

The smallest subarray whose sum is at least

7

is

[4, 3]

whose length is

2.

-------------------------------------------------------------------------------

Example

target = 7

nums = [2, 3, 1, 2, 4, 3]

print(minimum_size_subarray_sum(target, nums))

Output

2
"""


"""
===============================================================================
Step-by-Step Dry Run
===============================================================================

Input

Target

7

Array

2 3 1 2 4 3

-------------------------------------------------------------------------------

Initial State

Left = 0

Right = 0

Running Sum = 0

Minimum Length = Infinity

-------------------------------------------------------------------------------

Expand

Add

2

Running Sum

2

Valid?

No

Continue expanding.

-------------------------------------------------------------------------------

Expand

Add

3

Running Sum

5

Valid?

No

Continue expanding.

-------------------------------------------------------------------------------

Expand

Add

1

Running Sum

6

Valid?

No

Continue expanding.

-------------------------------------------------------------------------------

Expand

Add

2

Running Sum

8

Valid?

Yes

Current Window

[2, 3, 1, 2]

Length

4

Minimum Length

4

-------------------------------------------------------------------------------

Shrink

Remove

2

Running Sum

6

Move Left

Window becomes invalid.

Stop shrinking.

-------------------------------------------------------------------------------

Expand

Add

4

Running Sum

10

Window

[3, 1, 2, 4]

Length

4

Minimum Length

still

4

-------------------------------------------------------------------------------

Shrink

Remove

3

Running Sum

7

Still Valid

Window

[1, 2, 4]

Length

3

Update

Minimum Length

3

-------------------------------------------------------------------------------

Shrink Again

Remove

1

Running Sum

6

Window becomes invalid.

Stop shrinking.

-------------------------------------------------------------------------------

Expand

Add

3

Running Sum

9

Window

[2, 4, 3]

Length

3

Minimum Length

3

-------------------------------------------------------------------------------

Shrink

Remove

2

Running Sum

7

Still Valid

Window

[4, 3]

Length

2

Update

Minimum Length

2

-------------------------------------------------------------------------------

Shrink Again

Remove

4

Running Sum

3

Window becomes invalid.

Stop shrinking.

-------------------------------------------------------------------------------

The right pointer has reached the end.

Return

2

-------------------------------------------------------------------------------

Notice the rhythm.

Expand

↓

Become Valid

↓

Shrink

↓

Become Invalid

↓

Expand Again

This rhythm appears in almost every Variable Window problem.
"""


"""
===============================================================================
Why This Algorithm Works
===============================================================================

The algorithm works because of two important observations.

-------------------------------------------------------------------------------

Observation 1

If the current window is invalid,

removing elements cannot make it valid.

Suppose

Running Sum

is

5

while the target is

7.

Removing elements will only decrease the sum further.

Therefore,

the only useful action is

to expand the window.

-------------------------------------------------------------------------------

Observation 2

Once the window becomes valid,

expanding it further cannot help us find a smaller answer.

Suppose

Running Sum

is already

10

while the target is

7.

The current window satisfies the condition.

Adding more elements only makes the window larger.

Since we want

the smallest

valid window,

the only useful action is

to shrink it.

-------------------------------------------------------------------------------

These two observations completely determine pointer movement.

Invalid Window

↓

Expand

Valid Window

↓

Shrink

-------------------------------------------------------------------------------

Think about the maintained state.

The Running Sum tells us

whether the current window is valid.

That single piece of information determines

every future movement of both pointers.

The algorithm never asks

"Which pointer should move?"

Instead,

it asks

"Is the current window valid?"

The answer naturally determines

the next action.

"""

"""
===============================================================================
Pattern Evolution
===============================================================================

Fixed Window

↓

Window Size

Known

↓

Pointers move together.

↓

Maintain Window State.

------------------------------------------------------------

Variable Window

↓

Window Size

Unknown

↓

Pointers move independently.

↓

Maintain Window State

+

Maintain Window Validity.

------------------------------------------------------------

This is the first representative problem where

validity

becomes more important than

window size.

That idea will remain central throughout the rest of the Variable Window
chapter.
"""
"""
===============================================================================
Correctness Proof
===============================================================================

A correct algorithm is not one that merely works on a few examples.

We should be able to explain why it works for every valid input.

For this problem, the proof is based on maintaining an invariant throughout
the algorithm.

-------------------------------------------------------------------------------

Claim

At every point during the algorithm,

current_sum

is exactly equal to the sum of the elements inside the current window

nums[left ... right].

-------------------------------------------------------------------------------

Base Case

Initially,

the window is empty.

left = 0

right has not processed any element.

current_sum = 0

Therefore,

current_sum

correctly represents the empty window.

The invariant is true before the algorithm begins.

-------------------------------------------------------------------------------

Induction Step

Assume

before an iteration,

current_sum

correctly represents

nums[left ... right].

There are only two possible operations.

-------------------------------------------------------------------------------

Operation 1

Expand

The right pointer moves forward.

A new element enters the window.

The algorithm performs

current_sum = current_sum + nums[right]

Now

current_sum

again equals the sum of every element currently inside the window.

The invariant remains true.

-------------------------------------------------------------------------------

Operation 2

Shrink

The left pointer moves forward.

One element leaves the window.

The algorithm performs

current_sum = current_sum - nums[left]

before moving

left.

Again,

current_sum

now equals the sum of the new window.

The invariant remains true.

-------------------------------------------------------------------------------

Therefore,

after every expansion

and

after every contraction,

the invariant continues to hold.

-------------------------------------------------------------------------------

Why does shrinking produce the optimal answer?

Suppose the current window is valid.

Running Sum

>=

Target

If we keep expanding,

the window only becomes larger.

A larger window can never improve the answer because we are searching for
the

smallest

valid window.

Therefore,

once a valid window is found,

the only meaningful action is to remove unnecessary elements from the left.

The first moment the window becomes invalid,

we know that the previous window was the smallest valid window ending at
that right pointer.

Recording every such candidate guarantees that the global minimum will be
found.

-------------------------------------------------------------------------------

Conclusion

The invariant is true initially.

It remains true after every pointer movement.

Every valid window is examined.

Every smallest valid window ending at each right position is considered.

Therefore,

the algorithm always returns the length of the smallest valid subarray.

===============================================================================
Time Complexity
===============================================================================

Suppose

n

is the length of the array.

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

Moves to the end at most once.

Maximum movements

n

-------------------------------------------------------------------------------

Although there is a

while

loop inside the

for

loop,

the total number of left pointer movements over the entire algorithm is at
most

n.

Therefore,

Total Time Complexity

O(n)

-------------------------------------------------------------------------------

Intuition

Every element

enters the window once

and

leaves the window once.

No element is processed repeatedly.

===============================================================================
Space Complexity
===============================================================================

Extra Variables

left

right

current_sum

minimum_length

No additional data structure grows with the input size.

Therefore,

Space Complexity

O(1)

===============================================================================
Common Mistakes
===============================================================================

Mistake 1

Trying to decide the window size beforehand.

This immediately turns the problem back into a Fixed Window problem,

which cannot solve this question correctly.

-------------------------------------------------------------------------------

Mistake 2

Shrinking before the window becomes valid.

Suppose

Running Sum

is

5

and

Target

is

7.

Removing elements only decreases the sum further.

Shrinking is meaningless until the window first satisfies the condition.

-------------------------------------------------------------------------------

Mistake 3

Recording the answer only once.

Suppose the window is valid.

You should continue shrinking

while it remains valid.

A smaller valid window may still exist.

-------------------------------------------------------------------------------

Mistake 4

Forgetting to subtract the leaving element.

Then

current_sum

no longer represents the current window.

The invariant immediately breaks.

-------------------------------------------------------------------------------

Mistake 5

Using

if

instead of

while

for shrinking.

Wrong

if current_sum >= target:

Correct

while current_sum >= target:

Why?

Because multiple unnecessary elements may exist at the beginning of the
window.

We should remove all of them until the window becomes invalid.

===============================================================================
Interview Questions
===============================================================================

Question 1

Why does the right pointer never move backward?

-------------------------------------------------------------------------------

Question 2

Why is

while

necessary instead of

if

during shrinking?

-------------------------------------------------------------------------------

Question 3

Why can we safely stop shrinking as soon as the window becomes invalid?

-------------------------------------------------------------------------------

Question 4

How is this problem fundamentally different from

Maximum Sum of K Elements?

Expected Answer

Maximum Sum has a fixed window size.

This problem has an unknown window size that must be discovered.

-------------------------------------------------------------------------------

Question 5

Suppose the array contains negative numbers.

Would this algorithm still work?

Expected Answer

No.

The algorithm relies on the fact that adding a new positive element never
decreases the running sum.

With negative numbers,

expanding the window could actually decrease the sum,

breaking the reasoning behind the expand-shrink strategy.

===============================================================================
Revision Problems
===============================================================================

Easy

1.

Minimum Size Subarray Sum

(Implement from memory.)

------------------------------------------------------------

2.

Smallest Subarray with Sum Greater Than X

(Same pattern.)

-------------------------------------------------------------------------------

Medium

1.

Longest Substring Without Repeating Characters

New Maintained State

Frequency Map

------------------------------------------------------------

2.

Longest Repeating Character Replacement

New Maintained State

Frequency Map

+

Maximum Frequency

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

concepts.

===============================================================================
Pattern Evolution
===============================================================================

Fixed Window

↓

Known Window Size

↓

Maintain State

↓

Slide Together

------------------------------------------------------------

Minimum Size Subarray Sum

↓

Unknown Window Size

↓

Maintain Running Sum

↓

Validity Condition

Running Sum >= Target

↓

Expand Until Valid

↓

Shrink While Valid

------------------------------------------------------------

This problem introduces the most important rhythm of the Variable Window
pattern.

Expand

↓

Become Valid

↓

Shrink

↓

Become Invalid

↓

Expand Again

Every remaining Variable Window problem is a variation of this same cycle.

===============================================================================
One-Line Memory Hook
===============================================================================

"A Variable Window grows until it satisfies the condition, then shrinks until
it almost breaks it. The boundary between valid and invalid is where the
optimal answer is discovered."
"""
