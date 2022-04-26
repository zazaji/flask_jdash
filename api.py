# -*- coding: utf-8 -*-
from itertools import combinations
import json
import locale
import os
from datetime import timedelta as td
from datetime import datetime as dt
from random import randrange as rr
from random import choice, random,randint
import time
from flask_cors import CORS
from flask import (Blueprint, request,
    Flask,
    abort,
    request,
    jsonify,
    render_template,
)
locale.setlocale(locale.LC_ALL, '')


cwd = os.getcwd()
print(' path cwd is '+cwd)
app = Blueprint('fir_blueprint',__name__)
CORS(app, supports_credentials=True)

@app.route('/', methods=['GET'])
def home():
    return "home"

@app.route('/test', methods=['GET'])
def test():
    return "test success"


@app.route('/listapi')
def listapi():
    conn=engine.connect()
    sql = 'select guid,module,name,category from modules'
    result=pd.read_sql(sql,conn)[['module']].to_dict(orient='records')
    conn.close()
    result= [eval(r['module'].replace('\n',''))['dataSource'] for r in result]
    return str(set(result))


def recursive_d3_data(current=0, max_iters=12, data=None):
    """Generate d3js data for stress testing.
    Format is suitable in treemap, circlepack and dendrogram testing.
    """
    if current >= max_iters:
        return data
    if data is None:
        data = dict(name='foo', size=rr(10, 10000), children=[])
    data = dict(name='foo', size=rr(10, 10000),
                children=[data, data])
    return recursive_d3_data(
        current=current + 1,
        max_iters=max_iters,
        data=data)


def dates_list(max_dates=10):
    """Generate a timeseries dates list."""
    now = dt.now()
    return [str(now + td(days=i * 10))[0:10] for i in range(max_dates)]


def rr_list(max_range=10):
    """Generate a list of random integers."""
    return [rr(0, 100) for i in range(max_range)]
    # return random.sample(range(num), ncount)

def rand_hex_color():
    """Generate a random hex color.
    e.g. #FF0000
    """
    chars = list('0123456789ABCDEF')
    return '#{0}{1}{2}{3}{4}{5}'.format(
        choice(chars),
        choice(chars),
        choice(chars),
        choice(chars),
        choice(chars),
        choice(chars),
    )




@app.route("/echart_line")
def echart_lines():
    option =  {
       'theme':'light',
        'xAxis': {
            'type': 'category',
            'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [{
            'data': rr_list(7),
            'type': 'line',
            'smooth': True
        }, {
            'data': rr_list(7),
            'type': 'line',
            'smooth': True
        }]
    } 
    return option



@app.route("/nodes")
def nodes():

    nodes = request.args.get('nodes', 'abcdefghijijklmnopqrstuvwxyz1234567890')
    _vertices = list(nodes)
    _edges = combinations(_vertices, 2)
    edges, vertices = [], []
    edges=[]
    for (frm, to) in _edges:
        edge=dict(
            id='{}-{}'.format(frm, to),
            color=rand_hex_color(),
            source=frm,
            target=to,
            size=0.1*rr(2, 10),
            x=rr(1, 100),
            y=rr(1, 100),
        )
        if rr(0,50)>=47: edges.append(edge)
    for vertex in _vertices:
        vertices.append(dict(
            id=vertex,
            name='a'+vertex,
            size=rr(1, 10),
            x=rr(1, 100),
            y=rr(1, 100),
            color=rand_hex_color(),
            label='node {}'.format(vertex),
        ))
    data = dict(
        bgcolor='rgba(0,0,0,0)',
        nodes=vertices,
        links=edges,
        )
    return data


@app.route("/echart_multi")
def echart_multi():
    option= {
       'theme':'light',
       'legend': {},
       'tooltip': {},
      'xAxis': {
        'type': 'category',
        'data': ['AA', 'Milk', 'Tea', 'Cheese', 'Cocoa', 'Walnut', 'Brownie']
      },
      'yAxis': {},
      'series': [
        {
          'type': 'bar',
          'name': '2015',
          'data': rr_list(7)
        },
        {
          'type': 'line',
          'name': '2016',
          'data': rr_list(7)
        },
        {
          'type': 'scatter',
          'name': '2017',
          'data': rr_list(7)
        }
      ]
    }
    return option
