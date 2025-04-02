# -*- coding: utf-8 -*-
from functools import reduce
import re

text = """
На краю дороги стоял дуб. Вероятно, в десять раз старше берез, составлявших лес, он был в десять раз толще и в два раза выше каждой березы. Это был огромный в два обхвата дуб с обломанными, давно видно, суками и с обломанной корой, заросшей старыми болячками. С огромными своими неуклюжими, несимметрично-растопыренными  корявыми руками и пальцами, он старым, сердитым и презрительным уродом стоял между улыбающимися березами. Только он один не хотел подчиняться обаянию весны и не хотел видеть ни весны, ни солнца.

 "Весна, и любовь, и счастие!" - как будто говорил этот дуб. - И как не надоест вам все один и тот же глупый и бессмысленный обман. Все одно и то же, и все обман! Нет ни весны, ни солнца, ни счастья. Вон смотрите, сидят задавленные мертвые ели, всегда одинокие, и вон и я растопырил свои обломанные, ободранные пальцы, где ни выросли они - из спины, из боков; как выросли - так и стою, и не верю вашим надеждам и обманам".

 Князь Андрей несколько раз оглянулся на этот дуб, проезжая по лесу, как будто он чего-то ждал от него. Цветы и трава были и под дубом, но он все так же, хмурясь, неподвижно, уродливо и упорно, стоял посреди их.

 "Да, он прав, тысячу раз прав этот дуб, - думал князь Андрей, пускай другие, молодые, вновь поддаются на этот обман, а мы знаем жизнь, - наша жизнь кончена!" Целый новый ряд мыслей безнадежных, но грустно-приятных в связи с этим дубом, возник в душе князя Андрея. Во время этого путешествия он как будто вновь обдумал всю свою жизнь, и пришел к тому же прежнему успокоительному и безнадежному заключению, что ему начинать ничего было не надо, что он должен доживать свою жизнь, не делая зла, не тревожась и ничего не желая.

Встреча князя Андрея Болконского с дубом

"Да, здесь, в этом лесу был этот дуб, с которым мы были согласны,-  подумал князь Андрей. - Да где он",- подумал опять князь Андрей, глядя на левую сторону дороги и, сам того не зная, не узнавая его, любовался тем дубом, которого он искал. Старый дуб, весь преображенный, раскинувшись шатром сочной, темной зелени, млел, чуть колыхаясь в лучах вечернего солнца. Ни корявых пальцев, ни болячек, ни старого недоверия и горя - ничего не было видно. Сквозь жесткую, столетнюю кору пробились без сучков сочные, молодые листья, так что верить нельзя было, что этот старик произвел их. "Да  это тот самый дуб", -  подумал князь Андрей, и на него вдруг нашло беспричинное  весеннее чувство радости и обновления. Все лучшие минуты его жизни вдруг в одно и то же время вспомнились ему. И Аустерлиц с высоким небом, и мертвое, укоризненное лицо жены, и Пьер на пароме, и девочка, взволнованная красотою ночи, и эта ночь, и луна - и все это вдруг вспомнилось ему.

 "Нет, жизнь не кончена в 31 год,- вдруг окончательно, беспеременно решил князь Андрей. Мало того, что я знаю все то, что есть во мне, надо, чтобы и все знали это: и Пьер, и эта девочка, которая хотела улететь в небо, надо, чтобы все знали меня, чтобы не для одного меня шла моя жизнь, чтоб не жили они так независимо от моей жизни, чтоб на всех она отражалась и чтобы все они жили со мною вместе!"

https://www.chitalnya.ru/work/3450353/ """
# разделение на слова
cleaned_words = list(
    map(lambda word: re.sub(r'[^\w\s]', '', word.lower()), text.split())
)

# ф. количество каждого слова
def word_count(acc, word):
    if word in acc:
        acc[word] += 1
    else:
        acc[word] = 1
    return acc

#подсчета слов
word_counts = reduce(word_count, cleaned_words, {})
# top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[10:20]
print("от 10 до 20 наиболее встречающихся слов и их количество:")
for word, count in top_words:
    print(f"{word}: {count}")
