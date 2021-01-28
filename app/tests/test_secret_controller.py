import requests

server_url = "127.0.0.1"
server_port = "5000"


def test_secret_controller():
    controller_path = "secret"
    expected_result = ["code_name", "secret_code"]

    result = requests.get(f"http://{server_url}:{server_port}/{controller_path}").json().keys()
    result = list(result)
    result.sort()

    assert expected_result == result
