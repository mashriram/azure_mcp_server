# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
# Use an official Python image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set working directory
WORKDIR /app

# Install build system and dependencies
RUN pip install --upgrade pip && \
    pip install hatchling

# Copy the project files into the container
COPY . /app

# Install the project in editable mode (if necessary)
RUN hatch build && pip install .

# Set up environment variables for AWS credentials
ENV AZURE_STORAGE_ACCOUNT_URL="your_storage_account_url"
ENV AZURE_CLIENT_SECRET="your_client_secret"
ENV AZURE_CLIENT_ID="your_client_id"
ENV AZURE_TENANT_ID="your_tenant_id"
ENV AZURE_COSMOSDB_URL="your_cosmosdb_url"
ENV AZURE_COSMOSDB_KEY="your_cosmos_db_primary_read_write_key"
ENV AZURE_SAS_CREDENTIAL="your_azure_sas_credential"
ENV AZURE_CONNECTION_STRING="your_azure_connection_string:starts_with:BlobEndpoint="
ENV AZURE_COSMOSDB_ENDPOINT="your_cosmos_db_account_endpoint:starts_with:AccountEndpoint="

# Run the MCP server
CMD ["hatch", "run", "mcp_server_azure_cmd"]
