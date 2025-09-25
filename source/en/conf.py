# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# import common config from sifli_docs_toolbox
from sifli_docs_toolbox.docs_conf import *

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SF32LB52x 低功耗测试报告'
copyright = '2024, OpenSiFli'
author = 'OpenSiFli'
version = 'v1.0'
release = 'v1.0'

# uncomment this this line if you want to hide version listbox
# del html_context['versions']
# uncomment this this line if you want to hide language listbox
# del html_context['languages']
#git_last_updated_timezone = None

# Additional extensions for enhanced styling
extensions.extend([
    'sphinx_design',
    'myst_parser',
])

# MyST parser configuration for enhanced markdown support
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# HTML theme options for better appearance
html_theme_options.update({
    'show_prev_next': True,
    'show_navbar_depth': 2,
    'navbar_align': 'content',
    'use_edit_page_button': False,
})

# Custom CSS for enhanced styling
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]