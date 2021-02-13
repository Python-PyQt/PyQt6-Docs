.. sip:signal-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 51a4c54edfd36e0b77255f31e42ce699

This signal is emitted whenever the temporary status message changes. The new temporary message is passed in the *message* parameter which is a null-string when the message has been removed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar.showMessage`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.clearMessage`.
