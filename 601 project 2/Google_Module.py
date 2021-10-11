from google.cloud import language_v1
from nlp_module import NLP_Module

class Google_Module(NLP_Module):

    client = None

    def __init__(self):
        self.client = language_v1.LanguageServiceClient()

    def getScore(self, msgs):
        scores = []
        for msg in msgs:
            document = language_v1.Document(content=msg, type_=language_v1.Document.Type.PLAIN_TEXT)
            response = self.client.analyze_sentiment(request={'document': document})
            scores.append((response.document_sentiment.score, response.document_sentiment.magnitude))
        return scores

