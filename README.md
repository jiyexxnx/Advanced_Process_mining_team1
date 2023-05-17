# Advanced Process Mining Group1 Project
Poeysie Chuah, I-Chen Hsieh, Jiyeon Lee, Mariam Arustashvili, Alexander Gabitashvili, Hanchun Hua

# Paper
Encoding High-Level Control-Flow Construct Information for Process Outcome Prediction
- Paper: https://ieeexplore.ieee.org/document/9980737
- Author github: https://github.com/MozhganVD/LPMforPPM
- Datasets: https://github.com/irhete/predictive-monitoring-benchmark 

This repository provides implementation for reporducing our project. We did some minor change of the code to adapt our environment.

# System Information
We ran the experiment both on Windows and Mac, the detail information are revealed in the [sys_info](/sys_info)

# Step-by-step instructions
You first need to generate LPMs feature for each event log, then you can choose between one-hot encoding based methods or embedding layers to encode and train the LSTM model as described step by step below:

# Usage 
1. Use ProM 6.9 to transform raw data from .csv to .xes file and do local process mining and export .pnml (petri net markup language).
- Note: we couldn't find the function to export as .pnml which the authour suggested so we exported as .apnml instead.

2. Install dependencies (Python 3.8.0) :

```pip install -r requirements.txt```

## LPMs Feature Generation
1. Discover and save LPMs using ProM as .pnml format
2. Save event logs in xes format 
3. Run ```LPMDetection_Complete.py``` with following flags:
    -  *--LPMs_dir*: path/to/discovered/LPMs
    -  *--raw_log_file*: path/to/raw/eventlog/.xes
    -  *--processed_log_file*: path/to/save/processed/eventlog/.csv
    -  *--Min_prefix_size*
    -  *--Max_prefix_size*

- Example:

```Python LPMDetection_Complete.py --LPMs_dir "./LPMs" --raw_log_file "./datasets/eventlog.xes" --processed_log_file "./datasets/eventlog_processed.csv" --Min_prefix_size 2 --Max_prefix_size 36``` 

> Modify Code
- [line 30] Cast float object to int
for nr_events in range(int(min_length) + 1, int(max_length) + 1):

## One-hot encoding (Classic/ Wrapped)
1. Prepare dataset by running ```data_processing.py``` with following flags:
    -  *--dataset*: dataset name
    -  *--dir_path*: path/to/store/processed/data
    -  *--raw_log_file*: path/to/processed/eventlog/.csv
    -  *--Max_length*
    -  *--train_ratio*

- Example:

```Python data_processing.py --dataset "Production" --dir_path "./datasets" --raw_log_file "./datasets/eventlog_processed.csv" --Max_length 36 --train_ratio 0.8``` 

> Modify Code
- [line 38 and line 40] - added 'base_case_id'

2. Hyperparameter tuning by running ```HP_Optimization.py``` with following flags:
    -  *--dataset*: dataset name (same name as data processing name)
    -  *--data_dir*: path/to/store/processed/data
    -  *--checkpoint_dir*: path/to/sdave/results
    -  *--LPMs*: True/False
    -  *--encoding_type*: W: wrapped, C: classic one-hot
    -  *--LPMs_type*: LPMs_binary/LPMs_frequency (if you choose the wrapped for encoding type)
    
- Example:

```Python HP_Optimization.py --dataset "Production" --dir_path "./datasets" --checkpoint_dir "./checkpoints" --LPMs True --encoding_type "W" --LPMs_type "LPMs_binary"``` 

>Modify Code
- [line 132] 
- best = fmin(f_lstm_cv, space, algo=tpe.suggest, max_evals=50, trials=trials, rstate=np.random.RandomState(seed))
- best = fmin(f_lstm_cv, space, algo=tpe.suggest, max_evals=50, trials=trials, rstate=np.random.default_rng(seed))

>Modify Running code "HP_Optimization.py"  
- --dir_path  change to --data_dir



3. Run LSTM model with a predifined parameters by running ```Main_LSTM_LPMs.py``` with following flags:
    -  *--dataset*: dataset name (same name as data processing name)
    -  *--data_dir*: path/to/store/processed/data
    -  *--checkpoint_dir*: path/to/sdave/results
    -  *--LPMs*: True/False
    -  *--encoding_type*: W: wrapped, C: classic one-hot
    -  *--LPMs_type*: LPMs_binary/LPMs_frequency (if you choose the wrapped for encoding type)
    -  *--learning_rate*
    -  *--batch_size*
    -  *--layers*: number of LSTM layers
    -  *--opt*: RMSprop or adam
    -  *--rate*: dropout rate
    -  *--units*: number of neuron units per layer
    
## Embedding layers 
1. Hyperparameter tuning by running ```HPO_embedding_args.py``` with following flags:
    -  *--data_dir*: path/to/save/results
    -  *--raw_data*: path/to/processed/eventlog/.csv
    -  *--out_name*: dataset name
    -  *--LPMs*: True/False
    -  *--Only_LPMs*: True/False (if you want to train model only with LPMs not activities, in this case both LPMs and Only_LPMs flags must be True.)
    -  *--max_length*
    -  *--results*: path/to/save/results/in/.text
    
 - Example:
 
 ```Python HPO_embedding_args.py --data_dir "./datasets" --raw_data "./EventLog.csv" --out_name "production" --LPMs True --Only_LPMs False --max_length 36 --results "./results_lpms_act.txt"``` 
 
2. Run LSTM model with a predifined parameters by running ```Embedding_Run.py``` with following flags:
    -  *--data_dir*: path/to/save/results
    -  *--raw_data*: path/to/processed/eventlog/.csv
    -  *--out_name*: dataset name
    -  *--LPMs*: True/False
    -  *--Only_LPMs*: True/False (if you want to train model only with LPMs not activities, in this case both LPMs and Only_LPMs flags must be True.)
    -  *--max_length*
    -  *--results*: path/to/save/results/in/.text
    -  *--batch_size*
    -  *--embedding_act*: dimension of the embedding layers for activities 
    -  *--embedding_lpms*: dimension of the embedding layers for LPMs
    -  *--learning_rate*
    -  *--opt*: RMSprop or adam
    -  *--rate*: dropout rate
    -  *--units*: number of neuron units per layer
    -  *--layers*: number of LSTM layers

# Raw results
We had experiment on "Production" dataset and the results can be found in the following folders:
1. pnml files generated from ProM 6.9: [production_lpm](/production_lpm)
2. One-hot: [OneHot_LSTM/checkpoints/Production](OneHot_LSTM/checkpoints/Production)
3. Embedding: [Embedding_LSTM/datasets/production](Embedding_LSTM/datasets/production)
    


# System information
- We followed Author github's system requirement. (Windows)
- However, for Mac M1 chip, it's better to switch to tensorflow -mackos==2.9 and tensorflow-metal==0.5.0
- There's no ProM version for Mac OS.

    
