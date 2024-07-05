from transformers import pipeline

# This class was created to try as we wanted a way of ceating a neat summary for each query search. 
# It utilizes the Hugging Face transformers library to summarize the top and bottom articles based on sentiment scores from a DataFrame.
# This will give us a neat and concise string to package along with data and send to the database.
# NOTE: This slows down performace massively, might not actually be the summary system we need. Worth researching summarisers in more detail.


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
