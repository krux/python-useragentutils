from utilities import Enum, EnumValue

class DeviceType(Enum):
  def __init__(self, name):
    self.name = name

  #
  # Standard desktop or laptop computer
  #
  COMPUTER = EnumValue("Computer")
  #
  # Mobile phone or similar small mobile device
  #
  MOBILE = EnumValue("Mobile")
  #
  # Small tablet type computer.
  #
  TABLET = EnumValue("Tablet")
  #
  # Game console like the Wii or Playstation.
  #
  GAME_CONSOLE = EnumValue("Game console")
  #
  # Digital media receiver like the Google TV.
  #
  DMR = EnumValue("Digital media receiver")
  #
  # Other or unknow type of device.
  #
  UNKNOWN = EnumValue("Unknown");

