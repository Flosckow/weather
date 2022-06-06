from operator import ge
import geocoder as gcdr
from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longtitude: float


def get_gps_coordinates() -> Coordinates:
    geo = gcdr.ip('me')
    coordinate =  geo.latlng
    return Coordinates(latitude=coordinate[0], longtitude=coordinate[1])

get_gps_coordinates()
