# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- sys.path preparation ----------------------------------------------------
#

import os
import sys
sys.path.insert(0, os.path.abspath("."))


#
# -- Project information ------------------------------------------------------
#

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

project = "SymPy Documentation"
full_title = project
copyright = "2021, SymPy"
author = "Daniele Procida"
version = "1.8"
release = version

#
# -- General configuration ----------------------------------------------------
#

extensions = [
    "extensions",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
    "sphinx_inline_tabs",
    "sphinx_click",
    "notfound.extension",
]

if "spelling" in sys.argv:
    extensions.append("sphinxcontrib.spelling")

mermaid_version="8.5.2"

#
# -- Options for intersphinx --------------------------------------------------
#

intersphinx_mapping = {
    "user": ("https://sympy.org/", None),
    "python": ("https://docs.python.org/3", None),
    "django": (
        "https://docs.djangoproject.com/en/2.2/",
        "https://docs.djangoproject.com/en/2.2/_objects/"
    ),
    "django-cms": ("http://docs.django-cms.org/en/latest/", None),
    "celery": ("https://docs.celeryproject.org/en/stable/", None),
    "whitenoise": ("https://whitenoise.evans.io/en/stable/", None),
    "flask": ("https://flask.palletsprojects.com/", None),
}

#
# -- Options for the theme ----------------------------------------------------
#

html_theme = "furo"

#
# -- Options for HTML output --------------------------------------------------
#

html_title = full_title
htmlhelp_basename = "SymPydocs"

#
# -- Options for Sphinx -------------------------------------------------------
#

source_suffix = ".rst"
master_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "env"]
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

#
# -- Options for spelling -----------------------------------------------------
#

spelling_lang = "en_GB"
spelling_word_list_filename = "spelling_wordlist"
spelling_ignore_pypi_package_names = True

#
# -- Options for latex output -------------------------------------------------
#

latex_documents = [
    (master_doc, htmlhelp_basename + ".tex", full_title, author, "manual"),
]

#
# -- Options for manual page output -------------------------------------------
#

man_pages = [
    (master_doc, htmlhelp_basename, full_title, [author], 1)
]

#
# -- Options for TODOs --------------------------------------------------------
#

todo_include_todos = True
todo_link_only = True
todo_emit_warnings = False
