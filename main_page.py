import flet as ft  

def main():  
    pass  

def create_main_page(page):  

    return ft.Column([
        ft.Row([  
            ft.FilledTonalButton("New", icon=ft.Icons.ADD_OUTLINED),  
            ft.FilledTonalButton("Save", icon=ft.Icons.SAVE_AS_OUTLINED),  
            ft.FilledTonalButton("Export", icon=ft.Icons.IMPORT_EXPORT_OUTLINED),             
        ]),  
        ft.Divider(), 
        ft.Text("Definition Game", style="headlineMedium"),
        ft.FilledTonalButton("Create New Game", on_click=lambda _: page.go("/game")),
        ft.FilledTonalButton("Settings", on_click=lambda _: page.go("/settings")),
        ft.FilledTonalButton("Exit", on_click=lambda _: page.window_close()),
    ], alignment="center", horizontal_alignment="center")

if __name__ == "__main__":  
    main()


                