Encounter problem

- For python 3.8.0 
- conda activate myenv

- Cannot install -r requirements.txt (line 1), -r requirements.txt (line 3), -r requirements.txt (line 4) and numpy==1.19.2 because these package versions have conflicting dependencies.
- Solution: change requirements.txt numpy without specific version

- packaging.version.InvalidVersion: Invalid version: 'please use pm4py.algo.filtering.log.ltl.ltl_checker.eventually_follows’
- Solution : pip install --upgrade pm4py deprecation


- Missing Xes file, 
- Solution: find BPIC2012 https://data.4tu.nl/articles/dataset/BPI_Challenge_2012/12689204
- 


- LPMs Feature Generation
- Python LPMDetection_Complete.py --LPMs_dir "./LPMs" --raw_log_file "./datasets/xes_logs.xes" --processed_log_file "./datasets/eventlog_processed.csv" --Min_prefix_size 2 --Max_prefix_size 36


- One-hot encoding, preprocessing
- raise KeyError(key) from err KeyError: 'base_case_id'
- solution: add base_case_id in prodessor.py

Python Main_LSTM_LPMs.py --dataset "Production" --data_dir "./datasets" --checkpoint_dir "./checkpoints" --LPMs True --encoding_type "W" --LPMs_type "LPMs_binary" --units 32 --layers 2 --learning_rate 0.00001 --batch_size 8 --rate 0.01 --opt "Adam"

--dataset: dataset name (same name as data processing name)
--data_dir: path/to/store/processed/data
--checkpoint_dir: path/to/sdave/results
--LPMs: True/False
--encoding_type: W: wrapped, C: classic one-hot
--LPMs_type: LPMs_binary/LPMs_frequency (if you choose the wrapped for encoding type)
--learning_rate
--batch_size
--layers: number of LSTM layers
--opt: RMSprop or adam
--rate: dropout rate
--units: number of neuron units per layer


Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/eventlog_processed.csv" --out_name "production" --LPMs True --Only_LPMs False --max_length 36 --results "/results_lpms_act.txt"

Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/eventlog_processed.csv" --out_name "production" --LPMs True --Only_LPMs True --max_length 36 --results "/results_lpms_act_2.txt"

Python Embedding_Run.py --data_dir "./datasets" --raw_data "../datasets/eventlog_processed.csv" --out_name "production" --LPMs True --Only_LPMs False --max_length 36 --batch_size 8 --learning_rate 0.00001 --opt "Adam" --rate 0.01 --units 10 --layers 2

--------------------------------
--sepsis--

Python LPMDetection_Complete.py --LPMs_dir "./sepsis" --raw_log_file "./datasets/sepsis_cases.xes" --processed_log_file "./datasets/sepsis_eventlog_processed.csv" --Min_prefix_size 2 --Max_prefix_size 36

Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/sepsis_eventlog_processed.csv" --out_name "sepsis" --LPMs True --Only_LPMs False --max_length 36 --results "/results_lpms_act_sepsis.txt"

Python Embedding_Run.py --data_dir "./datasets" --raw_data "../datasets/sepsis_eventlog_processed.csv" --out_name "sepsis" --LPMs True --Only_LPMs False --max_length 36 --batch_size 8 --learning_rate 0.00001 --opt "Adam" --rate 0.01 --units 10 --layers 2
------
Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/Production.csv" --out_name "production" --LPMs True --Only_LPMs True --max_length 36 --results "/test_results_lpms_act.txt"

==========
production
Python LPMDetection_Complete.py --LPMs_dir "./production_lpm" --raw_log_file "./datasets/production_2.xes" --processed_log_file "./datasets/Production.csv" --Min_prefix_size 2 --Max_prefix_size 36

Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/Production.csv" --out_name "production" --LPMs True --Only_LPMs True --max_length 36 --results "/production_results_lpms_act.txt"

Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/Production.csv" --out_name "production" --LPMs True --Only_LPMs False --max_length 36 --results "/production_results_lpms_act_true.txt"

=========

===========
Rerun one hot - production 16.05

Python HP_Optimization.py --dataset "Production" --data_dir "./datasets" --checkpoint_dir "./checkpoints" --LPMs True --encoding_type "W" --LPMs_type "LPMs_binary"

Python HP_Optimization.py --dataset "Production" --data_dir "./datasets" --checkpoint_dir "./checkpoints" --LPMs True --encoding_type "C" 
====================
Rerun embedding - production 17.05

Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/Production.csv" --out_name "production" --LPMs True --Only_LPMs False --max_length 36 --results "/results_lpms_act.txt"

Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/Production.csv" --out_name "production" --LPMs True --Only_LPMs True --max_length 36 --results "/results_lpms_only.txt"

Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "../datasets/Production.csv" --out_name "production" --LPMs False --max_length 36 --results "/results_act_only.txt"