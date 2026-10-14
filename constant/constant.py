import os
from pathlib import Path
import streamlit as st

QGI_ROOT_DIR_PATH        = str(Path(__file__).resolve().parent.parent)
DATA_DIR                 = Path(__file__).resolve().parent.parent / "data"
PPR_PATH                 = QGI_ROOT_DIR_PATH + "/data/ppr/ppr.csv"
EVENTS_TXTS_FOLDER_PATH  = QGI_ROOT_DIR_PATH + "/data/events/"
COUNTRIES_CSV_PATH       = QGI_ROOT_DIR_PATH + "/data/country.csv"
COUNTRIES_PATTERNS_PATH  = QGI_ROOT_DIR_PATH + "/data/countries/"
COUNTRY_EVENTS_PATH      = QGI_ROOT_DIR_PATH + "/data/events/"
MATCHING_EVENTS_CSV_PATH = QGI_ROOT_DIR_PATH + "/data/matching_events.csv"

