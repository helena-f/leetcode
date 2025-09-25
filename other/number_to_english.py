class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num == 0:
            return "Zero"
        res = []
        # 0-9 : dict to english words
        # 10-90 : dict to english words
        digit = {0:"", 1: "One", 2 : "Two", 3: "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7: "Seven", 8:"Eight", 9: "Nine"}
        tens = {0: "", 1 : "One", 2 : "Twenty", 3 : "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        teen = {10: "Ten", 11 : "Eleven", 12: "Twelve", 13:"Thirteen",14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        desc = {6 : "Million", 3 : "Thousand", 9:"Billion", 12:"Trillion", 15:"Quadrillion", 18: "Quintillion", 21:"Sextillion", 24:"Septillion", 27:"Octillion", 30:"Nonillion", 33:"Decillion"}
        # 2(hundred)21(million),0(hundred)00(thousand),0(hundred)00
        # 221,000,000
        # 876,543,210
        # edge case: 11, 12, 13, 14, 15, 16, 17, 18, 19
        # edge case: 0, account by counting the offset number
        #            of zeros for the right descriptor

        # iteration of digits 
        # ignoring the last digit : dividing by 10
        # last digit : mod 10
        # stop when gone through all digits
        # 123 -> 12 -> 1 : 1 / 10 -> 0
        # print(1/10)
        # track placement in number
        counter = 0
        rest = num
        
        while rest != 0:
            curr_digit = rest % 10
            rest = rest / 10

            # if curr_digit == 0:
            #     zero_count = 1
            #     while curr_digit == 0:
                    
            #         counter += 1
            #         curr_digit = rest % 10
            #         rest = rest / 10

            # modulus counter of order in 3 digits
            curr_place = counter % 3

            # ones digit -> digit map
            if curr_place == 0:
                # value is added backwards
                if counter >= 3:
                    # add descriptor
                    if counter in desc:
                        res.append(desc[counter])
                # account for 10-19
                if (rest % 10) == 1:
                    res.append(teen[(10+curr_digit)])
                    # skip the next digit
                    counter += 1
                    rest = rest / 10
                elif curr_digit in digit:
                    res.append(digit[curr_digit]) 

            # tens digit -> tens map
            elif curr_place == 1:
                res.append(tens[curr_digit])


            # third : digit + descriptor
            elif curr_place == 2: 
                if curr_digit != 0:
                    res.append("Hundred")  
                    res.append(digit[curr_digit])

            prev = curr_digit
            counter += 1
            # account for 1's in the tens place

        

        # end loop after iterating through the entire number

        # account 3 digit separations
        res.reverse()
        fin = [res[0]]
        fin_count = 0
        for i in range(1, len(res)):
            if res[i] != "" and not (res[i] in desc.values() and fin[fin_count] in desc.values()):
                fin.append(res[i])
                fin_count += 1
            
        
        return " ".join(fin)
