.. sip:class-description::
    :status: todo
    :brief: Widget that allows for creating, editing and removing filters
    :digest: c55f12b500497d46fa62bf1c36e7fc82

The :sip:ref:`~PyQt6.QtHelp.QHelpFilterSettingsWidget` class provides a widget that allows for creating, editing and removing filters.

The instance of :sip:ref:`~PyQt6.QtHelp.QHelpFilterSettingsWidget` may be a part of a preferences dialog. Before showing the dialog, :sip:ref:`~PyQt6.QtHelp.QHelpFilterSettingsWidget.setAvailableComponents` and :sip:ref:`~PyQt6.QtHelp.QHelpFilterSettingsWidget.setAvailableVersions` should be called, otherwise the filter settings widget will only offer a creation of empty filters, which wouldn't be useful. In addition, :sip:ref:`~PyQt6.QtHelp.QHelpFilterSettingsWidget.readSettings` should also be called to fill up the filter settings widget with the list of filters already stored in the filter engine. The creation of new filters, modifications to existing filters and removal of unneeded filters are handled by the widget automatically. If you want to store the current state of the widget and apply it to the filter engine e.g. after the user clicked the apply button - call :sip:ref:`~PyQt6.QtHelp.QHelpFilterSettingsWidget.applySettings`.
