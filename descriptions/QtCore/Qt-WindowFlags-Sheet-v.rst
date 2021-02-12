.. sip:enum-member-description::
    :status: todo
    :value: 0x00000004 | Window
    :realname: Qt::WindowType::Sheet
    :digest: f6cda8575945b8ecb6d0b808a518609e

Indicates that the window is a sheet on macOS. Since using a sheet implies window modality, the recommended way is to use QWidget::setWindowModality(), or QDialog::open(), instead.