@app.route("/echart_array")
def echart_array():
    data= {
        'class_count':3,
        'theme':'light',
        'source':  [
          ['product', '2015', '2016', '2017'],
          ['Matcha Latte' ]+rr_list(3),
          ['Milk Tea']+rr_list(3),
          ['Cheese Cocoa']+rr_list(3),
          ['Walnut Brownie']+rr_list(3),
            ]
        }


    return data

@app.route('/map')
def map():
    data= {
        'theme':'dark',##dark
        'name': '地图测试',
        'type': 'map',
        'mapType': 'china', 
        'label': {
            'show': True
        },
        'max':100,
        'min':50,
        'data': [
            {'name': '西藏', 'value': rr(50, 100)},
            {'name': '新疆', 'value': rr(50, 100)},
            {'name': '北京', 'value': rr(50, 100)},
            {'name': '上海', 'value': rr(50, 100)},
            {'name': '内蒙古', 'value': rr(50, 100)},
            {'name': '甘肃', 'value': rr(50, 100)},
            {'name': '四川', 'value': rr(50, 100)},
            {'name': '云南', 'value': rr(50, 100)},
            {'name': '黑龙江', 'value': rr(50, 100)},
            {'name': '青海', 'value': rr(50, 100)},
            {'name': '成都', 'value': rr(50, 100)},
            {'name': '汉中', 'value': rr(50, 100)},
        ],
        'dataValue':[
            {'name':'天津', 'value': [117.2, 39.13,rr(50, 100)]},
            {'name':'青岛', 'value': [120.33, 36.07,rr(50, 100)]},
            {'name':'雄安', 'value': [115.9, 38.05,rr(50, 100)]},
            {'name':'长沙', 'value': [113, 28.21,rr(50, 100)] },
            {'name':'西安','value': [108.95, 34.27,rr(50, 100)]},
           { 'name':'成都','value': [104.06, 30.67,rr(50, 100)]}
          ]
    }

    
    return data
    
@app.route('/numbergroup')
def numbergroup():
    """Fake endpoint."""
    dataset = int(request.args.get('dataset', 0))
    # multiple examples shown here for variadic demonstrations
    datas = [
        [
            {
                "title": "Number of widgets sold in last day",
                "description": 'This is a good sign',
                "data": rr(300,5000),
                "color": "green",
            },
            {
                "title": "New customers signed up this week",
                "description": 'New user accounts created',
                "data": rr(300,5000),
            },
            {
                "title": "Average Daily Users",
                "description": "(aka DAU)",
                "data": rr(300,5000),
                "noformat": False,
            },
            {
                "title": "Max concurrent users this week",
                "description": "Server load peak",
                "data": rr(300,5000),
                "color": "orange",
                "noformat": True,
            },
        ],
        [
            {
                "title": "Simple thing",
                "data": rr(300,5000),
                "width": "33%",
                "description": "Just a simple number"
            },
            {
                "title": "Simple thing 2",
                "data": rr(30,500),
                "width": "33%",
                "description": "Just a simple number"
            },
            {
                "title": "Simple thing 3",
                "data": rr(30,500),
                "width": "33%",
                "description": "Just a simple number"
            },
        ],
        [
            {
                "title": "Average time on site",
                "description": "Signed in to signed out (units nostyle)",
                "data": str(rr(30,500))+' minutes',
                "color": "#7D4EE4",
            },
            {
                "title": "Average time on site page X",
                "description": "Signed in to signed out (custom units style)",
                "data": rr(30,500),
                "units": "minutes",
            },
            {
                "title": "Average $ spent per day",
                "description": "Yeeehaw (custom units style)",
                "data": rr(30,500),
                "units": "dollars"
            },
        ]
    ]
    return jsonify(datas[dataset])



@app.route('/combination')
def combination():
    """Fake endpoint."""
    data = {
        'columns': [
            ['data1', 30, 20, 50, 40, 60, 50],
            ['data2', 200, 130, 90, 240, 130, 220],
            ['data3', 300, 200, 160, 400, 250, 250],
            ['data4', 200, 130, 90, 240, 130, 220],
            ['data5', 130, 120, 150, 140, 160, 150],
            ['data6', 90, 70, 20, 50, 60, 120],
        ],
        'type': 'bar',
        'types': {
            'data3': 'spline',
            'data4': 'line',
            'data6': 'area',
        },
        'groups': [
            ['data1', 'data2'],
        ]
    }
    return jsonify(dict(data=data))



