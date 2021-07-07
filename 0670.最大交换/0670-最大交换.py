class Solution:
    def maximumSwap(self, num: int) -> int:
        number = []
        res = num
        while num:
            number.append(num%10)
            num = num//10
        number=number[::-1]

        sorted_number = sorted(number)[::-1]

        i = 0
        while i< len(number) and sorted_number[i] == number[i]:
            i+=1

        # print(number, sorted_number)

        if i == len(number):
            return res

        j = 1

        while j < len(number):
            if number[-j] == sorted_number[i]:
                number[i],number[-j] = number[-j], number[i]
                break
            j+=1
        
        # print(number)
        res = 0
        for n in number:
            res = res*10+n
        return res