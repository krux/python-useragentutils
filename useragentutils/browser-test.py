from browser import Browser
from version import Version
from operating_system import OperatingSystem

import unittest

ie6clients = [
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; T312461)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; XMPP Tiscali Communicator v.10.0.2; .NET CLR 2.0.50727)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
]

ie7clients = [
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
  "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0 ; .NET CLR 2.0.50215; SL Commerce Client v1.0; Tablet PC 2.0",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)" # Windows Mail on Vista
]

ie8clients = [
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; Media Center PC 5.0; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Win64; x64; .NET CLR 2.0.50727; SLCC1; Media Center PC 5.0; .NET CLR 3.0.04506)"
]

ie9clients = [
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0"
]

ie10clients = [
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"
]

ie55clients = [
  "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)",
  "Mozilla/4.0 (compatible; MSIE 5.5; Windows 95)"
]

ieTooOld = [
  "Mozilla/4.0 (compatible; MSIE 4.01; Windows 95)",
  "Mozilla/4.0 (compatible; MSIE 4.0; Windows 95; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/2.0 (compatible; MSIE 3.03; Windows 3.1)"
]

outlook2007 = [
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; .NET CLR 1.1.4322; MSOffice 12)"
]

outlook2010 = [
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB6.4; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; MSOffice 14)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Media Center PC 6.0; SLCC2; ms-office; MSOffice 14)"
]


outookExpress = [
  "Outlook-Express/7.0 (MSIE 6.0; Windows NT 5.1; SV1; SIMBAR={xxx] .NET CLR 2.0.50727; .NET CLR 1.1.4322; TmstmpExt)",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 5.1; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; TmstmpExt)"
]

ieMobile6 = [
  "HTC_TyTN Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12) Vodafone/1.0/HTC_s710/1.22.172.3",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.8) PPC; 240x320; HTC_TyTN/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1"
]

ieMobile7 = [
   "HTC_TouchDual Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.6)",
   "PPC; 240x320; HTC_P3450/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.6)",
   "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.6) PPC; MDA Vario/3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1",
   "Palm750/v0005 Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.6) UP.Link/6.3.0.0.0"
]

ieMobile9 = [
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
]

lotusNotes = [
  "Mozilla/4.0 (compatible; Lotus-Notes/5.0; Windows-NT)",
  "Mozilla/4.0 (compatible; Lotus-Notes/6.0; Windows-NT)"
]

# Not supported
# lynxClient = [
#   "Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
#   "Lynx/2.7.1ac-0.102+intl+csuite libwww-FM/2.14"
# ]

konqueror = [
  "Mozilla/5.0 (compatible; konqueror/3.3; linux 2.4.21-243-smp4G) (KHTML, like Geko)",
  "Mozilla/6.0 (compatible; Konqueror/4.2; i686 FreeBSD 6.4; 20060308)",
  "Mozilla/5.0 (compatible; Konqueror/3.1; Linux 2.4.21-20.0.1.ELsmp; X11; i686; , en_US, en, de)"
]

chromeMobile = [
  "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7",
  "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7"
]

chrome = [
  "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9"
]

chrome8 = [
  "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10",
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/8.1.0.0 Safari/540.0"
]

chrome9 = [
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14"
]

chrome10 = [
  "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15"
]

chrome11 = [
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.697.0 Safari/534.24"
]

chrome12 = [
  "Mozilla/5.0 (X11; CrOS i686 12.0.742.91) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30"
]

chrome13 = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1"
]

chrome14 = [
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1"
]

firefox3 = [
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.14) Gecko/2009090216 Ubuntu/9.04 (jaunty) Firefox/3.0.14"
]

firefox4 = [
  "Mozilla/5.0 (X11; Linux x86_64; rv:2.0b4) Gecko/20100818 Firefox/4.0b4",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre"
]

firefox5 = [
  "Mozilla/5.0 (Windows NT 6.1; U; ru; rv:5.0.1.6) Gecko/20110501 Firefox/5.0.1 Firefox/5.0.1",
  "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0"
]

firefox6 = [
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110612 Firefox/6.0a2"
]


firefox3mobile = [
  "Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20091127 Firefox/3.5 Maemo Browser 1.5.6 RX-51 N900"
]

safari = [
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/525.28.3 (KHTML, like Gecko) Version/3.2.3 Safari/525.28.3",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-gb) AppleWebKit/523.10.6 (KHTML, like Gecko) Version/3.0.4 Safari/523.10.6"
]

safari5 = [
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-us) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-us) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"
]

safari4 = [
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/4.0.1 Safari/530.18"
]

mobileSafari = [
  "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
  "Mozilla/5.0 (iPod; U; CPU iPhone OS 2_0 like Mac OS X; de-de) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/525.20", # Mobile Safari 3.1.1
  "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3", # Mobile Safari 3.0
  "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10",
  "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",

  # handle safari not in UA String
  "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206",
  "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10A403"
]

