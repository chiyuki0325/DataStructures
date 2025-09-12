from typing import List

class Solution1:
    # 暴力解法
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needle=dict()
        for char in p:
            if char in needle:
                needle[char]+=1
            else:
                needle[char]=1
        result=[]
        for i in range(len(s)-len(p)+1):
            # print(s[i:i+len(p)])
            n=needle.copy()
            hit=True
            for j in range(i,i+len(p)):
                if s[j] not in n:
                    hit=False
                    break
                # n.remove(s[j])
                if n[s[j]]>1:
                    n[s[j]]-=1
                else:
                    n.pop(s[j])
            # print(n)
            if hit and len(n)==0:
                result.append(i)
        return result

class Solution:
    # 正解：滑动窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):return []

        keyword=[0]*26
        for char in p:
            keyword[ord(char)-97]+=1
        result=[]

        window=[0]*26
        for i in range(len(p)):
            char=s[i]
            window[ord(char)-97]+=1

        if window==keyword:
            result.append(0)

        for i in range(1, len(s)-len(p)+1):
            char_to_delete=s[i-1]
            window[ord(char_to_delete)-97]-=1
            char_to_append=s[i+len(p)-1]
            window[ord(char_to_append)-97]+=1
            if window==keyword:
                result.append(i)
        return result

if __name__=="__main__":
    s=Solution()
    assert s.findAnagrams("cbaebabacd", "abc")==[0,6]
