class Lexicon(object):
    def __init__(self):
        pass

    def scan(self, stuff):

        words = stuff.split()
        
        #predefined values
        direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        verbs = ['go', 'stop', 'kill', 'eat']
        st_words = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', ' bear', 'princess', 'cabinet']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        #-----------------
        
        wmas = []
        wmas = words
        
        i = 0
        
        for line in words:
            for num in direction:
                if num == wmas[i]:
                    return ("direction", wmas[i])
            for num in verbs:
                if num == wmas[i]:
                    return ("verb", wmas[i])
            for num in st_words:
                if num == wmas[i]:
                    return ("stop word", wmas[i])
            for num in nouns:
                if num == wmas[i]:
                    return ("verb", wmas[i])
            for num in numbers:
                if num == wmas[i]:
                    return ("number", wmas[i])
            i+=1
            
    

