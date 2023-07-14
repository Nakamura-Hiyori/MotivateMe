#py38
from janome.tokenizer import Tokenizer
import markovify
from typing import List

def text_cleansing(text1):
    # 改行、スペース、問題を起こす文字の置換
    table1 = str.maketrans({
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
    text1 = text1.translate(table1)

    t = Tokenizer()
    result1 = t.tokenize(text1, wakati=True)
    result1 = list(result1)
    # 1単語毎に間に半角スペース、文末には改行を挿入
    splitted_text1 = ""
    for i in range(len(result1)):
        splitted_text1 += result1[i]
        if result1[i] != '。' and result1[i] != '！' and result1[i] != '？':
            splitted_text1 += ' '
        else:
            splitted_text1 += '\n'
    return splitted_text1

def cheer():
    cnt=1
    result_cheer=[]

    while cnt<11:
        with open('データ集め - 励まし・慰め.txt', mode='r', encoding='utf-8') as f:
            text1 = f.read()

        # テキストを単語毎に分割して記号を除去
        splitted_text1 = text_cleansing(text1)

        # データセットの量が不足していると確率でnoneが返ってくるので、生成結果が返るまでループさせる
        sentence1 = None
        while sentence1 == None:
            # モデル生成
            text1_model = markovify.Text(splitted_text1, state_size=3)
            # モデルから文章を生成
            sentence1 = text1_model.make_sentence(tries=70)
        sentence1 = str(sentence1).replace('..','.')
        sentence1 = sentence1.translate(str.maketrans({'.': '。', '！': None, ' ': None}))
        # json_sentence = "{'id': '"+str(cnt)+"','cheer': '"+sentence1+"'}"
        result_cheer.append(sentence1)
        print(cnt)
        cnt+=1
    # result_cheer = list(map(str,sentence1.split(',|.')))
    print(result_cheer)
    
    # with open('sentence1.txt', mode='a') as f:
    #     f.write(sentence1.replace(' ', ''))
    return result_cheer