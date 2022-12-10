all_scores = input('Please enter all the scores you want checked: \n').split()

high_score = 0 
for scores in all_scores:
    if int(scores) > high_score:
        high_score = int(scores)

print(str(high_score))