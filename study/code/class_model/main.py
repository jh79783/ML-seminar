import numpy as np
import class_model.dataset_mode as dm
import class_model.mlp_model as mm
import time

np.random.seed(9999)

# def randomize():
#     np.random.seed(time.time())


def main():
    data = dm.Regression('abalone', 'binary')
    model = mm.MlpModel("abalone_model", data, [20,10])
    model.exec_all(epoch_count=50, report=10, learning_rate=0.001)


if __name__ == '__main__':
    # randomize()
    main()


