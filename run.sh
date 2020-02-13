for i in {11..65535}
do
    if [[ $(($i % 10)) == 0 ]];
    then
        ./client_num opal.clear.rice.edu 18010 $i 100
    fi
done