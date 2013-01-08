from utilities import Enum, EnumValue

class BrowserType(Enum):

  def __init__(self, name):
    self.name = name

  ##
  # Standard web-browser
  ##
  WEB_BROWSER = EnumValue("Browser")

  ##
  # Special web-browser for mobile devices
  ##
  MOBILE_BROWSER = EnumValue("Browser (mobile)")

  ##
  # Text only browser like the good old Lynx
  ##
  TEXT_BROWSER = EnumValue("Browser (text only)")

  ##
  # Email client like Thunderbird
  ##
  EMAIL_CLIENT = EnumValue("Email Client")

  ##
  # Search robot, spider, crawler,...
  ##
  ROBOT = EnumValue("Robot")

  ##
  # Downloading tools
  ##
  TOOL = EnumValue("Downloading tool")

  UNKNOWN = EnumValue("unknown")
