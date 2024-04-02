# import the get function from requests
import requests
# define a constant function using uppercase and snake-case
BIBLE_URL: str = 'https://bible-api.com/'


# define our function that gets a random verse
async def get_random_verse():
    # get our bible verse from the api
    response: dict = requests.get(f'{BIBLE_URL}?random=verse').json()
    # return the important info
    return response.get('text'), response.get('reference'), response.get('translation_name')


async def get_random_verse_pt():
    # get our bible verse from the api
    response: dict = requests.get(f'{BIBLE_URL}?random=verse&translation=almeida').json()  # type: ignore
    # return the important info
    return response.get('text'), response.get('reference'), response.get('translation_name')


async def get_verse(verse: str):
    response: dict = requests.get(f'{BIBLE_URL}{verse}').json()
    if not response.get('error'):
        return response.get('text'), response.get('reference'), response.get('translation_name')
    else:
        return 'Unable to find that verse', 'Error while retrieving verse', 'Failed!'


async def get_verse_pt(verse: str):
    response: dict = requests.get(f'{BIBLE_URL}{verse}&translation=almeida').json()
    if not response.get('error'):
        return response.get('text'), response.get('reference'), response.get('translation_name')
    else:
        return 'Não foi possível encontrar esse versículo', 'Erro ao recuperar versículo', 'Erro!'


if __name__ == '__main__':
    test: dict = requests.get(f'{BIBLE_URL}john 1:s1').json()
    print(test.get('error'))