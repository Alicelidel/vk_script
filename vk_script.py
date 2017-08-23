import vk
import time
from settings import user_id, user_login, user_password, app_id


#подключаемся к сайту
#для подключения необходимо ввести id приложения, логин и пароль
session = vk.AuthSession(app_id, user_login, user_password, scope='wall, friends')
vk_api = vk.API(session)

#получаем список друзей в формате словаря
friends = vk_api.friends.get(fields='deactivated')

print(friends)
#проверяем статус каждого друга
for friend in friends:

    #задержка нужна потому что вк не любит частые запросы
    time.sleep(5)
    print('Проверяем статус пользователя', friend['first_name'])

    #если у пользователя есть статус деактивейтид значит он либо удалён либо забанен.
    if 'deactivated' in friend:
        print('Этот друг сейчас будет удалён')
        vk_api.friends.delete(user_id=friend['uid'])