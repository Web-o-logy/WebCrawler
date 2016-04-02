from urllib.request import urlopen
from page_links import PageLinks
from general import *

class Spider:

    project_name = ''
    domain_name = ''
    base_url = ''
    crawled_file = ''
    queue_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.crawled_file = project_name + '/crawled_links.txt'
        Spider.queue_file = project_name + '/queued_links.txt'
        self.boot()
        self.crawl_page('First Bug:')

    @staticmethod
    def boot():



