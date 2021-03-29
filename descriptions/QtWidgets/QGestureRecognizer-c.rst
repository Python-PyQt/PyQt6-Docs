.. sip:class-description::
    :status: todo
    :brief: The infrastructure for gesture recognition
    :digest: 651df81def1ac61a5275ce745198a59f

The :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer` class provides the infrastructure for gesture recognition.

Gesture recognizers are responsible for creating and managing :sip:ref:`~PyQt6.QtWidgets.QGesture` objects and monitoring input events sent to `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ and :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject` subclasses. :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer` is the base class for implementing custom gestures.

Developers that only need to provide gesture recognition for standard gestures do not need to use this class directly. Instances will be created behind the scenes by the framework.

For an overview of gesture handling in Qt and information on using gestures in your applications, see the `Gestures in Widgets and Graphics View <https://doc.qt.io/qt-6/gestures-overview.html>`_ document.

.. _qgesturerecognizer-recognizing-gestures:

Recognizing Gestures
--------------------

The process of recognizing gestures involves filtering input events sent to specific objects, and modifying the associated :sip:ref:`~PyQt6.QtWidgets.QGesture` objects to include relevant information about the user's input.

Gestures are created when the framework calls :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.create` to handle user input for a particular instance of a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject` subclass. A :sip:ref:`~PyQt6.QtWidgets.QGesture` object is created for each widget or item that is configured to use gestures.

Once a :sip:ref:`~PyQt6.QtWidgets.QGesture` has been created for a target object, the gesture recognizer will receive events for it in its :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.recognize` handler function.

When a gesture is canceled, the :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.reset` function is called, giving the recognizer the chance to update the appropriate properties in the corresponding :sip:ref:`~PyQt6.QtWidgets.QGesture` object.

.. _qgesturerecognizer-supporting-new-gestures:

Supporting New Gestures
-----------------------

To add support for new gestures, you need to derive from :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer` to create a custom recognizer class, construct an instance of this class, and register it with the application by calling :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.registerRecognizer`. You can also subclass :sip:ref:`~PyQt6.QtWidgets.QGesture` to create a custom gesture class, or rely on dynamic properties to express specific details of the gesture you want to handle.

Your custom :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer` subclass needs to reimplement the :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.recognize` function to handle and filter the incoming input events for `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ and :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject` subclasses. Although the logic for gesture recognition is implemented in this function, you can store persistent information about the state of the recognition process in the :sip:ref:`~PyQt6.QtWidgets.QGesture` object supplied. The :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.recognize` function must return a value of QGestureRecognizer::Result that indicates the state of recognition for a given gesture and target object. This determines whether or not a gesture event will be delivered to a target object.

If you choose to represent a gesture by a custom :sip:ref:`~PyQt6.QtWidgets.QGesture` subclass, you will need to reimplement the :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.create` function to construct instances of your gesture class. Similarly, you may need to reimplement the :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.reset` function if your custom gesture objects need to be specially handled when a gesture is canceled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGesture`.
