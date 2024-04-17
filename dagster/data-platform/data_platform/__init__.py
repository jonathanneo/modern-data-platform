from dagster import Definitions, load_assets_from_modules

from .assets.fivetran import fivetran

fivetran_assets = load_assets_from_modules([fivetran])

defs = Definitions(
    assets=[*fivetran_assets],
)
