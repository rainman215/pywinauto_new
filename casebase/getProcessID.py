import win32process
import win32gui
import win32api
import win32con
def assert_valid_process(process_id):
    """Raise ProcessNotFound error if process_id is not a valid process id"""
    try:
        process_handle = win32api.OpenProcess(win32con.MAXIMUM_ALLOWED, 0, process_id)
    except win32gui.error as exc:
        raise ProcessNotFoundError(str(exc) + ', pid = ' + str(process_id))

    if not process_handle:
        message = "Process with ID '%d' could not be opened" % process_id
        raise ProcessNotFoundError(message)

    return process_handle
def process_module(process_id):
    """Return the string module name of this process"""
    process_handle = assert_valid_process(process_id)

    return win32process.GetModuleFileNameEx(process_handle, 0)
class ProcessNotFoundError(Exception):

    """Could not find that process"""

    pass    # pragma: no cover
def process_get_modules():
    """Return the list of processes as tuples (pid, exe_path)"""
    modules = []

    # collect all the running processes
    pids = win32process.EnumProcesses()
    for pid in pids:
        if pid != 0 and isinstance(pid, int):  # skip system process (0x00000000)
            try:
                modules.append((pid, process_module(pid), None))
            except (win32gui.error, ProcessNotFoundError):
                continue
    return modules

# _list=process_get_modules()
# for i in range(len(_list)):
#     if "MainApp" in _list[i][1]:
#         print _list[i][0]