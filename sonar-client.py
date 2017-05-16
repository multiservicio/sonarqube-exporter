import requests

BASE_URL = 'http://local.dev:9000'

class Client:

    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
    
    def get_all_ids(self, endpoint):
        r = requests.get(BASE_URL + endpoint, auth=(self.user, self.passwd))
        data = r.json()
        ids = []
        for component in data['components']:
            ids.append(component['id'])
        return ids
    
    def get_all_available_metrics(self, endpoint):
        r = requests.get(BASE_URL + endpoint, auth=(self.user, self.passwd))
        data = r.json()
        metrics = []
        for metric in data['metrics']:
            metrics.append(metric['key'])
        return metrics
    
    def get_measures_by_component_id(self, endpoint):
        r = requests.get(BASE_URL + endpoint, auth=(self.user, self.passwd))
        data = r.json()
        return data['component']['measures']


client = Client('admin', 'admin')
ids = client.get_all_ids('/api/components/search?qualifiers=TRK')
print(ids)

metrics = client.get_all_available_metrics('/api/metrics/search')
print(metrics)

measures = client.get_measures_by_component_id('/api/measures/component?componentId=AVwRPRNPxAeEELfzG7wQ&metricKeys=ncloc,complexity,violations')
print(measures)