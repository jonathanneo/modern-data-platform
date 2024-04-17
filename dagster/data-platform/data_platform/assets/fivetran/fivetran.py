from dagster_fivetran import FivetranResource, load_assets_from_fivetran_instance
from dagster import EnvVar

# Pull API key and secret from environment variables
fivetran_instance = FivetranResource(
    api_key=EnvVar("FIVETRAN_API_KEY"),
    api_secret=EnvVar("FIVETRAN_API_SECRET"),
)

fivetran_assets = load_assets_from_fivetran_instance(fivetran_instance, connector_to_group_fn=lambda _ : "fivetran")
