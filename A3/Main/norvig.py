class HiddenMarkovModel:
    """A Hidden markov model which takes Transition model and Sensor model as inputs"""

    def __init__(self, transition_model, sensor_model, prior=None):
        self.transition_model = transition_model
        self.sensor_model = sensor_model
        self.prior = prior or [0.5, 0.5]

    def sensor_dist(self, ev):
        if ev is True:
            return self.sensor_model[0]
        else:
            return self.sensor_model[1]


def forward(HMM, fv, ev):
    prediction = vector_add(scalar_vector_product(fv[0], HMM.transition_model[0]),
                            scalar_vector_product(fv[1], HMM.transition_model[1]))
    sensor_dist = HMM.sensor_dist(ev)

    return normalize(element_wise_product(sensor_dist, prediction))
