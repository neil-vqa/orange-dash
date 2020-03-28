import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as do
from app import app
from data import data_parse

layout = dcc.Loading(html.Div(
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
			dbc.Col(dbc.Row(
					[dcc.Graph(id="card3",responsive=True,config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),
					dcc.Interval(id="interval-component",interval=2*60*1000,n_intervals=0)]
					,style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'40vh'}, md=4),
	]),
	dbc.Row([
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='left-chart',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'50vh'}, md=4),
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='wide-chart',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#fef5ed','height':'100%'})
		],style={'height':'50vh'}, md=8)

	], className='mt-4'),
	]
),type='graph',color='#38b44a')
		     
@app.callback(
	[Output('card1','figure'),
	Output('card2','figure'),
	Output('card3','figure'),
	Output('left-chart','figure'),
	Output('wide-chart','figure')],
	[Input('interval-component', 'n_intervals')]
)
def update_charts(n_intervals):
	data1,data2,data3,symbol = data_parse()
	
	plot1 = do.Figure(do.Scatter(
			x= data1.index,
			y= data1['Close'],
			name='Close',
			#fill='tozeroy',
			mode='lines',
			marker_color='#38b44a'))
			
	plot1.add_trace(
		do.Scatter(
			x= data1.index,
			y= data1['Close'].rolling(window=60).mean(),
			name='MA (window=60)',
			mode='lines',
			marker_color='#17a2b8'
		)
	)
			
	plot2 = do.Figure(do.Scatter(
			x= data2.index,
			y= data2['Close'],
			name='Close',
			#fill='tozeroy',
			mode='lines',
			marker_color='#38b44a'))
	
	plot2.add_trace(
		do.Scatter(
			x= data2.index,
			y= data2['Close'].rolling(window=60).mean(),
			name='MA (window=60)',
			mode='lines',
			marker_color='#17a2b8'
		)
	)
			
	plot3 = do.Figure(do.Scatter(
			x= data3.index,
			y= data3['Close'],
			name='Close',
			#fill='tozeroy',
			mode='lines',
			marker_color='#38b44a'))
			
	plot3.add_trace(
		do.Scatter(
			x= data3.index,
			y= data3['Close'].rolling(window=60).mean(),
			name='MA (window=60)',
			mode='lines',
			marker_color='#17a2b8'
		)
	)
	
	plot1.update_yaxes(showgrid=True,gridcolor='#cfcbc7',gridwidth=0.5)
	plot1.update_layout(margin= do.layout.Margin(t=60,b=30,r=25,l=15),
					title='{}'.format(symbol[0]), showlegend=False, plot_bgcolor='#ffffff', hovermode='x')
	
	plot2.update_yaxes(showgrid=True,gridcolor='#cfcbc7',gridwidth=0.5)
	plot2.update_layout(margin= do.layout.Margin(t=60,b=30,r=25,l=15),
					title='{}'.format(symbol[1]), showlegend=False, plot_bgcolor='#ffffff', hovermode='x')
	
	plot3.update_yaxes(showgrid=True,gridcolor='#cfcbc7',gridwidth=0.5)				
	plot3.update_layout(margin= do.layout.Margin(t=60,b=30,r=25,l=15),
					title='{}'.format(symbol[2]), showlegend=False, plot_bgcolor='#ffffff', hovermode='x')
	
	plot4 = do.Figure(do.Scatter(
			x= data1.index,
			y= data1['Close']/data1['Close'].iloc[0],
			name='{}'.format(symbol[0]),
			mode='lines',
			marker_color='#f08f6d'))
	
	plot4.add_trace(
		do.Scatter(
			x= data2.index,
			y= data2['Close']/data2['Close'].iloc[0],
			name='{}'.format(symbol[1]),
			mode='lines',
			marker_color='#cac5c0'
		)
	)
	
	plot4.add_trace(
		do.Scatter(
			x= data3.index,
			y= data3['Close']/data3['Close'].iloc[0],
			name='{}'.format(symbol[2]),
			mode='lines',
			marker_color='#f4d081'
		)
	)
	
	plot4.update_layout(margin= do.layout.Margin(t=60,b=30,r=25,l=15),
					title='Price Evolution', showlegend=False, plot_bgcolor='#ffffff', hovermode='x')
	
	plot5 = do.Figure(do.Scatter(
			x= data1.index,
			y= (data1['Close']/data1['Close'].shift(1)) - 1,
			name='{}'.format(symbol[0]),
			mode='lines',
			marker_color='#f08f6d'))
	
	plot5.add_trace(
		do.Scatter(
			x= data2.index,
			y= (data2['Close']/data2['Close'].shift(1)) - 1,
			name='{}'.format(symbol[1]),
			mode='lines',
			marker_color='#cac5c0'
		)
	)
	
	plot5.add_trace(
		do.Scatter(
			x= data3.index,
			y= (data3['Close']/data3['Close'].shift(1)) - 1,
			name='{}'.format(symbol[2]),
			mode='lines',
			marker_color='#f4d081'
		)
	)
	
	
	plot5.update_layout(margin= do.layout.Margin(t=60,b=30,r=25,l=15),
					title='Returns', showlegend=False, plot_bgcolor='#ffffff', hovermode='x')
	
	return plot1,plot2,plot3,plot4,plot5
