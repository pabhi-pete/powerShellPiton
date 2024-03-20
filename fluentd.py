from pywinauto.application import Application
import os
import wget
from time import sleep


def download_fluentd():
    print("----- Download fleuntd in progress -----")
    print("Downloading Fluentd ...")
    url = "https://s3.amazonaws.com/packages.treasuredata.com/5/windows/fluent-package-5.0.1-x64.msi"
    wget.download(url)
    print("Download Fluentd Completed!")


def pathfinder():
    abs_path = os.path.abspath('fluent-package-5.0.1-x64.msi')
    return abs_path


def install_fluentd():
    print("----- Start Fluentd Installation -----")
    abs_path = os.path.abspath('fluent-package-5.0.1-x64.msi')
    app = Application(backend="win32").start(r'msiexec /i' + str(abs_path))
    header = 'Fluent Package v5.0.1 setup'
    next_button = app.window(best_match=header, top_level_only=True).child_window(best_match='Next')
    checkbox = app.window(best_match=header, top_level_only=True).\
        child_window(best_match='I accept the terms in License Agreement')
    install = app.window(best_match=header, top_level_only=True).child_window(best_match='Install')
    sleep(2)
    print("Clicking Next")
    next_button.click_input()
    sleep(2)
    print("Terms of license agreements confirmed")
    checkbox.click_input()
    sleep(2)
    print("Clicking Next")
    next_button.click_input()
    sleep(2)
    print("Clicking Next")
    next_button.click_input()
    sleep(2)
    print("Installing Fluentd")
    install.click_input()
    print("----- Complete Fluentd Installation -----")


def remove_fluentd():
    print("----- Remove Fluentd -----")
    abs_path = pathfinder()
    app = Application(backend="win32").start(r'msiexec /i' + str(abs_path))
    header = 'Fluent Package v5.0.1 setup'
    app.window(best_match=header, top_level_only=True).child_window(best_match="Next").click_input()
    app.window(best_match=header, top_level_only=True).child_window(best_match="Remove").click_input()
    app.window(best_match=header, top_level_only=True).child_window(best_match="Remove").click_input()
    print("removing fluentd in progress ..")
    app.window(best_match=header, top_level_only=True).child_window(best_match="Finish").click_input()
    print("Successful uninstalled fluentd!")


def main():
    if not os.path.isfile('fluent-package-5.0.1-x64.msi'):
        download_fluentd()
    else:
        exit_path = pathfinder()
        print(f"Fluentd is already download and located at: {exit_path}")
    install_fluentd()


if __name__ == "__main__":
    main()