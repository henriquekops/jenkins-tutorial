from server import app

host = '0.0.0.0'
port = 8081
debug = True
if __name__ == '__main__':
	app.run(host, port, debug)
