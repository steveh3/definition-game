import flet as ft  
import json
import random
import os

def main():  
    pass  

def extract_meaning(dictionary_entry):
    # Try to extract the first MEANINGS entry's description
    meanings = dictionary_entry.get("MEANINGS", [])
    if meanings and isinstance(meanings, list):
        # meanings is a list of lists: [PoS, description, [categories], [examples]]
        first_meaning = meanings[0]
        if len(first_meaning) > 1:
            return f"{first_meaning[0]}: {first_meaning[1]}"
    return "No definition available"

def create_game_page(page):  
    # Read dictionary.json

    try:
        base_path = os.getenv("FLET_APP_STORAGE_DATA") 
        if not base_path:  
            base_path = os.getcwd()   
        dict_path = os.path.join(base_path, "dictionary.json") 
        with open(dict_path, "r", encoding="utf-8") as f:
            dictionary = json.load(f)
        # Filter words with valid definitions
        words = [
            word for word in dictionary.keys()
            if extract_meaning(dictionary.get(word, {}).get("dictionary", {})) != "No definition available"
        ]
    except Exception as e:
        print("Error loading dictionary:", e)
        words = []
        dictionary = {}

    # Difficulty range slider
    difficulty_slider = ft.RangeSlider(
        min=0.0,
        max=1.0,
        divisions=100,
        start_value=0.0,
        end_value=1.0,
        label="{value}",
        tooltip="Select difficulty range",
    )

    # Text widget to show current slider values
    slider_value_text = ft.Text(
        f"{difficulty_slider.start_value:.2f} - {difficulty_slider.end_value:.2f}"
    )

    def on_slider_change(e):
        slider_value_text.value = (
            f"{difficulty_slider.start_value:.2f} - {difficulty_slider.end_value:.2f}"
        )
        page.update()

    difficulty_slider.on_change = on_slider_change

    # ListView for word tiles, initially empty
    word_tiles_listview = ft.ListView(
        controls=[],
        expand=0,
        spacing=5,
    )

    def get_filtered_random_words():
        try:
            min_score = difficulty_slider.start_value
            max_score = difficulty_slider.end_value
            filtered = []
            for word in words:
                entry = dictionary.get(word, {})
                score = float(entry.get("weighted_score", 0))
                if min_score <= score <= max_score:
                    filtered.append(word)
            if len(filtered) >= 5:
                return random.sample(filtered, 5)
            return filtered
        except Exception as e:
            print("Error in get_filtered_random_words:", e)
            return []

    def refresh_words(_):
        selected_words = get_filtered_random_words()
        word_tiles_listview.controls.clear()
        for word in selected_words:
            entry = dictionary.get(word, {})
            dict_entry = entry.get("dictionary", {})
            meaning = extract_meaning(dict_entry)
            part_of_speech, definition = meaning.split(': ', 1)
            score = entry.get('weighted_score', 'N/A')
            word_tiles_listview.controls.append(
                ft.ListTile(
                    title=ft.Text(word, style="headlineSmall", weight=ft.FontWeight.BOLD),
                    subtitle=ft.Column([
                        ft.Text(definition, style="bodyMedium"),
                        ft.Text(f"{part_of_speech} | Score: {score}", style="bodySmall", color=ft.Colors.GREY)
                    ])
                )
            )
        page.update()

    # Difficulty category labels
    difficulty_labels = [
        ft.Row([
            ft.Text("Easy"),
            ft.Text("Medium"),
            ft.Text("Hard"),
        ], alignment="spaceBetween"),
    ]

    # UI for game page
    return ft.Column([
        ft.Text("Dictionary - The Definition Game", style="headlineMedium"),
        ft.Divider(),
        ft.Column([
            
            *difficulty_labels,
            difficulty_slider,
            ft.Text("Select difficulty range:", weight=ft.FontWeight.BOLD, scale=1.5),
            slider_value_text,  
            ft.FilledTonalButton("Refresh Words", on_click=refresh_words),
            word_tiles_listview,
            ft.Divider(),
            ft.FilledTonalButton("Back to Main", on_click=lambda _: page.go("/")),
        ], alignment="center", horizontal_alignment="center", scroll="auto")
    ], alignment="center", horizontal_alignment="center", scroll="auto")

if __name__ == "__main__":  
    main()