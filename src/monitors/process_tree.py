import psutil

def get_process_tree():

    process_tree = []

    for proc in psutil.process_iter(
        ["pid", "ppid", "name"]
    ):

        try:

            process_tree.append({
                "pid": proc.info["pid"],
                "ppid": proc.info["ppid"],
                "name": proc.info["name"]
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return process_tree