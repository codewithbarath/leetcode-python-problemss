class Solution():
    def firstuniqchar(self,s):
        for i in range(0,len(s)):
            if(s.count(s[i])==1):
               return (s.index(s[i]))
        return ""
c1=Solution()
print(c1.firstuniqchar("loveleetcode"))