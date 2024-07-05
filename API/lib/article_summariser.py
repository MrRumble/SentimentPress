from transformers import pipeline

"""
This class was developed to create concise summaries for each query search. 
It uses the Hugging Face transformers library to summarize the top and bottom 
articles based on sentiment scores extracted from a DataFrame. 
However, it significantly impacts performance and may not be the optimal summarization system for our needs.
Further research into alternative summarizers is recommended.
"""

class ArticleSummariser:
    def __init__(self):
        self.text_generation_pipeline = pipeline('summarization')

    def summarise_top_bottom_articles(self, df, top_n=3, bottom_n=3, max_summary_sentences=6):
        top_articles = df.nlargest(top_n, 'Sentiment Score')
        bottom_articles = df.nsmallest(bottom_n, 'Sentiment Score')
        combined_text = '. '.join(top_articles['Title'] + '. ' + top_articles['Description']) + '. ' + \
                        '. '.join(bottom_articles['Title'] + '. ' + bottom_articles['Description'])
        summary = self.text_generation_pipeline(combined_text, max_length=200, min_length=30, num_return_sequences=1, early_stopping=True)
        summarized_text = summary[0]['summary_text']
        summarized_sentences = summarized_text.split('. ')
        if len(summarized_sentences) > max_summary_sentences:
            summarized_text = '. '.join(summarized_sentences[:max_summary_sentences]) + '.'
        return summarized_text
