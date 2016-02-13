python data/pagerank_map.py < local_test_data/soc | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > output0.txt

for i in `seq 1 48`; do
    IN=output$(($i-1)).txt
    OUT=output$(($i)).txt
    echo $IN
    python data/pagerank_map.py < $IN | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > $OUT
done
