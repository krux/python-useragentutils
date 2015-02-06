from __future__ import absolute_import

import unittest

from useragentutils.operating_system import OperatingSystem
from useragentutils.device_type import DeviceType


tablets = [
    'Mozilla/5.0 (Linux U Android 2.2 es-es GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 '
    'Mobile Safari/533.1',
    'Mozilla/5.0 (Linux U Android 2.2 en-us SCH-I800 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 '
    'Mobile Safari/533.1',
    'Mozilla/5.0 (iPad U CPU iPhone OS 3_2 like Mac OS X en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7D11',
    'Mozilla/4.0 (compatible Linux 2.6.10) NetFront/3.3 Kindle/1.0 (screen 600x800)',
    'Mozilla/4.0 (compatible Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)',
    'Mozilla/5.0 (Linux U en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen '
    '600x800 rotate)',
    'Mozilla/5.0 (Linux U Android 3.0 en-us Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 '
    'Safari/534.13',
    # dropped the mobile part, so Android without mobile should be a tablet!
    'Mozilla/5.0 (PlayBook U RIM Tablet OS 1.0.0 en-US) AppleWebKit/534.8+ like Gecko) Version/0.0.1 Safari/534.8+',
    'Mozilla/5.0 (Linux U Android 4.0.3 en-us Transformer TF101 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) '
    'Version/4.0 Safari/534.30'
]

googleTV = [
    'Mozilla/5.0 (X11 U Linux i686 en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Large Screen '
    'Safari/533.4 GoogleTV/161242',
    'Mozilla/5.0 (X11 U: Linux i686 en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Large Screen '
    'Safari/533.4 GoogleTV/162671',
    # Sony
    'Mozilla/5.0 (X11 U: Linux i686 en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Large Screen '
    'Safari/533.4 GoogleTV/b39389'
    # Logitech Revue
]

gameconsoles = [
    'Mozilla/5.0 (PLAYSTATION 3 1.00)',
    'Opera/9.30 (Nintendo Wii U  2071 Wii Shop Channel/1.0 en)'
]

windowsCEdivices = [
    'Mozilla/4.0 (compatible MSIE 4.01 Windows CE O2 Xda 2mini PPC 240x320)',
    'Mozilla/4.0 (compatible MSIE 4.01 Windows CE PPC MDA Compact/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1',
    'HPiPAQhw6900/1.0/Mozilla/4.0 (compatible MSIE 4.01 Windows CE PPC 240x240)',
    'Mozilla/4.0 (compatible MSIE 6.0 Windows CE IEMobile 6.8) PPC 240x320 HTC_P3300/1.0 Profile/MIDP-2.0 '
    'Configuration/CLDC-1.1',
    'PPC 240x320 HTC_P3450/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 Mozilla/4.0 (compatible MSIE 6.0 Windows CE '
    'IEMobile 6.12)',
    'Mozilla/4.0 (compatible MSIE 4.01 Windows CE PPC MDA compact/3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1)',
    'Mozilla/4.0 (compatible MSIE 4.01 Windows CE PPC MDA Vario/1.2 Profile/MIDP-2.0 Configuration/CLDC-1.1)',
    'HTC_S620 Mozilla/4.0 (compatible MSIE 6.0 Windows CE IEMobile 6.12)',
    'HTCS620-Mozilla/4.0 (compatible MSIE 4.01 Windows CE Smartphone 320x240)',
    'Mozilla/4.0 (compatible MSIE 6.0 Windows CE PPC)',
    'SAMSUNG-SGH-i600/1.0 (compatible MSIE 6.0 Windows CE IEMobile 6.8)',
    'Mozilla/4.0 (compatible MSIE 6.0 Windows CE Smartphone)',
    'HTC_TouchDual Mozilla/4.0 (compatible MSIE 6.0 Windows CE IEMobile 7.6)',
    'Palm750/v0005 Mozilla/4.0 (compatible MSIE 6.0 Windows CE IEMobile 7.6) UP.Link/6.3.0.0.0'
]

palmOsDevices = [
    'Mozilla/4.0 (compatible MSIE 6.0 Windows 98 PalmSource/Palm-TunX Blazer/4.3) 16320x320',  # Palm LiveDrive
    'Mozilla/4.0 (compatible MSIE 6.0 Windows 98 PalmSource/Palm-D050 Blazer/4.3) 16320x320)',  # Palm TX PDA
    'Mozilla/4.76 (compatible MSIE 6.0 U Windows 95 PalmSource PalmOS WebPro Tungsten Proxyless 1.1 320x320x16)'
]

webOS = [
    'Mozilla/5.0 (webOS/1.3 U en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Desktop/1.0',
    'Mozilla/5.0 (webOS/1.0 U en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Pre/1.0'
]

