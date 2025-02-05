from . import OirInjectionRequestDto


class UsspOirMocks:
    OIR_ID: str = "9d158f59-80b7-4c11-9c0c-8a2b4d936b2d"

    INVALID_OIR_ID: str = "000000"

    OIR_INJECTION_REQUEST_BODY = {
        "extents": [
            {
                "volume": {
                    "outline_circle": {
                        "center": {"lng": -118.456, "lat": 34.123},
                        "radius": {"value": 300.183, "units": "M"},
                    },
                    "outline_polygon": {
                        "vertices": [
                            {"lng": -118.456, "lat": 34.123},
                            {"lng": -118.456, "lat": 34.123},
                            {"lng": -118.456, "lat": 34.123},
                        ]
                    },
                    "altitude_lower": {
                        "value": 100000,
                        "reference": "W84",
                        "units": "M",
                    },
                    "altitude_upper": {
                        "value": 100000,
                        "reference": "W84",
                        "units": "M",
                    },
                },
                "time_start": {
                    "value": "1985-04-12T23:20:50.52Z",
                    "format": "RFC3339",
                },
                "time_end": {
                    "value": "1985-04-12T23:20:50.52Z",
                    "format": "RFC3339",
                },
            }
        ],
        "key": ["9d158f59-80b7-4c11-9c0c-8a2b4d936b2d"],
        "state": "Accepted",
        "uss_base_url": "https://uss.example.com/utm",
        "subscription_id": "2f8343be-6482-4d1b-a474-16847e01af1e",
        "new_subscription": {
            "uss_base_url": "string",
            "notify_for_constraints": False,
        },
    }
