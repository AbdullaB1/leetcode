from collections import defaultdict
d = {
    'user1': ['xxx@ya.ru', 'foo@gmail.com', 'lol@mail.ru'],
    'user2': ['foo@gmail.com', 'ups@pisem.net'],
    'user4': ['ups@pisem.net', 'aaa@bbb.ru'],

    'user3': ['xyz@pisem.net', 'vasya@pupkin.com'],
    'user5': ['xyz@pisem.net'],
    'user6': ["test1", "test2"]
}

# a = {
#     'xxx@ya.ru': ['user1'],
#     'foo@gmail.com': ['user1', 'user2'],
#     'lol@mail.ru': ['user1'],
#     'ups@pisem.net': ['user2', 'user4'],
#     'aaa@bbb.ru': ['user4'],
#     'xyz@pisem.net': ['user3', 'user5'],
#     'vasya@pupkin.com': ['user3']
# }


def append_emails(arr_email: list[str], users, cur_user: str):
    for i in users:
        if i != cur_user:
            for mail in d[i]:
                if mail not in arr_email:
                    arr_email.append(mail)
            d[i] = []


def make_graph(users: dict[str, list[str]]) -> dict[str, list[str]]:
    graph = defaultdict(list)
    for user, emails in users.items():
        for email in emails:
            graph[email].append(user)
    print(graph)
    return graph


def unit_users(users_graph: dict[str, list[str]], emails_graph: dict[str, list[str]]) -> None:
    for user, emails in users_graph.items():
        for email in emails:
            append_emails(emails, emails_graph[email], user)


if __name__ == '__main__':
    grahp = make_graph(d)
    unit_users(d, grahp)
    for i, val in d.items():
        if val:
            print(f'{i}: {val}')
