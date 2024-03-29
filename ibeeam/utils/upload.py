import random


def get_user_avatar_path(instance, filename):
    random_number = random.randint(0, 2048)
    name, extension = filename.split('.')
    return 'user_avatars/{}/{}.{}'.format(instance.id, random_number, extension)


def get_post_image_path(instance, filename):
    random_number = random.randint(0, 2048)
    name, extension = filename.split('.')
    return 'post_images/{}/{}.{}'.format(instance.id, random_number, extension)
