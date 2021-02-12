.. sip:class-description::
    :status: todo
    :brief: The base class of all event classes. Event objects contain event parameters
    :digest: 9a1442e68106be7ea6b5d936c527781e

The :sip:ref:`~PyQt6.QtCore.QEvent` class is the base class of all event classes. Event objects contain event parameters.

Qt's main event loop (\ :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`) fetches native window system events from the event queue, translates them into QEvents, and sends the translated events to :sip:ref:`~PyQt6.QtCore.QObject`\ s.

In general, events come from the underlying window system (\ :sip:ref:`~PyQt6.QtCore.QEvent.spontaneous` returns ``true``), but it is also possible to manually send events using :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendEvent` and :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent` (\ :sip:ref:`~PyQt6.QtCore.QEvent.spontaneous` returns ``false``).

:sip:ref:`~PyQt6.QtCore.QObject` receive events by having their :sip:ref:`~PyQt6.QtCore.QObject.event` function called. The function can be reimplemented in subclasses to customize event handling and add additional event types; QWidget::event() is a notable example. By default, events are dispatched to event handlers like :sip:ref:`~PyQt6.QtCore.QObject.timerEvent` and QWidget::mouseMoveEvent(). :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter` allows an object to intercept events destined for another object.

The basic :sip:ref:`~PyQt6.QtCore.QEvent` contains only an event type parameter and an "accept" flag. The accept flag set with :sip:ref:`~PyQt6.QtCore.QEvent.accept`, and cleared with :sip:ref:`~PyQt6.QtCore.QEvent.ignore`. It is set by default, but don't rely on this as subclasses may choose to clear it in their constructor.

Subclasses of :sip:ref:`~PyQt6.QtCore.QEvent` contain additional parameters that describe the particular event.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.event`, :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendEvent`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.
