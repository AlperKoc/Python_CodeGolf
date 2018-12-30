# Your program must create the lowest integer from the input with the choice of subtracting each digit from 9 or not.
For example, 17 can become 12 by replacing the digit 7 by 2 (because 9 - 7 = 2).

- INPUT:
  - Line 1 : One integer N.

- OUTPUT:
  - Ligne 1 : One integer.

- CONSTRAINTS:
  - 0 ≤ N ≤ 10000

EXAMPLE:
- Input
  - 169
- Output
  - 130

# Answer
`print(*[i if i<5else 9-i for i in map(int,list(input()))],sep="")`
