# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
    datapath = os.path.dirname(os.path.abspath(mlproject.__file__)) + '/data'
    lon1,lat1,lon2,lat2 = 40.730610,-73.935242,37.773972,-122.431297
    assert haversine(lon1, lat1, lon2, lat2) == 5390.83454979928

