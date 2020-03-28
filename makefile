all: create_config deps compile
install: copy_exe anacron_script

deps:
	pip3 install -r requirements.txt

compile:
	pyinstaller zsh-day.py -y --onefile

create_config:
	cp .zshday ~/.zshday

anacron_script:
	echo '1\t0\tzsh-day\t/usr/bin/zsh-day' >> /etc/anacrontab

copy_exe:
	cp dist/zsh-day /usr/bin/ -r

clean:
	rm dist/ -r
	rm build/ -r
	rm zsh-day.spec

remove:
	rm ~/.zshday -r
	rm /usr/bin/zsh-day