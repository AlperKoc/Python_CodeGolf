# You are given two numbers X and N. You should output :X!/ (X - N)!

- Example: 
  - input: X = 6, N = 4

* output should be the result of 6*5*4*3

- Input
  - Two integers :
    * Line 1: X
    * Line 2: N
- Output
  - The result of X! / (X - N)!

- Constraints
  - 0 < X <= 18
  - X >= N > 0

- Example
  - Input
    * 6
    * 4
  - Output
    * 360

# Answer

`x=int(input())
f=lambda x:0**x or x*f(x-1)
print(f(x)//f(x-int(input())))`


