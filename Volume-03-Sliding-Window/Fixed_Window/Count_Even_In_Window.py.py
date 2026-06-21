"""
===============================================================================
Problem: Count Even Numbers in Every Window of Size K
Pattern: Fixed Sliding Window
Representative Problem of the Fixed Window Variation
===============================================================================

Problem Statement
-----------------

Given an array of integers and an integer k,

return the number of even elements present in every contiguous
subarray (window) of size exactly k.

Example

Input

nums = [2, 5, 6, 8, 1, 4]

k = 3

Windows

[2,5,6] -> 2 even numbers

[5,6,8] -> 2 even numbers

[6,8,1] -> 2 even numbers

[8,1,4] -> 2 even numbers

Output

[2,2,2,2]

-------------------------------------------------------------------------------

Why is this problem important?

At first glance,

this looks completely different from

Maximum Sum of K Elements.

However,

the underlying algorithm is identical.

The only thing that changes is

the maintained state.

Instead of maintaining

Running Sum,

we now maintain

Running Even Count.

This is the first problem that teaches us that

Sliding Window algorithms are built around

maintained state,

not around specific formulas.
"""

"""
===============================================================================
Brute Force
===============================================================================

Suppose we have never heard of Sliding Window.

How would we solve the problem?

For every possible window,

visit every element.

Count how many of them are even.

Store the answer.

Move to the next window.

Repeat.

-------------------------------------------------------------------------------

Example

Window

2 5 6

Even Count

2

------------------------------------------------------------

Window

5 6 8

Even Count

2

------------------------------------------------------------

Window

6 8 1

Even Count

2

------------------------------------------------------------

Window

8 1 4

Even Count

2

------------------------------------------------------------

This algorithm is correct.

But it repeatedly checks

the same elements

again and again.

The repeated work is hidden inside the counting process.
"""

"""
===============================================================================
Observation
===============================================================================

Compare two consecutive windows.

Window

2 5 6

↓

Window

5 6 8

Ask yourself

What actually changed?

Only two numbers.

2

left.

8

entered.

The element

5

was already checked.

The element

6

was already checked.

Why should we test

5

and

6

again?

Nothing about them changed.

Only one piece of information expired.

Only one new piece of information became available.

Everything else remains valid.

This is exactly the same observation we made while solving

Maximum Sum of K Elements.

The only difference is

what

we are maintaining.
"""

"""
===============================================================================
Optimization Journey
===============================================================================

Stage 1

Treat every window independently.

↓

Visit every element again.

↓

Repeated work

------------------------------------------------------------

Stage 2

Notice

neighboring windows overlap.

Only

one element leaves

and

one element enters.

------------------------------------------------------------

Stage 3

Instead of recounting every even number,

maintain

the number of even elements currently inside the window.

------------------------------------------------------------

Stage 4

Whenever the window moves,

update only the two elements that changed.

Leaving Element

↓

If it is even,

decrease the count.

------------------------------------------------------------

Entering Element

↓

If it is even,

increase the count.

------------------------------------------------------------

Everything else remains unchanged.

This transforms

O(n × k)

into

O(n).

The optimization once again comes from

preserving useful information.
"""

"""
===============================================================================
Repeated Work Being Eliminated
===============================================================================

Suppose

Current Window

2 5 6

Even Count

2

Now the next window becomes

5 6 8

The brute-force algorithm would again ask

Is 5 even?

No.

------------------------------------------------------------

Is 6 even?

Yes.

------------------------------------------------------------

Is 8 even?

Yes.

But notice something.

We already knew

5

and

6

from the previous window.

The only new question we actually need to answer is

Is the entering element even?

Similarly,

the only old information that might become invalid is

whether the leaving element contributed to the count.

Everything else can simply be carried forward.

This is the repeated work we eliminate.
"""

"""
===============================================================================
Maintained State
===============================================================================

In the previous representative problem,

our maintained state was

Running Sum.

For this problem,

we no longer care about the sum.

Instead,

we maintain

current_even_count

This variable always stores

the number of even elements

inside the current window.

Nothing else needs to be remembered.

Notice how the algorithm stayed exactly the same.

Only the maintained state changed.

This is one of the biggest ideas in Sliding Window.

The pattern stays.

The information changes.
"""

