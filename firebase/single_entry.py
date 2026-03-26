from google.cloud import firestore

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
