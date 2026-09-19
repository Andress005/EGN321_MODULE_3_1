# Assignment 3.1 Final Checklist

## Analysis
- [ ] I traced the legacy lookup logic before coding.
- [ ] I can identify both lookup criteria.
- [ ] I know which table applies to each valve family.

## Data Structure
- [ ] Lookup data is readable and separate from decision logic.
- [ ] I did not recreate the spreadsheet as deeply nested if-statements.
- [ ] Table ranges are visible and documented.

## Lookup / Interpolation
- [ ] Exact table matches return the listed value.
- [ ] Between-row values use linear interpolation.
- [ ] I can explain x, x1, x2, y1, and y2.
- [ ] Minimum and maximum table rows are accepted.

## Refusal
- [ ] Below-range values raise ValueError.
- [ ] Above-range values raise ValueError.
- [ ] Unknown valve families raise ValueError.
- [ ] The tool does not extrapolate.

## Testing
- [ ] At least 2 exact lookup tests.
- [ ] At least 2 interpolation tests.
- [ ] Lower and upper boundary tests.
- [ ] Below- and above-range refusal tests.
- [ ] Unknown-family refusal test.
- [ ] All tests pass.

## Documentation / GitHub
- [ ] README lists supported families and ranges.
- [ ] README explains interpolation.
- [ ] README explains refusal behavior.
- [ ] AI use is documented if applicable.
- [ ] At least 5 meaningful commits.
- [ ] I can explain every function and test.
- [ ] Final submission is the GitHub repository link.
