#!/usr/bin/env bash

COUNT=10  # how many times to run the program
SIZE=100  # how many numbers to generate
SUM=0     # total number of instructions
MAX=0     # worst case (maximum instructions)

for i in $(seq 1 $COUNT)
do
    ARG=$(python3 generate.py $SIZE)

    echo "Test $i:"
    ./push_swap $ARG | ./checker_linux $ARG

    INSTR=$(./push_swap $ARG | wc -l)
    echo "Number of instructions: $INSTR"
    echo
    SUM=$((SUM + INSTR))
    if [ $INSTR -gt $MAX ]; then
        MAX=$INSTR
    fi
done

AVG=$((SUM / COUNT))

echo "=========================="
echo "Worst case (max): $MAX"
echo "Average number of instructions: $AVG"

echo
echo "=========================="
echo "500 numbers"

SIZE=500
SUM=0
MAX=0

for i in $(seq 1 $COUNT)
do
    ARG=$(python3 generate.py $SIZE)

    echo "Test $i:"
    ./push_swap $ARG | ./checker_linux $ARG

    INSTR=$(./push_swap $ARG | wc -l)
    echo "Number of instructions: $INSTR"
    echo
    SUM=$((SUM + INSTR))
    if [ $INSTR -gt $MAX ]; then
        MAX=$INSTR
    fi
done

AVG=$((SUM / COUNT))

echo "=========================="
echo "Worst case (max): $MAX"
echo "Average number of instructions: $AVG"
