import nltk
import os
import sys

# Redirect stdout to suppress NLTK download messages
original_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')

# Download required NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Restore stdout
sys.stdout = original_stdout 