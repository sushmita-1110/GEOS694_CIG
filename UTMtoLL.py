from math import sin, cos, tan, sqrt, pi

_rad2deg = 180.0 / pi
_EquatorialRadius = 2
_eccentricitySquared = 3

_ellipsoid = [
    #  id, Ellipsoid name, Equatorial Radius, square of eccentricity
    # first once is a placeholder only, To allow array indices to match id
    # numbers
    [-1, "Placeholder", 0, 0],
    [1, "Airy", 6377563, 0.00667054],
    [2, "Australian National", 6378160, 0.006694542],
    [3, "Bessel 1841", 6377397, 0.006674372],
    [4, "Bessel 1841 (Nambia] ", 6377484, 0.006674372],
    [5, "Clarke 1866", 6378206, 0.006768658],
    [6, "Clarke 1880", 6378249, 0.006803511],
    [7, "Everest", 6377276, 0.006637847],
    [8, "Fischer 1960 (Mercury] ", 6378166, 0.006693422],
    [9, "Fischer 1968", 6378150, 0.006693422],
    [10, "GRS 1967", 6378160, 0.006694605],
    [11, "GRS 1980", 6378137, 0.00669438],
    [12, "Helmert 1906", 6378200, 0.006693422],
    [13, "Hough", 6378270, 0.00672267],
    [14, "International", 6378388, 0.00672267],
    [15, "Krassovsky", 6378245, 0.006693422],
    [16, "Modified Airy", 6377340, 0.00667054],
    [17, "Modified Everest", 6377304, 0.006637847],
    [18, "Modified Fischer 1960", 6378155, 0.006693422],
    [19, "South American 1969", 6378160, 0.006694542],
    [20, "WGS 60", 6378165, 0.006693422],
    [21, "WGS 66", 6378145, 0.006694542],
    [22, "WGS-72", 6378135, 0.006694318],
    [23, "WGS-84", 6378137, 0.00669438]
]


def UTMtoLL(ReferenceEllipsoid, northing, easting, zone):
    # Converts UTM coordinates to lat/long. Equations from USGS Bulletin 1532.

    k0 = 0.9996
    a = _ellipsoid[ReferenceEllipsoid][_EquatorialRadius]
    eccSquared = _ellipsoid[ReferenceEllipsoid][_eccentricitySquared]

    e1 = (1 - sqrt(1 - eccSquared)) / (1 + sqrt(1 - eccSquared))

    x = easting - 500000.0
    y = northing

    ZoneLetter = zone[-1]
    ZoneNumber = int(zone[:-1])

    if ZoneLetter < 'N':
        y -= 10000000.0 

    LongOrigin = (ZoneNumber - 1) * 6 - 180 + 3
    eccPrimeSquared = eccSquared / (1 - eccSquared)

    M = y / k0
    mu = M / (a * (1 - eccSquared / 4 - 3 * eccSquared * eccSquared /
                   64 - 5 * eccSquared * eccSquared * eccSquared / 256))

    phi1Rad = (mu + (3 * e1 / 2 - 27 * e1 * e1 * e1 / 32) * sin(2 * mu) +
               (21 * e1 * e1 / 16 - 55 * e1 * e1 * e1 * e1 / 32) *
               sin(4 * mu) + (151 * e1 * e1 * e1 / 96) * sin(6 * mu))
    phi1 = phi1Rad * _rad2deg

    N1 = a / sqrt(1 - eccSquared * sin(phi1Rad) * sin(phi1Rad))
    T1 = tan(phi1Rad) * tan(phi1Rad)
    C1 = eccPrimeSquared * cos(phi1Rad) * cos(phi1Rad)
    R1 = a * (1 - eccSquared) / pow(1 - eccSquared *
                                    sin(phi1Rad) * sin(phi1Rad), 1.5)
    D = x / (N1 * k0)

    Lat = phi1Rad - (N1 * tan(phi1Rad) / R1) *\
        (D * D / 2 -
         (5 + 3 * T1 + 10 * C1 - 4 * C1 * C1 - 9 * eccPrimeSquared) *
         D * D * D * D / 24 + (61 + 90 * T1 + 298 * C1 + 45 * T1 * T1 - 252 *
                               eccPrimeSquared - 3 * C1 * C1) *
         D * D * D * D * D * D / 720)
    Lat = Lat * _rad2deg

    Long = (D - (1 + 2 * T1 + C1) * D * D * D / 6 +
            (5 - 2 * C1 + 28 * T1 - 3 * C1 * C1 + 8 *
             eccPrimeSquared + 24 * T1 * T1) *
            D * D * D * D * D / 120) / cos(phi1Rad)
    Long = LongOrigin + Long * _rad2deg
    return (Lat, Long)
# from GEOCUBIT


if __name__ == "__main__":
    # UTMtoLL(ellipsoid, n, e, z)
    # from CUBIT_GEOCUBIT/geocubitlib/LatLongUTMconversion.py get (z, e, n) is (18T 500000.0 4982950.400444571) 
    lat, lon = UTMtoLL(23, 4982950.400444571, 500000.0, "18T").   
    print(lat, lon)