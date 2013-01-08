# python-useragentutils
A python port of the [user-agent-utils Java library](http://user-agent-utils.java.net/)

## Installation

```
pip install useragentutils
```

## Usage

```python
from useragentutils import UserAgent

uaString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.14 (KHTML, like Gecko) Version/6.0.1 Safari/536.26.14"

ua = UserAgent(uaString)

browser = ua.browser
print(browser)
print(browser.version(uaString))
print(browser.manufacturer)
print(browser.renderingEngine)
print(browser.browserType)

os = ua.operatingSystem
print(os)
print(os.version(uaString))
print(os.manufacturer)
print(os.deviceType)
```
