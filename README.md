# README

## Overview

This Python script, `main.py`, adjusts the display configuration by swapping the origin coordinates in the provided `displayplacer` string. It executes the modified configuration command followed by the original to reassign the primary display settings effectively.

## Purpose

The script is intended for users who need to quickly toggle between display configurations by correcting position values. This can be particularly useful when dealing with multiple monitors and needing to change or fix the origin coordinates rapidly.

## Functionality

- **Input**: Takes a `displayplacer` settings string as an argument. This string should represent display configuration details including origin coordinates (e.g., `origin:(x,y)`).
- **Transformation**: Swaps the two origin values found in the configuration string.
- **Execution**: Executes the swapped display setup command followed by the initial setup command to apply the original settings after swapping.

## Usage

1. Ensure Python3 is installed on your system.
2. Ensure that the `displayplacer` tool is installed and operational (if needed).
3. Run the script using the command line:

```bash
python main.py "<displayplacer configuration string>"
