from nx.core.constants import *

BASE_META_SET = {

# KEY                      NS   E  F  CLASS        SETTINGS

"ctime":                  ("o", 0, 0, DATETIME,    None),              # Creation time
"mtime":                  ("o", 0, 0, DATETIME,    None),              # Last modified time
"mark_in":                ("o", 1, 0, TIMECODE,    None),
"mark_out":               ("o", 1, 0, TIMECODE,    None),
"notes":                  ("o", 1, 1, TEXT,        None),              # Production notes
"promoted":               ("o", 1, 0, BOOLEAN,     None),              # Asset "promotion". It"s hit, important, favourite,....

#
# Asset specific
#

"media_type":             ("a", 0, 0, SELECT,      {"cs" : "urn:immstudios:metadata-cs:MediaTypeCS"}),
"content_type":           ("a", 0, 0, SELECT,      {"cs" : "urn:tva:metadata-cs:ContentTypeCS"}),
"asset_type":             ("a", 1, 0, INTEGER,     None),
"status":                 ("a", 0, 0, INTEGER,     None),              # OFFLINE, ONLINE, CREATING, TRASHED, ARCHIVED
"version_of":             ("a", 0, 0, INTEGER,     None),
"id_storage":             ("a", 0, 0, INTEGER,     None),
"path":                   ("a", 1, 1, TEXT,        None),
"subclips":               ("a", 1, 0, REGIONS,     None),
"article":                ("a", 1, 1, TEXT,        {"mode" : "rich"}),


# Descriptive
#
# If asset_type is changed and "m" key is not specified in the asset type settings, existing values are deleted
#


"title":                  ("m", 1, 1, STRING,      None),                       # dc.title.main - The title most commonly associated with the resource.
"subtitle":               ("m", 1, 1, STRING,      None),                       # dc.title.subtitle - Ancillary title information for the resource.
"description":            ("m", 1, 1, TEXT,        {"syntax" : "md"}),

"language":               ("m", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:ISO639_1LanguageCodeCS"}),
"editorial_format":       ("m", 1, 1, SELECT,      {"cs" : "urn:ebu:metadata-cs:EditorialFormatCodeCS"}),
"editorial_control":      ("m", 1, 1, SELECT,      {"cs" : "urn:ebu:metadata-cs:EditorialControlCodeCS"}),
"genre":                  ("m", 1, 1, SELECT,      {"cs" : "urn:ebu:metadata-cs:ContentGenreCS"}),
"origination":            ("m", 1, 1, SELECT,      {"cs" : "urn:tva:metadata:cs:OriginationCS"}),
"content_alert":          ("m", 1, 0, LIST,        {"cs" : "urn:tva:metadata-cs:ContentAlertCS"}),
"keywords":               ("m", 1, 1, TEXT,        None),                       # Comma delimited keywords list

"date":                   ("m", 1, 0, DATETIME,    {"mode" : "date"}),
"date/valid":             ("m", 1, 0, DATETIME,    {"mode" : "date"}),
"licence":                ("m", 1, 1, SELECT,      {"cs" : "urn:immstudios:metadata-cs:ContentLicenceCS"}),
"rights":                 ("m", 1, 1, TEXT,        None),

"source":                 ("m", 0, 1, STRING,      None),                       # Youtube, Vimeo, PirateBay....
"source/url":             ("m", 0, 1, STRING,      None),
"source/attribution":     ("m", 0, 1, STRING,      None),

"commercial_content":     ("m", 1, 1, LIST,        {"cs" : "urn:tva:metadata-cs:ContentCommercialCS"}),
"campaign":               ("m", 1, 1, INTEGER,     None),                       # Campaign event id

"id/main":                ("m", 1, 1, STRING,      None),                       # Primary Content ID (local or global)
"id/youtube":             ("m", 0, 1, STRING,      None),                       # Youtube ID if exists
"id/vimeo":               ("m", 0, 1, STRING,      None),                       # Vimeo ID if exists
"id/imdb":                ("m", 1, 1, STRING,      None),                       # IMDB ID for movies
"id/guid":                ("m", 0, 1, STRING,      None),                       # Created automatically when asset is created

#
# Technical (automated extraction)
#
# f - format: created by "meta" service
# q - quality/content: created by "analyzer" service
#

"duration":               ("f", 0, 0, TIMECODE,    None),              # Clip duration. From ffprobe/format/duration. if fails, taken from streams[0]/duration
"file/mtime":             ("f", 0, 0, DATETIME,    None),              # Timestamp of file last modification
"file/size":              ("f", 0, 0, INTEGER,     None),              # File size in bytes
"file/format":            ("f", 0, 0, STRING,      None),              # Container format name. from ffprobe/format/format_name
"video/width":            ("f", 0, 0, INTEGER,     None),              # Video frame / image width (pixels)
"video/height":           ("f", 0, 0, INTEGER,     None),              # Video frame / image height (pixels)
"video/fps":              ("f", 0, 0, FRACTION,    None),
"video/pixel_format":     ("f", 0, 0, STRING,      None),
"video/color_range":      ("f", 0, 0, STRING,      None),
"video/color_space":      ("f", 0, 0, STRING,      None),
"video/aspect_ratio":     ("f", 0, 0, FRACTION,    None),
"video/codec":            ("f", 0, 0, STRING       None),
"audio/codec":            ("f", 0, 0, STRING       None),

"qc/state":               ("q", 1, 0, INTEGER,     None),              # Special widget 1 and 2 are reserved for Auto QC failed and passed states
"qc/report":              ("q", 1, 0, TEXT,        None),              # Holds error report from QC Pass and/or rejection/approval message from QC humanoid
"audio/bpm":              ("q", 0, 0, NUMERIC,     None),              # Music BPM
"audio/r128/i":           ("q", 0, 0, NUMERIC,     None),              # Integrated loudness (LUFS)
"audio/r128/t":           ("q", 0, 0, NUMERIC,     None),              # Integrated loudness threshold (LUFS)
"audio/r128/lra":         ("q", 0, 0, NUMERIC,     None),              # LRA (LU)
"audio/r128/lra/t":       ("q", 0, 0, NUMERIC,     None),              # Loudness range threshold (LUFS)
"audio/r128/lra/l":       ("q", 0, 0, NUMERIC,     None),              # LRA Low (LUFS)
"audio/r128/lra/r":       ("q", 0, 0, NUMERIC,     None),              # LRA High (LUFS)
"audio/gain/mean":        ("q", 0, 0, NUMERIC,     None),
"audio/gain/peak":        ("q", 0, 0, NUMERIC,     None),
"audio/silence":          ("q", 0, 0, REGIONS,     None),              # Areas with silent audio
"audio/clipping":         ("q", 0, 0, REGIONS,     None),              # Audio clipping areas
"video/black":            ("q", 0, 0, REGIONS,     None),              # Areas where video is black-only
"video/static":           ("q", 0, 0, REGIONS,     None),              # Areas with static image
"video/is_interlaced":    ("q", 0, 0, BOOLEAN,     None),

}
