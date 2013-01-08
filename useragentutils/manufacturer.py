from utilities import Enum, EnumValue

class Manufacturer(Enum):

  def __init__(self, id, name):
    self.id = id
    self.name = name

  ##
  # Unknow or rare manufacturer
  ##
  OTHER = EnumValue(1, "Other")
  ##
  # Microsoft Corporation
  ##
  MICROSOFT = EnumValue(2, "Microsoft Corporation")
  ##
  # Apple Inc.
  ##
  APPLE = EnumValue(3, "Apple Inc.")
  ##
  # Sun Microsystems, Inc.
  ##
  SUN = EnumValue(4, "Sun Microsystems, Inc.")
  ##
  # Symbian Ltd.
  ##
  SYMBIAN = EnumValue(5, "Symbian Ltd.")
  ##
  # Nokia Corporation
  ##
  NOKIA = EnumValue(6, "Nokia Corporation")
  ##
  # Research In Motion Limited
  ##
  BLACKBERRY = EnumValue(7, "Research In Motion Limited")
  ##
  # Hewlett-Packard Company, previously Palm
  ##
  HP = EnumValue(8, "Hewlet Packard")
  ##
  # Sony Ericsson Mobile Communications AB
  ##
  SONY_ERICSSON = EnumValue(9, "Sony Ericsson Mobile Communications AB")
  ##
  # Samsung Electronics
  ##
  SAMSUNG = EnumValue(20, "Samsung Electronics")
  ##
  # Sony Computer Entertainment, Inc.
  ##
  SONY = EnumValue(10, "Sony Computer Entertainment, Inc.")
  ##
  # Nintendo
  ##
  NINTENDO = EnumValue(11, "Nintendo")
  ##
  # Opera Software ASA
  ##
  OPERA = EnumValue(12, "Opera Software ASA")
  ##
  # Mozilla Foundation
  ##
  MOZILLA = EnumValue(13, "Mozilla Foundation")
  ##
  # Google Inc.
  ##
  GOOGLE = EnumValue(15, "Google Inc.")
  ##
  # CompuServe Interactive Services, Inc.
  ##
  COMPUSERVE = EnumValue(16, "CompuServe Interactive Services, Inc.")
  ##
  # Yahoo Inc.
  ##
  YAHOO = EnumValue(17, "Yahoo Inc.")
  ##
  # AOL LLC.
  ##
  AOL = EnumValue(18, "AOL LLC.")
  ##
  # Mail.com Media Corporation
  ##
  MMC = EnumValue(19, "Mail.com Media Corporation")
  ##
  # Amazon.com, Inc.
  ##
  AMAZON = EnumValue(20, "Amazon.com, Inc.")
  ##
  # Roku sells home digital media products
  ##
  ROKU = EnumValue(21, "Roku, Inc.");
