import random

alphabets = "abcdefghijklmnopqrstuvwxyz "
alpha_list=list(alphabets)
target_sentence='methinks it is like a weasel'
closest_sentence=""
hightest_score=0

def get_sentence_score(sentence):
    score =0
    for i in range(len(sentence)):
        if sentence[i]==target_sentence[i]:
            score+=1

    return (1.0*score/len(sentence))*100

def get_random_sentence():
    random_sentence=""
    for i in range(len(target_sentence)):
        random_sentence+=random.choice(alpha_list)
    return  random_sentence


while hightest_score!=100:
    for i in range(10000):
        sentence=get_random_sentence()
        score=get_sentence_score(sentence)
        if hightest_score<score:
            closest_sentence=sentence
            hightest_score=score
            print("The closest sentence is %s which is %.2f percent similar to the target sentence %s" % (
            closest_sentence, hightest_score, target_sentence))


