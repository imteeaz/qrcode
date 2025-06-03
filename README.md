# QR Code Generator and Reader

This project provides two Python scripts for working with QR codes:
- `generate.py`: Generates a QR code from specified data and saves it as an image file.
- `read.py`: Reads a QR code from an image file and decodes the data it contains.

## Features

- **Generate QR Codes**: Create QR codes from text data (e.g., URLs, messages).
- **Read QR Codes**: Decode QR codes from image files (`.png` format).
- **Customizable**: Easily modify the data to be encoded in `generate.py` and the image path in `read.py`.

## Dependencies

To run these scripts, you'll need to install the following Python libraries:

- `qrcode`: For generating QR codes.
  ```bash
  pip install qrcode[pil]
  ```
- `opencv-python`: For image processing tasks, used by the QR code reader.
  ```bash
  pip install opencv-python
  ```
- `pyzbar`: For decoding QR codes.
  ```bash
  pip install pyzbar
  ```

You can install all dependencies at once using pip:
```bash
pip install qrcode[pil] opencv-python pyzbar
```

## Usage

### 1. Generating a QR Code

The `generate.py` script creates a QR code image named `qrcode.png` in the project directory.

**To run the script:**
```bash
python generate.py
```

**Customization:**
- To change the data encoded in the QR code, modify the `data` variable in `generate.py`:
  ```python
  data = "Your custom data here"
  ```
- You can also adjust QR code parameters like version, error correction, box size, and border within the `qrcode.QRCode()` instantiation in `generate.py`.

### 2. Reading a QR Code

The `read.py` script decodes the QR code from the `qrcode.png` image (or any other specified image) and prints the contained data to the console.

**To run the script (after generating `qrcode.png`):**
```bash
python read.py
```

**Customization:**
- To read a different QR code image, change the `image_path` variable in `read.py`:
  ```python
  image_path = 'path/to/your/qrcode_image.png'
  ```

## Example Workflow

1.  **Modify `generate.py` (Optional):**
    Open `generate.py` and set the `data` variable to your desired URL or text.
    ```python
    data = "https://www.example.com"
    ```
2.  **Run `generate.py`:**
    ```bash
    python generate.py
    ```
    This will create/overwrite `qrcode.png`.
3.  **Run `read.py`:**
    ```bash
    python read.py
    ```
    The script will output the data read from `qrcode.png`. For example:
    ```
    Type: QRCODE
    Data: https://www.example.com
    ```
