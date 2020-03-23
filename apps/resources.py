import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app


layout = dbc.Container([
	dbc.Row(
		dbc.Col(
			html.H1("Resources",className='mx-3 my-3')
		),
	),
	html.Hr(),
	dbc.Row([
		dbc.Col(
			dbc.Col([
				html.H4("Financial Analysis"),
				html.P(["Python for Finance — Stock Price Trend Analysis", html.Br(),"Jose Manu", html.Br(),
						"Source: https://towardsdatascience.com/python-python-for-finance-stock-price-trend-analysis-9111afc29259"]),
				html.P(["In 12 minutes: Stocks Analysis with Pandas and Scikit-Learn", html.Br(),"Vincent Tatan", html.Br(),
						"Source: https://towardsdatascience.com/in-12-minutes-stocks-analysis-with-pandas-and-scikit-learn-a8d8a7b50ee7"]),
			])
		)
	],
	className='mt-3 mx-md-3'),
	dbc.Row([
		dbc.Col(
			dbc.Col([
				html.H4("Data Source"),
				html.P(["All data used in analysis and visualizations are pulled from Yahoo! Finance.", html.Br(),
						"Source: https://finance.yahoo.com/"])
			])
		)
	],
	className='mt-3 mx-md-3'),
	dbc.Row([
		dbc.Col(
			dbc.Col([
				html.H4("Terms of Use"),
				html.P(["""All information featured in this dashboard are strictly for educational use only.
						Using this as a main resource for financial decision-making is highly discouraged.
						Commercial use is strictly prohibited."""])
			])
		)
	],
	className='mt-3 mx-md-3'),
	dbc.Row([
		dbc.Col(
			dbc.Col([
				html.H4("Contact"),
				html.P(["For concerns, suggestions, comments, and/or complaints, please contact the developer.", html.Br(),
						"Developer: Neil Alino", html.Br(), "Email: nvqa.business@gmail.com"])
			])
		)
	],
	className='mt-3 mx-md-3'),
	
	
],
className='shadow-lg rounded',
style={'backgroundColor':'#ffffff'})


