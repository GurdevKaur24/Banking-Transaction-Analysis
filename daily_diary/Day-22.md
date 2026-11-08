# Day 22 – Excel Functions

## Topics Covered
- Logical functions: `IF`, nested `IF`, `AND`, `OR`, `IFERROR`
- Conditional functions: `COUNTIF`, `COUNTIFS`, `SUMIF`, `SUMIFS`, `AVERAGEIF`
- Lookup functions: `VLOOKUP`, `XLOOKUP`, `INDEX` + `MATCH`
- Text functions
- Date functions

## Sample Data
| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| **1** | transaction_id | customer_id | amount | merchant_category | fraud_status | date |
| **2** | 500006 | 49108 | 274.13 | travel | Legitimate | 06-05-2023 |
| **3** | 500010 | 39120 | 967.29 | groceries | Legitimate | 15-05-2023 |
| **4** | 500018 | 50180 | 645.61 | travel | Fraud | 24-05-2023 |
| **5** | 500019 | 3885 | 33.22 | fashion | Legitimate | 09-05-2023 |
| ... | ... | ... | ... | ... | ... | ... |

## 1. Logical Functions

### IF
Returns one value if a condition is TRUE and another if it is FALSE.
```
=IF(condition, value_if_true, value_if_false)
```
```
=IF(C2>500, "High", "Low")
```

### Nested IF
An `IF` inside another `IF` for more than two results.
```
=IF(C2>750, "High", IF(C2>250, "Medium", "Low"))
```

### AND / OR
| Function | Returns TRUE when |
|---|---|
| `AND(cond1, cond2)` | **All** conditions are TRUE |
| `OR(cond1, cond2)` | **At least one** condition is TRUE |

```
=IF(AND(C2>500, E2="Fraud"), "Check", "OK")
=IF(OR(D2="travel", D2="electronics"), "Big spend category", "Other")
```

### IFERROR
Shows a custom value instead of an error such as `#N/A` or `#DIV/0!`.
```
=IFERROR(C2/B2, 0)
```

## 2. Conditional (Criteria-Based) Functions

| Function | Purpose | Syntax |
|---|---|---|
| `COUNTIF` | Count cells matching one condition | `=COUNTIF(range, criteria)` |
| `COUNTIFS` | Count cells matching multiple conditions | `=COUNTIFS(range1, criteria1, range2, criteria2)` |
| `SUMIF` | Add values matching one condition | `=SUMIF(range, criteria, sum_range)` |
| `SUMIFS` | Add values matching multiple conditions | `=SUMIFS(sum_range, range1, criteria1, range2, criteria2)` |
| `AVERAGEIF` | Average of values matching a condition | `=AVERAGEIF(range, criteria, average_range)` |

### Examples
```
=COUNTIF(E2:E100, "Fraud")                          → number of fraud transactions
=COUNTIF(C2:C100, ">500")                           → transactions above 500
=COUNTIFS(D2:D100, "travel", E2:E100, "Fraud")      → fraud transactions in travel
=SUMIF(D2:D100, "groceries", C2:C100)               → total amount spent on groceries
=SUMIFS(C2:C100, D2:D100, "fashion", E2:E100, "Legitimate")
=AVERAGEIF(D2:D100, "electronics", C2:C100)         → average electronics amount
```

**Fraud rate (%):**
```
=COUNTIF(E2:E100, "Fraud") / COUNTA(E2:E100) * 100
```

> **Note:** In `SUMIF` the sum range comes **last**, but in `SUMIFS` the sum range comes **first**.

## 3. Lookup Functions
Lookup functions find a value in one table and return related information from another column.

**category_info** (in another sheet, columns H:I)
| | H | I |
|---|---|---|
| **1** | category | risk_level |
| **2** | electronics | Medium |
| **3** | fashion | Low |
| **4** | gaming | Medium |
| **5** | groceries | High |
| **6** | travel | Low |

### VLOOKUP
Searches for a value in the **first column** of a table and returns a value from a column to its right.
```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```
```
=VLOOKUP(D2, $H$2:$I$6, 2, FALSE)
```

