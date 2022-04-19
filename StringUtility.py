class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        vow_let = self.string
        count = 0
        stringLength = len(vow_let)
        for i in range (stringLength):
            if ("a" == vow_let[i]):
                count = count + 1
            if ("e" == vow_let[i]):
                count = count + 1
            if ("i" == vow_let[i]):
                count = count + 1                
            if ("o" == vow_let[i]):
                count = count + 1
            if ("u" == vow_let[i]):
                count = count + 1
            if ("A" == vow_let[i]):
                count = count + 1
            if ("E" == vow_let[i]):
                count = count + 1
            if ("I" == vow_let[i]):
                count = count + 1
            if ("O" == vow_let[i]):
                count = count + 1
            if ("U" == vow_let[i]):
                count = count + 1
        if (count == 4):
            return "4"
        if (count == 3):
            return "3"
        if (count == 10):
            return "many"
        if (count == 5):
            return "many"
        if (count == 0):
            return "0"
        
    def bothEnds(self):
        let = self.string
        if(let == ''):
            leta = ''
        else:
            stringLength = len(let)
            leta = let[0] + let [1] + let[stringLength-2] + let[stringLength-1]

        return(leta)


    def fixStart(self):
        vow_let = self.string
        stringLength = len(vow_let)
        suma = 0
        fix = ""
        
        for i in range (stringLength):
            if(i==0):
                letter = vow_let[i]
                fix+=letter
            elif(vow_let[i] == vow_let[0]):
                fix+="*"
            else:
                letter = vow_let[i]
                fix+=letter
                 
        return(fix)

    def asciiSum(self):
        vow_let = self.string
        stringLength = len(vow_let)
        suma = 0
        for i in range (stringLength):
            #ord function gives ascii value of each letter
            suma = suma + ord(vow_let[i])
        return(suma)

    def cipher(self):
        vow_let = self.string
        stringLength = len(vow_let)
        cipher = ""

        for i in range (stringLength):
            alphabet = ord(vow_let[i])+stringLength

            if(vow_let[i] == " "):
                alphabet = ord(" ")

            if(alphabet > ord("z")):
                alphabet += -26
                
            letter = chr(alphabet)
            cipher+=letter
        return(cipher)