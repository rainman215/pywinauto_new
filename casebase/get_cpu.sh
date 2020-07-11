file=/home/usage.txt
result=/home/result.txt

if [ -f $result ]
then
	rm $result
fi
echo "Start time: `date`"| tee -a $result
while [ 1 ]
do
	top -bn 1 > $file
	idle=`cat $file | grep Cpu | awk '{print $5}' | sed 's/id,/ /g'`
	Target_usage=`cat $file | grep TargetApp | awk '{ print $10 }'`
	Target_mem=`cat $file | grep TargetApp | awk '{ print $11 }'`
	echo "Cpu idle is:  $idle">>$result
	echo "Target_usge is: $Target_usage">>$result
	echo "Target_mem is: $Target_mem">>$result
	echo "------------------------------------">>$result
	sleep 1
done
