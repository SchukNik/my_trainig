def single_root_words(root_word, *other_words):
    same_words =[]
    new_root_word = root_word.lower()
    new_other_words = [x.lower() for x in other_words]
    for i in range(len(other_words)):
        if new_root_word in new_other_words[i]:
            same_words.append(other_words[i])
        elif new_other_words[i] in new_root_word:
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)