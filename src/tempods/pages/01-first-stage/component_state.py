from pydantic import BaseModel, field_validator, Field
from cosmicds.state import BaseState

from ...base_marker import BaseMarker
import enum
from functools import cached_property
from ...base_component_state import BaseComponentState
import solara
from typing import Any

from ...state import LOCAL_STATE


class Marker(enum.Enum, BaseMarker):
    mee_gui1 = enum.auto()


class ComponentState(BaseComponentState, BaseState):
    current_step: Marker = Marker.mee_gui1
    stage_id: str = "first_stage"


COMPONENT_STATE = solara.reactive(ComponentState())
