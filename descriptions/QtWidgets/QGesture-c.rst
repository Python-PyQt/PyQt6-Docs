.. sip:class-description::
    :status: todo
    :brief: Represents a gesture, containing properties that describe the corresponding user input
    :digest: 63e4c92d4a2434c4e63f3b37fc9d5db3

The :sip:ref:`~PyQt6.QtWidgets.QGesture` class represents a gesture, containing properties that describe the corresponding user input.

Gesture objects are not constructed directly by developers. They are created by the :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer` object that is registered with the application; see :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.registerRecognizer`.

For an overview of gesture handling in Qt and information on using gestures in your applications, see the `Gestures in Widgets and Graphics View <https://doc.qt.io/qt-6/gestures-overview.html>`_ document.

.. _qgesture-gesture-properties:

Gesture Properties
------------------

The class has a list of properties that can be queried by the user to get some gesture-specific arguments. For example, the pinch gesture has a scale factor that is exposed as a property.

Developers of custom gesture recognizers can add additional properties in order to provide additional information about a gesture. This can be done by adding new dynamic properties to a :sip:ref:`~PyQt6.QtWidgets.QGesture` object, or by subclassing the :sip:ref:`~PyQt6.QtWidgets.QGesture` class (or one of its subclasses).

.. _qgesture-lifecycle-of-a-gesture-object:

Lifecycle of a Gesture Object
-----------------------------

A :sip:ref:`~PyQt6.QtWidgets.QGesture` instance is implicitly created when needed and is owned by Qt. Developers should never destroy them or store them for later use as Qt may destroy particular instances of them and create new ones to replace them.

The registered gesture recognizer monitors the input events for the target object via its :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.recognize` function, updating the properties of the gesture object as required.

The gesture object may be delivered to the target object in a :sip:ref:`~PyQt6.QtWidgets.QGestureEvent` if the corresponding gesture is active or has just been canceled. Each event that is delivered contains a list of gesture objects, since support for more than one gesture may be enabled for the target object. Due to the way events are handled in Qt, gesture events may be filtered by other objects.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureEvent`, :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer`.
