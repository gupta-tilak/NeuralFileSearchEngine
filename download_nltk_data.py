import nltk

def download_nltk_resources():
    print("Downloading NLTK resources...")
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    print("Download complete!")

if __name__ == "__main__":
    download_nltk_resources() 