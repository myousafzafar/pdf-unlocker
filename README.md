# 🔓 pdf-unlocker

**pdf-unlocker** is a simple Python script that brute-forces 4-digit (or longer) password-protected PDF files using the `pikepdf` library. It tries numeric combinations from 0000 to 9999, stops when the correct password is found, and saves an unlocked copy as `unlocked.pdf`. Designed for educational and ethical use only, this tool is ideal for recovering access to your own secured PDFs. Just install `pikepdf`, place your locked PDF as `file.pdf` in the same directory as script file, and run the script — clean, readable, and easy to extend to less or more digits if needed.

---

## ⚡ Features

- Brute-force passwords on locked PDFs
- Fully adjustable password digit length (just change a single line in the script)
- Stops instantly when the correct password is found
- Saves an unlocked copy of the PDF
- Simple, readable Python code
- For ethical and educational use only!!!

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have **Python 3** and `pip` installed.

Install required packages in Ubuntu:

```bash
sudo apt install python3-pip libqpdf-dev
pip install pikepdf
```

You can either install python3 using the following command *OR* simply install the python extension in Visual Studio Code (VS Code) instead (if you use that) and you can skip the following command:
```bash
sudo apt install python3
``` 

---

## 📂 Usage

1. Place your locked PDF in the project folder and rename it to `file.pdf`  
   (or change the filename inside `unlock-pdf.py`).

2. Run the script:

```bash
python unlock-pdf.py
```

Once unlocked, the script will:
- Print the password used in the terminal
- Save the unlocked version as `unlocked.pdf` in the same directory

---

## 🔐 Disclaimer

This tool is intended **only for ethical and educational purposes**.  
Do **not** use it to access PDFs without permission.  
Breaking encryption without authorization may be **illegal** in your jurisdiction.

---

## 📁 File Structure

```
pdf-unlocker/
│
├── unlock-pdf.py       # Main script
├── file.pdf            # Your locked PDF file (not included)
├── unlocked.pdf        # Output (if unlocked)
└── README.md
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Feel free to open an issue or submit a PR.

---

## ⭐️ Support

If you found this helpful, consider starring ⭐ this repo or sharing it!
