import nbformat as nbf

# Create a new notebook
nb = nbf.v4.new_notebook()

# Sections and pip install commands
sections = {
    "Introduction": [
        "This notebook contains pip installation commands for all major libraries used in data analysis and data science."
    ],
    "1. Basic Libraries": [
        "!pip install numpy",
        "!pip install pandas",
        "!pip install scipy"
    ],
    "2. Data Visualization": [
        "!pip install matplotlib",
        "!pip install seaborn",
        "!pip install plotly",
        "!pip install bokeh",
        "!pip install altair"
    ],
    "3. Machine Learning": [
        "!pip install scikit-learn",
        "!pip install xgboost",
        "!pip install lightgbm",
        "!pip install catboost"
    ],
    "4. Deep Learning": [
        "!pip install tensorflow",
        "!pip install keras",
        "!pip install torch",
        "!pip install torchvision",
        "!pip install fastai"
    ],
    "5. Natural Language Processing (NLP)": [
        "!pip install nltk",
        "!pip install spacy",
        "!pip install transformers"
    ],
    "6. Data Cleaning & Processing": [
        "!pip install missingno",
        "!pip install openpyxl",
        "!pip install xlrd"
    ],
    "7. Statistical Analysis": [
        "!pip install statsmodels",
        "!pip install pingouin"
    ],
    "8. Data Engineering": [
        "!pip install dask",
        "!pip install pyspark"
    ],
    "9. Model Deployment": [
        "!pip install flask",
        "!pip install fastapi",
        "!pip install mlflow"
    ],
    "10. Other Useful Libraries": [
        "!pip install tqdm",
        "!pip install joblib",
        "!pip install pyyaml",
        "!pip install requests"
    ]
}

# Add cells to the notebook
for section, commands in sections.items():
    nb.cells.append(nbf.v4.new_markdown_cell(f"## {section}"))
    for command in commands:
        nb.cells.append(nbf.v4.new_code_cell(command))

# Save the notebook to a file
output_path = "Data_Science_Pip_Installations.ipynb"
with open(output_path, 'w') as f:
    nbf.write(nb, f)

print(f"Notebook created: {output_path}")
