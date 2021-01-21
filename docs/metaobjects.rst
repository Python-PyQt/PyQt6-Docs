Other Support for Dynamic Meta-objects
======================================

PyQt6 creates a :sip:ref:`~PyQt6.QtCore.QMetaObject` instance for any Python
sub-class of :sip:ref:`~PyQt6.QtCore.QObject` without the need for the
equivalent of Qt's ``Q_OBJECT`` macro.  Most of a
:sip:ref:`~PyQt6.QtCore.QMetaObject` is populated automatically by defining
signals, slots and properties as described in previous sections.  In this
section we cover the ways in which the remaining parts of a
:sip:ref:`~PyQt6.QtCore.QMetaObject` are populated.


:sip:ref:`~PyQt6.QtCore.pyqtEnum`
---------------------------------

The :sip:ref:`~PyQt6.QtCore.pyqtEnum` class decorator is used to decorate
sub-classes of the Python :py:class:`~enum.Enum` class so that they are
published in the :sip:ref:`~PyQt6.QtCore.QMetaObject`.  The typical use in
PyQt6 is to declare symbolic constants that can be used by QML, and as the type
of properties that can be set in Qt Designer.  For example::

    from enum import Enum, Flag

    from PyQt6.QtCore import pyqtEnum, QObject


    class Instruction(QObject):

        @pyqtEnum
        class Direction(Enum):
            Up, Down, Left, Right = range(4)

        @pyqtEnum
        class Status(Flag):
            Null = 0x00
            Urgent = 0x01
            Acknowledged = 0x02
            Completed = 0x04


:sip:ref:`~PyQt6.QtCore.pyqtClassInfo`
--------------------------------------

The :sip:ref:`~PyQt6.QtCore.pyqtClassInfo` class decorator is used to specify a
a name/value pair that is placed in the class's
:sip:ref:`~PyQt6.QtCore.QMetaObject`.  It is the equivalent of Qt's
:c:macro:`Q_CLASSINFO` macro.

For example it is used by QML to define the default property of a class::

    from PyQt6.QtCore import pyqtClassInfo, QObject


    @pyqtClassInfo('DefaultProperty', 'guests')
    class BirthdayParty(QObject):

        pass

The decorator may be chained to define multiple name/value pairs.
