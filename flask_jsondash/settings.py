# -*- coding: utf-8 -*-

"""
flask_jsondash.settings
~~~~~~~~~~~~~~~~~~~~~~~

App/blueprint wide settings.

:copyright: (c) 2016 by Chris Tabor.
:license: MIT, see LICENSE for more details.
"""

import os

# DB Settings - Defaults to values specific for Mongo,
# but Postgresql is also supported.
# ACTIVE_DB = os.environ.get('CHARTS_ACTIVE_DB', 'mongo').lower()

ACTIVE_DB = os.environ.get('CHARTS_ACTIVE_DB', 'mysql').lower()
DB_PORT = int(os.environ.get('CHARTS_DB_PORT', 3306))
DB_TABLE = os.environ.get('CHARTS_DB_TABLE', 'views')

USERNAME ='root'
PASSWORD = 'root'
DB_NAME = os.environ.get('CHARTS_DB_DB', 'beescms')
DB_URI = os.environ.get('CHARTS_DB_HOST', '127.0.0.1')

# DB_URI = os.environ.get('CHARTS_DB_HOST', '82.157.143.130')
# DB_NAME = os.environ.get('CHARTS_DB_DB', 'bi_jsondash')

# USERNAME ='bi_jsondash'
# PASSWORD = '12345678'

# DB_URI = os.environ.get('CHARTS_DB_HOST', '10.10.163.19')
# DB_NAME = os.environ.get('CHARTS_DB_DB', 'qi_lan')
# USERNAME ='qi_lan'
# PASSWORD = 'RiREk5katX'

"""
Chart configuration below -- this is essential to making the frontend work.
Default values have been added, but you can change them by importing your
own override (see bottom).

Configuration:

'charts' is a list of 2-tuples, where:

1. The first index is the type -- this MUST NOT CHANGE!
2. The second index is the label -- This is configurable.

'css_url'/'js_url' can be relative or absolute paths.

"""

