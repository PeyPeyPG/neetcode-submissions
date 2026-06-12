class Solution:    
    def isHappy(self, n: int) -> bool:
        doub = set()
        def isHappyHelper(n):
            l = list(str(n))
            s = 0
            for digit in l:
                s += int(digit)**2
            if s in doub:
                return False
            if s == 1:
                return True
            print(s)
            doub.add(s)
            print(doub)
            return isHappyHelper(s)
        return isHappyHelper(n)