symbian9phones = [
    'Mozilla/5.0 (SymbianOS/9.2 U Series60/3.1 NokiaN95/10.0.018 Profile/MIDP-2.0 Configuration/CLDC-1.1 ) '
    'AppleWebKit/413 (KHTML, like Gecko) Safari/413',
    'Mozilla/5.0 (SymbianOS/9.1 U en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
    # No symbian in string. from 3.0 on it is Symbian OS 9.
    'NokiaN80-3/1.0552.0.7Series60/3.0Profile/MIDP-2.0Configuration/CLDC-1.1',
    'NokiaN73-1/3.0638.0.0.1 Series60/3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1',
    'Mozilla/5.0 (SymbianOS/9.2 U Series60/3.1 NokiaE90-1/07.40.1.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 ) '
    'AppleWebKit/413 (KHTML, like Gecko) Safari/413'
]

symbian8phones = [
    # No Symbian in string, but we know, that 2.6. and 2.8 are Symbian OS 8 phones.
    'NokiaN90-1/3.0545.5.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1'
]

symbian7phones = [
    'Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0Configuration/CLDC-1.0'
]

symbianPhones = [
    # One of the SE phones with Symbian OS
    'SonyEricssonP1i/R100 Mozilla/4.0 (compatible MSIE 6.0 Symbian OS 661) Opera 8.65 [nl]'
]

sonyEricssonPhones = [
    'SonyEricssonK550i/R1JD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1',
    'SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1'
]

iPhones = [
    'Mozilla/5.0 (iPhone U CPU like Mac OS X nl-nl) AppleWebKit/420.1 (KHTML, like Gecko)',
    'Mozilla/5.0 (iPhone U CPU like Mac OS X en) AppleWebKit/420+ (KHTML, like Gecko)',
    'Mozilla/5.0 (iPhone U CPU like Mac OS X en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 '
    'Safari/419.3'
]

iPhone4 = [
    'Mozilla/5.0 (iPhone Simulator U CPU iPhone OS 4_0 like Mac OS X en-us) AppleWebKit/532.9 (KHTML, like Gecko) '
    'Version/4.0.5 Mobile/8A293 Safari/6531.22.7',
    'Mozilla/5.0 (iPhone U CPU iPhone OS 4_0 like Mac OS X en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 '
    'Mobile/8A293 Safari/6531.22.7'
]

iPhone5 = [
    'Mozilla/5.0 (iPhone CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 '
    'Mobile/9A334 Safari/7534.48.3'
]

iPods = [
    'Mozilla/5.0 (iPod U CPU like Mac OS X nl-nl) AppleWebKit/420.1 (KHTML, like Gecko)',
    'Mozilla/5.0 (iPod U CPU like Mac OS X en) AppleWebKit/420.1 (KHTML, like Gecko)',
    'Mozilla/5.0 (iPod U CPU like Mac OS X en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a '
    'Safari/419.3'
]

iPad = [
    'Mozilla/5.0 (iPad U CPU OS 3_2 like Mac OS X en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 '
    'Mobile/7B367 Safari/531.21.10',
    # final iPad Simulator
    'Mozilla/5.0 (iPad U CPU OS 3_2 like Mac OS X en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 '
    'Mobile/7B334b Safari/531.21.10',
    'Mozilla/5.0 (iPad U CPU OS 4_2_1 like Mac OS X ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 '
    'Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 '
    'Safari/7534.48.3'
]

blackberries = [
    'BlackBerry8700/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/150',
    'BlackBerry8707/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/139',
    'BlackBerry7290/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1',
    'BlackBerry8310/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/120',
    'BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/150'
]

blackberry6 = [
    'Mozilla/5.0 (BlackBerry U BlackBerry 9800 en-US) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.141 Mobile '
    'Safari/534.1+'
]

blackberry7 = [
    'Mozilla/5.0 (BlackBerry U BlackBerry 9850 en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 '
    'Mobile Safari/534.11+'
]

android1g = [
    'Mozilla/5.0 (Linux U Android 1.6 nl-nl T-Mobile G1 Build/DRC92) AppleWebKit/528.5+ (KHTML, like Gecko) '
    'Version/3.1.2 Mobile Safari/525.20.1',
    'Mozilla/5.0 (Linux U Android 1.5 nl-nl HTC Hero Build/CUPCAKE) AppleWebKit/528.5+ (KHTML, like Gecko) '
    'Version/3.1.2 Mobile Safari/525.20.1'
]

android2g = [
    'Mozilla/5.0 (Linux U Android 2.1 en-gb Nexus One Build/ERD79) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 '
    'Mobile Safari/530.17',
    'Mozilla/5.0 (Linux U Android 2.0 en-gb Milestone Build/SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) '
    'Version/4.0 Mobile Safari/530.17'
]

