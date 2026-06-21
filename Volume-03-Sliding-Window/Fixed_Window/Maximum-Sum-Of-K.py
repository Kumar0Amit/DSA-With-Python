"""
===============================================================================
Problem: Maximum Sum of K Consecutive Elements
Pattern: Fixed Sliding Window
Representative Problem of the Fixed Window Variation
===============================================================================

Problem Statement
-----------------

Given an array of integers and an integer k,
find the maximum sum among all contiguous subarrays
(window) of size exactly k.

Example

Input

nums = [2, 1, 5, 1, 3, 2]
k = 3

Possible Windows

[2,1,5] -> 8

[1,5,1] -> 7

[5,1,3] -> 9

[1,3,2] -> 6

Output

9

-------------------------------------------------------------------------------

Why is this problem important?

This is one of the first problems that naturally leads us to discover the
Fixed Sliding Window pattern.

The objective is NOT to memorize this solution.

The objective is to understand WHY rebuilding every window is unnecessary
and HOW carrying information forward eliminates repeated work.

This problem teaches the DNA of every Fixed Window algorithm.
"""

"""
===============================================================================
Brute Force Thinking
===============================================================================

Whenever learning a new pattern, always begin with the simplest correct solution.

Imagine we know nothing about Sliding Window.

What would we naturally do?

For every possible window,

compute its sum independently.

Window 1

2 1 5

Compute

2 + 1 + 5

----------------------------

Window 2

1 5 1

Compute

1 + 5 + 1

----------------------------

Window 3

5 1 3

Compute

5 + 1 + 3

----------------------------

Window 4

1 3 2

Compute

1 + 3 + 2

----------------------------

This solution is perfectly correct.

However,

notice something.

Every new window performs almost the same calculations again.

The algorithm repeatedly throws away useful work and starts over.

This is the repeated work we want to eliminate.
"""

"""
===============================================================================
Observation
===============================================================================

Instead of looking at the sums,

compare the windows.

Window 1

2 1 5

↓

Window 2

1 5 1

Ask yourself

"What actually changed?"

Only two elements.

The number

2

left the window.

The number

1

entered the window.

Everything else

1

and

5

already existed.

That means most of the previous work is still useful.

Yet the brute-force algorithm ignores that information and computes
everything again.

This observation is the birth of the Sliding Window idea.

Instead of asking

"How do I compute the next answer?"

we now ask

"How do I update the previous answer?"
"""

"""
===============================================================================
Optimization Journey
===============================================================================

Stage 1

Treat every window as a completely independent problem.

↓

Time Complexity

O(n × k)

because every window recomputes all k elements.

------------------------------------------------------------

Stage 2

Notice that neighboring windows overlap heavily.

Only

one element leaves

and

one element enters.

------------------------------------------------------------

Stage 3

Instead of rebuilding the answer,

carry the previous answer forward.

Remove the expired contribution.

Add the new contribution.

------------------------------------------------------------

Stage 4

The algorithm now performs only constant work whenever the
window moves.

Instead of rebuilding,

we maintain.

This transforms the solution into an O(n) algorithm.

The optimization comes from preserving useful information.
"""

"""
===============================================================================
Repeated Work Being Eliminated
===============================================================================

Suppose

Window 1

2 1 5

Sum = 8

Now we need

Window 2

1 5 1

The brute-force algorithm performs

1 + 5 + 1

again.

But think carefully.

The previous answer already contains

1

and

5.

Why compute them again?

The only information that became invalid is

2

The only new information is

1

Therefore

New Sum

=

Old Sum

-

Leaving Element

+

Entering Element

This simple relationship removes all repeated computation.
"""

"""
===============================================================================
Maintained State
===============================================================================

Every Sliding Window problem maintains some information.

Different problems maintain different information.

This particular problem needs only one thing.

Current Window Sum

Nothing more.

Nothing less.

At every point during the algorithm,

we know the sum of the current window.

We never recompute it.

We simply update it whenever the window moves.

Notice something important.

The maintained state is chosen by the problem.

The Sliding Window technique does not tell us

what

to maintain.

It only tells us

how

to maintain it efficiently.
"""

