.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 32e5952164cf5eaa6aa85d33176f1728

Removes the specified *widget* from the status bar.

**Note:** This function does not delete the widget but *hides* it. To add the widget again, you must call both the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addWidget` and show() functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addPermanentWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.clearMessage`.
