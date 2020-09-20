# Python and Tesseract for Image Reading

Using Python with the Tesseract OCR library wrapper to read current TCCOR information from the Kadena Air Force Base weather website. Initially, I wanted to know how well I can train Tesseract to read the image and find variable information.

## Getting Started

This project is done in Python 3 using Tesseract OCR. I have two scripts; the main script is TCCOR.py and the local testing script is test_TCCOR.py. I used the local testing script just to test and perfect my tesseract attributes without pulling live from the website I was scraping.

The script locates the TCCOR image, downloads it and adjust it to best allow tesseract to locate the target text. The variables.csv file is all possible combinations that tesseract might find in the image. The absolute variable file contains what those outcomes should translate to.

## Installed Packages

Here is a list of the packages imported

```
astroid==2.4.2
beautifulsoup4==4.9.1
bs4==0.0.1
certifi==2020.6.20
chardet==3.0.4
idna==2.10
isort==5.5.2
lazy-object-proxy==1.4.3
mccabe==0.6.1
Pillow==7.2.0
pylint==2.6.0
pytesseract==0.3.6
regex==2020.7.14
requests==2.22.0
six==1.15.0
soupsieve==1.9.2
tesserocr==2.5.1
toml==0.10.1
typed-ast==1.4.1
urllib3==1.25.10
wrapt==1.12.1
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