"""
Validated lookup / interpolation tool.

Required behavior:
1. Validate valve family.
2. Identify that family's supported temperature range.
3. Refuse values outside the range.
4. Return exact table value when temperature matches a row.
5. Otherwise locate surrounding rows and interpolate.
6. Return useful details about how the result was produced.
"""
from src.interpolation import linear_interpolate
from src.lookup_tables import LOOKUP_TABLES


def select_coefficient(valve_family, temperature_c):
    """Select a valve coefficient using exact lookup or interpolation."""

    # Validate valve family
    if valve_family not in LOOKUP_TABLES:
        raise ValueError(
            f"Unsupported valve_family: {valve_family}"
        )

    # Get the selected family's table
    table = LOOKUP_TABLES[valve_family]

    # Determine supported temperature range
    minimum_temp = table[0][0]
    maximum_temp = table[-1][0]

    # Refuse extrapolation below the supported range
    if temperature_c < minimum_temp:
        raise ValueError(
            f"temperature_c {temperature_c} is below "
            f"the supported minimum {minimum_temp}"
        )

    # Refuse extrapolation above the supported range
    if temperature_c > maximum_temp:
        raise ValueError(
            f"temperature_c {temperature_c} exceeds "
            f"the supported maximum {maximum_temp}"
        )

    # Check for an exact table match
    for temperature, coefficient in table:
        if temperature_c == temperature:
            return {
                "valve_family": valve_family,
                "temperature_c": temperature_c,
                "coefficient": coefficient,
                "method": "exact",
                "lower_point": (temperature, coefficient),
                "upper_point": (temperature, coefficient),
                "supported_range": (minimum_temp, maximum_temp),
            }

    # Find the surrounding rows for interpolation
    for i in range(len(table) - 1):
        lower_temp, lower_coefficient = table[i]
        upper_temp, upper_coefficient = table[i + 1]

        if lower_temp < temperature_c < upper_temp:
            coefficient = linear_interpolate(
                x=temperature_c,
                x1=lower_temp,
                y1=lower_coefficient,
                x2=upper_temp,
                y2=upper_coefficient,
            )

            return {
                "valve_family": valve_family,
                "temperature_c": temperature_c,
                "coefficient": coefficient,
                "method": "interpolation",
                "lower_point": (lower_temp, lower_coefficient),
                "upper_point": (upper_temp, upper_coefficient),
                "supported_range": (minimum_temp, maximum_temp),
            }

    # This should only be reached if the table is malformed.
    raise ValueError(
        f"Could not determine lookup result for "
        f"{valve_family} at {temperature_c}°C"
    )