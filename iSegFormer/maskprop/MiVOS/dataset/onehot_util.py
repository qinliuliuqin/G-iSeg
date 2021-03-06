import numpy as np


def all_to_onehot(masks, labels):
    Ms = np.zeros((len(labels), masks.shape[0], masks.shape[1], masks.shape[2]), dtype=np.uint8)
    for k, l in enumerate(labels):
        Ms[k] = (masks == l).astype(np.uint8)
    return Ms
