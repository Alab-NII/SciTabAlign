# Reference: https://github.com/Alab-NII/2wikimultihop/blob/main/2wikimultihop_evaluate.py

from sklearn.metrics import precision_recall_fscore_support


def evaluate_claim_verification(predictions, ground_truth, labels = ["Supported", "Refuted"]):
    """
    """

    precision, recall, f1, _ = precision_recall_fscore_support(
        ground_truth,
        predictions,
        labels=labels,
        average='macro',
        zero_division=0  # Avoid division by zero if a class is missing
    )

    return {
        "precision": f"{precision * 100:.1f}",
        "recall": f"{recall * 100:.1f}",
        "macro_f1": f"{f1 * 100:.1f}"
    }
    
    

def compute_precision_recall_f1(y_true, y_pred):
    def precision_recall_f1_one(true_set, pred_set):
        # Convert inner lists (e.g., [2, 3]) to tuples (2, 3) for set compatibility
        true_set = set(map(tuple, true_set))
        pred_set = set(map(tuple, pred_set))

        tp, fp, fn = 0, 0, 0
        for e in pred_set:
            if e in true_set:
                tp += 1
            else:
                fp += 1
        for e in true_set:
            if e not in pred_set:
                fn += 1
        prec = 1.0 * tp / (tp + fp) if tp + fp > 0 else 0.0
        recall = 1.0 * tp / (tp + fn) if tp + fn > 0 else 0.0
        f1 = 2 * prec * recall / (prec + recall) if prec + recall > 0 else 0.0
        return prec, recall, f1

    precisions, recalls, f1s = [], [], []
    for true_labels, pred_labels in zip(y_true, y_pred):
        p, r, f1 = precision_recall_f1_one(true_labels, pred_labels)
        precisions.append(p)
        recalls.append(r)
        f1s.append(f1)

    macro_precision = sum(precisions) / len(precisions)
    macro_recall = sum(recalls) / len(recalls)
    macro_f1 = sum(f1s) / len(f1s)

    return macro_precision, macro_recall, macro_f1

    
def evaluate_evidence_cell(predictions, ground_truth):
    assert len(predictions) == len(ground_truth), "Mismatch in number of predictions and ground truth examples."

    precision, recall, macro_f1 = compute_precision_recall_f1(ground_truth, predictions)

    return {
        "precision": f"{precision * 100:.1f}",
        "recall": f"{recall * 100:.1f}",
        "macro_f1": f"{macro_f1 * 100:.1f}"
    }