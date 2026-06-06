from collections import deque


class ThreatTrend:

    def __init__(self):

        self.data = deque(
            maxlen=30
        )

    def add(
        self,
        threat_count
    ):

        try:

            self.data.append(
                int(threat_count)
            )

        except:

            self.data.append(0)

    def get_data(
        self
    ):

        return list(
            self.data
        )

    def get_latest(
        self
    ):

        if len(self.data) == 0:

            return 0

        return self.data[-1]

    def get_max(
        self
    ):

        if len(self.data) == 0:

            return 0

        return max(
            self.data
        )

    def get_average(
        self
    ):

        if len(self.data) == 0:

            return 0

        return round(

            sum(self.data)

            /

            len(self.data),

            2

        )

    def clear(
        self
    ):

        self.data.clear()