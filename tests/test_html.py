from bs4 import BeautifulSoup
import os

def test_index_html_exists():
    assert os.path.exists("index.html"), "Файл index.html не найден"

def test_button_and_background():
    with open("index.html", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Проверка на наличие кнопки
    button = soup.find("button")
    assert button is not None, "Кнопка <button> не найдена в index.html"

    # Проверка на цвет фона (ищем inline CSS или <style>)
    style_tags = soup.find_all("style")
    has_background = False
    for style in style_tags:
        if "background-color" in style.text:
            has_background = True
            break
    assert has_background, "Фон с цветом (background-color) не найден в <style>"
