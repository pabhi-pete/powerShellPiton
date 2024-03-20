import os
import subprocess
import xml.etree.ElementTree as ET


def run():
    exec_file = os.path.abspath("script.ps1")
    exec_path = r"C:\\Windows\\System32\WindowsPowerShell\\v1.0\\powershell.exe"
    command = [exec_path, exec_file]
    subprocess.call(command, shell=True)
    return


def utility():
    counter_list = ""
    if not os.path.isfile("collectorset.xml"):
        print("file not found")
    file_location = os.path.abspath("collectorset.xml")
    tree = ET.parse(file_location)
    root = tree.getroot()
    counter_list += ",\n".join([(f'"{child.text}"') for child in root.iter('Counter')])
    return counter_list


def force_empty_output():
    output = "sysdat.csv"
    debug_path = os.path.abspath(output)
    with open(output, "w") as f:
        f.write("")
        f.close()
    return


def set_script():
    force_empty_output()
    file_name = "script.ps1"
    counter_list = utility()
    debug_path = os.path.abspath("sysdat.csv")
    script = f"Get-Counter -Counter $CounterList -SampleInterval 2 -Continuous | Export-Counter -Force -FileFormat CSV -Path {debug_path}"
    with open(file_name, "w+", encoding="utf-8") as f:
        content = str(f"$CounterList={counter_list}")
        f.write(content)
        f.write(f"\n{script}")
        f.close()
    return

