.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: f15f3dbb583280322b664a1c8f619712

Sets the widget for which completion are provided for to *widget*. This function is automatically called when a :sip:ref:`~PyQt6.QtWidgets.QCompleter` is set on a :sip:ref:`~PyQt6.QtWidgets.QLineEdit` using :sip:ref:`~PyQt6.QtWidgets.QLineEdit.setCompleter` or on a `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_ using :sip:ref:`~PyQt6.QtWidgets.QComboBox.setCompleter`. The widget needs to be set explicitly when providing completions for custom widgets.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCompleter.widget`, :sip:ref:`~PyQt6.QtWidgets.QCompleter.setModel`, :sip:ref:`~PyQt6.QtWidgets.QCompleter.setPopup`.
