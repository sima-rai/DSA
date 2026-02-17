print("----------------Count Digits-------------------------")
# https://takeuforward.org/data-structure/count-digits-in-a-number

class Solution():
    def count_digits_in_a_number(self, digits):
        counter = 0
        for i in str(digits):
            counter +=1
        return counter

# optimized solution
class Solution():
    def count_digits_in_a_number(self, digits):
        counter = 0

        if digits == 0:
            return 1
        while digits >0:
            # digits = digits//10
            digits//=10
            counter +=1
        return counter  
sol = Solution()
print(sol.count_digits_in_a_number(12345))




print("----------------Reverse digits of a number-------------------------")
# https://takeuforward.org/maths/reverse-digits-of-a-number
class Solution():
    def reverse_integer(self, n):

        INT_MAX = 2**31 - 1

        sign = -1 if n <0 else 1
        rev_no = 0
        n = abs(n)
        while n>0:
            last_digit = n % 10
            n = n // 10 

            # if rev_no * 10 + last_digit > INT_MAX:
            if rev_no > (INT_MAX - last_digit)//10:
                return 0
            rev_no = rev_no * 10 + last_digit
        
        return rev_no*sign
    

sol = Solution()
print(sol.reverse_integer(-123))





print("----------------Number is palidrime-------------------------")
# https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not
class Solution():
    def is_palindrome(self, n):
        print(n)
        initial_no = n
        rev_no = 0
        while n>0:
            last_digit = n%10
            rev_no = rev_no * 10 + last_digit
            n = n //10
        
        return True if initial_no == rev_no else False
        
sol = Solution()
print(sol.is_palindrome(123621))


# optmized
class Solution():
    def is_palindrome(self, n):

        # for negatvie number

        if n < 0 or (n % 10 == 0 and n != 0):
            return False
        rev_no = 0
        while n>rev_no:
            last_digit = n%10
            rev_no = rev_no * 10 + last_digit
            n = n //10
        return n == rev_no or n == rev_no // 10
        
sol = Solution()
print(sol.is_palindrome(12))




print("----------------Greatest Common Divisor------------------------")
# https://takeuforward.org/data-structure/find-gcd-of-two-numbers
class Solution():
    def calculate_GCD(self, n1, n2):


        factors1 = [ i for i in range(1, n1+1) if n1%i== 0 ]
        factors2 = [ i for i in range(1, n2+1) if n2%i== 0 ]

        print(factors1, factors2)

        common_factors = []
        if len(factors1) < len(factors2):
            for i in factors1:
                if i in factors2:
                    common_factors.append(i)
        else:
            for i in factors2:
                if i in factors1:
                    common_factors.append(i)

        return max(common_factors)


sol = Solution()
print(sol.calculate_GCD(20, 15))


#optmized (better bruteforce)
class Solution():
    def calculate_GCD(self, n1, n2):

        for i in range(min(n1,n2), 1, -1):
            if n1%i == 0 and n2%i == 0:
                return i
            
        
        return 1

sol = Solution()
print(sol.calculate_GCD(20, 15))


#euclidean algorithn 
class Solution():
    def calculate_GCD(self, a, b):
        while b != 0:
            a, b = b, a%b
        return a

sol = Solution()
print(sol.calculate_GCD(15, 20))



# using math

import math
class Solution():
    def calculate_GCD(self, a, b):
        return math.gcd(a,b)


sol = Solution()
print(sol.calculate_GCD(15, 20))
