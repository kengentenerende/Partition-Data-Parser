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
```

## Script Breakdown
- *parse_partition_data(partition_hex):* Main function that takes a 32-character hex string and parses it into meaningful partition data.
- *hex_to_binary(hex_string):* Converts a hex string to its binary equivalent.
- *hex_to_little_endian(hex_string):* Converts a hex string to little-endian format.
- *binary_to_decimal(binary_string):* Converts a binary string to its decimal equivalent.
- *get_partition_type_label(partition_type_hex):* Matches the partition type hex value with a descriptive label.
- *calculate_partition_size(num_sectors):* Calculates partition size in bytes, KB, and MB.

## Notes
Ensure that the input hex string is exactly 32 characters long.
The partition type identification is based on standard partition type codes.
