.. sip:class-description::
    :status: todo
    :brief: Used to dynamically construct user interfaces from UI files at run-time
    :digest: 479536db63731283115c47fc0aa6d222

The :sip:ref:`~PyQt6.QtDesigner.QFormBuilder` class is used to dynamically construct user interfaces from UI files at run-time.

The :sip:ref:`~PyQt6.QtDesigner.QFormBuilder` class provides a mechanism for dynamically creating user interfaces at run-time, based on UI files created with *Qt Designer*. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_uilib_formbuilder.py
    :lines: 54-66

By including the user interface in the example's resources (``myForm.qrc``), we ensure that it will be present when the example is run:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_uilib_formbuilder.py
    :lines: 71-75

:sip:ref:`~PyQt6.QtDesigner.QFormBuilder` extends the :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder` base class with a number of functions that are used to support custom widget plugins:

* :sip:ref:`~PyQt6.QtDesigner.QFormBuilder.pluginPaths` returns the list of paths that the form builder searches when loading custom widget plugins.

* :sip:ref:`~PyQt6.QtDesigner.QFormBuilder.addPluginPath` allows additional paths to be registered with the form builder.

* :sip:ref:`~PyQt6.QtDesigner.QFormBuilder.setPluginPath` is used to replace the existing list of paths with a list obtained from some other source.

* :sip:ref:`~PyQt6.QtDesigner.QFormBuilder.clearPluginPaths` removes all paths registered with the form builder.

* :sip:ref:`~PyQt6.QtDesigner.QFormBuilder.customWidgets` returns a list of interfaces to plugins that can be used to create new instances of registered custom widgets.

The :sip:ref:`~PyQt6.QtDesigner.QFormBuilder` class is typically used by custom components and applications that embed *Qt Designer*. Standalone applications that need to dynamically generate user interfaces at run-time use the QUiLoader class, found in the QtUiTools module.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder`.
