make re
w=100
h=100
d=10
i=0
make
while [ $i -lt $1 ]
do
	touch map.txt
	clear
	perl script/generator.pl $w $h $d > map.txt
	i=`expr $i + 1`
	rm map.txt
done