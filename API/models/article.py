
class Article:
    def __init__(self, id, title, description, published_date, source, sentiment):
        self.id = id
        self.title = title
        self.description = description
        self.published_date = published_date
        self.source = source
        self.sentiment = sentiment

    def __repr__(self):
        return f"Article({self.id}, {self.title}, {self.description}, {self.published_date}, {self.source}, {self.sentiment})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'published_date': self.published_date,
            'source': self.source,
            'sentiment': self.sentiment
        }