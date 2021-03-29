.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3e9ab018826b2fedf4445e7682ef8030

This overrides :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint`. It differs from the standard repaint function in that it also calls :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents` to ensure the updates are displayed, even when there is no event loop present.
