select visitor_id, referer_id, count(*)
from evasion_visitorreferer
group by visitor_id, referer_id
having count(*) > 1

--select id, visitor_id, referer_id
--from evasion_visitorreferer
--where
-- (visitor_id=2094 and referer_id=1) or
-- (visitor_id=129 and referer_id=16) or
-- (visitor_id=350 and referer_id=8)

