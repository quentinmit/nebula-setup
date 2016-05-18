from .core.constants import *

ENUM_MTYPES = {
        0 : "File",
        1 : "Virtual",
    }

ENUM_CTYPES = {
    TEXT :  "Text",
    VIDEO :  "Video",
    AUDIO :  "Audio",
    IMAGE :  "Image"
}

ENUM_STATES = {
        0 : "New",
        3 :  "Rejected",
        4 : "Approved"
    }

meta_types = {
    #                        NS    E  F  I  CLASS      SET
    "ctime"               : ("o",  0, 0, 1, DATETIME,  None),              # Creation time
    "mtime"               : ("o",  0, 0, 1, DATETIME,  None),              # Last modified time
    "media_type"          : ("a",  0, 0, 1, SELECT,    ENUM_MTYPES),       # FILE / VIRTUAL
    "content_type"        : ("a",  0, 0, 1, SELECT,    ENUM_CTYPES),       # VIDEO / AUDIO /  IMAGE / TEXT
    "id_folder"           : ("a",  1, 0, 1, INTEGER,   None),
    "origin"              : ("a",  0, 0, 1, TEXT,      None),              # "Import", "Acquisition", "Library", "Ingest", "Edit", "Playout 1" ....
    "status"              : ("a",  0, 0, 1, INTEGER,   None),              # OFFLINE, ONLINE, CREATING, TRASHED, ARCHIVED
    "version_of"          : ("a",  0, 0, 1, INTEGER,   None),
    "start"               : ("e",  1, 0, 1, DATETIME,  None),
    "stop"                : ("e",  1, 0, 1, DATETIME,  None),
    "id_channel"          : ("e",  1, 0, 1, INTEGER,   None),
    "id_magic"            : ("e",  0, 0, 1, INTEGER,   None),
    "bin_type"            : ("b",  0, 0, 1, INTEGER,   None),
    "id_asset"            : ("i",  0, 0, 1, INTEGER,   None),
    "id_bin"              : ("i",  0, 0, 1, INTEGER,   None),
    "position"            : ("i",  0, 0, 1, INTEGER,   None),              # Order of the item within the bin
    "login"               : ("u",  0, 0, 1, TEXT,      None),
    "password"            : ("u",  0, 0, 1, TEXT,      None),

    #
    # Virtual tags
    #

    "rundown_symbol"      : ("v",  0, 0, 0, -1,        None),              # Primary symbol in rundown view (folder color for items, star for event promo)
    "rundown_status"      : ("v",  0, 0, 0, -1,        None),              # OFFLINE, READY etc
    "rundown_broadcast"   : ("v",  0, 0, 0, -1,        None),              # Scheduled start time of block/item
    "rundown_scheduled"   : ("v",  0, 0, 0, -1,        None),              # Real computed start time of the item
    "rundown_difference"  : ("v",  0, 0, 0, -1,        None),              # Real computed start time of the item
    "run_mode"            : ("E",  0, 0, 0, INTEGER,   None),              # AUTO / MANUAL / SOFT AUTO / HARD AUTO

    #
    # Base metadata
    #

    "id_storage"          : ("A",  0, 0, 0, INTEGER,   None),
    "path"                : ("A",  1, 1, 0, TEXT,      None),
    "subclips"            : ("A",  0, 0, 0, REGIONS,   None),
    "meta_probed"         : ("A",  0, 0, 0, BOOLEAN,   None),              # If true, meta_probes would not overwrite non-technical metadata during update
    "article"             : ("A",  1, 1, 0, BLOB,      {"syntax" : "md"}),
    "mark_in"             : ("AI", 1, 0, 0, TIMECODE,  None),
    "mark_out"            : ("AI", 1, 0, 0, TIMECODE,  None),

    #
    # Asset description
    #

    "title"               : ("m",  1, 1, 0, TEXT,       None),              # dc.title.main - The title most commonly associated with the resource.
    "title/original"      : ("m",  1, 1, 0, TEXT,       None),              # ebucore.title.original
    "title/alternate"     : ("m",  1, 1, 0, TEXT,       None),              # dc.title.alternate - Where a resource is known by more than one name
    "subtitle"            : ("m",  1, 1, 0, TEXT,       None),              # dc.title.subtitle - Ancillary title information for the resource.
    "subtitle/original"   : ("m",  1, 1, 0, TEXT,       None),
    "subtitle/alternate"  : ("m",  1, 1, 0, TEXT,       None),
    "description"         : ("m",  1, 1, 0, BLOB,       {"syntax" : "md"}),
    "description/original": ("m",  1, 1, 0, BLOB,       {"syntax" : "md"}),
    "series"              : ("m",  1, 1, 1, CS_SELECT,  "series"),          # dc.title.series - Where the resource is part of a series, name of the serie.
    "series/season"       : ("m",  1, 0, 1, INTEGER,    None),
    "series/episode"      : ("m",  1, 0, 1, INTEGER,    None),
    "language"            : ("m",  1, 0, 1, CS_SELECT,  "languages"),
    "date"                : ("m",  1, 0, 1, DATETIME,   {"mode" : "date"}),
    "date/valid"          : ("m",  1, 0, 1, DATETIME,   {"mode" : "date"}),
    "rights"              : ("m",  1, 1, 1, BLOB,       None),
    "format"              : ("m",  1, 1, 1, CS_SELECT,  "formats"),         # documentary / featrure / clip / sport event / ....
    "genre"               : ("m",  1, 1, 1, CS_SELECT,  "genres"),          # horror / football / punk rock
    "keywords"            : ("m",  1, 1, 1, TEXT,       None),              # Keywords
    "source"              : ("m",  0, 1, 1, TEXT,       None),              # Youtube, Vimeo, PirateBay....
    "source/url"          : ("m",  0, 1, 1, TEXT,       None),              # youtube url, torrent magnet link....
    "identifier/main"     : ("m",  1, 1, 1, TEXT,       None),              # Primary Content ID (IDEC, GUID...)
    "identifier/youtube"  : ("m",  0, 1, 1, TEXT,       None),              # Youtube ID if exists
    "identifier/vimeo"    : ("m",  0, 1, 1, TEXT,       None),              # Vimeo ID if exists
    "identifier/imdb"     : ("m",  1, 1, 1, TEXT,       None),              # IMDB ID for movies
    "album"               : ("m",  1, 1, 1, TEXT,       None),
    "album/track"         : ("m",  1, 0, 1, INTEGER,    None),
    "album/disc"          : ("m",  1, 0, 1, INTEGER,    None),
    "role/director"       : ("m",  1, 1, 1, TEXT,       None),              # ebu_RoleCode 20.16
    "role/composer"       : ("m",  1, 1, 1, TEXT,       None),              # ebu_RoleCode 17.1.7 (music)
    "role/performer"      : ("m",  1, 1, 1, TEXT,       None),              # ebu_RoleCode 17.2   (music) (A.K.A Artist)
    "notes"               : ("m",  1, 1, 0, BLOB,       None),
    "promoted"            : ("m",  1, 0, 1, BOOLEAN,    None),              # Asset "promotion". It"s hit, important, favourite,....
    "content_alert"       : ("m",  1, 0, 0, LIST,       None),
    "commercials/client"  : ("m",  1, 1, 1, CS_SELECT,  "clients"),
    "commercials/campaign": ("m",  1, 1, 1, INTEGER,    None),
    "duration"            : ("f",  0, 0, 1, TIMECODE,   None),              # Clip duration. From ffprobe/format/duration. if fails, taken from streams[0]/duration

    "file/mtime"          : ("f",  0, 0, 1, DATETIME,   None),              # Timestamp of file last modification
    "file/size"           : ("f",  0, 0, 1, INTEGER,    None),              # File size in bytes
    "file/format"         : ("f",  0, 0, 0, TEXT,       None),              # Container format name. from ffprobe/format/format_name
    "video/width"         : ("f",  0, 0, 0, INTEGER,    None),              # Video frame / image width (pixels)
    "video/height"        : ("f",  0, 0, 0, INTEGER,    None),              # Video frame / image height (pixels)
    "video/fps"           : ("f",  0, 0, 0, FRACTION,   None),
    "video/pixel_format"  : ("f",  0, 0, 0, TEXT,       None),
    "video/color_range"   : ("f",  0, 0, 0, TEXT,       None),
    "video/color_space"   : ("f",  0, 0, 0, TEXT,       None),
    "video/aspect_ratio"  : ("f",  0, 0, 0, FRACTION,   None),
    "video/codec"         : ("f",  0, 0, 0, TEXT,       None),
    "audio/codec"         : ("f",  0, 0, 0, TEXT,       None),

    "qc/state"            : ("q",  1, 0, 1, ENUM,       ENUM_STATES),       # 1 and 2 are reserved for Auto QC failed and passed states
    "qc/report"           : ("q",  1, 0, 0, BLOB,       None),              # Holds error report from QC Pass and/or rejection/approval message from QC humanoid
    "audio/bpm"           : ("q",  0, 0, 1, NUMERIC,    None),              # Music BPM
    "audio/r128/i"        : ("q",  0, 0, 0, NUMERIC,    None),              # Integrated loudness (LUFS)
    "audio/r128/t"        : ("q",  0, 0, 0, NUMERIC,    None),              # Integrated loudness threshold (LUFS)
    "audio/r128/lra"      : ("q",  0, 0, 0, NUMERIC,    None),              # LRA (LU)
    "audio/r128/lra/t"    : ("q",  0, 0, 0, NUMERIC,    None),              # Loudness range threshold (LUFS)
    "audio/r128/lra/l"    : ("q",  0, 0, 0, NUMERIC,    None),              # LRA Low (LUFS)
    "audio/r128/lra/r"    : ("q",  0, 0, 0, NUMERIC,    None),              # LRA High (LUFS)
    "audio/gain/mean"     : ("q",  0, 0, 0, NUMERIC,    None),
    "audio/gain/peak"     : ("q",  0, 0, 0, NUMERIC,    None),
    "audio/silence"       : ("q",  0, 0, 0, REGIONS,    None),              # Areas with silent audio
    "audio/clipping"      : ("q",  0, 0, 0, REGIONS,    None),              # Audio clipping areas
    "video/black"         : ("q",  0, 0, 0, REGIONS,    None),              # Areas where video is black-only
    "video/static"        : ("q",  0, 0, 0, REGIONS,    None),              # Areas with static image
    "video/is_interlaced" : ("q",  0, 0, 0, BOOLEAN,    None),

}
