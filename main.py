from heapq import nlargest

words_dict = {}
N = 10

with open("text.txt") as file:
    file1 = file.read()
    file2 = file1.replace("â€™", "").replace(".", "").replace(",", "").replace("~", "").replace("$", "")
    file3 = file2.replace("-", "").replace("?", "").replace("â€”", " ").replace("(", "").replace(")", "")
    file4 = file3.split()
    for word in file4:
        if len(word) == 1 or len(word) == 2 or len(word) == 3:
            pass
        else:
            count = file3.count(word.lower())
            if word.lower() in words_dict:
                pass
            else:
                words_dict[word] = count

    res = nlargest(N, words_dict, key=words_dict.get)

    for word in res:
        print(f"{word}: {words_dict[word]}")
file.close()

# print(words_dict)
