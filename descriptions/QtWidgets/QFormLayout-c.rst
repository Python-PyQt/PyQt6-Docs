.. sip:class-description::
    :status: todo
    :brief: Manages forms of input widgets and their associated labels
    :digest: 63906fe9b764ce744c07847e521e7378

The :sip:ref:`~PyQt6.QtWidgets.QFormLayout` class manages forms of input widgets and their associated labels.

:sip:ref:`~PyQt6.QtWidgets.QFormLayout` is a convenience layout class that lays out its children in a two-column form. The left column consists of labels and the right column consists of "field" widgets (line editors, spin boxes, etc.).

Traditionally, such two-column form layouts were achieved using :sip:ref:`~PyQt6.QtWidgets.QGridLayout`. :sip:ref:`~PyQt6.QtWidgets.QFormLayout` is a higher-level alternative that provides the following advantages:

* **Adherence to the different platform's look and feel guidelines.**

  For example, the `macOS Aqua <http://developer.apple.com/library/mac/#documentation/UserExperience/Conceptual/AppleHIGuidelines/Intro/Intro.html>`_ and KDE guidelines specify that the labels should be right-aligned, whereas Windows and GNOME applications normally use left-alignment.

* **Support for wrapping long rows.**

  For devices with small displays, :sip:ref:`~PyQt6.QtWidgets.QFormLayout` can be set to :sip:ref:`~PyQt6.QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows`, or even to :sip:ref:`~PyQt6.QtWidgets.QFormLayout.RowWrapPolicy.WrapAllRows`.

* **Convenient API for creating label--field pairs.**

  The :sip:ref:`~PyQt6.QtWidgets.QFormLayout.addRow` overload that takes a QString and a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ \* creates a :sip:ref:`~PyQt6.QtWidgets.QLabel` behind the scenes and automatically set up its buddy. We can then write code like this:

  .. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
      :lines: 54-58

  Compare this with the following code, written using :sip:ref:`~PyQt6.QtWidgets.QGridLayout`:

  .. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
      :lines: 63-79

The table below shows the default appearance in different styles.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QCommonStyle` derived styles (except QPlastiqueStyle)                                                                                                                                                                                     | QMacStyle                                                                                                                                                                                                                                                                        | QPlastiqueStyle                                                                                                                                    | Qt Extended styles                                                                                                                                             |
+======================================================================================================================================================================================================================================================================+==================================================================================================================================================================================================================================================================================+====================================================================================================================================================+================================================================================================================================================================+
| |image-qformlayout-win-png|                                                                                                                                                                                                                                          | |image-qformlayout-mac-png|                                                                                                                                                                                                                                                      | |image-qformlayout-kde-png|                                                                                                                        | |image-qformlayout-qpe-png|                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Traditional style used for Windows, GNOME, and earlier versions of KDE. Labels are left aligned, and expanding fields grow to fill the available space. (This normally corresponds to what we would get using a two-column :sip:ref:`~PyQt6.QtWidgets.QGridLayout`.) | Style based on the `macOS Aqua <http://developer.apple.com/library/mac/#documentation/UserExperience/Conceptual/AppleHIGuidelines/Intro/Intro.html>`_ guidelines. Labels are right-aligned, the fields don't grow beyond their size hint, and the form is horizontally centered. | Recommended style for KDE applications. Similar to MacStyle, except that the form is left-aligned and all fields grow to fill the available space. | Default style for Qt Extended styles. Labels are right-aligned, expanding fields grow to fill the available space, and row wrapping is enabled for long lines. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

The form styles can be also be overridden individually by calling :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setLabelAlignment`, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setFormAlignment`, :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setFieldGrowthPolicy`, and :sip:ref:`~PyQt6.QtWidgets.QFormLayout.setRowWrapPolicy`. For example, to simulate the form layout appearance of QMacStyle on all platforms, but with left-aligned labels, you could write:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qformlayout.py
    :lines: 84-87

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGridLayout`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`.

.. |image-qformlayout-win-png| image:: ../../../images/qformlayout-win.png
.. |image-qformlayout-mac-png| image:: ../../../images/qformlayout-mac.png
.. |image-qformlayout-kde-png| image:: ../../../images/qformlayout-kde.png
.. |image-qformlayout-qpe-png| image:: ../../../images/qformlayout-qpe.png
