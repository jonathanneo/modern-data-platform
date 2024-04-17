select
    {{ dbt_utils.generate_surrogate_key(['address.addressid']) }} as address_key,
    address.addressid,
    address.city as city_name,
    stateprovince.name as state_name,
    countryregion.name as country_name
from {{ source('person', 'address') }} as address
left join {{ source('person', 'stateprovince') }} as stateprovince
    on address.stateprovinceid = stateprovince.stateprovinceid
left join {{ source('person', 'countryregion') }} as countryregion
    on stateprovince.countryregioncode = countryregion.countryregioncode
