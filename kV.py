from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

key_vault_name = "triof-vault"
key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"
# The name of the secret you added in the Key Vault
secret_name = "customvision-key-caro"
secret_url = "customvision-uri-caro"

credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)

retrieved_secret_name = secret_client.get_secret(secret_name)
retrieved_secret_url = secret_client.get_secret(secret_url)
print(f"The secret key is: {retrieved_secret_name.value}")
print(f"The secret url is: {retrieved_secret_url.value}")
