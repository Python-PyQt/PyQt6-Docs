.. sip:enum-member-description::
    :status: todo
    :value: 7
    :digest: 3a5afa8fc769a34fc148ff08dc3d8935

Keyboard shortcuts on macOS are typically based on the Command (or Cmd) keyboard modifier, represented by the ⌘ symbol. For example, the 'Copy' action is Command+C (⌘+C). To ease cross platform development Qt will by default remap Command to the :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers.ControlModifier`, to align with other platforms. This allows creating keyboard shortcuts such as "Ctrl+J", which on macOS will then map to Command+J, as expected by macOS users. The actual Control (or Ctrl) modifier on macOS, represented by ⌃, is mapped to :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers.MetaModifier`.
