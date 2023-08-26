from requests import get
import json
from pprint import pprint
import datetime
from random import shuffle

from authapp.models import User
from mainapp.models import ImageBook, ImageNews


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
    def get_all():
        basket_base = get('https://localhost:5001/ServicesRest/ReadDatabaseBascets', verify=False)
        baskets = []
        for item in decode_data(basket_base):
            basket = {
                'id': item['IdUser'],
                'name': item['IdBook'],
                'author': item['QuantityBooks'],
                'foto': item['PricePerBook'],
            }
            baskets.append(basket)
        return baskets

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

    @staticmethod
    def random():
        data = QuoteNew.get_all()
        shuffle(data)
        return data

    @staticmethod
    def get_sorted(o_field):
        books = QuoteNew.get_all()
        books.sort(key=lambda dictionary: dictionary[o_field])
        return books

    @staticmethod
    def get_search(o_field, s_filed):
        books = QuoteNew.get_all()
        books.sort(key=lambda dictionary: dictionary[o_field])
        books_list = [x for x in books if s_filed.lower() in x['name'].lower() or s_filed.lower() in x['text'].lower() or s_filed.lower() in x['author'].lower()]
        return books_list


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
    def get_all():

        users_base = get('https://localhost:5001/ServicesRest/ReadDatabaseUserCard', verify=False)
        all_users = []
        for item in decode_data(users_base):
            news = {
                'id': item['idUser'],
                'first_name': item['userName'],
                'last_name': item['surnameUser'],
                'in_group': item['roleUser'],
                'gender': item['floorUser'],
                'age': item['ageUser'],
                'address': item['addressUser'],
                'telephone': item['telephoneUser'],
                'email': item['emailUser'],

                'date_create': datetime.datetime.strptime(item['dateCreationUser'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
                'date_update': datetime.datetime.strptime(item['updateDateUser'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
            }
            all_users.append(news)
        return all_users

    @staticmethod
    def get_by_guid(guid):
        if not guid:
            return False
        get_user_data = get(f'https://localhost:5001/ServicesRest/IDReadDatabaseUserCard/{guid}', verify=False)
        item = decode_data(get_user_data)
        user_data = {
            'id': item['idUser'],
            'first_name': item['userName'],
            'last_name': item['surnameUser'],
            'in_group': item['roleUser'],
            'gender': item['floorUser'],
            'age': item['ageUser'],
            'address': item['addressUser'],
            'telephone': item['telephoneUser'],
            'email': item['emailUser'],

            'date_create': datetime.datetime.strptime(item['dateCreationUser'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
            'date_update': datetime.datetime.strptime(item['updateDateUser'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
        }
        return user_data

    @staticmethod
    def get_last():
        return UserNew.get_all()[-1]

    @staticmethod
    def create(data):

        result = get(f'https://localhost:5001/ServicesRest/CreateDatabaseUserCard/'
                     f'{data["first_name"]}/'
                     f'{data["last_name"]}/'
                     f'Customer/'
                     f'{data["gender"]}/'
                     f'{data["age"]}/'
                     f'{data["address"]}/'
                     f'{data["telephone"]}/'
                     f'{data["email"]}/'
                     f'LoginUser/'
                     f'PasswordUser',
                     verify=False)
        if result.status_code == 200:
            return UserNew.get_last()['id']
        else:
            return False

    @staticmethod
    def login():
        pass

    @staticmethod
    def get_by_login(login, password):
        result = get(f'https://localhost:5001/LoginUserReadDatabaseUserCard/'
                   f'{login}/'
                   f'{password}', verify=False)
        result = decode_data(result)
        return result

    @staticmethod
    def get_group(guid):
        get_user_data = get(f'https://localhost:5001/ServicesRest/IDReadDatabaseUserCard/{guid}', verify=False)
        item = decode_data(get_user_data)
        return item["roleUser"]

    @staticmethod
    def update(data, guid):

        if not data.get('in_group'):
            group = UserNew.get_group(guid)
        else:
            group = data["in_group"]

        result = get(f'https://localhost:5001/ServicesRest/UpdateDatabaseUserCard/'
                     f'{guid}/'
                     f'{data["first_name"]}/'
                     f'{data["last_name"]}/'
                     f'{group}/'
                     f'{data["gender"]}/'
                     f'{data["age"]}/'
                     f'{data["address"]}/'
                     f'{data["telephone"]}/'
                     f'{data["email"]}/'
                     f'LoginUser/'
                     f'PasswordUser', verify=False)
        if result.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def delete(guid):
        pass


class NewsNew:
    @staticmethod
    def get_all():
        news_base = get('https://localhost:5001/ServicesRest/ReadDatabaseNewsCard', verify=False)
        all_news = []
        for item in decode_data(news_base):
            news = {
                'id': item['idNewsCard'],
                'name': item['headlineNews'],
                'description': item['contentNews'],
                'text': item['newsText'],

                'date_create': datetime.datetime.strptime(item['creationDate'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
                'date_update': datetime.datetime.strptime(item['updateDate'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
            }
            image = ImageNews.objects.filter(guid=news['id']).first()
            if image:
                news['foto'] = image.foto.url
            all_news.append(news)
        return all_news

    @staticmethod
    def get_last():
        return NewsNew.get_all()[-1]

    @staticmethod
    def get_by_guid(guid):
        get_book = get(f'https://localhost:5001/ServicesRest/IDReadDatabaseBookCard/{guid}', verify=False)
        item = decode_data(get_book)
        news = {
            'id': item['idNewsCard'],
            'name': item['headlineNews'],
            'description': item['gfhjfg'],
            'text': item['newsText'],

            'date_create': datetime.datetime.strptime(item['dateCreationBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
            'date_update': datetime.datetime.strptime(item['dateUpdateBook'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date(),
        }
        image = ImageNews.objects.filter(guid=news['id']).first()
        if image:
            news['foto'] = image.foto.url
        return news

    @staticmethod
    def create(data):
        result = get(f'https://localhost:5001/ServicesRest/CreateDatabaseNewsCard/'
                     f'{data["name"]}/'
                     f'{data["description"]}/'
                     f'{data["text"]}',
                     verify=False)
        if result.status_code == 200:
            return NewsNew.get_last()['id']
        else:
            return False

    @staticmethod
    def update(data, guid):
        result = get(f'https://localhost:5001/UpdateDatabaseNewsCard/'
                     f'{data["name"]}/'
                     f'{data["description"]}/'
                     f'{data["text"]}', verify=False)
        if result.status_code == 200:
            return guid
        else:
            return False

    @staticmethod
    def delete(guid):
        return get(f'https://localhost:5001/DeleteDatabaseNewsCard/{guid}', verify=False)

    @staticmethod
    def get_all_reverse():
        news = NewsNew.get_all()
        news.reverse()
        return news


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


