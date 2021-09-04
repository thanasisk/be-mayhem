#!/usr/bin/env python3
import os
import sys
import subprocess
from collections.abc import Iterable
ALLOWED_ASSEMBLERS = [ "vasm6502_oldstyle" ]

def build(file, ins):
    ins_line = ins.split()
    if ins_line[0] != ";BLD": # TODO: expand
        print("Invalid BLD sequence - how we even got here?")
        sys.exit(-1)
    ins_line.pop(0)
    assembler = ins_line.pop(0)
    if assembler not in ALLOWED_ASSEMBLERS:
        print("Invalid assembler: %s - exiting" % assembler)
        sys.exit(-1)
    stem = file.split(".")[0]
    final = stem + ".prg"
    lst = stem + ".lst"
    # flatten cmd line as a workaround ...
    cmd_line = assembler, file, ins_line,"-L", lst, "-o", final
    cmd_line = flatten(cmd_line)
    print(cmd_line)
    subprocess.Popen(cmd_line)

def find_assembly(directory):
    os.chdir(directory)
    for file in [f for f in os.listdir('.') if f.endswith('.asm')]:
        ins = has_build_instructions(file)
        if ins is not None:
            build(file, ins)

def has_build_instructions(asm):
    with open(asm, "r") as ifile:
        candidate = ifile.readline()
        if candidate.startswith(";BLD "):
            return candidate
    return None
# utility method
def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
# find all directories
dirs = os.listdir(".")
# for all directories, step in and check if there is at least one .asm file
for directory in dirs:
    if os.path.isdir(directory) and not directory.startswith("."):
        find_assembly(directory)
        # compile asm file with options given on file

