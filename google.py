from google.cloud import language_v1

text = u'This stuff is so cool!.'

client = language_v1.LanguageServiceClient()
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
response = client.analyze_sentiment(request={'document': document})
print(u"Document sentiment score: {}".format(response.document_sentiment.score))
print(u"Document sentiment magnitude: {}".format(response.document_sentiment.magnitude))

response = client.analyze_entity_sentiment(request={'document': document})
for entity in response.entities:
    print(u"Representative name for the entity: {}".format(entity.name))
    print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))
    print(u"Salience score: {}".format(entity.salience))
    sentiment = entity.sentiment
    print(u"Entity sentiment score: {}".format(sentiment.score))
    print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
    for metadata_name, metadata_value in entity.metadata.items():
        print(u"{} = {}".format(metadata_name, metadata_value))
    for mention in entity.mentions:
        print(u"Mention text: {}".format(mention.text.content))
        print(u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name))

