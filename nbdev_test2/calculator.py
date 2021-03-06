# AUTOGENERATED! DO NOT EDIT! File to edit: 00_calculator.ipynb (unless otherwise specified).

__all__ = ['Calculator']

# Cell
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def __str__(self):
        return 'currently holding {} and {} numbers'.format(self.a, self.b)

    def __repr__(self):
        return self.__str__()