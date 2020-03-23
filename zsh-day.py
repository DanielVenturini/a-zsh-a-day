import os
import re
import json

# return the absolute path of zsh config file
# '/home/venturini/.zshrc', eg.
def get_path(file):
	home_path  = os.getenv('HOME')
	return os.path.join(home_path, file)

# open the ~/.zshrc or ~/.zshday
def open_file(file, mode='r'):
	path = get_path(file)
	return open(path, mode)

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
		json.dump(zshday_obj, open(get_path('.zshday'), 'w'), indent=True)

# read all .zshrc file
# re-write all lines at file
# when re-writing, replace the 'ZSH_THEME="*"'
# it's necessary because i'm reading and writing at same time in same file
def update_theme(zshrc_file_reader, new_theme):
	# read all zshrc lines
	lines = zshrc_file_reader.readlines()

	# open a new .zshrc file to write
	with open_file(get_path('.zshrc'), 'w') as zshrc_file_writer:

		for line in lines:
			# ignore all line that starts with comments "#"
			# and only verify others lines
			if not line.startswith('#') and re.match('ZSH_THEME="[\w-]+"\n', line):
				line = 'ZSH_THEME="{}"\n'.format(new_theme)

			zshrc_file_writer.write(line)


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