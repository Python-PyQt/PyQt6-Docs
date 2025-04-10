.. sip:module-description::
    :status: done
    :brief:  Classes for creating and executing state graphs

The :sip:ref:`~PyQt6.QtStateMachine` module provides an API and execution model
that can be used to effectively embed the elements and semantics of statecharts
in PyQt applications.  The framework integrates tightly with PyQt's meta-object
system so that, for example, transitions between states can be triggered by
signals, and states can be configured to set properties and invoke methods on a
:sip:ref:`~PyQt6.QtCore.QObject`.  PyQt's event system is used to drive the
state machines.