android4g = [
    'Mozilla/5.0 (Linux U Android 4.0.1 en-us Galaxy Nexus Build/ICL41) AppleWebKit/534.30 (KHTML, like Gecko) '
    'Version/4.0 Mobile Safari/534.30',
]

android2_tablet = [
    'Mozilla/5.0 (Linux U Android 2.3.4 en-us Kindle Fire Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) '
    'Version/4.0 Mobile Safari/533.1'
]

android3_tablet = [
    'Mozilla/5.0 (Linux U Android 3.0 en-us Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 '
    'Safari/534.13',
    'Mozilla/5.0 (Linux U Android 3.0.1 en-us Xoom Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 '
    'Safari/534.13',
    'Mozilla/5.0 (Linux U Android 3.1 en-us GT-P7510 Build/HMJ37) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 '
    'Safari/534.13'
    # Samsung Galaxy Tab
]

android4_tablet = [
    'Mozilla/5.0 (Linux U Android 4.0.3 en-us Transformer TF101 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) '
    'Version/4.0 Safari/534.30',
    'Mozilla/5.0 (Linux U Android-4.0.3 en-us Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) '
    'CrMo/16.0.912.75 Safari/535.7'
]

windows98 = [
    'Mozilla/4.0 (compatible MSIE 6.0 Windows 98 Rogers HiSpeed Internet (R1 1.3))',
    'Mozilla/5.0 (Windows U Win98 en-US rv:1.8b3) Gecko/20050713 SeaMonkey/1.0a'
]

windowsXP = [
    'Mozilla/5.0 (Windows U Windows NT 5.1 de rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729)',
    'Mozilla/5.0 (compatible MSIE 7.0 Windows NT 5.2 WOW64 .NET CLR 2.0.50727)'
]

windowsVista = [
    'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 6.0 SLCC1 .NET CLR 2.0.50727 .NET CLR 3.0.04506)'
]

windows7 = [
    'Mozilla/4.0 (compatible MSIE 7.0 Windows NT 6.1 WOW64 Trident/4.0 SLCC2 .NET CLR 2.0.50727 .NET CLR 3.5.30729 '
    '.NET CLR 3.0.30729 Media Center PC 6.0 MDDC MSOffice 12)',
    'Mozilla/4.0 (compatible MSIE 8.0 Windows NT 6.1 Trident/4.0 Mozilla/4.0 (compatible MSIE 6.0 Windows NT 5.1 SV1) '
    ' SLCC2 .NET CLR 2.0.50727 .NET CLR 3.5.30729 .NET CLR 3.0.30729 Media Center PC 6.0 Media Center PC 5.0 SLCC1 '
    'InfoPath.2)'
]

windowsMobile7 = [
    'Mozilla/4.0 (compatible MSIE 7.0 Windows Phone OS 7.0 Trident/3.1 IEMobile/7.0) AsusGalaxy6',
    'Mozilla/5.0 (compatible MSIE 9.0 Windows Phone OS 7.5 Trident/5.0 IEMobile/9.0)'
]

bada = [
    'Mozilla/5.0 (SAMSUNG SAMSUNG-GT-S8500/S8500NEJE5 U Bada/1.0 fr-fr) AppleWebKit/533.1 (KHTML, like Gecko) '
    'Dolfin/2.0 Mobile WVGA SMM-MMS/1.2.0 NexPlayer/3.0 profile/MIDP-2.1 configuration/CLDC-1.1 OPN-B',
    'Mozilla/5.0 (SAMSUNG SAMSUNG-GT-S8500/S8500XXJL2 U Bada/1.2 de-de) AppleWebKit/533.1 (KHTML, like Gecko) '
    'Dolfin/2.2 Mobile WVGA SMM-MMS/1.2.0 OPN-B'
]

maemo = [
    'Mozilla/5.0 (X11 U Linux armv7l en-US rv:1.9.2a1pre) Gecko/20091127 Firefox/3.5 Maemo Browser 1.5.6 RX-51 N900'
]

kindle2 = [
    'Mozilla/4.0 (compatible Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)'
]

kindle3 = [
    'Mozilla/5.0 (Linux U en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen '
    '600x800 rotate)'
]

kindle_fire = [
    'Mozilla/5.0 (Linux U Android 2.3.4 en-us Kindle Fire Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) '
    'Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Macintosh U Intel Mac OS X 10_6_3 en-us Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) '
    'Version/5.0 Safari/533.16 Silk-Accelerated=true'
    # silk mode
]

roku = [
    'Roku/DVP-4.1 (024.01E01250A)',  # Roku 2 XD
    'Roku/DVP-3.0 (013.00E02227A)'
]


