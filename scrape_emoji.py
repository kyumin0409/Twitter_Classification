import emoji

emojiLabels={}

def text_has_emoji(text):
    emojiExists=False
    for character in text:
        if character in emoji.UNICODE_EMOJI:
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
