import json
import os


IOC_FILE = os.path.join(
    os.path.dirname(__file__),
    "ioc_database.json"
)


def load_iocs():

    try:

        with open(
            IOC_FILE,
            "r"
        ) as f:

            return json.load(f)

    except:

        return []


def check_process_ioc(
    process_name
):

    process_name = process_name.lower()

    iocs = load_iocs()

    for ioc in iocs:

        if (
            ioc["type"] == "process"
            and
            ioc["value"].lower()
            == process_name
        ):

            return (
                True,
                ioc["severity"]
            )

    return (
        False,
        "NONE"
    )