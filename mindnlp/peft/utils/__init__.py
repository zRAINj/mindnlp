# Copyright 2023 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""utils for peft"""

from .config import PeftConfig, PeftType, TaskType, PromptLearningConfig
from .save_and_load import get_peft_model_state_dict, set_peft_model_state_dict
from .other import (
    CONFIG_NAME,
    WEIGHTS_NAME,
    _set_trainable,
    transpose,
    shift_tokens_right,
    _get_submodules,
    _set_adapter,
    _freeze_adapter,
    ModulesToSaveWrapper,
    TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING
)
