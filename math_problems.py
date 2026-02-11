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

