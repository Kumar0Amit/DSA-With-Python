---

## Reader / Writer

### Goal

Build a finished portion while scanning the array once.

### Core Idea

Reader discovers.

Writer commits.

### Invariant

Everything before Writer is already correct.

### Pointer Movement

Reader always moves.

Writer moves only after finding a valid element.

### Recognition Keywords

- remove
- compress
- filter
- keep only
- move
- stable
- preserve order
- in-place

### Representative Problems

- Remove Duplicates
- Move Zeroes
- Remove Element

---

