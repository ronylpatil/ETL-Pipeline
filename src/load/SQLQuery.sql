use sampledb;

select *
from yellow_processed;


-- What are the peak hours for taxi usage?
-- From 13:00-17:00 is pick hours  
select top 5 pickup_hours, count(1) 'no_of_rides'
from (select *, DATEPART(hour, tpep_pickup_datetime) 'pickup_hours'
from yellow_processed) t
group by pickup_hours
order by no_of_rides desc


-- How does passenger count affect the trip fare?
select passenger_count, avg(total_amount) 'avg_total_amount', avg(cost_per_passanger) 'avg_cost_per_pass'
from yellow_processed
group by passenger_count
order by passenger_count


-- What are the trends in usage over the year?
select DATEPART(year, tpep_pickup_datetime) 'trip_year', count(1) 'trip_count'
from yellow_processed
group by DATEPART(year, tpep_pickup_datetime)
order by trip_count


