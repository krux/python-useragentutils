from base_product import BaseProduct
from manufacturer import Manufacturer
from rendering_engine import RenderingEngine
from browser_type import BrowserType
from utilities import EnumValue


class Browser(BaseProduct):
    required = ['browserType', 'renderingEngine']

    # before MSIE
    OPERA = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=None,
        versionId=1,
        name='Opera',
        aliases=['Opera'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.PRESTO,
        versionRegexString='Opera\\/(([\\d]+)\\.([\\w]+))')

    # Opera for mobile devices
    OPERA_MINI = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=20,
        name='Opera Mini',
        aliases=['Opera Mini'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.PRESTO,
        versionRegexString=None)

    ##
    # For some strange reason Opera uses 9.80 in the user-agent string and otherwise it is very inconsistent. Use the
    # getVersion method if you really want to know which version it is.
    ##

    OPERA26 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=21,
        name='Opera 26',
        aliases=['OPR/26'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA25 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=22,
        name='Opera 25',
        aliases=['OPR/25'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA24 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=23,
        name='Opera 24',
        aliases=['OPR/24'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA23 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=24,
        name='Opera 23',
        aliases=['OPR/23'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA22 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=25,
        name='Opera 22',
        aliases=['OPR/22'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA21 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=26,
        name='Opera 21',
        aliases=['OPR/21'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA20 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=27,
        name='Opera 20',
        aliases=['OPR/20'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA19 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=28,
        name='Opera 19',
        aliases=['OPR/19'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA18 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=29,
        name='Opera 18',
        aliases=['OPR/18'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA17 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=30,
        name='Opera 17',
        aliases=['OPR/17'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA16 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=31,
        name='Opera 16',
        aliases=['OPR/16'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    OPERA15 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=32,
        name='Opera 15',
        aliases=['OPR/15'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=r'OPR/(([\d]+)\.([\w]+)?(\.[\w]+)?(\.[\w]+)?)')

    # Skipping 11-14 b/c they're rarely in the wild these days.

    OPERA10 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=10,
        name='Opera 10',
        aliases=['Opera/9.8'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.PRESTO,
        versionRegexString='Version\\/(([\\d]+)\\.([\\w]+))')

    OPERA9 = EnumValue(
        manufacturer=Manufacturer.OPERA,
        parent=OPERA,
        versionId=5,
        name='Opera 9',
        aliases=['Opera/9'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.PRESTO,
        versionRegexString=None)

    KONQUEROR = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=1,
        name='Konqueror',
        aliases=['Konqueror'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.KHTML,
        versionRegexString='Konqueror\\/(([0-9]+)\\.?([\\w]+)?(-[\\w]+)?)')

    ##
    # Outlook email client
    ##
    # before IE7
    OUTLOOK = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=None,
        versionId=100,
        name='Outlook',
        aliases=['MSOffice'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.WORD,
        versionRegexString='MSOffice (([0-9]+))')

    ##
    # Microsoft Outlook 2007 identifies itself as MSIE7 but uses the html rendering engine of Word 2007.
    # Example user agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR
    # 3.0.04506; .NET CLR 1.1.4322; MSOffice 12)
    ##
    # before IE7
    OUTLOOK2007 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=OUTLOOK,
        versionId=107,
        name='Outlook 2007',
        aliases=['MSOffice 12'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.WORD,
        versionRegexString=None)

    ##
    # Outlook 2010 is still using the rendering engine of Word. http:#www.fixoutlook.org
    ##
    # before IE7
    OUTLOOK2010 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=OUTLOOK,
        versionId=108,
        name='Outlook 2010',
        aliases=['MSOffice 14'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.WORD,
        versionRegexString=None)

    ##
    # Family of Internet Explorer browsers
    ##
    # before Mozilla
    IE = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=None,
        versionId=1,
        name='Internet Explorer',
        aliases=['MSIE'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString='MSIE (([\\d]+)\\.([\\w]+))')

    ##
    # Since version 7 Outlook Express is identifying itself. By detecting Outlook Express we can not
    # identify the Internet Explorer version which is probably used for the rendering.
    # Obviously this product is now called Windows Live Mail Desktop or just Windows Live Mail.
    ##
    # before IE7, previously known as Outlook Express. First released in 2006, offered with different name later
    OUTLOOK_EXPRESS7 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=110,
        name='Windows Live Mail',
        aliases=['Outlook-Express/7.0'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    ##
    # Since 2007 the mobile edition of Internet Explorer identifies itself as IEMobile in the user-agent.
    # If previous versions have to be detected, use the operating system information as well.
    ##
    # before MSIE strings
    IEMOBILE9 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=123,
        name='IE Mobile 9',
        aliases=['IEMobile/9'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE strings
    IEMOBILE7 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=121,
        name='IE Mobile 7',
        aliases=['IEMobile 7'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE
    IEMOBILE6 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=120,
        name='IE Mobile 6',
        aliases=['IEMobile 6'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    EDGE = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=None,
        versionId=96,
        name='Edge',
        aliases=['Edge'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.EDGEHTML,
        versionRegexString='Edge\\/(([0-9]+)\\.([0-9]+))')

    EDGE12 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=EDGE,
        versionId=97,
        name='Edge 12',
        aliases=['Edge/12'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.EDGEHTML,
        versionRegexString=None)

    # before Mozilla
    IE11 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=95,
        name='Internet Explorer 11',
        aliases=['Trident/7', 'IE 11.'],
        exclude=['MSIE 7'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=r'(?:Trident\/7|IE)(?:\.[0-9]*;)?(?:.*rv:| )(([0-9]+)\.?([0-9]+))')

    # before MSIE
    IE10 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=92,
        name='Internet Explorer 10',
        aliases=['MSIE 10'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE
    IE9 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=90,
        name='Internet Explorer 9',
        aliases=['MSIE 9'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE
    IE8 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=80,
        name='Internet Explorer 8',
        aliases=['MSIE 8'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE
    IE7 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=70,
        name='Internet Explorer 7',
        aliases=['MSIE 7'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE
    IE6 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=60,
        name='Internet Explorer 6',
        aliases=['MSIE 6'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE
    IE5_5 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=55,
        name='Internet Explorer 5.5',
        aliases=['MSIE 5.5'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    # before MSIE
    IE5 = EnumValue(
        manufacturer=Manufacturer.MICROSOFT,
        parent=IE,
        versionId=50,
        name='Internet Explorer 5',
        aliases=['MSIE 5'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.TRIDENT,
        versionRegexString=None)

    ##
    # Google Chrome browser
    ##
    # before Mozilla
    CHROME = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=None,
        versionId=1,
        name='Chrome',
        aliases=['Chrome'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString='Chrome\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)')

    # before Mozilla
    CHROME40 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=44,
        name='Chrome 40',
        aliases=['Chrome/40'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME39 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=43,
        name='Chrome 39',
        aliases=['Chrome/39'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME38 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=42,
        name='Chrome 38',
        aliases=['Chrome/38'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME37 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=41,
        name='Chrome 37',
        aliases=['Chrome/37'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME36 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=40,
        name='Chrome 36',
        aliases=['Chrome/36'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME35 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=39,
        name='Chrome 35',
        aliases=['Chrome/35'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME34 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=38,
        name='Chrome 34',
        aliases=['Chrome/34'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME33 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=37,
        name='Chrome 33',
        aliases=['Chrome/33'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME32 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=36,
        name='Chrome 32',
        aliases=['Chrome/32'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME31 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=35,
        name='Chrome 31',
        aliases=['Chrome/31'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME30 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=34,
        name='Chrome 30',
        aliases=['Chrome/30'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME29 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=45,
        name='Chrome 29',
        aliases=['Chrome/29'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME28 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=33,
        name='Chrome 28',
        aliases=['Chrome/28'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.BLINK,
        versionRegexString=None)

    # before Mozilla
    CHROME27 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=32,
        name='Chrome 27',
        aliases=['Chrome/27'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME26 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=31,
        name='Chrome 26',
        aliases=['Chrome/26'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME25 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=30,
        name='Chrome 25',
        aliases=['Chrome/25'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME24 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=29,
        name='Chrome 24',
        aliases=['Chrome/24'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME23 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=28,
        name='Chrome 23',
        aliases=['Chrome/23'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME22 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=27,
        name='Chrome 22',
        aliases=['Chrome/22'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME21 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=26,
        name='Chrome 21',
        aliases=['Chrome/21'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME20 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=25,
        name='Chrome 20',
        aliases=['Chrome/20'],
        exclude=['OPR/', 'Web Preview'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME19 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=24,
        name='Chrome 19',
        aliases=['Chrome/19'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME18 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=23,
        name='Chrome 18',
        aliases=['Chrome/18'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME17 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=22,
        name='Chrome 17',
        aliases=['Chrome/17'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME16 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=21,
        name='Chrome 16',
        aliases=['Chrome/16'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME15 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=20,
        name='Chrome 15',
        aliases=['Chrome/15'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME14 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=19,
        name='Chrome 14',
        aliases=['Chrome/14'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME13 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=18,
        name='Chrome 13',
        aliases=['Chrome/13'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME12 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=17,
        name='Chrome 12',
        aliases=['Chrome/12'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME11 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=16,
        name='Chrome 11',
        aliases=['Chrome/11'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME10 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=15,
        name='Chrome 10',
        aliases=['Chrome/10'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME9 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=10,
        name='Chrome 9',
        aliases=['Chrome/9'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    CHROME8 = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=CHROME,
        versionId=5,
        name='Chrome 8',
        aliases=['Chrome/8'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    #
    OMNIWEB = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=2,
        name='Omniweb',
        aliases=['OmniWeb'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before AppleWebKit
    SAFARI = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=None,
        versionId=1,
        name='Safari',
        aliases=['Safari', 'iphone', 'ipad'],
        exclude=['OPR/', 'Web Preview', 'Googlebot-Mobile'],
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString='Version\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)')

    CHROME_MOBILE = EnumValue(
        manufacturer=Manufacturer.GOOGLE,
        parent=SAFARI,
        versionId=100,
        name='Chrome Mobile',
        aliases=['CrMo', 'CriOS'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString='CrMo\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)')

    # before Safari
    MOBILE_SAFARI = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=SAFARI,
        versionId=2,
        name='Mobile Safari',
        aliases=['Mobile Safari', 'Mobile/'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # http:#en.wikipedia.org/wiki/Amazon_Silk
    SILK = EnumValue(
        manufacturer=Manufacturer.AMAZON,
        parent=SAFARI,
        versionId=15,
        name='Silk',
        aliases=['Silk/'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString='Silk\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\-[\\w]+)?)')

    # before AppleWebKit
    SAFARI8 = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=SAFARI,
        versionId=8,
        name='Safari 8',
        aliases=['Version/8'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before AppleWebKit
    SAFARI7 = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=SAFARI,
        versionId=7,
        name='Safari 7',
        aliases=['Version/7'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before AppleWebKit
    SAFARI6 = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=SAFARI,
        versionId=6,
        name='Safari 6',
        aliases=['Version/6'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before AppleWebKit
    SAFARI5 = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=SAFARI,
        versionId=5,
        name='Safari 5',
        aliases=['Version/5'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before AppleWebKit
    SAFARI4 = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=SAFARI,
        versionId=4,
        name='Safari 4',
        aliases=['Version/4'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # webkit based browser for the bada os
    DOLFIN2 = EnumValue(
        manufacturer=Manufacturer.SAMSUNG,
        parent=None,
        versionId=1,
        name='Samsung Dolphin 2',
        aliases=['Dolfin/2'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # Microsoft Entrourage/Outlook 2010 also only identifies itself as AppleWebKit
    APPLE_MAIL = EnumValue(
        manufacturer=Manufacturer.APPLE,
        parent=None,
        versionId=50,
        name='Apple Mail',
        aliases=['AppleWebKit'],
        exclude=['OPR/'],
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.WEBKIT,
        versionRegexString=None)

    # before Mozilla
    LOTUS_NOTES = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=3,
        name='Lotus Notes',
        aliases=['Lotus-Notes'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString='Lotus-Notes\\/(([\\d]+)\\.([\\w]+))')

    ##
    # Thunderbird email client, based on the same Gecko engine Firefox is using.
    ##
    # using Gecko Engine
    THUNDERBIRD = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=None,
        versionId=110,
        name='Thunderbird',
        aliases=['Thunderbird'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString='Thunderbird\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)')

    # using Gecko Engine
    THUNDERBIRD12 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=185,
        name='Thunderbird 12',
        aliases=['Thunderbird/12'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    THUNDERBIRD11 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=184,
        name='Thunderbird 11',
        aliases=['Thunderbird/11'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    THUNDERBIRD10 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=183,
        name='Thunderbird 10',
        aliases=['Thunderbird/10'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    THUNDERBIRD8 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=180,
        name='Thunderbird 8',
        aliases=['Thunderbird/8'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    THUNDERBIRD7 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=170,
        name='Thunderbird 7',
        aliases=['Thunderbird/7'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    THUNDERBIRD6 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=160,
        name='Thunderbird 6',
        aliases=['Thunderbird/6'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    THUNDERBIRD3 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=130,
        name='Thunderbird 3',
        aliases=['Thunderbird/3'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    THUNDERBIRD2 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=THUNDERBIRD,
        versionId=120,
        name='Thunderbird 2',
        aliases=['Thunderbird/2'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    CAMINO = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=5,
        name='Camino',
        aliases=['Camino'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString='Camino\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)')

    # using Gecko Engine
    CAMINO2 = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=CAMINO,
        versionId=17,
        name='Camino 2',
        aliases=['Camino/2'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FLOCK = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=4,
        name='Flock',
        aliases=['Flock'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString='Flock\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)')

    # using Gecko Engine
    FIREFOX = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=None,
        versionId=10,
        name='Firefox',
        aliases=['Firefox'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString='Firefox\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?(\\.[\\w]+)?)')

    # using Gecko Engine
    FIREFOX3MOBILE = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=31,
        name='Firefox 3 Mobile',
        aliases=['Firefox/3.5 Maemo'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX36 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=135,
        name='Firefox 36',
        aliases=['Firefox/36'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX35 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=128,
        name='Firefox 35',
        aliases=['Firefox/35'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX34 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=127,
        name='Firefox 34',
        aliases=['Firefox/34'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX33 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=126,
        name='Firefox 33',
        aliases=['Firefox/33'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX32 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=125,
        name='Firefox 32',
        aliases=['Firefox/32'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX31 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=124,
        name='Firefox 31',
        aliases=['Firefox/31'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX30 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=123,
        name='Firefox 30',
        aliases=['Firefox/30'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX29 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=122,
        name='Firefox 29',
        aliases=['Firefox/29'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX28 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=121,
        name='Firefox 28',
        aliases=['Firefox/28'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX27 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=129,
        name='Firefox 27',
        aliases=['Firefox/27'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX26 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=119,
        name='Firefox 26',
        aliases=['Firefox/26'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX25 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=118,
        name='Firefox 25',
        aliases=['Firefox/25'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX24 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=117,
        name='Firefox 24',
        aliases=['Firefox/24'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX23 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=116,
        name='Firefox 23',
        aliases=['Firefox/23'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX22 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=115,
        name='Firefox 22',
        aliases=['Firefox/22'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX21 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=114,
        name='Firefox 21',
        aliases=['Firefox/21'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX20 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=113,
        name='Firefox 20',
        aliases=['Firefox/20'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX19 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=112,
        name='Firefox 19',
        aliases=['Firefox/19'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX18 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=111,
        name='Firefox 18',
        aliases=['Firefox/18'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX17 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=131,
        name='Firefox 17',
        aliases=['Firefox/17'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX16 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=109,
        name='Firefox 16',
        aliases=['Firefox/16'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX15 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=108,
        name='Firefox 15',
        aliases=['Firefox/15'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    FIREFOX14 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=107,
        name='Firefox 14',
        aliases=['Firefox/14'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX13 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=94,
        name='Firefox 13',
        aliases=['Firefox/13'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX12 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=93,
        name='Firefox 12',
        aliases=['Firefox/12'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX11 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=92,
        name='Firefox 11',
        aliases=['Firefox/11'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX10 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=91,
        name='Firefox 10',
        aliases=['Firefox/10'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX9 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=90,
        name='Firefox 9',
        aliases=['Firefox/9'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX8 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=80,
        name='Firefox 8',
        aliases=['Firefox/8'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX7 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=70,
        name='Firefox 7',
        aliases=['Firefox/7'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX6 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=60,
        name='Firefox 6',
        aliases=['Firefox/6'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX5 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=50,
        name='Firefox 5',
        aliases=['Firefox/5'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX4 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=40,
        name='Firefox 4',
        aliases=['Firefox/4'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX3 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=30,
        name='Firefox 3',
        aliases=['Firefox/3'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX2 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=20,
        name='Firefox 2',
        aliases=['Firefox/2'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    FIREFOX1_5 = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=FIREFOX,
        versionId=15,
        name='Firefox 1.5',
        aliases=['Firefox/1.5'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString=None)

    # using Gecko Engine
    SEAMONKEY = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=15,
        name='SeaMonkey',
        aliases=['SeaMonkey'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.GECKO,
        versionRegexString='SeaMonkey\\/(([0-9]+)\\.?([\\w]+)?(\\.[\\w]+)?)')

    BOT = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=12,
        name='Robot/Spider',
        aliases=['Googlebot', 'bot', 'spider', 'crawler', 'Feedfetcher', 'Slurp', 'Twiceler', 'Nutch', 'BecomeBot'],
        exclude=None,
        browserType=BrowserType.ROBOT,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    # rest of the mozilla browsers
    MOZILLA = EnumValue(
        manufacturer=Manufacturer.MOZILLA,
        parent=None,
        versionId=1,
        name='Mozilla',
        aliases=['Mozilla', 'Moozilla'],
        exclude=None,
        browserType=BrowserType.WEB_BROWSER,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    # Mac OS X cocoa library
    CFNETWORK = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=6,
        name='CFNetwork',
        aliases=['CFNetwork'],
        exclude=None,
        browserType=BrowserType.UNKNOWN,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    # email client by Qualcomm
    EUDORA = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=7,
        name='Eudora',
        aliases=['Eudora', 'EUDORA'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    POCOMAIL = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=8,
        name='PocoMail',
        aliases=['PocoMail'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    # Email Client
    THEBAT = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=9,
        name='The Bat!',
        aliases=['The Bat'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    # mobile device browser
    NETFRONT = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=10,
        name='NetFront',
        aliases=['NetFront'],
        exclude=None,
        browserType=BrowserType.MOBILE_BROWSER,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    # http:#www.go-evolution.org/Camel.Stream
    EVOLUTION = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=11,
        name='Evolution',
        aliases=['CamelHttpStream'],
        exclude=None,
        browserType=BrowserType.EMAIL_CLIENT,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    DOWNLOAD = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=16,
        name='Downloading Tool',
        aliases=['cURL', 'wget'],
        exclude=None,
        browserType=BrowserType.TEXT_BROWSER,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)

    UNKNOWN = EnumValue(
        manufacturer=Manufacturer.OTHER,
        parent=None,
        versionId=14,
        name='Unknown',
        aliases=[],
        exclude=None,
        browserType=BrowserType.UNKNOWN,
        renderingEngine=RenderingEngine.OTHER,
        versionRegexString=None)
