import random
import time

from src.vectorstore_client import VectorstoreClient, Item

# TODO: Need to replace this with specific API key
API_KEY = ""
HOST = "https://maplevector.dev"
VECTORSTORE_CLIENT = VectorstoreClient(HOST, API_KEY)
BATCH_SIZE = 100
HEADERS = {"api_key": API_KEY, 'Content-type': 'application/json'}

states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
          'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


def pick_random_state():
    return random.choice(states)


def get_random_vector(dimension):
    vector = []
    for i in range(dimension):
        vector.append(random.random())
    return vector


def get_all_half_vector(dimension):
    vector = []
    for i in range(dimension):
        vector.append(0.5)
    return vector

def generate_ids(max_id):
    ids = []
    for i in range(max_id):
        ids.append(i + 1)
    return ids


def batch_index_vectors(index_name, max_number, dimension):
    ids = generate_ids(max_number)

    total_indexed_items = 0
    for dataset_partition in chunk_it(ids, BATCH_SIZE):
        items = []
        for row in dataset_partition:
            items.append(Item(row, get_random_vector(dimension), metadata={"state": pick_random_state()}))
        response = VECTORSTORE_CLIENT.batch_index_item(index_name, items)
        total_indexed_items += len(items)
        print(total_indexed_items, response.status_code, response.json())


def query_index(index_name, vector):
    start = time.time()
    response = VECTORSTORE_CLIENT.query(index_name, vector, 10, filter_expr="state in [CA, OR]")
    print("query_index", response.status_code, response.json())
    end = time.time()
    print(end - start)


def chunk_it(seq, size):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


if __name__ == '__main__':
    # Step 1: Specify index name
    # Change index name accordingly for different experiments.
    # TODO: change the index name accordingly
    test_index_name = "metadata_filtering_20220809"
    test_dimension = 128
    test_max_id = 3000

    # Step 2: Create index
    # 4096 is vector dimension, while 50000 is the max_number_vectors, which is greater
    # than the number of vectors in data file.
    VECTORSTORE_CLIENT.create_index(test_index_name, test_dimension, 100000)

    batch_index_vectors(test_index_name, test_max_id, test_dimension)

    # query_vector = get_random_vector(test_dimension)
    query_vector = get_all_half_vector(test_dimension)
    query_index(test_index_name, query_vector)

    # If need to delete index, uncomment the line.
    # VectorstoreClient.delete_index(test_index_name)
