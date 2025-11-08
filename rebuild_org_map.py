import pandas as pd

org_map = {'team_name': ['FinOps','Infra','Support','Security'], 
           'primary_areas': ['Payments,Billing','Deployment,Downtime','Customer queries,Account setup','Access,Encryption'], 
           'excluded_areas': ['Refunds','API logic','Code issues','UI bugs'], 
           'known_misconceptions': ['People assume FinOps owns refunds','Infra handles downtime, not logic errors','Support handles only Tier 1','Security doesn’t manage UI problems']}

df = pd.DataFrame(org_map)
df.to_csv("data/org_map_rebuild.csv", index=False)
print("✅ Org skillset map rebuilt successfully in ./data/org_map_rebuild.csv")
