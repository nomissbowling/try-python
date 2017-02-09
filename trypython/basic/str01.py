# coding: utf-8

"""
str についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, unicode_width


class Sample(SampleBase):
    def exec(self):
        #
        # Python 2 と 3 で大きく異なるのが文字列
        # Python 2 では、ascii と unicode が明確に別れていたのが
        # Python 3 から 標準が unicode となった。
        #
        # 文字列型は、大量のメソッドを持っている
        #
        str01 = 'hello world'

        #
        # 文字列は 文字 の シーケンス でもある
        #
        for c in str01:
            pr('chr', c)

        #
        # シーケンスなのでインデックスアクセス可能
        #
        pr('2文字目', str01[1])

        #
        # 文字列はイミュータブル
        #
        try:
            str01[1] = 'z'
        except TypeError as e:
            pr('文字列はイミュータブル', e)

        #
        # unicode なのでasciiと日本語ではバイト数が異なる
        #
        str02 = 'abcde'
        str03 = 'ＡＢＣＤＥ'

        pr('asciiのbyte-length', unicode_width(str02))
        pr('日本語含む場合のbyte-length', unicode_width(str03))

        # でも len() は文字数を返すので同じとなる
        pr('len(str02)', len(str02))
        pr('len(str03)', len(str03))

        #
        # 文字列に * 演算子 で繰り返しを行える
        #
        pr('*演算子', str01 * 2)

        #
        # スライスは リスト等と同様
        # [start:end:step]
        #
        pr('スライス', str01[2:10:2])

        #
        # capitalize()
        # 先頭を大文字にする
        #
        pr('capitalize()', str01.capitalize())

        #
        # casefold()
        # 大文字小文字に関係ないマッチに利用できる文字列を返す
        #
        pr('casefold()', 'HELLo WoRLd'.casefold())

        #
        # center()
        # 中央寄せ
        #
        pr('center()', str01.center(15))

        #
        # count()
        # 指定した部分文字列のカウントを返す
        #
        pr('count()', str01.count('o'))

        #
        # encode()
        # 指定したエンコーディングの bytes オブジェクトを返す
        #
        pr('encode() -- utf-8', str03.encode('utf-8'))
        pr('encode() -- sjis', str03.encode('sjis'))

        #
        # endswith()
        # 指定した部分文字列で終わっているかどうか
        #
        pr('endswith()', str01.endswith('ld'))

        #
        # expandtabs()
        # 文字列中のタブをスペースに置換した文字列を返す
        #
        str04 = 'hello\twor\tld'
        pr('expandtabs()', str04.expandtabs(tabsize=4))

        #
        # find()
        # 指定した部分文字列に合致する最初のインデックスを返す
        # 見つからなかった場合、-1 を返す
        #
        pr('find()', str01.find('wo'))

        #
        # format()
        # 書式化文字列を理解して変換して返す
        # 書式化文字列については
        #   https://docs.python.jp/3/library/string.html#formatstrings
        # を参照。
        #
        str05 = 'text is {0}'
        pr('format()', str05.format(str01))

        #
        # index()
        # find() と同じ挙動をするが、見つからなかった場合に
        # 例外を発生させる
        #
        try:
            str01.index('notexists')
        except ValueError as e:
            pr('index()', e)

        #
        # 以下の関数については省略（使ったことがない）
        #
        # isalnum(), isalpha(), isdecimal(), isdigit()
        # isidentifier(), islower(), isnumeric(), isprintable()
        # isspace(), istitle(), isupper(), maketrans(), translate()
        #

        #
        # join()
        # 指定したシーケンスを結合した文字列を返す
        # シーケンスの中身は文字列でないと例外が発生する
        #
        pr('join()', ','.join(str(x) for x in range(10)))

        #
        # ljust()
        # 指定した長さの左揃えの文字列を返す
        #
        pr('ljust()', str01.ljust(15, '*'))

        #
        # lower()
        # 小文字にする
        #
        str06 = 'HELLO WORLD'
        pr('lower()', str06.lower())

        #
        # lstrip()
        # 文字列の先頭の文字を除去した文字列を返す
        #
        str07 = bin(1000)
        pr('lstrip()', str07.lstrip('0b'))

        #
        # partition()
        # 指定した文字列の最初の出現位置で区切り、その前後と区切った部分を返す
        #
        pr('partition()', str01.partition(' '))

        #
        # replace()
        # 指定したパターンを指定した文字列で置換する
        #
        pr('replace()', str01.replace('world', 'WORLD'))

        #
        # rfind()
        # find() の 逆側から検索を行うバージョン
        #
        # 省略

        #
        # rindex()
        # index() の 逆側から検索を行うバージョン
        #
        # 省略

        #
        # rjust()
        # 指定した長さの右揃えの文字列を返す
        #
        pr('rjust()', str01.rjust(15, '*'))

        #
        # rpartition()
        # partition() の 最後の出現位置で区切るバージョン
        #
        # 省略

        #
        # rsplit()
        # split() の 右側から処理を行うバージョン
        #
        # 省略

        #
        # rstrip()
        # lstrip() の右側バージョン
        #
        # 省略

        #
        # split()
        # 指定した部分文字列で区切ったリストを返す
        #
        pr('split()', str01.split(' '))

        #
        # splitlines()
        # 文字列を改行で区切ったリストを返す
        #
        str08 = 'hello world\ntest message\nhello world'
        pr('splitlines()', str08.splitlines())

        #
        # startswith()
        # 指定した文字列で始まっているかを判定
        #
        pr('startswith()', str01.startswith('he'))

        #
        # strip()
        # lstrip() + rstrip()
        #
        pr('strip() -- original', str01.center(20))
        pr('strip()', str01.center(20).strip())

        #
        # swapcase()
        # 大文字は小文字に、小文字は大文字に変換される
        #
        pr('swapcase()', str01.swapcase())

        #
        # title()
        # 文字列を、単語ごとに大文字から始まり、残りの文字のうち大小文字の区別があるものは全て小文字にする
        # この関数は、全角に対しても動作する
        #
        pr('title()', 'ａｂｃｄｅ ｆｇ'.title())

        #
        # upper()
        # 大文字にする
        #
        pr('upper()', str01.upper())

        #
        # zfill()
        # 指定したサイズになるよう '0' を左側に埋める
        # 先頭文字が符号(+ or -)の場合は、その後ろに埋める
        #
        pr('zfill()', '100'.zfill(5))
        pr('zfill() -- 先頭が符号', '-100'.zfill(5))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
