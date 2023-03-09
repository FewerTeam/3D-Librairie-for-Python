"""Errors file for the project Python-3D-Libs"""

#ERRORS CLASS
class UnknowModeNameError(Exception):
    pass

class ArgumentError(Exception):
    pass

class Object3DError(Exception):
    pass

class CubePointsError(Object3DError):
    pass

class PointError(Exception):
    pass

class NotTestedCodeWarning(Warning):
    pass
