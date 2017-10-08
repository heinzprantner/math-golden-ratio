"""

domain  : math
package : golden_ratio
version : 0.0.1
class   : t_golden_ratio
yaml    : resources/classes/math/math_golden_ratio_classes.yml
factory : class_factory.py

"""

_domain  = "math"
_package = "golden_ratio"
_version = "0.0.1"


class class_t_golden_ratio():
    """Class Definition for t_golden_ratio
    
    yaml: resources/classes/math/math_golden_ratio_classes.yml
    
    entries:
    """

    def __init__(self,tau = 1e-3):
      """
      golden ratio functions implementations
      - tau ... tolerance, precision, granularity (default 0.001)
      """
      self._tau  = tau 
      pass


    def E_BE(self,s,l):
      """
      golden ratio error function (E) for big endian (BE) notation
      relating the larger to the smaller
      - s ... smaller
      - l ... larger
      - return delta aligned to granularity
      """
      if s>l: return self.E_BE(l,s)
      if s == 0: return -100
      if l == 0: return -100
      delta = (((s+l)/l)-(l/s)) 
      return delta-delta%self._tau

    def GR_LE(self,s,l,cb=None):
      """
      golden ratio function (GR) for little endian (LE) notation
      return modified s,l for a given pair of s,l
      - w ... whole
      - s ... smaller
      - l ... larger
      """
      if s>l: return self.GR_LE(l,s)
      delta = self.E_LE(s,l)
      if (abs(delta)>self._tau):
        if cb: cb(delta,s,l) 
        l = l+delta*s 
        s = s-delta*s
        return self.GR_LE(s,l,cb=cb)
      if cb: cb(delta,s,l) 
      return (s,l)

    def E_LE_norm(self,s,l):
      """
      golden ratio error function (E) for little endian (LE) notation
      relating the smaller to the larger
      normalized to range 0..1
      - s ... smaller
      - l ... larger
      - return delta aligned to granularity
      """
      if s>l: return self.E_LE_norm(l,s)
      delta = ((s/l)-(l/(s+l)))
      delta = delta-delta%self._tau
      delta_norm = ((delta + 1.0) * 100.0) / 150.0
      return delta_norm

    def E_LE(self,s,l):
      """
      golden ratio error function (E) for little endian (LE) notation
      relating the smaller to the larger
      - s ... smaller
      - l ... larger
      - return delta aligned to granularity
      """
      if s>l: return self.E_LE(l,s)
      delta = ((s/l)-(l/(s+l)))
      return delta-delta%self._tau


