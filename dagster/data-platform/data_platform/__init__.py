from dagster import Definitions, load_assets_from_modules

from .assets.fivetran import fivetran
from .assets.dbt import dbt
from .assets.dbt.dbt import dbt_analytics_resource, dbt_reporting_resource, dbt_web_events_resource
from .assets.census import census
from .assets.census.census import configured_census_resource
from .jobs import fivetran_job, dbt_analytics_job, dbt_reporting_job, dbt_web_events_job, fivetran_analytics_reporting_job
from .schedules import fivetran_schedule, dbt_analytics_schedule, dbt_reporting_schedule, dbt_web_events_schedule, dim_date_schedule, fivetran_analytics_reporting_schedule

fivetran_assets = load_assets_from_modules([fivetran])
dbt_assets = load_assets_from_modules([dbt])
census_assets = load_assets_from_modules([census])

defs = Definitions(
    assets=[*fivetran_assets, *dbt_assets, *census_assets],
    resources={
        "dbt_analytics_resource": dbt_analytics_resource,
        "dbt_reporting_resource": dbt_reporting_resource,
        "dbt_web_events_resource": dbt_web_events_resource,
        "census": configured_census_resource,
    },
    jobs=[fivetran_job, dbt_analytics_job, dbt_reporting_job, dbt_web_events_job, fivetran_analytics_reporting_job],
    schedules=[fivetran_schedule, dbt_analytics_schedule, dbt_reporting_schedule, dbt_web_events_schedule, fivetran_analytics_reporting_schedule, dim_date_schedule],
)
