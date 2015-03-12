ant=$(date -r /media/usb-up-r/random_picture.log +%j)
hoy=$(date +%j)
hoy=${hoy#0}
ant=${ant#0}
dif=$(($hoy-$ant))
if [ $dif -lt 2 ]; then
	mi_msg="$(tail -1 /home/me/random_picture.log | awk -F "/" '{print $5"-"$6}' | tr ' ' '_')"
	/home/me/tg/bin/telegram-cli -k /home/me/tg/tg-server.pub -WR -e "send_photo chat#xxxxxx /home/me/selected.jpg"
	sleep 30
else
        mi_msg="no pude ver fotos. Hoy nos quedamos sin ella"
fi
/home/me/tg/bin/telegram-cli -k /home/me/tg/tg-server.pub -WR -e "msg chat#xxxxxx "$mi_msg
