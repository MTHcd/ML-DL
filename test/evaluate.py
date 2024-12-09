
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from rouge_score import rouge_scorer

# Define the generate_text function
def generate_text(model, tokenizer, input_text, max_length=50):
    # Encode input text to get the input IDs
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate text using the model
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the generated text back to a string
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Define the function to evaluate ROUGE scores
def evaluate_rouge(generated_text, human_references):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'])

    scores = []
    for reference in human_references:
        scores.append(scorer.score(reference, generated_text))

    return scores

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can specify other GPT models like "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Example of human references (you should modify them as per your dataset)
human_references = [
    "Once upon a time, there was a young girl named Cinderella who lived with her evil stepmother.",
    "The dragon soared over the mountains, its wings beating fiercely against the wind.",
    "The princess found a hidden treasure chest beneath the old oak tree in the royal garden."
]

# Generate text from the input prompt
input_text = "Once upon a time"
generated_text = generate_text(model, tokenizer, input_text)

# Evaluate using ROUGE
rouge_scores = evaluate_rouge(generated_text, human_references)

# Print the generated text and ROUGE scores
print(f"Generated Text: {generated_text}")
print(f"ROUGE Scores: {rouge_scores}")

