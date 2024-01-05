# Text-Summarizer-Projectcd 
Installation and Setup:

The code begins by installing necessary libraries such as transformers, datasets, sacrebleu, rouge_score, and py7zr using pip.
Library Import:

Various libraries are imported, including transformers, datasets, matplotlib, pandas, nltk, tqdm, and torch.
Device Configuration and Model Loading:

The code checks for GPU availability, sets the device, and loads the Pegasus model and tokenizer from Hugging Face.
Dataset Loading:

A dataset is downloaded, extracted, and loaded using the Hugging Face datasets library.
Data Exploration:

Information about the dataset, column names, and a sample dialogue and summary are printed for exploration.
Tokenizing and Formatting Dataset:

A function is defined to tokenize and format the dataset for training using the Pegasus tokenizer.
Training Setup:

Training configuration is set up, including training arguments, data collator, and trainer.
Model Training:

The model is trained for text summarization using the defined trainer.
Evaluation and ROUGE Score Calculation:

A function is defined to calculate ROUGE scores on the test dataset using the trained model. ROUGE scores are computed and displayed.
Model and Tokenizer Saving:

The trained model and tokenizer are saved for future use.
Model Inference:

The code demonstrates how to load the saved model and tokenizer for making predictions on new text.
Conclusion:

The provided code establishes an end-to-end text summarization pipeline using the Pegasus model. It covers data loading, model training, evaluation, and inference. The code is well-organized and documented for clarity and reproducibility.
