/et/ssystemd/system/

vim uwsgi_gestao_rh.service

[Unit]
Description=uWSGI Emperor
After=syslog.target

[Service]
ExecStart=/home/ubuntu/venv/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid wwww-data
RuntimeDirectory=uwsgi
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User=ubuntu

[Install]
WantedBy=multi-user.target


sudo chmod -664 /etc/systemd/system/uwsgi_gestao_rh.service

sudo systemctl daemon-reload
sudo systemctl enable uwsgi_gestao_rh.service
sudo systemctl start uwsgi_gestao_rh.service
sudo systemctl status uwsgi_gestao_rh.service
sudo journalctl -u uwsgi_gestao_rh.service


