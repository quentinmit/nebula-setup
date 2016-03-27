from nx.core.constants import *

ENUM_MTYPES = [
    [0 , "File"],
    [1 , "Virtual"]
]

ENUM_CTYPES = [
    [TEXT,  "Text"],
    [VIDEO, "Video"],
    [AUDIO, "Audio"],
    [IMAGE, "Image"]
]

ENUM_STATES = [
    [0, "New"],
    [3, "Rejected"],
    [4, "Approved"]
]

BASE_META_SET = [

# NS   KEY                       E  F  CLASS        SET

("o",  "ctime",                  0, 0, DATETIME,    None),              # Creation time
("o",  "mtime",                  0, 0, DATETIME,    None),              # Last modified time

("a",  "media_type",             0, 0, SELECT,      ENUM_MTYPES),        # FILE / VIRTUAL
("a",  "content_type",           0, 0, SELECT,      ENUM_CTYPES),        # VIDEO / AUDIO /  IMAGE / TEXT
("a",  "id_folder",              1, 0, INTEGER,     None),
("a",  "id_origin",              0, 0, INTEGER,     None),              # "Import", "Acquisition", "Library", "Ingest", "Edit", "Playout 1" ....
("a",  "status",                 0, 0, INTEGER,     None),              # OFFLINE, ONLINE, CREATING, TRASHED, ARCHIVED
("a",  "version_of",             0, 0, INTEGER,     None),

("e",  "start",                  1, 0, DATETIME,    None),
("e",  "stop",                   1, 0, DATETIME,    None),
("e",  "id_channel",             1, 0, INTEGER,     None),
("e",  "id_magic",               0, 0, INTEGER,     None),

("b",  "bin_type",               0, 0, INTEGER,     None),

("i",  "id_asset",               0, 0, INTEGER,     None),
("i",  "id_bin",                 0, 0, INTEGER,     None),
("i",  "position",               0, 0, INTEGER,     None),              # Order of the item within the bin

("u",  "login",                  0, 0, TEXT,        None),
("u",  "password",               0, 0, TEXT,        None),

#
# Virtual tags
#

("v", "rundown_symbol",          0, 0, -1,          None),              # Primary symbol in rundown view (folder color for items, star for event promo)
("v", "rundown_status",          0, 0, -1,          None),              # OFFLINE, READY etc
("v", "rundown_broadcast",       0, 0, -1,          None),              # Scheduled start time of block/item
("v", "rundown_scheduled",       0, 0, -1,          None),              # Real computed start time of the item
("v", "rundown_difference",      0, 0, -1,          None),              # Real computed start time of the item
("E", "run_mode",                0, 0, INTEGER,     None),              # AUTO / MANUAL / SOFT AUTO / HARD AUTO

#
# Base metadata
#

("A",  "id_storage",             0, 0, INTEGER,     None),
("A",  "path",                   1, 1, TEXT,        None),
("A",  "subclips",               0, 0, REGIONS,     None),
("A",  "meta_probed",            0, 0, BOOLEAN,     None),              # If true, meta_probes would not overwrite non-technical metadata during update
("A",  "article",                1, 1, BLOB,        {"syntax" : "md"}),

("AI", "mark_in",                1, 0, TIMECODE,    None),
("AI", "mark_out",               1, 0, TIMECODE,    None),

#
# Asset description
#

("m",  "title",                  1, 1, TEXT,        None),              # dc.title.main - The title most commonly associated with the resource.
("m",  "title/original",         1, 1, TEXT,        None),              # ebucore.title.original
("m",  "title/alternate",        1, 1, TEXT,        None),              # dc.title.alternate - Where a resource is known by more than one name
("m",  "subtitle" ,              1, 1, TEXT,        None),              # dc.title.subtitle - Ancillary title information for the resource.
("m",  "subtitle/original",      1, 1, TEXT,        None),
("m",  "subtitle/alternate",     1, 1, TEXT,        None),
("m",  "description",            1, 1, BLOB,        {"syntax" : "md"}),
("m",  "description/original",   1, 1, BLOB,        {"syntax" : "md"}),

("m",  "series",                 1, 1, CS_SELECT,   "series"),          # dc.title.series - Where the resource is part of a series, name of the serie.
("m",  "series/season",          1, 0, INTEGER,     None),
("m",  "series/episode",         1, 0, INTEGER,     None),

("m",  "language",               1, 0, CS_SELECT,   "languages"),
("m",  "date",                   1, 0, DATETIME,    {"mode" : "date"}),
("m",  "date/valid",             1, 0, DATETIME,    {"mode" : "date"}),
("m",  "rights",                 1, 1, BLOB,        None),

("m",  "format",                 1, 1, CS_SELECT,   "formats"),         # documentary / featrure / clip / sport event / ....
("m",  "genre",                  1, 1, CS_SELECT,   "genres"),          # horror / football / punk rock
("m",  "keywords",               1, 1, TEXT,        None),              # Keywords

("m",  "source",                 0, 1, TEXT,        None),              # Youtube, Vimeo, PirateBay....
("m",  "source/url",             0, 1, TEXT,        None),              # youtube url, torrent magnet link....

("m",  "identifier/main",        1, 1, TEXT,        None),              # Primary Content ID (IDEC, GUID...)
("m",  "identifier/youtube",     0, 1, TEXT,        None),              # Youtube ID if exists
("m",  "identifier/vimeo",       0, 1, TEXT,        None),              # Vimeo ID if exists
("m",  "identifier/imdb",        1, 1, TEXT,        None),              # IMDB ID for movies

("m",  "album",                  1, 1, TEXT,        None),
("m",  "album/track",            1, 0, INTEGER,     None),
("m",  "album/disc",             1, 0, INTEGER,     None),

("m",  "role/director",          1, 1, TEXT,        None),              # ebu_RoleCode 20.16
("m",  "role/composer",          1, 1, TEXT,        None),              # ebu_RoleCode 17.1.7 (music)
("m",  "role/performer",         1, 1, TEXT,        None),              # ebu_RoleCode 17.2   (music) (A.K.A Artist)

#
# Special
#

("m",  "notes",                  1, 1, BLOB,        None),
("m",  "promoted",               1, 0, BOOLEAN,     None),              # Asset "promotion". It"s hit, important, favourite,....
("m",  "content_alert",          1, 0, LIST,        None),
("m",  "commercials/client",     1, 1, CS_SELECT,   "clients"),
("m",  "commercials/campaign",   1, 1, INTEGER,     None),


#
# Technical (automated extraction)
#

("f", "duration",                0, 0, TIMECODE,    None),              # Clip duration. From ffprobe/format/duration. if fails, taken from streams[0]/duration
("f", "file/mtime",              0, 0, DATETIME,    None),              # Timestamp of file last modification
("f", "file/size",               0, 0, INTEGER,     None),              # File size in bytes
("f", "file/format",             0, 0, TEXT,        None),              # Container format name. from ffprobe/format/format_name
("f", "video/width",             0, 0, INTEGER,     None),              # Video frame / image width (pixels)
("f", "video/height",            0, 0, INTEGER,     None),              # Video frame / image height (pixels)
("f", "video/fps",               0, 0, FRACTION,    None),
("f", "video/pixel_format",      0, 0, TEXT,        None),
("f", "video/color_range",       0, 0, TEXT,        None),
("f", "video/color_space",       0, 0, TEXT,        None),
("f", "video/aspect_ratio",      0, 0, FRACTION,    None),
("f", "video/codec",             0, 0, TEXT,        None),
("f", "audio/codec",             0, 0, TEXT,        None),

("q", "qc/state",                1, 0, ENUM,        ENUM_STATES),       # 1 and 2 are reserved for Auto QC failed and passed states
("q", "qc/report",               1, 0, BLOB,        None),              # Holds error report from QC Pass and/or rejection/approval message from QC humanoid
("q", "audio/bpm",               0, 0, NUMERIC,     None),              # Music BPM
("q", "audio/r128/i",            0, 0, NUMERIC,     None),              # Integrated loudness (LUFS)
("q", "audio/r128/t",            0, 0, NUMERIC,     None),              # Integrated loudness threshold (LUFS)
("q", "audio/r128/lra",          0, 0, NUMERIC,     None),              # LRA (LU)
("q", "audio/r128/lra/t",        0, 0, NUMERIC,     None),              # Loudness range threshold (LUFS)
("q", "audio/r128/lra/l",        0, 0, NUMERIC,     None),              # LRA Low (LUFS)
("q", "audio/r128/lra/r",        0, 0, NUMERIC,     None),              # LRA High (LUFS)
("q", "audio/gain/mean",         0, 0, NUMERIC,     None),
("q", "audio/gain/peak",         0, 0, NUMERIC,     None),
("q", "audio/silence",           0, 0, REGIONS,     None),              # Areas with silent audio
("q", "audio/clipping",          0, 0, REGIONS,     None),              # Audio clipping areas
("q", "video/black",             0, 0, REGIONS,     None),              # Areas where video is black-only
("q", "video/static",            0, 0, REGIONS,     None),              # Areas with static image
("q", "video/is_interlaced",     0, 0, BOOLEAN,     None),

]
