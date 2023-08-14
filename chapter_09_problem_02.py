def game():
    return 100
score=game()
with open("High_score.txt") as f:
    High_score_str=(f.read())
if  High_score_str=='':
    with open ("High_score.txt","w") as f:
        f.write(str(score))
elif int (High_score_str) <score :
    with open ("High_score.txt","w") as f:
        f.write(str(score))
# In starting i have entered 100 in High_score.txt but now it has been updated to 105.
# If the name.txt file does not contain anything then it will store the record(score)