.. sip:class-description::
    :status: todo
    :brief: Allows you to change the focus of Qt Designer's action editor
    :digest: 9250dbf16970ddc1b6c23a0c7e4c7127

The :sip:ref:`~PyQt6.QtDesigner.QDesignerActionEditorInterface` class allows you to change the focus of Qt Designer's action editor.

The :sip:ref:`~PyQt6.QtDesigner.QDesignerActionEditorInterface` class is not intended to be instantiated directly. You can retrieve an interface to *Qt Designer*'s action editor using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.actionEditor` function.

You can control which actions that are available in the action editor's window using the :sip:ref:`~PyQt6.QtDesigner.QDesignerActionEditorInterface.manageAction` and :sip:ref:`~PyQt6.QtDesigner.QDesignerActionEditorInterface.unmanageAction` functions. An action that is managed by *Qt Designer* is available in the action editor while an unmanaged action is ignored.

:sip:ref:`~PyQt6.QtDesigner.QDesignerActionEditorInterface` also provides the :sip:ref:`~PyQt6.QtDesigner.QDesignerActionEditorInterface.core` function that you can use to retrieve a pointer to *Qt Designer*'s current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object, and the :sip:ref:`~PyQt6.QtDesigner.QDesignerActionEditorInterface.setFormWindow` function that enables you to change the currently selected form window.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`.
