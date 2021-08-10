from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# --- Main Menu ---
btnMain = KeyboardButton('Вселенная')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMain)

# --- Other Menu ---
btnInfo = KeyboardButton('Отдел информации')
btnFloppa = KeyboardButton('Планета Флопп')
btnRandom = KeyboardButton('Рандомное число')
btnCats = KeyboardButton('КотоМир')
btnVideo = KeyboardButton('Планета милых видео')
btnMeow = KeyboardButton('Планета мультиков')
Menu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnInfo, btnFloppa,btnCats,btnVideo, btnMeow)