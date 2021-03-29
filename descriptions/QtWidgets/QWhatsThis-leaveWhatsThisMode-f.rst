.. sip:method-description::
    :status: todo
    :pysig: a81259cef8e959c624df1d456e5d3297
    :realsig: ()
    :digest: 1404c6fcf7dd4ea25c0091e7298ada5b

If the user interface is in "What's This?" mode, this function switches back to normal mode; otherwise it does nothing.

When leaving "What's This?" mode, a :sip:ref:`~PyQt6.QtCore.QEvent` of type Qt::LeaveWhatsThisMode is sent to all toplevel widgets.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.enterWhatsThisMode`, :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.inWhatsThisMode`.
