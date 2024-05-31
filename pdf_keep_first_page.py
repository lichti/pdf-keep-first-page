import os
from PyPDF2 import PdfReader, PdfWriter

def keep_first_page(src_dir, dest_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        if filename.endswith(".pdf"):
            # Full path of the source PDF file
            src_file = os.path.join(src_dir, filename)

            # Read the PDF file
            with open(src_file, 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                writer = PdfWriter()

                # Check if the PDF has at least one page
                if len(reader.pages) > 0:
                    # Add the first page to the new PDF file
                    writer.add_page(reader.pages[0])

                    # Full path of the destination PDF file
                    dest_file = os.path.join(dest_dir, filename)

                    # Write the new PDF file with only the first page
                    with open(dest_file, 'wb') as new_pdf_file:
                        writer.write(new_pdf_file)

            print(f'Processed: {filename}')

# Define the source and destination directories in the same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
source_directory = os.path.join(script_dir, 'input')
destination_directory = os.path.join(script_dir, 'output')

# Call the function to process the files
keep_first_page(source_directory, destination_directory)
