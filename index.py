import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app, server
from apps import home, technical, resources, login
from flask_login import logout_user, current_user


sidebar_header = dbc.Row(
	[
		dbc.Col(html.H5("An Orange, Inc.", className="h5", style={'color':'#ffffff'})),
		dbc.Col(
			html.Button(
				html.Span(className="navbar-toggler-icon"),
				className="navbar-toggler",
				style={"color": "rgba(0,0,0,.5)","border-color": "rgba(250,250,250,.3)"},
				id="toggle",
			),
			width="auto",
			align="center",
		),
	]
)

sidebar = html.Div(
    [
        sidebar_header,
        html.Div(
            [
                html.Hr(style={'borderColor':'#ffffff'}),
            ],
            id="blurb",
        ),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink([html.I(id='home-button',className='fas fa-chart-line fa-3x')], href="/home", id="page-1-link",style={'color':'#ffffff'}),
                    dbc.NavLink([html.I(id='technical-button',className='fas fa-file-alt fa-3x')], href="/apps/technical", id="page-2-link",style={'color':'#ffffff'}),
                    dbc.NavLink([html.I(id='resources-button',className='fas fa-info-circle fa-3x')], href="/apps/resources", id="page-3-link",style={'color':'#ffffff'}),
                    dbc.NavLink([html.I(id='logout-button',className='fas fa-sign-out-alt fa-2x')], href="/logout", id="logout-link",style={'color':'#ffffff'}, className='mt-5'),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
    style={'backgroundColor':'#e95420'}
)

content = html.Div(id="page-content", style={'backgroundColor':'#cac5c0',})


def serve_layout():
	return html.Div([dcc.Location(id="url"), sidebar, content])

app.layout = serve_layout

# active pill
@app.callback(
	[Output(f"page-{i}-link", "active") for i in range(1, 4)],
	[Input("url", "pathname")],
)
def toggle_active_links(pathname):
	if pathname == "/home":
		return True, False, False
	return [pathname == "/home", pathname == "/apps/technical", pathname == "/apps/resources"]
    
# toggle -- side bar when hidden (interaction)
@app.callback(
	Output("collapse", "is_open"),
	[Input("toggle", "n_clicks")],
	[State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
	if n:
		return not is_open
	return is_open

# this is where linking to other apps happen
@app.callback(
	Output("page-content", "children"), 
	[Input("url", "pathname")]
)
def render_page_content(pathname):
#	if pathname == "/home":
#		if current_user.is_authenticated:
#			return home.layout
#		else:
#			return login.layout   
#	elif pathname == "/apps/technical":
#		if current_user.is_authenticated:
#			return technical.layout
#		else:
#			return login.layout
#	elif pathname == "/apps/resources":
#		if current_user.is_authenticated:
#			return resources.layout
#		else:
#			return login.layout
#	elif pathname == '/logout':
#		if current_user.is_authenticated:
#			logout_user()
#			return login.layout
#		else:
#			return login.layout
#	else:
#		return login.layout
		
	if current_user.is_authenticated:
		if pathname == "/home":
			return home.layout
		elif pathname == "/apps/technical":
			return technical.layout
		elif pathname == "/apps/resources":
			return resources.layout
		elif pathname == '/logout':
			logout_user()
			return login.layout
	else:
		return login.layout


if __name__ == "__main__":
    app.run_server(debug=True)
