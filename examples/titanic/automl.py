import cflearn
import numpy as np

tr_file = "./train.csv"
te_file = "./test.csv"


def write_submissions(name: str, predictions_: np.ndarray) -> None:
    with open(te_file, "r") as f:
        f.readline()
        id_list = [line.strip().split(",")[0] for line in f]
    with open(name, "w") as f:
        f.write("PassengerId,Survived\n")
        for test_id, prediction in zip(id_list, predictions_.ravel()):
            f.write(f"{test_id},{prediction}\n")


# Score : achieved ~0.79
auto = cflearn.Auto("clf")
auto.fit(tr_file, extra_config={"data_config": {"label_name": "Survived"}})
predictions = auto.pattern.predict(te_file)
write_submissions("automl.csv", predictions)
