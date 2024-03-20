from pywinauto.application import Application
from time import sleep
import subprocess
import csv
import io


def open_perfmon():
    exec_path = r"C:\\Windows\\System32\WindowsPowerShell\\v1.0\\powershell.exe"
    subprocess.call([exec_path, "perfmon.exe"], shell=True)
    return


def validate_process():
    commands = "tasklist /v /fo csv"
    process = subprocess.Popen(['powershell', commands], stdout=subprocess.PIPE)
    outputs = str(process.communicate()[0].decode("utf-8"))
    return outputs


def find_pid():
    outputs = validate_process()
    rows = csv.DictReader(io.StringIO(outputs))
    sleep(2)
    for row in rows:
        # print(row)
        if row["Window Title"] == "Performance Monitor":
            pid = row["PID"]
            return pid


def connect_perfmon():
    pid = find_pid()
    app = Application(backend="uia").connect(process=int(pid))
    return app


def perform_selection():
    app = connect_perfmon()
    title = 'Performance Monitor'
    data_collector_sets = app.window(best_match=title, top_level_only=True).child_window(
        best_match="Data Collector Sets")
    user_define = app.window(best_match=title, top_level_only=True).child_window(best_match="User Defined")
    open_create_new_collector = app.window(best_match=title, top_level_only=True).child_window(
        best_match="Create a new Data Collector Set")
    sleep(1)
    data_collector_sets.click_input()
    sleep(1)
    user_define.click_input()
    sleep(1)
    open_create_new_collector.click_input()
    sleep(1)


def child_monitor():
    dialog = r'Create new Data Collector Set.'
    app = connect_perfmon()
    child = app.window(best_match=r'Performance Monitor', top_level_only=True).child_window(best_match=dialog)
    return child


def set_new_collector():
    child_app = child_monitor()
    data_collector_name = child_app.child_window(title="Name:", auto_id="2801", control_type="Edit")
    create_manually = child_app.child_window(title="Create manually (Advanced)", auto_id="2803", control_type="RadioButton")
    performance_counter = child_app.child_window(title="Performance counter", auto_id="3202", control_type="CheckBox")
    click_next = child_app.child_window(best_match="Next")
    sample_interval = child_app.child_window(title="Sample interval:", auto_id="3604", control_type="Edit")
    add = child_app.child_window(title="Add...", auto_id="3602", control_type="Button")
    data_collector_name.set_text("")
    sleep(1)
    data_collector_name.type_keys("CloudXR-Logs-Gen")
    create_manually.click_input()
    click_next.click_input()
    if performance_counter.get_toggle_state() == 0:
        performance_counter.click_input()
    click_next.click_input()
    sample_interval.set_text("")
    sleep(1)
    sample_interval.type_keys("1")
    add.click_input()