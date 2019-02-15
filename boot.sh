#!/bin/bash
if [ ! -d "$APACHE_RUN_DIR" ]; then
	mkdir "$APACHE_RUN_DIR"
	chown $APACHE_RUN_USER:$APACHE_RUN_GROUP "$APACHE_RUN_DIR"
fi
if [ -f "$APACHE_PID_FILE" ]; then
	rm "$APACHE_PID_FILE"
fi

service ssh restart

curl http://192.168.1.56:5080/langdetect/ -H "Content-Type:application/json" -d '{"texto":"Mira que cosa más linda."}' -X POST -s

curl http://192.168.1.56:5080/postagging/ -H "Content-Type:application/json" \
-d '{"texto": "{\"1\":\"El\", \"2\":\"presidente\", \"3\":\"de\", \"4\":\"el\", \"5\":\"Barcelona\"}" }' -X POST -s

/usr/sbin/apache2ctl -D FOREGROUND