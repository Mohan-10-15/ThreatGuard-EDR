import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class AIEngine:

    def __init__(self):

        data = pd.DataFrame({
            "cpu": [1, 5, 10, 20, 40, 60, 80],
            "memory": [1, 3, 5, 10, 20, 40, 60],
            "connections": [0, 1, 2, 5, 10, 20, 50],
            "label": [0, 0, 0, 0, 1, 1, 1]
        })

        X = data[
            [
                "cpu",
                "memory",
                "connections"
            ]
        ]

        y = data["label"]

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        self.model.fit(X, y)

    def predict_score(
        self,
        cpu,
        memory,
        connections
    ):

        input_data = pd.DataFrame(
            [{
                "cpu": cpu,
                "memory": memory,
                "connections": connections
            }]
        )

        score = self.model.predict_proba(
            input_data
        )[0][1]

        return round(score * 100, 2)


ai_engine = AIEngine()