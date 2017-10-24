import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def dispatcher(app, request):
    params = {
        'data': request.body,
        'method': request.method,
        'content_type': request.content_type
    }
    with app.server.test_request_context(request.path, **params):
        app.server.preprocess_request()
        try:
            response = app.server.full_dispatch_request()
        except Exception as e:
            response = app.server.make_response(app.server.handle_exception(e))
        return response.get_data()


def create_app(request):

    app = dash.Dash(url_base_pathname="/models/")

    df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/'
        'cb5392c35661370d95f300086accea51/raw/'
        '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
        'indicators.csv')

    available_indicators = df['Indicator Name'].unique()

    server = app.server

    app.layout = html.Div([
        html.Div([

            html.Div([
                dcc.Dropdown(
                    id='xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Fertility rate, total (births per woman)'
                ),
                dcc.RadioItems(
                    id='xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ],
            style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id='yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Life expectancy at birth, total (years)'
                ),
                dcc.RadioItems(
                    id='yaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),

        dcc.Graph(id='indicator-graphic'),

        dcc.Slider(
            id='year--slider',
            min=df['Year'].min(),
            max=df['Year'].max(),
            value=df['Year'].max(),
            step=None,
            marks={str(year): str(year) for year in df['Year'].unique()}
        )
    ])

    @app.callback(
        dash.dependencies.Output('indicator-graphic', 'figure'),
        [dash.dependencies.Input('xaxis-column', 'value'),
         dash.dependencies.Input('yaxis-column', 'value'),
         dash.dependencies.Input('xaxis-type', 'value'),
         dash.dependencies.Input('yaxis-type', 'value'),
         dash.dependencies.Input('year--slider', 'value')])
    def update_graph(xaxis_column_name, yaxis_column_name,
                     xaxis_type, yaxis_type,
                     year_value):
        dff = df[df['Year'] == year_value]

        return {
            'data': [go.Scatter(
                x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
            'layout': go.Layout(
                xaxis={
                    'title': xaxis_column_name,
                    'type': 'linear' if xaxis_type == 'Linear' else 'log'
                },
                yaxis={
                    'title': yaxis_column_name,
                    'type': 'linear' if yaxis_type == 'Linear' else 'log'
                },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                hovermode='closest'
            )
        }

    return render(request, 'models/analyze/', {
        'my_data': app.index(),
    })
    #return HttpResponse(dispatcher(app, request), content_type= 'application/json')

