#this will be a function that'll take a list of words as an argument and in for a new list via looping and searching the minimum word

def sort(word_list):
    words = word_list.split(" ")
    res = []
    
    min = words[0]
    max = words[0]
    
    while len(res) < len(words):
        for i in range(0, len(words)):
            if words[i] < min:
                if words[i] not in res:
                    min = words[i]
        res.append(min)
        
        for i in range(0, len(words)):
            if words[i] > max:
                    max = words[i]
        min = max

    print res

sort ('bob zorg rodrik akana pedro cedric')

