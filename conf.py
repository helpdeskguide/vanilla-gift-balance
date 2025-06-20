# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate Peacock TV on Your Device'
copyright = '2025, NBCUniversal'
author = 'NBCUniversal'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Activate Peacock TV at PeacockTV.com/tv – Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Peacock TV Activation"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'  # Place your favicon in the _static directory

# Theme (you can uncomment this if using ReadTheDocs or others)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# Uncomment the line below if you have custom styles, favicon, etc.
# html_static_path = ['_static']

# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
