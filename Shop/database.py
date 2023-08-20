from requests import get
import json
from pprint import pprint
import datetime
from random import shuffle
from mainapp.models import ImageBook


class BookNew:

    @staticmethod
    def get_all():
        books_base = get('https://localhost:5001/ServicesRest/ReadDatabaseBookCard', verify=False)
        books = []
        for item in decode_data(books_base):
            book = {
                'id': item['idBook'],
                'name': item['nameBook'],
                'author': item['authorBook'],
                'foto': item['photoBook'],
                'article': item['vendorCodeBook'],
                'date_receipt': datetime.datetime.strptime(item['recieptDateBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
                'category': item['genreBook'],
                'description': item['descriptionBook'],
                'price': item['priceBook'],
                'date_create': datetime.datetime.strptime(item['dateCreationBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
                'date_update': datetime.datetime.strptime(item['dateUpdateBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
            }
            image = ImageBook.objects.filter(guid=book['id']).first()
            if image:
                book['foto'] = image.foto.url
            books.append(book)
        return books

    @staticmethod
    def get_last():
        return BookNew.get_all()[-1]

    @staticmethod
    def create(data, files):
        result = get(f' https://localhost:5001/ServicesRest/CreateDatabaseBookCard/'
                   f'{data["name"]}/'
                   f'{data["author"]}/'
                   f'{1}/'
                   f'{data["article"]}/'
                   f'{data["category"]}/'
                   f'{data["description"]}/'
                   f'{data["price"]}',
                   verify=False)
        if result.status_code == 200:
            return BookNew.get_last()['id']
        else:
            return False

    @staticmethod
    def get_by_guid(guid):
        get_book = get(f'https://localhost:5001/ServicesRest/IDReadDatabaseBookCard/{guid}', verify=False)
        item = decode_data(get_book)
        book = {
            'id': item['idBook'],
            'name': item['nameBook'],
            'author': item['authorBook'],
            'foto': item['photoBook'],
            'article': item['vendorCodeBook'],
            'date_receipt': datetime.datetime.strptime(item['recieptDateBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
            'category': item['genreBook'],
            'description': item['descriptionBook'],
            'price': item['priceBook'],
            'date_create': datetime.datetime.strptime(item['dateCreationBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
            'date_update': datetime.datetime.strptime(item['dateUpdateBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
        }
        image = ImageBook.objects.filter(guid=book['id']).first()
        if image:
            book['foto'] = image.foto.url
        return book

    @staticmethod
    def update(data, guid):
        result = get(f'https://localhost:5001/ServicesRest/UpdateDatabaseBookCard/'
                   f'{guid}/'
                   f'{data["name"]}/'
                   f'{data["author"]}/'
                   f'{1}/'
                   f'{data["article"]}/'
                   f'{data["category"]}/'
                   f'{data["description"]}/'
                   f'{data["price"]}', verify=False)
        if result.status_code == 200:
            return guid
        else:
            return False

    @staticmethod
    def delete(guid):
        return get(f'https://localhost:5001/ServicesRest/DeleteDatabaseBookCard/{guid}', verify=False)

    @staticmethod
    def random():
        data = BookNew.get_all()
        shuffle(data)
        return data

    @staticmethod
    def get_all_reverse():
        books = BookNew.get_all()
        books.reverse()
        return books

    @staticmethod
    def get_sorted(o_field):
        books = BookNew.get_all()
        books.sort(key=lambda dictionary: dictionary[o_field])
        return books

    @staticmethod
    def get_sorted_filtered(o_field, f_filed):
        books = BookNew.get_all()
        books.sort(key=lambda dictionary: dictionary[o_field])
        books_list = [x for x in books if f_filed in x['category'] or f_filed in x['author']]
        return books_list

    @staticmethod
    def get_search(o_field, s_filed):
        books = BookNew.get_all()
        books.sort(key=lambda dictionary: dictionary[o_field])
        books_list = [x for x in books if s_filed.lower() in x['category'].lower() or s_filed.lower() in x['author'].lower() or s_filed.lower() in x['name'].lower() or s_filed in str(x['price'])]
        return books_list


class BasketNew:

    @staticmethod
    def create(**kwargs):
        return get(f'https://localhost:5001/CreateDatabaseBaskets/IdUser/IdBook/QuantityBooks/PricePerBook')

    @staticmethod
    def add():
        pass

    @staticmethod
    def get_by_user(guid):
        pass

    @staticmethod
    def get_by_guid(guid):
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete(guid):
        pass


class OrderNew:

    @staticmethod
    def create():
        pass

    @staticmethod
    def get_by_user(guid):
        pass

    @staticmethod
    def get_by_guid(guid):
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete(guid):
        pass


class QuoteNew:

    @staticmethod
    def get_all():
        quotes_base = get('https://localhost:5001/ServicesRest/ReadDatabaseQuoteCard', verify=False)
        quotes = []
        for item in decode_data(quotes_base):
            quote = {
                'id': item['idQuote'],
                'name': item['QuoteTitle'],
                'text': item['QuoteText'],
                'author': item['QuoteAutor'],
            }
            quotes.append(quote)
        return quotes

    @staticmethod
    def create(data):
        result = get(f'https://localhost:5001/ServicesRest/CreateDatabaseQuoteCard/'
                   f'{data["name"]}/'
                   f'{data["text"]}/'
                   f'{data["author"]}',
                   verify=False)
        if result.status_code == 200:
            return result

        else:
            return False

    @staticmethod
    def get_by_guid(guid):
        get_quote = get(f'https://localhost:5001/ServicesRest/IDReadDatabaseQuoteCard/{guid}')
        item = decode_data(get_quote)
        quote = {
            'id': item['IdQuote'],
            'name': item['QuoteTitle'],
            'text': item['QuoteText'],
            'author': item['QuoteAutor']
        }
        return quote

    @staticmethod
    def update(**kwargs):
        return get(f'https://localhost:5001/ServicesRest/UpdateDatabaseQuoteCard/'
                   f'{kwargs["id"]}/'
                   f'{kwargs["name"]}/'
                   f'{kwargs["text"]}/'
                   f'{kwargs["author"]}')

    @staticmethod
    def delete(guid):
        return get(f'https://localhost:5001/ServicesRest/DeleteDatabaseQuoteCard/{guid}', verify=False)


class RequestNew:

    @staticmethod
    def create():
        pass

    @staticmethod
    def get_by_user(guid):
        pass

    @staticmethod
    def get_by_book(guid):
        pass

    @staticmethod
    def get_by_guid(guid):
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete(guid):
        pass


class UserNew:

    @staticmethod
    def create(data, user_id):
        result = get(f'https://localhost:5001/ServicesRest/CreateDatabaseUserCard/'
                     f'{data["first_name"]}/'
                     f'{data["last_name"]}/'
                     f'RoleUser/'
                     f'{data["gender"]}/'
                     f'{data["age"]}/'
                     f'{data["address"]}/'
                     f'{data["telephone"]}/'
                     f'{data["email"]}/'
                     f'{user_id}/'
                     f'{user_id}',
                     verify=False)
        print(result.status_code)
        if result.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def login():
        pass

    @staticmethod
    def get_by_guid(guid):
        pass

    @staticmethod
    def get_by_login(login, password):
        result = get(f'https://localhost:5001/LoginUserReadDatabaseUserCard/'
                   f'{login}/'
                   f'{password}', verify=False)
        result = decode_data(result)
        return result

    @staticmethod
    def update(data):
        pass

    @staticmethod
    def delete(guid):
        pass


def decode_data(data):
    """
        :param data: str
        :return: json
    """
    data = data.content.decode(encoding=data.encoding)
    data = json.loads(data)
    return data


if __name__ == '__main__':
    pass


