from . import home
@home.route("/")
def index():
	return "<h1 style='color:green'>这是前台</h1>"