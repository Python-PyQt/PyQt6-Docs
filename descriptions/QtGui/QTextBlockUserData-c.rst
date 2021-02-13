.. sip:class-description::
    :status: todo
    :brief: Used to associate custom data with blocks of text
    :digest: e201dbdc4f00d09e7aaa518b8100a6eb

The :sip:ref:`~PyQt6.QtGui.QTextBlockUserData` class is used to associate custom data with blocks of text.

:sip:ref:`~PyQt6.QtGui.QTextBlockUserData` provides an abstract interface for container classes that are used to associate application-specific user data with text blocks in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

Generally, subclasses of this class provide functions to allow data to be stored and retrieved, and instances are attached to blocks of text using :sip:ref:`~PyQt6.QtGui.QTextBlock.setUserData`. This makes it possible to store additional data per text block in a way that can be retrieved safely by the application.

Each subclass should provide a reimplementation of the destructor to ensure that any private data is automatically cleaned up when user data objects are deleted.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlock`.
