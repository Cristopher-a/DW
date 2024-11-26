import flet as ft
from dashboard import dsh
from team import  tm
from estadisticas import stadistics
from settings import sett
def nav(page: ft.Page, correo): 
    page.padding = ft.Margin(10, 10, 10, 10)
    is_mobile = page.width < 600
    page.window.maximized = not is_mobile

    def change(e):
        index = e.control.selected_index
        page.controls.clear()

        if (index == 0):
            page.add(navigation_bar)
            page.add(dsh(page, correo))  
        elif index == 1:
            page.add(navigation_bar)
            page.add(tm(page,correo))
        elif index == 2:
            page.add(navigation_bar)
            page.add(stadistics(page,correo))
        elif index == 3:
            page.add(navigation_bar)
            page.add(sett(page,correo))

        page.update()

    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=change,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.SPACE_DASHBOARD_OUTLINED,
                selected_icon=ft.icons.SPACE_DASHBOARD_ROUNDED,
                label="Dashboard"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.GROUP_OUTLINED,
                selected_icon=ft.icons.GROUP,
                label="Equipos"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.DATA_THRESHOLDING_OUTLINED,
                selected_icon=ft.icons.DATA_THRESHOLDING,
                label="Estadisticas"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label="Configuración"
            ),
        ]
    )
    page.add(dsh(page, correo))  
    return navigation_bar
if __name__ == "__main__":
    ft.app(target=lambda page: nav(page, "correo@example.com")) 
