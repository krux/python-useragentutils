from utilities import Enum, EnumValue


class RenderingEngine(Enum):
    def __init__(self, name):
        self.name = name

    ##
    # Trident is the the Microsoft layout engine, mainly used by Internet Explorer.
    ##
    TRIDENT = EnumValue('Trident')

    ##
    # EdgeHTML is a proprietary layout engine developed for the Microsoft Edge web browser
    # Trident fork
    ##
    EDGEHTML = EnumValue('EdgeHTML')

    ##
    # HTML parsing and rendering engine of Microsoft Office Word, used by some other products of the Office suite
    # instead of Trident.
    ##
    WORD = EnumValue('Microsoft Office Word')

    ##
    # Open source and cross platform layout engine, used by Firefox and many other browsers.
    ##
    GECKO = EnumValue('Gecko')

    ##
    # Layout engine based on KHTML, used by Safari, Chrome and some other browsers.
    ##
    WEBKIT = EnumValue('WebKit')

    ##
    # Proprietary layout engine by Opera Software ASA
    ##
    PRESTO = EnumValue('Presto')

    ##
    # Original layout engine of the Mozilla browser and related products. Predecessor of Gecko.
    ##
    MOZILLA = EnumValue('Mozilla')

    ##
    # Layout engine of the KDE project
    ##
    KHTML = EnumValue('KHTML')

    ##
    # Layout engine for Chrome and Opera from 2013 onwards
    ##
    BLINK = EnumValue('Blink')

    ##
    # Other or unknown layout engine.
    ##
    OTHER = EnumValue('Other')
