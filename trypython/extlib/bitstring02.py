# coding: utf-8

"""
bitstringモジュールに関するサンプルです。

BitArray.prepend()
BitArray.append()

について
"""
import bitstring as bs

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------------
        # BitArray には、前後にビットを付与できる
        # メソッドが存在する。
        #
        # 前方に付与するのが prepend()
        # 後方に付与するのが append()
        #
        # どちらのメソッドも破壊的変更を加える。
        # (つまり対象オブジェクト自身が変更される)
        # ----------------------------------------------

        # ----------------------------------------------
        # 1ビットだけの BitArray を生成
        # ----------------------------------------------
        # BitArrayのコンストラクタに数値を指定すると
        # そのサイズのビットを持つ BitArray が生成できる
        # ----------------------------------------------
        # 値は　uint で　0 (0x00) となる
        # ----------------------------------------------
        ba01 = bs.BitArray(1)
        pr('ba01.bin', ba01.bin)
        pr('ba01.uint', ba01.uint)

        # ----------------------------------------------
        # prepend を使用して、前に 3ビット(0b100) 分追加
        # ----------------------------------------------
        # 値 uint で 8 (0x08) となる
        # ----------------------------------------------
        ba01.prepend('0b100')
        pr('ba01.bin', ba01.bin)
        pr('ba01.hex', ba01.hex)
        pr('ba01.uint', ba01.uint)

        # ----------------------------------------------
        # append を使用して、前に 4ビット(0b1111) 分追加
        # ----------------------------------------------
        # 値 uint で 143 (0x8F) となる
        # ----------------------------------------------
        ba01.append('0b1111')
        pr('ba01.bin', ba01.bin)
        pr('ba01.hex', ba01.hex)
        pr('ba01.uint', ba01.uint)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
