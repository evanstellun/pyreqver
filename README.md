# PyReqVer - Python Requirements Version Checker

PyReqVer is a command-line tool that helps you find Python versions that support all libraries in your requirements.txt file. It analyzes each package's compatibility information from PyPI and determines the intersection of Python versions that support all your dependencies.

## Features

- Analyzes packages in requirements.txt files
- Fetches Python version compatibility data from PyPI
- Identifies common Python versions supported by all packages
- Handles complex version specifiers and classifiers
- Provides clear output showing compatible Python versions
- Uses concurrent requests for efficient package information retrieval

## Installation

### From Source

1. Clone or download this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Using pip (if published)

```bash
pip install pyreqver
```

## Usage

### Basic Usage

```bash
python main.py path/to/your/requirements.txt
```

Example:
```bash
python main.py requirements.txt
```

### Command Line Arguments

- `requirements`: Path to the requirements.txt file (required)

## Output Example

```
requests available on: ['3.13', '3.12', '3.11', '3.10', '3.9', '3.8', '3.7', '3.6', '3.5', '2.7']
scikit-learn available on: ['3.13', '3.12', '3.11', '3.10', '3.9', '3.8', '3.7', '3.6', '3.5']
pandas available on: ['3.13', '3.12', '3.11', '3.10', '3.9', '3.8', '3.7', '3.6', '3.5', '2.7']
matplotlib available on: ['3.13', '3.12', '3.11', '3.10', '3.9', '3.8', '3.7', '3.6', '3.5']
numpy available on: ['3.13', '3.12', '3.11', '3.10', '3.9', '3.8', '3.7', '3.6', '3.5', '2.7']
--------------------------------------------------------------------------------
Supported Python versions for all libraries: ['3.13', '3.12', '3.11', '3.10', '3.9', '3.8', '3.7', '3.6', '3.5']
```

## How It Works

1. **Parsing Requirements**: The tool reads and parses the requirements.txt file to extract package names.
2. **Fetching Package Information**: For each package, it queries PyPI's JSON API to get metadata about available versions and their Python version compatibility.
3. **Analyzing Compatibility**: It examines two sources of compatibility information:
   - The `requires_python` field in package metadata
   - Package classifiers that indicate Python version support
4. **Finding Common Versions**: It calculates the intersection of Python versions that support all packages in your requirements.
5. **Displaying Results**: The tool shows which Python versions each package supports and highlights the versions that are compatible with all packages.

## Technical Details

- Uses the `packaging` library to handle version specifiers
- Implements caching to avoid redundant API calls
- Uses concurrent requests for efficient package information retrieval
- Handles various edge cases like missing package information or incomplete metadata

## Dependencies

- `requests>=2.25.0`: For HTTP requests to PyPI
- `packaging>=21.0`: For parsing version specifiers and handling version comparisons

## Limitations

1. Requires an internet connection to fetch package information from PyPI
2. Some packages may not have explicit Python version support information
3. Results are based on package metadata and may not reflect actual runtime compatibility
4. The tool checks for declared compatibility, not actual functionality across Python versions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Notes

1. This tool requires an internet connection to fetch package information from PyPI
2. Some packages may not have explicit Python version support information
3. Results are for reference only, please ensure to test your code for compatibility on the selected Python version
4. The tool may not work correctly with packages that use non-standard versioning schemes