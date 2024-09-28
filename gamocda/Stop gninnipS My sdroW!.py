def spin_words(sentence):
    result = ' '
    for x in sentence.split():
        if len(x) < 5:
            result.join(x)
        if len(x) >= 5:
            result.join(x[::-1])
    return result