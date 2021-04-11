import datetime
from Vk_Yandex import Vk_image_saver, Yandex_uploader

today = datetime.datetime.today().strftime("%Y-%m-%d-%S")
my_path = f'C:/{today}/'
ya_disk_api = input("Введите Ваш Yandex API token: ")
token = input("Введите Ваш VK token: ")

vk1 = Vk_image_saver(token, my_path)
vk1.get_albums()
vk1.get_photo(None, int(input("Введите id альбома: ")))
vk1.save_photo(int(input("Введите количество файлов для скачивания: ")))
ya1 = Yandex_uploader(ya_disk_api)
ya1.upload()