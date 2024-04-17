select
    {{ dbt_utils.generate_surrogate_key(['customer.customerid']) }} as customer_key,
    customer.customerid,
    person.businessentityid as personbusinessentityid,
    concat(coalesce(person.firstname, ''), ' ', coalesce(person.middlename, ''), ' ', coalesce(person.lastname, '')) as fullname,
    store.businessentityid as storebusinessentityid,
    store.storename
from {{ source('adventureworks_sales', 'customer') }} as customer
left join {{ source('adventureworks_person', 'person') }} as person
    on customer.personid = person.businessentityid
left join {{ source('adventureworks_sales', 'store') }} as store
    on customer.storeid = store.businessentityid
