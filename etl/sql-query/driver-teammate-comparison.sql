-- DRIVER AND HIS TEAMMATE POINTS COMPARISON
create or replace view driver_teammate_comparison as
with driver_results as (
    select 
        rr.driver_id,
        d.driver_name as driver,
        rr.constructor_id,
        c.name as constructor,
        rr.points as race_points,
        COALESCE(sr.points, 0) as sprint_points,
        rr.points + COALESCE(sr.points, 0) as total_points,
        r.race_id,
        r.name as race,
        r.year
    from races r
    join race_results rr 
        on r.race_id = rr.race_id
    left join sprint_results sr 
        on r.race_id = sr.race_id 
       and rr.driver_id = sr.driver_id
    join drivers d 
        on rr.driver_id = d.driver_id
    join constructors c 
        on rr.constructor_id = c.constructor_id
),
teammate_comparison as (
    select
        dr1.driver_id,
        dr1.driver as driver,
        dr1.total_points as driver_points,
        dr2.driver_id as teammate_id,
        dr2.driver as teammate,
        dr2.total_points as teammate_points,
        dr1.constructor_id,
        dr1.constructor,
        dr1.total_points + dr2.total_points as constructor_points,
        dr1.race_id,
        dr1.race,
        dr1.year,
    from driver_results dr1
    join driver_results dr2
        on dr1.race_id = dr2.race_id
        and dr1.constructor_id = dr2.constructor_id
        and dr1.driver_id <> dr2.driver_id
)
select
    driver_id,
    driver,
    sum(driver_points) as driver_points,
    teammate_id,
    teammate,
    sum(teammate_points) as teammate_points,
    constructor_id,
    constructor
from teammate_comparison
group by driver_id, driver, teammate_id, teammate, constructor_id, constructor
order by driver_id asc;