#!/usr/bin/env python

import os
import sys
import json

from defaults import *

def make_trans_table(lang_code):
    trans_table_fname = os.path.join("aliases", "meta-aliases-{}.json".format(lang_code))
    prev = {}
    l = json.load(open(trans_table_fname))
    for key, alias, col, description in l:
        prev[key] = [alias, col, description]

    mdata = []
    for key in data["meta_types"]:
        if key in prev:
            alias, col, description = prev[key]
        else:
            alias, col, description = "", "", ""
        mdata.append([
            "\"{}\"".format(key),
            "\"{}\"".format(alias),
            "\"{}\"".format(col),
            "\"{}\"".format(description),
            ])

    result = "[\n"
    for i, r in enumerate(mdata):
        if i < len(mdata) - 1:
            r.append(",")
        else:
            r.append("")
        result += """  [{:<25}, {:<25}, {:<20}, {}]{}\n""".format(*r)
    result+= "]"
    f = open(trans_table_fname, "w")
    f.write(result)
    f.close()


if __name__ == "__main__":
    for lang_code in [
                "en",
            ]:
        make_trans_table(lang_code)
