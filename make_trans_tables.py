#!/usr/bin/env python

import os
import sys
import json

from setup import *

def make_trans_table(lang_code):
    trans_table_fname = os.path.join("support", "aliases-{}.json".format(lang_code))

    prev = {}
    l = json.load(open(trans_table_fname))
    for key, alias, col in l:
        prev[key] = [alias, col]

    data = []
    for ns, key, e, f, c, s in BASE_META_SET:
        if key in prev:
            alias, col = prev[key]
        else:
            alias, col = "", ""
        data.append([
            "\"{}\"".format(key),
            "\"{}\"".format(alias),
            "\"{}\"".format(col),
            ])

    result = "[\n"
    for i, r in enumerate(data):
        if i < len(data) - 1:
            r.append(",")
        else:
            r.append("")
        result += """  [{:<25}, {:<25}, {}]{}\n""".format(*r)
    result+= "]"
    f = open(trans_table_fname, "w")
    f.write(result)
    f.close()


if __name__ == "__main__":
    for lang_code in [
                "en",
                "cs"
            ]:
        make_trans_table(lang_code)
