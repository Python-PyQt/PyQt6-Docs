.. sip:method-description::
    :status: todo
    :pysig: 364191bc772363d61cf96ad3eac70cf9
    :realsig: (const QSize&)
    :digest: 2b320fe94944741f2189428cfd8d6570

Sets both the minimum and maximum sizes of the widget to *s*, thereby preventing it from ever growing or shrinking.

This will override the default size constraints set by :sip:ref:`~PyQt6.QtWidgets.QLayout`.

To remove constraints, set the size to :sip:ref:`~PyQt6.QtWidgets.QWIDGETSIZE_MAX`.

Alternatively, if you want the widget to have a fixed size based on its contents, you can call :sip:ref:`~PyQt6.QtWidgets.QLayout.setSizeConstraint`\ (\ :sip:ref:`~PyQt6.QtWidgets.QLayout.SizeConstraint.SetFixedSize`);

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.maximumSize`, :sip:ref:`~PyQt6.QtWidgets.QWidget.minimumSize`.
