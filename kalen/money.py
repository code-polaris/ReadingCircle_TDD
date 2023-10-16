
# reduceメソッドを統合するためにExpressionインターフェイスに
# アブストラクトメソッドで設定

from abc import ABC, abstractmethod
class Expression(ABC):

    @abstractmethod
    def reduce(self, to: str):
        pass

# ---------------------
# reduceメソッドを強制
class Bank:
    def reduce(self, source: Exception, to: str):
        if type(source) is Money:
            return source

        sum = source
        return sum.reduce(to)
    
    def reduce(self, source: Exception, to: str):
        return source.reduce(to)


# ---------------------

class Sum(Expression):
    def __init__(self, augend, addend):
        self.__augend = augend
        self.__addend = addend
    @property
    def augend(self):
        return self.__augend
    @property
    def addend(self):
        return self.__addend
    
    def reduce(self, to):
        amount = self.__augend.amount + self.__addend.amount
        return Money(amount, to)
    
# ---------------------

class Money(Expression):
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
    
    @property
    def currency(self):
        return self.__currency

    @property
    def amount(self):
        return self.__amount
    
    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")

    def __eq__(self, object) -> bool:
        return self.__dict__ == object.__dict__
        #return self.amount == object.amount and self.currency == object.currency

    def __add__(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
        
    # reduceメソッドを強制
    def reduce(self, to: str):
        return self