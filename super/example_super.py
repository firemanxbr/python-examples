r"""
Example using the super function

Gain access to inherited methods

Shows the ordered resolution:
    help(SubY)

  A
 / \
B   X
 \ /
  Y

Method resolution order:
    SubY
    SubB
    SubX
    ParentA
    __builtin__.object
"""
class ParentA(object):
    """
    Parent Class A
    """
    def method_foo(self):
        """
        Method of Parent Class A
        """
        print('AAA')

class SubB(ParentA):
    """
    Sub Class B
    """
    def method_bar(self):
        """
        Method of Sub Class B
        """
        super(SubB, self).method_foo()
        print('BBB')

class SubX(ParentA):
    """
    Sub Class X
    """
    def method_foo(self):
        """
        Method of Sub Class X
        """
        print('XXX')

class SubY(SubB, SubX):
    """
    Sub Class Y
    """
    pass


if __name__ == "__main__":
    SubY().method_bar()
