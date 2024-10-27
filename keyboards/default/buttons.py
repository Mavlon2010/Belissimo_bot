from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.db_api.db_code import ProductDB


def btn_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    menu = KeyboardButton("Menu")
    basket = KeyboardButton("Buyurtmamni ko`rsat")
    return kb.add(menu, basket)


def menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    menu = KeyboardButton("Menu")
    return kb.add(menu)


def btn_pizza_list():
    btns_pizza = ReplyKeyboardMarkup(resize_keyboard=True)
    products = ProductDB().get()
    btns = []
    for product in products:
        btn = KeyboardButton(str(product[0]))
        btns.append(btn)
    return btns_pizza.add(*btns)


def back_basket():
    btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    back = KeyboardButton("Ortga")
    basket = KeyboardButton("Savatni ko'rsat")
    buy = KeyboardButton("Buyurtmani rasmiylashtirish")
    btns.add(
        back, basket, buy
    )
    return btns


def delivery_or_take_away():
    btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    back = KeyboardButton("Olib ketish")
    basket = KeyboardButton("Yetkazib berish")
    btns.add(back, basket)
    return btns


def belissimo_branches():
    btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    yunsobod = KeyboardButton("Mega planet filliali")
    chilonzor = KeyboardButton("Chilonzor filliali")
    olmazor = KeyboardButton("Olmazor filliali")
    mirzo_ulugbek = KeyboardButton("Mirzo Ulug`bek filliali")
    sergeli = KeyboardButton("Sergeli filliali")
    yashnaobod = KeyboardButton("Aviasozlar filliali")
    pushkin = KeyboardButton("Pushkin filliali")
    chorsu = KeyboardButton("Chorsu filliali")
    yakkasaroy = KeyboardButton("Yakkasaroy filliali")
    mirobod = KeyboardButton("Mirobod filliali")
    uchtepa = KeyboardButton("Uchtepa filliali")
    urikzor = KeyboardButton("O`rikzor filliali")
    btns.add(yunsobod, chilonzor, olmazor, mirzo_ulugbek, sergeli, yashnaobod, pushkin, chorsu, yakkasaroy, mirobod,
             uchtepa, urikzor)
    return btns


def share_location():
    btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    loc = KeyboardButton("Lokatsiya yuborish", request_location=True)
    return btns.add(loc)


def share_contact():
    btns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    number = KeyboardButton("Telefon nomer yuborish", request_contact=True)
    return btns.add(number)
