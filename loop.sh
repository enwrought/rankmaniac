python data/pagerank_map.py < local_test_data/GNPn100p05 | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > output0.txt

for i in `seq 1 47`; do
    IN=output$(($i-1)).txt
    OUT=output$(($i)).txt
    echo $IN
    echo $OUT
    python data/pagerank_map.py < $IN | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > $OUT
done
