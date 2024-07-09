from transformers import pipeline
from openai import OpenAI


import os
from dotenv import load_dotenv

class ArticleSummariser:
    def __init__(self):
        load_dotenv()
        self.text_generation_pipeline = pipeline('summarization')
        self.api_key = os.getenv("OPEN_AI_KEY")

    def summarise_top_bottom_articles(self, df, top_n=3, bottom_n=3, max_summary_sentences=6) -> str:
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

    def summarise_all_articles_with_prompt_ai(self, df) -> str: #NOT CURRENTLY WORKING OR USED ANYWHERE
        client = OpenAI(api_key=self.api_key)
        article_texts = '. '.join(df['Title'] + '. ' + df['Description'])

        prompt = f"""This is a summary of all titles and descriptions on a given topic of news for a specific day.
                    Summarize all articles based on their titles and descriptions:

                    {article_texts}

                    Please extract the main headlines and create a concise summary for the user.
                 """

        response = client.completions.create(
                    model="davinci-002",  # Specify the model
                    prompt=prompt,
                    max_tokens=50,
                    stop=None,
                    temperature=0.5,
                    top_p=1.0,
                    n=1,
                    echo=True)

        summarised_text = response['choices'][0]['text'] 

        return summarised_text
