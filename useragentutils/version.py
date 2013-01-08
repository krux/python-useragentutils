import utilities as util

class Version(util.Base):
  __metaclass__ = type

  def __init__(self, version, majorVersion, minorVersion):
    self.version = version
    self.majorVersion = majorVersion
    self.minorVersion = minorVersion

  def __str__(self):
    return self.version

  def __repr__(self):
    return "<"+ type(self).__name__ + ":" + self.majorVersion + "." + self.minorVersion + ">"

