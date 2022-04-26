
import os

# DB Settings - Defaults to values specific for Mongo,
# but Postgresql is also supported.
DB_URI = os.environ.get('CHARTS_DB_HOST', 'localhost')
DB_PORT = int(os.environ.get('CHARTS_DB_PORT', 27017))
DB_NAME = os.environ.get('CHARTS_DB_DB', 'charts')
# This name is used for table/collection,
# regardless of Postgresql or Mongodb usage.
DB_TABLE = os.environ.get('CHARTS_DB_TABLE', 'views')
ACTIVE_DB = os.environ.get('CHARTS_ACTIVE_DB', 'mongo').lower()

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
        'js_url': ['/static/js/vendor/d3.min.js'],
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
            ('//cdnjs.cloudflare.com/ajax/libs/cytoscape/'
             '3.1.0/cytoscape.min.js'),
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
    'Sparklines': {
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
            ('//cdnjs.cloudflare.com/ajax/libs/jquery-sparklines/'
             '2.1.2/jquery.sparkline.min.js'),
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


def get_all_assets():
    """Load ALL asset files for css/js from config."""
    cssfiles, jsfiles = [], []
    for c in CHARTS_CONFIG.values():
        if c['css_url'] is not None:
            cssfiles += c['css_url']
        if c['js_url'] is not None:
            jsfiles += c['js_url']
    return dict(
        css=cssfiles,
        js=jsfiles
    )


def get_active_assets(families):
    """Given a list of chart families, determine what needs to be loaded."""
    families += ['d3']
    assets = dict(css=[], js=[])
    families = set(families)
    for family, data in CHARTS_CONFIG.items():
        if family in families:
            # Also add all dependency assets.
            if data['dependencies']:
                for dep in data['dependencies']:
                    assets['css'] += [
                        css for css in CHARTS_CONFIG[dep]['css_url']
                        if css not in assets['css']]

                    assets['js'] += [
                        js for js in CHARTS_CONFIG[dep]['js_url']
                        if js not in assets['js']
                    ]
            assets['css'] += [
                css for css in data['css_url'] if css not in assets['css']]
            assets['js'] += [
                js for js in data['js_url'] if js not in assets['js']]
    assets['css'] = list(assets['css'])
    assets['js'] = list(assets['js'])
    return assets
