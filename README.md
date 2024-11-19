# img-generator

## Overview

This tool generates images with either random or specified colors, at a specified size, and saves them to a specified directory. It's a versatile script that allows precise customization of output through flexible command-line arguments.

## Features

- Generate images with **random colors** or a **specified hex color code**.
- Specify the **size** (width and height) of the generated images.
- Optionally generate multiple random images at once.
- Save images to a **specified output directory**, or default to the current directory.
- User-friendly help messages for guidance.

## Requirements

- Python 3.x
- `Pillow` library for image processing

Install dependencies with:

```bash
pip install pillow
```

## Usage

Run the script using the following command structure:

```
python run.py -s <width> <height> [-n <number>] [-c <color>] [-d <output_directory>]
```

### Options

| Option     | Short | Description                                                  | Default                 |
| ---------- | ----- | ------------------------------------------------------------ | ----------------------- |
| `--size`   | `-s`  | **(Required)** Specify the size of the image as width and height (e.g., `-s 800 600`). | N/A                     |
| `--number` | `-n`  | Number of random images to generate (ignored if `--color` is specified). | `1`                     |
| `--color`  | `-c`  | Specify the color in 6-character hex format (e.g., `-c ffffff`). | Randomly generated      |
| `--dir`    | `-d`  | Specify the output directory where images will be saved.     | Current directory (`.`) |
| `--help`   | `-h`  | Show detailed help and usage instructions.                   | N/A                     |

## Examples

### 1. Generate a single random color image

```bash
python run.py -s 800 600
```

**Output:**

- A single image of size `800x600` with a random color saved in the current directory.

### 2. Generate multiple random color images

```bash
python run.py -s 800 600 -n 3
```

**Output:**

- Three images of size `800x600` with random colors saved in the current directory.

### 3. Generate an image with a specified color

```bash
python run.py -s 750 300 -c c6e3d9
```

**Output:**

- A single image of size `750x300` with the color `c6e3d9` saved in the current directory.

### 4. Save images to a specified directory

```bash
python run.py -s 1024 768 -n 5 -d ./output
```

**Output:**

- Five images of size `1024x768` with random colors saved in the `./output` directory.

### 5. Generate an image with a specified color and a specified size to a specific directory

```bash
python run.py -s 600 400 -c ffffff -d ./images
```

**Output:**

- A single image of size `600x400` with the color `ffffff` saved in the `./images` directory.

## Error Handling

1. **Invalid color format**: If the provided color is not a valid 6-character hex code:

    ```
    Error: Invalid color format. Please provide a valid 6-character hex color (e.g., ffffff).
    ```

2. **Invalid size or count**: If the provided size or count is missing or invalid:

    ```
    usage: run.py [-h] [-c COLOR] -s WIDTH HEIGHT [-n NUMBER] [-d DIR]
    Error: Missing required arguments or invalid values.
    ```

3. **Output directory creation**: If the specified output directory does not exist, it will be created automatically.

## File Naming Convention

Generated images follow the naming pattern:

```
<YYYYMMDD>_<COLOR_HEX>_<WIDTH>x<HEIGHT>.png
```

For example:

```
20241119_C6E3D9_800x600.png
```

## Output Directory

By default, images are saved in the current directory. To specify a custom output directory, use the `-d/--dir` option.

## License

This tool is open-source and available under the MIT License.

## Author

Created by [Your Name]. Feel free to contribute or suggest improvements!