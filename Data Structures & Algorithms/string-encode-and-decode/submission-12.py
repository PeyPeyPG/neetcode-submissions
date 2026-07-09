class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for i in strs:
            final_string += f"#{len(i)}#{i}"
        print(final_string)
        return final_string




    def decode(self, s: str) -> List[str]:
        pointer = 0
        # string_len = ""
        # seen = ""
        substrings = []
        while pointer < len(s):
            next_hash = s.find('#',pointer+1)
            string_len = int(s[pointer+1:next_hash])
            substrings.append(s[next_hash+1:next_hash+1+string_len])
            pointer = next_hash+1+string_len
        return substrings