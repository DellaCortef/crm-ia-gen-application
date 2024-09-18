import chromadb
chroma_client = chromadb.Client()

# Creating our Vector Database - "my_collection"
collection = chroma_client.get_or_create_collection(name="crm_expansion")

# Inserting two parameters in Vector Database model
collection.add(
    documents=[
        "Expansion of CRM to Brazil",
        "Expansion CRM to Singapore",
        "Expansion CRM to Taiwan",
        "Expansion CRM to China",
        "Expansion of CRM to France",
        "Expansion of CRM to the United Kingdom",
        "Expansion of CRM to Japan",
        "Expansion of CRM to Germany"
    ],
    ids=["country1", "country2", "country3", "country4", "country5", "country6", "country7", "country8"]
)