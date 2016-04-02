from html.parser import HTMLParser
from urllib import parse

class PageLinks(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        print(message)
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attributes, values) in attrs:
                if attributes == 'href':
                    self.links.add(parse.urljoin(self.base_url, values))

    def print_page_links(self):
        counter = 0
        for link in self.links:
            counter += 1
            print(str(counter) + ": " + link)

    def get_page_links(self):
        return self.links

    def number_of_links(self):
        return len(self.links)


class LinkFinder(PageLinks):
    pass
