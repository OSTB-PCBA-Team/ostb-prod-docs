# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ostb-docs'
copyright = '2025, https://cn.ostb-pcba.com'
author = 'https://cn.ostb-pcba.com'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []
html_show_sourcelink = False

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_favicon = '_static/images/favicon.png'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.autodoc',
  'recommonmark',
  'rst2pdf.pdfbuilder'
]

# Note:  'display_version' option is now obsolete in the current (08-Oct-2024)
# version of sphinx-rtd-theme (upgraded for Sphinx v8.x).  The removed line
# is preserved by commenting it out in case it is ever needed again.
html_theme_options = {
    "sidebar_hide_name": True,      # True when the logo carries project name
    "light_logo": "images/logo-light.png",
    "dark_logo": "images/logo-dark.png",
}
