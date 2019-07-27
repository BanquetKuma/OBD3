import dash
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_daq as daq
import os

df=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/OBD/master/OBD_GPS_CSV")
mapbox_access_token="pk.eyJ1IjoiYmFucXVldGt1bWEiLCJhIjoiY2p0YjZ4bGJ2MGlseTN5bzlxcnlsbW8xNCJ9.udbxOpc2gZQcUX4m1VIqBg"

app = dash.Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])
server = app.server

speed_count=500
nenpi_count=500
engine_load_count=500
engine_rotation_count=500
horse_power_count=500
intake_volume_count=500
O2_sensor_count=500
acceleration_count=500
map_count=500    #カウンター

app.layout = html.Div([
    html.H1("来来亭　桂川店　→　京都縦貫道　→　湯の花温泉"),
    dcc.Graph(id='kyoto-drive'),
    dcc.Interval(
        id='interval-component',
        interval=2*100,  # in milliseconds
        n_intervals=0), #公式ドキュメントより

    html.Div(
        daq.Gauge(
            id='my-speed-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='速度',
            labelPosition="bottom",
            units="km/h",
            min=0,
            max=100,
            size=200), style={'columnCount': 8, 'margin-left': '250px'}, className='one columns'),

    html.Div(
        daq.Gauge(
            id='my-nenpi-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='燃費',
            labelPosition="bottom",
            units="km/l",
            min=0,
            max=70,
            size=200), style={'columnCount': 8, 'margin-left': '150px'}, className='one columns'),

    html.Div(
        daq.Gauge(
            id='my-engine_load-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='エンジン負荷',
            labelPosition="bottom",
            units="%",
            min=0,
            max=100,
            size=200), style={'columnCount': 8, 'margin-left': '150px'}, className='one columns'),

    html.Div(
        daq.Gauge(
            id='my-engine_rotation-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='エンジン回転数',
            labelPosition="bottom",
            units="rpm",
            min=0,
            max=4000,
            size=200), style={'columnCount': 8, 'margin-left': '150px'}, className='one columns'),

    html.Div(
        daq.Gauge(
            id='my-horse_power-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='馬力',
            labelPosition="bottom",
            units="hp",
            min=0,
            max=100,
            size=200), style={'columnCount': 8, 'margin-left': '150px'}, className='one columns'),

    html.Div(
        daq.Gauge(
            id='my-intake_volume-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='吸気量',
            labelPosition="bottom",
            units="g/s",
            min=0,
            max=60,
            size=200), style={'columnCount': 8, 'margin-left': '150px'}, className='one columns'),

    html.Div(
        daq.Gauge(
            id='my-O2_sensor-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='O2センサ電流値',
            labelPosition="bottom",
            units="mA",
            min=0,
            max=2,
            size=200), style={'columnCount': 8, 'margin-left': '150px'}, className='one columns'),

    html.Div(
        daq.Gauge(
            id='my-acceleration-gauge',
            color="#9B51E0",
            showCurrentValue=True,
            label='加速度',
            labelPosition="bottom",
            units="m/s2",
            min=0,
            max=10,
            size=200), style={'columnCount': 8, 'margin-left': '150px'}, className='one columns')
])

@app.callback(
    dash.dependencies.Output('my-speed-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global speed_count
    if speed_count < 1728:
        speed_count+=1
        return df["速度 (km/h)"][speed_count-1]
    else:
        speed_count = 0
        update_output("n")

@app.callback(
    dash.dependencies.Output('my-nenpi-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global nenpi_count
    nenpi_count+=1
    if nenpi_count < 1728:
        return df["燃費 (km/l)"][nenpi_count - 1]
    else:
        nenpi_count = 0
        update_output("n")

@app.callback(
    dash.dependencies.Output('my-engine_load-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global engine_load_count
    engine_load_count+=1
    if engine_load_count < 1728:
        return df["エンジン負荷 (%)"][engine_load_count - 1]
    else:
        engine_load_count = 0
        update_output("n")

@app.callback(
    dash.dependencies.Output('my-engine_rotation-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global engine_rotation_count
    engine_rotation_count+=1
    if engine_rotation_count < 1728:
        return df["エンジン回転数 (rpm)"][engine_rotation_count - 1]
    else:
        engine_rotation_count = 0
        update_output("n")

@app.callback(
    dash.dependencies.Output('my-horse_power-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global horse_power_count
    horse_power_count+=1
    if horse_power_count < 1728:
        return df["馬力 (hp)"][horse_power_count - 1]
    else:
        horse_power_count = 0
        update_output("n")


@app.callback(
    dash.dependencies.Output('my-intake_volume-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global intake_volume_count
    intake_volume_count+=1
    if intake_volume_count < 1728:
        return df["吸気量 (g/s)"][intake_volume_count - 1]
    else:
        intake_volume_count = 0
        update_output("n")


@app.callback(
    dash.dependencies.Output('my-O2_sensor-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global O2_sensor_count
    O2_sensor_count+=1
    if O2_sensor_count < 1728:
        return df["O2センサ電流値 (mA)"][O2_sensor_count - 1]
    else:
        O2_sensor_count = 0
        update_output("n")


@app.callback(
    dash.dependencies.Output('my-acceleration-gauge','value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_output(n):
    global acceleration_count
    acceleration_count+=1
    if acceleration_count < 1728:
        return df["加速度 (m/s2)"][acceleration_count - 1]
    else:
        acceleration_count = 1
        update_output("n")


@app.callback(
    Output('kyoto-drive', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_figure(n):
    global map_count
    map_count += 1
    if map_count<1728:
        filtered_df = df[df["id"] == map_count]
        traces = []
        for i in filtered_df["id"]:
            traces.append(go.Scattermapbox(
                lat = df[df['id']== i]['緯度　(°)'],
                lon = df[df['id']== i]['経度　(°)'],
                mode = 'markers',
                marker = dict(size=df[df['id']== i]['速度 (km/h)'],color="#FF9999"))),
            return {
            'data': traces,
            'layout':go.Layout(
                autosize=True,
                hovermode='closest',
                mapbox = dict(
                    accesstoken=mapbox_access_token,
                    bearing = 0,
                    center = dict(
                        lat=35,
                        lon=135.65
                    ),
                    pitch = 90,
                    zoom=12,
                    ),
                height=900
            ) }

    else:
        map_count=0
        update_figure("n")

if __name__ == '__main__':
    app.run_server(debug=True)
