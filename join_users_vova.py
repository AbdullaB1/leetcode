import json
from collections import defaultdict, deque


# можно предстаивть азадчу как переходы между двудольными графами
# users -> [emails] и email -> [users]
# делаем обход по графу в ширину, если во время прохода наткнулись на email,
# то добавляем его к результату для пользователя, от коротого начали обход,
# и все пройденные вершины добавляем в seen, чтобы нигде не пройтись дважды
def join_users(user_emails: dict[str, list[str]]) -> dict[str, list[str]]:
    email_users = defaultdict(list)
    for user_id in user_emails.keys():
        for email in user_emails[user_id]:
            email_users[email].append(user_id)
    used = set()
    result = defaultdict(list)
    for user_id in user_emails.keys():

        if user_id in used:
            continue

        queue = deque([user_id])

        while queue:
            node_name = queue.popleft()
            used.add(node_name)
            nodes_to = user_emails
            if node_name in email_users:
                result[user_id].append(node_name)
                nodes_to = email_users
            for to in nodes_to[node_name]:
                if to not in used:
                    queue.append(to)

    return result


users = {
    "user1": ["xxx@ya.ru", "foo@gmail.com", "lol@mail.ru"],
    "user2": ["foo@gmail.com", "ups@pisem.net"],
    "user4": ["ups@pisem.net", "aaa@bbb.ru"],
    "user3": ["xyz@pisem.net", "vasya@pupkin.com"],
    "user5": ["xyz@pisem.net"],
    "user6": ["test1", "test2"]
}

print(json.dumps(join_users(users), indent=4))
