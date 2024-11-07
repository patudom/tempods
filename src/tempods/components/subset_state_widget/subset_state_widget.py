from glue.core import ComponentID, Data, Subset
from glue.core.subset import AndState, CategorySubsetState, RangeSubsetState
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
        
        self.type_state = CategorySubsetState(self.type_att, [])
        self.size_state = RangeSubsetState(0, 0, self.size_att)
        self.type_options = list(unique(self.subset.data[self.type_att]))
        self.size_options = [0, 1, 2]
        self.type_selections = sorted(list(unique(self.subset.data[self.type_att].codes)))
        self.size_selections = self.size_options

    def _update_type_state(self, type_indices: list[int]):
        self.type_state = CategorySubsetState(self.size_att, type_indices)
        self._update_state()

    def _update_size_state(self, size_indices: list[int]):
        low = (min(size_indices) + 1) ** 2
        high = (max(size_indices) + 1) ** 2
        self.size_state = RangeSubsetState(low, high, self.size_att)
        self._update_state()

    def _update_state(self):
        self.subset.subset_state = AndState(self.type_state, self.size_state)

    @observe('type_selections')
    def _on_type_selections_changed(self, change: dict):
        self._update_type_state([int(c) for c in change["new"]])
        
    @observe('size_selections')
    def _on_size_selections_changed(self, change: dict):
        print(sorted(change["new"]))
        self._update_size_state(sorted(change["new"]))
