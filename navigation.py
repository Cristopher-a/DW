import flet as ft
from dashboard import dsh

def nav(page: ft.Page):
    
    def change(e):
        
        index = e.control.selected_index
        page.controls.clear()

        if index == 0:
            page.add(navigation_bar)
            dsh(page)  
        elif index == 1:
            page.add(navigation_bar)
            page.add(ft.Text("Sección Equipos"))
        elif index == 2:
            page.add(navigation_bar)
            page.add(ft.Text("Sección Uso"))
        elif index == 3:
            page.add(navigation_bar)
            page.add(ft.Text("Sección C02"))
        elif index == 4:
            page.add(navigation_bar)
            page.add(ft.Text("Sección Explore"))

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
                icon=ft.icons.ACCESS_TIME,
                selected_icon=ft.icons.ACCESS_TIME_FILLED,
                label="Uso"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.ENERGY_SAVINGS_LEAF_OUTLINED,
                selected_icon=ft.icons.ENERGY_SAVINGS_LEAF_SHARP,
                label="C02"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore"
            ),
        ]
    )

    page.add(navigation_bar)
    dsh(page) 

if __name__ == "__main__":
    ft.app(target=nav)