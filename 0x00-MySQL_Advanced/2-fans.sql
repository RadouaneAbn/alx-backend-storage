-- This script ranks coutry origin of bands, ordered by the number of fans.

select origin, SUM(fans) as nb_fans
	from metal_bands
	group by origin
	order by nb_fans desc;