"""
===============================================================================
Core Invariant
===============================================================================

Throughout the entire algorithm,

current_even_count

must always equal

the number of even elements

inside the current window.

This invariant must never become false.

Whenever the window moves,

the maintained state must immediately be updated

so that it once again represents

exactly

the current window.

If this invariant breaks,

every future answer becomes incorrect.
"""

"""
===============================================================================
Pointer / Variable Responsibilities
===============================================================================

Left Side Responsibility

The left side removes expired information.

If the leaving element is even,

it contributed

1

to the current count.

That contribution must now be removed.

If the leaving element is odd,

it never contributed anything.

Nothing changes.

------------------------------------------------------------

Right Side Responsibility

The right side introduces new information.

If the entering element is even,

it contributes

1

to the maintained count.

If it is odd,

nothing changes.

------------------------------------------------------------

current_even_count Responsibility

Always represent

the number of even elements

inside

the current window.

Never the previous window.

Never the next window.

Only

the current window.

------------------------------------------------------------

result Responsibility

Store the answer

for every window

in the order in which the windows are processed.
"""

"""
===============================================================================
Algorithm (Reasoning Only)
===============================================================================

Step 1

Build the first complete window.

Count how many even numbers it contains.

------------------------------------------------------------

Step 2

Store this count as the answer for the first window.

------------------------------------------------------------

Step 3

Slide the window.

------------------------------------------------------------

Step 4

If the leaving element is even,

decrease

current_even_count.

------------------------------------------------------------

Step 5

If the entering element is even,

increase

current_even_count.

------------------------------------------------------------

Step 6

Store the updated count.

------------------------------------------------------------

Step 7

Repeat until every window has been processed.

Notice something remarkable.

The algorithm is almost identical to

Maximum Sum of K Elements.

The only difference is

the maintained state.

This is the essence of the Fixed Sliding Window variation.
"""

"""
===============================================================================
Runnable Python Code
===============================================================================

The implementation below follows exactly the reasoning developed earlier.

Compare it with the implementation of

Maximum_Sum_of_K.py

You will notice something remarkable.

Almost every line is identical.

The only thing that changes is the maintained state.

Instead of maintaining

current_sum

we now maintain

current_even_count.

This demonstrates one of the most important lessons of the Fixed Window
variation.

The algorithm remains the same.

Only the maintained state changes.
"""


def count_even_numbers_in_every_window(nums, k):

    # Edge Case
    if len(nums) < k:
        return []

    result = []

    # -----------------------------------------------------------------
    # Build the first complete window
    # -----------------------------------------------------------------

    current_even_count = 0

    for index in range(k):

        if nums[index] % 2 == 0:
            current_even_count = current_even_count + 1

    result.append(current_even_count)

    # -----------------------------------------------------------------
    # Slide the window
    # -----------------------------------------------------------------

    for right in range(k, len(nums)):

        left = right - k

        # Remove the leaving element's contribution

        if nums[left] % 2 == 0:
            current_even_count = current_even_count - 1

        # Add the entering element's contribution

        if nums[right] % 2 == 0:
            current_even_count = current_even_count + 1

        result.append(current_even_count)

    return result


"""
===============================================================================
Example Run
===============================================================================

Input

nums = [2, 5, 6, 8, 1, 4]

k = 3

Output

[2, 2, 2, 2]

-------------------------------------------------------------------------------

Example

nums = [2, 5, 6, 8, 1, 4]

k = 3

print(count_even_numbers_in_every_window(nums, k))

Output

[2, 2, 2, 2]
"""


"""
===============================================================================
Step-by-Step Dry Run
===============================================================================

Array

2 5 6 8 1 4

Window Size

3

-------------------------------------------------------------------------------

Step 1

Build the first window.

Window

2 5 6

Even Elements

2

6

current_even_count

=

2

Store

2

Result

[2]

-------------------------------------------------------------------------------

Slide Window

Old Window

2 5 6

↓

New Window

5 6 8

Leaving Element

2

Entering Element

8

2 is even

↓

Decrease count

2 → 1

8 is even

↓

Increase count

1 → 2

Store

2

Result

[2, 2]

-------------------------------------------------------------------------------

Slide Again

Old Window

5 6 8

↓

New Window

6 8 1

Leaving Element

5

Entering Element

1

5 is odd

↓

No change

1 is odd

↓

No change

current_even_count

=

2

Store

2

Result

[2, 2, 2]

-------------------------------------------------------------------------------

Slide Again

Old Window

6 8 1

↓

New Window

8 1 4

Leaving Element

6

Entering Element

4

6 is even

↓

Decrease

2 → 1

4 is even

↓

Increase

1 → 2

Store

2

Final Result

[2, 2, 2, 2]
"""


