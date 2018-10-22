import re
import string


def count_clusters(filename, length):

    if length <= 0:
        print "length must be at least 1"
        return {}

    regex = re.compile('[%s]' % re.escape(string.punctuation))

    with open(filename) as f:
        text = f.read().lower()
    text = regex.sub('', text)
    words = text.split()

    counts = {}

    word_map = {}
    for i in range(length):
        word_map[i] = words[i:]

    current_cluster = []
    for index, word in enumerate(words):
            if index + length > len(words):
                break
            current_cluster.append(word)
            for i in range(1, length):
                current_cluster.append(words[index+i])
            current_string = " ".join(current_cluster)
            print(current_string)
            current_cluster =  []
            if current_string in counts:
                counts[current_string] += 1
            else:
                counts[current_string] = 1

    return counts

def main():
    from sys import argv
    filename = argv[1]
    length = int(argv[2])

    counts = count_clusters(filename, length)
    print counts

if __name__ == '__main__':
    main()

