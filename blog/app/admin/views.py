from . import admin
@admin.route("/")
def index():
	return "<h1 style='color:red'>这是后台</h1>"