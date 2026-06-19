"""
===============================================================================
Problem: Valid Palindrome
LeetCode: 125
Pattern: Two Pointers -> Symmetric Converging
Difficulty: Easy
===============================================================================

PROBLEM DESCRIPTION
-------------------

A phrase is called a palindrome if, after:

1. Converting all uppercase letters to lowercase.
2. Ignoring spaces.
3. Ignoring punctuation.
4. Ignoring all non-alphanumeric characters.

it reads exactly the same forwards and backwards.

Return True if the given string is a palindrome.

Otherwise return False.

------------------------------------------------------------

Example 1

Input

"A man, a plan, a canal: Panama"

Output

True

------------------------------------------------------------

Example 2

Input

"race a car"

Output

False

------------------------------------------------------------

Notice

We DO NOT reverse the string.

We simply compare corresponding characters.

===============================================================================
THOUGHT PROCESS
===============================================================================

Question 1

What are we actually comparing?

Answer

Only valid alphanumeric characters.

Everything else should be ignored.

------------------------------------------------------------

Question 2

Does every valid character have a mirror partner?

Yes.

This immediately suggests

Symmetric Converging.

------------------------------------------------------------

Question 3

Can we compare immediately?

Not always.

Sometimes a pointer is standing on:

- space
- comma
- colon
- punctuation

Those characters are irrelevant.

We must first move to the next valid character.

------------------------------------------------------------

Question 4

After finding two valid characters,

what should we do?

Compare them.

If equal

Move both pointers.

If different

Return False immediately.

------------------------------------------------------------

Question 5

Why do we use while instead of if while skipping?

Because one invalid character may be followed by
another invalid character.

Example

"a,,,b"

Stopping after skipping one comma is not enough.

We must continue until we reach a valid character.

===============================================================================
INVARIANT
===============================================================================

Everything outside the two pointers
has already been successfully matched.

Every invalid character outside the pointers
has already been skipped.

===============================================================================
POINTER RESPONSIBILITIES
===============================================================================

Left Pointer

- Find the next valid character from the left.

------------------------------------------------------------

Right Pointer

- Find the next valid character from the right.

------------------------------------------------------------

After both become valid

Compare them.

If equal

Move both.

If different

Palindrome breaks.

===============================================================================
"""


def is_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left = left + 1

        while left < right and not s[right].isalnum():
            right = right - 1

        if s[left].lower() != s[right].lower():
            return False

        left = left + 1
        right = right - 1

    return True


###############################################################################
# Example Run
###############################################################################

if __name__ == "__main__":

    s = "A man, a plan, a canal: Panama"

    print(is_palindrome(s))


"""
===============================================================================
DRY RUN
===============================================================================

String

"A man, a plan, a canal: Panama"

------------------------------------------------------------

Left

'A'

Right

'a'

Convert both to lowercase

'a'

'a'

Equal

Move both.

------------------------------------------------------------

Left

space

Skip.

Reader keeps moving.

------------------------------------------------------------

Now

Left

'm'

Right

'm'

Equal

Move both.

------------------------------------------------------------

Continue.

Whenever

space

comma

colon

or punctuation appears,

keep skipping until reaching
the next valid alphanumeric character.

------------------------------------------------------------

Eventually

Left crosses Right.

All valid pairs matched.

Return

True.

===============================================================================
WHY DOES THIS WORK?
===============================================================================

Every valid character is compared exactly once.

Every invalid character is skipped exactly once.

Every processed pair is permanently correct.

The invariant

"Everything outside the pointers is matched"

never breaks.

===============================================================================
PATTERN EVOLUTION
===============================================================================

Reverse String

↓

Need comparison instead of swapping

↓

Valid Palindrome

↓

Need skipping of invalid characters

↓

Conditional Pointer Movement

Notice

The underlying pattern never changed.

Only one additional rule was introduced.

===============================================================================
TIME COMPLEXITY
===============================================================================

Each pointer only moves forward.

Every character is visited at most once.

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

Using

if

instead of

while

while skipping punctuation.

Wrong.

There may be multiple consecutive
invalid characters.

------------------------------------------------------------

2.

Comparing before skipping.

This compares punctuation.

Wrong answer.

------------------------------------------------------------

3.

Forgetting lowercase conversion.

'A'

and

'a'

should be considered equal.

------------------------------------------------------------

4.

Moving both pointers while skipping.

Wrong.

One pointer may already be on
a valid character.

Only the invalid pointer should move.

------------------------------------------------------------

5.

Reversing the string first.

Correct,

but uses unnecessary extra work.

===============================================================================
INTERVIEW QUESTIONS
===============================================================================

1.

Why do we need while instead of if?

------------------------------------------------------------

2.

What invariant is maintained?

------------------------------------------------------------

3.

Why does only one pointer sometimes move?

------------------------------------------------------------

4.

Why do we convert to lowercase
before comparison?

------------------------------------------------------------

5.

How is this different from Reverse String?

===============================================================================
REVISION PROBLEMS
===============================================================================

Easy

1.

Valid Palindrome II
(LeetCode 680)

2.

Reverse Vowels of a String
(LeetCode 345)

------------------------------------------------------------

Medium

3.

Sentence Similarity III
(LeetCode 1813)

4.

Append Characters to String to Make Subsequence
(LeetCode 2486)

------------------------------------------------------------

Hard

5.

Shortest Palindrome
(LeetCode 214)

===============================================================================
ONE-LINE MEMORY HOOK
===============================================================================

Skip.

Compare.

Move inward.

Repeat.

===============================================================================

"""