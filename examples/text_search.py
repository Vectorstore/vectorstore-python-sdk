import time

# Install sentence_transformers via https://pypi.org/project/sentence-transformers/
from sentence_transformers import SentenceTransformer

from src.vectorstore_client import VectorstoreClient, Item

# TODO: Need to replace this with specific API key
API_KEY = ""
HOST = "https://maplevector.dev"
VECTORSTORE_CLIENT = VectorstoreClient(HOST, API_KEY)
HEADERS = {"api_key": API_KEY, 'Content-type': 'application/json'}

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")
sentences = ['This framework generates embeddings for each input sentence',
             'Sentences are passed as a list of string.',
             'The quick brown fox jumps over the lazy dog.']


def index_vectors(index_name):
    for x in range(len(sentences)):
        # Use item_id starting from 1 instead of 0.
        item_id = x + 1
        # Need to convert ndarray to list as the API is based on JSON.
        vector = model.encode(sentences[x]).tolist()
        VECTORSTORE_CLIENT.index_item(index_name, Item(item_id, vector, {}))


if __name__ == '__main__':
    # TODO: Fill the index name accordingly
    test_index_name = ""
    if len(test_index_name) == 0:
        raise Exception("Please specify a non-empty index name.")

    test_dimension = 768
    # Step 1. Create index
    VECTORSTORE_CLIENT.create_index(test_index_name, test_dimension, 100000, "l2")

    # Step 2. Index item one by one
    index_vectors(test_index_name)

    # Sleep 30 seconds to build index.
    time.sleep(30)

    query_vector = model.encode("test").tolist()
    start = time.time()
    response = VECTORSTORE_CLIENT.query(test_index_name, query_vector, 20,
                                        filter_expr="user_id == 'ebeb4eaf-72ae-410a-8fab-c168e11c58f1'")
    print("query_index", response.status_code, response.json())
    end = time.time()
    print(end - start)

    # Step 3. Delete index
    # VECTORSTORE_CLIENT.delete_index(test_index_name)
