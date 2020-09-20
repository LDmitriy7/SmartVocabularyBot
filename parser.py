"""Parse translations and examples from 'Reverso Context'"""
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import quote
from text_utils import define_lang
from fake_headers import make_headers

BASE_URL = f'https://context.reverso.net/{quote("перевод")}/'


def make_url(word):
    """Make url with word"""
    lang = define_lang(word)
    return BASE_URL + quote(f'{lang}/{word}')


def get_soup(word):
    """Return BS-object from response for word"""
    try:
        headers = make_headers()
        html = requests.get(make_url(word), headers=headers)
        return BS(html.text, 'lxml')
    except Exception as exc:
        print('залогировать:', exc)


def parse_translations(soup: BS, limit=5):
    """Return non-empty translation list or None"""
    try:
        div = soup.find('div', id="translations-content")
        words = div.text.split()
    except AttributeError:
        print('залогировать')
    else:
        return words[:limit] or None


def parse_examples(soup: BS, limit=3):
    """Return non-empty example list or None"""
    try:
        section = soup.find('section', id="examples-content")
        divs = section.find_all('div', class_='example', limit=limit)
        examples = []
        for div in divs:
            span1, span2 = div.find_all('span', class_='text', limit=2)
            result = (span1.text.strip(), span2.text.strip())
            examples.append(result)
    except AttributeError:
        print('залогировать')
    else:
        return examples or None


def get_dict(word) -> dict:
    """Return dict: {'translations': [list, None], 'examples': [list, None]} for word"""
    result = {'translations': None, 'examples': None}
    if not define_lang(word):
        return result
    soup = get_soup(word)
    result['translations'] = parse_translations(soup)
    if result['translations'] is None:
        return result
    result['examples'] = parse_examples(soup)
    return result
