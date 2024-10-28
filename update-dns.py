# Description: This script updates the DNS records of a Google Cloud DNS managed zone.
from google.oauth2 import service_account  # type: ignore
import googleapiclient.discovery  # type: ignore
names = [f"{i}.fwebtraincse.com." for i in range(669, 700)]
rrdatas = ["34.75.172.129", "35.185.62.129"]
key_file = "key.json"

credentials = service_account.Credentials.from_service_account_file(key_file)

def update_dns_record(project: str, managed_zone: str, record_set: dict) -> dict:
    """Updates a DNS record."""
    dns_service = googleapiclient.discovery.build("dns", "v1", credentials=credentials)
    
    change_body = {
        "additions": [record_set],
        "deletions": []
    }
    
    request = dns_service.changes().create(
        project=project,
        managedZone=managed_zone,
        body=change_body
    )
    
    response = request.execute()
    print("Updated DNS record: " + str(response))
    return response

for name in names:
    record_set = {
        "name": name,
        "type": "A",
        "ttl": 5,
        "rrdatas": rrdatas
    }
    update_dns_record("cse-us-341516", "fwebtraincse-com", record_set)




