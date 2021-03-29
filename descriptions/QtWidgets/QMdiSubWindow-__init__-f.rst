.. sip:method-description::
    :status: todo
    :pysig: 8df747f14ef8054a8aeecb93fe4f1471
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: 95cbc4a203b59eec66b81ce2d4fed8eb

Constructs a new :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` widget. The *parent* and *flags* arguments are passed to `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_'s constructor.

Instead of using addSubWindow(), it is also simply possible to use setParent() when you add the subwindow to a :sip:ref:`~PyQt6.QtWidgets.QMdiArea`.

Note that only :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow`\ s can be set as children of :sip:ref:`~PyQt6.QtWidgets.QMdiArea`; you cannot, for instance, write:

::

    //bad code
    QMdiArea mdiArea;
    QTextEdit editor(&mdiArea); // invalid child widget

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.addSubWindow`.
