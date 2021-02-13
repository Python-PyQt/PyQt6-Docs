.. sip:method-description::
    :status: todo
    :pysig: 063b4bd94a2c6c9a999b20cc06cd4567
    :realsig: (const QPainterPath&) const
    :digest: ec132dfcc54bb92b7da2c56632300dcc

Returns ``true`` if the current path intersects at any point the given path *p*. Also returns ``true`` if the current path contains or is contained by any part of *p*.

Set operations on paths will treat the paths as areas. Non-closed paths will be treated as implicitly closed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.contains`.
