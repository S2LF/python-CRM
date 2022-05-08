"""Module to generate random users"""
from faker import Faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(level=logging.WARNING, filename=BASE_DIR / "logs" /"user.log")

print(BASE_DIR)

fake = Faker()


def get_user() -> str:
    """Function to create a user with Faker

    Returns:
        str: user
    """
    logging.info("Creating a user")
    return fake.name()


def get_users(nb: int) -> list:
    """Function to create a list of users with Faker

    Args:
        nb (int): number of users to create

    Returns:
        list[str]: users
    """
    try :
        logging.info(f"Creating {nb} users")
        return [get_user() for _ in range(nb)]
    except TypeError:
        logging.error(f"Wrong type of argument ({nb})")
        print("Veuillez entrer un nombre entier")
        return []

if __name__ == "__main__":
    print(get_user())
    print(get_users(5))
    print(get_users("d"))