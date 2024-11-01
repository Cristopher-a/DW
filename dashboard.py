import flet as ft

def dsh(page):
    categoria = ft.Dropdown(
        hint_text="Categoria",
        options=[
            ft.dropdown.Option(text="Computadoras"), 
            ft.dropdown.Option(text="Herramientas"), 
            ft.dropdown.Option(text="Robot"),
        ]
    )
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    
    # Controlador (formulario de entrada) - Columna Izquierda
    controller = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row([ft.TextField(label="Nombre del dispositivo")]),
                    ft.Row([ft.TextField(label="Watts", suffix_text="W", keyboard_type=ft.KeyboardType.NUMBER)]),
                    ft.Row([categoria]),
                    ft.Row([
                        ft.ElevatedButton(
                            "Choose files...",
                            on_click=lambda _: file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)
                        )
                    ]),
                    ft.Row([ft.ElevatedButton("Guardar", icon=ft.icons.CHECK)]),
                ]
            ),
            padding=25,
        )
    )  
    
    # Vista de cuadrícula para imágenes - Columna Derecha
    dash = ft.GridView(
        runs_count=3,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    # Llenado de imágenes en el GridView
    for i in range(0, 20):  # Reducido a 20 imágenes para mejor visualización
        dash.controls.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

    # Estructura de la interfaz con controller y dash en columnas separadas sin expansión vertical
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Column([controller]),
                    width=400,  # Ancho fijo solo horizontalmente
                    alignment=ft.alignment.top_left  # Alineación superior izquierda
                ),
                ft.Container(
                    content=ft.Column([dash]),
                    width=600,  # Ancho fijo solo horizontalmente
                    alignment=ft.alignment.top_left  # Alineación superior izquierda
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20  # Espaciado entre las dos columnas
        )
    )

if __name__ == "__main__":
    ft.app(target=dsh)
