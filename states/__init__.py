class StatefulObject(object):
    states = []

    def _get_specific_state(self, state):
        if state.__class__ is str:
            return getattr(self, state, False)
        else:
            return state

    def _getCurrentState(self):
        try:
            return self.states[-1]
        except IndexError:
            return None

    def resetState(self):
        """ Reset our state back to the original class's behaviors. """

        self.states = []

    def getState(self, state=None):
        """ Get the current state, or the requested state if one is provided
            as the state argument.
        """

            # Gets a specific state
        if state is not None:
            return self._get_specific_state(state)

            # Gets the current state
        else:
            return self._getCurrentState()

    def gotoState(self, state):
        """ Ignores current state completely and sets the state to the state
            with the name provided.
        """

        next_state = self.getState(state) 

        if next_state:
            self.states = [next_state]

    def pushState(self, state):
        """ Appends the requested state to our state stack. """

        # Convert strings into objects
        state = self.getState(state)

        self.states.append(state)

    def popState(self):
        """ Pop a state from our list. """

        return self.states.pop()

    def __getattribute__(self, name):
        """ Overrides all attributes based on current state. """

        def derived(n):
            """ Because this was too verbose. """

            return object.__getattribute__(self, n)

        def state_factory(context, method):
            """ Factory for generating callable state handlers. """
            def handler(*args, **kwargs):
                method(context, *args, **kwargs)

            return handler

        current_state_index = len(derived('states')) - 1
        state_attribute = None

        while current_state_index > -1:
            current_state = derived('states')[current_state_index]
            state_attribute = getattr(current_state, name, None)

            if state_attribute is not None:
                if callable(state_attribute):
                    return state_factory(self, state_attribute)
                else:
                    return state_attribute
    
            current_state_index = current_state_index - 1

        return derived(name)

