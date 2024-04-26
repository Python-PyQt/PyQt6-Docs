.. sip:enum-member-description::
    :status: todo
    :value: 0x00000004
    :realname: QFileDialog::Option::DontConfirmOverwrite
    :digest: e2e2be3e13822d48b3e2bf8a66a8ae6f

Don't ask for confirmation if an existing file is selected. By default, confirmation is requested. This option is only effective if :sip:ref:`~PyQt6.QtWidgets.QFileDialog.acceptMode` is :sip:ref:`~PyQt6.QtWidgets.QFileDialog.AcceptMode.AcceptSave`). It is furthermore not used on macOS for native file dialogs.
