# vfr-spickzettel
A cheat sheet for glider pilots [flying](https://en.wikipedia.org/wiki/Visual_flight_rules) near Stuttgart airport ([EDDS](https://en.wikipedia.org/wiki/Stuttgart_Airport)), considering glider sectors.

## Links

For details refer to [Arbeitskreis Sektoren](https://www.bwlv.de/verband-service/ak-sektoren).

## Dependencies

* [Python](https://www.python.org/) >= 3.9.0
* packages:
  * [numpy](https://numpy.org/), numpy-2.0.2,  see [w3schools.com](https://www.w3schools.com/python/numpy/default.asp)
  * [matplotlib](https://matplotlib.org), matplotlib-3.9.4 and related packages, see [w3schools.com](https://www.w3schools.com/python/matplotlib_intro.asp)


## Run Script

Running `vfr_spickzettel_plot.py` will create diagrams as 'vfr-spickzettel' in PNG, PDF, and SVG-format.

## Example

![vfr-spickzettel.png](vfr-spickzettel.png)

## VENV

On running in a virtual enviroment
* `py -m venv .venv`
* `.venv\Scripts\activate`
* recommended: `py -m pip install --upgrade pip`

`pip freeze` will detect no dependencies, so get Packages.
* `pip install numpy`
* `pip install matplotlib`

Then `pip freeze > requirements.txt` will create an appropriate file.

In your (virtual) enviroment, just get all of them by `pip install -r requirements.txt` !

---eof