.. sip:method-description::
    :status: todo
    :pysig: e7d4b6e3f87ba9fe2928216c4f159b5b
    :realsig: (QEvent*)
    :digest: dcc3b645db6a8463d22dc9f5ab78afc2

This event handler can be reimplemented in a subclass to receive custom events. Custom events are user-defined events with a type value at least as large as the :sip:ref:`~PyQt6.QtCore.QEvent.Type.User` item of the :sip:ref:`~PyQt6.QtCore.QEvent.Type` enum, and is typically a :sip:ref:`~PyQt6.QtCore.QEvent` subclass. The event is passed in the *event* parameter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.event`, :sip:ref:`~PyQt6.QtCore.QEvent`.
