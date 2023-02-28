import nbformat

# Reading the notebooks
first_notebook = nbformat.read('Assignment1.ipynb', 4)
second_notebook = nbformat.read('Assignment1Group1.ipynb', 4)

# Creating a new notebook
final_notebook = nbformat.v4.new_notebook(metadata=first_notebook.metadata)

# Concatenating the notebooks
final_notebook.cells = first_notebook.cells + second_notebook.cells

# Saving the new notebook 
nbformat.write(final_notebook, 'final_notebook.ipynb')