CHARTS_CONFIG = {
    'd3force': {
        'charts': [
            ('3dnode', '3dnode'),
        ],
        'dependencies': ['d3force'],

        'js_url': [
            '/static/js/vendor/three.js',
            '/static/js/vendor/three-spritetext.min.js',
            '/static/js/vendor/3d-force-graph.min.js',
            '/static/js/vendor/d3force.js'
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'http://c3js.org/reference.html',
    },
    'force2d': {
        'charts': [
            ('2dnode', '2dnode'),
        ],
        'dependencies': ['force2d'],

        'js_url': [
        # '/static/js/vendor/d3v4.min.js',
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'http://c3js.org/reference.html',
    },
    'echarts': {
        'charts': [
            ('basice', 'basic echart'),
            ('linee', 'lines echart'),
            ('array', 'array echart'),
            ('map', 'map echart'),
        ],
        'dependencies': ['echarts'],
        'js_url': ['/static/js/vendor/echarts.min.js',
                    # '/static/js/vendor/map/china.js',
                    # '/static/js/vendor/map/beijing.js',
                    # '/static/js/vendor/map/hunan.js',                    
                    # '/static/js/vendor/map/sichuan.js',
                    '/static/js/vendor/echarts.bundle.min.js'],
        'css_url': [],
        'enabled': True,
        'help_link': 'http://echart.org/',
    },
    'C3': {
        'charts': [
            ('line', 'Line chart'),
            ('bar', 'Bar chart'),
            ('timeseries', 'Timeseries chart'),
            ('step', 'Step chart'),
            ('pie', 'Pie chart'),
            ('area', 'Area chart'),
            ('donut', 'Donut chart'),
            ('spline', 'Spline chart'),
            ('gauge', 'Gauge chart'),
            ('scatter', 'Scatter chart'),
            ('area-spline', 'Area spline chart'),
        ],
        'dependencies': ['D3'],
        'js_url': ['/static/js/vendor/c3.min.js'],
        'css_url': ['/static/css/vendor/c3.min.css'],
        'enabled': True,
        'help_link': 'http://c3js.org/reference.html',
    },
    'D3': {
        'charts': [
            ('radial-dendrogram', 'Radial Dendrogram'),
            ('dendrogram', 'Dendrogram'),
            ('treemap', 'Treemap'),
            ('voronoi', 'Voronoi'),
            ('circlepack', 'Circle Pack'),
        ],
        'dependencies': [],
        'js_url': ['/static/js/vendor/d3.v3.min.js'],
        'css_url': [],
        'enabled': True,
        'help_link': 'https://github.com/d3/d3/wiki',
    },
    'FlameGraph': {
        'charts': [
            ('flamegraph', 'Flame Graph'),
        ],
        'dependencies': ['D3'],
        'js_url': [
            '/static/js/vendor/d3.flameGraph.js',
            '/static/js/vendor/d3.tip.v0.6.3.js'
        ],
        'css_url': ['/static/css/vendor/d3.flameGraph.css'],
        'enabled': True,
        'help_link': 'https://github.com/spiermar/d3-flame-graph',
    },
    'WordCloud': {
        'charts': [
            ('wordcloud', 'Word Cloud'),
        ],
        'js_url': [
            ('/static/js/vendor/d3.layout.cloud.min.js'),
        ],
        'css_url': [],
        'enabled': True,
        'dependencies': ['D3'],
        'help_link': 'https://github.com/jasondavies/d3-cloud',
    },
    'Basic': {
        'charts': [
            ('custom', 'Custom direct loading of any arbitrary html.'),
            ('iframe', 'Embedded iframe.'),
            ('image', 'Image (inline embed)'),
            ('numbergroup', ('Group of numbers with titles '
                             'representing some aggregate values for '
                             'each column.')),
            ('number', ('Single number (size autoscaled) representing '
                        'some aggregate value.')),
            ('youtube', 'YouTube video embedded as an iframe.'),
        ],
        'dependencies': [],
        'js_url': [],
        'css_url': [],
        'enabled': True,
        'help_link': ('https://github.com/christabor/flask_jsondash/blob/'
                      'master/docs/schemas.md'),
    },
    'Vega': {
        'charts': [
            ('vega-lite', 'vega-lite specification.'),
        ],
        'dependencies': ['D3'],
        'js_url': [
            ('/static/js/vendor/vega.min.js'),
            ('/static/js/vendor/vega-lite.min.js'),
            ('/static/js/vendor/vega-embed.min.js'),
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'https://vega.github.io/vega-lite/docs',
    },
    'DataTable': {
        'charts': [
            ('datatable', 'A table of data, with sorting and filtering.'),
        ],
        'dependencies': [],
        'js_url': [
            ('/static/js/vendor/jquery.dataTables.min.js'),
            ('/static/js/vendor/dataTables.bootstrap.min.js')
        ],
        'css_url': [
            ('/static/css/vendor/dataTables.bootstrap.min.css'),
        ],
        'enabled': True,
        'help_link': 'https://datatables.net/reference/index',
    },
    'Timeline': {
        'charts': [
            ('timeline', 'A timeline.js timeline'),
        ],
        'dependencies': [],
        'js_url': ['/static/js/vendor/timeline.js'],
        'css_url': [
            '/static/css/vendor/timeline.css'],
        'enabled': True,
        'help_link': 'https://timeline.knightlab.com/docs/',
    },
    'Venn': {
        'charts': [
            ('venn', 'A venn.js Venn or Euler diagram'),
        ],
        'dependencies': ['D3'],
        'js_url': ['/static/js/vendor/venn.js'],
        'css_url': [],
        'enabled': True,
        'help_link': 'https://github.com/benfred/venn.js/',
    },
    'SigmaJS': {
        'charts': [
            ('sigma', 'SigmaJS default json based graph'),
        ],
        'dependencies': [],
        'js_url': [
            '/static/js/vendor/sigma.min.js',
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'http://sigmajs.org',
    },
    'Cytoscape': {
        'charts': [
            ('cytoscape', ('Cytoscape compatible json configuration '
                           '(core layouts only).')),
        ],
        'dependencies': [],
        'js_url': [
            ('/static/js/vendor/cytoscape.min.js'),
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'http://js.cytoscape.org/',
    },
    'Graph': {
        'charts': [
            ('graph', 'Graph using the graphviz .dot specification'),
        ],
        'dependencies': ['D3'],
        'js_url': [
            ('/static/js/vendor/dagre-d3.min.js'),
            ('/static/js/vendor/graphlib-dot.min.js'),
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'https://github.com/cpettitt/dagre-d3/wiki',
    },
    'Sparkline': {
        'charts': [
            ('sparklines-line', 'Sparkline Line'),
            ('sparklines-bar', 'Sparkline Bar'),
            ('sparklines-tristate', 'Sparkline Tristate'),
            ('sparklines-discrete', 'Sparkline Discrete'),
            ('sparklines-bullet', 'Sparkline Bullet'),
            ('sparklines-pie', 'Sparkline Pie'),
            ('sparklines-box', 'Sparkline Box'),
        ],
        'dependencies': [],
        'js_url': [
            ('/static/js/vendor/jquery.sparkline.min.js'),
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'http://omnipotent.net/jquery.sparkline/#s-docs',
    },
    'PlotlyStandard': {
        'charts': [
            ('plotly-any', 'Plotly serializable specification'),
        ],
        'dependencies': [],
        'js_url': [
            '/static/js/vendor/plotly-latest.min.js',
        ],
        'css_url': [],
        'enabled': True,
        'help_link': 'https://plot.ly/javascript/',
    },
}