@app.route('/timeseriesc3')
def timeseriesc3():
    """Fake endpoint."""
    return jsonify(dict(
        dates=[
            '19{}-{}-{}'.format(rr(10, 99), rr(10, 31), rr(10, 31))
            for _ in range(4)
        ],
        abc=rr_list(max_range=4),
        cde=rr_list(max_range=4),
    ))




@app.route('/stacked-bar')
def stackedbar():
    """Fake endpoint."""
    return jsonify({
        'data': {
            'columns': [
                ['data1', -30, 200, 200, 400, -150, 250],
                ['data2', 130, 100, -100, 200, -150, 50],
                ['data3', -230, 200, 200, -300, 250, 250]
            ],
            'type': 'bar',
            'groups': [
                ['data1', 'data2']
            ]
        },
        'grid': {
            'y': {
                'lines': [{'value': 0}]
            }
        }
    })

@app.route('/timevalues')
def timevalues():
    """Fake endpoint."""

    return jsonify({
    "dates": [time.time()],
    "line1": [randint(10,100)],

    })



@app.route('/wordcloud')
def wordcloud():
    """Fake endpoint."""
    words = [
        '富强', '民主', '文明', 'the', 'flask', 'jsondash', 'graphs',
        'charts', 'd3', 'js', 'dashboards', 'c3','最近', '数据大屏', '可视化项目','项目',
        '要求', '形式', '直观', '展示', '业务数据', '绘制', '地图'
        ]
    sizes = range(len(words))
    data = [
        {
            'text': word,
            'size': rr(2,20) * 12
        }
        for i, word in enumerate(words)
    ]
    return jsonify(data)



@app.route('/sigma')
def sigma():
    """Fake endpoint."""
    chart_name = request.args.get('name', 'basic')
    if chart_name == 'random':
        nodes = request.args.get('nodes', 'abcdefghij')
        _vertices = list(nodes)
        _edges = combinations(_vertices, 2)
        edges, vertices = [], []
        for (frm, to) in _edges:
            edges.append(dict(
                id='{}-{}'.format(frm, to),
                color=rand_hex_color(),
                source=frm,
                target=to,
                size=rr(1, 10),
                x=rr(1, 100),
                y=rr(1, 100),
            ))
        for vertex in _vertices:
            vertices.append(dict(
                id=vertex,
                size=rr(10, 100),
                x=rr(1, 1000),
                y=rr(1, 100),
                color=rand_hex_color(),
                label='node {}'.format(vertex),
            ))
        data = dict(
            nodes=vertices,
            edges=edges,
        )
        return jsonify(data)
    filename = '{}/examples/sigma/{}.json'.format(cwd, chart_name)
    try:
        with open(filename, 'r') as chartjson:
            return chartjson.read()
    except IOError:
        pass
    return jsonify({})



@app.route('/flamegraph')
def flamegraph():
    """Fake endpoint."""
    chart_name = request.args.get('name', 'stacks')
    filename = '{}/examples/flamegraph/{}.json'.format(cwd, chart_name)
    try:
        with open(filename, 'r') as chartjson:
            return chartjson.read()
    except IOError:
        pass
    return jsonify({})



@app.route('/cytoscape')
def cytoscape():
    """Fake endpoint.

    Reads data from a local cytoscape spec, and if there is a
    remote url specified, (assuming it exists here), open and load it as well.

    This returns all required json as a single endpoint.
    """
    chart_name = request.args.get('name', 'basic')
    filename = '{}/examples/cytoscape/{}.json'.format(cwd, chart_name)
    try:
        with open(filename, 'r') as chartjson:
            return chartjson.read()
    except IOError:
        pass
    return jsonify({})



@app.route('/vegalite')
def vegalite():
    """Fake endpoint.

    Reads data from a local vega spec, and if there is a
    remote url specified, (assuming it exists here), open and load it as well.

    This returns all required json as a single endpoint.
    """
    chart_type = request.args.get('type', 'bar')
    filename = '{}/examples/vegalite/{}.json'.format(cwd, chart_type)
    print(filename,'--------------------')
    try:
        with open(filename, 'r') as chartjson:
            chartjson = chartjson.read()
            data = json.loads(chartjson)
            if data.get('data', {}).get('url') is not None:
                datapath = '{}/examples/vegalite/{}'.format(
                    cwd, data['data']['url']
                )
                with open(datapath, 'r') as datafile:
                    if datapath.endswith('.json'):
                        raw_data = datafile.read()
                        raw_data = json.loads(raw_data)
                    # TODO: adding csv support for example.
                    data.update(data=dict(
                        name='some data',
                        values=raw_data,
                    ))
                    return jsonify(data)
            else:
                return chartjson
    except IOError:
        pass
    return jsonify({})



