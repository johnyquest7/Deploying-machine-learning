from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

import pickle
import pandas as pd
import os
import numpy as np


# Preparing the Classifier
cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/classifier.pkl'), 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
	
	return render_template('index2.html')

@app.route('/results', methods=['POST'])
def predict():
	thickness = int(request.form['thickness'])
	size = int(request.form['size'])
	shape = int(request.form['shape'])
	adhesion = int(request.form['adhesion'])
	single = int(request.form['single'])
	nuclei = int(request.form['nuclei'])
	chromatin = int(request.form['chromatin'])
	nucleoli = int(request.form['nucleoli'])
	mitosis = int(request.form['mitosis'])

	input_data = [{'thickness': thickness, 'size': size, 'shape': shape, 'adhesion': adhesion, 'single': single, 'nuclei': nuclei, 'chromatin': chromatin,
				   'nucleoli': nucleoli, 'mitosis': mitosis}]
	data = pd.DataFrame(input_data)
	label = {0: 'Benign', 1: 'Malignant'}
	logreg = clf.predict(data)[0]
	resfinal = label[logreg]
	return render_template('results.html', res=resfinal)

if __name__ == '__main__':
	app.run(debug=True)