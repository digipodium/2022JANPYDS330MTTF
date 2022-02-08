from string import punctuation

def punc_remover(text):
    for p in punctuation:
        text = text.replace(p,'')
    return text

def escape_char_remover(text):
    esc = ['\n','\t','\r',]
    for e in esc:
        text = text.replace(e,'')
    return text

def emoji_remover(text):
    return text

