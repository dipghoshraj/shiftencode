def ascii_(words):
    word_list = []
    for word_ in words:
        word_list.append(ord(word_))
    return word_list

def avgsalt(words):
    avg_values = 0
    for keyword in words:
        avg_values = avg_values + ord(str(keyword))
    avg_value = int(avg_values/len(words))
    return avg_value

    