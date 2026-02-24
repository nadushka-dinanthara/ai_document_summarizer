from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summarize_text(text, sentences_count=5):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, sentences_count)
        summary_text = " ".join([str(sentence) for sentence in summary])
        if not summary_text:
            return text  # fallback if text too short
        return summary_text
    except:
        return text