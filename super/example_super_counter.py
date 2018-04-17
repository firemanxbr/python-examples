r"""
Example using the super function in the real life

Shows the ordered resolution:
    help(OCounter)

       dict
      /    \
Counter  OrderedDict
      \    /
     OCounter

Method resolution order:
    OCounter
    collections.Counter
    collections.OrderedDict
    __builtin__.dict
    __builtin__.object
"""
from collections import Counter, OrderedDict


class OCounter(Counter, OrderedDict):
    """
    Changing the ordered resolution
    """
    pass


if __name__ == "__main__":
    print('Default: {}'.format(Counter('python').keys()))
    print('Ordered: {}'.format(OCounter('python').keys()))
