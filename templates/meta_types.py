__all__ = ["META_TYPES"]

STRING       = 0       # Single-line plain text (default)
TEXT         = 1       # Multiline text. 'syntax' can be provided in config
INTEGER      = 2       # Integer only value (for db keys etc)
NUMERIC      = 3       # Any integer of float number. 'min', 'max' and 'step' values can be provided in config
BOOLEAN      = 4       # 1/0 checkbox
DATETIME     = 5       # Date and time information. Stored as timestamp
TIMECODE     = 6       # Timecode information, stored as float(seconds), presented as HH:MM:SS:FF or HH:MM:SS.CS (centiseconds)
REGIONS      = 7
FRACTION     = 8       # 16/9 etc. Stored as string
SELECT       = 9
LIST         = 10


META_TYPES = {

# KEY                      NS   E  I  F  CLASS        SETTINGS

"ctime":                  ("o", 0, 0, 0, DATETIME,    None),              # Creation time
"mtime":                  ("o", 0, 0, 0, DATETIME,    None),              # Last modified time
"mark_in":                ("o", 1, 0, 0, TIMECODE,    None),
"mark_out":               ("o", 1, 0, 0, TIMECODE,    None),
"notes":                  ("o", 1, 0, 1, TEXT,        None),              # Production notes
"promoted":               ("o", 1, 0, 0, BOOLEAN,     None),              # Asset "promotion". It"s hit, important, favourite,....


#
# Asset specific
#

"media_type":             ("a", 0, 1, 0, SELECT,      {"cs" : "urn:immstudios:metadata-cs:MediaTypeCS"}),
"content_type":           ("a", 0, 1, 0, SELECT,      {"cs" : "urn:tva:metadata-cs:ContentTypeCS"}),
"status":                 ("a", 0, 0, 0, INTEGER,     {"default" : 1}),              # OFFLINE, ONLINE, CREATING, TRASHED, ARCHIVED
"version_of":             ("a", 0, 0, 0, INTEGER,     {"default" : 0}),
"id_storage":             ("a", 0, 0, 0, INTEGER,     None),
"path":                   ("a", 0, 0, 1, TEXT,        None),
"subclips":               ("a", 1, 0, 0, REGIONS,     None),
"article":                ("a", 1, 0, 1, TEXT,        {"mode" : "rich"}),

#
# Descriptive
#
# If asset_type is changed and "m" key is not specified in the asset type settings, existing values are deleted
#

#                               E  I  F
"title":                  ("m", 1, 0, 9, STRING,      None),                       # dc.title.main - The title most commonly associated with the resource.
"subtitle":               ("m", 1, 0, 8, STRING,      None),                       # dc.title.subtitle - Ancillary title information for the resource.
"description":            ("m", 1, 0, 7, TEXT,        {"syntax" : "md"}),

"title/original":         ("m", 1, 0, 9, STRING,      None),                       # dc.title.main - The title most commonly associated with the resource.
"subtitle/original":      ("m", 1, 0, 8, STRING,      None),                       # dc.title.subtitle - Ancillary title information for the resource.
"description/original":   ("m", 1, 0, 7, TEXT,        {"syntax" : "md"}),

"language":               ("m", 1, 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:ISO639_1LanguageCodeCS"}),
"editorial_format":       ("m", 1, 0, 1, SELECT,      {"cs" : "urn:ebu:metadata-cs:EditorialFormatCodeCS"}),
"editorial_control":      ("m", 1, 0, 1, SELECT,      {"cs" : "urn:ebu:metadata-cs:EditorialControlCodeCS"}),
"genre":                  ("m", 1, 1, 1, SELECT,      {"cs" : "urn:ebu:metadata-cs:ContentGenreCS"}),
"origination":            ("m", 1, 0, 1, SELECT,      {"cs" : "urn:tva:metadata:cs:OriginationCS"}),
"content_alert":          ("m", 1, 0, 0, LIST,        {"cs" : "urn:tva:metadata-cs:ContentAlertCS"}),
"keywords":               ("m", 1, 0, 9, TEXT,        None),                       # Comma delimited keywords list

"date":                   ("m", 1, 0, 0, DATETIME,    {"mode" : "date"}),
"date/valid":             ("m", 1, 0, 0, DATETIME,    {"mode" : "date"}),
"licence":                ("m", 1, 0, 1, SELECT,      {"cs" : "urn:immstudios:metadata-cs:ContentLicenceCS"}),
"rights":                 ("m", 1, 0, 1, TEXT,        None),

"source":                 ("m", 0, 0, 1, STRING,      None),                       # Youtube, Vimeo, PirateBay....
"source/url":             ("m", 0, 0, 1, STRING,      None),
"source/attribution":     ("m", 0, 0, 1, STRING,      None),
"source/rating":          ("m", 0, 1, 0, INTEGER,     None),                       # Provided rating normalized to: from 0 (worst) to 100 (best)

"commercial_content":     ("m", 1, 0, 0, LIST,        {"cs" : "urn:tva:metadata-cs:ContentCommercialCS"}),
"campaign":               ("m", 1, 0, 0, INTEGER,     None),                       # Campaign event id

"album":                  ("m", 1, 0, 1, STRING,      None),
"serie":                  ("m", 1, 0, 1, STRING,      {"cs" : "urn:site:series"}),
"serie/season":           ("m", 1, 0, 1, INTEGER,     None),
"serie/episode":          ("m", 1, 0, 1, INTEGER,     None),

"id/main":                ("m", 1, 0, 8, STRING,      None),                       # Primary Content ID (local or global)
"id/youtube":             ("m", 0, 0, 8, STRING,      None),                       # Youtube ID if exists
"id/vimeo":               ("m", 0, 0, 8, STRING,      None),                       # Vimeo ID if exists
"id/imdb":                ("m", 1, 0, 8, STRING,      None),                       # IMDB ID for movies
"id/guid":                ("m", 0, 0, 8, STRING,      None),                       # Created automatically when asset is created

"role/director":          ("m", 1, 0, 7, STRING,      None),
"role/performer":         ("m", 1, 0, 7, STRING,      None),
"role/composer":          ("m", 1, 0, 7, STRING,      None),
"role/cast":              ("m", 1, 0, 7, STRING,      None),                       # Coma delimited cast

#
# Technical (automated extraction)
#
# f - format: created by "meta" service
# q - quality/content: created by "analyzer" service
#
#                               E  I  F

"duration":               ("f", 0, 0, 0, TIMECODE,    None),              # Clip duration. From ffprobe/format/duration. if fails, taken from streams[0]/duration
"file/mtime":             ("f", 0, 0, 0, DATETIME,    None),              # Timestamp of file last modification
"file/size":              ("f", 0, 0, 0, INTEGER,     None),              # File size in bytes
"file/format":            ("f", 0, 0, 0, STRING,      None),              # Container format name. from ffprobe/format/format_name
"video/width":            ("f", 0, 0, 0, INTEGER,     None),              # Video frame / image width (pixels)
"video/height":           ("f", 0, 0, 0, INTEGER,     None),              # Video frame / image height (pixels)
"video/fps":              ("f", 0, 0, 0, FRACTION,    None),
"video/pixel_format":     ("f", 0, 0, 0, STRING,      None),
"video/color_range":      ("f", 0, 0, 0, STRING,      None),
"video/color_space":      ("f", 0, 0, 0, STRING,      None),
"video/aspect_ratio":     ("f", 0, 0, 0, FRACTION,    None),
"video/codec":            ("f", 0, 0, 0, STRING,      None),
"audio/codec":            ("f", 0, 0, 0, STRING,      None),

"qc/state":               ("q", 1, 1, 0, INTEGER,     None),              # Special widget 1 and 2 are reserved for Auto QC failed and passed states
"qc/report":              ("q", 1, 0, 0, TEXT,        None),              # Holds error report from QC Pass and/or rejection/approval message from QC humanoid
"audio/bpm":              ("q", 0, 0, 0, NUMERIC,     None),              # Music BPM
"audio/r128/i":           ("q", 0, 0, 0, NUMERIC,     None),              # Integrated loudness (LUFS)
"audio/r128/t":           ("q", 0, 0, 0, NUMERIC,     None),              # Integrated loudness threshold (LUFS)
"audio/r128/lra":         ("q", 0, 0, 0, NUMERIC,     None),              # LRA (LU)
"audio/r128/lra/t":       ("q", 0, 0, 0, NUMERIC,     None),              # Loudness range threshold (LUFS)
"audio/r128/lra/l":       ("q", 0, 0, 0, NUMERIC,     None),              # LRA Low (LUFS)
"audio/r128/lra/r":       ("q", 0, 0, 0, NUMERIC,     None),              # LRA High (LUFS)
"audio/gain/mean":        ("q", 0, 0, 0, NUMERIC,     None),
"audio/gain/peak":        ("q", 0, 0, 0, NUMERIC,     None),
"audio/silence":          ("q", 0, 0, 0, REGIONS,     None),              # Areas with silent audio
"audio/clipping":         ("q", 0, 0, 0, REGIONS,     None),              # Audio clipping areas
"video/black":            ("q", 0, 0, 0, REGIONS,     None),              # Areas where video is black-only
"video/static":           ("q", 0, 0, 0, REGIONS,     None),              # Areas with static image
"video/is_interlaced":    ("q", 0, 0, 0, BOOLEAN,     None),

}
