# Image Processing

This project offers a simple script for extracting text from images and translating it using OpenCV, Tesseract OCR, and Argos Translate.

## Installation and Setup

### 1. Clone the project

    git clone https://github.com/singhkailash9/image-processing.git


### 2. Install Dependencies:
Run the following command to install the required Python packages:

    pip install -r requirements.txt


### 3. Install Tesseract-OCR
Follow the installation guide for Tesseract-OCR [here](https://tesseract-ocr.github.io/tessdoc/Installation.html). 

During or after installation, you can optionally download additional language scripts and packs from the Tesseract GitHub [tessdata repository](https://github.com/tesseract-ocr/tessdata). 

Choose any language pack you need for text extraction.

### 4. Download Translation Packages
Use the provided Python script `translation_package_download.py` to download translation packages from Argos Translate. 

Adjust the `from_code` and `to_code` variables in the script according to your requirements. 

Find the correct language codes [here](https://www.argosopentech.com/argospm/index/).

### 5. Prepare Your Image
Place the image you wish to process in the `Data` directory. 

In the `text_extract.py` file, update the image file name and specify the correct language code for the text you're extracting. 

Language codes can be found in the Tesseract [tessdata repository](https://github.com/tesseract-ocr/tessdata).

To run it, use the following command:

    python text_extract.py

### 6. Translate Extracted Text
To translate the extracted text, adjust the `TRANSLATE_FROM` and `TRANSLATE_TO` variables in the translate.py file as needed. 

This script reads the extracted text from `data.txt`, translates it, and saves the output to `translated_data.txt` within the Text directory.

To run it, use the following command:

    python translate.py

### 7. Running the Scripts
To process a new image, simply replace the image file in the `Data` directory and adjust the script parameters as needed. 

If you decide to translate to a different language in the future, remember to modify the translation language variables accordingly.

### 8. Summarize the extracted/translated text
After extracting and optionally translating text, you can further process the text to get a condensed summary. To do this, run the `summarize.py` script. Make sure to update the `FILE_NAME` constant within the script to match the name of the file you wish to summarize. If the file resides in a specific directory, adjust the `FILE` path accordingly.

This step requires the summarization model, which will be automatically downloaded upon the first execution of `summarize.py`. Ensure you have an internet connection for this initial download. Subsequent executions will use the cached model, thus not requiring an internet connection. The summarized content will be saved in the same text directory as the extracted and translated data files.

## Additional Notes

- This project is intended for educational purposes and serves as a basic introduction to image processing, text extraction, and language translation using Python.
- Remember to check for updates to dependencies and language packs to utilise the latest model.
- The project is not considered a final product; improvements and updates are planned for the future. Any feeback and contributions are welcomed.
