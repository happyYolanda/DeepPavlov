# Copyright 2017 Neural Networks and Deep Learning lab, MIPT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy as np
from typing import List, Tuple

from sklearn.metrics import log_loss

from deeppavlov.core.common.metrics_registry import register_metric
from deeppavlov.models.classifiers.utils import labels2onehot


@register_metric('classification_log_loss')
def classification_log_loss(y_true: List[list], y_predicted: List[Tuple[list, dict]]) -> float:
    """
    Calculate log loss for classification module

    Args:
        y_true:  true binary labels
        y_predicted: predictions. \
            Each prediction is a tuple of two elements \
            (predicted_labels, dictionary like {"label_i": probability_i} ) \
            where probability is float or keras.tensor

    Returns:
        log loss
    """
    classes = np.array(list(y_predicted[0][1].keys()))
    y_true_one_hot = labels2onehot(y_true, classes)
    y_pred_probas = [list(y_predicted[i][1].values()) for i in range(len(y_predicted))]

    return log_loss(y_true_one_hot, y_pred_probas)
