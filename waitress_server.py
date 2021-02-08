from waitress import serve
import app
serve(app.app, port=9000)