dolfin = [
  "Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S8500/S8500NEJE5; U; Bada/1.0; fr-fr) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/2.0 Mobile WVGA SMM-MMS/1.2.0 NexPlayer/3.0 profile/MIDP-2.1 configuration/CLDC-1.1 OPN-B"
]

# similar to Safari, but doesn't mention Safari in the user-agent string
appleMail = [
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-us) AppleWebKit/533.18.1 (KHTML, like Gecko)"
]

omniWeb = [
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/531.9+(KHTML, like Gecko, Safari/528.16) OmniWeb/v622.10.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/525.18 (KHTML, like Gecko, Safari/525.20) OmniWeb/v622.3.0.105198"
]

opera = [
  "Opera/8.0 (Macintosh; PPC Mac OS X; U; en)",
  ]

opera9 = [
  "Opera/9.52 (Windows NT 5.1; U; en)",
  "Opera/9.20 (Macintosh; Intel Mac OS X; U; en)"
  ]

opera10 = [
  "Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10",
  "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61"
  ]

operaMini = [
  "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.13337/458; U; en) Presto/2.2.0",
  "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/1428; U; en) Presto/2.2.0"
]

camino2 = [
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.0.19) Gecko/2010111021 Camino/2.0.6 (MultiLang) (like Firefox/3.0.19)",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.0.18) Gecko/2010021619 Camino/2.0.2 (like Firefox/3.0.18)"
]

camino = [
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; it; rv:1.8.1.21) Gecko/20090327 Camino/1.6.7 (MultiLang) (like Firefox/2.0.0.21pre)",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.4) Gecko/20060613 Camino/1.0.2"
]

flock = [
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008100716 Firefox/3.0.3 Flock/2.0"
]

seaMonkey = [
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.13) Gecko/20100914 Mnenhy/0.8.3 SeaMonkey/2.0.8"
]

bots = [
  "Mozilla/5.0 (compatible; Googlebot/2.1; http:#www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http:#help.yahoo.com/help/us/ysearch/slurp)",
  "Googlebot-Image/1.0"
]

tools = [
  "curl/7.19.5 (i586-pc-mingw32msvc) libcurl/7.19.5 OpenSSL/0.9.8l zlib/1.2.3",
  "Wget/1.8.1"
]

thunderbird3 = [
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.12) Gecko/20101027 Thunderbird/3.1.6",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE; rv:1.9.2.8) Gecko/20100802 Thunderbird/3.1.2 ThunderBrowse/3.3.2"
]

thunderbird2 = [
  "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.8.1.14) Gecko/20080421 Thunderbird/2.0.0.14",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.17) Gecko/20080914 Thunderbird/2.0.0.17"
]

silk = [
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true"
]

