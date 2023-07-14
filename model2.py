#py38
from janome.tokenizer import Tokenizer
import markovify
from typing import List

def text_cleansing(text2):
    # 改行、スペース、問題を起こす文字の置換
    table2 = str.maketrans({
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
    text2 = text2.translate(table2)

    t = Tokenizer()
    result2 = t.tokenize(text2, wakati=True)
    result2 = list(result2)
    # 1単語毎に間に半角スペース、文末には改行を挿入
    splitted_text2 = ""
    for i in range(len(result2)):
        splitted_text2 += result2[i]
        if result2[i] != '。' and result2[i] != '！' and result2[i] != '？':
            splitted_text2 += ' '
        else:
            splitted_text2 += '\n'
    return splitted_text2

def praise():
    cnt=1
    result_praise=[]

    while cnt<11:
        with open('データ集め - お褒め.txt', mode='r', encoding='utf-8') as f:
            text2 = f.read()

        # テキストを単語毎に分割して記号を除去
        splitted_text2 = text_cleansing(text2)

        # データセットの量が不足していると確率でnoneが返ってくるので、生成結果が返るまでループさせる
        sentence2 = None
        while sentence2 == None:
            # モデル生成
            text2_model = markovify.NewlineText(splitted_text2, state_size=2)
            # モデルから文章を生成
            sentence2 = text2_model.make_sentence(tries=120)
        sentence2 = str(sentence2).replace(' ','')
        sentence2 = sentence2.translate(str.maketrans({'.': '。', '！': None, ' ': None}))

        result_praise.append(sentence2)
        print(cnt)
        cnt+=1
    print(result_praise)
    
    return result_praise

# with open('sentence2.txt', mode='a') as f:
#     f.write(sentence2.replace(' ', ''))