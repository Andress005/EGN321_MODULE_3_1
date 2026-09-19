# Lookup Trace

Use this before coding.

| Step | Spreadsheet Logic                                                             | Criterion / Value                  | Table or Range Used                  | Python Replacement                                                                         |
| ---- | ----------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------ |
| 1    | Select the valve family                                                       | Valve Family                       | VX-100, VX-200, VX-300               | `LOOKUP_TABLES[valve_family]`                                                              |
| 2    | Check the operating temperature against the selected family's supported range | Operating Temperature (°C)         | Family-specific minimum and maximum  | Check minimum and maximum temperature and raise `ValueError` outside the range             |
| 3    | Find the matching or surrounding temperature rows                             | Temperature                        | Selected valve family's lookup table | Return exact row when temperature matches; otherwise find lower and upper surrounding rows |
| 4    | Calculate the coefficient                                                     | Temperature and coefficient values | Two surrounding table rows           | Return exact coefficient or use `linear_interpolate()` between the two rows                |

## Questions

1. **What is the first lookup criterion?**
   Valve Family.

2. **What is the second lookup criterion?**
   Operating Temperature in degrees Celsius.

3. **Which table applies?**
   The lookup table corresponding to the selected valve family: `VX-100`, `VX-200`, or `VX-300`.

4. **What happens on an exact row?**
   The coefficient from the matching table row is returned directly and the result method is reported as `exact`.

5. **What happens between rows?**
   The two surrounding rows are identified and linear interpolation is used to calculate the coefficient.

6. **What happens outside the supported range?**
   The tool refuses the lookup by raising `ValueError`. It does not extrapolate outside the provided engineering evidence.
