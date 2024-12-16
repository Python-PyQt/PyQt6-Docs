.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a mouse event
    :digest: 79438f458ce8479eac08d3a78502a4b0

The :sip:ref:`~PyQt6.QtGui.QHoverEvent` class contains parameters that describe a mouse event.

Mouse events occur when a mouse cursor is moved into, out of, or within a widget, and if the widget has the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_Hover` attribute.

The function pos() gives the current cursor position, while :sip:ref:`~PyQt6.QtGui.QHoverEvent.oldPos` gives the old mouse position.

There are a few similarities between the events :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverEnter` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverLeave`, and the events :sip:ref:`~PyQt6.QtCore.QEvent.Type.Enter` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.Leave`. However, they are slightly different because we do an update() in the event handler of HoverEnter and HoverLeave.

:sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverMove` is also slightly different from :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`. Let us consider a top-level window A containing a child B which in turn contains a child C (all with mouse tracking enabled):

.. image:: ../../../images/hoverevents.png

Now, if you move the cursor from the top to the bottom in the middle of A, you will get the following :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove` events:

#. A::MouseMove

#. B::MouseMove

#. C::MouseMove

You will get the same events for :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverMove`, except that the event always propagates to the top-level regardless whether the event is accepted or not. It will only stop propagating with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_NoMousePropagation` attribute.

In this case the events will occur in the following way:

#. A::HoverMove

#. A::HoverMove, B::HoverMove

#. A::HoverMove, B::HoverMove, C::HoverMove
