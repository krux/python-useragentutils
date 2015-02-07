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

## Developing

Setup vagrant in the usual way (see: [vagrant-setup](https://github.com/krux/vagrant-setup)).

Setup your environment:

```shell
cd $PROJECT_DIR
mkvirtualenv python-useragentutils
setvirtualenvproject .
pip install --upgrade pip==1.4.1
pip install -r requirements.pip
```

Run the tests:

```shell
nosetests
```

Write some code including tests..

Run the tests:
```shell
nosetests
```

File PRs against master w/ a new semantic version. When it merges jenkins will put the package in our pip repo.


