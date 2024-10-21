#!/usr/bin/env python3

# Generate test file: ascii-control-chars.txt

control_chars = [i for i in range(32)]

with open("ascii-control-chars.txt", mode="wb") as f:
    f.write(bytes(control_chars))