@app.route('/plotly')
def plotly():
    """Fake endpoint."""
    chart_type = request.args.get('chart', 'scatter3d')
    filename = '{}/examples/plotly/{}.json'.format(cwd, chart_type)
    with open(filename, 'r') as chartjson:
        data=chartjson.read()
        print('============')
        print(type(json.loads(data)))
        data= json.loads(data)
        # if not(chart_type in ['polar','heatmap']):
        #     data['data'][0]['y']=rr_list(len(data['data'][0]['y']))
        return data
    return jsonify({})



@app.route('/plotly-dynamic')
def plotly_dynamic():
    """Fake endpoint."""
    filename = '{}/examples/plotly/bar_line_dynamic.json'.format(cwd)
    with open(filename, 'r') as chartjson:
        return chartjson.read()
    return jsonify({})



@app.route('/timeline')
def timeline():
    """Fake endpoint."""
    with open('{}/examples/timeline3.json'.format(cwd), 'r') as timelinejson:
        return timelinejson.read()
    return jsonify({})


@app.route('/dtable', methods=['GET'])
def dtable():
    """Fake endpoint."""
    if 'stress' in request.args:
        return jsonify([
            dict(
                foo=rr(1, 1000),
                bar=rr(1, 1000),
                baz=rr(1, 1000),
                quux=rr(1, 1000)) for _ in range(STRESS_MAX_POINTS)
        ])
    fname = 'dtable-override' if 'override' in request.args else 'dtable'
    with open('{}/examples/{}.json'.format(os.getcwd(), fname), 'r') as djson:
        return djson.read()
    return jsonify({})



@app.route('/timeseries')
def timeseries():
    """Fake endpoint."""
    return jsonify({
        "dates": dates_list(),
        "line1": rr_list(max_range=10),
        "line2": rr_list(max_range=10),
        "line3": rr_list(max_range=10),
    })



@app.route('/custom')
def custompage():
    """Fake endpoint."""
    kwargs = dict(number=rr(1, 1000))
    return render_template('examples/custom.html', **kwargs)

@app.route('/number')
def number():
    """Fake endpoint."""
    return dict(number=rr(1, 1000))



@app.route('/gauge')
def gauge():
    """Fake endpoint."""
    return jsonify({'data': rr(1, 100)})



@app.route('/area-custom')
def area_custom():
    """Fake endpoint."""
    return jsonify({
        "data": {
            "columns": [
                ["data1", 300, 350, 300, 0, 0, 0],
                ["data2", 130, 100, 140, 200, 150, 50]
            ],
            "types": {
                "data1": "area",
                "data2": "area-spline"
            }
        }
    })



@app.route('/scatter')
def scatter():
    """Fake endpoint."""
    if 'override' in request.args:
        with open('{}/examples/overrides.json'.format(cwd), 'r') as jsonfile:
            return jsonfile.read()
    return jsonify({
        "bar1": [1, 2, 30, 12, 100],
        "bar2": rr_list(max_range=40),
        "bar3": rr_list(max_range=40),
        "bar4": [-10, 1, 5, 4, 10, 20],
    })



@app.route('/pie')
def pie():
    """Fake endpoint."""
    letters = list('abcde')
    if 'stress' in request.args:
        letters = range(STRESS_MAX_POINTS)
    return jsonify({'data {}'.format(name): rr(1, 100) for name in letters})



@app.route('/custom-inputs')
def custom_inputs():
    """Fake endpoint."""
    _range = int(request.args.get('range', 5))
    entries = int(request.args.get('entries', 3))
    starting = int(request.args.get('starting_num', 0))
    prefix = request.args.get('prefix', 'item')
    if 'override' in request.args:
        show_axes = request.args.get('show_axes', False)
        show_axes = show_axes == 'on'
        data = dict(
            data=dict(
                columns=[
                    ['{} {}'.format(prefix, i)] + rr_list(max_range=entries)
                    for i in range(starting, _range)
                ],
            )
        )
        if show_axes:
            data.update(axis=dict(
                x=dict(label='This is the X axis'),
                y=dict(label='This is the Y axis')))
        return jsonify(data)
    return jsonify({
        i: rr_list(max_range=_range) for i in range(starting, entries)
    })



