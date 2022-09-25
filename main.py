import convert
from flask import Flask

import csv_converter

app = Flask(__name__)


app.register_blueprint(convert.conversion_router, url_prefix='/convert')


if __name__ == '__main__':
    output: bytes = csv_converter.convert('examples/TechCrunchcontinentalUSA.csv', 'examples/query.sparql')
    foutput = open('output.rdf', 'wb')
    foutput.write(output)
    foutput.close()
