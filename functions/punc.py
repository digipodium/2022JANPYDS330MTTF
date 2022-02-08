# function that remove all the punctuation from a text

from string import punctuation

# text = "hello*(@#&) w!:#{}orld@#!..."
# for p in punctuation:
#     text = text.replace(p,'')
# print(text)

def clean_text(text):
    for p in punctuation:
        text = text.replace(p,'')
    return text

sample_text ="I {}{}am coding functions **** @@ ..." 
cleaned_text = clean_text(sample_text)

print(sample_text)
print(cleaned_text)