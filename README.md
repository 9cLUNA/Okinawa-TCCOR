# Python and Tesseract for Image Reading

Using Python with the Tesseract OCR library wrapper to read current TCCOR information from the Kadena Air Force Base weather website. Initially, I wanted to know how well I can train Tesseract to read the image and find variable information.

## Getting Started

This project is done in Python 3 using Tesseract OCR. There is two main scripts. One is called "Live" which is the active script that pulls from the active website. I do not control the website so this script needs to be smart enough to adapt to changes that their website makes.

The non-live script is only using the local folders of test images that were pullled from previous versions of the website.

The variables.csv file contains all those possible outcomes that Tesseract is looking for.

## Built With

Software

* [Python 3](https://www.python.org/) - High-level, general purpose programming language.
* [Tesseract](https://github.com/tesseract-ocr/tesseract) - OCR engine.
* [pytesseract](https://pypi.org/project/pytesseract/) - Python's wrapper for Google's Tesseract-OCR engine.


Website

* [Shogun Weather](https://www.kadena.af.mil/Agencies/Local-Weather/) - Website that contains the current Typhoon condition for Okinawa, Japan.

## Acknowledgments

* All the websites I had to Google...thanks!
* Most notably: https://stackabuse.com/linear-regression-in-python-with-scikit-learn & https://towardsdatascience.com/linear-regression-in-python-9a1f5f000606