from google.cloud import firestore

server = input("Write the server info here: ").strip()
project_name = input("Write the collection name here: ").strip()
doc_name = input("Please write the doc name: ").strip()
user_data = input("Now please write the data: ").strip()


database = firestore.Client(project=server)
collection = database.collection(project_name)
doc_ref = database.collection(collection).document(doc_name)

