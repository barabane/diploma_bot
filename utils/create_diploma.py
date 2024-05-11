from random import randint
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


def create_diploma(filepath: str, user_data):
    fio_text = ImageFont.truetype(font="static/arial.ttf", size=48)
    date_text = ImageFont.truetype(font="static/arial.ttf", size=28)
    project_text = ImageFont.truetype(font="static/arial.ttf", size=28)
    year_text = ImageFont.truetype(font="static/arial.ttf", size=56)

    image = Image.open(filepath)
    drawer = ImageDraw.Draw(image)

    drawer.text((670, 380), user_data["fio"],
                font=fio_text, anchor="mb", fill='#3B181D')
    drawer.text((355, 770), str(datetime.now().today().date()), anchor="ld",
                font=date_text, fill="#3B181D")
    drawer.text((700, 500), user_data["project"], anchor="mm",
                font=project_text, fill="#3B181D")
    drawer.text((905, 145), str(datetime.now().year), anchor="mm",
                font=year_text, fill="#3B181D")

    diploma_name = f"{randint(5, 1000)}.png"
    image.save(f"static/{diploma_name}")
    return diploma_name
