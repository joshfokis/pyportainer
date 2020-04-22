import json
import requests


class PyPortainer():
    def __init__(self, portainer_endpoint, verifySSL=True):
        self.portainer_endpoint = portainer_endpoint+"/api"
        self.verifySSL = verifySSL

    def login(self, username, password):
        r = requests.post(
            f"{self.portainer_endpoint}/auth",
            data=json.dumps({"Username": username, "Password": password}),
            verify=self.verifySSL)
        j = r.json()
        self.token = j.get("jwt")

    def get_dockerhub_info(self):
        r = requests.get(
            f"{self.portainer_endpoint}/dockerhub",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def put_dockerhub_info(self, options):
        r = requests.put(
            f"{self.portainer_endpoint}/dockerhub",
            data=json.dumps(options),
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def get_status(self):
        r = requests.get(
            f"{self.portainer_endpoint}/status",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def get_endpoints(self):
        r = requests.get(
            f"{self.portainer_endpoint}/endpoints",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def new_endpoint(self, options):
        r = requests.post(
            f"{self.portainer_endpoint}/endpoints",
            data=json.dumps(options),
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def get_endpoint(self, identifier):
        r = requests.get(
            f"{self.portainer_endpoint}/endpoints/{identifier}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def update_endpoint(self, identifier, options):
        r = requests.put(
            f"{self.portainer_endpoint}/endpoints/{identifier}",
            data=json.dumps(options),
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def delete_endpoint(self, identifier):
        r = requests.delete(
            f"{self.portainer_endpoint}/endpoints/{identifier}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def endpoint_job(self, identifier, options):
        r = requests.post(
            f"{self.portainer_endpoint}/endpoints/{identifier}/job",
            data=json.dumps(options),
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def access_endpoint(self, identifier, options):
        """Possibly depricated no info in docs"""
        #TODO: Verify if this API call is available
        r = requests.put(
            f"{self.portainer_endpoint}/endpoints/{identifier}/access",
            data=json.dumps(options),
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def get_stacks(self, endpoint):
        r = requests.get(
            f"{self.portainer_endpoint}/endpoints/{endpoint}/stacks",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def new_stack(self, endpoint, options):
        r = requests.post(
            f"{self.portainer_endpoint}/endpoints/{endpoint}/stacks",
            data=json.dumps(options),
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def get_stack(self, endpoint, stack):
        r = requests.get(
            f"{self.portainer_endpoint}/endpoints/{endpoint}/stacks/{stack}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def update_stack(self, endpoint, stack, options):
        r = requests.put(
            f"{self.portainer_endpoint}/endpoints/{endpoint}/stacks/{stack}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def delete_stack(self, endpoint, stack):
        r = requests.delete(
            f"{self.portainer_endpoint}/endpoints/{endpoint}/stacks/{stack}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def get_stackfile(self, endpoint, stack):
        uri = f"/endpoints/{endpoint}/stacks/{stack}/stackfile"
        r = requests.get(
            f"{self.portainer_endpoint}{uri}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def get_endpoint_containers(self, identifier):
        uri = f"/endpoints/{identifier}/docker/containers/json"
        r = requests.get(
            f"{self.portainer_endpoint}{uri}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def start_endpoint_container(self, identifier, container_id):
        uri = f"/endpoints/{identifier}/docker/containers/{container_id}/start"
        r = requests.post(
            f"{self.portainer_endpoint}{uri}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()

    def stop_endpoint_container(self, identifier, container_id):
        uri = f"/endpoints/{identifier}/docker/containers/{container_id}/stop"
        r = requests.post(
            f"{self.portainer_endpoint}{uri}",
            headers={"Authorization": f"Bearer {self.token}"},
            verify=self.verifySSL)
        return r.json()