"""
===============================================================================
Core Invariant
===============================================================================

The invariant is the statement that must remain true
throughout the entire algorithm.

For this problem

current_sum

always equals

the sum of the current window.

This statement must never become false.

Whenever the window moves,

current_sum

must immediately be updated so that it continues to represent
exactly the new window.

If this invariant breaks,

every future calculation becomes incorrect.
"""

"""
===============================================================================
Pointer / Variable Responsibilities
===============================================================================

Even though this is a Fixed Window problem,

it is still useful to think in terms of responsibilities
instead of movement.

------------------------------------------------------------

Left Side Responsibility

Remove expired information.

The leftmost element has left the current window.

Its contribution must be removed from

current_sum.

------------------------------------------------------------

Right Side Responsibility

Introduce new information.

The newest element has entered the current window.

Its contribution must be added to

current_sum.

------------------------------------------------------------

current_sum Responsibility

Represent exactly the sum of the current window.

It should never represent

the previous window

or

the next window.

It always represents

the current window.

------------------------------------------------------------

maximum_sum Responsibility

Store the largest window sum seen so far.

Unlike current_sum,

maximum_sum never decreases.

It simply records the best answer discovered during the journey.
"""

"""
===============================================================================
Algorithm (Reasoning Only)
===============================================================================

Step 1

Build the first complete window.

Compute its sum.

This becomes both

current_sum

and

maximum_sum.

------------------------------------------------------------

Step 2

Move the window by one position.

------------------------------------------------------------

Step 3

Remove the contribution of the element leaving the window.

------------------------------------------------------------

Step 4

Add the contribution of the new element entering the window.

------------------------------------------------------------

Step 5

Compare

current_sum

with

maximum_sum.

If the current window is better,

update the answer.

------------------------------------------------------------

Step 6

Repeat until every possible window has been processed.

Notice something interesting.

At no point do we ever recompute the entire window.

Every movement performs only two updates.

Remove one contribution.

Add one contribution.

That is the essence of the Fixed Window pattern.
"""
"""
===============================================================================
Runnable Python Code
===============================================================================

The following implementation directly follows the reasoning developed earlier.

Notice that the code itself is intentionally simple.

All of the difficulty lies in discovering the maintained state and the
invariant—not in writing the Python syntax.
"""


def maximum_sum_of_k_elements(nums, k):

    # Edge Case
    if len(nums) < k:
        return None

    # ------------------------------------------------------------
    # Build the first complete window
    # ------------------------------------------------------------

    current_sum = 0

    for index in range(k):
        current_sum = current_sum + nums[index]

    maximum_sum = current_sum

    # ------------------------------------------------------------
    # Slide the window through the remaining elements
    # ------------------------------------------------------------

    for right in range(k, len(nums)):

        left = right - k

        current_sum = current_sum - nums[left]

        current_sum = current_sum + nums[right]

        if current_sum > maximum_sum:
            maximum_sum = current_sum

    return maximum_sum


"""
===============================================================================
Example Run
===============================================================================

Input

nums = [2, 1, 5, 1, 3, 2]

k = 3

Possible Windows

[2,1,5] -> 8

[1,5,1] -> 7

[5,1,3] -> 9

[1,3,2] -> 6

Output

9

-------------------------------------------------------------------------------

Example

nums = [2, 1, 5, 1, 3, 2]

k = 3

print(maximum_sum_of_k_elements(nums, k))

Output

9
"""


