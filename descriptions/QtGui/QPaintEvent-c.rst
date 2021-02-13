.. sip:class-description::
    :status: todo
    :brief: Contains event parameters for paint events
    :digest: 12687cff39eb32423f62ff495d225a47

The :sip:ref:`~PyQt6.QtGui.QPaintEvent` class contains event parameters for paint events.

Paint events are sent to widgets that need to update themselves, for instance when part of a widget is exposed because a covering widget was moved.

The event contains a :sip:ref:`~PyQt6.QtGui.QPaintEvent.region` that needs to be updated, and a :sip:ref:`~PyQt6.QtGui.QPaintEvent.rect` that is the bounding rectangle of that region. Both are provided because many widgets cannot make much use of :sip:ref:`~PyQt6.QtGui.QPaintEvent.region`, and :sip:ref:`~PyQt6.QtGui.QPaintEvent.rect` can be much faster than :sip:ref:`~PyQt6.QtGui.QPaintEvent.region`.boundingRect().

.. _qpaintevent-automatic-clipping:

Automatic Clipping
------------------

Painting is clipped to :sip:ref:`~PyQt6.QtGui.QPaintEvent.region` during the processing of a paint event. This clipping is performed by Qt's paint system and is independent of any clipping that may be applied to a :sip:ref:`~PyQt6.QtGui.QPainter` used to draw on the paint device.

As a result, the value returned by :sip:ref:`~PyQt6.QtGui.QPainter.clipRegion` on a newly-constructed :sip:ref:`~PyQt6.QtGui.QPainter` will not reflect the clip region that is used by the paint system.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter`.
