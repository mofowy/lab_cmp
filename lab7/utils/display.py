from prettytable import PrettyTable
from colorama import Fore, Style

def display_posts(posts):
    table = PrettyTable(["ID", "Title", "Body"])
    for post in posts:
        table.add_row([post['id'], post['title'], post['body']])
    print(Fore.CYAN + table.get_string() + Style.RESET_ALL)