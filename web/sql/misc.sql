-- UNWANTED DUPLICATES
-- select visitor_id, referer_id, count(*)
-- from evasion_visitorreferer
-- group by visitor_id, referer_id
-- having count(*) > 1

-- select id, visitor_id, referer_id
-- from evasion_visitorreferer
-- where
-- (visitor_id=2094 and referer_id=1) or
-- (visitor_id=129 and referer_id=16) or
-- (visitor_id=350 and referer_id=8)


-- MESSAGES THROUGH SPECIFIC REFERERS
-- %nuit%amour% - %chambre%jacuzzi% - %suite%jacuzzi% - ...
select distinct r.host, count(distinct m.id) as c
from
  evasion_message as m, 
  evasion_referer as r,
  evasion_visitorreferer as vr,
  evasion_visitor as v
where
  m.visitor_id = vr.visitor_id and
  vr.referer_id = r.id 
--   and (r.host like '%suite%jacuzzi%' or r.host like '%chambre%jacuzzi%' or r.host like '%nuit%amour%')
--   and (r.host not like '%suite%jacuzzi%' and r.host not like '%chambre%jacuzzi%' and r.host not like '%nuit%amour%')
  and r.host != 'evasion-antillaise.fr'
  and m.date_message > '2014-09-24' and m.date_message < '2014-10-09' -- 2 weeks nuit-amour
--   and m.date_message > '2014-08-24' and m.date_message < '2014-09-08' -- 2 weeks chambre/suiteavecjacuzzi
group by r.host
order by c desc
