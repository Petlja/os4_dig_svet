
import os
import petljadoc

from runestone import runestone_static_dirs, runestone_extensions

petljadoc.runestone_ext.add_module('blockly')
#petljadoc.runestone_ext.add_module('blockpylib')
#petljadoc.runestone_ext.add_module('simanim')
#petljadoc.runestone_ext.add_module('pycode')
#petljadoc.runestone_ext.add_module('p5js')
#petljadoc.runestone_ext.add_module('dbDirective')
#petljadoc.runestone_ext.add_module('regexcheck')
#petljadoc.runestone_ext.add_module('nimgame')
                          

extensions = ['sphinx.ext.mathjax'] + runestone_extensions() + petljadoc.runestone_ext.extensions()

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The root toctree document.
root_doc = 'index'

# General information about the project.
project = 'Petlja - os4_dig_svet'
#pylint: disable=redefined-builtin
copyright = '2023 me'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'
locale_dirs = ['locals']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# `keep_warnings <http://www.sphinx-doc.org/en/stable/config.html#confval-keep_warnings>`_:
# If true, keep warnings as “system message” paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run.
keep_warnings = True

# `rst_prolog <http://www.sphinx-doc.org/en/stable/config.html#confval-rst_prolog>`_:
# A string of reStructuredText that will be included at the beginning of every
# source file that is read.
rst_prolog = (
# For fill-in-the-blank questions, provide a convenient means to indicate a blank.
"""

.. |blank| replace:: :blank:`x`
"""
)

# -- Options for HTML output ---------------------------------------------------


html_context = {'course_id': 'os4_dig',
                'login_required':'false',
                'appname': "runestone",
                'loglevel': int("0"),
                'course_url': "http://127.0.0.1:8000",
                'use_services': 'false',
                'python3': 'true',
                'dburl': os.environ['DBURL'] if 'DBURL' in os.environ else '',
                'default_ac_lang': 'python',
                'basecourse': 'os4_dig',
                'jobe_server': 'http://jobe2.cosc.canterbury.ac.nz',
                'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
                'proxy_uri_files': '/jobe/index.php/restapi/files/',
                'downloads_enabled': 'false',
                'enable_chatcodes': 'false',
                'course':petljadoc.cli.read_course(),
                'page_settings':petljadoc.cli.read_page_settings(),
               }

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'petljadoc_course_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "Petlja - os4_dig_svet",
    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Chapters",
    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,
    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "false",
    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nav",
    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    #
    # Note that this is served off CDN, so won't be available offline.
    #'bootswatch_theme': "slate",
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["_templates/plugin_layouts"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Petlja - os4_dig_svet'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title ='Petlja - os4_dig_svet'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']  + runestone_static_dirs() + petljadoc.runestone_ext.static_dirs()

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**' : ['globaltoc.html']
}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If false, no index is generated.
html_use_index = False

petljadoc.runestone_ext.config_values_for_components(globals())