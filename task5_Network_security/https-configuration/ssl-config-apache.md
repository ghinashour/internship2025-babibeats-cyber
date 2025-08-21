# SSL Configuration for Apache

## Installing SSL Certificate

### 1. Install Apache and SSL module

```bash
sudo apt update
sudo apt install apache2
sudo a2enmod ssl
sudo systemctl restart apache2
```

### 2.Create ssl directory

```bash
sudo mkdir /etc/apache2/ssl
```

### 3.Generate Self-Signed Certificate (for testing)

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/apache2/ssl/apache.key \
  -out /etc/apache2/ssl/apache.crt
```

### 4. Configure Apache SSL Site

Edit /etc/apache2/sites-available/default-ssl.conf:
<IfModule mod_ssl.c>
<VirtualHost _default_:443>
ServerAdmin webmaster@localhost
DocumentRoot /var/www/html

        SSLEngine on
        SSLCertificateFile /etc/apache2/ssl/apache.crt
        SSLCertificateKeyFile /etc/apache2/ssl/apache.key

        <FilesMatch "\.(cgi|shtml|phtml|php)$">
            SSLOptions +StdEnvVars
        </FilesMatch>

        <Directory /usr/lib/cgi-bin>
            SSLOptions +StdEnvVars
        </Directory>
    </VirtualHost>

</IfModule>

### 5. Enable SSL Site and Restart

```bash
sudo a2ensite default-ssl
sudo systemctl restart apache2
```
