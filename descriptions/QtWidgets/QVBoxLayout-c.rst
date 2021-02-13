.. sip:class-description::
    :status: todo
    :brief: Lines up widgets vertically
    :digest: 51ede2cd5f01cd3ae32c0d55c98430bc

The :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout` class lines up widgets vertically.

This class is used to construct vertical box layout objects. See :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` for details.

The simplest use of the class is like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 89-89

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 91-91

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 93-96

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 100-100

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 102-107

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 111-111

First, we create the widgets we want to add to the layout. Then, we create the :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout` object, setting ``window`` as parent by passing it in the constructor; next we add the widgets to the layout. ``window`` will be the parent of the widgets that are added to the layout.

If you don't pass parent ``window`` in the constrcutor, you can at a later point use :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayout` to install the :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout` object onto ``window``. At that point, the widgets in the layout are reparented to have ``window`` as their parent.

.. image:: ../../../images/qvboxlayout-with-5-children.png

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`, `Layout Management <https://doc.qt.io/qt-6/layout.html>`_, `Basic Layouts Example <https://doc.qt.io/qt-6/qtwidgets-layouts-basiclayouts-example.html>`_.
