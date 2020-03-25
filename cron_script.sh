# get the previous crontabs and put it in a temp file
crontab -l > /tmp/crontab_zshday

# add the crontab commands to a-zsh-a-day in a temp file
echo '' >> /tmp/crontab_zshday
echo '# execute a-zsh-a-day at midnight' >> /tmp/crontab_zshday
echo '0 0 * * * /usr/bin/zsh-day' >> /tmp/crontab_zshday

# add the temp file to a crontab
crontab /tmp/crontab_zshday