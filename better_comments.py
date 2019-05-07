import random

WORD_LIST = [[
    "This", "The", "Wow!, This", "Nice! This", "Your", 
    "Nice! Your", "Wow, that", "That", "Nice! That"
],

["picture", "pic", "feed", "post", "shot"],

["looks", "is", "is quite"],

[
    "amazing", "great", "well composed", "beautiful", "fantastic", 
    "remarkable", "terrific", "impressive", "phenomenal",
    "charming", "good", "satisfying", "astonishing",
    "lovely", "on point", "fire", "amazing.",
    "great, keep it up", "well composed", 
    "beautiful", "fantastic, keep it up", "remarkable",
    "terrific, keep it up", "impressive", "phenomenal, keep it up",
    "charming", "good, keep it up", "astonishing, keep it up", 
    "lovely, keep it up", "amazing, great job",
    "beautiful", "fantastic, great job", "remarkable",
    "impressive", "phenomenal, great job", "charming, great job",
    "good, great job", "satisfying, great job",
    "astonishing", "lovely, great job"
],

[ 
    ".", "!", "!!", "!!!", ". :-)", "! :-)", ". <3", "! <3",
    "!!! =^_^=", ". (*_*)", "=D", ":')", " ;)", "!! ;-)",
    "!! O_o", ".. O_O", "! ^_^"
]]

def create_comment(sentence, num):
    comments = []
    for i in range(num):
        comments.append(( ' '.join([random.choice(word) for word in sentence])))
    return comments

if __name__ == "__main__":
    print(create_comment(WORD_LIST, 25))
   
