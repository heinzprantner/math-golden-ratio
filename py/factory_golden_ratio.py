# -*- coding: latin-1 -*-
"""

"""

import numpy as np
import math_golden_ratio_t_golden_ratio

class factory_golden_ratio():
    """
    """

    def __init__(self):
      """
      """
      self.run()

    def count(self,delta,s,l):
      """
      callback function for each iteration of recursive gr calc step,
      count number of iterations
      """
      self._c += 1

    def documentation(self):
      """
      document the golden ratio calculation iterations as text
      """
      print('golden ratio calculation - recursive')
      print('    whole w : {}'.format(self._w))
      print('  smaller s : {:06.3f}'.format(self._s))
      print('   larger l : {:06.3f}'.format(self._l))
      print('        tau : {:06.3f} ... precision'.format(self._tau))
      print(' iterations :')
      i = 0
      for e in self._series_sle:
        print('   [{}] E_LE:{: 05.3f} s:{: 06.4f} l:{: 06.4f}'.format(i,e[2],e[0],e[1]))
        i += 1

    def run(self):
      """
      calculate golden ratio with use of error function,
      recursive call with adoption of s,l based on deviation (error function result)
      until a given precision, granularity tau is reached.
      we start with 'random', initial s and l 
      """
      self.setup()
      self._s = self._w/2-self._tau 
      self._l = self._w - self._s
      (self._s,self._l) = self._golden_ratio.GR_LE(self._s,self._l,cb=self.callback)
      self.documentation()

    def setup(self):
      """
      setup for recursive golden ratio calculation
      """
      self._tau = 1e-3
      self._c = 0
      self._i = 0
      self._w = 1.0
      self._golden_ratio = math_golden_ratio_t_golden_ratio.class_t_golden_ratio(tau=self._tau)
      self._s = self._w/2-self._tau 
      self._l = self._w - self._s
      (self._s,self._l) = self._golden_ratio.GR_LE(self._s,self._l,cb=self.count)
      self._series_sle = np.zeros((self._c,3))

    def callback(self,delta,s,l):
      """
      callback function for each iteration of recursive gr calc step,
      """
      self._series_sle[self._i] = (s,l,delta)
      self._i += 1

if __name__ == "__main__":
  factory = factory_golden_ratio()

