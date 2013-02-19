TAXONOMY = {
    "types": {
        "launch": {"contains": ["launch_vehicle", "ground_systems"], "fields": [{"name": "launch_date", "type": "datetime"}]},
        "launch_vehicle": {"contains": ["project"]},
        "ground_systems": {"contains": ["project"]},
        "project": {"contains": ["part", "software"]},
        "part": {"contains": []},
        "software": {"contains": []},
    },
    "top": {
        "site": "launch"
    }
}
