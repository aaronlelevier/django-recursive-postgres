with recursive t(id) AS (
        select
            T3.id
        from {{db_table}} as T1
            join {{m2m_db_table}} as T2 on T1.id = T2.{{m2m_reverse_name}}
            join {{db_table}} as T3 on T3.id = T2.{{m2m_column_name}}
        where T1.id = '{{pk}}'
    union
        select
            T3.id
        from t
            join {{m2m_db_table}} as T2 on t.id = T2.{{m2m_reverse_name}}
            join {{db_table}} as T3 on T3.id = T2.{{m2m_column_name}}
)
select *
from t;