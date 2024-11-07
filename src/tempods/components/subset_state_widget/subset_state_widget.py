from glue.core import ComponentID, Data, Subset
from glue.core.subset import AndState, CategorySubsetState
import ipyvuetify as v
from numpy import unique
from traitlets import List, observe

from cosmicds.utils import load_template


class SubsetStateWidget(v.VuetifyTemplate):
    template = load_template("subset_state_widget.vue", __file__, traitlet=True).tag(sync=True)
    size_options = List().tag(sync=True)
    size_selections = List().tag(sync=True)
    type_options = List().tag(sync=True)
    type_selections = List().tag(sync=True)

    def __init__(self, subset: Subset):
        super().__init__()
        self.subset = subset
        self.type_att: ComponentID = subset.data.id["PrimSource"]
        self.size_att: ComponentID = subset.data.id["Size_binned"]
        
        self.type_options = list(unique(self.subset.data[self.type_att]))
        self.size_options = list(unique(self.subset.data[self.size_att]))
        self.type_selections = self.subset.data[self.type_att].codes
        self.size_selections = self.subset.data[self.size_att].codes
        self.type_state = CategorySubsetState(self.type_att, self.type_selections)
        self.size_state = CategorySubsetState(self.size_att, self.size_selections)

    def _update_type_state(self, type_indices: List[int]):
        self.type_state = CategorySubsetState(self.type_att, type_indices)
        self._update_state()

    def _update_size_state(self, size_indices: List[str]):
        self.size_state = CategorySubsetState(self.size_att, size_indices)
        self._update_state()

    def _update_state(self):
        self.subset.subset_state = AndState(self.type_state, self.size_state)

    @observe('type_selections')
    def _on_type_selections_changed(self, change: dict):
        self._update_type_state(change["new"])
