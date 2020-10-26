from transformers import T5Tokenizer, TFT5ForConditionalGeneration
import os

def loadModel(name, path=None):
    """Load a pretrained model from HuggingFace, or optionally from a given path.

    - **parameters**::
        :param str name: The name of the hugging face pretrained model.
        :param str path: An optional path to load pretrained model from, which will be tried before trying to load from cloud.
    """

    # if a path is given, try to load from that path first
    if path:
        try:
            model = TFT5ForConditionalGeneration.from_pretrained(path)
            tokenizer = T5Tokenizer.from_pretrained(path)
            
            return model, tokenizer
        except:
            print(f"WARNING: Could not load the model from the path ({path}) specified with --from-pretrained flag. Trying to load '{name}' from cloud instead.")

    # if no path was specified, or the load from path failed, try to load from cloud using the given model name
    model = TFT5ForConditionalGeneration.from_pretrained(name)
    tokenizer = T5Tokenizer.from_pretrained(name)
    
    return model, tokenizer

# if a path was given to a pretrained model, try to load from there first
if os.environ.get("PRETRAINED_MODEL_PATH"):
    model, tokenizer = loadModel("t5-base", os.environ.get("PRETRAINED_MODEL_PATH"))

else:
    # if no path was given, load from the cloud
    model, tokenizer = loadModel("t5-base")

print("\nModel loaded successfully, ready to handle requests...\n")

def translateEnToDe(phrase):
    """
    Translate a phrase from english to german
    """
    inputs = tokenizer(f"translate English to German: {phrase}", return_tensors="tf").input_ids
    result = model.generate(inputs)

    return tokenizer.decode(result[0])

