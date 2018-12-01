import emoji
import os 

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

def text_has_emoji(file):
    d = open(directory + '/' + file.split('.')[0]+'emoji.txt', "a")
    print(directory + '/' + file.split('.')[0]+'emoji.txt')
    with open(directory + '/'+ file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]     
    for text in content:
        emojiExists=False
        for character in text:
            if character in positiveEmojis or character in negativeEmojis:
                emojiExists=True
        if(emojiExists==True):
            d.write(text)
            d.write('\n')
    return str(file)
 
directory = '/Users/aisirimurulidhar/Downloads/585FinalProject-master 2/app_data/tweets_by_keyword'    
for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        text_has_emoji(filename)
