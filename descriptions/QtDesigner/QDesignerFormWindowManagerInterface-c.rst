.. sip:class-description::
    :status: todo
    :brief: Allows you to manipulate the collection of form windows in Qt Designer, and control Qt Designer's form editing actions
    :digest: 8b44e05843b8a0dac4074dff6657590f

The :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface` class allows you to manipulate the collection of form windows in Qt Designer, and control Qt Designer's form editing actions.

:sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface` is not intended to be instantiated directly. *Qt Designer* uses the form window manager to control the various form windows in its workspace. You can retrieve an interface to *Qt Designer*'s form window manager using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.formWindowManager` function. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractformwindowmanager.py
    :lines: 54-60

When implementing a custom widget plugin, a pointer to *Qt Designer*'s current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter. You must subclass the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` to expose your plugin to Qt Designer.

The form window manager interface provides the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.createFormWindow` function that enables you to create a new form window which you can add to the collection of form windows that the manager maintains, using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.addFormWindow` slot. It also provides the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindowCount` function returning the number of form windows currently under the manager's control, the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindow` function returning the form window associated with a given index, and the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.activeFormWindow` function returning the currently selected form window. The :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.removeFormWindow` slot allows you to reduce the number of form windows the manager must maintain, and the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.setActiveFormWindow` slot allows you to change the form window focus in *Qt Designer*'s workspace.

In addition, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface` contains a collection of functions that enables you to intervene and control *Qt Designer*'s form editing actions. All these functions return the original action, making it possible to propagate the function further after intervention.

Finally, the interface provides three signals which are emitted when a form window is added, when the currently selected form window changes, or when a form window is removed, respectively. All the signals carry the form window in question as their parameter.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`.
