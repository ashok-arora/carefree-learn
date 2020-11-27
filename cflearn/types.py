import torch

import numpy as np

from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union
from typing import Callable
from typing import Optional
from cfdata.tabular import TabularDataset


param_type = Union[torch.Tensor, torch.nn.Parameter]
data_type = Optional[Union[np.ndarray, List[List[float]], str]]
np_dict_type = Dict[str, Union[np.ndarray, Any]]
tensor_dict_type = Dict[str, Union[torch.Tensor, Any]]
tensor_tuple_type = Tuple[torch.Tensor, torch.Tensor]
general_config_type = Optional[Union[str, Dict[str, Any]]]
predictor_type = Optional[Callable[[int, TabularDataset, np.ndarray], np.ndarray]]
evaluator_type = Optional[Callable[[List[np.ndarray], List[np.ndarray]], np.ndarray]]
tensor_batch_type = Tuple[Dict[str, torch.Tensor], Optional[torch.Tensor]]


__all__ = [
    "param_type",
    "data_type",
    "np_dict_type",
    "tensor_dict_type",
    "tensor_tuple_type",
    "general_config_type",
    "predictor_type",
    "evaluator_type",
    "tensor_batch_type",
]
