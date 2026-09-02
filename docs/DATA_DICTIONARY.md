# Launch Library 2 Data Dictionary

## Response Envelope

| Field | Observed type | What it means |
|---|---|---|
| `count` | int | The total number of launch records that match the request, even when only one small page is returned |
| `next` | string URL or null | The full URL to request the next page of matching results; it is null when there is no next page |
| `previous` | string URL or null | The full URL to request the previous page of matching results; it is null when the current page is the first page |
| `results` | list of dicts | The actual launch records returned for the current page |

## Launch Record Fields

| Field path | Observed type | Can it be null in my five-record sample? | Why it might matter |
| :---: | :---: | :---: | :---: |
| `id` | string | No in my five-record sample | identifies one specific launch |
| `name` | string | No in my five-record sample | human-readable launch name |
| `net` | ISO 8601 UTC timestamp string | No in my five-record sample | planned “no earlier than” launch time; it is not a guaranteed final launch time and can change |
| `status` | dict and nested dicts| Doesn't appear to be able to be null | provides the current launch status of the launch |
| `launch_service_provider` | dict | No in my five-record sample | identifies the organization/service provider responsible for the launch |
| `rocket` | dict and nested dicts | No in my five-record sample | provides information specifically about the rocket being used ie: id, name, variant |
| `mission` | dict w/ nested dicts | No in my five-record sample | provides mission information ie: id, orbit, the celestial body |
| `pad` | dict w/ nested dicts | No in my five-record sample | provides locational launch information |
| `last_updated` | timestamp string | No in my five-record sample | It records when LL2 last updated that launch record |