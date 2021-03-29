.. sip:class-description::
    :status: todo
    :brief: Convenience class that simplifies dynamically overriding QStyle elements
    :digest: 7619593e2ef4e049701a5337ab873733

The :sip:ref:`~PyQt6.QtWidgets.QProxyStyle` class is a convenience class that simplifies dynamically overriding :sip:ref:`~PyQt6.QtWidgets.QStyle` elements.

A :sip:ref:`~PyQt6.QtWidgets.QProxyStyle` wraps a :sip:ref:`~PyQt6.QtWidgets.QStyle` (usually the default system style) for the purpose of dynamically overriding painting or other specific style behavior.

The following example shows how to override the shortcut underline behavior on any platform:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_qproxystyle.py
    :lines: 70-96

Warning: The :sip:ref:`~PyQt6.QtWidgets.QCommonStyle` provided by Qt will respect this hint, because they call :sip:ref:`~PyQt6.QtWidgets.QStyle.proxy`, but there is no guarantee that :sip:ref:`~PyQt6.QtWidgets.QStyle.proxy` will be called for user defined or system controlled styles. It would not work on a Mac, for example, where menus are handled by the operating system.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle`.
