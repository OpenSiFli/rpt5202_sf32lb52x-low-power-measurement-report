# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# import common config from sifli_docs_toolbox
from sifli_docs_toolbox.docs_conf import *

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SF32LB52x Low Power Measurement Report'

# uncomment this this line if you want to hide version listbox
# del html_context['versions']
# uncomment this this line if you want to hide language listbox
# del html_context['languages']
#git_last_updated_timezone = None

# Additional extensions for enhanced styling

chip = 'SF32LB52x'
doc_id = 'RPT5202'
doc_name = 'Low Power Consumption Scenario Testing Report'
doc_dir = 'rpt5202_sf32lb52x-low-power-measurement-report'

html_context.update({
    'chip': chip,
    'doc_id': doc_id,
    'doc_name': doc_name,
    })

pdf_url_enabled = True