class OperatingSystemTest(unittest.TestCase):
    #
    # Test method for {@link nl.bitwalker.useragentutils.OperatingSystem#isInUserAgentString(java.lang.String)}.
    #

    def testIsInUserAgentString(self):
        self.assertTrue(OperatingSystem.SYMBIAN9.isInUserAgentString(symbian9phones[0]))

    #
    # Test method for {@link nl.bitwalker.useragentutils.OperatingSystem#parseUserAgentString(java.lang.String)}.
    #

    def testParseUserAgentString(self):
        self.agentTest(windowsCEdivices, OperatingSystem.WINDOWS_MOBILE)
        self.agentTest(windowsMobile7, OperatingSystem.WINDOWS_MOBILE7)
        self.agentTest(windowsVista, OperatingSystem.WINDOWS_VISTA)
        self.agentTest(windows7, OperatingSystem.WINDOWS_7)
        self.agentTest(windowsXP, OperatingSystem.WINDOWS_XP)
        self.agentTest(windows98, OperatingSystem.WINDOWS_98)
        self.agentTest(palmOsDevices, OperatingSystem.PALM)
        self.agentTest(bada, OperatingSystem.BADA)
        self.agentTest(webOS, OperatingSystem.WEBOS)
        self.agentTest(symbian9phones, OperatingSystem.SYMBIAN9)
        self.agentTest(symbian8phones, OperatingSystem.SYMBIAN8)
        self.agentTest(symbian7phones, OperatingSystem.SYMBIAN7)
        self.agentTest(symbianPhones, OperatingSystem.SYMBIAN)
        self.agentTest(sonyEricssonPhones, OperatingSystem.SONY_ERICSSON)
        self.agentTest(iPhones, OperatingSystem.MAC_OS_X_IPHONE)
        self.agentTest(iPhone4, OperatingSystem.iOS4_IPHONE)
        self.agentTest(iPhone5, OperatingSystem.iOS5_IPHONE)
        self.agentTest(iPods, OperatingSystem.MAC_OS_X_IPOD)
        self.agentTest(iPad, OperatingSystem.MAC_OS_X_IPAD)
        self.agentTest(blackberries, OperatingSystem.BLACKBERRY)
        self.agentTest(blackberry6, OperatingSystem.BLACKBERRY6)
        self.agentTest(android1g, OperatingSystem.ANDROID1)
        self.agentTest(android2g, OperatingSystem.ANDROID2)
        self.agentTest(android4g, OperatingSystem.ANDROID4)
        self.agentTest(android2_tablet, OperatingSystem.ANDROID2_TABLET)
        self.agentTest(android3_tablet, OperatingSystem.ANDROID3_TABLET)
        self.agentTest(android4_tablet, OperatingSystem.ANDROID4_TABLET)
        self.agentTest(maemo, OperatingSystem.MAEMO)
        self.agentTest(kindle2, OperatingSystem.KINDLE2)
        self.agentTest(kindle3, OperatingSystem.KINDLE3)
        self.agentTest(roku, OperatingSystem.ROKU)
        self.agentTest(googleTV, OperatingSystem.GOOGLE_TV)

    def testAllDeviceTypes(self):
        self.deviceTypeTest(windowsCEdivices, DeviceType.MOBILE)
        self.deviceTypeTest(windowsMobile7, DeviceType.MOBILE)
        self.deviceTypeTest(windowsVista, DeviceType.COMPUTER)
        self.deviceTypeTest(palmOsDevices, DeviceType.MOBILE)
        self.deviceTypeTest(bada, DeviceType.MOBILE)
        self.deviceTypeTest(tablets, DeviceType.TABLET)
        self.deviceTypeTest(gameconsoles, DeviceType.GAME_CONSOLE)
        self.deviceTypeTest(googleTV, DeviceType.DMR)

    def testGroupRecursion(self):
        self.assertEquals(OperatingSystem.ANDROID2_TABLET.group, OperatingSystem.ANDROID)  # 2 levels deep
        self.assertEquals(OperatingSystem.BLACKBERRY6.group, OperatingSystem.BLACKBERRY)  # one level
        self.assertEquals(OperatingSystem.MAC_OS.group, OperatingSystem.MAC_OS)  # no children

    #
    # Test if generated id values are unique.
    #

    def testUniqueIdValues(self):
        retrievedIdValues = []

        for operatingSystem in OperatingSystem.values:
            self.assertFalse(operatingSystem.id in retrievedIdValues)
            retrievedIdValues.append(operatingSystem.id)

    def deviceTypeTest(self, agentStrings, expectedDeviceType):
        for agentString in agentStrings:
            self.assertEquals(expectedDeviceType, OperatingSystem.parseUserAgentString(agentString).deviceType)

    def agentTest(self, agentStrings, expectedOperatingSystem):
        for agentString in agentStrings:
            self.assertEquals(expectedOperatingSystem, OperatingSystem.parseUserAgentString(agentString))

