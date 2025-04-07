# Running an LLM
## Assignment 8 - Natalie Temple

For this week's assignment I chose to run an mT5-multilingual-XLSum model.

[mt5-multilingual-XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum#mt5-multilingual-xlsum)

[My Code](llmshw.py)

To run this LLM I had to install a library (protobuf) and a token converter (sentencepiece). I documented this in the code.

Then, when running the model, pytorch_model.bin as well as model.safetensors downloaded.

I plugged an article into the the article_text variable and then the summary was printed in my terminal.

This model did take a while to work and it ended up freezing a few times before and after it worked.