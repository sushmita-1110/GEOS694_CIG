def _utm_letter_designator(lat):
    """
    Returns the UTM letter designator for a given latitude.
    Returns 'Z' if latitude is outside UTM limits (-80 to 84).
    """
    if not -80 <= lat <= 84:
        return 'Z'
    # UTM letters from C to X, omitting O and I
    letters = "CDEFGHJKLMNPQRSTUVWX"
    return letters[int((lat + 80) // 8)]


if __name__ == "__main__":
    # Test a set of latitudes
    latitudes = [-80, -45, 0, 8, 45, 72]
    print(*[f"{lat}: {_utm_letter_designator(lat)}" for lat in latitudes], sep="\n")
