.. sip:method-description::
    :status: todo
    :pysig: d33117a4cf830e8da8ce315c28395b25
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: 95cbc4a203b59eec66b81ce2d4fed8eb

Constructs a new :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` widget. The *parent* and *flags* arguments are passed to :sip:ref:`~PyQt6.QtWidgets.QWidget`'s constructor.

Instead of using addSubWindow(), it is also simply possible to use setParent() when you add the subwindow to a :sip:ref:`~PyQt6.QtWidgets.QMdiArea`.

Note that only :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow`\ s can be set as children of :sip:ref:`~PyQt6.QtWidgets.QMdiArea`; you cannot, for instance, write:

::

    //bad code
    QMdiArea mdiArea;
    QTextEdit editor(&mdiArea); // invalid child widget

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.addSubWindow`.
