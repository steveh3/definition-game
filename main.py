import flet as ft
from main_page import create_main_page
from game_page import create_game_page
from settings_page import create_settings_page

def main(page: ft.Page):
    # Page routes
    def route_change(e: ft.RouteChangeEvent):
        page.controls.clear()
        if e.route == "/":
            page.add(ft.Container(content=create_main_page(page)))
        elif e.route == "/game":
            page.add(ft.Container(content=create_game_page(page)))
        elif e.route == "/settings":
            page.add(ft.Container(content=create_settings_page(page)))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="src/assets")