#!/usr/bin/env python
#
# stlearn documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))
import stlearn

# Setup files
import os

if not os.path.isdir("./_static"):
    url = "https://www.dropbox.com/s/gwbpu2xct6nbx6a/download.zip?dl=1"
    os.system("wget " + url)
    os.system("mv download.zip?dl=1 download.zip")
    os.system("unzip download.zip")

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "recommonmark",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "nbsphinx",
    "jupyter_sphinx",
    "sphinx_gallery.load_style",
]

# Generate the API documentation when building
autosummary_generate = True
autodoc_member_order = "bysource"
# autodoc_default_flags = ['members']
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_use_rtype = True  # having a separate entry generally helps readability
napoleon_use_param = True
napoleon_custom_sections = [("Params", "Parameters")]
todo_include_todos = False
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "stLearn"
copyright = "2022, Genomics and Machine Learning lab"
author = "Genomics and Machine Learning lab"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = stlearn.__version__
# The full version, including alpha/beta/rc tags.
release = stlearn.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#


def setup(app):
    app.add_stylesheet("css/theme_override.css")


html_theme = "sphinx_rtd_theme"
html_css_files = [
    "css/custom.css",
]
# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "stlearndoc"


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "stlearn.tex",
        "stLearn Documentation",
        "Genomics and Machine Learning lab",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "stlearn", "stLearn Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "stlearn",
        "stLearn Documentation",
        author,
        "stlearn",
        "One line description of project.",
        "Miscellaneous",
    ),
]


nbsphinx_thumbnails = {
    "tutorials/stSME_clustering": "_static/img/thumbnail/sme.png",
    "tutorials/stSME_comparison": "_static/img/thumbnail/com.png",
    "tutorials/Pseudo-time-space-tutorial": "_static/img/thumbnail/psts.png",
    "tutorials/stLearn-CCI": "_static/img/thumbnail/cci.png",
    "tutorials/Read_MERFISH": "_static/img/thumbnail/mer.png",
    "tutorials/Read_seqfish": "_static/img/thumbnail/seq.png",
    "tutorials/Working-with-Old-Spatial-Transcriptomics-data": "_static/img/thumbnail/legacy.png",
    "tutorials/Read_slideseq": "_static/img/thumbnail/slide.png",
    "tutorials/ST_deconvolution_visualization": "_static/img/thumbnail/decon.png",
    "tutorials/Interactive_plot": "_static/img/thumbnail/bokeh.gif",
    "tutorials/Working_with_scanpy": "_static/img/thumbnail/scanpy.png",
    "tutorials/Core_plots": "_static/img/thumbnail/core_plots.png",
    "tutorials/Read_any_data": "_static/img/thumbnail/any.png",
    "tutorials/Integration_multiple_datasets": "_static/img/thumbnail/integrate.png",
    "tutorials/Xenium_PSTS": "_static/img/thumbnail/xenium_psts.png",
    "tutorials/Xenium_CCI": "_static/img/thumbnail/xenium_cci.png",
}
