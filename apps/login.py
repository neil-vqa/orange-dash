import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import no_update
from dash.dependencies import Input, Output, State
from app import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash

layout = html.Div([
	       dcc.Location(id='login-url',refresh=True),
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H4('Login',className='card-title'),
                                    dbc.Input(id='login-email',placeholder='Email (try "admin@mail.com")'),
                                    dbc.Input(id='login-password',placeholder='Password (try "password")',type='password', className='mt-2'),
                                    dbc.Button('Submit',id='login-button',color='success',block=True, className='mt-4'),
                                ],
                                body=True
                            ),
                            md=6
                        ),
                        justify='center',
                        style = {'height':'94vh'}
                    )
                ]
            )	
])
@app.callback(
	Output('login-url','pathname'),
	[Input('login-button','n_clicks')],
	[State('login-email','value'),
	State('login-password','value')]
)
def success(n_clicks,email,password):
	user = User.query.filter_by(email=email).first()
	if user:
		if check_password_hash(user.password, password):
			login_user(user)
			return '/home'
		else:
			pass
	else:
		pass

