# PDF Keep First Page

This Python script opens all PDF files in a directory, keeps the first page, removes the others, and saves the result in a new directory.

## How to Use

### Clone the Repository
```bash
git clone git@github.com:lichti/pdf-keep-first-page.git
cd pdf-keep-first-page
```

### Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create the Input Directory
```bash
mkdir input
```

### Run the Script
```bash
python3 pdf_keep_first_page.py
```

### Check the Output Files
The processed files will be saved in the `output` directory.
```

Ensure that the `requirements.txt` file is present in the repository and contains the necessary dependencies, such as `PyPDF2`. Here is an example of what the `requirements.txt` could look like:

```
PyPDF2
```
