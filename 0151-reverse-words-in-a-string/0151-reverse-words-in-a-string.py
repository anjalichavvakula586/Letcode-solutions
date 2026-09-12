class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        n=len(a)
        for i in range(n//2):
            a[i],a[n-i-1]=a[n-i-1],a[i]
        return ' '.join(a)
        