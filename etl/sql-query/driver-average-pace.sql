-- DRIVER AVERAGE PACE WITH GAP TO FASTEST
create or replace view driver_avg_pace_with_gap as
with driver_avg_pace as (
    select
        d.driver_id,
        d.driver_code,
        d.driver_name as driver,
        c.constructor_id,
        c.name as constructor,
        lt.race_id,
        r.name as race,
        r.year as year,
        avg(lt.milliseconds) as avg_lap_time
    from lap_times lt
    join drivers d on lt.driver_id = d.driver_id
    join race_results rr
        on rr.race_id = lt.race_id
       and rr.driver_id = lt.driver_id
    join constructors c on rr.constructor_id = c.constructor_id
    join races r on lt.race_id = r.race_id
    where lt.milliseconds > 0
    group by d.driver_id, d.driver_code, d.driver_name, c.constructor_id, c.name, lt.race_id, race, year
)
select
    dap.driver_id,
    dap.driver,
    dap.driver_code,
    dap.constructor_id,
    dap.constructor,
    dap.race_id,
    dap.race,
    dap.year,
    dap.avg_lap_time,
    (dap.avg_lap_time - min(dap.avg_lap_time) over (partition by dap.race_id)) / 1000 as gap_to_fastest
from driver_avg_pace dap;