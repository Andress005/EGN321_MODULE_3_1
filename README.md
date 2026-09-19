# EGN 321 — Module 3, Assignment 3.1

## Lookup Tool — Student Package

### Your Goal

Replace difficult-to-read spreadsheet lookup logic with a Python tool that:

1. selects the correct engineering table by valve family;
2. returns exact table values when possible;
3. interpolates between surrounding rows;
4. states and enforces the supported range;
5. refuses extrapolation;
6. proves the behavior with automated tests.

### Assigned Files

* `VALVE_SELECTION_rev3.xlsx`
* `data/valve_lookup_table.csv`
* `data/lookup_challenge_cases.csv`
* starter Python files
* starter tests
* planning templates
* README / AI / Git guides
* guided Colab notebook

### Core Rule

**Interpolate inside the evidence. Refuse outside it.**

The final submission is the GitHub repository link.

### Assignment Documents

* `ASSIGNMENT_SPEC.md` — complete assignment requirements.
* `GRADING_RUBRIC.md` — 100-point grading criteria.

# Module 3 Lookup Tool

## Purpose

This tool replaces the lookup and interpolation logic from the valve selection workbook with a readable and testable Python implementation.

The tool selects a valve coefficient using:

* valve family; and
* operating temperature in degrees Celsius.

For a temperature that exactly matches a lookup-table row, the corresponding coefficient is returned directly.

For a temperature between two supported lookup-table rows, the tool calculates the coefficient using linear interpolation.

Temperatures outside the supported range are rejected instead of being extrapolated.

## Source Data

The lookup data is based on the assigned valve engineering lookup table provided in:

* `VALVE_SELECTION_rev3.xlsx`
* `data/valve_lookup_table.csv`

The lookup table contains temperature and coefficient values for three valve families: `VX-100`, `VX-200`, and `VX-300`.

The Python lookup data is stored in `src/lookup_tables.py` as a clear family-to-table structure rather than nested conditional logic.

## Supported Valve Families

| Family | Minimum Temperature | Maximum Temperature |
| ------ | ------------------: | ------------------: |
| VX-100 |               20 °C |              100 °C |
| VX-200 |               10 °C |               90 °C |
| VX-300 |               25 °C |              125 °C |

## Lookup Behavior

### Exact Lookup

If the requested operating temperature exactly matches a temperature in the selected valve family's table, the corresponding coefficient is returned.

For example:

```text
VX-100 at 20 °C → 0.88
```

The result identifies the method as `exact`.

### Surrounding-Row Search

If there is no exact temperature match, the tool searches the selected family's table for the two rows surrounding the requested temperature.

For example, for `VX-200` at `65 °C`, the surrounding rows are:

```text
50 °C → 1.27
70 °C → 1.39
```

### Interpolation

The coefficient is calculated using linear interpolation between the surrounding rows.

For example:

```text
VX-200 at 65 °C → 1.36
```

The result identifies the method as `interpolation`.

### Refusal to Extrapolate

The tool checks the supported temperature range before attempting interpolation.

A temperature below the minimum or above the maximum supported temperature raises a `ValueError`.

This prevents the tool from producing a coefficient outside the engineering evidence provided by the lookup table.

## Interpolation Formula

The tool uses the following linear interpolation equation:

```text
y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)
```

Where:

* `x` = requested operating temperature
* `x1` = lower surrounding temperature
* `x2` = upper surrounding temperature
* `y1` = coefficient at the lower temperature
* `y2` = coefficient at the upper temperature
* `y` = interpolated coefficient

For example, for `VX-100` at `35 °C`:

```text
x  = 35
x1 = 20
x2 = 40
y1 = 0.88
y2 = 0.93

y = 0.88 + ((35 - 20) / (40 - 20)) * (0.93 - 0.88)
  = 0.9175
```

## Refusal Behavior

The tool raises `ValueError` for unsupported inputs.

### Below-range example

```text
VX-100 at 5 °C
```

The requested temperature is below the supported minimum of `20 °C`.

### Above-range example

```text
VX-100 at 110 °C
```

The requested temperature is above the supported maximum of `100 °C`.

### Unknown-family example

```text
VX-999 at 50 °C
```

`VX-999` is not one of the supported valve families.

These cases are refused rather than producing extrapolated or unsupported results.

## Testing

The project uses `pytest` for automated testing.

The test suite covers:

* exact lookup;
* interpolation;
* lower supported boundary;
* upper supported boundary;
* below-range refusal;
* above-range refusal;
* unknown valve family;
* multiple valve families;
* challenge cases;
* interpolation helper calculations.

The current test suite contains 15 tests, all of which pass.

## Running Tests

From the project root, run:

```bash
python -m pytest
```

Expected result:

```text
15 passed
```

## Assumptions

* Temperature inputs are provided in degrees Celsius.
* Lookup-table temperatures are ordered from lowest to highest.
* The supplied lookup-table values are the engineering evidence used by the tool.
* Linear interpolation is appropriate between adjacent supported table points.
* Values outside the documented range must be refused rather than extrapolated.

## Known Limitations

* The tool currently supports only the valve families contained in the assigned lookup table.
* The lookup data is static and must be updated if the engineering source table changes.
* The tool does not perform extrapolation outside the supported temperature ranges.
* Input validation is focused on the assignment's required valve-family and temperature lookup behavior.

## AI Use

AI assistance was used during development to help understand the assignment requirements, organize the lookup and interpolation implementation, develop and review automated tests, and troubleshoot test failures.

Specific AI assistance and development decisions are documented in `AI_LOG.md`.
