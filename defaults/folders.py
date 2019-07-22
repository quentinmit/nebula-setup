

primary_description = [
            ("title", {}),
            ("subtitle", {}),
            ("description", {}),
            ("keywords", {}),

    ]

serie_description = [
        ("serie", {}),
        ("serie/season", {}),
        ("serie/episode", {}),
    ]

roles_description = [
        ("role/director", {}),
        ("role/cast", {}),
    ]

movie_genre_pattern = "^3\.(1|4|5|7|8|9)(\.\d+){0,2}$"
music_genre_pattern = "^3\.6\.(\d|4.(\d|14(.\d)?))$"
content_description = [
        ("genre", {"filter" : movie_genre_pattern}),
        ("editorial_format", {"filter" : "^2(\.\d+){0,2}$"}),
        ("atmosphere", {}),
        ("intention", {"filter" : "^1\.(1|2|3|4|5|6|7|8)$"}),
        ("intended_audience", {}),
        ("content_alert", {}),
        ("content_alert/scheme", {"filter" : "^53\.1\.\d", "default": "53.1.1"}),
    ]

production_description = [
        ("date/valid", {}),
        ("editorial_control", {}),
        ("rights", {}),
        ("rights/type", {}),
        ("rights/description", {}),
        ("notes", {}),
        ("qc/report", {}),
    ]


FOLDERS = {

#
# Main
#

    1 : {
        "title" : "Movie",
        "color" : 0x2872B3,
        "meta_set" : \
                primary_description + \
                roles_description + \
                content_description + \
                production_description
    },


    2 : {
        "title" : "Episode",
        "color" : 0x0397BB,
        "meta_set" : \
                primary_description + \
                serie_description + \
                roles_description + \
                content_description + \
                production_description
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
            ] + production_description
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
                ("genre", {"cs" : "urn:ebu:metadata-cs:ContentGenreCS", "filter" : music_genre_pattern}),
                ("content_alert", {}),
                ("content_alert/scheme", {}),

            ] + production_description
    },

    5 : {
        "title" : "Fill",
        "color" : 0x81c77f,
        "meta_set" : \
                primary_description + \
                content_description + \
                production_description
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
                ("title/original", {}),
                ("subtitle", {}),
                ("subtitle/original", {}),
                ("description", {}),
                ("description/original", {}),

                ("qc/report", {}),
            ]
    },

    13 : {
        "title" : "Series",
        "color" : 0xa0aac5,
        "meta_set" : [
                ("title", {}),
                ("description", {}),
                ("genre", {}),
                ("editorial_format", {}),
                ("intention", {"filter" : "^1\.(1|2|3|4|5|6|7|8)$"}),
                ("intended_audience", {}),
                ("editorial_control", {}),
                ("rights", {}),
                ("rights/type", {}),
                ("rights/description", {}),
                ("notes", {}),
            ],
        "links" : [
                {
                    "source_key" : "id",
                    "target_key" : "serie",
                    "id_view" : 1,
                    "title": "Show episodes"
                }
            ]
    },

} # END OF FOLDERS
