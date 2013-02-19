TAXONOMY = {
    "types": {
        "launch": {"contains": ["launch_vehicle", "ground_system"]},
        "launch_vehicle": {"contains": ["project"]},
        "ground_system": {"contains": ["project"]},
        "project": {"contains": ["part", "software"]},
        "part": {"contains": []},
        "software": {"contains": []},
    },
    "top": "launch",
}
