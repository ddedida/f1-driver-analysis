-- DRIVER LAP TIME
create or replace view driver_lap_time as
select
    lt.lap_time_id,
    d.driver_id,
    d.driver_name,
    d.driver_code,
    rr.driver_number,
    c.constructor_id,
    c.name as constructor,
    r.race_id,
    r.name as race,
    r.year as year,
    rr.grid,
    lt.lap,
    lt.position,
    lt.time,
    lt.milliseconds
from lap_times lt
join drivers d
    on lt.driver_id = d.driver_id
join races r
    on lt.race_id = r.race_id
join race_results rr
    on r.race_id = rr.race_id
    AND d.driver_id = rr.driver_id 
join constructors c
    on rr.constructor_id = c.constructor_id;