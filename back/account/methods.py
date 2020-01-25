import shutil


def pic_path(user, file_name):
    try:
        shutil.rmtree(f"media/users/{user.role}s/{user.username}/profile pic")
    except Exception as e:
        print(e)
    file_name = file_name.split('.')[1]
    return f"users/{user.latin_role}s/{user.username}/profile pic/{user.username}.{file_name}"



