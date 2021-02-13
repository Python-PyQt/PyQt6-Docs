.. sip:class-description::
    :status: todo
    :brief: Event sent by the input context to input objects
    :digest: d6a2eea2381e1a622bd2e8da796d50f7

The :sip:ref:`~PyQt6.QtGui.QInputMethodQueryEvent` class provides an event sent by the input context to input objects.

It is used by the input method to query a set of properties of the object to be able to support complex input method operations as support for surrounding text and reconversions.

:sip:ref:`~PyQt6.QtGui.QInputMethodQueryEvent.queries` specifies which properties are queried.

The object should call :sip:ref:`~PyQt6.QtGui.QInputMethodQueryEvent.setValue` on the event to fill in the requested data before calling accept().
