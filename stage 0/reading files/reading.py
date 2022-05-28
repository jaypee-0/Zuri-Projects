def read_file_content(filename):
    txt = open(filename)
    return txt.read()


def count_words():
    text = read_file_content("story.txt")
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(count_words())