from base_product import BaseProduct
from manufacturer import Manufacturer
from device_type import DeviceType
from utilities import EnumValue

class OperatingSystem(BaseProduct):
  required = ["deviceType"]

  # replace
  #  (.*?)\(\s*(.*?),\s*(.*?),\s*(.*?),\s*(.*?),\s*(.*?\}),\s*(.*?),\s*(.*?),\s*(.*)\),[ ]*(.*)
  #  $10\n  $1 = EnumValue(\n    manufacturer = $2,\n    parent = $3,\n    versionId = $4,\n    name = $5,\n    aliases = $6,\n    exclude = $7,\n    deviceType = $8,\n    versionRegexString = $9)\n

  # replace
  #new String\[\] \{(.*?)\}
  #[$1]



  # catch the rest of older Windows systems (95, NT,...)
  WINDOWS = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = None,
    versionId = 1,
    name = "Windows",
    aliases = [ "Windows" ],
    exclude = [ "Palm" ],
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )

  # before Win, yes, Windows 7 is called 6.1 LOL
  WINDOWS_7 = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = WINDOWS,
    versionId = 21,
    name = "Windows 7",
    aliases = [ "Windows NT 6.1" ],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )

  # before Win
  WINDOWS_VISTA = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = WINDOWS,
    versionId = 20,
    name = "Windows Vista",
    aliases = [ "Windows NT 6" ],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )

  # before Win
  WINDOWS_2000 = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = WINDOWS,
    versionId = 15,
    name = "Windows 2000",
    aliases = [ "Windows NT 5.0" ],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )

  # before Win, 5.1 and 5.2 are basically XP systems
  WINDOWS_XP = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = WINDOWS,
    versionId = 10,
    name = "Windows XP",
    aliases = [ "Windows NT 5" ],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )

  # before Win
  WINDOWS_MOBILE7 = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = WINDOWS,
    versionId = 51,
    name = "Windows Mobile 7",
    aliases = [ "Windows Phone OS 7" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  # before Win
  WINDOWS_MOBILE = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = WINDOWS,
    versionId = 50,
    name = "Windows Mobile",
    aliases = [ "Windows CE" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  # before Win
  WINDOWS_98 = EnumValue(
    manufacturer = Manufacturer.MICROSOFT,
    parent = WINDOWS,
    versionId = 5,
    name = "Windows 98",
    aliases = [ "Windows 98","Win98" ],
    exclude = [ "Palm" ],
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )



  ANDROID = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = None,
    versionId = 0,
    name = "Android",
    aliases = [ "Android" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  #
  # First Android 4 device is the Galaxy Nexus phone. Once there are also Tablets with Android 4 we we will have to find a solution to distinguish between mobile phones and tablets.
  #

  ANDROID4 = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = ANDROID,
    versionId = 4,
    name = "Android 4.x",
    aliases = [ "Android 4","Android-4" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  ANDROID4_TABLET = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = ANDROID4,
    versionId = 40,
    name = "Android 4.x Tablet",
    aliases = [ "Xoom", "Transformer" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )

  # as long as there are not Android 3.x phones this should be enough
  ANDROID3_TABLET = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = ANDROID,
    versionId = 30,
    name = "Android 3.x Tablet",
    aliases = [ "Android 3" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )


  ANDROID2 = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = ANDROID,
    versionId = 2,
    name = "Android 2.x",
    aliases = [ "Android 2" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  ANDROID2_TABLET = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = ANDROID2,
    versionId = 20,
    name = "Android 2.x Tablet",
    aliases = [ "Kindle Fire", "GT-P1000","SCH-I800" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )


  ANDROID1 = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = ANDROID,
    versionId = 1,
    name = "Android 1.x",
    aliases = [ "Android 1" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  #
  # PalmOS, exact version unkown
  #

  WEBOS = EnumValue(
    manufacturer = Manufacturer.HP,
    parent = None,
    versionId = 11,
    name = "WebOS",
    aliases = [ "webOS" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  PALM = EnumValue(
    manufacturer = Manufacturer.HP,
    parent = None,
    versionId = 10,
    name = "PalmOS",
    aliases = [ "Palm" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )



  #
  # iOS4, with the release of the iPhone 4, Apple renamed the OS to iOS.
  #
  # before MAC_OS_X_IPHONE for all older versions
  IOS = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = None,
    versionId = 2,
    name = "iOS",
    aliases = [ "like Mac OS X" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  # before MAC_OS_X_IPHONE for all older versions
  iOS5_IPHONE = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = IOS,
    versionId = 42,
    name = "iOS 5 (iPhone)",
    aliases = [ "iPhone OS 5" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  # before MAC_OS_X_IPHONE for all older versions
  iOS4_IPHONE = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = IOS,
    versionId = 41,
    name = "iOS 4 (iPhone)",
    aliases = [ "iPhone OS 4" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  # before Mac OS X
  MAC_OS_X_IPAD = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = IOS,
    versionId = 50,
    name = "Mac OS X (iPad)",
    aliases = [ "iPad" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )

  # before Mac OS X
  MAC_OS_X_IPHONE = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = IOS,
    versionId = 40,
    name = "Mac OS X (iPhone)",
    aliases = [ "iPhone" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  # before Mac OS X
  MAC_OS_X_IPOD = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = IOS,
    versionId = 30,
    name = "Mac OS X (iPod)",
    aliases = [ "iPod" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  # before Mac
  MAC_OS_X = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = None,
    versionId = 10,
    name = "Mac OS X",
    aliases = [ "Mac OS X" , "CFNetwork"],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )


  #
  # Older Mac OS systems before Mac OS X
  #
  # older Mac OS systems
  MAC_OS = EnumValue(
    manufacturer = Manufacturer.APPLE,
    parent = None,
    versionId = 1,
    name = "Mac OS",
    aliases = [ "Mac" ],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )


  #
  # Linux based Maemo software platform by Nokia. Used in the N900 phone. http:#maemo.nokia.com/
  #

  MAEMO = EnumValue(
    manufacturer = Manufacturer.NOKIA,
    parent = None,
    versionId = 2,
    name = "Maemo",
    aliases = [ "Maemo" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  #
  # Bada is a mobile operating system being developed by Samsung Electronics.
  #

  BADA = EnumValue(
    manufacturer = Manufacturer.SAMSUNG,
    parent = None,
    versionId = 2,
    name = "Bada",
    aliases = [ "Bada" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


    #
    #  Google TV uses Android 2.x or 3.x but doesn't identify itself as Android.
    #

  GOOGLE_TV = EnumValue(
    manufacturer = Manufacturer.GOOGLE,
    parent = None,
    versionId = 100,
    name = "Android (Google TV)",
    aliases = [ "GoogleTV" ],
    exclude = None,
    deviceType = DeviceType.DMR,
    versionRegexString = None )


  #
  # Various Linux based operating systems.
  #

  KINDLE = EnumValue(
    manufacturer = Manufacturer.AMAZON,
    parent = None,
    versionId = 1,
    name = "Linux (Kindle)",
    aliases = [ "Kindle" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )


  KINDLE3 = EnumValue(
    manufacturer = Manufacturer.AMAZON,
    parent = KINDLE,
    versionId = 30,
    name = "Linux (Kindle 3)",
    aliases = [ "Kindle/3" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )


  KINDLE2 = EnumValue(
    manufacturer = Manufacturer.AMAZON,
    parent = KINDLE,
    versionId = 20,
    name = "Linux (Kindle 2)",
    aliases = [ "Kindle/2" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )

  # CamelHttpStream is being used by Evolution, an email client for Linux
  LINUX = EnumValue(
    manufacturer = Manufacturer.OTHER,
    parent = None,
    versionId = 2,
    name = "Linux",
    aliases = [ "Linux" , "CamelHttpStream" ],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )


  #
  # Other Symbian OS versions
  #

  SYMBIAN = EnumValue(
    manufacturer = Manufacturer.SYMBIAN,
    parent = None,
    versionId = 1,
    name = "Symbian OS",
    aliases = [ "Symbian", "Series60"],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  #
  # Symbian OS 9.x versions. Being used by Nokia (N71, N73, N81, N82, N91, N92, N95, ...)
  #

  SYMBIAN9 = EnumValue(
    manufacturer = Manufacturer.SYMBIAN,
    parent = SYMBIAN,
    versionId = 20,
    name = "Symbian OS 9.x",
    aliases = ["SymbianOS/9", "Series60/3"],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  #
  # Symbian OS 8.x versions. Being used by Nokia (6630, 6680, 6681, 6682, N70, N72, N90).
  #

  SYMBIAN8 = EnumValue(
    manufacturer = Manufacturer.SYMBIAN,
    parent = SYMBIAN,
    versionId = 15,
    name = "Symbian OS 8.x",
    aliases = [ "SymbianOS/8", "Series60/2.6", "Series60/2.8"],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  #
  # Symbian OS 7.x versions. Being used by Nokia (3230, 6260, 6600, 6620, 6670, 7610),
  # Panasonic (X700, X800), Samsung (SGH-D720, SGH-D730) and Lenovo (P930).
  #

  SYMBIAN7 = EnumValue(
    manufacturer = Manufacturer.SYMBIAN,
    parent = SYMBIAN,
    versionId = 10,
    name = "Symbian OS 7.x",
    aliases = [ "SymbianOS/7"],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  #
  # Symbian OS 6.x versions.
  #

  SYMBIAN6 = EnumValue(
    manufacturer = Manufacturer.SYMBIAN,
    parent = SYMBIAN,
    versionId = 5,
    name = "Symbian OS 6.x",
    aliases = [ "SymbianOS/6"],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  #
  # Nokia's Series 40 operating system. Series 60 (S60) uses the Symbian OS.
  #

  SERIES40  = EnumValue(
    manufacturer = Manufacturer.NOKIA,
    parent = None,
    versionId = 1,
    name = "Series 40",
    aliases = [ "Nokia6300"],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )

  #
  # Proprietary operating system used for many Sony Ericsson phones.
  #
  # after symbian, some SE phones use symbian
  SONY_ERICSSON  = EnumValue(
    manufacturer = Manufacturer.SONY_ERICSSON,
    parent = None,
    versionId = 1,
    name = "Sony Ericsson",
    aliases = [ "SonyEricsson"],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None  )


  SUN_OS = EnumValue(
    manufacturer = Manufacturer.SUN,
    parent = None,
    versionId = 1,
    name = "SunOS",
    aliases = [ "SunOS" ],
    exclude = None,
    deviceType = DeviceType.COMPUTER,
    versionRegexString = None )

  PSP = EnumValue(
    manufacturer = Manufacturer.SONY,
    parent = None,
    versionId = 1,
    name = "Sony Playstation",
    aliases = [ "Playstation" ],
    exclude = None,
    deviceType = DeviceType.GAME_CONSOLE,
    versionRegexString = None )

  #
  # Nintendo Wii game console.
  #

  WII = EnumValue(
    manufacturer = Manufacturer.NINTENDO,
    parent = None,
    versionId = 1,
    name = "Nintendo Wii",
    aliases = [ "Wii" ],
    exclude = None,
    deviceType = DeviceType.GAME_CONSOLE,
    versionRegexString = None )

  #
  # BlackBerryOS. The BlackBerryOS exists in different version. How relevant those versions are, is not clear.
  #

  BLACKBERRY = EnumValue(
    manufacturer = Manufacturer.BLACKBERRY,
    parent = None,
    versionId = 1,
    name = "BlackBerryOS",
    aliases = [ "BlackBerry" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  BLACKBERRY7 = EnumValue(
    manufacturer = Manufacturer.BLACKBERRY,
    parent = BLACKBERRY,
    versionId = 7,
    name = "BlackBerry 7",
    aliases = [ "Version/7" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )


  BLACKBERRY6 = EnumValue(
    manufacturer = Manufacturer.BLACKBERRY,
    parent = BLACKBERRY,
    versionId = 6,
    name = "BlackBerry 6",
    aliases = [ "Version/6" ],
    exclude = None,
    deviceType = DeviceType.MOBILE,
    versionRegexString = None )



  BLACKBERRY_TABLET = EnumValue(
    manufacturer = Manufacturer.BLACKBERRY,
    parent = None,
    versionId = 100,
    name = "BlackBerry Tablet OS",
    aliases = [ "RIM Tablet OS" ],
    exclude = None,
    deviceType = DeviceType.TABLET,
    versionRegexString = None )



  ROKU = EnumValue(
    manufacturer = Manufacturer.ROKU,
    parent = None,
    versionId = 1,
    name = "Roku OS",
    aliases = [ "Roku" ],
    exclude = None,
    deviceType = DeviceType.DMR,
    versionRegexString = None )

  UNKNOWN = EnumValue(
    manufacturer = Manufacturer.OTHER,
    parent = None,
    versionId = 1,
    name = "Unknown",
    aliases = [],
    exclude = None,
    deviceType = DeviceType.UNKNOWN,
    versionRegexString = None )

