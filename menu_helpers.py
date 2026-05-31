"""Хелперы для создания динамических меню."""
import database as db
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_main_menu_labels():
    """Получает названия разделов меню из БД."""
    catalog = await db.get_text("menu_catalog", "Каталог")
    selector = await db.get_text("menu_selector", "Подбор")
    cart = await db.get_text("menu_cart", "Корзина")
    info = await db.get_text("menu_info", "Информация")
    return {
        "catalog": catalog,
        "selector": selector,
        "cart": cart,
        "info": info
    }


async def build_main_menu():
    """Строит главное меню с динамическими названиями."""
    labels = await get_main_menu_labels()
    kb = InlineKeyboardBuilder()
    kb.button(text=f"📋 {labels['catalog']}",     callback_data="catalog")
    kb.button(text=f"🔍 {labels['selector']}",  callback_data="selector")
    kb.button(text=f"🛒 {labels['cart']}",       callback_data="cart")
    kb.button(text=f"💬 {labels['info']}",        callback_data="info")
    kb.adjust(2, 2)
    return kb.as_markup()
