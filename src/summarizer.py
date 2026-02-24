from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summarize_text(text, sentences_count=3):

    if not text.strip():
        return "No text extracted to summarize."

    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()

        summary = summarizer(parser.document, sentences_count)

        return " ".join(str(sentence) for sentence in summary)

    except Exception as e:
        print("Summarization Error:", e)
        return "Summarization failed."