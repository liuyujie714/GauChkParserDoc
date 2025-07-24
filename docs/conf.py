# Configuration file for the Sphinx documentation builder.

project = 'GauChkParser'
copyright = '2025, Yujie Liu'
author = 'Yujie Liu'
release = __import__('GauChkParser').__version__
version = release


#import os
#import sys
#sys.path.insert(0, os.path.abspath('../../GauChkParser'))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
#    'sphinx.ext.viewcode',  # 支持查看源码
    'sphinx.ext.napoleon',  # 支持 Doxygen 风格
    'sphinx_markdown_tables', 'myst_parser', # 支持Markdown
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# show python api order
autodoc_member_order = 'bysource'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


