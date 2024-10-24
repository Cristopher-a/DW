import flet as ft

def dsh(page):
    categoria = ft.Dropdown(
        hint_text="Categoria",
        options=[
            ft.dropdown.Option(text="Categoría 1"), 
            ft.dropdown.Option(text="Categoría 2"), 
            ft.dropdown.Option(text="Categoría 3")
        ]
    )
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    
    d = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row([
                        ft.TextField(label="Nombre del dispositivo")
                    ]),
                    ft.Row([
                        ft.TextField(label="Wats",suffix_text="W", keyboard_type=ft.KeyboardType.NUMBER)
                    ]),
                    ft.Row([
                        categoria
                    ]),
                    ft.Row([
                       ft.ElevatedButton("Choose files...",on_click=lambda _: file_picker.pick_files(allow_multiple=True))
                    ]),
                    ft.Row([
                        ft.ElevatedButton("Guardar", icon=ft.icons.CHECK,on_click=print("Hola"))
                    ]),
                ]
            ),
            width=400,
            padding=25,
        ),
        margin=ft.margin.only(top=28)
    )  
    page.add(d)
