import solara
from solara.alias import rv
from ..layout import Layout


@solara.component
def Page():
    with rv.Row():
        with rv.Col(cols=12):
            solara.Div("Tempo Data Story", classes=["display-1", "mb-8"])

            solara.Div(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit sed "
                "do eiusmod tempor incididunt ut labore et dolore magna "
                "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                "Duis aute irure dolor in reprehenderit in voluptate velit "
                "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
                "occaecat cupidatat non proident, sunt in culpa qui officia "
                "deserunt mollit anim id est laborum."
            )
