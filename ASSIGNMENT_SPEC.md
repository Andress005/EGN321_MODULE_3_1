# Module 3 — Assignment 3.1: Lookup Tool

## Assignment Overview
Rebuild the assigned spreadsheet selection calculation as a readable, testable Python lookup tool.

Your program must:
1. use valve family as the first lookup criterion;
2. use operating temperature as the second criterion;
3. keep lookup table data separate from decision logic;
4. return exact table values for exact matches;
5. use linear interpolation for supported values between rows;
6. identify the supported range for the selected family;
7. explicitly refuse extrapolation below or above the table;
8. reject unsupported valve families;
9. include automated tests proving normal, boundary, interpolation, and refusal behavior;
10. document table sources, supported ranges, assumptions, and limitations.

## Minimum Test Evidence
- 2 exact lookup tests
- 2 interpolation tests
- 1 lower-boundary test
- 1 upper-boundary test
- 1 below-range refusal test
- 1 above-range refusal test
- 1 unsupported-family refusal test

## Git / Documentation
- At least 5 meaningful commits.
- Complete README.
- AI_LOG.md if AI is used.
- Final submission: GitHub repository link.

## Engineering Rule
**Interpolate inside the evidence. Refuse outside it.**
