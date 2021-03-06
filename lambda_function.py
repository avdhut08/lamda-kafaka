import re
from urllib.request import urlopen
import bs4 as bs



def lambda_handler(event,context):
    url = event['url']
    html_data = urlopen(url).read()
    soup_data = bs.BeautifulSoup(html_data, 'html.parser')
    nav = soup_data.nav
    for nav_url in nav.find_all('a', text='environmental'):
        category_data = urlopen(nav_url.get('href')).read()
        category_soup_data = bs.BeautifulSoup(category_data, 'html.parser')
        for div in category_soup_data.find_all('div', string=re.compile('epidemic|corona virus', re.IGNORECASE)):
            for article_link in div.find_all('a'):
                article_data = urlopen(url + article_link.get('href')).read()
                article_soup_data = bs.BeautifulSoup(article_data, 'html.parser')
                article_url = url + article_link.get('href')
                ### we can save this variable into s3 bucket or else into
                return article_soup_data.title , article_url , article_soup_data.element_classes

