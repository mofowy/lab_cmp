from lab7.api.unit_of_work import UnitOfWork
from lab7.utils.user_input import get_user_command
from lab7.utils.display import display_posts
from lab7.utils.history_logger import log_user_request
from lab7.save_data import save_to_json, save_to_csv

def main():
    uow = UnitOfWork()
    command = get_user_command()

    if command == "show posts":
        posts = uow.fetch_and_commit()
        display_posts(posts)
        log_user_request(command, posts)
        save_to_json(posts)
        save_to_csv(posts)
    else:
        print("Невідома команда")

if __name__ == "__main__":
    main()