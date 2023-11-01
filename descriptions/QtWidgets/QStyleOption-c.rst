.. sip:class-description::
    :status: todo
    :brief: Stores the parameters used by QStyle functions
    :digest: 74303f35d78836fd7b990f7615895b8f

The :sip:ref:`~PyQt6.QtWidgets.QStyleOption` class stores the parameters used by :sip:ref:`~PyQt6.QtWidgets.QStyle` functions.

:sip:ref:`~PyQt6.QtWidgets.QStyleOption` and its subclasses contain all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw a graphical element.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

The caller of a :sip:ref:`~PyQt6.QtWidgets.QStyle` function usually creates :sip:ref:`~PyQt6.QtWidgets.QStyleOption` objects on the stack. This combined with Qt's extensive use of `implicit sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_ for types such as QString, :sip:ref:`~PyQt6.QtGui.QPalette`, and :sip:ref:`~PyQt6.QtGui.QColor` ensures that no memory allocation needlessly takes place.

The following code snippet shows how to use a specific :sip:ref:`~PyQt6.QtWidgets.QStyleOption` subclass to paint a push button:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstyleoption-main.py
    :lines: 70-82

In our example, the control is a :sip:ref:`~PyQt6.QtWidgets.QStyle.ControlElement.CE_PushButton`, and according to the :sip:ref:`~PyQt6.QtWidgets.QStyle.drawControl` documentation the corresponding class is :sip:ref:`~PyQt6.QtWidgets.QStyleOptionButton`.

When reimplementing :sip:ref:`~PyQt6.QtWidgets.QStyle` functions that take a :sip:ref:`~PyQt6.QtWidgets.QStyleOption` parameter, you often need to cast the :sip:ref:`~PyQt6.QtWidgets.QStyleOption` to a subclass. For safety, you can use qstyleoption_cast() to ensure that the pointer type is correct. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstyleoption-main.py
    :lines: 96-109

The qstyleoption_cast() function will return 0 if the object to which ``option`` points is not of the correct type.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle`, :sip:ref:`~PyQt6.QtWidgets.QStylePainter`.
