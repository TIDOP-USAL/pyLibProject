# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_path, '..'))
# sys.path.append(os.path.join(current_path, '../..'))

from pyLibProject.defs import defs_project as defs_project

LAYERS_GROUPS_POS_ORDER = 1
LAYERS_GROUP_FIELD_MIN_ZOOM_DEFAULT_VALUE = 1
LAYERS_GROUP_FIELD_MAX_ZOOM_DEFAULT_VALUE = 25

MANAGEMENT_LAYERS_GROUP_NAME = defs_project.MANAGEMENT_LAYER_NAME
LAYERS_GROUP_FIELD_NAME = 'name'
LAYERS_GROUP_FIELD_DESCRIPTION = 'description'
LAYERS_GROUP_FIELD_VISIBILITY = 'visibility'
LAYERS_GROUP_FIELD_POS_ORDER = 'pos_order'
LAYERS_GROUP_FIELD_MIN_ZOOM = 'min_zoom'
LAYERS_GROUP_FIELD_MAX_ZOOM = 'max_zoom'
LAYERS_GROUP_FIELD_OPEN_IN_LAYERS_WITCHER = 'openinlayerswitcher'
fields_by_layers_group = {}
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME] = {}
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME][LAYERS_GROUP_FIELD_NAME] = MANAGEMENT_LAYERS_GROUP_NAME
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME][LAYERS_GROUP_FIELD_DESCRIPTION] = 'Layer group used in project management'
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME][LAYERS_GROUP_FIELD_VISIBILITY] = True
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME][LAYERS_GROUP_FIELD_POS_ORDER] = LAYERS_GROUPS_POS_ORDER
LAYERS_GROUPS_POS_ORDER = LAYERS_GROUPS_POS_ORDER + 1
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME][LAYERS_GROUP_FIELD_MIN_ZOOM] = LAYERS_GROUP_FIELD_MIN_ZOOM_DEFAULT_VALUE
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME][LAYERS_GROUP_FIELD_MAX_ZOOM] = LAYERS_GROUP_FIELD_MAX_ZOOM_DEFAULT_VALUE
fields_by_layers_group[MANAGEMENT_LAYERS_GROUP_NAME][LAYERS_GROUP_FIELD_OPEN_IN_LAYERS_WITCHER] = True

# {
#   "name": "Nuevo Grupo",
#   "description": null,
#   "visibility": true,
#   "pos_order": 1,
#   "min_zoom": 1,
#   "max_zoom": 25,
#   "openinlayerswitcher": true
# }
