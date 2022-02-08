from os import sep


def word_counter(paragraph,sep=' '):
    words = paragraph.split(sep)
    return len(words)

print(word_counter("I am working"))

print(word_counter('red,green,yellow',sep=','))
