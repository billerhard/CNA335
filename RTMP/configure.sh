sudo apt install build-essential
sudo apt install libpcre3
sudo apt install libpcre3-dev
sudo apt install libssl-dev
sudo apt install zlib1g-dev
sudo apt install curl
wget http://nginx.org/download/nginx-1.15.1.tar.gz
wget https://github.com/sergey-dryabzhinsky/nginx-rtmp-module/archive/dev.zip
tar -zxvf nginx-1.15.1.tar.gz
unzip dev.zip
cd nginx-1.15.1
./configure --with-http_ssl_module --with-openssl=/usr/lib/ssl --add-module=../nginx-rtmp-module-dev
make
sudo make install
sudo /usr/local/nginx/sbin/nginx
curl http://127.0.0.1
