# Vehicle Registration Analysis (Python)

A Python program for a university programming course. It reads open
vehicle data from Traficom (Finnish Transport and Communications Agency),
analyzes it and saves the results to text files.

## Features
- Reads a text file of first-registered vehicles (2025 data)
- Counts the vehicles registered in each week of the year
- Categorizes vehicles into four groups by CO2 emissions (WLTP, g/km):
  - Category 1: under 125
  - Category 2: 125-175
  - Category 3: 175-225
  - Category 4: 225 or more
- Saves the results to text files
- Menu-driven interface

## Files
- `HTPerus.py` - main program and menu
- `HTPerusKirjasto.py` - library of functions used by the main program
- `paastot_15.txt` - small sample input file (first 15 rows)

## How to run
1. Install Python 3
2. Download the files into the same folder
3. Run `python HTPerus.py`
4. Choose 1 and enter `paastot_15.txt` to read the data
5. Choose 2 or 4 to analyze, and 3 to save the results

## Input format
Semicolon-separated: `id;EnsirekisterointiPvm;Ajoneuvoluokka;CO2_WLTP`

## Concepts used
- Functions and a separate function library
- Objects stored in lists
- Reading and writing files
- Date handling with the `time` library
- Input validation (file extension must be .txt)

## Status
Basic-level tasks done. Target-level tasks coming soon.
