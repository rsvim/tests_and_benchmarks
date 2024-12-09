# RSVIM Tests and Benchmarks

This repository contains resources of tests and benchmarks for the RSVIM editor.

There are some python scripts and text files for testing/benchmarking the editor.

## Setup Tests and Benchmarks

Requirements:

- `bash` or `zsh`.
- `curl` and `wget`.
- `tar`.
- [Python 3.9+](https://www.python.org/), please setup the environment with:
  - Create venv: `python3 -m venv ./venv`
  - Activate venv: `source ./venv/bin/activate`
  - Install dependencies: `python3 -m pip install -r requirements..txt`

### Create `tests` and `benches` directories for `rsvim`

To setup the tests and benches, please clone both [rsvim](https://github.com/rsvim/rsvim) and this [tests_and_benchmarks](https://github.com/rsvim/tests_and_benchmarks) project under the same working directory, then create link under `rsvim` project:

```bash
# Clone the two projects:
git clone --depth=1 https://github.com/rsvim/rsvim
git clone --depth=1 https://github.com/rsvim/tests_and_benchmarks

# Remove existed folders
rm -rf $PWD/rsvim/rsvim_cli/tests
rm -rf $PWD/rsvim/rsvim_cli/benches

# Create folder link
ln -s $PWD/tests_and_benchmarks/cli-tests $PWD/rsvim/rsvim_cli/tests
ln -s $PWD/tests_and_benchmarks/cli-benches $PWD/rsvim/rsvim_cli/benches
```

<!-- ### Download External Resources -->
<!---->
<!-- There're some external resources we use to test/benchmark, please run `python3 install.py` scripts to download/install them. -->
