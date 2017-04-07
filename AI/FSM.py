# Finite State Machine


class FiniteStateMachine (object):
    """
    A Finite State Machine base class.
    Objects that are run with FSMs should inherit from this class.
    """
    def __init__(self, state_manager):
        """
        Initialize a FSM
        :param state_manager: A method that manages the FSM. A state_manager can re-assign itself.
        """
        self.run_state = None
        self.set_state(state_manager)

    def set_state(self, state_manager):
        self.run_state = state_manager
