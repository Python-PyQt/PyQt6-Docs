.. sip:class-description::
    :status: todo
    :brief: Contains event parameters for expose events
    :digest: 6081606a55399794d1e3603503a7e0e6

The :sip:ref:`~PyQt6.QtGui.QExposeEvent` class contains event parameters for expose events.

Expose events are sent to windows when they move between the un-exposed and exposed states.

An exposed window is potentially visible to the user. If the window is moved off screen, is made totally obscured by another window, is minimized, or similar, an expose event is sent to the window, and isExposed() might change to false.

Expose events should not be used to paint. Handle :sip:ref:`~PyQt6.QtGui.QPaintEvent` instead.

The event handler :sip:ref:`~PyQt6.QtGui.QWindow.exposeEvent` receives expose events.
