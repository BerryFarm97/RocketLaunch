import httpx

URL_TIMEOUT = 10
UPCOMING_LAUNCHES_URL = "https://lldev.thespacedevs.com/2.3.0/launches/upcoming/"


def get_api_data(url, params, timeout):
    response = httpx.get(url, params=params, timeout=timeout)
    response.raise_for_status()

    try:
        data = response.json()
    except ValueError:
        raise ValueError("JSON response is malformed.")
    

    if not isinstance(data, dict):
        raise ValueError("Expected the API response to be a JSON object.")
    if "results" not in data:
        raise ValueError("Expected the API response to contain a results list.")
    if not isinstance(data["results"], list):
        raise ValueError("Expected the JSON response object 'results' to be a list.")

    return data


def main():
    params = {
        "limit": 1,
    }

    api_response = get_api_data(UPCOMING_LAUNCHES_URL, params, URL_TIMEOUT)
    print(api_response["results"])


if __name__ == "__main__":
    main()
