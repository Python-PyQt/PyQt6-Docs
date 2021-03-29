.. sip:method-description::
    :status: todo
    :pysig: a81259cef8e959c624df1d456e5d3297
    :realsig: ()
    :digest: ef3a1129cf85bc6c19a076e308112984

This function switches the user interface into "What's This?" mode. The user interface can be switched back into normal mode by the user (e.g. by them clicking or pressing Esc), or programmatically by calling :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.leaveWhatsThisMode`.

When entering "What's This?" mode, a :sip:ref:`~PyQt6.QtCore.QEvent` of type Qt::EnterWhatsThisMode is sent to all toplevel widgets.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.inWhatsThisMode`, :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.leaveWhatsThisMode`.
