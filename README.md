# IMEI Generator for Moto XT1750 and Similar Models

This Python script generates IMEI numbers in both decimal and hexadecimal formats specifically for the NVRAM of Motorola Moto XT1750 devices and similar models. The script is designed to assist in updating the IMEI using the Maumeta program, by providing the necessary values based on the given memory addresses.

## Features

- **Device Compatibility:** Supports Motorola Moto XT1750 and similar models.
- **Slot Selection:** Generate IMEI for either the primary or secondary slot (IMEI 1 or 2).
- **Format Options:** Outputs IMEI values in both decimal and hexadecimal formats.
- **Memory Address Mapping:** Generates the correct IMEI values depending on the specified memory addresses.

## How It Works

1. **IMEI Validation:** The script first ensures that the provided IMEI is a valid 15-digit numeric string and identifies whether it is intended for IMEI 1 or IMEI 2.
2. **Slot Identification:** Based on the selected slot, the script determines the appropriate memory address range for the IMEI values.
3. **Randomized Value Generation:** For each digit of the IMEI, the script maps it to a predefined range of values and selects a random number from this range.
4. **Formatted Output:** The script produces the IMEI values formatted for use with the Maumeta program, including both decimal and hexadecimal representations.

## Usage

### Prerequisites

- Python 3.x

### Running the Script

```bash
python imei_generator.py
