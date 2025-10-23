.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 1bebe081e2a004f0d6febdba356555a4

Enables or disables length caching according to the value of *enabled*.

Enabling caching speeds up repeated calls to the member functions involving path length and percentage values, such as :sip:ref:`~PyQt6.QtGui.QPainterPath.length`, :sip:ref:`~PyQt6.QtGui.QPainterPath.percentAtLength`, :sip:ref:`~PyQt6.QtGui.QPainterPath.pointAtPercent` etc., at the cost of some extra memory usage for storage of intermediate calculations. By default it is disabled.

Disabling caching will release any allocated cache memory.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.isCachingEnabled`, :sip:ref:`~PyQt6.QtGui.QPainterPath.length`, :sip:ref:`~PyQt6.QtGui.QPainterPath.percentAtLength`, :sip:ref:`~PyQt6.QtGui.QPainterPath.pointAtPercent`, :sip:ref:`~PyQt6.QtGui.QPainterPath.trimmed`.