"""
===============================================================================
Step-by-Step Dry Run
===============================================================================

Array

2 1 5 1 3 2

Window Size

3

-------------------------------------------------------------------------------

Step 1

Build the first window.

Window

2 1 5

current_sum

=

8

maximum_sum

=

8

-------------------------------------------------------------------------------

Slide Window

Old Window

2 1 5

↓

New Window

1 5 1

Leaving Element

2

Entering Element

1

Update

current_sum

=

8

-

2

+

1

=

7

maximum_sum

=

max(8,7)

=

8

-------------------------------------------------------------------------------

Slide Again

Old Window

1 5 1

↓

New Window

5 1 3

Leaving

1

Entering

3

Update

current_sum

=

7

-

1

+

3

=

9

maximum_sum

=

max(8,9)

=

9

-------------------------------------------------------------------------------

Slide Again

Old Window

5 1 3

↓

New Window

1 3 2

Leaving

5

Entering

2

Update

current_sum

=

9

-

5

+

2

=

6

maximum_sum

=

max(9,6)

=

9

-------------------------------------------------------------------------------

Right pointer has reached the end.

Return

9
"""


"""
===============================================================================
Why This Algorithm Works
===============================================================================

The algorithm works because of one simple observation.

When a fixed-size window moves by one position,

only two elements change.

Exactly one element leaves.

Exactly one element enters.

Every other element remains unchanged.

Therefore,

recomputing the entire window is unnecessary.

Instead,

we transform the previous answer into the next answer.

New Window Sum

=

Old Window Sum

-

Leaving Element

+

Entering Element

Since this relationship is mathematically correct for every slide,

every window sum is computed correctly.

The algorithm simply repeats this transformation until every window
has been processed.

-------------------------------------------------------------------------------

Another way to think about it

Imagine carrying a notebook.

The notebook contains only one piece of information.

The sum of the current window.

When the window moves,

you never throw away the notebook.

You simply erase one contribution

and

write one new contribution.

The notebook always stays synchronized with the current window.

That synchronization is exactly the invariant we proved earlier.
"""


