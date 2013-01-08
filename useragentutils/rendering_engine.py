from utilities import Enum, EnumValue

class RenderingEngine(Enum):
  def __init__(self, name):
    self.name = name

  ##
  # Trident is the the Microsoft layout engine, mainly used by Internet Explorer.
  ##
  TRIDENT = EnumValue("Trident")

  ##
  # HTML parsing and rendering engine of Microsoft Office Word, used by some other products of the Office suite instead of Trident.
  ##
  WORD = EnumValue("Microsoft Office Word")

  ##
  # Open source and cross platform layout engine, used by Firefox and many other browsers.
  ##
  GECKO = EnumValue("Gecko")

  ##
  # Layout engine based on KHTML, used by Safari, Chrome and some other browsers.
  ##
  WEBKIT = EnumValue("WebKit")

  ##
  # Proprietary layout engine by Opera Software ASA
  ##
  PRESTO = EnumValue("Presto")

  ##
  # Original layout engine of the Mozilla browser and related products. Predecessor of Gecko.
  ##
  MOZILLA = EnumValue("Mozilla")

  ##
  # Layout engine of the KDE project
  ##
  KHTML = EnumValue("KHTML")

  ##
  # Other or unknown layout engine.
  ##
  OTHER = EnumValue("Other")
