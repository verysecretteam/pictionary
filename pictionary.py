import random

from bottle import route, run, template


idx = 0
words = []


def load_words(word_file):
    f = open(word_file, "r")
    for word in f:
        words.append(word.strip())
    random.shuffle(words)


def draw_word():
    global idx
    if idx >= len(words):
        random.shuffle(words)
        idx = 0
        return "No more words left, starting over!"

    word = words[idx]
    idx += 1
    return word


@route("/")
def index():
    word = draw_word()
    return template("<h1>{{word}}</h1>", word=word)


def main():
    load_words("./words.txt")
    run(reloader=True, host="0.0.0.0", port=8082)


if __name__ == "__main__":
    main()
