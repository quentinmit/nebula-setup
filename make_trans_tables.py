#!/usr/bin/env python

import os
import sys
import json
#
# Env setup
#

if sys.version_info[:2] < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')

nebula_root = os.path.abspath(os.getcwd())

#
# Vendor imports
#

vendor_dir = os.path.join(nebula_root, "vendor")
if os.path.exists(vendor_dir):
    for pname in os.listdir(vendor_dir):
        pname = os.path.join(vendor_dir, pname)
        pname = os.path.abspath(pname)
        if not pname in sys.path:
            sys.path.insert(0, pname)

from nebula.template_meta import BASE_META_SET

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
                "en-US",
            ]:
        make_trans_table(lang_code)