"""
===============================================================================
Pattern Evolution
===============================================================================

Brute Force

↓

Treat every window independently.

↓

Repeated Work

↓

Notice neighboring windows overlap.

↓

Observation

↓

Only one element leaves.

Only one element enters.

↓

Maintained State

↓

Running Sum

↓

Invariant

↓

current_sum always represents
the current window.

↓

Local Updates

↓

Subtract Leaving Element.

↓

Add Entering Element.

↓

Linear Time Solution

-------------------------------------------------------------------------------

This evolution is more important than the final code.

Future Fixed Window problems will not always maintain

a sum.

Sometimes they will maintain

• Even Count

• Frequency Map

• Character Inventory

• Distinct Count

The maintained state changes.

The optimization journey does not.
"""
"""
===============================================================================
Mathematical / Logical Proof of Correctness
===============================================================================

A good algorithm is not only one that works.

It is one whose correctness can be explained.

Instead of saying

"It worked on the examples."

we want to prove

"It will work for every valid input."

-------------------------------------------------------------------------------

Claim

At every iteration,

current_sum

is exactly equal to the sum of the current window.

-------------------------------------------------------------------------------

Proof

Base Case

Before the sliding process begins,

we explicitly compute the sum of the first complete window.

Therefore,

current_sum

correctly represents the first window.

So the invariant is true before the loop starts.

-------------------------------------------------------------------------------

Induction Step

Assume

before one slide,

current_sum

correctly represents the current window.

Now the window moves by one position.

Exactly one element leaves.

Exactly one element enters.

The old window sum can be written as

Leaving Element

+

Middle Elements

The new window becomes

Middle Elements

+

Entering Element

Therefore

New Sum

=

Old Sum

-

Leaving Element

+

Entering Element

Our algorithm performs exactly these two operations.

Since nothing else changes,

current_sum

now correctly represents the new window.

Thus,

the invariant remains true after every slide.

-------------------------------------------------------------------------------

Conclusion

The invariant is true initially.

It remains true after every iteration.

Therefore,

current_sum

correctly represents every window processed by the algorithm.

Since

maximum_sum

is updated using every valid window,

the algorithm eventually returns the largest window sum.

Hence,

the algorithm is correct.

===============================================================================
Time Complexity
===============================================================================

Suppose

n = length of the array

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

The window slides

n - k

times.

Each slide performs only

1 subtraction

1 addition

1 comparison

All constant-time operations.

Time

O(n - k)

-------------------------------------------------------------------------------

Overall Time Complexity

O(k) + O(n - k)

=

O(n)

-------------------------------------------------------------------------------

Intuition

Every element participates in the running sum only a constant number of times.

No window is recomputed from scratch.

Repeated work has been eliminated.

===============================================================================
Space Complexity
===============================================================================

Extra variables used

current_sum

maximum_sum

left

right

All require constant memory.

Therefore

Space Complexity

O(1)

===============================================================================
Common Mistakes
===============================================================================

Mistake 1

Recomputing every window.

Wrong

For every window

calculate the complete sum again.

Why it is wrong

This brings the complexity back to

O(n × k)

and completely defeats the purpose of Sliding Window.

-------------------------------------------------------------------------------

Mistake 2

Building the first window incorrectly.

Some learners start sliding immediately.

The first complete window must always be built before the sliding process
begins.

-------------------------------------------------------------------------------

Mistake 3

Subtracting the wrong element.

Many beginners subtract

nums[right]

instead of

nums[right - k]

or the equivalent left index.

Remember

The leaving element is always

k

positions behind the entering element.

-------------------------------------------------------------------------------

Mistake 4

Updating the answer before updating the window.

Always

Remove

↓

Add

↓

Update Answer

Otherwise,

the maintained state no longer represents the current window.

-------------------------------------------------------------------------------

Mistake 5

Forgetting edge cases.

Example

k > len(nums)

No complete window exists.

Handle this case before starting the algorithm.

===============================================================================
Interview Questions
===============================================================================

Question 1

Why is this algorithm O(n) instead of O(n × k)?

-------------------------------------------------------------------------------

Question 2

What repeated work is eliminated by the Sliding Window technique?

-------------------------------------------------------------------------------

Question 3

Why is maintaining a running sum sufficient for this problem?

-------------------------------------------------------------------------------

Question 4

What invariant does current_sum maintain throughout the algorithm?

-------------------------------------------------------------------------------

Question 5

If instead of the sum we wanted the count of even numbers in each window,

what would change?

Expected Answer

Only the maintained state changes.

The overall Sliding Window algorithm remains the same.

===============================================================================
Revision Problems
===============================================================================

Easy

1.

Maximum Sum of K Consecutive Elements

(Implement again from memory.)

--------------------------------------------

2.

Average of Every K Consecutive Elements

(Maintained State

Running Sum)

-------------------------------------------------------------------------------

Medium

1.

Count Even Numbers in Every Window of Size K

(Maintained State

Running Even Count)

--------------------------------------------

2.

Maximum Number of Vowels in a Substring of Length K

(Maintained State

Running Vowel Count)

-------------------------------------------------------------------------------

Hard (Relative to This Variation)

1.

Permutation in String

(Maintained State

Frequency Map)

Notice

The window movement stays identical.

Only the maintained state becomes more sophisticated.

===============================================================================
Pattern Evolution
===============================================================================

Hashing

↓

Maintain Information

↓

Two Pointers

↓

Assign Pointer Responsibilities

↓

Fixed Sliding Window

↓

Maintain Window State

↓

Variable Sliding Window

↓

Maintain Window Validity

-------------------------------------------------------------------------------

Notice something important.

The algorithm itself barely changes.

Only

the maintained state

becomes richer.

This is why mastering the Fixed Window variation first makes every future
Sliding Window problem much easier.

===============================================================================
One-Line Memory Hook
===============================================================================

"A Fixed Window algorithm never rebuilds information.

It removes what expired,

adds what arrived,

and carries everything else forward."
"""


