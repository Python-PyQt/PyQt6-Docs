.. sip:class-description::
    :status: todo
    :brief: Describes a pinch gesture made by the user
    :digest: 9b231553a1d93474c13b54730d74d091

The :sip:ref:`~PyQt6.QtWidgets.QPinchGesture` class describes a pinch gesture made by the user.

A pinch gesture is a form of touch user input in which the user typically touches two points on the input device with a thumb and finger, before moving them closer together or further apart to change the scale factor, zoom, or level of detail of the user interface.

For an overview of gesture handling in Qt and information on using gestures in your applications, see the `Gestures in Widgets and Graphics View <https://doc.qt.io/qt-6/gestures-overview.html>`_ document.

.. image:: ../../../images/pinchgesture.png

Instead of repeatedly applying the same pinching gesture, the user may continue to touch the input device in one place, and apply a second touch to a new point, continuing the gesture. When this occurs, gesture events will continue to be delivered to the target object, containing an instance of :sip:ref:`~PyQt6.QtWidgets.QPinchGesture` in the :sip:ref:`~PyQt6.QtCore.Qt.GestureState.GestureUpdated` state.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPanGesture`, :sip:ref:`~PyQt6.QtWidgets.QSwipeGesture`.
