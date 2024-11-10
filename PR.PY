import flet as ft

def main(page: ft.Page):
    # Función para mostrar el submenú al pasar el cursor sobre el botón principal
    def show_submenu(e):
        submenu.visible = True
        page.update()

    # Función para ocultar el submenú al salir del área del submenú
    def hide_submenu(e):
        submenu.visible = False
        page.update()

    # Crear el botón principal con evento on_hover
    main_button = ft.TextButton(
        "Opciones",
        on_hover=lambda e: show_submenu(e) if e.data == "true" else hide_submenu(e),
    )

    # Crear el submenú con su propio evento on_hover
    submenu = ft.Container(
        content=ft.Column(
            [
                ft.TextButton("Subopción 1", on_click=lambda e: print("Subopción 1 seleccionada")),
                ft.TextButton("Subopción 2", on_click=lambda e: print("Subopción 2 seleccionada")),
                ft.TextButton("Subopción 3", on_click=lambda e: print("Subopción 3 seleccionada")),
            ]
        ),
        padding=10,
        bgcolor=ft.colors.LIGHT_BLUE_50,
        visible=False,  # Submenú oculto inicialmente
        on_hover=lambda e: show_submenu(e) if e.data == "true" else hide_submenu(e),
    )

    # Agregar el botón principal y el submenú al contenedor de la página
    page.add(
        ft.Column(
            [
                main_button,
                submenu
            ]
        )
    )

ft.app(target=main)
