class CliffEnv:
    def __init__(self, rows, cols, cliffs):
        self.rows = rows
        self.cols = cols
        self.cliffs = cliffs
        self.start = (rows - 1, 0)
        self.goal = (rows - 1, cols - 1)
        self.reset()

    def reset(self):
        self.agent = self.start
        return self._state()

    def _state(self):
        return self.agent[0] * self.cols + self.agent[1]

    def step(self, action):
        r, c = self.agent

        if action == 0: r -= 1
        elif action == 1: c += 1
        elif action == 2: r += 1
        elif action == 3: c -= 1

        r = max(0, min(self.rows - 1, r))
        c = max(0, min(self.cols - 1, c))
        self.agent = (r, c)

        if self.agent in self.cliffs:
            return self.reset(), -100, False, {}

        if self.agent == self.goal:
            return self._state(), 1, True, {}

        return self._state(), -1, False, {}
