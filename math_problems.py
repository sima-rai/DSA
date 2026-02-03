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
