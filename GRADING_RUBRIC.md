# Assignment 3.1 Grading Rubric — 100 Points

| Criterion | Points | Full-Credit Evidence |
|---|---:|---|
| Spreadsheet lookup analysis | 10 | Correctly identifies the two lookup criteria, table source, and legacy logic. |
| Readable table structure | 15 | Data is separated from logic and easy to inspect. |
| Exact lookup behavior | 10 | Exact table rows return the correct listed coefficient. |
| Linear interpolation | 20 | Correct surrounding rows and correct interpolation formula/results. |
| Range validation / no extrapolation | 15 | Explicitly rejects below- and above-range requests. |
| Unsupported-family validation | 5 | Unknown family is rejected with a useful error. |
| Automated tests | 15 | Required exact, interpolation, boundary, and refusal tests pass. |
| README / assumptions / limits | 5 | Supported ranges, formula, source data, and limits are documented. |
| Git history / AI documentation | 5 | At least 5 meaningful commits; AI use documented when applicable. |
| **Total** | **100** | |

## Important Grading Note
A tool that returns a number outside the documented table range does not meet the assignment requirement, even if the extrapolation math is internally correct.
