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

("o",  "ctime",                  0, 0, DATETIME,    False),              # Creation time
("o",  "mtime",                  0, 0, DATETIME,    False),              # Last modified time

("a",  "media_type",             0, 0, SELECT,      ENUM_MTYPES),        # FILE / VIRTUAL
("a",  "content_type",           0, 0, SELECT,      ENUM_CTYPES),        # VIDEO / AUDIO /  IMAGE / TEXT
("a",  "id_folder",              1, 0, INTEGER,     False),
("a",  "id_origin",              0, 0, INTEGER,     False),              # "Import", "Acquisition", "Library", "Ingest", "Edit", "Playout 1" ....
("a",  "status",                 0, 0, INTEGER,     False),              # OFFLINE, ONLINE, CREATING, TRASHED, ARCHIVED
("a",  "version_of",             0, 0, INTEGER,     False),

("e",  "start",                  1, 0, DATETIME,    False),
("e",  "stop",                   1, 0, DATETIME,    False),
("e",  "id_channel",             1, 0, INTEGER,     False),
("e",  "id_magic",               0, 0, INTEGER,     False),

("b",  "bin_type",               0, 0, INTEGER,     False),

("i",  "id_asset",               0, 0, INTEGER,     False),
("i",  "id_bin",                 0, 0, INTEGER,     False),
("i",  "position",               0, 0, INTEGER,     False),              # Order of the item within the bin

("u",  "login",                  0, 0, TEXT,        False),
("u",  "password",               0, 0, TEXT,        False),

#
# Virtual tags
#

("v", "rundown_symbol",          0, 0, -1,          False),              # Primary symbol in rundown view (folder color for items, star for event promo)
("v", "rundown_status",          0, 0, -1,          False),              # OFFLINE, READY etc
("v", "rundown_broadcast",       0, 0, -1,          False),              # Scheduled start time of block/item
("v", "rundown_scheduled",       0, 0, -1,          False),              # Real computed start time of the item
("v", "rundown_difference",      0, 0, -1,          False),              # Real computed start time of the item
("E", "run_mode",                0, 0, INTEGER,     False),              # AUTO / MANUAL / SOFT AUTO / HARD AUTO

#
# Base metadata
#

("A",  "id_storage",             0, 0, INTEGER,     False),
("A",  "path",                   1, 1, TEXT,        False),
("A",  "article",                1, 1, BLOB,        {"syntax" : "md"}),
("A",  "subclips",               0, 0, REGIONS,     False),
("A",  "meta_probed",            0, 0, BOOLEAN,     False),              # If true, meta_probes would not overwrite non-technical metadata during update

("AI", "mark_in",                1, 0, TIMECODE,    False),
("AI", "mark_out",               1, 0, TIMECODE,    False),

("m",  "title",                  1, 1, TEXT,        False),              # dc.title.main - The title most commonly associated with the resource.
("m",  "title/subtitle",         1, 1, TEXT,        False),              # dc.title.subtitle - Ancillary title information for the resource.
("m",  "title/alternate",        1, 1, TEXT,        False),              # dc.title.alternate - Where a resource is known by more than one name
("m",  "title/series",           1, 1, CS_SELECT,   "series"),           # dc.title.series - Where the resource is part of a series, name of the serie.
("m",  "title/original",         1, 1, TEXT,        False),              # ebucore.title.original
("m",  "description",            1, 1, BLOB,        {"syntax" : "md"}),
("m",  "description/original",   1, 1, BLOB,        {"syntax" : "md"}),
("m",  "promoted",               1, 0, BOOLEAN,     False),              # Asset "promotion". It"s hit, important, favourite,....

("m",  "series/season",          1, 0, INTEGER,     False),
("m",  "series/episode",         1, 0, INTEGER,     False),

("m",  "language",               1, 0, CS_SELECT,   "languages"),
("m",  "date",                   1, 0, DATETIME,    {"mode":"date"}),
("m",  "date/valid",             1, 0, DATETIME,    {"mode":"date"}),
("m",  "subject",                1, 1, BLOB,        False),              # Keywords
("m",  "rights",                 1, 1, BLOB,        False),
("m",  "version",                1, 1, TEXT,        False),
("m",  "notes",                  1, 1, BLOB,        False),
("m",  "runs",                   0, 0, INTEGER,     False),


