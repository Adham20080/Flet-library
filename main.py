import flet as ft

# def main(pg: ft.Page):
#     txt = ft.Text(value="My name is .....", color="green")
#     pg.controls.append(txt)
#     pg.update()
#
#
# ft.app(target=main)

import time


def main(pg: ft.Page):
    txt = ft.Text(color="blue")
    pg.add(txt)
    for i in range(100):
        txt.value = f"Step {i}"
        pg.update()
        time.sleep(1)


ft.app(target=main)
