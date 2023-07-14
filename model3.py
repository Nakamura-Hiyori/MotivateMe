from janome.tokenizer import Tokenizer
import markovify

def text_cleansing(text3):
    # 改行、スペース、問題を起こす文字の置換
    table3 = str.maketrans({
        '。': '.',
        '\n': '',
        '\r': '',
        '…': '',
        '、': '',
        '々': '',
        '「': '',
        '」': '.',
        '(': '（',
        ')': '）',
        '[': '［',
        ']': '］',
        '"': '”',
        "'": "’",
    })
    text3 = text3.translate(table3)

    t = Tokenizer()
    result3 = t.tokenize(text3, wakati=True)
    result3 = list(result3)
    # 1単語毎に間に半角スペース、文末には改行を挿入
    splitted_text3 = ""
    for i in range(len(result3)):
        splitted_text3 += result3[i]
        if result3[i] != '。' and result3[i] != '！' and result3[i] != '？':
            splitted_text3 += ' '
        else:
            splitted_text3 += '\n'
    return splitted_text3

def love():
    cnt=1
    result_love=[]

    while cnt<11:
        with open('データ集め - ときめき.txt', mode='r', encoding='utf-8') as f:
            text3 = f.read()

# テキストを単語毎に分割して記号を除去
        splitted_text3 = text_cleansing(text3)

# データセットの量が不足していると確率でnoneが返ってくるので、生成結果が返るまでループさせる
        sentence3 = None
        while sentence3 == None:
            # モデル生成
            text3_model = markovify.Text(splitted_text3, state_size=2)
            # モデルから文章を生成
            sentence3 = text3_model.make_sentence(tries=150)
        sentence3 = str(sentence3).replace(' ','')
        sentence3 = sentence3.translate(str.maketrans({'.': '。', '！': None, ' ': None}))

        result_love.append(sentence3)
        print(cnt)
        cnt+=1
    print(result_love)
    
    return result_love

# with open('sentence3.txt', mode='a') as f:
#     f.write(sentence3.replace(' ', ''))