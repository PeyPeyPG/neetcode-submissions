class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += s + '分'
        return code
    def decode(self, s: str) -> List[str]:
        a = s.split('分')
        return a[0:len(a)-1]