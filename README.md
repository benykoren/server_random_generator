The way to run it is to clone it from the repository and then run the 'install_and_run' file. After that, two containers will be created: one for the database and one for the server.

You can test the system using BloomRPC. Here's a brief explanation of the code:
RandomService() is a class that houses the server. It receives RPC requests from the client. Upon receiving a request, it generates a random number, stores it in the database, and then returns the number to the client.

In order to communicate with the database, an API was created. This API allows you to connect to the database container, add a number, and retrieve all the saved numbers."