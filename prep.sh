for test in assign and_gate priority_encoder mux half_adder counter lfsr fsm left-rotate ram permutation truthtable signed-addition-overflow countslow advfsm advshifter abro
    do
        zip "$test".zip *"$test"*.v
    done