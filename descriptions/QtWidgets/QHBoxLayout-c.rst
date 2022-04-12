.. sip:class-description::
    :status: todo
    :brief: Lines up widgets horizontally
    :digest: 9399a1ca0dc9355f3968e86d8a713d71

The :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout` class lines up widgets horizontally.

This class is used to construct horizontal box layout objects. See :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` for details.

The simplest use of the class is like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 61-61

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 63-63

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 65-68

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 72-72

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 74-79

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 83-83

First, we create the widgets we want to add to the layout. Then, we create the :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout` object, setting ``window`` as parent by passing it in the constructor; next we add the widgets to the layout. ``window`` will be the parent of the widgets that are added to the layout.

If you don't pass a parent ``window`` to the constructor, you can at a later point use :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayout` to install the :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout` object onto ``window``. At that point, the widgets in the layout are reparented to have ``window`` as their parent.

.. image:: ../../../images/qhboxlayout-with-5-children.png

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`, `Layout Management <https://doc.qt.io/qt-6/layout.html>`_, `Basic Layouts Example <https://doc.qt.io/qt-6/qtwidgets-layouts-basiclayouts-example.html>`_.
