from vk_api import VkApi
import os
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def keyboard_settings():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Cookies', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Cakes', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Donuts', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_openlink_button('Links', link='https://github.com/arturgafizov')
    return keyboard


token = os.environ.get("VK_TOKEN")
authorize = VkApi(token=token)


def write_message(sender, message, attachments, keyboard):
    authorize.method("messages.send", {
        "user_id": sender,
        "message": message,
        "random_id": get_random_id(),
        'attachment': ','.join(attachments),
        "keyboard": keyboard.get_keyboard()
    })
    print(sender, message)


def main(keyboard):
    image = '/app/pngegg.png'

    longpool = VkLongPoll(authorize)
    upload = VkUpload(authorize)


    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            reseived_message = event.text
            sender = event.user_id
            attachments = []
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            if reseived_message == 'Hello':
                write_message(sender, 'Good afternoon!', attachments, keyboard)
            elif reseived_message == 'Buy':
                write_message(sender, 'Good buy!', attachments, keyboard)
            else:
                write_message(sender, "I don't understand you!", attachments, keyboard)


if __name__ == "__main__":
    keyboard = keyboard_settings()
    main(keyboard)
