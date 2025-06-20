# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Check Your Vanilla Gift Card Balance'
copyright = '2025, Vanilla'
author = 'Vanilla Gift Card Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = []

# Templates path
templates_path = ['_templates']

# Patterns to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Check Your Vanilla Gift Card Balance at vanillagift.com – Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Vanilla Balance Check"

# Favicon (place favicon.ico in the root or _static folder if available)
html_favicon = 'favicon.ico'

# Theme (you can uncomment and set a different one if installed)
# html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'  # Default Sphinx theme

# Hide the "View page source" link
html_show_sourcelink = False

# Allow raw HTML in .rst files (important for embedded buttons, videos, etc.)
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
    'description': 'Step-by-step instructions to check your Vanilla Gift Card balance online.',
}

# Paths to static files like custom CSS or JavaScript (optional)
# html_static_path = ['_static']
