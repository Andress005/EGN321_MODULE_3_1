# Assignment 3.1 Test Plan

| Test Name | Category | Family | Temperature | Expected Result | Evidence Source | Why It Matters |
|---|---|---|---:|---|---|---|
| | Exact lookup | | | | Reference Cases | |
| | Interpolation | | | | Reference Cases | |
| | Lower boundary | | | | Supported Ranges | |
| | Upper boundary | | | | Supported Ranges | |
| | Below range | | | ValueError | Supported Ranges | |
| | Above range | | | ValueError | Supported Ranges | |
| | Unknown family | | | ValueError | Engineering Tables | |

Minimum required evidence:
- 2 exact lookup tests
- 2 interpolation tests
- 1 lower-boundary test
- 1 upper-boundary test
- 1 below-range refusal test
- 1 above-range refusal test
- 1 unknown-family refusal test
