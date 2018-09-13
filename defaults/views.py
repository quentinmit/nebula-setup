VIEWS = {
    1: {
        "title" : "Main",
        "position" : 1,
        "folders" : [1, 2],
        "states" : [0, 1, 2, 5, 11],
        "columns" : [
                "qc/state",
                "title",
                "subtitle",
                "id/main",
                "duration",
                "mtime"
            ]
    },


    2 : {
        "title" : "Fill",
        "position" : 2,
        "folders" : [5, 6, 7, 8],
        "states" : [0, 1, 2, 5, 11],
        "columns" : [
                "qc/state",
                "title",
                "id/main",
                "id_folder",
                "duration",
            ]
    },


    3 : {
        "title" : "Music",
        "position" : 3,
        "folders" : [4],
        "states" : [0, 1, 2, 5, 11],
        "columns" : [
                "promoted",
                "title",
                "role/performer",
                "genre",
                "duration",
            ]
    },


    4 : {
        "title" : "Stories",
        "position" : 4,
        "folders" : [3],
        "states" : [0, 1, 2, 5, 11],
        "columns" : [
                "qc/state",
                "title",
                "genre",
            ]
    },


    5 : {
        "title" : "Commercial",
        "position" : 5,
        "folders" : [9, 10],
        "states" : [0, 1, 2, 5, 11],
        "columns" : [
                "qc/state",
                "title",
                "commercial/client",
                "duration",
                "mtime",
                "genre",
            ]
    },

#
# Auxiliary views
#

    10 : {
        "title" : "-",
        "position" : 10,
    },

    11 : {
        "title" : "Trash",
        "position" : 11,
        "states" : [3],
        "columns" : [
                "title",
                "id/main",
                "mtime"
            ]
    },

    12 : {
        "title" : "Archive",
        "position" : 12,
        "states" : [4, 11],
        "columns" : [
                "title",
                "id/main",
                "mtime"
            ]
    }

}  # END FOLDERS
