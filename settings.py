import os
import kivy
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from shortcuts import run_syscall
from kivy.storage.jsonstore import JsonStore

PATH_SEPERATOR = '\\' if os.path.realpath(__file__).find('\\') != -1 else '/'

PROJECT_PATH = PATH_SEPERATOR.join(os.path.realpath(__file__).
                                   split(PATH_SEPERATOR)[:-1])

KIVY_FONTS = [
    {
        "name": "FiraSans",
        "fn_regular": "%(pp)s%(ps)sassets%(ps)sfonts%(ps)sFiraSans-Regular.ttf" % {'pp': PROJECT_PATH,
                                                                                   'ps': PATH_SEPERATOR},
    },
    {
        "name": "WebAwesome",
        "fn_regular": "%(pp)s%(ps)sassets%(ps)sfonts%(ps)sfontawesome-webfont.ttf" % {'pp': PROJECT_PATH,
                                                                                      'ps': PATH_SEPERATOR},
    },
    {
        "name": "FiraSansBold",
        "fn_regular": "%(pp)s%(ps)sassets%(ps)sfonts/FiraSans-Bold.ttf" % {'pp': PROJECT_PATH,
                                                                           'ps': PATH_SEPERATOR},
    }
]

for font in KIVY_FONTS:
    LabelBase.register(**font)

KIVY_DEFAULT_FONT = "FiraSans"
KIVY_ICONIC_FONT = "WebAwesome"
KIVY_DEFAULT_BOLD_FONT = "FiraSansBold"

KIVY_DEFAULT_BOLD_FONT_PATH = filter(
    lambda x: x['name'] == KIVY_DEFAULT_BOLD_FONT, KIVY_FONTS)[0]['fn_regular']
KIVY_DEFAULT_FONT_PATH = filter(
    lambda x: x['name'] == KIVY_DEFAULT_FONT, KIVY_FONTS)[0]['fn_regular']
KIVY_ICONIC_FONT_PATH = filter(
    lambda x: x['name'] == KIVY_ICONIC_FONT, KIVY_FONTS)[0]['fn_regular']

if PATH_SEPERATOR == '/':
    cmd = "echo $HOME"
else:
    cmd = "echo %USERPROFILE%"

out = run_syscall(cmd)
REPOFILE = "%(out)s%(ps)s.kivyrepowatcher%(ps)srepowatcher" % {'out': out.rstrip(),
                                                               'ps': PATH_SEPERATOR}
KIVY_VERSION = kivy.__version__

DB = JsonStore(REPOFILE)
directory = os.path.dirname(REPOFILE)
if not os.path.exists(directory):
    os.makedirs(directory)
    DB.store_put('repos', [])
    DB.store_put('theme', 'CUSTOM')
    DB.store_put('screen', 'Changes')
if not DB.store_exists('repos') and not DB.store_exists('theme'):
    repos = DB.store_load()
    DB._data = {}
    DB.store_put('repos', repos if repos else [])
    DB.store_sync()
if not DB.store_exists('repos'):
    DB.store_put('repos', [])
if not DB.store_exists('theme'):
    DB.store_put('theme', 'CUSTOM')
if not DB.store_exists('screen'):
    DB.store_put('screen', 'Changes')
if not DB.store_exists('current_repo'):
    DB.store_put('current_repo', "")
DB.store_sync()

COLOR_SCHEMAS = [
    dict(name='MAC',
         COLORS=dict(HEX_COLOR1="F2F2F2",
                     HEX_COLOR2="A8B2BF",
                     HEX_COLOR3="64718C",
                     HEX_COLOR4="D8E3F2",
                     HEX_COLOR5="3B4259")),
    dict(name='MAC LEOPARD',
         COLORS=dict(HEX_COLOR1="E3E3E3",
                     HEX_COLOR2="787878",
                     HEX_COLOR3="575757",
                     HEX_COLOR4="A3A3A3",
                     HEX_COLOR5="3D3D3D")),
    dict(name='CUSTOM',
         COLORS=dict(HEX_COLOR1="DDDCC5",
                     HEX_COLOR2="353F45",
                     HEX_COLOR3="711819",
                     HEX_COLOR4="DBCA99",
                     HEX_COLOR5="6A6A61")),
    dict(name="ASPRIN C",
         COLORS=dict(HEX_COLOR1="F3FFE2",
                     HEX_COLOR2="1695A3",
                     HEX_COLOR3="225378",
                     HEX_COLOR4="ACF0F2",
                     HEX_COLOR5="EB7F00")),
    dict(name="FIRENZE",
         COLORS=dict(HEX_COLOR1="FFF0A5",
                     HEX_COLOR2="8E2800",
                     HEX_COLOR3="FFA33B",
                     HEX_COLOR4="468966",
                     HEX_COLOR5="B64926")),
    dict(name="DIRT",
         COLORS=dict(HEX_COLOR1="B29C85",
                     HEX_COLOR2="3B424C",
                     HEX_COLOR3="1D181F",
                     HEX_COLOR4="306E73",
                     HEX_COLOR5="782719")),
    dict(name="SPA",
         COLORS=dict(HEX_COLOR1="ECEBF0",
                     HEX_COLOR2="687D77",
                     HEX_COLOR3="484A47",
                     HEX_COLOR4="C1CE96",
                     HEX_COLOR5="353129")),
    dict(name="JAPANESE GARDEN",
         COLORS=dict(HEX_COLOR1="EFE4BD",
                     HEX_COLOR2="A39770",
                     HEX_COLOR3="A32500",
                     HEX_COLOR4="BAB293",
                     HEX_COLOR5="2B2922")),
    dict(name="WINTER ROAD",
         COLORS=dict(HEX_COLOR1="F1F2D8",
                     HEX_COLOR2="778C7A",
                     HEX_COLOR3="425955",
                     HEX_COLOR4="BFBD9F",
                     HEX_COLOR5="282B38")),
    dict(name="HAITIRELIEF",
         COLORS=dict(HEX_COLOR1="DC8505",
                     HEX_COLOR2="32450C",
                     HEX_COLOR3="717400",
                     HEX_COLOR4="EC5519",
                     HEX_COLOR5="8F1E04")),
]

COLOR_THEMES = map(lambda x: x['name'], COLOR_SCHEMAS)

try:
    COLORS = filter(lambda x: x['name'] == DB.get('theme'), COLOR_SCHEMAS)[
        0]['COLORS']
except:
    COLORS = filter(lambda x: x['name'] == 'CUSTOM', COLOR_SCHEMAS)[
        0]['COLORS']

HEX_COLOR1 = COLORS['HEX_COLOR1']
HEX_COLOR2 = COLORS['HEX_COLOR2']
HEX_COLOR3 = COLORS['HEX_COLOR3']
HEX_COLOR4 = COLORS['HEX_COLOR4']
HEX_COLOR5 = COLORS['HEX_COLOR5']


COLOR1 = get_color_from_hex(HEX_COLOR1)
COLOR2 = get_color_from_hex(HEX_COLOR2)
COLOR3 = get_color_from_hex(HEX_COLOR3)
COLOR4 = get_color_from_hex(HEX_COLOR4)
COLOR5 = get_color_from_hex(HEX_COLOR5)
