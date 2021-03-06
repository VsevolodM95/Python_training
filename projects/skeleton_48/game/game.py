class lexicon(object):
    def __init__(self, name):
        self.name = name

    def scan(self, stuff):

        words = stuff.split()
        
        #predefined values
        directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        verbs = ['go', 'stop', 'kill', 'eat']
        st_words = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', 'bear', 'princess', 'cabinet']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        #-----------------
        
        wmas = []
        wmas = words
        
        i = 0
        j = 0
        res = []
        appended = False
        isNumber = True
        
        for line in words:
            appended = False
            for num in directions:
                if num == wmas[i]:
                    res.append(("direction", wmas[i]))
                    appended = True
            for num in verbs:
                if num == wmas[i]:
                    res.append(("verb", wmas[i]))
                    appended = True
            for num in st_words:
                if num == wmas[i]:
                    res.append(("stop", wmas[i]))
                    appended = True
            for num in nouns:
                if num == wmas[i]:
                    res.append(("noun", wmas[i]))
                    appended = True

            #checking if it's number
            if appended == False:
                chyslo = []
                chyslo = wmas[i]
                
                while j < len(chyslo) and isNumber == True:
                    if chyslo[j] not in numbers:
                        isNumber = False #it's not a number
                    j+=1
                    
                if isNumber == True:
                    res.append(("number", int(wmas[i])))
                    appended = True  
            #        
            if appended == False:
                res.append(("error", wmas[i]))
                
            i+=1
            
        return res

