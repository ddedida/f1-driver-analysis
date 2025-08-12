drop database formula_one_world_championship;
create database formula_one_world_championship;

create table seasons(
	"year" int primary key,
	url varchar(255)
);

create table circuits(
	circuit_id int primary key,
	circuit_ref varchar(255),
	"name" varchar(255),
	"location" varchar(255),
	country varchar(255),
	lat decimal(12, 8),
	lng decimal(12, 8),
	alt int,
	url varchar(255)
);

create table constructors(
	constructor_id int primary key,
	constructor_ref varchar(255),
	"name" varchar(255),
	nationality varchar(255),
	url varchar(255)
);

create table drivers(
	driver_id int primary key,
	driver_ref varchar(255),
	"number" varchar(255),
	code varchar(255),
	forename varchar(255),
	surname varchar(255),
	dob date,
	nationality varchar(255),
	url varchar(255)
);

create table status(
	status_id int primary key,
	status varchar(255)
);

create table races(
	race_id int primary key,
	"year" int,
	round int,
	circuit_id int,
	"name" varchar(255),
	"date" date,
	"time" varchar(255),
	url varchar(255),
	fp1_date varchar(255),
	fp1_time varchar(255),
	fp2_date varchar(255),
	fp2_time varchar(255),
	fp3_date varchar(255),
	fp3_time varchar(255),
	quali_date varchar(255),
	quali_time varchar(255),
	sprint_date varchar(255),
	sprint_time varchar(255)
);

create table constructor_results(
	constructor_result_id int primary key,
	race_id int,
	constructor_id int,
	points int,
	status varchar(255),
	foreign key (race_id) references races(race_id),
	foreign key (constructor_id) references constructors(constructor_id)
);

create table constructor_standings(
	constructor_standing_id int primary key,
	race_id int,
	constructor_id int,
	points int,
	"position" int,
	position_text varchar(255),
	wins int,
	foreign key (race_id) references races(race_id),
	foreign key (constructor_id) references constructors(constructor_id)
);

create table driver_standings(
	driver_standing_id int primary key,
	race_id int,
	driver_id int,
	points int,
	"position" int,
	position_text varchar(255),
	wins int,
	foreign key (race_id) references races(race_id),
	foreign key (driver_id) references drivers(driver_id)
);

create table lap_times(
	lap_time_id int generated always as identity primary key,
	race_id int,
	driver_id int,
	lap int,
	"position" int,
	"time" varchar(255),
	milliseconds int,
	foreign key (race_id) references races(race_id),
	foreign key (driver_id) references drivers(driver_id)
);

create table pit_stops(
	pit_stop_id int generated always as identity primary key,
	race_id int,
	driver_id int,
	stop int,
	lap int,
	"time" time,
	duration varchar(255),
	milliseconds int,
	foreign key (race_id) references races(race_id),
	foreign key (driver_id) references drivers(driver_id)
);

create table qualifying(
	qualifying_id int primary key,
	race_id int,
	driver_id int,
	constructor_id int,
	"number" varchar(255),
	"position" int,
	q1 varchar(255),
	q2 varchar(255),
	q3 varchar(255),
	foreign key (race_id) references races(race_id),
	foreign key (driver_id) references drivers(driver_id),
	foreign key (constructor_id) references constructors(constructor_id)
);

create table results(
	result_id int primary key,
	race_id int,
	driver_id int,
	constructor_id int,
	"number" varchar(255),
	grid int,
	"position" varchar(255),
	position_text varchar(255),
	position_order int,
	points int,
	laps int,
	time varchar(255),
	milliseconds varchar(255),
	fastest_lap varchar(255),
	"rank" varchar(255),
	fastest_lap_time varchar(255),
	fastest_lap_speed varchar(255),
	status_id int,
	foreign key (race_id) references races(race_id),
	foreign key (driver_id) references drivers(driver_id),
	foreign key (constructor_id) references constructors(constructor_id),
	foreign key (status_id) references status(status_id)
);

create table sprint_results(
	result_id int primary key,
	race_id int,
	driver_id int,
	constructor_id int,
	"number" varchar(255),
	grid int,
	"position" varchar(255),
	position_text varchar(255),
	position_order int,
	points int,
	laps int,
	time varchar(255),
	milliseconds varchar(255),
	fastest_lap varchar(255),
	fastest_lap_time varchar(255),
	status_id int,
	foreign key (result_id) references results(result_id),
	foreign key (race_id) references races(race_id),
	foreign key (driver_id) references drivers(driver_id),
	foreign key (constructor_id) references constructors(constructor_id),
	foreign key (status_id) references status(status_id)
);