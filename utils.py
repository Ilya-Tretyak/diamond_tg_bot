
def generation_create_for_user(class_obj, keyboard_buttons):
    """Функция генерирующая 'text' из callback-ов получивших с InlineButton"""
    """func(class_obj: CallbackQuery/Message, keyboard_buttons: list[InlineButton])"""
    for i in range(0, len(keyboard_buttons)):
        for j in range(0, len(keyboard_buttons[i])):
            if class_obj.data == keyboard_buttons[i][j].callback_data:
                return keyboard_buttons[i][j].text