class BrowserTest(unittest.TestCase):


  def testIsBrowser(self):
    self.assertTrue(Browser.SAFARI.isInUserAgentString("Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3"))

  def test_version_detection(self):
    # Lynx is not supported
    # self.versionTest("Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d", Version("2.8.5rel.1","2","8"))
    self.versionTest("Mozilla/6.0 (compatible; Konqueror/4.2; i686 FreeBSD 6.4; 20060308)", Version("4.2", "4","2"))
    self.versionTest("Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021219)", Version("3.1-rc5","3","1"))
    self.versionTest("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.14) Gecko/2009090216 Ubuntu/9.04 (jaunty) Firefox/3.0.14", Version("3.0.14","3","0"))
    self.versionTest("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0 ; .NET CLR 2.0.50215; SL Commerce Client v1.0; Tablet PC 2.0", Version("7.0b","7","0b")) # is minor here b or 0b?
    self.versionTest("Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10", Version("10.10", "10", "10"))
    self.versionTest("Opera/8.0 (Macintosh; PPC Mac OS X; U; en)", Version("8.0","8","0"))
    self.versionTest("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10",Version("8.0.558.0","8","0"))
    self.versionTest("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0", Version("9.1.0.0","9","1"))
    self.versionTest("Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-gb) AppleWebKit/523.10.6 (KHTML, like Gecko) Version/3.0.4 Safari/523.10.6", Version("3.0.4","3","0"))
    self.versionTest("Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17", Version("4.0","4","0"))
    self.versionTest("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; GTB6.4; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; MSOffice 14)", Version("14","14","0"))
    self.versionTest("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; it; rv:1.8.1.21) Gecko/20090327 Camino/1.6.7 (MultiLang) (like Firefox/2.0.0.21pre)", Version("1.6.7","1","6"))
    self.versionTest("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008100716 Firefox/3.0.3 Flock/2.0", Version("2.0","2","0"))
    self.versionTest("Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.17) Gecko/20080914 Thunderbird/2.0.0.17", Version("2.0.0.17","2","0"))
    self.versionTest("Mozilla/4.0 (compatible; Lotus-Notes/5.0; Windows-NT)", Version("5.0","5","0"))
    self.versionTest("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.13) Gecko/20100914 Mnenhy/0.8.3 SeaMonkey/2.0.8", Version("2.0.8", "2", "0"))
    self.versionTest("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0",None)
    self.versionTest("Mozilla/5.0 (compatible; Googlebot/2.1; http:#www.google.com/bot.html)", None) # no version information for some browsers
    self.versionTest("Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7", Version("16.0.912.75", "16", "0"))
    self.versionTest("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true", Version("1.1.0-80", "1", "1"))


  def versionTest(self, ua, expectedVersion):
    version = Browser.parseUserAgentString(ua).version(ua)
    self.assertEquals(expectedVersion, version)

  def testParseUserAgentString(self):
    self.agentTest(ie55clients, Browser.IE5_5)
    self.agentTest(ie6clients, Browser.IE6)
    self.agentTest(ie7clients, Browser.IE7)
    self.agentTest(ie8clients, Browser.IE8)
    self.agentTest(ie9clients, Browser.IE9)
    self.agentTest(ie10clients, Browser.IE10)
    self.agentTest(ieTooOld, Browser.IE)
    self.agentTest(outlook2007, Browser.OUTLOOK2007)
    self.agentTest(outlook2010, Browser.OUTLOOK2010)
    self.agentTest(outookExpress, Browser.OUTLOOK_EXPRESS7)
    self.agentTest(ieMobile6, Browser.IEMOBILE6)
    self.agentTest(ieMobile7, Browser.IEMOBILE7)
    self.agentTest(ieMobile9, Browser.IEMOBILE9)
    self.agentTest(lotusNotes, Browser.LOTUS_NOTES)
    # Lynx is not supported
    #self.agentTest(lynxClient, Browser.LYNX)
    self.agentTest(konqueror, Browser.KONQUEROR)
    self.agentTest(chromeMobile, Browser.CHROME_MOBILE)
    self.agentTest(chrome, Browser.CHROME)
    self.agentTest(chrome8, Browser.CHROME8)
    self.agentTest(chrome9, Browser.CHROME9)
    self.agentTest(chrome10, Browser.CHROME10)
    self.agentTest(chrome11, Browser.CHROME11)
    self.agentTest(chrome12, Browser.CHROME12)
    self.agentTest(chrome13, Browser.CHROME13)
    self.agentTest(chrome14, Browser.CHROME14)
    self.agentTest(firefox3, Browser.FIREFOX3)
    self.agentTest(firefox4, Browser.FIREFOX4)
    self.agentTest(firefox5, Browser.FIREFOX5)
    self.agentTest(firefox6, Browser.FIREFOX6)
    self.agentTest(firefox3mobile, Browser.FIREFOX3MOBILE)
    self.agentTest(safari, Browser.SAFARI)
    self.agentTest(dolfin, Browser.DOLFIN2)
    self.agentTest(safari5, Browser.SAFARI5)
    self.agentTest(safari4, Browser.SAFARI4)
    self.agentTest(mobileSafari, Browser.MOBILE_SAFARI)
    self.agentTest(appleMail, Browser.APPLE_MAIL)
    self.agentTest(omniWeb, Browser.OMNIWEB)
    self.agentTest(operaMini, Browser.OPERA_MINI)
    self.agentTest(opera9, Browser.OPERA9)
    self.agentTest(opera, Browser.OPERA)
    self.agentTest(opera10, Browser.OPERA10)
    self.agentTest(camino2, Browser.CAMINO2)
    self.agentTest(flock, Browser.FLOCK)
    self.agentTest(seaMonkey, Browser.SEAMONKEY)
    self.agentTest(bots, Browser.BOT)
    self.agentTest(tools, Browser.DOWNLOAD)
    self.agentTest(thunderbird3, Browser.THUNDERBIRD3)
    self.agentTest(thunderbird2, Browser.THUNDERBIRD2)
    self.agentTest(silk, Browser.SILK)

  def agentTest(self, agentStrings, expected):
    for agentString in agentStrings:
      actual = Browser.parseUserAgentString(agentString)

      self.assertEquals(expected, actual, ""+ str(expected) + " != " + str(actual) + " ua: " + agentString)

  def test_incompleteUAString(self):
    browser = Browser.parseUserAgentString("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us) AppleWebKit/531.21.11 (KHTML, like")
    browser.version("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us) AppleWebKit/531.21.11 (KHTML, like")
    browser2 = Browser.parseUserAgentString("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.8) Gecko/2009032608 Firefox")
    browser2.version("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.8) Gecko/2009032608 Firefox")
    browser3 = Browser.parseUserAgentString("Mozilla/4.0 (compatible; MSIE 8")
    browser3.version("Mozilla/4.0 (compatible; MSIE 8")

  def test_unique_id_values(self):

    retrievedIdValues = []

    for browser in Browser.values:
      self.assertFalse(browser.id in retrievedIdValues, browser.name)
      retrievedIdValues.append(browser.id)

if __name__ == '__main__':
  unittest.main()
