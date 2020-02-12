# Python and Tesseract for Image Reading

Using Python with the Tesseract OCR library wrapper to read current TCCOR information from the Kadena Air Force Base weather website. Initially, I wanted to know how well I can train Tesseract to read the image and find variable information.

## Getting Started

This project is done in Python 3 using Tesseract OCR. I have two scripts; the main script is TCCOR.py and the local testing script is test_TCCOR.py. I used the local testing script just to test and perfect my tesseract attributes without pulling live from the website I was scraping.

The script locates the TCCOR image, downloads it and adjust it to best allow tesseract to locate the target text. The variables.csv file is all possible combinations that tesseract might find in the image. The absolute variable file contains what those outcomes should translate to.

## Installed Packages

Here is a list of the packages imported

```
astroid==2.2.5
beautifulsoup4==4.7.1
bs4==0.0.1
certifi==2019.6.16
chardet==3.0.4
idna==2.8
isort==4.3.21
lazy-object-proxy==1.4.1
mccabe==0.6.1
Pillow==7.0.0
pylint==2.3.1
pytesseract==0.2.7
regex==2019.6.8
requests==2.22.0
six==1.12.0
soupsieve==1.9.2
typed-ast==1.4.0
urllib3==1.25.3
wrapt==1.11.2
```

## Running the script


```
python3 tccor.py
```

## Built With

Software

* [Python 3](https://www.python.org/) - High-level, general purpose programming language.
* [Tesseract](https://github.com/tesseract-ocr/tesseract) - Optical Character Recognition engine; sponsored by Google.
* [pytesseract](https://pypi.org/project/pytesseract/) - Python's wrapper for Google's Tesseract-OCR engine.
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Python package for parsing HTML and XML websites. Useful to extract data and other web scraping needs.

Website

* [Shogun Weather](https://www.kadena.af.mil/Agencies/Local-Weather/) - Website that contains the current Typhoon condition for Okinawa, Japan.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.