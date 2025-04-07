import torch # pip install torch
from transformers import pipeline
from flask import Flask, render_template, request
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# pip install protobuf
# pip install sentencepiece
# pytorch_model.bin downloaded
# model.safetensors downloaded


WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

article_text = """
The historic roots of mass incarceration:
The year 1865 should be as notable to criminologists as is the year 1970. 
While it marked the end of the Civil War and the passage of the 13th Amendment, it also triggered the nation's first prison boom when state governments arrested and incarcerated increasing numbers of Black Americans.

A century later, mass incarceration began to pick up steam as politicians took steps 
to curb gains from the Civil Rights Movement and to link crime with race. From President 
Lyndon Johnson's “War on Crime” to President Richard Nixon's infamous “Southern Strategy,” 
politicians began to focus on “law and order” messages with explicit racial undertones, 
setting the stage for the next dramatic increase in incarceration beginning in 1970, 
with a rise in harsher drug laws, punitive policing, and longer sentences.


A future without mass incarceration?
Although in recent years we've seen some initial signs of reform and a decrease in 
incarceration rates, there is much work to be done to truly end the decades-long 
practice and related harms of mass incarceration.
"""
model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(summary)
