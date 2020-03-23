import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app


layout = dbc.Container([
	dbc.Row(
		dbc.Col(
			html.H1("Technical Details",className='mx-3 my-3')
		),
	),
	html.Hr(),
	dbc.Row([
		dbc.Col(
			dbc.Col([
				html.P("""Each of the 3 charts of the upper section shows the intra-day price movement of MSFT, AAPL, and GOOGL
						respectively by 1-minute intervals."""),
				html.P("The Moving Average has a window = 60."),
				html.P("Note: All charts on the Dashboard Home section are automatically updated every 2 minutes.")
			]),
		md=6),
		dbc.Col(
			dbc.Col(
				html.Img(src=app.get_asset_url('msft.png'), style={'width':'90%'})
			),
		md=6)
	],
	className='mt-3 mx-md-3'),
	html.Hr(),
	dbc.Row([
		dbc.Col(
			dbc.Col([
				html.P("""This chart compares the price trend of the stocks. The metric was calculated by dividing each 
						stock's opening price by their succeeding price. A value greater than 1 indicates that the price
						has gone up relative to the opening price while a value lower than 1 indicates the price has declined.""")
			]),
		md=6),
		dbc.Col(
			dbc.Col(
				html.Img(src=app.get_asset_url('price-evo.png'), style={'width':'90%'})
			),
		md=6)
	],
	className='mt-3 mx-md-3'),
	html.Hr(),
	dbc.Row([
		dbc.Col(
			dbc.Col([
				html.P("""This chart presents the return rates for each stock.""")
			]),
		md=6),
		dbc.Col(
			dbc.Col(
				html.Img(src=app.get_asset_url('returns.png'), style={'width':'90%'})
			),
		md=6)
	],
	className='mt-3 mx-md-3'),
],
className='shadow-lg rounded',
style={'backgroundColor':'#ffffff'})












