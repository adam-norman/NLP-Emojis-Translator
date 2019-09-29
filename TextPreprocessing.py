import emoji
import codecs


y=[]

def Translate_emojis(line):
    compiledtext = ''
    for c in line:
        if c in emoji.UNICODE_EMOJI:
            compiledtext += ' ' + emoji.demojize(c)+' '
        else:
            compiledtext += c
    for w in compiledtext.split():
        if w not in y:
            y.append(w)
    return compiledtext



file = open("Training.txt", encoding='utf-16', errors='ignore')
x=''
print('Step1 has been started')
for line in file.readlines():
    x +=Translate_emojis(line)


print('Step1 has been finished')
file = codecs.open("Words.txt", "w", "utf-16")


print('Step2 has been started')
for Word in y:
    file.write(Word+'\n')



print('Step2 has been finished')
file = codecs.open("TrainingTranslated.txt", "w", "utf-16")
file.write(x)
file.close()


print('done')
