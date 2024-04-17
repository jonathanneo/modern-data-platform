from dagster import Definitions, load_assets_from_modules

from .assets.fivetran import fivetran
from .assets.dbt import dbt
from .assets.dbt.dbt import dbt_analytics_resource, dbt_reporting_resource

fivetran_assets = load_assets_from_modules([fivetran])
dbt_assets = load_assets_from_modules([dbt])

defs = Definitions(
    assets=[ *dbt_assets], #  *fivetran_assets,
    resources={
        "dbt_analytics_resource": dbt_analytics_resource,
        "dbt_reporting_resource": dbt_reporting_resource,
    }
)
