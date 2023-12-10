# Advent of Code 2023
# ===================
In python.
Usually TDD, but sometimes if I'm in a hurry I do an experiment and don't look back if AoC tells me it's correct.

**I'm happy about any feedback on my solutions.**

# Setup
`python -m venv venv`
`pip install -r requirements.txt`

# Run Tests
`pytest`

# Run Solution
Example for day one:
`cd aoc_1 && python aoc_1.py`

# Script to create new day and pull input.txt
Extract session cookie from Advent Of Code website after being logged in.
`cp .env.example .env`
Store session cookie in .env file in root directory.
`python init_day.py`
Wait for prompt and enter a day between 1 and 25.