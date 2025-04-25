import sys

def make():
    graph = {}
    with open("translations.csv", "r") as file:
        for line in file:
            lang1, word1, lang2, word2 = line.strip().split(",")
            key1 = (lang1, word1)
            key2 = (lang2, word2)

            if key1 not in graph:
                graph[key1] = []
            if key2 not in graph:
                graph[key2] = []

            graph[key1].append(key2)
            graph[key2].append(key1)  
    return graph

def vocab(lang):
    words = set()
    with open("translations.csv", "r") as file:
        for line in file:
            lang1, word1, lang2, word2 = line.strip().split(",")
            if lang1 == lang:
                words.add(word1)
            if lang2 == lang:
                words.add(word2)
    result = sorted(list(words), reverse=True)
    print(result)

def all_translations(lang1, lang2, graph):
    translations = set()
    visited = set()

    for (l, w) in graph:
        if l == lang1:
            queue = [((l, w), [])]
            visited.clear()
            visited.add((l, w))
            while queue:
                (curr_lang, curr_word), path = queue.pop(0)
                path = path + [(curr_lang, curr_word)]
                if curr_lang == lang2 and (curr_lang, curr_word) != (l, w):
                    translations.add((path[0][1], curr_word))
                    break
                for neighbor in graph.get((curr_lang, curr_word), []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path))
    return sorted(translations)

def translate_word(lang1, lang2, word, graph):
    queue = [(lang1, word)]
    visited = set()
    visited.add((lang1, word))

    while queue:
        current = queue.pop(0)
        curr_lang, curr_word = current
        if curr_lang == lang2 and curr_word != word:
            return curr_word
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return "UNK"

if __name__ == "__main__":
    query_type = sys.argv[1]
    graph = make()
    if query_type == "1":
        vocab(sys.argv[2])
    elif query_type == "2":
        lang1, lang2 = sys.argv[2], sys.argv[3]
        result = all_translations(lang1, lang2, graph)
        print(result)
    elif query_type == "3":
        lang1, lang2, word = sys.argv[2], sys.argv[3], sys.argv[4]
        result = translate_word(lang1, lang2, word, graph)
        print(result)