"""
===============================================================================
Why This Algorithm Works
===============================================================================

The algorithm works because the parity (even or odd nature) of every element
is fixed.

Once we know whether an element contributes to the current window,

its contribution never changes while it remains inside the window.

When the window slides,

only two elements can affect the maintained state.

1.

The element leaving the window.

2.

The element entering the window.

Every other element remains inside the window.

Their contribution is already known and remains unchanged.

Therefore,

there is no need to inspect every element again.

Instead,

we simply update the maintained count.

-------------------------------------------------------------------------------

Think about the maintained state.

It answers only one question.

"How many even numbers are currently inside this window?"

Whenever the window moves,

we update only the information that changed.

This is exactly the same philosophy used in

Maximum Sum of K Elements.

The maintained state changed.

The Sliding Window pattern did not.

"""


"""
===============================================================================
Pattern Evolution
===============================================================================

Brute Force

↓

Visit every element in every window.

↓

Repeated Work

↓

Rechecking the same elements.

↓

Observation

↓

Neighboring windows overlap.

↓

Maintained State

↓

Running Even Count

↓

Invariant

↓

current_even_count always represents

the current window.

↓

Local Updates

↓

Remove Leaving Contribution

↓

Add Entering Contribution

↓

Linear-Time Algorithm

-------------------------------------------------------------------------------

Compare this evolution with

Maximum Sum of K Elements.

Only one box changes.

Running Sum

↓

Running Even Count

Everything else remains identical.

This is exactly how you should begin recognizing patterns.

Do not memorize problems.

Recognize

what information needs to be maintained.
"""

