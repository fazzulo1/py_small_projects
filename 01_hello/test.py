#!/usr/bin/env python3
import os
from subprocess import getoutput, getstatusoutput

prg = "./hello.py"
prg_arg = "./arg_hello.py Mary Jane"
prg_opt_arg = "./opt_arg_hello.py -n anything"
prg_opt_arg2 = "./opt_arg_hello.py"

# ------------------------------------------------
def test_exists():
    assert os.path.isfile(prg)

# ------------------------------------------------
def test_runnable():
    out = getoutput(f"python3 {prg}")
    assert out.strip() == "Hello world"

# ------------------------------------------------
def test_executable():
    out = getoutput(prg)
    assert out.strip() == "Hello world"

# -------------------------------------------------
def test_usage():
    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg_arg} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage")

def test_arg():
    out = getoutput(prg_arg)
    assert out.strip() == "Hello Mary Jane"

# -------------------------------------------------
def test_opt_arg():
    out = getoutput(prg_opt_arg)
    print(out.strip())
    assert out.strip() == "Hello anything"

# -------------------------------------------------
def test_opt_arg_2():
    out = getoutput(prg_opt_arg2)
    assert out.strip() == "Hello world"
