.. sip:class-description::
    :status: todo
    :brief: The base class of geometry managers
    :digest: f495b89196fcdae1fd078a2d73260669

The :sip:ref:`~PyQt6.QtWidgets.QLayout` class is the base class of geometry managers.

This is an abstract base class inherited by the concrete classes :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout`, :sip:ref:`~PyQt6.QtWidgets.QFormLayout`, and :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`.

For users of :sip:ref:`~PyQt6.QtWidgets.QLayout` subclasses or of :sip:ref:`~PyQt6.QtWidgets.QMainWindow` there is seldom any need to use the basic functions provided by :sip:ref:`~PyQt6.QtWidgets.QLayout`, such as :sip:ref:`~PyQt6.QtWidgets.QLayout.setSizeConstraint` or :sip:ref:`~PyQt6.QtWidgets.QLayout.setMenuBar`. See `Layout Management <https://doc.qt.io/qt-6/layout.html>`_ for more information.

To make your own layout manager, implement the functions :sip:ref:`~PyQt6.QtWidgets.QLayout.addItem`, sizeHint(), :sip:ref:`~PyQt6.QtWidgets.QLayout.setGeometry`, :sip:ref:`~PyQt6.QtWidgets.QLayout.itemAt` and :sip:ref:`~PyQt6.QtWidgets.QLayout.takeAt`. You should also implement :sip:ref:`~PyQt6.QtWidgets.QLayout.minimumSize` to ensure your layout isn't resized to zero size if there is too little space. To support children whose heights depend on their widths, implement hasHeightForWidth() and heightForWidth(). See the `Flow Layout <https://doc.qt.io/qt-6/qtwidgets-layouts-flowlayout-example.html>`_ example for more information about implementing custom layout managers.

Geometry management stops when the layout manager is deleted.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`, `Layout Management <https://doc.qt.io/qt-6/layout.html>`_, `Basic Layouts Example <https://doc.qt.io/qt-6/qtwidgets-layouts-basiclayouts-example.html>`_, `Flow Layout Example <https://doc.qt.io/qt-6/qtwidgets-layouts-flowlayout-example.html>`_.
