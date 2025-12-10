# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_path, '..'))

from pyLibProject.defs import defs_project as defs_project
from pyLibProject.defs import defs_layers_groups as defs_layers_groups

LAYERS_POS_ORDER = 1
LAYERS_FIELD_MIN_ZOOM = 1
LAYERS_FIELD_MAX_ZOOM = 25

LOCATIONS_LAYER_NAME = defs_project.LOCATIONS_LAYER_NAME
LAYER_FIELD_POS_ORDER = 'pos_order'
LAYER_FIELD_TITLE = 'title'
LAYER_FIELD_TABLE_NAME = 'table_name'
LAYER_SLD_CONTENT = 'sld_content'
LAYER_FIELD_VISIBILITY = 'visibility'
LAYER_FIELD_MIN_ZOOM = 'min_zoom'
LAYER_FIELD_MAX_ZOOM = 'max_zoom'
LAYERS_GROUP_ID = 'group_id'

fields_by_layer = {}
fields_by_layer[LOCATIONS_LAYER_NAME] = {}
fields_by_layer[LOCATIONS_LAYER_NAME][LAYER_FIELD_POS_ORDER] = LAYERS_POS_ORDER
LAYERS_POS_ORDER = LAYERS_POS_ORDER + 1
fields_by_layer[LOCATIONS_LAYER_NAME][LAYER_FIELD_TITLE] = defs_project.LOCATIONS_LAYER_NAME
fields_by_layer[LOCATIONS_LAYER_NAME][LAYER_FIELD_TABLE_NAME] = defs_project.LOCATIONS_LAYER_NAME
fields_by_layer[LOCATIONS_LAYER_NAME][LAYER_SLD_CONTENT] = None # or assign by code
fields_by_layer[LOCATIONS_LAYER_NAME][LAYER_FIELD_VISIBILITY] = True
fields_by_layer[LOCATIONS_LAYER_NAME][LAYER_FIELD_MIN_ZOOM] = LAYERS_FIELD_MIN_ZOOM
fields_by_layer[LOCATIONS_LAYER_NAME][LAYER_FIELD_MAX_ZOOM] = LAYERS_FIELD_MAX_ZOOM
fields_by_layer[LOCATIONS_LAYER_NAME][LAYERS_GROUP_ID] = None # or assign by code

layers_group_name_by_layer= {}
layers_group_name_by_layer[LOCATIONS_LAYER_NAME] = defs_layers_groups.MANAGEMENT_LAYERS_GROUP_NAME
# {
#   "pos_order": 1,
#   "title": "Locations",
#   "table_name": "locations",
#   "sld_content": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><StyledLayerDescriptor xmlns=\"http://www.opengis.net/sld\" xsi:schemaLocation=\"http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd\" xmlns:se=\"http://www.opengis.net/se\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" version=\"1.1.0\" xmlns:ogc=\"http://www.opengis.net/ogc\"><NamedLayer><se:Name>prueba_poligonos</se:Name><UserStyle><se:Name>prueba_poligonos</se:Name><se:FeatureTypeStyle><se:Rule><se:Name>Single symbol</se:Name><se:LineSymbolizer><se:Stroke><se:SvgParameter name=\"stroke\">#987db7</se:SvgParameter><se:SvgParameter name=\"stroke-width\">4</se:SvgParameter><se:SvgParameter name=\"stroke-linejoin\">bevel</se:SvgParameter><se:SvgParameter name=\"stroke-linecap\">square</se:SvgParameter></se:Stroke></se:LineSymbolizer></se:Rule></se:FeatureTypeStyle></UserStyle></NamedLayer></StyledLayerDescriptor>",
#   "visibility": true,
#   "min_zoom": 10,
#   "max_zoom": 25,
#   "group_id": null
# }