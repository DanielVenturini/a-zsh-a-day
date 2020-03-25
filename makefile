all: create_config deps compile

deps:
	pip3 install -r requirements.txt

compile:
	pyinstaller zsh-day.py -y --onefile

create_config:
	cp .zshday ~/.zshday

cron_script:
	sh cron_script.sh

install:
	cp dist/zsh-day /usr/bin/ -r

clean:
	rm dist/ -r
	rm build/ -r
	rm zsh-day.spec

remove:
	rm ~/.zshday -r
	rm /usr/bin/zsh-day