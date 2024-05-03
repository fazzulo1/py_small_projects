#!/usr/bin/env python3

import os
from subprocess import getoutput, getstatusoutput

cons = ["bull", "dog"]
vowel_article = ["animal", "ant"]
prg = "./crowsnest.py"
prg_arg = "./arg_crow.py"
prg_vow = "./arg_crow.py"

# ----------------
def test_file_exists():
    assert os.path.isfile(prg)

# ----------------
def test_article_cons():
    for c in cons:
        out = getoutput(f"{prg_arg} {c}")
        assert out.strip() == f"There is a {c}"

#------------------------
def test_article_vowel():
    for v in vowel_article:
        out = getoutput(f"{prg_vow} {v}")
        assert out.strip() == f"There is an {v}"
