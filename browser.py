class Base(object):
  def __eq__(self, other):
    return self is other or self.__dict__ == other.__dict__



def setProperties(self, **kwargs):
  for name, val in kwargs.items():
    setattr(self, name, val)


class EnumValue(object):
  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs

# Establish enums based on
class EnumMeta(type):
  def __init__(cls, name, bases, dct):
    cls.values = {}
    for name, value in dct.items():
      if isinstance(value, EnumValue):
        cls.resolveAttrs(value.kwargs)

        value.actual = actual = cls(*value.args, **value.kwargs)
        actual.name = name
        cls.values[name] = actual
        setattr(cls, name, actual)

  @classmethod
  def resolveAttrs(cls, attrs):
    for name, val in attrs.items():
      if isinstance(val, EnumValue):
        attrs[name] = val.actual



class Enum(object):
  __metaclass__ = EnumMeta

  def __repr__(self):
    return "<"+ type(self).__name__ + ":" + self.name + ">"


class Version(Base):
  __metaclass__ = type

  def __init__(self, version, majorVersion, minorVersion):
    self.version = version
    self.majorVersion = majorVersion
    self.minorVersion = minorVersion

  def __str__(self):
    return self.version





class Browser(Enum):
  def __init__(self, label, a=1, b=7, c=3, d=4):
    setProperties(**locals())

  IE = EnumValue("fever", a=16)

  IE6 = EnumValue("fever 6", a=2, b=IE)


print(Browser.IE6.__dict__)
