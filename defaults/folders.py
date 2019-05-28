FOLDERS = {

#
# Main
#

    1 : {
        "title" : "Movie",
        "color" : 0x2872B3,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("description", {}),
                ("keywords", {}),

                ("role/director", {}),
                ("role/cast", {}),

                ("genre", {"cs" : "urn:nxtv:metadata-cs:movie-genres"}),
                ("intention", {}),
                ("atmosphere", {}),
                ("intended_audience", {}),

                ("editorial_format", {}),
                ("content_alert", {}),

                # production notes
                ("date/valid", {}),
                ("editorial_control", {}),
                ("rights", {}),
                ("rights/type", {}),
                ("rights/description", {}),
                ("qc/report", {}),
                ("notes", {}),
            ]
    },

    2 : {
        "title" : "Serie",
        "color" : 0x0397BB,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("description", {}),
                ("keywords", {}),

                ("role/director", {}),
                ("role/cast", {}),

                ("genre", {"cs" : "urn:nxtv:metadata-cs:movie-genres"}),
                ("intention", {}),
                ("atmosphere", {}),
                ("intended_audience", {}),

                ("editorial_format", {}),
                ("content_alert", {}),

                ("serie", {}),
                ("serie/season", {}),
                ("serie/episode", {}),

                # production notes
                ("date/valid", {}),
                ("editorial_control", {}),
                ("rights", {}),
                ("rights/type", {}),
                ("rights/description", {}),
                ("qc/report", {}),
                ("notes", {}),
            ]
    },

#
# Shorts
#

    3 : {
        "title" : "Story",
        "color" : 0x00b9ce,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("description", {}),
                ("article", {}),

                # production notes
                ("editorial_control", {}),
                ("rights", {}),
                ("rights/type", {}),
                ("rights/description", {}),
                ("qc/report", {}),
                ("notes", {}),
            ]
    },

    4 : {
        "title" : "Song",
        "color" : 0xb9c0dd,
        "meta_set" : [
                ("title", {}),
                ("role/performer", {}),
                ("role/composer", {}),
                ("album", {}),
                ("year", {}),

                ("description", {}),
                ("genre", {"cs" : "urn:nxtv:metadata-cs:music-genres"}),
                ("content_alert", {}),

                # production notes
                ("rights", {}),
                ("rights/type", {}),
                ("rights/description", {}),
                ("qc/report", {}),
                ("notes", {}),
            ]
    },

    5 : {
        "title" : "Fill",
        "color" : 0x81c77f,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("description", {}),
                ("genre", {"cs" : "urn:nxtv:metadata-cs:movie-genres"}),

                # production notes
                ("editorial_control", {}),
                ("rights", {}),
                ("rights/type", {}),
                ("rights/description", {}),
                ("qc/report", {}),
                ("notes", {}),
            ]
    },

    6 : {
        "title" : "Trailer",
        "color" : 0x008E5C,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("date/valid", {}),
                ("qc/report", {}),
                ("notes", {}),
            ]
    },

    7 : {
        "title" : "Jingle",
        "color" : 0xcf1f45,
        "meta_set" : [
                ("title", {}),
                ("graphic_usage", {}),
                ("notes", {}),
            ]
    },

    8 : {
        "title" : "Graphics",
        "color" : 0xf2799c,
        "meta_set" : [
                ("title", {}),
                ("graphic_usage", {}),
                ("notes", {}),
            ]
    },

#
# Commercial content
#

    9 : {
        "title" : "Commercial",
        "color" : 0xf6d258,
        "meta_set" : [
                ("title", {}),
                ("commercial/client", {}),
                ("commercial/content", {}),
                ("notes", {}),
            ]
    },

    10 : {
        "title" : "Teleshopping",
        "color" : 0xe3d6d5,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("commercial/client", {}),
                ("commercial/content", {}),
                ("notes", {}),
            ]
    },

#
# Aux
#

    11 : {
        "title" : "Dataset",
        "color" : 0xa0aac5,
        "meta_set" : [
                ("title", {})
            ]
    },

    12 : {
        "title" : "Incoming",
        "color" : 0x998e88,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("description", {}),
                ("qc/report", {}),
            ]
    },

} # END OF FOLDERS
