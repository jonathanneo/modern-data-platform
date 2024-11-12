import os
from pathlib import Path
import json

from dagster_dbt import DbtCliResource
from dagster import AssetExecutionContext, DailyPartitionsDefinition, OpExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from .dbt_translator import CustomDagsterDbtTranslator

# dbt analytics
dbt_analytics_project_dir = Path(__file__).joinpath("..", "..", "..", "..", "..", "..", "dbt", "analytics").resolve()
dbt_analytics_resource = DbtCliResource(project_dir=os.fspath(dbt_analytics_project_dir))
dbt_analytics_manifest_path = (
    dbt_analytics_resource.cli(
        ["--quiet", "parse"],
        target_path=Path("target"),
    )
    .wait()
    .target_path.joinpath("manifest.json")
)
@dbt_assets(
    manifest=dbt_analytics_manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(),
)
def dbt_analytics(context: AssetExecutionContext, dbt_analytics_resource: DbtCliResource):
    yield from dbt_analytics_resource.cli(["build"], context=context).stream()

# dbt reporting
dbt_reporting_project_dir = Path(__file__).joinpath("..", "..", "..", "..", "..", "..", "dbt", "reporting").resolve()
dbt_reporting_resource = DbtCliResource(project_dir=os.fspath(dbt_reporting_project_dir))
dbt_reporting_manifest_path = (
    dbt_reporting_resource.cli(
        ["--quiet", "parse"],
        target_path=Path("target"),
    )
    .wait()
    .target_path.joinpath("manifest.json")
)
@dbt_assets(
    manifest=dbt_reporting_manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(),
)
def dbt_reporting(context: AssetExecutionContext, dbt_reporting_resource: DbtCliResource):
    yield from dbt_reporting_resource.cli(["build"], context=context).stream()

# dbt web_events
dbt_web_events_project_dir = Path(__file__).joinpath("..", "..", "..", "..", "..", "..", "dbt", "web_events").resolve()
dbt_web_events_resource = DbtCliResource(project_dir=os.fspath(dbt_web_events_project_dir))
dbt_web_events_manifest_path = (
    dbt_web_events_resource.cli(
        ["--quiet", "parse"],
        target_path=Path("target"),
    )
    .wait()
    .target_path.joinpath("manifest.json")
)
@dbt_assets(
    manifest=dbt_web_events_manifest_path,
    partitions_def=DailyPartitionsDefinition(start_date="2011-06-03", end_date="2011-12-21"),
    dagster_dbt_translator=CustomDagsterDbtTranslator(),
)
def dbt_web_events(context: OpExecutionContext, dbt_web_events_resource: DbtCliResource):
    start, end = context.partition_time_window
    dbt_vars = {"start_date": start.isoformat(), "end_date": end.isoformat()}
    dbt_build_args = ["build", "--vars", json.dumps(dbt_vars)]
    yield from dbt_web_events_resource.cli(dbt_build_args, context=context).stream()
