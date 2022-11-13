from rake_nltk import Rake

r = Rake()
f = open('text.txt', 'r', encoding='utf8')
text = f.read()
f.close()
print(text)
r.extract_keywords_from_text(text)


def printWithoutScores():
    result = r.get_ranked_phrases()
    while result:
        print(result.pop() + '\n')


def printWithScores():
    result = r.get_ranked_phrases_with_scores()[::-1]
    while result:
        print(result.pop())


printWithScores()