"""
===============================================================================
Correctness Proof
===============================================================================

A good algorithm is not only one that produces the correct answer.

It should also be possible to explain why it is correct for every valid input.

For this problem, the proof is based on maintaining an invariant throughout
the execution of the algorithm.

-------------------------------------------------------------------------------

Claim

At every stage of the algorithm,

current_even_count

is exactly equal to the number of even elements inside the current window.

-------------------------------------------------------------------------------

Proof

Base Case

Before the sliding process begins,

we build the first complete window.

While building this window,

we inspect every element exactly once.

For every even element,

we increase

current_even_count.

Therefore,

after building the first window,

current_even_count

correctly represents the number of even elements in that window.

Hence,

the invariant is true before the sliding process begins.

-------------------------------------------------------------------------------

Induction Step

Assume that before sliding,

current_even_count

correctly represents the current window.

Now the window moves by one position.

Exactly one element leaves the window.

Exactly one element enters the window.

There are four possible situations.

-------------------------------------------------------------------------------

Case 1

Leaving Element → Odd

Entering Element → Odd

Neither element contributes to the even count.

Therefore,

current_even_count

does not change.

The invariant remains true.

-------------------------------------------------------------------------------

Case 2

Leaving Element → Even

Entering Element → Odd

The leaving element contributed

1

to the count.

The entering element contributes

0.

Therefore,

we decrease

current_even_count

by

1.

The invariant remains true.

-------------------------------------------------------------------------------

Case 3

Leaving Element → Odd

Entering Element → Even

The leaving element contributed

0.

The entering element contributes

1.

Therefore,

we increase

current_even_count

by

1.

The invariant remains true.

-------------------------------------------------------------------------------

Case 4

Leaving Element → Even

Entering Element → Even

The leaving element contributed

1.

The entering element also contributes

1.

We remove one contribution

and

add one contribution.

The total count remains unchanged.

The invariant still holds.

-------------------------------------------------------------------------------

Conclusion

Every possible window movement falls into one of these four cases.

In every case,

the maintained state remains synchronized with the current window.

Therefore,

the algorithm correctly computes the number of even elements for every
window.

===============================================================================
Time Complexity
===============================================================================

Suppose

n = number of elements

k = window size

-------------------------------------------------------------------------------

Building the first window

requires

k

operations.

Time

O(k)

-------------------------------------------------------------------------------

Sliding the window

The window moves

n - k

times.

Each movement performs only

• One parity check for the leaving element.

• One parity check for the entering element.

• At most one decrement.

• At most one increment.

These are all constant-time operations.

Time

O(n - k)

-------------------------------------------------------------------------------

Overall Time Complexity

O(k) + O(n - k)

=

O(n)

-------------------------------------------------------------------------------

Intuition

Every element is examined only when it enters the window and when it leaves.

No window is scanned from scratch.

===============================================================================
Space Complexity
===============================================================================

Extra variables

current_even_count

left

right

result list

Ignoring the output array,

the algorithm uses only constant extra memory.

Auxiliary Space

O(1)

If the output list is included,

its size equals the number of windows,

which is

n - k + 1.

Output Space

O(n - k + 1)

===============================================================================
Common Mistakes
===============================================================================

Mistake 1

Recounting every window.

Wrong

Visit all k elements for every window.

Why it is wrong

The entire purpose of the Fixed Window pattern is to avoid rebuilding
information.

-------------------------------------------------------------------------------

Mistake 2

Checking every element again after sliding.

Only two elements changed.

Checking the remaining elements is repeated work.

-------------------------------------------------------------------------------

Mistake 3

Always decrementing when the window moves.

Remember,

the leaving element should reduce the count

only if it is even.

Otherwise,

the maintained state becomes incorrect.

-------------------------------------------------------------------------------

Mistake 4

Always incrementing the entering element.

Again,

only even elements contribute.

Odd elements should not change the maintained state.

-------------------------------------------------------------------------------

Mistake 5

Building the first answer incorrectly.

Always finish constructing the first complete window

before beginning the sliding process.

===============================================================================
Interview Questions
===============================================================================

Question 1

Why is this algorithm O(n) instead of O(n × k)?

-------------------------------------------------------------------------------

Question 2

What repeated work is eliminated?

-------------------------------------------------------------------------------

Question 3

Why is maintaining only the even count sufficient?

Why don't we need to remember every even element individually?

-------------------------------------------------------------------------------

Question 4

Suppose the problem changes to

"Count odd numbers in every window."

What changes?

Expected Answer

Only the maintained state update condition changes.

The Sliding Window algorithm remains identical.

-------------------------------------------------------------------------------

Question 5

Suppose the problem changes to

"Count numbers divisible by 3."

Would the algorithm change?

Expected Answer

No.

Only the contribution rule changes.

The pattern remains exactly the same.

===============================================================================
Revision Problems
===============================================================================

Easy

1.

Count Odd Numbers in Every Window of Size K

(Maintained State

Running Odd Count)

------------------------------------------------------------

2.

Count Positive Numbers in Every Window of Size K

(Maintained State

Running Positive Count)

-------------------------------------------------------------------------------

Medium

1.

Maximum Number of Vowels in a Substring of Length K

(Maintained State

Running Vowel Count)

------------------------------------------------------------

2.

Count Distinct Elements in Every Window of Size K

(Maintained State

Frequency Map + Distinct Count)

-------------------------------------------------------------------------------

Hard (Relative to This Variation)

1.

Permutation in String

(Maintained State

Frequency Map)

Notice how the maintained state evolves

from

a single integer

to

an entire data structure.

===============================================================================
Pattern Evolution
===============================================================================

Maximum Sum of K Elements

↓

Maintained State

Running Sum

↓

Count Even Numbers in Every Window

↓

Maintained State

Running Even Count

↓

Permutation in String

↓

Maintained State

Frequency Map

-------------------------------------------------------------------------------

Notice the progression.

The Sliding Window framework never changes.

Only the maintained state becomes richer.

Learning these representative problems in this order helps you understand
that the pattern is reusable regardless of what information is being
maintained.

===============================================================================
One-Line Memory Hook
===============================================================================

"A Fixed Window algorithm succeeds by maintaining exactly the information the
problem asks for—and updating only the part that changes."
"""

