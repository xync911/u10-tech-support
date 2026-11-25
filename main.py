"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one funny line from a hopeless tech support agent,
spoken to a desperate customer, at most 199 characters.
The agent is cheerful and useless in equal measure, and the twist
is that the fix is not just turning it off and on again — the
customer must also apologize to the computer first.
The customer is never the butt of the joke; the computer is.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
