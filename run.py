#!/usr/bin/env python
# -*- coding: utf-8 -*-
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time

model_path = '/data/home/yaokj5/dl/models/baichuan-7B'

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)
device = torch.cuda.current_device()
print(device)
stopword='q'

while True:
    print("\n用户：")
    query = ""
    for line in iter(input, stopword):  # 每行接收的东西 用了iter的哨兵模式
        query += line + "\n"  # 换行

    start_time = time.time()
    inputs = tokenizer(query.strip(), return_tensors='pt')
    inputs = {k: v.to(device) for k, v in inputs.items()}
    pred = model.generate(**inputs, max_new_tokens=200, repetition_penalty=1.1)
    end_time = time.time()
    response = tokenizer.decode(pred.cpu()[0], skip_special_tokens=True)
    print(f'\n回答：{response}\n')
    print(f'\nTook {round(end_time - start_time, 3)} s\n\n\n\n')
