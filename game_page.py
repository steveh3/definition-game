import flet as ft  

def main():  
    pass  

def create_game_page(page):  

    return ft.Column([
        ft.Row([  
            ft.FilledTonalButton("New", icon=ft.Icons.ADD_OUTLINED),  
            ft.FilledTonalButton("Save", icon=ft.Icons.SAVE_AS_OUTLINED),  
            ft.FilledTonalButton("Export", icon=ft.Icons.IMPORT_EXPORT_OUTLINED),             
        ]),  
        ft.Divider(), 
        ft.Column([
            ft.Text("Game Page", style="headlineMedium"),
            ft.Text("Choose your game options below."),
            ft.ElevatedButton("Start Game"),
            ft.ElevatedButton("Back to Main", on_click=lambda _: page.go("/")),
        ], alignment="center", horizontal_alignment="center")
    ], alignment="center", horizontal_alignment="center")

if __name__ == "__main__":  
    main()


                