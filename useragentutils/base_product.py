from utilities import Enum, EnumValue, setProperties
from version import Version
import re

# Find any of the values in array of strings, case insensitive.
def rgxFindAnyCaseInsensitive(arr):
  arr = arr or []
  return re.compile('|'.join(map(re.escape, arr)), re.I)

class BaseProduct(Enum):
  required = ["manufacturer", "parent", "versionId", "name", "aliases", "exclude", "versionRegexString"]

  def __init__(self, **kwargs):
    required = self.required
    required.extend(BaseProduct.required)

    for arg in required:
      if not arg in kwargs:
        raise Exception("Missing required arg: " + arg)

    setProperties(self, **kwargs)
    self.id = (self.manufacturer.id << 8) + self.versionId
    self.children = []
    if self.parent:
      self.parent.children.append(self)
    self._versionRegEx = re.compile(self.versionRegexString) if self.versionRegexString else None

    # find any alias, case-insensitive
    self.aliasRgx = rgxFindAnyCaseInsensitive(self.aliases)
    if self.exclude:
      self.excludeRgx = rgxFindAnyCaseInsensitive(self.exclude)

  @property
  def group(self):
    return self.parent.group if self.parent else self

  @property
  def versionRegEx(self):
    if self._versionRegEx:
      return self._versionRegEx
    if self.group is not self:
      return self.group.versionRegEx
    return None

  def version(self, userAgentString):
    pattern = self.versionRegEx
    if userAgentString and pattern:
      match = pattern.search(userAgentString)
      if match:
        full, major = match.group(1, 2)
        minor = match.group(3) if len(match.groups()) > 2 else "0"
        return Version(full, major, minor)

  def isInUserAgentString(self, userAgentString):
    return self.aliasRgx.search(userAgentString)

  def containsExcludeToken(self, userAgentString):
    if hasattr(self, 'excludeRgx'):
      return self.excludeRgx.search(userAgentString)

  def checkUserAgent(self, userAgentString):
    if self.isInUserAgentString(userAgentString):
      for child in self.children:
        value = child.checkUserAgent(userAgentString)
        if value:
          return value
      if not self.containsExcludeToken(userAgentString):
        return self

  @classmethod
  def parseUserAgentString(self, userAgentString):
    for value in self.values:
      if not value.parent:
        value = value.checkUserAgent(userAgentString)
        if value:
          return value
    return self.UNKNOWN

