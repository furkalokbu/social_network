import json
import random
from django.core.management.base import BaseCommand

from apps.posts.models import Post
from apps.users.models import User

FILE_NAME_BOT_CONFIG = 'bot_config.json'
PASSWORD_FOR_USER = 'qwerty'


def read_config():
    with open(FILE_NAME_BOT_CONFIG, 'r') as config_file:
        config = json.load(config_file)
    return config


def create_bot_activity(**config):
    # Create users
    for i in range(config['number_of_users']):
        user = User.objects.create_user(username=f'user_{i}', password=PASSWORD_FOR_USER)

        # Create posts for each user
        num_posts = random.randint(1, config['max_posts_per_user'])
        for j in range(num_posts):
            title = f"Post title by {user.username}"
            body = f"Post body content by {user.username}"
            post = Post(author=user, title=title, body=body)
            post.save()

            # Create randomly like for each posts
            for item in range(random.randint(0, config['max_likes_per_user'])):
                user_to_like = User.objects.get(username=random.choice(User.objects.all()))
                post.liked.add(user_to_like)


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            config = read_config()
            create_bot_activity(**config)
            return f'The bot successfully completed its task'
        except Exception:
            raise 'There is a problem with the bot'
