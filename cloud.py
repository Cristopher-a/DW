import flet as ft
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

cloudinary.config(
    cloud_name="djlskhtyf",
    api_key="222451394828739",
    api_secret="tqa7hpx_06pBYMKhQxT7my4Jk40",
    secure=True
)

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        
        # Subir el archivo a Cloudinary
        if e.files:  # Asegurarse de que haya archivos seleccionados
            for file in e.files:
                upload = cloudinary.uploader.upload(file.path, public_id="Avatar")
                print("Archivo subido exitosamente:", upload.get('url'))

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )

ft.app(main)
