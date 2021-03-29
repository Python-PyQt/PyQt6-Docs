.. sip:method-description::
    :status: todo
    :pysig: 2a38832352a50ffc5e738fd2b818b613
    :realsig: (QWidget*,int)
    :digest: bd98578e016fc0a82eb9b382b86b98ca

Adds a mapping between a *widget* and a *section* from the model. The *section* is a column in the model if the orientation is horizontal (the default), otherwise a row.

For the following example, we assume a model ``myModel`` that has two columns: the first one contains the names of people in a group, and the second column contains their ages. The first column is mapped to the :sip:ref:`~PyQt6.QtWidgets.QLineEdit` ``nameLineEdit``, and the second is mapped to the :sip:ref:`~PyQt6.QtWidgets.QSpinBox` ``ageSpinBox``:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qdatawidgetmapper.py
    :lines: 64-67

**Notes:**

* If the *widget* is already mapped to a section, the old mapping will be replaced by the new one.

* Only one-to-one mappings between sections and widgets are allowed. It is not possible to map a single section to multiple widgets, or to map a single widget to multiple sections.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.removeMapping`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.mappedSection`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.clearMapping`.
