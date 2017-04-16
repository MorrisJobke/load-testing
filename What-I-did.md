# replaced with my version with proper virtual hosts
sudo rm /etc/apache2/sites-enabled/nextcloud.conf

# add following to /etc/hosts (to test with their internal network)
127.0.0.1       status.local
1.2.3.4	locust1.local nextcloud-nfs.local
1.2.3.5	locust2.local nextcloud-os.local

# placed new nextcloud apache config
cat /etc/apache2/sites-enabled/nextcloud-virtual-host.conf

# set proper domain in config.php
/etc/apache2/sites-enabled/nextcloud.conf

# installing netdata for monitoring
curl -Ss 'https://raw.githubusercontent.com/firehol/netdata-demo-site/master/install-required-packages.sh' >/tmp/kickstart.sh && bash /tmp/kickstart.sh -i netdata-all
cd /opt
sudo git clone https://github.com/firehol/netdata.git --depth=1
cd netdata
sudo ./netdata-installer.sh

#  You are about to build and install netdata to your system.
#
#  It will be installed at these locations:
#
#   - the daemon     at /usr/sbin/netdata
#   - config files   in /etc/netdata
#   - web files      in /usr/share/netdata
#   - plugins        in /usr/libexec/netdata
#   - cache files    in /var/cache/netdata
#   - db files       in /var/lib/netdata
#   - log files      in /var/log/netdata
#   - pid file       at /var/run/netdata.pid
#   - logrotate file at /etc/logrotate.d/netdata

sudo killall netdata
sudo cp system/netdata.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable netdata
sudo service netdata start


# setup apache & mysql monitoring
sudo vim /etc/netdata/python.d.conf # uncomment mysql and apache
# update apache with proper status.local instead of localhost
sudo vim /etc/netdata/python.d/apache.conf
# set mysql settings
sudo mysql -u root
create user 'netdata'@'localhost';
grant usage on *.* to 'netdata'@'localhost' with grant option;
flush privileges;

# install blackfire for profiling
wget -O - https://packagecloud.io/gpg.key | sudo apt-key add -
echo "deb http://packages.blackfire.io/debian any main" | sudo tee /etc/apt/sources.list.d/blackfire.list
sudo apt-get update
sudo apt-get install blackfire-agent
sudo blackfire-agent -register
# enter ID and token here
sudo /etc/init.d/blackfire-agent restart
sudo apt-get install blackfire-php
sudo service apache2 restart

# install blackfire CLI
sudo apt-get install blackfire-agent

# create test files
dd if=/dev/urandom of=/tmp/sample-small.dat bs=756938 count=1 
dd if=/dev/urandom of=/tmp/sample-medium.dat bs=4569380 count=1
dd if=/dev/urandom of=/tmp/sample-large.dat bs=34549338 count=10