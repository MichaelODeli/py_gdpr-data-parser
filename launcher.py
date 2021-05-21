from consolemenu import *
from consolemenu.items import *
import emoji
current_version='0.1.1-alpha'
def notReady():
    print('This feature is not avaliable.')
    input()
DiscordMenu = ConsoleMenu("GDPR Parcer. Discord", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
DiscordMenu1 = FunctionItem('Name', notReady)
DiscordMenu2 = FunctionItem('Name', notReady)
DiscordMenu3 = FunctionItem('Name', notReady)
DiscordMenu.append_item(DiscordMenu1)
DiscordMenu.append_item(DiscordMenu2)
DiscordMenu.append_item(DiscordMenu3)

GoogleMenu = ConsoleMenu("GDPR Parcer. Google", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
GoogleMenu1 = FunctionItem('Name', notReady)
GoogleMenu2 = FunctionItem('Name', notReady)
GoogleMenu3 = FunctionItem('Name', notReady)
GoogleMenu.append_item(GoogleMenu1)
GoogleMenu.append_item(GoogleMenu2)
GoogleMenu.append_item(GoogleMenu3)

MailRUMenu = ConsoleMenu("GDPR Parcer. MailRU", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
MailRUMenu1 = FunctionItem('Name', notReady)
MailRUMenu2 = FunctionItem('Name', notReady)
MailRUMenu3 = FunctionItem('Name', notReady)
MailRUMenu.append_item(MailRUMenu1)
MailRUMenu.append_item(MailRUMenu2)
MailRUMenu.append_item(MailRUMenu3)

TelegramMenu = ConsoleMenu("GDPR Parcer. Telegram", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
TelegramMenu1 = FunctionItem('Name', notReady)
TelegramMenu2 = FunctionItem('Name', notReady)
TelegramMenu3 = FunctionItem('Name', notReady)
TelegramMenu.append_item(TelegramMenu1)
TelegramMenu.append_item(TelegramMenu2)
TelegramMenu.append_item(TelegramMenu3)

TikTokMenu = ConsoleMenu("GDPR Parcer. TikTok", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
TikTokMenu1 = FunctionItem('Name', notReady)
TikTokMenu2 = FunctionItem('Name', notReady)
TikTokMenu3 = FunctionItem('Name', notReady)
TikTokMenu.append_item(TikTokMenu1)
TikTokMenu.append_item(TikTokMenu2)
TikTokMenu.append_item(TikTokMenu3)

VKMenu = ConsoleMenu("GDPR Parcer. VK", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
VKMenu1 = FunctionItem('Name', notReady)
VKMenu2 = FunctionItem('Name', notReady)
VKMenu3 = FunctionItem('Name', notReady)
VKMenu.append_item(VKMenu1)
VKMenu.append_item(VKMenu2)
VKMenu.append_item(VKMenu3)

WhatsAppMenu = ConsoleMenu("GDPR Parcer. WhatsApp", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
WhatsAppMenu1 = FunctionItem('Name', notReady)
WhatsAppMenu2 = FunctionItem('Name', notReady)
WhatsAppMenu3 = FunctionItem('Name', notReady)
WhatsAppMenu.append_item(WhatsAppMenu1)
WhatsAppMenu.append_item(WhatsAppMenu2)
WhatsAppMenu.append_item(WhatsAppMenu3)

YandexMenu = ConsoleMenu("GDPR Parcer. Yandex", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
YandexMenu1 = FunctionItem('Name', notReady)
YandexMenu2 = FunctionItem('Name', notReady)
YandexMenu3 = FunctionItem('Name', notReady)
YandexMenu.append_item(YandexMenu1)
YandexMenu.append_item(YandexMenu2)
YandexMenu.append_item(YandexMenu3)

# Show - menus - for - applications
def showDiscordPanel():
    DiscordMenu.show()
def showGooglePanel():
    GoogleMenu.show()
def showMailRUPanel():
    MailRUMenu.show()
def showTelegramPanel():
    TelegramMenu.show()
def showTikTokPanel():
    TikTokMenu.show()
def showVKPanel():
    VKMenu.show()
def showWhatsAppPanel():
    WhatsAppMenu.show()
def showYandexPanel():
    YandexMenu.show()


mainMenu = ConsoleMenu("GDPR Parcer", current_version, exit_option_text='Выход', prologue_text='Выберите необходимый Вам сервис', epilogue_text='Приложение представляет из себя парсер репортов GDPR данных и их визуализацию.')
mainMenuItem1 = FunctionItem('Discord', showDiscordPanel)
mainMenuItem2 = FunctionItem('Google', showGooglePanel)
mainMenuItem3 = FunctionItem('Mail.ru', showMailRUPanel)
mainMenuItem4 = FunctionItem('Telegram', showTelegramPanel)
mainMenuItem5 = FunctionItem('TikTok', showTikTokPanel)
mainMenuItem6 = FunctionItem('VK', showVKPanel)
mainMenuItem7 = FunctionItem('WhatsApp', showWhatsAppPanel)
mainMenuItem8 = FunctionItem('Yandex', showYandexPanel)

mainMenu.append_item(mainMenuItem1)
mainMenu.append_item(mainMenuItem2)
mainMenu.append_item(mainMenuItem3)
mainMenu.append_item(mainMenuItem4)
mainMenu.append_item(mainMenuItem5)
mainMenu.append_item(mainMenuItem6)
mainMenu.append_item(mainMenuItem7)
mainMenu.append_item(mainMenuItem8)
mainMenu.show()