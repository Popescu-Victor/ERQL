from google.cloud import firestore

# This code uploads a single entry to Firestore. It creates a document with the specified data and automatically adds a timestamp.

db = firestore.Client(project="project-xxxxxxxx")
collection_name = "ERQL_Single"
doc_name = "Entry_001"

doc_ref = db.collection(collection_name).document(doc_name)
doc_ref.set({
    "Teacher": "Prof. Andrei Pop",
    "Name": "Ion Ionescu",
    "Final Grade" : 9.5,
    "timestamp": firestore.SERVER_TIMESTAMP
})

print("Upload complete")


'''
ULTRA CONCISE VERSION:

database = firestore.Client(project="XYZ")
collection = db.collection("XYZ")
collection.document("XYZ").set({XYZ})
'''
