for i in {11..65535}
do
    if [[ $(($i % 100)) == 0 ]];
    then
        ./client_num jade.clear.rice.edu 18005 $i 100
    fi
done