| Argument | Meaning |
|---|---|
| `lookup_value` | Value to search for (`D2`) |
| `table_array` | Table to search in (`$H$2:$I$6`) |
| `col_index_num` | Column number to return from (`2` = risk_level) |
| `range_lookup` | `FALSE` = exact match, `TRUE` = approximate match |

**Limitation:** VLOOKUP can only look to the **right** of the first column.

### XLOOKUP
A newer, more flexible lookup that can search **in any direction**.
```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])
```
```
=XLOOKUP(D2, $H$2:$H$6, $I$2:$I$6, "Not found")
```

### INDEX + MATCH
An older but flexible combination that also works in any direction.
```
=INDEX($I$2:$I$6, MATCH(D2, $H$2:$H$6, 0))
```
- `MATCH` finds the **position** of the value
- `INDEX` returns the value at that **position**

### VLOOKUP vs XLOOKUP
| VLOOKUP | XLOOKUP |
|---|---|
| Looks only to the right | Looks left or right |
| Needs a column number | Uses a return range directly |
| Approximate match by default | Exact match by default |
| Shows `#N/A` if not found | Can show a custom "not found" message |
| Works in all Excel versions | Excel 2021 / Microsoft 365 and later |

## 4. Text Functions
| Function | Purpose | Example | Result |
|---|---|---|---|
| `UPPER()` | Uppercase | `=UPPER("travel")` | `TRAVEL` |
| `LOWER()` | Lowercase | `=LOWER("FRAUD")` | `fraud` |
| `PROPER()` | First letter of each word capital | `=PROPER("data analysis")` | `Data Analysis` |
| `LEN()` | Number of characters | `=LEN("Excel")` | `5` |
| `TRIM()` | Removes extra spaces | `=TRIM("  hello  ")` | `hello` |
| `LEFT()` | Characters from the left | `=LEFT("Banking", 4)` | `Bank` |
| `RIGHT()` | Characters from the right | `=RIGHT("2023-05", 2)` | `05` |
| `MID()` | Characters from the middle | `=MID("Analytics", 3, 4)` | `alyt` |
| `CONCAT()` / `&` | Join text | `="ID-" & A2` | `ID-500006` |
| `TEXTJOIN()` | Join with a separator | `=TEXTJOIN(", ", TRUE, D2:D4)` | `travel, groceries, travel` |
| `SUBSTITUTE()` | Replace text | `=SUBSTITUTE("fraud_case", "_", " ")` | `fraud case` |

## 5. Date Functions
| Function | Purpose | Example |
|---|---|---|
| `TODAY()` | Today's date | `=TODAY()` |
| `NOW()` | Current date and time | `=NOW()` |
| `DAY()` | Day number from a date | `=DAY(F2)` → `6` |
| `MONTH()` | Month number | `=MONTH(F2)` → `5` |
| `YEAR()` | Year | `=YEAR(F2)` → `2023` |
| `TEXT()` | Format a date as text | `=TEXT(F2, "mmmm")` → `May` |
| `TEXT()` | Weekday name | `=TEXT(F2, "dddd")` → `Saturday` |
| `WEEKDAY()` | Weekday number (1 = Sunday) | `=WEEKDAY(F2)` |
| `DATEDIF()` | Difference between two dates | `=DATEDIF(F2, TODAY(), "d")` |

> These are similar to `dt.month_name()` and `dt.day_name()` in Pandas, which I used to create the `month_name` and `day_name` columns in my project.

## Common Errors
| Error | Meaning |
|---|---|
| `#N/A` | Value not found (common in lookups) |
| `#DIV/0!` | Division by zero |
| `#VALUE!` | Wrong type of data (e.g. text in a math formula) |
| `#REF!` | Formula refers to a deleted cell |
| `#NAME?` | Function name spelled wrong |


## Key Takeaway
Excel functions make analysis fast without coding. `IF`, `AND` and `OR` add logic, `COUNTIFS` and `SUMIFS` summarise data by conditions (like `groupby` in Pandas), and `VLOOKUP`/`XLOOKUP` combine data from different tables (like a SQL JOIN). Text and date functions help clean and prepare data for analysis.
