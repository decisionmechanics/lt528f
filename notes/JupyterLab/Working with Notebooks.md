## Working with Notebooks

### Basic Operations
- **Writing and Executing Code**:
	  - Input code into a cell and execute it using 'Shift + Enter'.
	  - The output or result is displayed immediately below the cell.
- **Adding Markdown Text**:
	  - Use Markdown cells for adding text, headers, lists, links, and images to annotate your code.
	  - Markdown syntax is simple: use `#` for headers, `*` or `-` for bullet points, `**text**` for bold, `*text*` for italics.
- **Using Keyboard Shortcuts**:
	  - Familiarise with shortcuts like 'A' (insert cell above), 'B' (insert cell below), 'DD' (delete cell), 'M' (convert cell to markdown), 'Y' (convert cell to code), etc.
	  - Access the full list from 'Help' \> 'Keyboard Shortcuts' in the Menu Bar.

### Data Visualisation
- **Introduction to Visualisation Libraries**:
	  - Libraries like Matplotlib, Seaborn, or Plotly can be used for data visualisation in notebooks.
	  - Basic usage involves importing the library and calling its functions to create plots.
- **Creating a Simple Plot**:
	  - Example: `import matplotlib.pyplot as plt`, followed by `plt.plot([data])` to create a line plot.
	  - Display the plot in the notebook with `plt.show()`.
- **Customising Plots**:
	  - Adjust plot size, color, labels, title, and axis details using Matplotlib's functions.
	  - Example: `plt.title('Your Title')` to add a title to the plot.

### Saving and Exporting Work
- **Saving Notebooks**:
	  - Regularly save your work with 'Ctrl + S' (or 'Cmd + S' on macOS).
	  - JupyterLab also autosaves notebooks at regular intervals.
- **Exporting Notebooks**:
	  - Export notebooks to various formats like PDF, HTML, or Python script via 'File' \> 'Export Notebook As'.
	  - Useful for sharing your work with others who do not have JupyterLab.
- **Version Control**:
	  - Consider using version control systems like Git for managing changes and collaboration.
	  - JupyterLab can integrate with Git and GitHub for version control.