.. sip:class-description::
    :status: todo
    :brief: Allows you to control the contents of Qt Widgets Designer's widget box
    :digest: ca6bdf48b9a64a08a66f0c215805970c

The :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface` class allows you to control the contents of Qt Widgets Designer's widget box.

:sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface` contains a collection of functions that is typically used to manipulate the contents of Qt Widgets Designer's widget box.

Qt Widgets Designer uses an XML file to populate its widget box. The name of that file is one of the widget box's properties, and you can retrieve it using the :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface.fileName` function.

:sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface` also provides the :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface.save` function that saves the contents of the widget box in the file specified by the widget box's file name property. If you have made changes to the widget box, for example by dropping a widget into the widget box, without calling the :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface.save` function, the original content can be restored by a simple invocation of the :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface.load` function:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractwidgetbox.py
    :lines: 54-57

The :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface` class is not intended to be instantiated directly. You can retrieve an interface to Qt Designer's widget box using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.widgetBox` function. A pointer to Qt Widgets Designer's current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter. When implementing a custom widget plugin, you must subclass the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` to expose your plugin to Qt Widgets Designer.

If you want to save your changes, and at the same time preserve the original contents, you can use the :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface.save` function combined with the :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface.setFileName` function to save your changes into another file. Remember to store the name of the original file first:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractwidgetbox.py
    :lines: 62-65

Then you can restore the original contents of the widget box by resetting the file name to the original file and calling :sip:ref:`~PyQt6.QtDesigner.QDesignerWidgetBoxInterface.load`:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractwidgetbox.py
    :lines: 70-71

In a similar way, you can later use your customized XML file:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractwidgetbox.py
    :lines: 76-79

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`.
