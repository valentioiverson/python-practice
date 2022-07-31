def minion_game(string):
    # your code goes here
    vowel = ['A', 'E', 'I', 'O', 'U']
    score_kevin = 0
    score_stuart = 0
    for i in range(len(string)):
        if string[i] in vowel:
            score_kevin += (len(string) - i)
        else:
            score_stuart += (len(string) - i)
    if score_kevin > score_stuart:
        print("Kevin " + str(score_kevin))
    elif score_stuart > score_kevin: 
        print("Stuart " + str(score_stuart))
    else:
        print("Draw")
        
