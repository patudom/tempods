from cosmicds.layout import BaseLayout
from .state import GLOBAL_STATE, LOCAL_STATE
import solara
from solara.toestand import Ref
from cosmicds.components import MathJaxSupport, PlotlySupport
from .remote import LOCAL_API
from cosmicds.logger import setup_logger

logger = setup_logger("LAYOUT")


@solara.component
def Layout(children=[]):

    MathJaxSupport()
    PlotlySupport()
    logger.info("Mounted external libraries.")

    student_id = Ref(GLOBAL_STATE.fields.student.id)
    loaded_states = solara.use_reactive(False)

    async def _load_global_local_states():
        logger.info(
            "Here is where we would load story stage and measurements for the user.",
        )

    solara.lab.use_task(_load_global_local_states, dependencies=[student_id.value])

    # solara.use_memo(_load_local_state, dependencies=[student_id.value])

    async def _write_local_global_states():
        if not loaded_states.value:
            return

        logger.info(
            "Here is where we would write the local and global states to the database."
        )

    solara.lab.use_task(
        _write_local_global_states, dependencies=[GLOBAL_STATE.value, LOCAL_STATE.value]
    )

    with BaseLayout(
        local_state=LOCAL_STATE,
        children=children,
        story_name=LOCAL_STATE.value.story_id,
        story_title=LOCAL_STATE.value.title,
    ):
        pass
