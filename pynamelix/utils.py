import requests

NAMELIX_URL = 'https://namelix.com/app/load2.php'


def get_names(keywords, styles='brandable', lengths='short', **kwargs):
    """get the names from namelix.com"""
    data = kwargs.copy()
    data['keywords'] = ' '.join(keywords) if isinstance(keywords, list) else keywords
    data['styles[]'] = styles  # multiword, brandable, language, wordmix, spelling, dictionary, rhyme, person
    data['lengths[]'] = lengths  # short, medium, long
    resp = requests.post(NAMELIX_URL, data=data)

    for item in resp.json():
        yield item.get('title')
