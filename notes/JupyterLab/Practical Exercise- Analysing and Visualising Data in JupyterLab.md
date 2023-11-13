## Practical Exercise: Analysing and Visualising Data in JupyterLab

### Objective
Install JupyterLab on a Windows system, create a new Jupyter notebook, perform a basic data analysis, and visualise the results using a chart.

### Requirements
- A Windows-based computer.
- Internet access for downloading necessary software and data.

### Instructions

#### Part 1: Installation
1. **Install Python**:
   - Ensure Python is installed on your system. If not, download and install the latest version of Python from [python.org](https://www.python.org/downloads/windows/).

2. **Install JupyterLab**:
   - Open Command Prompt and run the following command:

	```bash
	pip install jupyterlab     
	```

3. **Launch JupyterLab**:
   - In Command Prompt, run:

	```bash
	jupyter lab
	```

   - Your default web browser will open with the JupyterLab interface.

#### Part 2: Creating and Running a Notebook
1. **Create a New Notebook**:
   - Click on the '+' icon to open the Launcher and select 'Python 3' under the Notebook section.

2. **Name Your Notebook**:
   - Click on the notebook title (Untitled.ipynb by default) at the top of the page and rename it to 'Sample_Data_Analysis'.

#### Part 3: Simple Data Analysis
1. **Installing scikit-learn, Pandas and Matplotlib**:
   - If not already installed, add a new cell and run:

	```bash
	!pip install scikit-learn pandas matplotlib
	```

2. **Import Libraries**:
   - In a new cell, import the necessary libraries:

	```python
	import pandas as pd
	import matplotlib.pyplot as plt
	from sklearn.datasets import load_iris
	```

3. **Load Sample Data**:
   - Use the Iris dataset:
	```python
	iris = load_iris()
	df = pd.DataFrame(iris.data, columns=iris.feature_names)
	```

4. **Basic Data Analysis**:
   - Add a new cell to calculate basic statistics:

	```python
	 df.describe()
	```

#### Part 4: Visualising Data
1. **Create a Chart**:
   - In a new cell, type the following code to create a line chart:

	```python
	df.plot()
	plt.title('Iris Dataset Features')
	plt.xlabel('Sample Number')
	plt.ylabel('Feature Value')
	plt.show()
	```

#### Part 5: Conclusion
1. **Save Your Notebook**:
   - Use 'Ctrl + S' or the 'Save' icon to save your notebook.

2. **Close JupyterLab**:
   - In Command Prompt, press 'Ctrl + C' to stop JupyterLab.
