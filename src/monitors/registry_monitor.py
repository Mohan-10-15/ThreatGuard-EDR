import winreg


def scan_registry():

    entries = []

    registry_paths = [
        (
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run"
        ),
        (
            winreg.HKEY_LOCAL_MACHINE,
            r"Software\Microsoft\Windows\CurrentVersion\Run"
        )
    ]

    for hive, path in registry_paths:

        try:

            key = winreg.OpenKey(
                hive,
                path
            )

            count = winreg.QueryInfoKey(
                key
            )[1]

            for i in range(count):

                try:

                    name, value, _ = winreg.EnumValue(
                        key,
                        i
                    )

                    entries.append({
                        "name": name,
                        "value": value
                    })

                except Exception:
                    continue

        except Exception:
            continue

    return entries