#-*- coding: utf-8 -*-

from yuantacat.pipeline.state.state import State

import logging

class InitialState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
    
    def run(self):
        self.logger.info('run initial state')
