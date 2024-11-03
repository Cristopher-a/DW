import flet as ft

def dsh(page):
  
    is_mobile = page.width < 600  
    if not is_mobile:
        page.window.maximized = True
    
    grid_view = ft.GridView(
        expand=False,  
        max_extent=300 if not is_mobile else 150,  
        spacing=10, 
        run_spacing=10,   
        height=800 if not is_mobile else 400, 
    )
    
    
    type_dropdown = ft.Dropdown(
        hint_text="Categoria",
        options=[
            ft.dropdown.Option(text="Computadoras"), 
            ft.dropdown.Option(text="Herramientas"), 
            ft.dropdown.Option(text="Robot"),
        ]
    )
    name = ft.TextField(label="Nombre del dispositivo")
    watts = ft.TextField(label="Watts", suffix_text="W", keyboard_type=ft.KeyboardType.NUMBER)
    file_picker = ft.FilePicker()
    files = ft.ElevatedButton(
        "Choose files...",
        on_click=lambda _: file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)
    )
    page.overlay.append(file_picker)

    def agregar(e):
        nombre = name.value
        wts = watts.value
        categoria = type_dropdown.value
        content = ft.Card(
            content=ft.Column([
                ft.Text(f"Nombre: {nombre}"),
                ft.Text(f"Categoria: {categoria}"),
                ft.Text(f"Watts: {wts}"),
            ])
        )
        grid_view.controls.append(content)
        page.update()

    controller = ft.Row([
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([name]),
                    ft.Row([watts]),
                    ft.Row([type_dropdown]),
                    ft.Row([files]),
                    ft.Row([ft.ElevatedButton("Guardar", icon=ft.icons.CHECK, on_click=agregar)]),
                ]),
                padding=25,
                width=300 if is_mobile else 400 
            )
        ),
        ft.Container(
            content=grid_view,
            width=500 if is_mobile else 1000, 
            bgcolor="green200"  
        )
    ])
    page.add(controller)

if __name__ == "__main__":
    ft.app(target=dsh)
