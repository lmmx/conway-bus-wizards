The age of the wizard is 90

90 is the only number which admits multiple factorisations which
share the same length, making it impossible to know from the
number itself (90) and the number of "children" (i.e. the number
of factors in the factorisation) which of the possible factorisations
it is.

Specifically, these potential factorisations are:

- `1, 9, 10` ⇒ Σ = 20 (cardinality = 3)
- `2, 3, 15` ⇒ Σ = 20 (cardinality = 3)

and

- `2, 5, 9`  ⇒ Σ = 16 (cardinality = 3)
- `3, 3, 10` ⇒ Σ = 16 (cardinality = 3)

The other numbers (up to 100) which admit factorisations that
share a length of factors with each other are:

- 36
  - `2, 2, 9` and `1, 6, 6` ⇒ Σ = 13 (cardinality = 3)
- 40
  - `1, 5, 8` and `2, 2, 10` ⇒ Σ = 14 (cardinality = 3)
- 48
  - `1, 3, 4, 4` and `2, 2, 2, 6` ⇒ Σ = 12 (cardinality = 4)
- 72
  - `2, 6, 6` and `2, 3, 8` ⇒ Σ = 13 (cardinality = 3)
  - `1, 2, 6, 6`, `1, 3, 3, 8`, and `2, 2, 2, 9` (cardinality = 4)
- 80
  - `1, 2, 5, 8` and `2, 2, 2, 10` ⇒ Σ = 16 (cardinality = 4)
- 96
  - `1, 4, 4, 6` and `2, 2, 3, 8` ⇒ Σ = 15 (cardinality = 4)
  - `1, 2, 3, 4, 4` and `2, 2, 2, 2, 6` ⇒ Σ = 14 (cardinality = 5)

These are output by the program `calc.py` (which I then inspected manually).

Only 90 has two sums which would mean that with the assumption the other wizard
has forgotten the number of the bus (?!) then with only the age of the wizard and
the number of children alone it would be impossible to tell which it is...

Update: this can apparently not be the assumption, as Robin clarifies to someone else
[here](https://twitter.com/robinhouston/status/1250767790190981120)
