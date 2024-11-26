import flet as ft


def sett(page:ft.Page, correo):
    page.title = "Configuración"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = ft.Margin(10, 10, 10, 10)
    is_mobile = page.width < 600
    page.window.maximized = not is_mobile

    Grid= ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    avatar=ft.Container(ft.CircleAvatar(
                foreground_image_src="http://res.cloudinary.com/djlskhtyf/image/upload/v1732593675/Avatar.jpg",
                max_radius=100,
                
            ),on_click=lambda: print("HOla"))
    contenido = ft.Row([
        ft.Column([
            avatar,
            ft.FilledButton(icon=ft.icons.CREATE, text="Crear",data="Create",),
            ft.FilledButton(icon=ft.icons.ADD_LINK, text="Unirse",data="Join",)
        
        ], width=150),
        ft.Container(
            content=Grid,
            width=500 if is_mobile else 1000,
            bgcolor="green200"
        )
    ])
    
    return contenido