import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output, State
#import plotly.graph_objects as do
from app import app
#from data import data_parse
#import os

layout = html.Div(
	[
	dbc.Row([
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id="card1",responsive=True,config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'40vh'}, md=4),
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id="card2",responsive=True,config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'40vh'}, md=4),
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id="card3",responsive=True,config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'40vh'}, md=4),
	]),
	dbc.Row([
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='mini-table',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'50vh'}, md=4),
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='map',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'50vh'}, md=8)

	], className='mt-4'),
	]
)


