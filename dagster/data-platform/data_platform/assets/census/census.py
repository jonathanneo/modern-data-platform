from dagster import asset, AssetKey, AutoMaterializePolicy
from dagster_census import census_resource

configured_census_resource = census_resource.configured(
    {
        "api_key": {"env": "CENSUS_API_KEY"},
    }
)

@asset(
    group_name="census", 
    deps=[AssetKey(["reports", "sales"])],
    required_resource_keys={"census"},
    auto_materialize_policy=AutoMaterializePolicy.eager(),
    kinds={"s3","census"},
)
def sales_export(context):
    # Census recently changed their Plans such that API calls now require a paid plan starting from $350 USD/month.
    # context.resources.census.trigger_sync_and_poll(sync_id=780230)
    print("mock succeed")
