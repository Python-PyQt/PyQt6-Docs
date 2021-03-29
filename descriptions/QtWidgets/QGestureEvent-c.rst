.. sip:class-description::
    :status: todo
    :brief: The description of triggered gestures
    :digest: 6da29ca0beecb54e6a52794fb87affd3

The :sip:ref:`~PyQt6.QtWidgets.QGestureEvent` class provides the description of triggered gestures.

The :sip:ref:`~PyQt6.QtWidgets.QGestureEvent` class contains a list of gestures, which can be obtained using the :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.gestures` function.

The gestures are either active or canceled. A list of those that are currently being executed can be obtained using the :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.activeGestures` function. A list of those which were previously active and have been canceled can be accessed using the :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.canceledGestures` function. A gesture might be canceled if the current window loses focus, for example, or because of a timeout, or for other reasons.

If the event handler does not accept the event by calling the generic :sip:ref:`~PyQt6.QtCore.QEvent.accept` function, all individual :sip:ref:`~PyQt6.QtWidgets.QGesture` object that were not accepted and in the :sip:ref:`~PyQt6.QtCore.Qt.GestureState.GestureStarted` state will be propagated up the parent widget chain until a widget accepts them individually, by calling :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.accept` for each of them, or an event filter consumes the event.

.. _qgestureevent-further-reading:

Further Reading
---------------

For an overview of gesture handling in Qt and information on using gestures in your applications, see the `Gestures in Widgets and Graphics View <https://doc.qt.io/qt-6/gestures-overview.html>`_ document.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGesture`, :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabGesture`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject.grabGesture`.
