.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: bf878a6a23bad29d9db3600791714a2f

Copies the selected text to the clipboard and deletes it, if there is any, and if :sip:ref:`~PyQt6.QtWidgets.QLineEdit.echoMode` is :sip:ref:`~PyQt6.QtWidgets.QLineEdit.EchoMode.Normal`.

If the current validator disallows deleting the selected text, cut() will copy without deleting.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLineEdit.copy`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit.paste`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setValidator`.
