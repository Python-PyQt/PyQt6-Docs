.. sip:class-description::
    :status: todo
    :brief: Interface for reading from and writing to open files
    :digest: 6ad57113c4c79040ebdd1b6b6fdfc1f3

The :sip:ref:`~PyQt6.QtCore.QFileDevice` class provides an interface for reading from and writing to open files.

:sip:ref:`~PyQt6.QtCore.QFileDevice` is the base class for I/O devices that can read and write text and binary files and `resources <https://doc.qt.io/qt-6/resources.html>`_. :sip:ref:`~PyQt6.QtCore.QFile` offers the main functionality, :sip:ref:`~PyQt6.QtCore.QFileDevice` serves as a base class for sharing functionality with other file devices such as :sip:ref:`~PyQt6.QtCore.QSaveFile`, by providing all the operations that can be done on files that have been opened by :sip:ref:`~PyQt6.QtCore.QFile` or :sip:ref:`~PyQt6.QtCore.QSaveFile`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtCore.QSaveFile`.
