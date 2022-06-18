from collections import defaultdict


def join_users(user_emails: dict[str, list[str]]) -> dict[str, list[str]]:
    email_users = {}
    users_joins = defaultdict(lambda: None)
    for user_id in user_emails:
        emails = user_emails[user_id]
        for e in emails:
            if e not in email_users:
                email_users[e] = user_id
            else:
                cur_child = email_users[e]
                # если у пользователя, которого мы хотим присоединить к себе,
                # уже есть родитель, то ищем его корневого родителя
                # если другой email уже успел соединить этих пользователей, то ничего не поменяется
                while users_joins[cur_child] != None and users_joins[cur_child] != user_id:
                    cur_child = users_joins[cur_child]
                users_joins[cur_child] = user_id

    print(*users_joins.items(), sep="\n")
    roots = {}
    for ue in user_emails:
        if ue not in users_joins:
            roots[ue] = [user_emails[ue]]
    for uj in users_joins:
        emails_for_join = user_emails[uj]
        cur_user = uj
        while cur_user not in roots:
            cur_user = users_joins[cur_user]
        roots[cur_user].append(emails_for_join)
    print(roots)
    for root in roots:
        email_list = roots[root]
        roots[root] = set([el for lst in email_list for el in lst])
    print(*roots.items(), sep="\n")


users = {
    "user1": ["xxx@ya.ru", "foo@gmail.com", "lol@mail.ru"],
    "user2": ["foo@gmail.com", "ups@pisem.net"],
    "user4": ["ups@pisem.net", "aaa@bbb.ru"],
    "user3": ["xyz@pisem.net", "vasya@pupkin.com"],
    "user5": ["xyz@pisem.net"],
    "user6": ["test1", "test2"]
}


join_users(users)
