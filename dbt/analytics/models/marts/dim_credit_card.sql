with salesorderheader as (
    select distinct creditcardid
    from {{ source('sales', 'salesorderheader') }}
    where creditcardid is not null
)

select
    {{ dbt_utils.generate_surrogate_key(['salesorderheader.creditcardid']) }} as creditcard_key,
    salesorderheader.creditcardid,
    creditcard.cardtype
from salesorderheader
inner join {{ source('sales', 'creditcard') }} as creditcard
    on salesorderheader.creditcardid = creditcard.creditcardid
