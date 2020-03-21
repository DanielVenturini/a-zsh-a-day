import os

# return the absolute path of zsh config file
# '/home/venturini/.zshrc', eg.
def get_path(file):
	home_path  = os.getenv('HOME')
	return os.path.join(home_path, file)

# open the ~/.zshrc or ~/.zshday
def open_file(file):
	path = get_path(file)
	return open(path)

# open the ~/.zshrc file and the ~/.zshday file
# then select and change the theme name
def worker():
	try:
		zshrc_file  = open_file('.zshrc')
		zshday_file = open_file('.zshday')
	except FileNotFoundError as ex:
		print(str(ex))

if __name__.__eq__('__main__'):
	worker()