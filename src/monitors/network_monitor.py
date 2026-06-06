import psutil


def get_connection_count(pid):
    """
    Returns the number of active network connections
    for a given process.
    """

    try:
        process = psutil.Process(pid)

        connections = process.net_connections()

        return len(connections)

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess
    ):
        return 0

    except Exception:
        return 0