from typing import Any, Mapping, Optional

from dagster import AssetKey
from dagster_dbt import DagsterDbtTranslator


class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    
    @classmethod
    def get_group_name(cls, dbt_resource_props: Mapping[str, Any]) -> Optional[str]:
        """
        Translates the project's database name into dagster's group name.
        Dagster asset groups are used to denote logical boundaries between groups of assets.
        In our use-case, we use dagster asset groups to represent dbt projects. 1 dagster asset group == 1 dbt project.

        :param dbt_resource_props: A single dbt resource based on https://docs.getdbt.com/reference/artifacts/manifest-json#resource-details
        :returns: a dagster group name
        """
        return "dbt_" + dbt_resource_props.get("package_name")

    @classmethod
    def get_tags(cls, dbt_resource_props: Mapping[str, Any]) -> Mapping[str, str]:
        tags: dict = dbt_resource_props.get("meta", {}).get("dagster", {}).get("tags", {})
        return {key: str(tags[key]) for key in tags.keys()}
