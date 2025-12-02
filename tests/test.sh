for directory in intermediate*
    do 
    cd $directory
    echo $directory
    unzip *.zip

    for verilog in prompt*.v
        do
        iverilog -o "$verilog".out $verilog tb*.v
        done

    for sim in *out
        do
        vvp $sim > "$sim".results
        done
    cd ..
    done