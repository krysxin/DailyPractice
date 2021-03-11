'''
March LeetCoding Challenge 2021
Week2: Integer to Roman
URL: https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/

My Solution:
Continuously match the digit with the corresponding Roman char from right to left.

Solution2 (More efficient):
Creat a look up table for the conversion between digit and numeral. 
Deal with the values in descending orders and insert the appropriate numral(s) while 
reducing the target Number(N) by the same amount.
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        res = ""
        for i in range(len(str(num))):
            temp = num % 10
            num = num // 10
            if i == 0:
                if temp < 4:
                    s = "I"*temp
                elif temp == 4:
                    s = "IV"
                elif temp > 4 and temp < 9:
                    s = "V"+"I"*(temp-5)
                elif temp == 9:
                    s = "IX"
                ans.append(s)
            elif i == 1:
                if temp < 4:
                    s = "X"*temp
                elif temp == 4:
                    s = "XL"
                elif temp > 4 and temp < 9:
                    s = "L"+"X"*(temp-5)
                elif temp == 9:
                    s = "XC"
                ans.append(s)
            elif i == 2:
                if temp < 4:
                    s = "C"*temp
                elif temp == 4:
                    s = "CD"
                elif temp > 4 and temp < 9:
                    s = "D"+"C"*(temp-5)
                elif temp == 9:
                    s = "CM"
                ans.append(s)
            else:
                s = "M"*temp
                ans.append(s)
            
        for i in range(len(ans)-1, -1, -1):
            res += ans[i]
        
        return res


class Solution2:
    def intToRoman(self, N: int) -> str:
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        ans = ""
        for i in range(13):
            while N >= val[i]:
                ans += rom[i]
                N -= val[i]
        return ans
                
        