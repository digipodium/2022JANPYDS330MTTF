from utils import punc_remover, escape_char_remover

text = 'i am a \rstring!@(*#)\t() wi!@#th data \n'
ctext = escape_char_remover(punc_remover(text))
print(ctext)