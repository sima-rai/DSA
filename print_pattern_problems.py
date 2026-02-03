# Pattern-1: Rectangular Star Pattern


# def print_pattern(n):
#     for i in range(n):
#         for j in range(n):
#             print('*', end='')
#         print()
    
# print(print_pattern(6))


# n = 3

# for _ in range(n):
#     print("*" * n)



# class Solution:
#     # Function to print a square pattern of stars
#     def pattern1(self, N):
#         # Outer loop to handle rows
#         for i in range(N):
#             # Inner loop to handle columns for each row
#             for j in range(N):
#                 # Print a star followed by a space
#                 print("*", end=" ")
#             # After printing stars in a row, move to the next line
#             print() 

# # Driver code
# sol = Solution()
# N = 5  # Set the size of the square (5x5)
# sol.pattern1(N)  # Call the function to print the pattern



print("--------------------------------------")
class Solution:
    def pattern4(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print(i, end="")

            print()

sol = Solution()
sol.pattern4(5)

print("--------------------------------------")
class Solution:
    def pattern5(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print('*', end="")

            print()

sol = Solution()
sol.pattern5(5)

print("--------------------------------------")
class Solution:
    def pattern6(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print(j+1, end="")

            print()

sol = Solution()
sol.pattern6(5)



print("--------------------------------------")
class Solution:
    def pattern7(self, n):
        c = n-1
        s = ' '
        m = 1
        for i in range(n):
            print(c*s + '*'*m +c*s)
            c-=1
            m+=2
sol = Solution()
sol.pattern7(5)



print("--------------------------------------")
class Solution:
    def pattern8(self, n):
        a =2*n-1
        s = ' '
        m = 0
        for i in range(n):
            print(m*s + a*'*' + m*s)
            a-=2
            m +=1
        
sol = Solution()
sol.pattern8(5)



print("--------------------------------------")
class Solution:
    def pattern9(self, n):
        N = 2*n
        c = n-1
        s= ' '
        m = 1

        for i in range(N):
            if i<n:
                print(c*s + '*'* m + c*s)
                c -=1
                m +=2
            else:
                c +=1
                m -=2
                print(c*s + '*'* m + c*s)
           
sol = Solution()
sol.pattern9(5)



print("--------------------------------------")
class Solution:
    def pattern10(self, n):
        N = 2*n
        c = n-1
        s= ' '
        m = 1

        for i in range(N):
            if i<n:
                print('*'* m + c*s)
                c -=1
                m +=1
            else:
                c +=1
                m -=1
                print('*'* m + c*s)
           
sol = Solution()
sol.pattern10(5)





print("--------------------------------------")
class Solution:
    def pattern7(self, n):
        for i in range(n):
            print(' '*(n-i-1) + '*'*(2*i+1))
sol = Solution()
sol.pattern7(5)



print("---------------11-----------------------")
# class Solution:
#     def pattern11(self, n):
#         x = '1'
#         y = '0 1'
#         for i in range(1, n+1):
#             if i % 2 != 0:
#                 print(x)
#                 x += ' 0 1'
#             else:
#                 print(y)
#                 y += ' 0 1'

# sol = Solution()
# sol.pattern11(5)


class Solution:
    def pattern11(self, n):
        for i in range(1, n + 1):
            start = 1 if i % 2 != 0 else 0
            for j in range(i):
                # print(j,"j loop")
                print(start, end=" ")
                start = 1 - start
            print()

sol = Solution()
sol.pattern11(5)





print("----------------12----------------------")
# https://takeuforward.org/plus/dsa/problems/pattern-12

class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            for j in range(1,i+1):
                print(j, end=" ")
            m =2*n-i*2
            print('  '* m, end= "")
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()
sol = Solution()
sol.pattern12(4)




print("----------------13----------------------")
# https://takeuforward.org/plus/dsa/problems/pattern-13

class Solution:
    def pattern13(self, n):
        x = 1
        for i in range(1, n+1):
            for _ in range(1, i+1):
                print(x, end=" ")
                x +=1
            print()

            
sol = Solution()
sol.pattern13(4)



print("----------------14----------------------")
# https://takeuforward.org/plus/dsa/problems/pattern-14


# class Solution:
#     def pattern14(self, n):
#         import string
#         s = string.ascii_uppercase
#         for i in range(n):
#             for j in range(i+1):
#                 print(s[j], end=" ")
#             print()
    
# sol = Solution()
# sol.pattern14(4)


class Solution:
    def pattern14(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(ord('A')+j), end=" ")
            print()
    
sol = Solution()
sol.pattern14(4)






print("----------------15----------------------")
# https://takeuforward.org/plus/dsa/problems/pattern-15

class Solution:
    def pattern15(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print(chr(ord('A')+j), end="")
            print()
      

sol = Solution()
sol.pattern15(5)



print("----------------16----------------------")
# https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern

class Solution:
    def pattern16(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(ord('A')+i), end="")
            print()
      

sol = Solution()
sol.pattern16(5)


print("----------------17----------------------") 
# https://takeuforward.org/plus/dsa/problems/pattern-17
class Solution:
    def pattern17(self, n):
       x = n
       for i in range(n):
            print(" "*(x-1), end="")
            for j in range(i+1): 
                print(chr(ord('A')+j), end="")
            for j in range(i,0,-1): 
                print(chr(ord('A')+j-1), end="")
            print()
            x-=1
sol = Solution()
sol.pattern17(4)



print("----------------18----------------------")
# https://takeuforward.org/plus/dsa/problems/pattern-18
class Solution:
    def pattern18(self, n):
       for i in range(n):
            for j in range(i+1, 0,-1):
               print(chr(ord('A') + n-j), end=" ")
            print()
sol = Solution()
sol.pattern18(4)



print("----------------19----------------------")
# https://takeuforward.org/plus/dsa/problems/pattern-19

class Solution:
    def pattern19(self, n):
        for i in range(n):
           print('*'*(n-i), end="")
           print(' '*i*2, end="")
           print('*'*(n-i))
        for i in range(n-1,-1,-1):
           print('*'*(n-i), end="")
           print(' '*i*2, end="")
           print('*'*(n-i))
sol = Solution()
sol.pattern19(5)



print("----------------21----------------------")
# https://takeuforward.org/plus/dsa/problems/pattern-21
class Solution:
    def pattern21(self, n):
        for i in range(n):
            if i == 0 or i ==(n-1):
                print('*'*n)
            else:
                print('*' + ' '*(n-2) + '*')

sol = Solution()
sol.pattern21(4)



print("----------------22 final----------------------")
# # https://takeuforward.org/plus/dsa/problems/pattern-22
class Solution:
    def pattern22(self, n):
        for i in range(n):
            for j in range(i+1):
                print(n-j, end="")
            for j in range(i+1, n):
                print(n-i, end="")
            for j in range(n-1-i):
                print(n-i, end="")
            for j in range(i,0,-1):
                print(n+1-j, end="")
            print()
        
        for i in range(n-1):
            for j in range(n, i+2, -1):
                print(j, end="")
            for j in range(i+2):
                print(i+2, end="")
            for j in range(i+1):
                print(i+2, end="")
            for j in range(i+3, n+1):
                print(j, end="")

            print()



# optimized solution
class Solution:
    def pattern22(self, n):
        size = 2 * n - 1
        for i in range(size):
            for j in range(size):
                val = n - min(i, j, size - 1 - i, size - 1 - j)
                print(val, end="")
            print()

        
sol = Solution()
sol.pattern22(5)