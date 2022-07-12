import zope.interface

class BaseI(zope.interface.Interface):
    def m1(self, x):
        pass

    def m2(self):
        pass

class DerivedI(BaseI):
    def m3(self, x, y):
        pass

@zope.interface.implementer(DerivedI)
class cls:
    def m1(self, z):
        return z ** 3

    def m2(self):
        return 'foo'

    def m3(self, x, y):
        return x ^ y