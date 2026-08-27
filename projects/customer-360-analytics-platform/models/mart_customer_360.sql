select
  c.company_id,
  c.company_name,
  c.industry,
  count(distinct ct.contact_id) as contacts,
  count(distinct case when tk.status <> 'closed' then tk.ticket_id end) as open_tickets,
  sum(case when d.stage = 'closed_won' then d.amount_usd else 0 end) as closed_won_revenue_usd
from companies c
left join contacts ct on c.company_id = ct.company_id
left join deals d on c.company_id = d.company_id
left join tickets tk on c.company_id = tk.company_id
group by 1, 2, 3;
