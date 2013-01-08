class Base(object):
  def __eq__(self, other):
    return self is other or hasattr(other, "__dict__") and self.__dict__ == other.__dict__

def setProperties(self, **kwargs):
  for name, val in kwargs.items():
    setattr(self, name, val)


class EnumValue(object):
  def __init__(self, *args, **kwargs):
    self._id = type(self).nextId()
    self.args = args
    self.kwargs = kwargs

  _id = 0

  @classmethod
  def nextId(cls):
    cls._id +=1
    return cls._id

# Establish enums based on
class EnumMeta(type):
  def __init__(cls, name, bases, dct):
    cls.values = []
    values = [(name, value) for name, value in dct.items() if isinstance(value, EnumValue)]
    values.sort(key = lambda (key, val): val._id)

    for name, value in values:
      cls.resolveAttrs(value)

      value.actual = actual = cls(*value.args, **value.kwargs)
      actual._name = name

      cls.values.append(actual)
      setattr(cls, name, actual)

  @classmethod
  def resolveAttr(cls, val):
    return val.actual if isinstance(val, EnumValue) else val

  @classmethod
  def resolveAttrs(cls, enumValue):
    enumValue.kwargs = dict((name, cls.resolveAttr(val)) for (name, val) in enumValue.kwargs.items())
    enumValue.args = map(cls.resolveAttr, enumValue.args)

class Enum(object):
  __metaclass__ = EnumMeta

  def __repr__(self):
    return "<"+ type(self).__name__ + ":" + self._name + ">"

  def __str__(self):
    return "<"+ type(self).__name__ + ":" + self._name + ">"


