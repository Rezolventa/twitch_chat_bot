from pymongo import MongoClient
from settings import IGNORED_USERS, VIEWER_XP_PER_LEVEL_PROGRESSION
import time


# получить данные пользователя - словарь
def get_viewer_data(user):
    res = collection.find({'user': user})
    if res.count() > 0:
        return res[0]
    return None


# процедура, вызываемая при каждом сообщении, проверяет, как давно пользователь отправил предыдущее
# если прошла минута, добавляет опыт и монетку
def pay_xp_coins(user_obj):
    user = user_obj.name
    if user in IGNORED_USERS:
        return
    viewer_data = get_viewer_data(user)
    print('viewer_data :', viewer_data)
    new_xp_date = int(time.time())
    if not viewer_data:
        # new user
        new_doc = {'user': user, 'xp' : 1, 'coins' : 1, 'xp_date': new_xp_date}
        collection.insert(new_doc)
        return
    old_xp_date = viewer_data.get('xp_date')

    # сабы получают больше
    value = 2 if user_obj.is_subscriber else 1

    if new_xp_date - old_xp_date > 60:
        collection.update_one({'_id': viewer_data.get('_id')}, {
            '$set': {'xp_date': new_xp_date, 'xp': viewer_data.get('xp') + value,
                     'coins': viewer_data.get('coins') + value}},
                              upsert=False)
        print(str(value), 'xp added to', user.upper(), 'delta time:', new_xp_date - old_xp_date) #del


def give_minerals(user, count):
    viewer_data = get_viewer_data(user)
    collection.update_one({'_id': viewer_data.get('_id')}, {
        '$set': {'coins': viewer_data.get('coins') + count}},
                          upsert=False)


def charge_minerals(user, count):
    viewer_data = get_viewer_data(user)
    if viewer_data.get('coins') >= count:
        collection.update_one({'user': user}, {
            '$set': {'coins': viewer_data.get('coins') - count}},
                              upsert=False)
        return True
    return False


def get_xp_data(user):
    viewer_data = get_viewer_data(user)
    if not viewer_data:
        return

    xp_counter = viewer_data.get('xp')
    i = 0
    last_xp_for_level = 0
    while True:

        if i < len(VIEWER_XP_PER_LEVEL_PROGRESSION):
            xp_for_i = VIEWER_XP_PER_LEVEL_PROGRESSION[i]
            last_xp_for_level = VIEWER_XP_PER_LEVEL_PROGRESSION[i]
        # за пределами списка берем посление значения - это верхний кап экспы на уровень
        else:
            xp_for_i = VIEWER_XP_PER_LEVEL_PROGRESSION[-1]
            last_xp_for_level = VIEWER_XP_PER_LEVEL_PROGRESSION[-1]

        # если в счетчике не хватает экспы на этот уровень - разрываем
        if xp_counter - xp_for_i < 0:
            xp = xp_counter
            break

        # а если хватает, повторяем
        xp_counter -= xp_for_i
        i += 1

    return {'lvl': i, 'xp': xp, 'xp_for_level': last_xp_for_level, 'coins': viewer_data.get('coins')}


def null_clicks():
    found = collection.find({'user': 'system'})
    if found.count() == 1:
        collection.update_one({'_id': found[0].get('_id')}, {
            '$set': {'clicks': 0}},
                       upsert=False)


def add_click():
    found = collection.find({'user': 'system'})
    if found.count() == 1:
        new_count = found[0].get('clicks') + 1
        collection.update_one({'_id': found[0].get('_id')}, {
            '$set': {'clicks': new_count}},
                       upsert=False)
        return new_count
    elif found.count() == 0:
        collection.insert_one({'user': 'system', 'clicks': 1})
        return 1


client = MongoClient()
collection = client.admin.twitch_chat_parser
null_clicks()