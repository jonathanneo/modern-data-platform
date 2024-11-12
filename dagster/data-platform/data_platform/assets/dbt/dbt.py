import os
from pathlib import Path

from dagster_dbt import DbtCliResource
from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslatorSettings
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
