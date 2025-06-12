# Table-Text Alignment: Explaining Claim Verification

This is the repository for the paper: [Table-Text Alignment: Explaining Claim Verification Against Tables in Scientific Papers]


## Reproduction of Results
- download [data.zip](https://www.dropbox.com/scl/fi/6ao624vxshbe3col40bet/data.zip?rlkey=4nxsetvtmyk60pyu1ejzlqzs2&st=bzdxhy39&dl=0)
- download [outputs.zip](https://www.dropbox.com/scl/fi/tmwptpn9qy99gruyl63nh/outputs.zip?rlkey=jhgbf77mxi90vqba9qdkbujct&st=c0g2ccsa&dl=0) 


### Table 1: Claim Prediction Results
```bash
python3 run_eval.py claim_task
```

### Table 1: Evidence Selection Results
```bash
python3 run_eval.py evi_task
```



## Running process

### Run the Claim Label Prediction Task
```bash
python3 run_claim.py
```

### Run the Cell-level Evidence Selection Task
```bash
python3 run_evi.py
```

### Evaluation
```bash
python3 run_eval.py claim_task
python3 run_eval.py evi_task
```