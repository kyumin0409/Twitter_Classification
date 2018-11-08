import emoji

emojiLabels={}

notEmojis = ['\U0001f9d0','\U0001f92e','\U0001f92f','\U0001f9e1','\U0001f92c','\U0001f92a','\U0001f91f','\U0001f928',
               '\U0001f92b','\U0001f929','\U0001f931','\U0001f6f8','\U0001f92d','\U0001f9da','\U0001f995','\U0001f9e0',
               '\U0001f9d1','\U0001f9d8', '\U0001f96a', '\U0001f96b','\U0001f9d9','\U0001f9d5','\U0001f9dd','\U0001f996']

def text_has_emoji(text):
    emojiExists=False
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            if character not in notEmojis:
                emojiExists=True
                if character not in emojiLabels:
                    emojiLabels[character]=''
    if(emojiExists==True):
        d.write(text)
        d.write('\n')
    return emojiLabels
 
d = open('/Users/aisirimurulidhar/Downloads/ireland_tweetsCopy.txt', "a")
with open('/Users/aisirimurulidhar/Downloads/ireland_tweets.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]     
    
for c in content:
    text_has_emoji(c)

positiveEmojis = ['👍','😊','😆','😄','⭐','😁', '😇','♥', '🙏','💖','😃','😆','🤑','🥂', '😛','👍', '👋', '😍','💖','🌚','🙌', '🗳', '🙋','👏','💜','😊','❤', '😀', '💕', '✅', '☘',
                 '💚', '✨','💘', '😉', '👐','🤗', '😂','🤣','🤗', '😏','💓', '💝', '💟','👼', '🎶', '🌈', '🐣', '✌', '👌',
                 '😃','🎉','🤝', '🖤','😘','🖐', '❣', '😙', '💃','😄','😆','💙','😎','😁','💞','💛', '💗',
                 '🤓','😋', '😜','🙂','✔','🌻','☺', '🤙','🌸','🌺','☘','🌟','😺','😌','😹','🎈', '😚','👯','💍', '👰',
                 '😻','😇','☝', '🐥', '🍻', '🥇','💸','🎓','😛', '😝', '🌷','😸','🌼', '🎂', '🎁','🏆','🏅','💐', '🤸',
                 '🍾', '😳','🍺','💌','🌝','🤕','🤒','😺','💯','😋','🍻','😻']
negativeEmojis = ['😠', '😦','😔','😐','😑','😨','😖','🚫','😩','☹','😪','😣','😦','🤐','😾','😒','😫','😟', '💔','🙁','😧','👹','🚨','🙃','🙄','😱','😡', '😢','😥','🤦','😞','☠', '💀','😬','😣','😭', '😑','😠','😓',
                 '😷', '👎', '🖐','😕','😖','😔', '😯','😶','🙀', '😨','☹', '🖕','🔥','😤','😲','😰','😕', '✋',
                 '👹', '⬇', '🤚','❎','🤢','😐','👿','😈','🤐','😪','✖','🙁', '😵','🤧','🤥', '😮', '👺','⚠', '😟','🤕',
                 '😫','🤒','🐍','💣','😿', '🎊','🥀','😷','😶']


for key in emojiLabels.keys():
    if key in positiveEmojis:
        emojiLabels[key]='Positive'
    elif key in negativeEmojis:
        emojiLabels[key]='Negative'

with open('/Users/aisirimurulidhar/Downloads/ireland_tweetsCopy.txt') as m:   #change file name here
        content = m.readlines()
content = [x.strip() for x in content]
    
tweetAndLabel={}
    
for c in content: 
    for character in c:
        if character in emoji.UNICODE_EMOJI:
            if character not in notEmojis:
                if emojiLabels[character]=='Positive':
                    tweetAndLabel[c]='Positive'
                elif emojiLabels[character]=='Negative':
                    tweetAndLabel[c]='Negative'

with open('/Users/aisirimurulidhar/Downloads/ireland_tweetsCopy.txt') as m:   #change file name here
        content = m.readlines()
content = [x.strip() for x in content]
    
tweetAndLabel={}
    
n = open('/Users/aisirimurulidhar/Downloads/ireland_tweets_labeled.txt', "a")
    
for c in content: 
    for character in c:
        if character in emoji.UNICODE_EMOJI:
            if character not in notEmojis:
                if emojiLabels[character]=='Positive':
                    tweetAndLabel[c]='Positive'
                elif emojiLabels[character]=='Negative':
                    tweetAndLabel[c]='Negative'

for x in tweetAndLabel:
    n.write(x + " : " + tweetAndLabel[x] + "\n")
