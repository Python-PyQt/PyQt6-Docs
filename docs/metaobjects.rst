Other Support for Dynamic Meta-objects
======================================

PyQt5 creates a :sip:ref:`~PyQt5.QtCore.QMetaObject` instance for any Python
sub-class of :sip:ref:`~PyQt5.QtCore.QObject` without the need for the
equivalent of Qt's ``Q_OBJECT`` macro.  Most of a
:sip:ref:`~PyQt5.QtCore.QMetaObject` is populated automatically by defining
signals, slots and properties as described in previous sections.  In this
section we cover the ways in which the remaining parts of a
:sip:ref:`~PyQt5.QtCore.QMetaObject` are populated.

.. note::
    :sip:ref:`~PyQt5.QtCore.Q_ENUM`, :sip:ref:`~PyQt5.QtCore.Q_FLAG` and
    :sip:ref:`~PyQt5.QtCore.Q_CLASSINFO` are not available when PyQt5 is built
    for PyPy.


:sip:ref:`~PyQt5.QtCore.Q_ENUM` and :sip:ref:`~PyQt5.QtCore.Q_FLAG`
-------------------------------------------------------------------

.. versionadded:: 5.11

The :sip:ref:`~PyQt5.QtCore.Q_ENUM` and :sip:ref:`~PyQt5.QtCore.Q_FLAG`
functions declare enumerated types and flag types respectively that are
published in the :sip:ref:`~PyQt5.QtCore.QMetaObject`.  The typical use in
PyQt5 is to declare symbolic constants that can be used by QML, and as type of
properties that can be set in Qt Designer.

Each function takes a Python type object or an ``Enum`` object that implements
the enumerated or flag type.  For example::

    from enum import Enum

    from PyQt5.QtCore import Q_ENUM, Q_FLAG, QObject


    class Instruction(QObject):

        class Direction(Enum):
            Up, Down, Left, Right = range(4)

        Q_ENUM(Direction)

        class Status:
            Null = 0x00
            Urgent = 0x01
            Acknowledged = 0x02
            Completed = 0x04

        Q_FLAG(Status)

.. versionadded:: 5.2

The (now deprecated) :sip:ref:`~PyQt5.QtCore.Q_ENUMS` and
:sip:ref:`~PyQt5.QtCore.Q_FLAGS` functions are also provided.  These differ
from the above in that they can define multiple types in one invocation.


:sip:ref:`~PyQt5.QtCore.Q_CLASSINFO`
------------------------------------

The :sip:ref:`~PyQt5.QtCore.Q_CLASSINFO` function is used in the same way as
Qt's macro of the same name, i.e. it is called from a class's definition in
order to specify a name/value pair that is placed in the class's
:sip:ref:`~PyQt5.QtCore.QMetaObject`.

For example it is used by QML to define the default property of a class::

    from PyQt5.QtCore import Q_CLASSINFO, QObject


    class BirthdayParty(QObject):

        Q_CLASSINFO('DefaultProperty', 'guests')
