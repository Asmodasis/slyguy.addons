from slyguy.language import BaseLanguage


class Language(BaseLanguage):
    OUTPUT_DIR             = 30001
    MERGE_EVERY_X          = 30002
    X_HOURS                = 30003
    RESTART_PVR            = 30004
    PAGE_SIZE              = 30005
    SETUP_IPTV_SIMPLE      = 30006
    SETUP_IPTV_COMPLETE    = 30007
    SETTING_UP_IPTV        = 30008
    PLAYLISTS              = 30009
    ADD_PLAYLIST           = 30010
    DELETE_PLAYLIST        = 30011
    SOURCE_EXISTS          = 30012
    URL                    = 30013
    FILE                   = 30014
    ADDON                  = 30015
    SELECT_SOURCE_TYPE     = 30016
    ENTER_SOURCE_URL       = 30017
    SELECT_SOURCE_FILE     = 30018
    NO_SOURCE_ADDONS       = 30019
    SELECT_SOURCE_ADDON    = 30020
    ADD_EPG                = 30021
    EDIT_PLAYLIST          = 30022
    SOURCE_LABEL           = 30023
    ARCHIVE_TYPE_LABEL     = 30024
    ARCHIVE_NONE           = 30025
    GZIP                   = 30026
    ENABLED_LABEL          = 30027
    SKIP_PLIST_CHNO_LABEL  = 30028
    START_CHNO_LABEL       = 30029
    DEFAULT_VISIBILE_LABEL = 30030
    GROUP_NAME_LABEL       = 30031
    SKIP_PLIST_GROUP_NAMES = 30032
    GROUP_LABEL            = 30033
    ENTER_GROUP_NAME       = 30034
    ENTER_START_CHNO       = 30035
    SELECT_ARCHIVE_TYPE    = 30036
    MANAGE_TV              = 30037
    ALL_CHANNELS           = 30038
    DELETE_EPG             = 30039
    EDIT_EPG               = 30040
    EPG_LABEL              = 30041
    DISABLED               = 30042
    MERGE_COMPLETE         = 30043
    RUN_MERGE              = 30044
    MERGE_STARTED          = 30045
    MERGE_IN_PROGRESS      = 30046
    ENTER_CHANNEL_URL      = 30047
    NEXT_PAGE              = 30048
    CHANNEL_LABEL          = 30049
    CHANNEL_HIDDEN         = 30050
    NO_NAME                = 30051
    SHOW_CHANNEL           = 30052
    HIDE_CHANNEL           = 30053
    PLAY_CHANNEL           = 30054
    DELETE_CHANNEL         = 30055
    RESET_CHANNEL          = 30056
    EDIT_CHANNEL           = 30057
    CHANNEL_MODIFIED       = 30058
    PLAYLIST               = 30059
    ADD_CHANNEL            = 30060
    EPGS                   = 30061
    ADDON_METHOD_TIMEOUT   = 30062
    ADDON_METHOD_FAILED    = 30063
    LOCAL_PATH_MISSING     = 30064
    SLUG                   = 30065
    IPTV_MERGE_PROXY       = 30066
    ADDON_SETTINGS         = 30067
    PENDING_MERGE          = 30068
    DISABLED_MERGE         = 30069
    START_CH_NO            = 30070
    MANAGE_RADIO           = 30071
    RADIO_GROUP            = 30072
    BOOT_MERGE             = 30073
    XZ                     = 30074
    ARCHIVE_AUTO           = 30075
    INSERT_PLAYLIST        = 30076
    ASK_TO_ADD             = 30077
    GROUP_ORDER            = 30078
    HTTP_SETTING           = 30079
    HTTP_FORCE_SETTING     = 30080
    REMOVE_EPG_ORPHANS     = 30081
    CONFIGURE_ADDON        = 30082
    USE_STARTING_CHNO      = 30083
    CONF_DELETE_PLAYLIST   = 30084
    CONF_DELETE_EPG        = 30085
    DISABLE_PLAYLIST       = 30086
    ENABLE_PLAYLIST        = 30087
    MOVE_UP                = 30088
    MOVE_DOWN              = 30089
    CONF_DELETE_CHANNEL    = 30090
    DISABLE_EPG            = 30091
    ENABLE_EPG             = 30092
    MERGE_PLAYLISTS        = 30093
    MERGE_EPGS             = 30094
    DISABLE_GROUPS         = 30095
    SERVICE_DELAY          = 30096
    HIDE_GROUPS            = 30097
    MERGE_AT_HOUR          = 30098
    MERGE_HOUR             = 30099
    IGNORE_PLAYLIST_EPGS   = 30100


_ = Language()
