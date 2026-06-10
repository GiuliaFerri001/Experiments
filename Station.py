Station = {"name": "Skagen", "temp_c": 9.3, "wind_ms": 14.1, "raining": True}
Station["temp_c"] = 11.0
Station["pressure"] = 1008
Station.items()
update = {"temp_c": 10.5, "raining": False} 
Merge = {**Station, **update}
print(Merge)

for key,value in Station.items():
    print(f"{key}: {value}")
