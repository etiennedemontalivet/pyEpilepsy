# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('./../../'))

# -- Project information -----------------------------------------------------
from pyepilepsy import __version__

project = 'pyEpilepsy'
copyright = '2023, Etienne de Montalivet'
author = 'Etienne de Montalivet'
release = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "numpydoc",
    "sphinx.ext.autosectionlabel",
]

templates_path = ['_templates']
exclude_patterns = []

# copy code button settings
copybutton_prompt_text = ">>> "

# numpydoc_class_members_toctree = True
# numpydoc_show_class_members = True
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 10

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autosummary_imported_members = False
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
