
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model():
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    print("Loaded GPT-2 model and tokenizer")
    return model, tokenizer

    