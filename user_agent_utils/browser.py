from utilities import Enum, EnumValue, setProperties
from manufacturer import Manufacturer
from rendering_engine import RenderingEngine
from browser_type import BrowserType

class Browser(Enum):

  def __init__(self, manufacturer, parent, versionId, name, aliases, exclude, browserType, renderingEngine, versionRegexString):
    setProperties(**locals())

  OPERA = EnumValue(      Manufacturer.OPERA, None, 1, "Opera", [ "Opera" ], None, BrowserType.WEB_BROWSER, RenderingEngine.PRESTO, "Opera\\/(([\\d]+)\\.([\\w]+))")   # before MSIE
  OPERA_MINI = EnumValue(   Manufacturer.OPERA, OPERA, 20, "Opera Mini", [ "Opera Mini"], None, BrowserType.MOBILE_BROWSER, RenderingEngine.PRESTO, None) # Opera for mobile devices
  ##
  # For some strange reason Opera uses 9.80 in the user-agent string and otherwise it is very inconsistent. Use the getVersion method if you really want to know which version it is.
  ##
  OPERA10 = EnumValue(    Manufacturer.OPERA, OPERA, 10, "Opera 10", [ "Opera/9.8" ], None, BrowserType.WEB_BROWSER, RenderingEngine.PRESTO, "Version\\/(([\\d]+)\\.([\\w]+))")
  OPERA9 = EnumValue(     Manufacturer.OPERA, OPERA, 5, "Opera 9", [ "Opera/9" ], None, BrowserType.WEB_BROWSER, RenderingEngine.PRESTO, None)
  KONQUEROR = EnumValue(    Manufacturer.OTHER, None, 1, "Konqueror", [ "Konqueror"], None, BrowserType.WEB_BROWSER, RenderingEngine.KHTML, "Konqueror\\/(([0-9]+)\\.?([\\w]+)?(-[\\w]+)?)" )

  ##
  # Outlook email client
  ##
  OUTLOOK = EnumValue(  Manufacturer.MICROSOFT, None, 100, "Outlook", ["MSOffice"], None, BrowserType.EMAIL_CLIENT, RenderingEngine.WORD, "MSOffice (([0-9]+))") # before IE7
  ##
  # Microsoft Outlook 2007 identifies itself as MSIE7 but uses the html rendering engine of Word 2007.
  # Example user agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; .NET CLR 1.1.4322; MSOffice 12)
  ##
  OUTLOOK2007 = EnumValue(  Manufacturer.MICROSOFT, OUTLOOK, 107, "Outlook 2007", ["MSOffice 12"], None, BrowserType.EMAIL_CLIENT, RenderingEngine.WORD, None) # before IE7
  ##
  # Outlook 2010 is still using the rendering engine of Word. http:#www.fixoutlook.org
  ##
  OUTLOOK2010 = EnumValue(  Manufacturer.MICROSOFT, OUTLOOK, 108, "Outlook 2010", ["MSOffice 14"], None, BrowserType.EMAIL_CLIENT, RenderingEngine.WORD, None) # before IE7

  ##
  # Family of Internet Explorer browsers
  ##
  IE = EnumValue(       Manufacturer.MICROSOFT, None, 1, "Internet Explorer", [ "MSIE"], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, "MSIE (([\\d]+)\\.([\\w]+))" ) # before Mozilla
  ##
  # Since version 7 Outlook Express is identifying itself. By detecting Outlook Express we can not
  # identify the Internet Explorer version which is probably used for the rendering.
  # Obviously this product is now called Windows Live Mail Desktop or just Windows Live Mail.
  ##
  OUTLOOK_EXPRESS7 = EnumValue( Manufacturer.MICROSOFT, IE, 110, "Windows Live Mail", ["Outlook-Express/7.0"], None, BrowserType.EMAIL_CLIENT, RenderingEngine.TRIDENT, None) # before IE7, previously known as Outlook Express. First released in 2006, offered with different name later
  ##
  # Since 2007 the mobile edition of Internet Explorer identifies itself as IEMobile in the user-agent.
  # If previous versions have to be detected, use the operating system information as well.
  ##
  IEMOBILE9 = EnumValue(    Manufacturer.MICROSOFT, IE, 123, "IE Mobile 9", [ "IEMobile/9" ], None, BrowserType.MOBILE_BROWSER, RenderingEngine.TRIDENT, None) # before MSIE strings
  IEMOBILE7 = EnumValue(    Manufacturer.MICROSOFT, IE, 121, "IE Mobile 7", [ "IEMobile 7" ], None, BrowserType.MOBILE_BROWSER, RenderingEngine.TRIDENT, None) # before MSIE strings
  IEMOBILE6 = EnumValue(    Manufacturer.MICROSOFT, IE, 120, "IE Mobile 6", [ "IEMobile 6" ], None, BrowserType.MOBILE_BROWSER, RenderingEngine.TRIDENT, None) # before MSIE
  IE10 = EnumValue(     Manufacturer.MICROSOFT, IE, 92, "Internet Explorer 10", [ "MSIE 10" ], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, None )   # before MSIE
  IE9 = EnumValue(      Manufacturer.MICROSOFT, IE, 90, "Internet Explorer 9", [ "MSIE 9" ], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, None )   # before MSIE
  IE8 = EnumValue(      Manufacturer.MICROSOFT, IE, 80, "Internet Explorer 8", [ "MSIE 8" ], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, None )   # before MSIE
  IE7 = EnumValue(      Manufacturer.MICROSOFT, IE, 70, "Internet Explorer 7", [ "MSIE 7" ], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, None)   # before MSIE
  IE6 = EnumValue(      Manufacturer.MICROSOFT, IE, 60, "Internet Explorer 6", [ "MSIE 6" ], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, None )   # before MSIE
  IE5_5 = EnumValue(      Manufacturer.MICROSOFT, IE, 55, "Internet Explorer 5.5", [ "MSIE 5.5" ], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, None) # before MSIE
  IE5 = EnumValue(      Manufacturer.MICROSOFT, IE, 50, "Internet Explorer 5", [ "MSIE 5" ], None, BrowserType.WEB_BROWSER, RenderingEngine.TRIDENT, None ) # before MSIE

  ##
  # Google Chrome browser
  ##
  CHROME = EnumValue(     Manufacturer.GOOGLE, None, 1, "Chrome", [ "Chrome" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, "Chrome\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)" ) # before Mozilla
  CHROME19 = EnumValue(     Manufacturer.GOOGLE, CHROME, 24, "Chrome 19", [ "Chrome/19" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME18 = EnumValue(     Manufacturer.GOOGLE, CHROME, 23, "Chrome 18", [ "Chrome/18" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME17 = EnumValue(     Manufacturer.GOOGLE, CHROME, 22, "Chrome 17", [ "Chrome/17" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME16 = EnumValue(     Manufacturer.GOOGLE, CHROME, 21, "Chrome 16", [ "Chrome/16" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME15 = EnumValue(     Manufacturer.GOOGLE, CHROME, 20, "Chrome 15", [ "Chrome/15" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME14 = EnumValue(     Manufacturer.GOOGLE, CHROME, 19, "Chrome 14", [ "Chrome/14" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME13 = EnumValue(     Manufacturer.GOOGLE, CHROME, 18, "Chrome 13", [ "Chrome/13" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME12 = EnumValue(     Manufacturer.GOOGLE, CHROME, 17, "Chrome 12", [ "Chrome/12" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME11 = EnumValue(     Manufacturer.GOOGLE, CHROME, 16, "Chrome 11", [ "Chrome/11" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME10 = EnumValue(     Manufacturer.GOOGLE, CHROME, 15, "Chrome 10", [ "Chrome/10" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME9 = EnumValue(    Manufacturer.GOOGLE, CHROME, 10, "Chrome 9", [ "Chrome/9" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla
  CHROME8 = EnumValue(    Manufacturer.GOOGLE, CHROME, 5, "Chrome 8", [ "Chrome/8" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None ) # before Mozilla



  OMNIWEB = EnumValue(    Manufacturer.OTHER, None, 2, "Omniweb", [ "OmniWeb" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None) #

  SAFARI = EnumValue(     Manufacturer.APPLE, None, 1, "Safari", [ "Safari" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, "Version\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)" )  # before AppleWebKit
  CHROME_MOBILE = EnumValue(  Manufacturer.GOOGLE, SAFARI, 100, "Chrome Mobile", [ "CrMo" ], None, BrowserType.MOBILE_BROWSER, RenderingEngine.WEBKIT, "CrMo\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)" )
  MOBILE_SAFARI = EnumValue(  Manufacturer.APPLE, SAFARI, 2, "Mobile Safari", [ "Mobile Safari","Mobile/" ], None, BrowserType.MOBILE_BROWSER, RenderingEngine.WEBKIT, None )  # before Safari
  SILK = EnumValue(     Manufacturer.AMAZON, SAFARI, 15, "Silk", [ "Silk/" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, "Silk\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\-[\\w]+)?)" )  # http:#en.wikipedia.org/wiki/Amazon_Silk
  SAFARI5 = EnumValue(    Manufacturer.APPLE, SAFARI, 3, "Safari 5", [ "Version/5" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None )  # before AppleWebKit
  SAFARI4 = EnumValue(    Manufacturer.APPLE, SAFARI, 4, "Safari 4", [ "Version/4" ], None, BrowserType.WEB_BROWSER, RenderingEngine.WEBKIT, None )  # before AppleWebKit

  DOLFIN2 = EnumValue(    Manufacturer.SAMSUNG, None, 1, "Samsung Dolphin 2", [ "Dolfin/2" ], None, BrowserType.MOBILE_BROWSER, RenderingEngine.WEBKIT, None ) # webkit based browser for the bada os

  APPLE_MAIL = EnumValue(   Manufacturer.APPLE, None, 50, "Apple Mail", [ "AppleWebKit" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.WEBKIT, None) # Microsoft Entrourage/Outlook 2010 also only identifies itself as AppleWebKit
  LOTUS_NOTES = EnumValue(  Manufacturer.OTHER, None, 3, "Lotus Notes", [ "Lotus-Notes" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.OTHER, "Lotus-Notes\\/(([\\d]+)\\.([\\w]+))")  # before Mozilla

  ##
  # Thunderbird email client, based on the same Gecko engine Firefox is using.
  ##
  THUNDERBIRD = EnumValue(  Manufacturer.MOZILLA, None, 110, "Thunderbird", [ "Thunderbird" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, "Thunderbird\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)" )  # using Gecko Engine
  THUNDERBIRD12 = EnumValue(  Manufacturer.MOZILLA, THUNDERBIRD, 185, "Thunderbird 12", [ "Thunderbird/12" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine
  THUNDERBIRD11 = EnumValue(  Manufacturer.MOZILLA, THUNDERBIRD, 184, "Thunderbird 11", [ "Thunderbird/11" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine
  THUNDERBIRD10 = EnumValue(  Manufacturer.MOZILLA, THUNDERBIRD, 183, "Thunderbird 10", [ "Thunderbird/10" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine
  THUNDERBIRD8 = EnumValue(   Manufacturer.MOZILLA, THUNDERBIRD, 180, "Thunderbird 8", [ "Thunderbird/8" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine
  THUNDERBIRD7 = EnumValue(   Manufacturer.MOZILLA, THUNDERBIRD, 170, "Thunderbird 7", [ "Thunderbird/7" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine
  THUNDERBIRD6 = EnumValue(   Manufacturer.MOZILLA, THUNDERBIRD, 160, "Thunderbird 6", [ "Thunderbird/6" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine
  THUNDERBIRD3 = EnumValue(   Manufacturer.MOZILLA, THUNDERBIRD, 130, "Thunderbird 3", [ "Thunderbird/3" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine
  THUNDERBIRD2 = EnumValue(   Manufacturer.MOZILLA, THUNDERBIRD, 120, "Thunderbird 2", [ "Thunderbird/2" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.GECKO, None )  # using Gecko Engine

  CAMINO = EnumValue(     Manufacturer.OTHER, None, 5, "Camino", [ "Camino" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, "Camino\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)" )  # using Gecko Engine
  CAMINO2 = EnumValue(    Manufacturer.OTHER, CAMINO, 17, "Camino 2", [ "Camino/2" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FLOCK = EnumValue(      Manufacturer.OTHER, None, 4, "Flock", ["Flock"], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, "Flock\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)")

  FIREFOX = EnumValue(    Manufacturer.MOZILLA, None, 10, "Firefox", [ "Firefox" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, "Firefox\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)")  # using Gecko Engine
  FIREFOX3MOBILE = EnumValue( Manufacturer.MOZILLA, FIREFOX, 31, "Firefox 3 Mobile", [ "Firefox/3.5 Maemo" ], None, BrowserType.MOBILE_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX13 = EnumValue(    Manufacturer.MOZILLA, FIREFOX, 94, "Firefox 13", [ "Firefox/13" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX12 = EnumValue(    Manufacturer.MOZILLA, FIREFOX, 93, "Firefox 12", [ "Firefox/12" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX11 = EnumValue(    Manufacturer.MOZILLA, FIREFOX, 92, "Firefox 11", [ "Firefox/11" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX10 = EnumValue(    Manufacturer.MOZILLA, FIREFOX, 91, "Firefox 10", [ "Firefox/10" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX9 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 90, "Firefox 9", [ "Firefox/9" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX8 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 80, "Firefox 8", [ "Firefox/8" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX7 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 70, "Firefox 7", [ "Firefox/7" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX6 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 60, "Firefox 6", [ "Firefox/6" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX5 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 50, "Firefox 5", [ "Firefox/5" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX4 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 40, "Firefox 4", [ "Firefox/4" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX3 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 30, "Firefox 3", [ "Firefox/3" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX2 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 20, "Firefox 2", [ "Firefox/2" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine
  FIREFOX1_5 = EnumValue(   Manufacturer.MOZILLA, FIREFOX, 15, "Firefox 1.5", [ "Firefox/1.5" ], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, None )  # using Gecko Engine

  SEAMONKEY = EnumValue(    Manufacturer.OTHER, None, 15, "SeaMonkey", ["SeaMonkey"], None, BrowserType.WEB_BROWSER, RenderingEngine.GECKO, "SeaMonkey\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)") # using Gecko Engine

  BOT = EnumValue(      Manufacturer.OTHER, None,12, "Robot/Spider", ["Googlebot","bot", "spider", "crawler", "Feedfetcher", "Slurp", "Twiceler", "Nutch", "BecomeBot"], None, BrowserType.ROBOT, RenderingEngine.OTHER, None)

  MOZILLA = EnumValue(    Manufacturer.MOZILLA, None, 1, "Mozilla", [ "Mozilla", "Moozilla" ], None, BrowserType.WEB_BROWSER, RenderingEngine.OTHER, None) # rest of the mozilla browsers

  CFNETWORK = EnumValue(    Manufacturer.OTHER, None, 6, "CFNetwork", [ "CFNetwork" ], None, BrowserType.UNKNOWN, RenderingEngine.OTHER, None ) # Mac OS X cocoa library

  EUDORA = EnumValue(     Manufacturer.OTHER, None, 7, "Eudora", [ "Eudora", "EUDORA" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.OTHER, None )  # email client by Qualcomm

  POCOMAIL = EnumValue(   Manufacturer.OTHER, None, 8, "PocoMail", [ "PocoMail" ], None, BrowserType.EMAIL_CLIENT, RenderingEngine.OTHER, None )

  THEBAT = EnumValue(     Manufacturer.OTHER, None, 9, "The Bat!", ["The Bat"], None, BrowserType.EMAIL_CLIENT, RenderingEngine.OTHER, None) # Email Client

  NETFRONT = EnumValue(   Manufacturer.OTHER, None, 10, "NetFront", ["NetFront"], None, BrowserType.MOBILE_BROWSER, RenderingEngine.OTHER, None) # mobile device browser

  EVOLUTION = EnumValue(    Manufacturer.OTHER, None, 11, "Evolution", ["CamelHttpStream"], None, BrowserType.EMAIL_CLIENT, RenderingEngine.OTHER, None) # http:#www.go-evolution.org/Camel.Stream

  # Strange regex, not worth investigating.
  #LYNX = EnumValue(     Manufacturer.OTHER, None, 13, "Lynx", ["Lynx"], None, BrowserType.TEXT_BROWSER, RenderingEngine.OTHER, "Lynx\\/(([0-9]+)\\.([\\d]+)\\.?([\\w-+]+)?\\.?([\\w-+]+)?)")

  DOWNLOAD = EnumValue(     Manufacturer.OTHER, None, 16, "Downloading Tool", ["cURL","wget"], None, BrowserType.TEXT_BROWSER, RenderingEngine.OTHER, None)

  UNKNOWN = EnumValue(    Manufacturer.OTHER, None, 14, "Unknown", [], None, BrowserType.UNKNOWN, RenderingEngine.OTHER, None )


