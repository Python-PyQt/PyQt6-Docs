.. sip:class-description::
    :status: todo
    :brief: Group box frame with a title
    :digest: 54292d78cb8ddbc9d0085254c85c032d

The :sip:ref:`~PyQt6.QtWidgets.QGroupBox` widget provides a group box frame with a title.

.. image:: ../../../images/fusion-groupbox.png

A group box provides a frame, a title on top, a keyboard shortcut, and displays various other widgets inside itself. The keyboard shortcut moves keyboard focus to one of the group box's child widgets.

:sip:ref:`~PyQt6.QtWidgets.QGroupBox` also lets you set the :sip:ref:`~PyQt6.QtWidgets.QGroupBox.title` (normally set in the constructor) and the title's `alignment <https://doc.qt.io/qt-6/stylesheet-reference.html#alignment>`_. Group boxes can be checkable. Child widgets in checkable group boxes are enabled or disabled depending on whether or not the group box is checked.

You can minimize the space consumption of a group box by enabling the flat property. In most :sip:ref:`~PyQt6.QtWidgets.QStyle`, enabling this property results in the removal of the left, right and bottom edges of the frame.

:sip:ref:`~PyQt6.QtWidgets.QGroupBox` doesn't automatically lay out the child widgets (which are often :sip:ref:`~PyQt6.QtWidgets.QCheckBox`\ es or :sip:ref:`~PyQt6.QtWidgets.QRadioButton`\ s but can be any widgets). The following example shows how we can set up a :sip:ref:`~PyQt6.QtWidgets.QGroupBox` with a layout:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qgroupbox.py
    :lines: 11-24

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QButtonGroup`.
