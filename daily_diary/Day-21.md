# Day 21 – Excel Basics

## Topics Covered
- Introduction to Microsoft Excel
- Excel interface
- Data entry and cell referencing
- Formatting data
- Sorting and filtering
- Basic formulas and functions

## Introduction to Excel
**Microsoft Excel** is a spreadsheet application used to **store, organise, calculate and analyse data** in rows and columns.
It is one of the most widely used tools in data analysis for quick calculations, reports, pivot tables and charts.

## Excel Interface
| Term | Meaning |
|---|---|
| **Workbook** | The whole Excel file (`.xlsx`) |
| **Worksheet (Sheet)** | A single page inside a workbook; one workbook can have many sheets |
| **Row** | Horizontal line of cells, numbered 1, 2, 3, ... |
| **Column** | Vertical line of cells, labelled A, B, C, ... |
| **Cell** | The box where a row and column meet, e.g. `B3` |
| **Range** | A group of cells, e.g. `A1:A10` |
| **Ribbon** | Menu bar at the top with tabs: Home, Insert, Formulas, Data, View |
| **Name Box** | Shows the address of the selected cell |
| **Formula Bar** | Shows and edits the content or formula of the selected cell |

## Data Entry
- Click a cell and type a value, then press **Enter** (move down) or **Tab** (move right).
- **AutoFill:** drag the small square at the bottom-right of a cell (fill handle) to copy a value or continue a series (1, 2, 3 or Jan, Feb, Mar).
- **Flash Fill (`Ctrl + E`):** fills data automatically by recognising a pattern, e.g. extracting first names from full names.

## Cell Referencing
| Type | Example | Meaning |
|---|---|---|
| **Relative** | `A1` | Changes when the formula is copied to another cell |
| **Absolute** | `$A$1` | Stays fixed when copied |
| **Mixed** | `$A1` or `A$1` | Only the column or only the row is fixed |

> Press **F4** while editing a formula to switch between reference types.

Example: to calculate each item's share of a total in cell `B10`:
```
=B2/$B$10
```
When copied down, `B2` changes to `B3`, `B4`, ..., but `$B$10` stays the same.

## Formatting Data
| Formatting | Purpose |
|---|---|
| **Number format** | Show values as Number, Currency, Percentage, Date, etc. |
| **Font, bold, colour** | Highlight headings and important values |
| **Borders and fill colour** | Make tables clear and readable |
| **Alignment / Wrap Text** | Arrange text inside cells |
| **Merge & Center** | Combine cells for a title |
| **Format as Table (`Ctrl + T`)** | Converts data into an Excel Table with automatic filters and styling |
| **Freeze Panes** | Keeps header row visible while scrolling (View → Freeze Panes) |

## Sorting and Filtering

### Sorting
Arranges data in order.
- **Data → Sort A to Z / Z to A** for a single column
- **Data → Sort** for sorting by multiple columns (e.g. by category, then by amount)

### Filtering
Shows only the rows that match a condition.
- **Data → Filter** (or `Ctrl + Shift + L`) adds drop-down arrows to headers
- Filter by values, text (contains, begins with) or numbers (greater than, top 10)

Example: filter the `fraud_status` column to show only **Fraud** transactions.

## Basic Formulas and Functions
Every formula in Excel starts with an **equals sign `=`**.

### Arithmetic Formulas
| Operator | Example | Meaning |
|---|---|---|
| `+` | `=A1+B1` | Addition |
| `-` | `=A1-B1` | Subtraction |
| `*` | `=A1*B1` | Multiplication |
| `/` | `=A1/B1` | Division |
| `^` | `=A1^2` | Power |

### Basic Functions
| Function | Purpose | Example |
|---|---|---|
| `SUM()` | Total of values | `=SUM(D2:D100)` |
| `AVERAGE()` | Average of values | `=AVERAGE(D2:D100)` |
| `COUNT()` | Counts cells with numbers | `=COUNT(D2:D100)` |
| `COUNTA()` | Counts non-empty cells | `=COUNTA(A2:A100)` |
| `MIN()` | Smallest value | `=MIN(D2:D100)` |
| `MAX()` | Largest value | `=MAX(D2:D100)` |
| `ROUND()` | Rounds a number | `=ROUND(D2, 2)` |

> **AutoSum (`Alt + =`)** quickly adds a `SUM` formula for the selected range.

## Useful Shortcuts
| Shortcut | Action |
|---|---|
| `Ctrl + C` / `Ctrl + V` | Copy / Paste |
| `Ctrl + Z` / `Ctrl + Y` | Undo / Redo |
| `Ctrl + Arrow key` | Jump to the end of data in that direction |
| `Ctrl + Shift + Arrow key` | Select data to the end |
| `Ctrl + T` | Format as Table |
| `Ctrl + Shift + L` | Turn filters on/off |
| `Alt + =` | AutoSum |
| `F2` | Edit the selected cell |
| `F4` | Switch reference type ($) |


## Key Takeaway
Excel organises data in workbooks, sheets, rows, columns and cells. Formatting, sorting and filtering make data easy to read and explore, and basic formulas like `SUM`, `AVERAGE`, `COUNT`, `MIN` and `MAX` give quick calculations. Understanding relative and absolute references is important for copying formulas correctly.
