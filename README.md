# JSON-equipment-inventory-to-CSV
This converts a JSON file into the CSV file which is easier to study

Laboratories often receive data from a purchasing or inventory system in a format designed
for programs rather than for spreadsheets. JSON (JavaScript Object Notation) is a text format
that represents a record by putting field names and values inside { and }. A collection of
records is commonly put inside [ and ]. JSON is useful because the same structured data can
be sent between different programs and stored as an ordinary text file.
For example, one equipment record can be written as:
{"id": "E17", "room": "Lab-2", "kind": "oscilloscope", "working": true}
Our Programme will convert a small, specified subset of JSON to CSV (comma-separated
values), which is convenient to open as a table in a spreadsheet.
