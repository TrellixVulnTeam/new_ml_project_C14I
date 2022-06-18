from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app =Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    logging.info("we are testing logging module")
    return 'starting of machine learning project'


if __name__ == "__main__":
    app.run(debug=True)