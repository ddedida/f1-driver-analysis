create or replace table analytics.circuits as
select
    circuit_id,
    cast(circuit_ref as varchar(255)) as circuit_ref,
    cast(name as varchar(255)) as name,
    cast(location as varchar(255)) as location,
    cast(country as varchar(255)) as country,
    lat,
    lng,
    cast(alt as float) as alt,
    cast(url as varchar(255)) as url,
from raw.circuits;

create or replace table analytics.constructors as
select
    constructor_id,
    cast(constructor_ref as varchar(255)) as constructor_ref,
    cast(name as varchar(255)) as name,
    cast(nationality as varchar(255)) as nationality,
    cast(url as varchar(255)) as url
from raw.constructors;

create or replace table analytics.constructor_results as
select
    constructor_result_id,
    race_id,
    constructor_id,
    points
from raw.constructor_results;

create or replace table analytics.constructor_standings as
select
    constructor_standing_id,
    race_id,
    constructor_id,
    points,
    position,
    cast(position_text as varchar(16)) as position_text,
    wins
from raw.constructor_standings;

create or replace table analytics.drivers as
select
    driver_id,
    cast(driver_ref as varchar(255)) as driver_ref,
    try_cast(number as number) as driver_number,
    case
        when code like '%\\N' or code is null
            then upper(left(surname, 3))
        else cast(code as varchar(16))
    end as driver_code,
    (cast(forename as varchar(255)) || ' ' || cast(surname as varchar(255))) as driver_name,
    cast(forename as varchar(255)) as forename,
    cast(surname as varchar(255)) as surname,
    dob as date_of_birth,
    cast(nationality as varchar(255)) as nationality,
    cast(url as varchar(255)) as url
from raw.drivers;

create or replace table analytics.driver_standings as
select
    driver_standing_id,
    race_id,
    driver_id,
    points,
    position,
    cast(position_text as varchar(16)) as position_text,
    wins
from raw.driver_standings;

create or replace table analytics.lap_times as
select
    lap_time_id,
    race_id,
    driver_id,
    lap,
    position,
    cast(time as varchar(255)) as time,
    milliseconds
from raw.lap_times;

create or replace table analytics.qualifying as
select
    qualifying_id,
    race_id,
    driver_id,
    constructor_id,
    try_cast(number as number) as driver_number,
    position,
    q1 as q1_time,
    q2 as q2_time,
    q3 as q3_time
from raw.qualifying;

create or replace table analytics.races as
select
    race_id,
    year,
    round,
    circuit_id,
    cast(name as varchar(255)) as name,
    date,
    cast(time as varchar(255)) as time,
    cast(url as varchar(255)) as url,
    try_cast(fp1_date as date) as fp1_date,
    try_cast(fp1_time as time) as fp1_time,
    try_cast(fp2_date as date) as fp2_date,
    try_cast(fp2_time as time) as fp2_time,
    try_cast(fp3_date as date) as fp3_date,
    try_cast(fp3_time as time) as fp3_time,
    try_cast(quali_date as date) as quali_date,
    try_cast(quali_time as time) as quali_time,
    try_cast(sprint_date as date) as sprint_date,
    try_cast(sprint_time as time) as sprint_time,
from raw.races;

create or replace table analytics.race_results as
select
    result_id as race_result_id,
    race_id,
    driver_id,
    constructor_id,
    try_cast(number as number) as driver_number,
    grid,
    try_cast(position as number) as position,
    cast(position_text as varchar(16)) as position_text,
    position_order,
    points,
    laps,
    cast(time as varchar(255)) as time,
    try_cast(milliseconds as number) as milliseconds,
    try_cast(fastest_lap as number) as fastest_lap,
    cast(fastest_lap_time as varchar(255)) as fastest_lap_time,
    try_cast(rank as number) as fastest_lap_rank,
    try_cast(fastest_lap_speed as float) as fastest_lap_speed,
    status_id
from raw.results;

create or replace table analytics.sprint_results as
select
    result_id as sprint_result_id,
    race_id,
    driver_id,
    constructor_id,
    try_cast(number as number) as driver_number,
    grid,
    try_cast(position as number) as position,
    cast(position_text as varchar(16)) as position_text,
    position_order,
    points,
    laps,
    cast(time as varchar(255)) as time,
    try_cast(milliseconds as number) as milliseconds,
    try_cast(fastest_lap as number) as fastest_lap,
    cast(fastest_lap_time as varchar(255)) fastest_lap_time,
    status_id
from raw.sprint_results;

create or replace table analytics.status as
select
    status_id,
    cast(status as varchar(255)) as status
from raw.status;