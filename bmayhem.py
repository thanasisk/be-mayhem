#!/usr/bin/env python3
# (C) Athanasios Kostopoulos 2021
# GPLv3
import os
import sys
import subprocess
from collections.abc import Iterable
import argparse

SIG = ";MHM"
ALLOWED_ASSEMBLERS = [
"vasm6502_madmac",
"vasm6502_oldstyle",
"vasm6502_std",
"vasm6800_oldstyle",
"vasm6800_std",
"vasm6809_oldstyle",
"vasm6809_std",
"vasmarm_std",
"vasmc16x_std",
"vasmjagrisc_madmac",
"vasmjagrisc_std",
"vasmm68k_madmac",
"vasmm68k_mot",
"vasmm68k_std",
"vasmpdp11_std",
"vasmppc_std",
"vasmqnice_std",
"vasmtr3200_oldstyle",
"vasmtr3200_std",
"vasmvidcore_std",
"vasmx86_std",
"vasmz80_oldstyle",
"vasmz80_std" ]

def build(file, ins):
    ins_line = ins.split()
    if ins_line[0] != SIG: # TODO: expand
        print("Invalid BLD sequence - how we even got here?")
        sys.exit(-1)
    ins_line.pop(0)
    assembler = ins_line.pop(0)
    suffix = ins_line.pop(0)
    if assembler not in ALLOWED_ASSEMBLERS:
        print("Invalid assembler: %s - exiting" % assembler)
        sys.exit(-1)
    stem = file.split(".")[0]
    final = stem + "." + suffix
    lst = stem + ".lst"
    # flatten cmd line as a workaround ...
    cmd_line = assembler, file, ins_line,"-L", lst, "-o", final
    cmd_line = flatten(cmd_line)
    subprocess.Popen(cmd_line)

def find_assembly(directory):
    popdir = os.getcwd()
    os.chdir(directory)
    for file in [f for f in os.listdir('.') if f.endswith('.asm')]:
        ins = has_build_instructions(file)
        if ins is not None:
            build(file, ins)
    os.chdir(popdir)

def has_build_instructions(asm):
    """
    is the first line starting with ;BLD? if yes, it is a candidate
    """
    with open(asm, "r") as ifile:
        candidate = ifile.readline()
        if candidate.startswith(SIG):
            return candidate
    return None

# utility method
def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--inputdir",type=str,
    help="top-level directory to scan for asm", default=".")
    args = parser.parse_args()
    # find all directories
    dirs = os.listdir(args.inputdir)
    # for all directories, step in and check if there is at least one .asm file
    for directory in dirs:
        if os.path.isdir(directory) and not directory.startswith("."):
            find_assembly(directory)

if __name__ == "__main__":
    main()
