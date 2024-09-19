import solara
from solara.alias import rv
from pathlib import Path
from cosmicds.components import ScaffoldAlert
from .component_state import COMPONENT_STATE
from .component_state import Marker
from ...base_component_state import transition_next

GUIDELINE_ROOT = Path(__file__).parent / "guidelines"


@solara.component
def Page():
    with rv.Row():
        with rv.Col(cols=4):
            ScaffoldAlert(
                GUIDELINE_ROOT / "GuidelineIntro.vue",
                event_next_callback=lambda _: transition_next(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.mee_gui1),
                speech=None,
            )

        with rv.Col(cols=8):
            with rv.Card():
                rv.Img(
                    src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
                    class_="mx-auto d-block",
                )

                with rv.CardTitle():
                    solara.Text("Guidelines")

                with rv.CardText():
                    solara.Text(
                        "In this section, you will be presented with a series "
                        "of guidelines that you will need to follow in order "
                        "to complete the task. Click 'Next' to continue.",
                    )
