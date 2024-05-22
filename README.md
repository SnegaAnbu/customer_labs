# customer_labs
Project Overview
The purpose of the Data Pusher project is to create a Django web application that acts as an intermediary for receiving data and forwarding it to various specified destinations using webhook URLs. This application is designed to handle data for different accounts and send it across multiple platforms as specified by the account settings.

Modules
1. Account Module
Purpose: Manages account information.
Fields:
email (Mandatory, unique): The email address associated with the account.
account_id (Unique): A unique identifier for the account, automatically generated.
account_name (Mandatory): The name of the account.
app_secret_token (Automatically generated): A unique secret token for authentication.
website (Optional): The website associated with the account.

2. Destination Module
Purpose: Manages the destinations to which data should be sent for each account.
Fields:
url (Mandatory): The webhook URL where data will be sent.
http_method (Mandatory): The HTTP method to use when sending data (GET, POST, PUT).
headers (Mandatory, multiple values): Headers to include in the HTTP request. Examples

3. Data Handler
Purpose: Receives incoming JSON data via a POST request and forwards it to the specified destinations.
Functionality:
Receives data with a secret token in the header (CL-X-TOKEN).
Identifies the account using the secret token.
Sends the data to the account's destinations using the specified URLs, HTTP methods, and headers.
If the destination's HTTP method is GET, the data is sent as query parameters. If the method is POST or PUT, the data is sent as a JSON payload.
