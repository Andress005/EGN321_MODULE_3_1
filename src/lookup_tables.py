"""
EGN 321 — Module 3, Assignment 3.1
Lookup table data.

The values below are taken from the course-provided
valve_lookup_table.csv / engineering lookup table.

Each valve family maps to a list of:
    (temperature_c, coefficient)
"""

LOOKUP_TABLES = {
    "VX-100": [
        (20, 0.88),
        (40, 0.93),
        (60, 0.99),
        (80, 1.06),
        (100, 1.14),
    ],
    "VX-200": [
        (10, 1.10),
        (30, 1.18),
        (50, 1.27),
        (70, 1.39),
        (90, 1.54),
    ],
    "VX-300": [
        (25, 1.42),
        (50, 1.55),
        (75, 1.71),
        (100, 1.90),
        (125, 2.12),
    ],
}