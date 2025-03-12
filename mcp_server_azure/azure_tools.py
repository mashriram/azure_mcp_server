# azure_tools.py
from mcp.types import Tool


def get_blob_storage_tools() -> list[Tool]:
    return [
        Tool(
            name="blob_container_create",
            description="Create a new Blob Storage container",
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {
                        "type": "string",
                        "description": "Name of the Blob Storage container to create",
                    }
                },
                "required": ["container_name"],
            },
        ),
        Tool(
            name="blob_container_list",
            description="List all Blob Storage containers",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="blob_container_delete",
            description="Delete a Blob Storage container",
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {
                        "type": "string",
                        "description": "Name of the Blob Storage container to delete",
                    }
                },
                "required": ["container_name"],
            },
        ),
        Tool(
            name="blob_upload",
            description="Upload a blob to Blob Storage",
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {
                        "type": "string",
                        "description": "Name of the Blob Storage container",
                    },
                    "blob_name": {
                        "type": "string",
                        "description": "Name of the blob in the container",
                    },
                    "file_content": {
                        "type": "string",
                        "description": "Base64 encoded file content for upload",
                    },
                },
                "required": ["container_name", "blob_name", "file_content"],
            },
        ),
        Tool(
            name="blob_delete",
            description="Delete a blob from Blob Storage",
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {
                        "type": "string",
                        "description": "Name of the Blob Storage container",
                    },
                    "blob_name": {
                        "type": "string",
                        "description": "Name of the blob to delete",
                    },
                },
                "required": ["container_name", "blob_name"],
            },
        ),
        Tool(
            name="blob_list",
            description="List blobs in a Blob Storage container",
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {
                        "type": "string",
                        "description": "Name of the Blob Storage container",
                    }
                },
                "required": ["container_name"],
            },
        ),
        Tool(
            name="blob_read",
            description="Read a blob's content from Blob Storage",
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {
                        "type": "string",
                        "description": "Name of the Blob Storage container",
                    },
                    "blob_name": {
                        "type": "string",
                        "description": "Name of the blob to read",
                    },
                },
                "required": ["container_name", "blob_name"],
            },
        ),
    ]


def get_cosmosdb_tools() -> list[Tool]:
    return [
        Tool(
            name="cosmosdb_container_create",  # Renamed from table to container
            description="Create a new Cosmos DB container",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                    "partition_key": {
                        "type": "object",
                        "description": "Partition key definition for the container (e.g., {'paths': ['/partitionKey'], 'kind': 'Hash'})",
                    },
                },
                "required": [
                    "container_name",
                    "partition_key",
                ],  # Partition key is usually required for Cosmos DB
            },
        ),
        Tool(
            name="cosmosdb_container_describe",  # Renamed from table to container
            description="Get details about a Cosmos DB container",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                },
                "required": ["container_name"],
            },
        ),
        Tool(
            name="cosmosdb_container_list",  # Renamed from table to container
            description="List all Cosmos DB containers in a database",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    }
                },
            },
        ),
        Tool(
            name="cosmosdb_container_delete",  # Renamed from table to container
            description="Delete a Cosmos DB container",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                },
                "required": ["container_name"],
            },
        ),
        Tool(
            name="cosmosdb_item_create",  # Renamed from put to create, and table to container
            description="Create a new item in a Cosmos DB container",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                    "item": {
                        "type": "object",
                        "description": "Item data to create (JSON object)",
                    },
                },
                "required": ["container_name", "item"],
            },
        ),
        Tool(
            name="cosmosdb_item_read",  # Renamed from get to read, and table to container
            description="Read an item from a Cosmos DB container",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                    "item_id": {
                        "type": "string",
                        "description": "ID of the item to read",
                    },
                    "partition_key": {
                        "type": "string",
                        "description": "Partition key value for the item",
                    },
                },
                "required": ["container_name", "item_id", "partition_key"],
            },
        ),
        Tool(
            name="cosmosdb_item_replace",  # Renamed from update to replace, and table to container, using replace_item for full replace
            description="Replace an item in a Cosmos DB container",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                    "item_id": {
                        "type": "string",
                        "description": "ID of the item to replace",
                    },
                    "partition_key": {
                        "type": "string",
                        "description": "Partition key value for the item",
                    },
                    "item": {
                        "type": "object",
                        "description": "Updated item data (JSON object)",
                    },
                },
                "required": ["container_name", "item_id", "partition_key", "item"],
            },
        ),
        Tool(
            name="cosmosdb_item_delete",  # Renamed table to container
            description="Delete an item from a Cosmos DB container",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                    "item_id": {
                        "type": "string",
                        "description": "ID of the item to delete",
                    },
                    "partition_key": {
                        "type": "string",
                        "description": "Partition key value for the item",
                    },
                },
                "required": ["container_name", "item_id", "partition_key"],
            },
        ),
        Tool(
            name="cosmosdb_item_query",  # Renamed table to container, simplified query
            description="Query items in a Cosmos DB container using SQL",  # Updated description
            inputSchema={
                "type": "object",
                "properties": {
                    "container_name": {  # Renamed from table_name
                        "type": "string",
                        "description": "Name of the Cosmos DB container",  # Updated description
                    },
                    "database_name": {
                        "type": "string",
                        "description": "Name of the Cosmos DB database (optional, defaults to 'defaultdb')",
                    },
                    "query": {
                        "type": "string",
                        "description": "Cosmos DB SQL query string",
                    },
                    "parameters": {
                        "type": "array",
                        "description": "Parameters for the SQL query (optional)",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "value": {},  # Value can be any type
                            },
                        },
                    },
                },
                "required": ["container_name", "query"],
            },
        ),
    ]

def get_app_configuration_tools() -> list[Tool]:
    return [
        Tool(
            name="app_configuration_kv_read",
            description="Read key-values from Azure App Configuration",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "The key to read (optional, use * for wildcards, e.g. 'app1/*')",
                    },
                    "label": {
                        "type": "string",
                        "description": "The label filter (optional, use '\\0' for no label, '*' for any label)",
                    },
                },
                "required": [],
            },
        ),
        Tool(
            name="app_configuration_kv_write",
            description="Write or update a key-value in Azure App Configuration",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "The key to write",
                    },
                    "value": {
                        "type": "string",
                        "description": "The value to store",
                    },
                    "label": {
                        "type": "string",
                        "description": "The label for the key-value (optional)",
                    },
                    "content_type": {
                        "type": "string",
                        "description": "Content type of the value (optional, e.g. 'application/json')",
                    },
                },
                "required": ["key", "value"],
            },
        ),
        Tool(
            name="app_configuration_kv_delete",
            description="Delete a key-value from Azure App Configuration",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "The key to delete",
                    },
                    "label": {
                        "type": "string",
                        "description": "The label of the key-value to delete (optional)",
                    },
                },
                "required": ["key"],
            },
        ),
    ]

def get_azure_tools() -> list[Tool]:
    return [
        *get_blob_storage_tools(), 
        *get_cosmosdb_tools(),
        *get_app_configuration_tools()
    ]
