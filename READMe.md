# Partition Data Parser

This Python script allows you to parse a 32-character hex string representing partition data. It extracts and calculates details such as CHS values, partition type, LBA, and the size of the partition in bytes, kilobytes, and megabytes.

## Features

- **CHS Calculation**: Extracts Cylinder, Head, and Sector values for both starting and ending CHS.
- **Partition Type Identification**: Identifies the partition type based on the provided hex value and matches it with its label.
- **LBA and Sector Analysis**: Calculates the starting LBA and the total number of sectors.
- **Size Calculation**: Determines the partition size in bytes, kilobytes, and megabytes.

## Usage

To use the script, simply input a 32-character hex string representing the partition data when prompted.

### Example

```bash
python partition_parser.py