@app.route('/bar')
def barchart():
    """Fake endpoint."""
    if 'stress' in request.args:
        return jsonify({
            'bar-{}'.format(k): rr_list(max_range=STRESS_MAX_POINTS)
            for k in range(STRESS_MAX_POINTS)
        })
    return jsonify({
        "bar1": [1, 2, 30, 12, 100],
        "bar2": rr_list(max_range=5),
        "bar3": rr_list(max_range=5),
          "x": [
            "1960-28-20", 
            "1932-16-11", 
            "1998-30-25", 
            "1916-20-21"
          ]
    })


@app.route('/bar1')
def bar1():
    """Fake endpoint."""
    return jsonify(dict(
        dates=['a','ee','ff','d'],
        abc=rr_list(max_range=4),
        cde=rr_list(max_range=4),
    ))

@app.route('/line')
def linechart():
    """Fake endpoint."""
    if 'stress' in request.args:
        return jsonify({
            'bar-{}'.format(k): rr_list(max_range=STRESS_MAX_POINTS)
            for k in range(STRESS_MAX_POINTS)
        })
    return jsonify({
        "line1": [1, 4, 3, 10, 12, 14, 18, 10],
        "line2": [1, 2, 10, 20, 30, 6, 10, 12, 18, 2],
        "line3": rr_list(),
    })



@app.route('/shared')
def shared_data():
    """Fake endpoint to demonstrate sharing data from one source."""
    letters = list('abcde')
    piedata = {'data {}'.format(name): rr(1, 100) for name in letters}
    bardata = {
        "bar1": [1, 2, 30, 12, 100],
        "bar2": rr_list(max_range=5),
        "bar3": rr_list(max_range=5),
    }
    linedata = {
        "line1": [1, 4, 3, 10, 12, 14, 18, 10],
        "line2": [1, 2, 10, 20, 30, 6, 10, 12, 18, 2],
        "line3": rr_list(),
    }
    return jsonify({
        'multicharts': {
            'line': linedata,
            'bar': bardata,
            'pie': piedata,
        }
    })



@app.route('/singlenum')
def singlenum():
    """Fake endpoint."""
    _min, _max = 10, 10000
    if 'sales' in request.args:
        val = locale.currency(float(rr(_min, _max)), grouping=True)
    else:
        val = rr(_min, _max)
    if 'negative' in request.args:
        val = '-{}'.format(val)
    return jsonify(data=val)



@app.route('/deadend')
def test_die():
    """Fake endpoint that ends in a random 50x error."""
    # Simulate slow connection
    sleep = request.args.get('sleep', True)
    if sleep != '':
        sleep_for = request.args.get('sleep_for')
        time.sleep(int(sleep_for) if sleep_for is not None else random())
    err_code = request.args.get('error_code')
    rand_err = choice([500, 501, 502, 503, 504])
    abort(int(err_code) if err_code is not None else rand_err)



@app.route('/venn')
def test_venn():
    """Fake endpoint."""
    data = [
        {'sets': ['A'], 'size': rr(10, 100)},
        {'sets': ['B'], 'size': rr(10, 100)},
        {'sets': ['C'], 'size': rr(10, 100)},
        {'sets': ['A', 'B'], 'size': rr(10, 100)},
        {'sets': ['A', 'B', 'C'], 'size': rr(10, 100)},
    ]
    return jsonify(data)



@app.route('/sparklines', methods=['GET'])
def sparklines():
    """Fake endpoint."""
    if any([
        'pie' in request.args,
        'discrete' in request.args,
    ]):
        return jsonify([rr(1, 100) for _ in range(10)])
    return jsonify([[i, rr(i, 100)] for i in range(10)])



