from tests.test_secret_controller import test_secret_controller


class Health:
    project_url = ""
    container_url = ""

    def __init__(self):
        self.project_url = "https://github.com/OhadScripts/devops-challenge-ohad"
        self.container_url = "https://hub.docker.com/r/scr1pter/devops-challenge"

    def get_health_string(self):
        return "healthy" if self.check_health() else "Unhealthy!"

    @staticmethod
    def check_health():
        try:
            test_secret_controller()
            return True

        except AssertionError:
            return False

    def get_health_shot(self):
        return {
            "status": self.get_health_string(),
            "container": self.container_url,
            "project": self.project_url
        }