("m",  "source",                 0, 1, TEXT,        False),              # Youtube, Vimeo, PirateBay....
("m",  "source/url",             0, 1, TEXT,        False),              # youtube url, torrent magnet link....

("m",  "format",                 1, 1, CS_SELECT,   "formats"),          # documentary / featrure / clip / sport event / ....
("m",  "genre",                  1, 1, CS_SELECT,   "genres"),           # horror / football / punk rock

("m",  "identifier/main",        1, 1, TEXT,        False),              # Primary Content ID (IDEC, GUID...)
("m",  "identifier/youtube",     0, 1, TEXT,        False),              # Youtube ID if exists
("m",  "identifier/vimeo",       0, 1, TEXT,        False),              # Vimeo ID if exists
("m",  "identifier/imdb",        1, 1, TEXT,        False),              # IMDB ID for movies

("m",  "role/director",          1, 1, TEXT,        False),              # ebu_RoleCode 20.16
("m",  "role/composer",          1, 1, TEXT,        False),              # ebu_RoleCode 17.1.7 (music)
("m",  "role/performer",         1, 1, TEXT,        False),              # ebu_RoleCode 17.2   (music) (A.K.A Artist)


("m",  "album",                  1, 1, TEXT,        False),
("m",  "album/track",            1, 0, INTEGER,     False),
("m",  "album/disc",             1, 0, INTEGER,     False),

("m",  "contains/cg_text",       1, 0, BOOLEAN,     False),              # TODO: Create ENUMS for contains/* (full frontal etc.)
("m",  "contains/nudity",        1, 0, BOOLEAN,     False),
("m",  "contains/violence",      1, 0, BOOLEAN,     False),

("m",  "commercials/client",     1, 1, CS_SELECT,   "clients"),


("f", "duration",                0, 0, TIMECODE,    False),              # Clip duration. From ffprobe/format/duration. if fails, taken from streams[0]/duration
("f", "file/mtime",              0, 0, DATETIME,    False),              # Timestamp of file last modification
("f", "file/size",               0, 0, INTEGER,     False),              # File size in bytes
("f", "file/format",             0, 0, TEXT,        False),              # Container format name. from ffprobe/format/format_name
("f", "video/width",             0, 0, INTEGER,     False),              # Video frame / image width (pixels)
("f", "video/height",            0, 0, INTEGER,     False),              # Video frame / image height (pixels)
("f", "video/fps",               0, 0, FRACTION,    False),
("f", "video/pixel_format",      0, 0, TEXT,        False),
("f", "video/aspect_ratio",      0, 0, FRACTION,    False),
("f", "video/codec",             0, 0, TEXT,        False),
("f", "audio/codec",             0, 0, TEXT,        False),

("q", "qc/state",                1, 0, ENUM,        ENUM_STATES),        # 1 and 2 are reserved for Auto QC failed and passed states
("q", "qc/report",               1, 0, BLOB,        False),              # Holds error report from QC Pass and/or rejection/approval message from QC humanoid
("q", "audio/bpm",               0, 0, NUMERIC,     False),              # Music BPM
("q", "audio/r128/i",            0, 0, NUMERIC,     False),              # Integrated loudness (LUFS)
("q", "audio/r128/t",            0, 0, NUMERIC,     False),              # Integrated loudness threshold (LUFS)
("q", "audio/r128/lra",          0, 0, NUMERIC,     False),              # LRA (LU)
("q", "audio/r128/lra/t",        0, 0, NUMERIC,     False),              # Loudness range threshold (LUFS)
("q", "audio/r128/lra/l",        0, 0, NUMERIC,     False),              # LRA Low (LUFS)
("q", "audio/r128/lra/r",        0, 0, NUMERIC,     False),              # LRA High (LUFS)
("q", "audio/silence",           0, 0, REGIONS,     False),              # Areas with silent audio
("q", "audio/clipping",          0, 0, REGIONS,     False),              # Audio clipping areas
("q", "video/black",             0, 0, REGIONS,     False),              # Areas where video is black-only
("q", "video/static",            0, 0, REGIONS,     False)               # Areas with static image

]

