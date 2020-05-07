ls = []
while len(ls) <= 5:
    def low_t(text):
        for i in range(len(text)):
            ls.append(text[i][0:1].title() + text[i][1:])
        return ' '.join(ls)
    print(low_t(input('Input text, to quit type more than 5 words: ').split()))
