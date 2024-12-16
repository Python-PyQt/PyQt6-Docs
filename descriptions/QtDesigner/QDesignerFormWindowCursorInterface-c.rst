.. sip:class-description::
    :status: todo
    :brief: Allows you to query and modify a form window's widget selection, and in addition modify the properties of all the form's widgets
    :digest: 4ec82ecb2922f06a53ea0058a7c83426

The :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface` class allows you to query and modify a form window's widget selection, and in addition modify the properties of all the form's widgets.

:sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface` is a convenience class that provides an interface to the associated form window's text cursor; it provides a collection of functions that enables you to query a given form window's selection and change the selection's focus according to defined modes (\ :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveMode.MoveMode`) and movements (\ :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.MoveOperation.MoveOperation`). You can also use the interface to query the form's widgets and change their properties.

The interface is not intended to be instantiated directly, but to provide access to the selections and widgets of Qt Widgets Designer's current form windows. :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface` always provides an associated cursor interface. The form window for a given widget can be retrieved using the static :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.findFormWindow` functions. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractformwindowcursor.py
    :lines: 54-57

You can retrieve any of Qt Widgets Designer's current form windows through Qt Widgets Designer's :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface`.

Once you have a form window's cursor interface, you can check if the form window has a selection at all using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.hasSelection` function. You can query the form window for its total :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.widgetCount` and :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.selectedWidgetCount`. You can retrieve the currently selected widget (or widgets) using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.current` or :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.selectedWidget` functions.

You can retrieve any of the form window's widgets using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.widget` function, and check if a widget is selected using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.isWidgetSelected` function. You can use the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setProperty` function to set the selected widget's properties, and the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setWidgetProperty` or :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.resetWidgetProperty` functions to modify the properties of any given widget.

Finally, you can change the selection by changing the text cursor's :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.position` using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setPosition` and :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.movePosition` functions.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface`.
