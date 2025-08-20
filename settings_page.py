import flet as ft  
from settings import AppSettings   

def main():  
    pass       

def create_settings_page(page):  
    settings = AppSettings()  
    def change_setting(e):  
        settings.set_setting(e.control.label,e.control.value)  

    return ft.Column([
        ft.Text(f"Author: {settings.get_setting('Author')}"),
        ft.Text(f"Version: {settings.get_setting('Version')}"),
        ft.Divider(),
        ft.Row([ft.Switch(
            label="Setting1",
            value=settings.get_setting("Setting1"),
            on_change=change_setting,
        )], alignment="center"),
        ft.Row([ft.Switch(
            label="Setting2",
            value=settings.get_setting("Setting2"),
            on_change=change_setting,
        )], alignment="center"),
        ft.Divider(),
        ft.FilledTonalButton("Back to Main", on_click=lambda _: page.go("/")),
    ], alignment="center", horizontal_alignment="center")


if __name__ == "__main__":  
    main()