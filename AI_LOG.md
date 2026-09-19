# AI Usage Log — Module 3 Assignment 3.1

## Interaction

* **Tool:** ChatGPT
* **Date:** September 2026
* **Prompt:** Asked for help implementing the valve lookup and interpolation tool according to the assignment requirements, including exact lookup, interpolation, supported-range enforcement, refusal of extrapolation, and automated tests.
* **AI output:** Provided guidance for structuring the lookup tables, implementing linear interpolation, implementing the valve selection logic, and creating pytest tests.
* **What I used:** I used the suggested Python structure for the lookup table, interpolation helper, selection function, and automated tests.
* **What I changed:** I entered the code into the provided starter files and tested it with pytest. I also corrected one expected test value after pytest showed that the expected value for VX-100 at 35 °C was incorrect.
* **Why I changed it:** The calculated value from the implemented linear interpolation was 0.9175, while the test initially expected 0.945. I recalculated the interpolation using the table values of 0.88 at 20 °C and 0.93 at 40 °C and confirmed that 0.9175 was the correct result.
* **How I verified it:** I ran the automated test suite using `python -m pytest`. The final test suite completed successfully with 15 passed tests.
* **Which test proves the behavior:** The selection tests verify exact lookup, interpolation, lower and upper boundaries, below-range refusal, above-range refusal, unknown-family refusal, and additional challenge cases. The interpolation tests also verify the standalone interpolation function.

## Required Reflection

**Did the AI attempt to extrapolate outside the table? If so, how did you correct it?**

No. The implementation was designed to check the supported temperature range before interpolation. Temperatures below the minimum or above the maximum are rejected with `ValueError`, so the tool does not extrapolate outside the engineering evidence provided by the lookup table.

The core rule used in the implementation is:

**Interpolate inside the evidence. Refuse outside it.**
