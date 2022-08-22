# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

num1 = "505"
num2 = "2501"

# simplest approach: eval function
def addStrings(num1, num2):
    return eval(num1) + eval(num2)

print(addStrings(num1, num2))

# more complex: ord

def solution(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1 
        m1 = m1//10        

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1 + n2)

print(solution(num1, num2))