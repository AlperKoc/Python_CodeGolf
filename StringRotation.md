# A string rotation is done by taking characters one-by-one from one end of a string and placing them on the other end. A right rotation is done by taking characters from the end and placing them at the beginning of the string, and a left rotation is done by taking characters from the beginning and placing at the end of the string.

Given a string s1 and s2, determine whether s2 is a rotation (left or right) of s1, ignoring the case.

- Example 1:
  - s1 = "AbcD" and s2 = "CDab", print "true"
    - s2 can be rotated 2 times to the right to be equal to s1: ("CDab" => "bCDa" => "abCD")

- Example 2:
  - s1 = "ZYXW" and s2 = "XYzW", print "false"

No matter how many times you rotate s2, it'll never be equal to s1

- Input
  * Line 1: String s1
  * Line 2: String s2
- Output
  * "true" if s2 is a rotation of s1 and "false" if not.
  
- Constraints
  * Length of s1,s2 <= 100
  * Strings s1 and s2 can contain any character on the ASCII table ;)

- Example
  - Input
    * AbcD
    * CDab
- Output
  * true

# Answer

`print(["false","true"][input().lower()in input().lower()*2])`

