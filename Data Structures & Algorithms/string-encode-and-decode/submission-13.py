class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstring = ''
        for word in strs:
            encodedstring = encodedstring + str(len(word)) + ','
        encodedstring += '#'

        for word in strs:
            encodedstring += word

        print(encodedstring)
        
        return encodedstring


    def decode(self, s: str) -> List[str]:
        i = 0
        finallist = []

        while s[i] != "#":
            i += 1
        
        firsthalf = s[:i-1]
        print(firsthalf)
        secondhalf = s[i+1:]
        print(secondhalf)

        if firsthalf == '':
            return []
        else:
            numlist = firsthalf.split(",")
        print(numlist)
        int_list = [int(item) for item in numlist]
        print(int_list)


        initial = 0
        for num in int_list:
            finallist.append(secondhalf[initial: initial + num])
            initial += num
        
        return finallist
        