@app.route('/circlepack', methods=['GET'])
def circlepack():
    """Fake endpoint."""
    if 'stress' in request.args:
        # Build a very large dataset
        return jsonify(recursive_d3_data())
    # with open('{}/examples/flare.json'.format(cwd), 'r') as djson:
    #     return djson.read()
    js={
     "name": "flare",
     "children": [
      {
       "name": "analytics",
       "children": [
        {
         "name": "cluster",
         "children": [
          {"name": "AgglomerativeCluster", "size": rr(100, 1000)},
          {"name": "CommunityStructure", "size": rr(100, 1000)},
          {"name": "HierarchicalCluster", "size": rr(100, 1000)},
          {"name": "MergeEdge", "size": rr(100, 1000)}
         ]
        },
        {
         "name": "graph",
         "children": [
          {"name": "BetweennessCentrality", "size": rr(100, 1000)},
          {"name": "LinkDistance", "size": rr(100, 1000)},
          {"name": "MaxFlowMinCut", "size": rr(100, 1000)},
          {"name": "ShortestPaths", "size": rr(100, 1000)},
          {"name": "SpanningTree", "size": rr(100, 1000)}
         ]
        },
        {
         "name": "optimization",
         "children": [
          {"name": "AspectRatioBanker", "size": rr(100, 1000)}
         ]
        }
       ]
      },
      {
       "name": "animate",
       "children": [
        {"name": "Easing", "size": rr(100, 1000)},
        {"name": "FunctionSequence", "size": rr(100, 1000)},
        {
         "name": "interpolate",
         "children": [
          {"name": "ArrayInterpolator", "size": rr(100, 1000)},
          {"name": "ColorInterpolator", "size": rr(100, 1000)},
          {"name": "DateInterpolator", "size": rr(100, 1000)},
          {"name": "Interpolator", "size": rr(100, 1000)},
          {"name": "MatrixInterpolator", "size": rr(100, 1000)},
          {"name": "NumberInterpolator", "size": rr(100, 1000)},
          {"name": "ObjectInterpolator", "size": rr(100, 1000)},
          {"name": "PointInterpolator", "size": rr(100, 1000)},
          {"name": "RectangleInterpolator", "size": rr(100, 1000)}
         ]
        },
        {"name": "ISchedulable", "size": rr(100, 1000)},
        {"name": "Parallel", "size": rr(100, 1000)},
        {"name": "Pause", "size": rr(100, 1000)},
        {"name": "Scheduler", "size": rr(100, 1000)},
        {"name": "Sequence", "size": rr(100, 1000)},
        {"name": "Transition", "size": rr(100, 1000)},
        {"name": "Transitioner", "size": rr(100, 1000)},
        {"name": "TransitionEvent", "size": rr(100, 1000)},
        {"name": "Tween", "size": rr(100, 1000)}
       ]
      }
      ]
      }
    return jsonify(js)



@app.route('/treemap', methods=['GET'])
def treemap():
    """Fake endpoint."""
    if 'stress' in request.args:
        # Build a very large dataset
        return jsonify(recursive_d3_data())
    with open('{}/examples/flare.json'.format(cwd), 'r') as djson:
        return djson.read()
    return jsonify({})



@app.route('/map', methods=['GET'])
def datamap():
    """Fake endpoint."""
    return render_template('examples/map.html')



@app.route('/dendrogram', methods=['GET'])
def dendro():
    """Fake endpoint."""
    if 'stress' in request.args:
        # Build a very large dataset
        return jsonify(recursive_d3_data())
    filename = 'flare-simple' if 'simple' in request.args else 'flare'
    with open('{}/examples/{}.json'.format(cwd, filename), 'r') as djson:
        return djson.read()
    return jsonify({})



@app.route('/voronoi', methods=['GET'])
def voronoi():
    """Fake endpoint."""
    w, h = request.args.get('width', 800), request.args.get('height', 800)
    max_points = int(request.args.get('points', 100))
    if 'stress' in request.args:
        max_points = 500
    return jsonify([[rr(1, h), rr(1, w)] for _ in range(max_points)])



@app.route('/digraph', methods=['GET'])
def graphdata():
    """Fake endpoint."""
    if 'filetree' in request.args:
        with open('{}/examples/filetree_digraph.dot'.format(cwd), 'r') as dot:
            return jsonify(dict(graph=dot.read()))
    if 'simple' in request.args:
        graphdata = """
        digraph {
            a -> b;
            a -> c;
            b -> c;
            b -> a;
            b -> b;
        }
        """
        return jsonify(dict(graph=graphdata))
    nodes = list('abcdefghijkl')
    node_data = '\n'.join([
        '{0} -> {1};'.format(choice(nodes), choice(nodes))
        for _ in range(10)
    ])
    graphdata = """digraph {lb} {nodes} {rb}""".format(
        lb='{', rb='}', nodes=node_data)
    return jsonify(dict(
        graph=graphdata,
    ))
