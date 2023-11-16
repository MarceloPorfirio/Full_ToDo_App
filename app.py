import flet
from flet import *
from datetime import datetime
import sqlite3

def main(page:Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    __main__column_ = Column(
        scroll='hidden',
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text('To-Do Items', size=18,weight='bold',color='white'),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        icon_color='white',

                    )
                ]
            )
        ]
    )

    page.add(
        Container(
            width=1500,
            height=800,
            margin=-10,
            bgcolor='bluegrey900',
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=280,
                        height=500,
                        bgcolor="#0f0f0f",
                        border_radius=40,
                        border=border.all(0.5,'white'),
                        padding=padding.only(top=35, left=20,right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE,
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                __main__column_,
                            ]
                        )
                    )
                ],
            ),


        )
    )
    page.update()

if __name__ == '__main__':
    flet.app(target=main)