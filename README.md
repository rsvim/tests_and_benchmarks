# RSVIM Tests and Benchmarks

This repository contains resources of tests and benchmarks for the RSVIM editor.

There are some python scripts and text files for testing/benchmarking the editor.

## Requirements

Requirements:

- Bash compatible shells and core utils: `bash`, `curl`, `wget`, `tar`.
- [Python 3.9+](https://www.python.org/), please setup the environment with:
  - Create venv: `python3 -m venv ./venv`
  - Activate venv: `source ./venv/bin/activate`
  - Install dependencies: `python3 -m pip install -r requirements..txt`

## Setup

1. To setup the tests and benches, please first clone [rsvim](https://github.com/rsvim/rsvim):

   ```bash
   git clone https://github.com/rsvim/rsvim
   ```

2. Then `cd` into the `rsvim` project, then clone this [tests_and_benchmarks](https://github.com/rsvim/tests_and_benchmarks):

   ```bash
   cd ./rsvim
   git clone --depth=1 https://github.com/rsvim/tests_and_benchmarks
   ```

3. Or you could clone this project under the same directory with `rsvim`, and create a symlink for it:

   ```bash
   # Don't have to `cd ./rsvim`
   git clone --depth=1 https://github.com/rsvim/tests_and_benchmarks

   # Create symlink
   ln -s $PWD/tests_and_benchmarks $PWD/rsvim/tests_and_benchmarks
   ```
