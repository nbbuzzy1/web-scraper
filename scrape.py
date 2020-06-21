import requests
from bs4 import BeautifulSoup
import pprint

imporant_stories = []


def scape_hn(pages):
    for page_number in range(pages):
        page = requests.get(
            f'https://news.ycombinator.com/news?p={page_number + 1}')
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        create_custom_hn(links, subtext)

    return sort_stories_by_votes(imporant_stories)


def create_custom_hn(links, subtext):
    for i, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None)
        vote = subtext[i].select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))

            if points > 100:
                imporant_stories.append({
                    'title': title,
                    'link': href,
                    'votes': points
                })


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


pprint.pprint(scape_hn(5))
