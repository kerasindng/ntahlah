# Copyright (c) 2022 Indomie Project
""" Init file which loads all of the assistant modules """
from indomie import LOGS
from indomie.utils._base import IndomieDB

kio = IndomieDB()


def __list_asst_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    asst_modules = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return asst_modules


ASST_MODULES = sorted(__list_asst_modules())
LOGS.info(f"Connecting to {kio.name}...")
if kio.ping():
    LOGS.info(f"Connected to {kio.name} Successfully!")
LOGS.info("Starting To Load Asst Plugins")
LOGS.info(
    f"Succesfully Load {len(ASST_MODULES)} Asst Plugins",
)
__asst__ = ASST_MODULES + ["ASST_MODULES"]
