from utilities import Base
from browser import Browser
from operating_system import OperatingSystem

class UserAgent(Base):
  def __init__(self, userAgentString):
    self.userAgentString = userAgentString
    self.browser = Browser.parseUserAgentString(userAgentString)

    self.operatingSystem = OperatingSystem.UNKNOWN
    if browser is not Browser.BOT:
      self.operatingSystem = OperatingSystem.parseUserAgentString(userAgentString)

