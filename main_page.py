import flet as ft  

def main():  
    pass  

def create_main_page(page):  

    return ft.Column([
        ft.Text("Dictionary - The Definition Game", style="headlineMedium"),
        ft.Divider(),
        ft.FilledTonalButton("New Game", on_click=lambda _: page.go("/game")),
        ft.FilledTonalButton("Settings", on_click=lambda _: page.go("/settings")),
        ft.FilledTonalButton("Exit", on_click=lambda _: page.window.close()),
    ], alignment="center", horizontal_alignment="center")

if __name__ == "__main__":  
    main()
