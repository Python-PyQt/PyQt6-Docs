.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: cc0e72c404d8a2a20b17b90ffe4e7314

Returns ``true`` if the pen is cosmetic; otherwise returns ``false``.

Cosmetic pens are used to draw strokes that have a constant width regardless of any transformations applied to the :sip:ref:`~PyQt6.QtGui.QPainter` they are used with. Drawing a shape with a cosmetic pen ensures that its outline will have the same thickness at different scale factors.

A zero width pen is cosmetic by default.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPen.setCosmetic`, :sip:ref:`~PyQt6.QtGui.QPen.widthF`.
