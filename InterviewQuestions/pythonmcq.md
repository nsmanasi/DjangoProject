1) What is the output of the following program?
str1 = '{2}, {1} and {0}'.format('a', 'b', 'c') 
str2 = '{0}{1}{0}'.format('abra', 'cad') 
print(str1, str2) 

2)
a = 2
b = '3.77'
c = -8
str1 = '{0:.4f} {0:3d} {2} {1}'.format(a, b, c) 
print(str1) 


3)

import string 
import string 
Line1 = "And Then There Were None"
Line2 = "Famous In Love"
Line3 = "Famous Were The Kol And Klaus"
Line4 = Line1 + Line2 + Line3 
print(string.find(Line1, 'Were'), string.count((Line4), 'And')) 


4)
line = "I'll come by then."
eline = "" 
for i in line: 
	eline += chr(ord(i)+3) 
print(eline)	 

5)

line = "What will have so will"
L = line.split('a') 
for i in L: 
	print(i, end=' ') 

Answers ::
1.c, b and a abracadabra
2.2.0000 2 -8 3.77
3.(15, 2)
4.L*oo#frph#e|#wkhq1
5.
Wh t will h ve so will

source --
https://www.geeksforgeeks.org/output-python-programs-set-19-strings/
