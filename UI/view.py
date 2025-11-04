import flet as ft
from UI.alert import AlertManager

class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.alert = AlertManager(page)
        self.controller = None
        self.txt_titolo = None
        self.txt_responsabile = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")
        self.lista_auto = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)
        self.input_modello_auto = ft.TextField(label="Modello")
        self.lista_auto_ricerca = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.ElevatedButton("Conferma", on_click=self.controller.conferma_responsabile)
        pulsante_mostra_auto = ft.ElevatedButton("Mostra", on_click=self.controller.mostra_automobili)
        pulsante_cerca_auto = ft.ElevatedButton("Cerca", on_click=self.controller.cerca_automobili)

        self.page.add(
            self.toggle_cambia_tema,
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            ft.Text("Automobili", size=20),
            ft.Row(controls=[pulsante_mostra_auto]),
            self.lista_auto,
            ft.Divider(),
            ft.Text("Cerca Automobile", size=20),
            ft.Row(controls=[self.input_modello_auto, pulsante_cerca_auto]),
            self.lista_auto_ricerca,
            ft.Divider(),
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
