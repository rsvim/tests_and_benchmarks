#!/usr/bin/env python3

# Generate test file: ascii-control-chars.txt
# See: https://www.ascii-code.com/

control_chars = [i for i in range(32)]

with open("ascii_control_chars.txt", mode="wb") as f:
    f.write(bytes(control_chars))
