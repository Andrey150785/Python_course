import time
class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, tittle:str, duration: int, adult_mode:bool = False):
        self.tittle = tittle
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    def __init__(self):
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print("Вы вошли")
                return True
            else:
                print(f'Пользователь с именем с таким именем не существует')
        return False

    def register(self, nickname: str, password: str, age: int):
        new_user = User(nickname, password, age)
        for user in self.users:
            if new_user == user:
                print(f"Пользователь {nickname} уже существует")
                return None
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word: str):
        watch_list = []
        for video in self.videos:
            if search_word.lower() in video.tittle.lower():
                watch_list.append(video.tittle)
        return watch_list

    def watch_video(self, search_tittle:str):
        videos_finded = []
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return None
        for video in self.videos:
            if search_tittle.lower() == video.tittle.lower():
                videos_finded.append(video)
        if not videos_finded:
            return None
        for video in videos_finded:
            if video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return None
            while video.time_now < video.duration:
                video.time_now += 1
                print(video.time_now, end=' ')
                # time.sleep(1)
            print("Конец видео")
            video.time_now = 0

            # Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')