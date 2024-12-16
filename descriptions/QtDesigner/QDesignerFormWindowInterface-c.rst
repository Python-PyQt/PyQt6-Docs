.. sip:class-description::
    :status: todo
    :brief: Allows you to query and manipulate form windows appearing in Qt Widgets Designer's workspace
    :digest: b5d2d8b268c9e55fcfd021bb4db43714

The :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface` class allows you to query and manipulate form windows appearing in Qt Widgets Designer's workspace.

:sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface` provides information about the associated form window as well as allowing its properties to be altered. The interface is not intended to be instantiated directly, but to provide access to Qt Widgets Designer's current form windows controlled by Qt Widgets Designer's :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface`.

If you are looking for the form window containing a specific widget, you can use the static :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.findFormWindow` function:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractformwindow.py
    :lines: 54-55

But in addition, you can access any of the current form windows through Qt Widgets Designer's form window manager: Use the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.formWindowManager` function to retrieve an interface to the manager. Once you have this interface, you have access to all of Qt Widgets Designer's current form windows through the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface.formWindow` function. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractformwindow.py
    :lines: 60-68

The pointer to Qt Widgets Designer's current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter. When implementing a custom widget plugin, you must subclass the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` class to expose your plugin to Qt Widgets Designer.

Once you have the form window, you can query its properties. For example, a plain custom widget plugin is managed by Qt Widgets Designer only at its top level, i.e. none of its child widgets can be resized in Qt Widgets Designer's workspace. But :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface` provides you with functions that enables you to control whether a widget should be managed by Qt Widgets Designer, or not:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractformwindow.py
    :lines: 73-74

The complete list of functions concerning widget management is: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.isManaged`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.manageWidget` and :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.unmanageWidget`. There is also several associated signals: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.widgetManaged`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.widgetRemoved`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.aboutToUnmanageWidget` and :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.widgetUnmanaged`.

In addition to controlling the management of widgets, you can control the current selection in the form window using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.selectWidget`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.clearSelection` and :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.emitSelectionChanged` functions, and the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.selectionChanged` signal.

You can also retrieve information about where the form is stored using :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.absoluteDir`, its include files using :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.includeHints`, and its layout and pixmap functions using :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.layoutDefault`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.layoutFunction` and :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.pixmapFunction`. You can find out whether the form window has been modified (but not saved) or not, using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.isDirty` function. You can retrieve its :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.author`, its :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.contents`, its :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.fileName`, associated :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.comment` and :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.exportMacro`, its mainContainer(), its :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.features`, its :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.grid` and its :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.resourceFiles`.

The interface provides you with functions and slots allowing you to alter most of this information as well. The exception is the directory storing the form window. Finally, there is several signals associated with changes to the information mentioned above and to the form window in general.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowManagerInterface`.
