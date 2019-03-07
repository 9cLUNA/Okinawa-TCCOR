# Python and Tesseract for Image Reading

Using Python with the Tesseract OCR library wrapper to read current TCCOR information from the Kadena Air Force Base weather website. Initially, I wanted to know how well I can train Tesseract to read the image and find variable information.

## Getting Started

This project is done in Python 3 using Tesseract OCR. There is three main scripts.

One is the live script that pulls from the active website. I do not control the website so this script needs to be smart enough to adapt to changes that their website makes.

The other two scripts are test scripts. One is used for local testting purposes only, and the other is being used to pull the live website to create a method to actively search for the image or current TCCOR information if there is no image present.

The variables.csv file contains all those possible outcomes that Tesseract is looking for. We don't know what the image contains so all possible variations are presented to tesseract. The var_absolute file contains only those that we want to output or pass. These are what the final outcome should look like.

## Running the tests

Currently, the LIVE script is throwing an error.

```
tccorurl = urllink + tccor.find('img')['src'] # create the complete url
AttributeError: 'NoneType' object has no attribute 'find'
```

This occurs because there is currently no image and because the webmasters have changed the ID name of the DIV. Work is being done right now to ensure that the script looks through each DIV in the content section of the website to find the current TCCOR status.

## Built With

Software

* [Python 3](https://www.python.org/) - High-level, general purpose programming language.
* [Tesseract](https://github.com/tesseract-ocr/tesseract) - OCR engine.
* [pytesseract](https://pypi.org/project/pytesseract/) - Python's wrapper for Google's Tesseract-OCR engine.
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Python package for parsing HTML and XML websites. Useful to extract data and other web scraping needs.

Website

* [Shogun Weather](https://www.kadena.af.mil/Agencies/Local-Weather/) - Website that contains the current Typhoon condition for Okinawa, Japan.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.