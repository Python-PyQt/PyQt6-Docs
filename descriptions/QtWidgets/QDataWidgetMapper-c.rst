.. sip:class-description::
    :status: todo
    :brief: Mapping between a section of a data model to widgets
    :digest: 23c69d57a97525623f83dafb43511e38

The :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper` class provides mapping between a section of a data model to widgets.

:sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper` can be used to create data-aware widgets by mapping them to sections of an item model. A section is a column of a model if the orientation is horizontal (the default), otherwise a row.

Every time the current index changes, each widget is updated with data from the model via the property specified when its mapping was made. If the user edits the contents of a widget, the changes are read using the same property and written back to the model. By default, each widget's user property is used to transfer data between the model and the widget. Since Qt 4.3, an additional :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.addMapping` function enables a named property to be used instead of the default user property.

It is possible to set an item delegate to support custom widgets. By default, a :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` is used to synchronize the model with the widgets.

Let us assume that we have an item model named ``model`` with the following contents:

+---+--------------+-----------+
| 1 | Qt Norway    | Oslo      |
+---+--------------+-----------+
| 2 | Qt Australia | Brisbane  |
+---+--------------+-----------+
| 3 | Qt USA       | Palo Alto |
+---+--------------+-----------+
| 4 | Qt China     | Beijing   |
+---+--------------+-----------+
| 5 | Qt Germany   | Berlin    |
+---+--------------+-----------+

The following code will map the columns of the model to widgets called ``mySpinBox``, ``myLineEdit`` and ``myCountryChooser``:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qdatawidgetmapper.py
    :lines: 54-59

After the call to :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.toFirst`, ``mySpinBox`` displays the value ``1``, ``myLineEdit`` displays ``Qt Norway`` and ``myCountryChooser`` displays ``Oslo``. The navigational functions :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.toFirst`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.toNext`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.toPrevious`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.toLast` and :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setCurrentIndex` can be used to navigate in the model and update the widgets with contents from the model.

The :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setRootIndex` function enables a particular item in a model to be specified as the root index - children of this item will be mapped to the relevant widgets in the user interface.

:sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper` supports two submit policies, ``AutoSubmit`` and ``ManualSubmit``. ``AutoSubmit`` will update the model as soon as the current widget loses focus, ``ManualSubmit`` will not update the model unless :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.submit` is called. ``ManualSubmit`` is useful when displaying a dialog that lets the user cancel all modifications. Also, other views that display the model won't update until the user finishes all their modifications and submits.

Note that :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper` keeps track of external modifications. If the contents of the model are updated in another module of the application, the widgets are updated as well.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`.
