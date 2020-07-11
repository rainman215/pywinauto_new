id=`ps -ef | grep get_cpu.sh | sed -n '1p' | awk '{print $2}'`
kill -9 $id
