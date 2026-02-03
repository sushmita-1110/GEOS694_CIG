# Assume you already have LLtoUTM() defined in your code above
ellipsoid = 23  # WGS-84

# Elvey Building coordinates
lat = 64.8598
lon = -147.8491

# Compute UTM
zone, easting, northing = LLtoUTM(ellipsoid, lat, lon)

print(f"Elvey Building UTM coordinates:")
print(f"Zone: {zone}")
print(f"Easting: {easting:.3f} m")
print(f"Northing: {northing:.3f} m")
