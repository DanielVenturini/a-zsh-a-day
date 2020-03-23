import os
import json

# return the absolute path of zsh config file
# '/home/venturini/.zshrc', eg.
def get_path(file):
	home_path  = os.getenv('HOME')
	return os.path.join(home_path, file)

# open the ~/.zshrc or ~/.zshday
def open_file(file):
	path = get_path(file)
	return open(path)

# read the ~/.zshday and return the new theme
# also, update the ~/.zshday file
def get_theme(zshday_file):
	zshday_obj = json.load(zshday_file)
	try:
		theme_number = zshday_obj['theme_of_day']
		# at the end of themes, come back to first theme
		zshday_obj['theme_of_day'] = (theme_number + 1) % len(zshday_obj['themes'])
		return zshday_obj['themes'][theme_number]
	except Exception as ex:
		print(str(ex))
		exit(1)
	finally:
		# before go out the function, update the .zshday file
		json.dump(zshday_obj, open(get_path('./.zshday'), 'w'))

def update_theme(zshrc_file, new_theme):
	pass

# open the ~/.zshrc file and the ~/.zshday file
# then select and change the theme name
def worker():
	try:
		zshrc_file  = open_file('.zshrc')
		zshday_file = open_file('.zshday')

		new_theme = get_theme(zshday_file)
		update_theme(zshrc_file, new_theme)
	except FileNotFoundError as ex:
		print(str(ex))

if __name__.__eq__('__main__'):
	worker()