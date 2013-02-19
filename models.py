TAXONOMY = {
    "types": {
        "launch": {"contains": ["launch_vehicle", "ground_systems"]},
        "launch_vehicle": {"contains": ["project"]},
        "ground_systems": {"contains": ["project"]},
        "project": {"contains": ["part", "software"]},
        "part": {"contains": ["status"]},
        "software": {"contains": ["status"]},
        "status": {"contains": []},
    },
    "top": "launch",
}
