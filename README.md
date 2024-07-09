# Blockchain Project

This project is a simple implementation of a blockchain and cryptocurrency, built with Python and Flask. It includes basic functionalities such as creating transactions, mining blocks, registering nodes, and implementing consensus algorithms.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10
- Flask
- UUID

You can install all the required packages using the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

### Running the Server

To start the Flask server on your local machine, run:

```sh
python server.py
```

This will start the server on `http://0.0.0.0:5001/`.

### Features
- Mining Blocks: Nodes can mine blocks by making a GET request to `/mine`.
- Creating Transactions: New transactions can be created by sending a POST request to `/transactions/new`.
- Registering Nodes: New nodes can be registered to the network by sending a POST request to `/nodes/register`.
- Consensus Algorithm: The consensus algorithm can be triggered by making a GET request to `/nodes/resolve`.
- ...

### Testing

The project includes unit tests for various components of the blockchain. You can run the tests using:

```sh
python -m unittest test/test_blockchain.py
```

### Project Structure

- `chain/`: Contains the blockchain implementation.
- `server.py`: Flask server that provides the API endpoints.
- `test/`: Contains unit tests for the blockchain functionality.

### License

This project is licensed under the MIT License.
