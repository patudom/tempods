<template>
  <v-card
    flat
    variant="outlined"
    class="subset_state_widget"
  >
    <v-card-title>Select Power Plants to Show</v-card-title>
    <v-list>
      <v-list-title>Plant type</v-list-title>
      <v-list-item-group
        multiple
        v-model="type_selections"
      >
        <v-list-item
          v-for="(option, index) in type_options"
          :key="index"
          :value="index"
        >
          <template v-slot:default="{ active }">
            <v-list-item-content
              class="font-weight-bold"
            >
              {{ toTitleCase(option) }}
            </v-list-item-content>
            <v-list-item-action>
              <v-checkbox
                :input-value="active"
                :color="type_colors[index]"
              />
            </v-list-item-action>
          </template>
        </v-list-item>
      </v-list-item-group>
    </v-list>
    <v-list>
      <v-list-title>Size</v-list-title>
      <v-list-item-group
        multiple
        v-model="size_selections"
      >
        <v-list-item
          v-for="(option, index) in size_options"
          :key="index"
          :value="index"
        >
          <template v-slot:default="{ active }">
            <v-list-item-content
              class="font-weight-bold"
            >
              {{ option }}
            </v-list-item-content>
            <v-list-item-action>
              <v-checkbox
                :input-value="active"
                color="gray"
              />
            </v-list-item-action>
          </template>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
export default {
  methods: {
    toTitleCase(str) {
      return str.replace(
        /\w\S*/g,
        text => text.charAt(0).toUpperCase() + text.substring(1).toLowerCase()
      );
    }
  }
}
</script>
