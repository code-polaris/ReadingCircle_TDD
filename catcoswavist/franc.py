from money import Money
class Franc:
    def __init__(self,amount:int) -> int:
        # amount関数のprivate化
        # Javaは同一のクラスであれば別インスタンスのprivateフィールドにアクセスできる。
        # ~~Pythonは同一のクラス別インスタンスのprivateフィールドにアクセスできない？~~
        # -> 躓きの原因はインデントだった。@propertyは def __init__()の列
        self.__amount = amount
        # 【疑問】kalen573さんの拝見 デコレータ@propertyをなぜ使うか疑問
        # 【疑問】アンダースコア(_)1個？2個？
 
    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier:int):
        return Franc(self.__amount*multiplier)
    
    def equals(self,other):
        franc = other
        return self.__amount == franc.amount