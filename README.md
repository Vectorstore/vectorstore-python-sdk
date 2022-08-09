# Vectorstore Python SDK

---

## About

<table>
<tr>
<td>

The Python SDK is used to interact with the Vectorstore [SaaS solution](https://vectorstore.webflow.io/) to do semantic search. It follows the current [API reference](https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit#).

</td>
</tr>
</table>

## Getting Started

### Prerequisites

Install Python 3.8 to get started.

### Usage

#### Vectorstore Client 

Vectorstore Client is located in src/vectorstore_client.py, which has the Vectorstore endpoint hardcoded inside. Your implementation can code against this client.

#### Example of ingestion code.

The example code is located in examples/us_states_metadata_filtering.py, which generates random vectors and metadata (one of US state). In its main function, it shows the steps: create an index, index vectors and query.
