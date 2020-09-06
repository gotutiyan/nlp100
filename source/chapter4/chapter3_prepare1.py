import MeCab
tagger = MeCab.Tagger()
text_info = []
data = open('neko.txt', "r").read()
out = open('neko_mecab.txt', "w")
out.write(tagger.parse(data))

    

