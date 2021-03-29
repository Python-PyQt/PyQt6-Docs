.. sip:enum-member-description::
    :status: todo
    :value: 0x00000000
    :realname: Qt::ApplicationState::ApplicationSuspended
    :digest: e34a285e2bd2f5ff39f2368f4f7863e6

The application is about to suspend. When entering this state, the application should save its state, cease all activities, and be prepared for code execution to stop. While suspended, the application can be killed at any time without further warnings (e.g. when low memory forces the OS to purge suspended applications).
