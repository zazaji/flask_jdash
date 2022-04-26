import settings

from flask import (Blueprint, request,
    Flask,
    abort,
    request,
    jsonify,
    render_template,
)
app = Blueprint('example',__name__)

@app.route('/chartit', methods=['GET'])
def chartit():

    # modules=[
    # # {'name': 'chart', 'type': 'line', 'family': 'C3', 'width': 'col-3', 'height': 400, 'dataSource': 'http://127.0.0.1:8080/api/timeseriesc3', 'override': False, 'order': 3, 'refresh': True, 'refreshInterval': 5000, 'classes': [], 'row': 1, 'guid': 'f74a7ab3-2289-a705-0de3-d6e8e390134a', 'cachedData': None},
    # #  {'name': 'bar', 'type': 'bar', 'family': 'C3', 'width': 'col-4', 'height': 400, 'dataSource': 'http://127.0.0.1:8080/api/timeseriesc3', 'override': False, 'order': 2, 'refresh': False, 'refreshInterval': None, 'classes': [], 'row': 1, 'guid': '735f6525-221e-d1da-9e5a-571af513650a', 'cachedData': None},
    # #  {'name': '生产主页xc', 'type': 'flamegraph', 'family': 'FlameGraph', 'width': 'col-3', 'height': 400, 'dataSource': 'http://127.0.0.1:8080/api/flamegraph', 'override': False, 'order': 1, 'refresh': True, 'refreshInterval': 50000, 'classes': [], 'row': 1, 'guid': 'fbe2869d-f040-dfb3-147d-f0dc536a72bc', 'cachedData': None},
    #  {'name': '词云图', 'type': 'wordcloud', 'family': 'WordCloud', 'width': 'col-2', 'height': 400, 'dataSource': 'http://127.0.0.1:8080/api/wordcloud', 'override': False, 'order': 0, 'refresh': True, 'refreshInterval': None, 'classes': [], 'row': 1, 'guid': 'ec876e3f-a04e-8f80-1845-710f12d3d17e'}
    #  ]
    modules=[
                {
                    "name": "柱状图",
                    "type": "bar",
                    "family": "C3",
                    "width": "col-4",
                    "height": 400,
                    "dataSource": "http://127.0.0.1:8080/api/timeseriesc3",
                    "override": False,
                    "order": 1,
                    "refresh": True,
                    "refreshInterval": 5000,
                    "classes": [],
                    "guid": "07b37e5c-28b7-2f79-1d1f-b4999ac91643"
                },
                {
                    "name": "词云图",
                    "type": "wordcloud",
                    "family": "WordCloud",
                    "width": "col-4",
                    "height": 400,
                    "dataSource": "http://127.0.0.1:8080/api/wordcloud",
                    "override": False,
                    "order": 0,
                    "refresh": True,
                    "refreshInterval": 6000,
                    "classes": [],
                    "guid": "33d0293a-b798-909d-8207-0e65808bf225"
                }
            ]
    viewjson={
            "name": "这是一个动态仪表板",
            "slogan": "可以自由创建你所需要的视图组合",
            "modules": modules,
            "date": "2022-03-31 16:17:20.235000",
            "id": "91279fca-b0bc-11ec-b16c-005056c00008",
            "layout": "grid",
            "created_by": "anonymous",
            "username": "anonymous"
        }



    if 'modules' not in viewjson:
        flash('Invalid configuration - missing modules.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    active_charts = [v.get('family') for v in viewjson['modules']
                     if v.get('family') is not None]
    can_edit = True
    layout_type = viewjson.get('layout', 'freeform')
    kwargs = dict(
        id=23,
        view=viewjson,
        num_rows=( None  ),
        modules=viewjson['modules'],
        assets=settings.get_active_assets(active_charts),
        can_edit=can_edit,
        can_edit_global=1,
        is_global=1,
    )
    
    return render_template('render/charts.html', **kwargs)
