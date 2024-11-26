import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "infly/OpenCoder-1.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             torch_dtype=torch.bfloat16,
                                             device_map="auto",
                                             #device_map=torch.device("cpu"),
                                             trust_remote_code=True)

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)