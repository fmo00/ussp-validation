class OirMocks:
    OIR_ID = "9d158f59-80b7-4c11-9c0c-8a2b4d936b2d"

    USSP_OIR_INJECTION_REQUEST_BODY = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "coordinates": [
                        [
                            [-38.96606107787872, -12.598713957988977],
                            [-38.96606107787872, -12.601582859887188],
                            [-38.96284242706122, -12.601582859887188],
                            [-38.96284242706122, -12.598713957988977],
                            [-38.96606107787872, -12.598713957988977],
                        ]
                    ],
                    "type": "Polygon",
                },
            }
        ],
    }

    USSP_GET_OIR_BY_ID_RESPONSE = {
        "operational_intent": {
            "reference": {
                "id": "2f8343be-6482-4d1b-a474-16847e01af1e",
                "flight_type": "VLOS",
                "manager": "uss1",
                "uss_availability": "Unknown",
                "version": 1,
                "state": "Accepted",
                "ovn": "9d158f59-80b7-4c11-9c0c-8a2b4d936b2d",
                "time_start": {"value": "1985-04-12T23:20:50.52Z", "format": "RFC3339"},
                "time_end": {"value": "1985-04-12T23:20:50.52Z", "format": "RFC3339"},
                "uss_base_url": "https://uss.example.com/utm",
                "subscription_id": "78ea3fe8-71c2-4f5c-9b44-9c02f5563c6f",
            },
            "details": {"volumes": [], "off_nominal_volumes": [], "priority": 0},
        }
    }

    DSS_GET_OIR_BY_ID_RESPONSE = {
        "operational_intent_reference": {
            "id": "2f8343be-6482-4d1b-a474-16847e01af1e",
            "flight_type": "VLOS",
            "manager": "uss1",
            "uss_availability": "Unknown",
            "version": 1,
            "state": "Accepted",
            "ovn": "9d158f59-80b7-4c11-9c0c-8a2b4d936b2d",
            "time_start": {"value": "1985-04-12T23:20:50.52Z", "format": "RFC3339"},
            "time_end": {"value": "1985-04-12T23:20:50.52Z", "format": "RFC3339"},
            "uss_base_url": "https://uss.example.com/utm",
            "subscription_id": "78ea3fe8-71c2-4f5c-9b44-9c02f5563c6f",
        }
    }
