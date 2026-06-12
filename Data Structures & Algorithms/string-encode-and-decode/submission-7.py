class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "-1"
        sol = ""
        for i in range(len(strs)-1):
            sol += strs[i] + "分"
        if strs:
            sol += strs[-1]
        return sol

    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []
        if len(s) == 0:
            return [s]
        return s.split("分")