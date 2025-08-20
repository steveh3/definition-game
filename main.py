import flet as ft
from main_page import create_main_page
from game_page import create_game_page

def main(page: ft.Page):
    # Page routes
    def route_change(e: ft.RouteChangeEvent):
        page.controls.clear()
        if e.route == "/":
            page.add(create_main_page(page))
        elif e.route == "/game":
            page.add(create_game_page(page))
        elif e.route == "/settings":
            page.add(
                ft.Column([
                    ft.Text("Settings Page", style="headlineMedium"),
                    ft.Text("Modify your settings here."),
                    ft.ElevatedButton("Back to Main", on_click=lambda _: page.go("/")),
                ], alignment="center", horizontal_alignment="center")
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)

'''ft.Column([  
        #ft.Text("Generate Page Content"),  
        ft.Row([  
            ft.FilledTonalButton("New", icon=ft.Icons.ADD_OUTLINED),  
            ft.FilledTonalButton("Save", icon=ft.Icons.SAVE_AS_OUTLINED),  
            ft.FilledTonalButton("Export", icon=ft.Icons.IMPORT_EXPORT_OUTLINED),             
        ]),  
        ft.Divider(),  '''