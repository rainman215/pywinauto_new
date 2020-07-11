dir='/home/Release-GCC'
if [ `pidof TargetApp` > 0 ]
then
	kill -9 `pidof TargetApp`
fi

if [ -d $dir ]
then
	rm $dir -fr
fi
sleep 1
file='/home/'`cat /home/log`
tar -zxvf $file -C /home
cd /home/Release-GCC
sh Run
