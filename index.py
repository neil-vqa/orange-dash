import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app, server
from apps import home, technical, resources, login
from flask_login import logout_user, current_user


sidebar_header = dbc.Row(
	[
		dbc.Col(html.H5(id="display-user", className="h5", style={'color':'#ffffff'})),
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
		html.Div(id='dummy',style={"display":"none"})
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
                    dbc.NavLink([html.I(id='home-button',className='fas fa-chart-line fa-3x', title='Dashboard Home')], href="/home", id="page-1-link",style={'color':'#ffffff'}),
                    dbc.NavLink([html.I(id='technical-button',className='fas fa-file-alt fa-3x', title='Technical')], href="/apps/technical", id="page-2-link",style={'color':'#ffffff'}),
                    dbc.NavLink([html.I(id='resources-button',className='fas fa-info-circle fa-3x', title='Resources')], href="/apps/resources", id="page-3-link",style={'color':'#ffffff'}),
                    dbc.NavLink([html.I(id='logout-button',className='fas fa-sign-out-alt fa-2x', title='Logout')], href="/logout", id="logout-link",style={'color':'#ffffff'}, className='mt-5'),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")


def serve_layout():
	return html.Div([dcc.Location(id="url"), sidebar, content], style={'backgroundColor':'#cac5c0'})

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
	[Output("sidebar",component_property='style'),
	Output("page-content", "children"),
	Output("display-user","children")], 
	[Input("url", "pathname")]
)
def render_page_content(pathname):
	default_name = "An Orange, Inc."	
	if current_user.is_authenticated:
		name = str(current_user.username)
		if pathname in ["/home","/"]:
			return {'backgroundColor':'#e95420'},home.layout, name
		elif pathname == "/apps/technical":
			return {'backgroundColor':'#e95420'},technical.layout, name
		elif pathname == "/apps/resources":
			return {'backgroundColor':'#e95420'},resources.layout, name
		elif pathname == '/logout':
			logout_user()
			return {'transform':'scale(0)'},login.layout, default_name
	else:
		return {'transform':'scale(0)'},login.layout, default_name


if __name__ == "__main__":
    app.run_server(debug=False)
