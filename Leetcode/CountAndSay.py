'''
LeetCode
Top Interview Question
String: Count and Say
URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        else:
            res = ""
            s = self.countAndSay(n-1)
            i,j = 0,0
            cnt = 0
            while j < len(s):
                if s[j] == s[i]:
                    cnt += 1
                    j += 1
                else:
                    res += str(cnt)+str(s[i])
                    cnt = 1
                    i = j
                    j += 1
            res += str(cnt)+str(s[i])
            return res
            
            
                
        
            
        