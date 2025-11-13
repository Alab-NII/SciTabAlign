# Table-Text Alignment: Explaining Claim Verification

This is the repository for the paper: [Table-Text Alignment: Explaining Claim Verification Against Tables in Scientific Papers](https://aclanthology.org/2025.findings-emnlp.135/)
(Findings of EMNLP 2025) 

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

## Citation

If you plan to use the dataset, please cite our paper:

```
@inproceedings{ho-etal-2025-table,
    title = "Table-Text Alignment: Explaining Claim Verification Against Tables in Scientific Papers",
    author = "Ho, Xanh  and
      Kumar, Sunisth  and
      Wu, Yun-Ang  and
      Boudin, Florian  and
      Takasu, Atsuhiro  and
      Aizawa, Akiko",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2025",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-emnlp.135/",
    pages = "2509--2517",
    ISBN = "979-8-89176-335-7",
}
```
