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
                ("genre", {"cs" : "urn:nxtv:metadata-cs:movie-genres"}),
                ("content_alert", {}),
                ("date/valid", {}),
            ]
    },

    2 : {
        "title" : "Serie",
        "color" : 0x0397BB,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("description", {}),
                ("serie", {}),
                ("genre", {"cs" : "urn:nxtv:metadata-cs:movie-genres"}),
                ("serie/season", {}),
                ("serie/episode", {}),
                ("content_alert", {}),
                ("date/valid", {}),
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
                ("date/valid", {}),
            ]
    },

    6 : {
        "title" : "Trailer",
        "color" : 0x008E5C,
        "meta_set" : [
                ("title", {}),
                ("subtitle", {}),
                ("date/valid", {}),
            ]
    },

    7 : {
        "title" : "Jingle",
        "color" : 0xcf1f45,
        "meta_set" : [
                ("title", {}),
            ]
    },

    8 : {
        "title" : "Graphics",
        "color" : 0xf2799c,
        "meta_set" : [
                ("title", {})
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
            ]
    },

    10 : {
        "title" : "Teleshopping",
        "color" : 0xe3d6d5,
        "meta_set" : [
                ("title", {}),
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
        "title" : "Incomming",
        "color" : 0x998e88,
        "meta_set" : [
                ("title", {}),
                ("description", {}),
                ("qc/report", {}),
            ]
    },

} # END OF FOLDERS


import socket
HOST = socket.gethostname()

SERVICES = {
    1  : ["mesg",   HOST, "mesg",  "template/services/mesg.xml",  True,  5],
}
