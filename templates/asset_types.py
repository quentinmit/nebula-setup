ASSET_TYPES = {
    1 : {
        "title" : "Movies",
        "color" : 0x2872B3,
        "meta_set" : [
                ("title",               {}),
                ("subtitle",            {}),
                ("title/original",      {}),
                ("description",         {}),
                ("description/original",{}),
                ("role/director",       {}),
                ("genre",               {"cs" : "urn:immstudios:metadata-cs:movie-genres"}),
                ("keywords",            {}),
                ("content_alert",       {}),
            ]
    },

    2 : {
        "title" : "Series",
        "color" : 0x0397BB,
        "meta_set" : [
                ("title",               {}),
                ("subtitle",            {}),
                ("title/original",      {}),
                ("subtitle/original",   {}),
                ("serie",               {}),
                ("description",         {}),
                ("description/original",{}),
                ("role/director",       {}),
                ("genre",               {"cs" : "urn:immstudios:metadata-cs:movie-genres"}),
                ("keywords",            {}),
                ("serie/season",        {}),
                ("serie/episode",       {}),
                ("content_alert",       {}),
                ("qc/report",           {}),
            ]
    },

    3 : {
        "title" : "Trailers",
        "color" : 0x008E5C,
        "meta_set" : [
                ("title",               {}),
            ]
    },

    4 : {
        "title" : "Jingles",
        "color" : 0xE0E0E0,
        "meta_set" : [
                ("title",               {}),
            ]
    },

    5 : {
        "title" : "Music",
        "color" : 0x8AC91A,
        "meta_set" : [
                ("title",               {}),
                ("role/performer",      {}),
                ("role/composer",       {}),
                ("album",               {}),
                ("description",         {}),
                ("description/original",{}),
                ("genre",               {"cs" : "urn:immstudios:metadata-cs:music-genres"}),
                ("contains/cg_text",    {}),
                ("qc/report"       ,    {}),
            ]
    },

    6 : {
        "title" : "News",
        "color" : 0xFE0002,
        "meta_set" : [
            ("title",                   {}),
            ("title/subtitle",          {}),
            ("description",             {}),
            ("identifier/main",         {}),
            ("article",                 {}),
        ]
    },

    7 : {
        "title" : "Fill",
        "color" : 0x646464,
        "meta_set" : [
            ("title",                   {}),
            ("description",             {}),
            ("description/original",    {}),
            ("genre",                   {"cs" : "urn:immstudios:metadata-cs:movie-genres"}),
            ("qc/report",               {}),
        ]
    },

    8 : {
        "title" : "Templates",
        "color" : 0xC7037F,
        "meta_set" : [
            ("title",                   {})
        ]
    },

    10 : {
        "title" : "Incomming",
        "color" : 0xb0b0b0,
        "meta_set" : [
            ("title",                  {}),
            ("description",            {}),
            ("qc/report",              {}),
        ]
    }


} # END OF ASSET_TYPES
