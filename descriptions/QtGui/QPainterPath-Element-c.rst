.. sip:class-description::
    :status: todo
    :brief: QPainterPath::Element class specifies the position and type of a subpath
    :digest: 7e0a1283dcbfe1abfd613e44bae3617d

The :sip:ref:`~PyQt6.QtGui.QPainterPath.Element` class specifies the position and type of a subpath.

Once a :sip:ref:`~PyQt6.QtGui.QPainterPath` object is constructed, subpaths like lines and curves can be added to the path (creating :sip:ref:`~PyQt6.QtGui.QPainterPath.ElementType.LineToElement` and :sip:ref:`~PyQt6.QtGui.QPainterPath.ElementType.CurveToElement` components).

The lines and curves stretch from the currentPosition() to the position passed as argument. The currentPosition() of the :sip:ref:`~PyQt6.QtGui.QPainterPath` object is always the end position of the last subpath that was added (or the initial start point). The moveTo() function can be used to move the currentPosition() without adding a line or curve, creating a :sip:ref:`~PyQt6.QtGui.QPainterPath.ElementType.MoveToElement` component.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath`.
