import emoji
import re

data_path = './app_data/brexit/brexit_data.txt'
data_path2 = './app_data/brexit/brexit_data2.txt'

#\S: nonwhitespace, (): capture, \1: match first capture, *: 0 or more prev element, +: 1 or more prev element, []: shorthand OR, {2,}: repeat prev 2 or more
url_reg = re.compile(r'\S*(https|www)\S*')
query_reg = re.compile(r'\S*[bB]rexit\S*')
username_reg = re.compile(r'\S*@\S+')
repeat_reg = re.compile(r'(\w)\1{2,}')

#Create Emoji regex, re.escape to match string literally, even if contains regex
emoji_list = emoji.UNICODE_EMOJI.keys()
emoji_list = sorted(emoji_list, key=len, reverse=True)
emoji_reg = re.compile(r'(?:\S*{}\S*)'.format('|'.join(map(re.escape, emoji_list))))

#Load in entire file as single string
with open(data_path, "r",  encoding="utf-8") as f:
    content = f.read()
#Use regex objects to substitute terms
content = emoji_reg.sub('EMOJI_TERM', content)
content = query_reg.sub('QUERY_TERM', content)
content = url_reg.sub('URL_TERM', content)
content = username_reg.sub('USERNAME_TERM', content)
content = repeat_reg.sub(r'\1\1', content)

with open(data_path2, "w+",  encoding="utf-8") as f:
    f.write(content)


#emoji_test =  'efef👩\u200d❤️\u200d💋\u200d👨 fehiofhif feoifh 👨💋 efefef 👨\u200d👨\u200d👦\u200d👦efef \n'
#url_test = "I love you (https:/feoihfeih) https:efhioeihf www.bob.com bobbbb \n"
#query_test = "Brexit filfeBrexit bbbBrexit feoifhe brexitww\n"
#username_test = "@harmon @fefe @ fff@feoihfoie\n"
#repeat_test = 'I lOOOve pieeeeeee mmmmmmmdd\n'