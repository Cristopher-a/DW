import flet as ft

def tm(page, correo):
    creareq=ft.AlertDialog(
        modal=True,
                title=ft.Text("Crear Equipo"),
                content=ft.Column([
                    ft.Row([
                        ft.TextField(label="Nombre", width=300),

                    ]),
                    ft.Row([
                        ft.TextField(label="Ciudad", width=300),
                    ]),
                    ft.Row([
                        ft.TextField(label="Contraseña", width=300),
                    ])
                ]),
                actions=[
        ft.CupertinoDialogAction(
            "Crear",
            is_destructive_action=True,
        ),
        ft.CupertinoDialogAction(
            text="Salir",
            is_default_action=False,
        ),
    ]
            )
    def crear(e):
        page.open(
            creareq            
        )
    def handle_on_hover(e):
        print(f"{e.control.content.value}.on_hover")
    rail=ft.Column([
        ft.Row([
            ft.ElevatedButton(icon=ft.icons.CREATE_SHARP,text="Crear",on_click=crear)
        ]),
        ft.Row([
            ft.ElevatedButton(icon=ft.icons.ADD_LINK,text="Unirse")
        ]),
        ft.Divider(height=9, thickness=3),
        ft.Row([
            ft.SubmenuButton(
                content=ft.Text("Team1"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("dashboard"),
                        leading=ft.Icon(ft.icons.COLORIZE),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click=lambda: print("Blue")
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Info"),
                        leading=ft.Icon(ft.icons.COLORIZE),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN}),
                        on_click=lambda: print("Green")
                    ),
                    
                ]
            )
        ]),
        
    ])

    return(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
