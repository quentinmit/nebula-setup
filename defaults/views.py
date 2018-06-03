VIEWS = {
    1: {
        "title" : "Main",
        "owner" : 0,
        "position" : 1,
        "settings" : """<?xml version="1.0"?>
<view>
    <folders>1,2</folders>
    <statuses>0,1,2,5</statuses>
    <columns>
        <column>qc/state</column>
        <column>title</column>
        <column>subtitle</column>
        <column>id/main</column>
        <column>duration</column>
        <column>mtime</column>
    </columns>
</view>"""
    },


    2 : {
        "title" : "Fill",
        "owner" : 0,
        "position" : 2,
        "settings" : """
<view>
    <folders>5,6,7,8</folders>
    <statuses>0,1,2,5</statuses>
    <columns>
        <column>qc/state</column>
        <column>title</column>
        <column>id/main</column>
        <column>id_folder</column>
        <column>duration</column>
    </columns>
</view>"""
    },


    3 : {
        "title" : "Music",
        "owner" : 0,
        "position" : 3,
        "settings" : """<?xml version="1.0"?>
<view>
    <folders>4</folders>
    <statuses>0,1,2,5</statuses>
    <columns>
        <column>promoted</column>
        <column>title</column>
        <column>role/performer</column>
        <column>genre</column>
        <column>duration</column>
    </columns>
</view>"""
    },


    4 : {
        "title" : "Stories",
        "owner" : 0,
        "position" : 4,
        "settings" : """<?xml version="1.0"?>
<view>
    <folders>3</folders>
    <statuses>0,1,2,5</statuses>
    <columns>
        <column>qc/state</column>
        <column>title</column>
        <column>genre</column>
    </columns>
</view>"""
    },


    5 : {
        "title" : "Commercial",
        "owner" : 0,
        "position" : 5,
        "settings" : """<?xml version="1.0"?>
<view>
    <folders>9,10</folders>
    <statuses>0,1,2,5</statuses>
    <columns>
        <column>title</column>
        <column>commercial/client</column>
        <column>duration</column>
        <column>mtime</column>
    </columns>
</view>"""
    },


#
# Auxiliary views
#


    10 : {
        "title" : "-",
        "owner" : 0,
        "position" : 10,
        "settings" : "<?xml version=\"1.0\"?><view/>"
    },

    11 : {
        "title" : "Trash",
        "owner" : 0,
        "position" : 11,
        "settings" : """<?xml version="1.0"?>
<view>
    <statuses>3</statuses>
    <columns>
        <column>title</column>
    </columns>
</view>"""
    },

    12 : {
        "title" : "Archive",
        "owner" : 0,
        "position" : 12,
        "settings" : """<?xml version="1.0"?>
<view>
    <statuses>4</statuses>
    <columns>
        <column>title</column>
    </columns>
</view>"""
    }

}  # END FOLDERS
