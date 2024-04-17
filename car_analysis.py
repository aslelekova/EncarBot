# car_analysis.py
import locale

from aiogram.utils.markdown import hbold, hlink


def analyze_car_data(data):
    for item in data:
        # Extracting brand, model, and price information from the data.
        brand = item.get("vehicle_info", {}).get("mark_info", {}).get("code", "").lower()
        model = item.get("vehicle_info", {}).get("model_info", {}).get("code", "").lower()
        generation = item.get("vehicle_info", {}).get("super_gen", {}).get("name", "").lower()
        price = item.get("price_info", {}).get("price", "")

        # Getting information about whether the car is new or used.
        is_used = item.get("section") == "used"
        complectation_id = item.get("vehicle_info", {}).get("complectation", {}).get("id", "")
        tech_param_id = item.get("vehicle_info", {}).get("tech_param", {}).get("id", "")
        sale_id = item.get("saleId", "")

        # Formatting the base part of the link.
        base_link = f"https://auto.ru/cars/"

        # Adding type of the car (new or used) to the link.
        if is_used:
            base_link += f"used/sale/{brand.lower()}/{model.lower()}/{sale_id}/"
        else:
            base_link += f"new/group/{brand.lower()}/{model.lower()}/{tech_param_id}/{complectation_id}/{sale_id}"

        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

        formatted_price = locale.format_string("%.0f", price, grouping=True)

        # Generating the card with car details and link.
        card = (
            f"{hlink(f'{brand.upper()} {model.title()} {generation.upper()}', base_link)}\n\n"
            f"{hbold('Модель: ')} {model.title()}\n"
            f"{hbold('Цена: ')} {formatted_price} ₽\n"
        )

        return card
