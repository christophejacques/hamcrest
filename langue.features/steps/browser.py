class Browser:
    URL: str = ""

    @classmethod
    def open(cls, url):
        cls.URL = url

    @classmethod
    def close(cls):
        cls.URL = ""

    @classmethod
    def get(cls) -> str:
        return cls.URL

    @classmethod
    def is_connected(cls) -> bool:
        return cls.URL != ""


if __name__ == '__main__':
    adresse = "http://www.google.com"

    browser = Browser()
    assert not browser.is_connected()

    browser.open(adresse)
    assert browser.is_connected()

    assert adresse == browser.get()
    browser.close()
    assert not browser.is_connected()

    raise Exception("Tous les controles sont OK") 
