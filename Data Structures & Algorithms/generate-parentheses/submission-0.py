class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        array = []
        def generateParenthesisHelper(n, s, op, close):
            if close < op and close < n and op < n:
                generateParenthesisHelper(n, s+"(", op+1, close)
                generateParenthesisHelper(n, s+")", op, close+1)
            elif close == op and op < n:
                generateParenthesisHelper(n, s+"(", op+1, close)
            elif op == n and close < n:
                generateParenthesisHelper(n, s+")", op, close+1)
            else:
                array.append(s)
                return
        generateParenthesisHelper(n, "", 0, 0)
        return array
