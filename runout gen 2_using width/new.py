import subprocess
#input touchscreen swipe 541 1726 608 773 2
cmd_input = """adb
adb shell
input touchscreen swipe 541 1726 608 773 2"""

process = subprocess.Popen(
    "adb shell",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)
process.communicate( b"input touchscreen swipe 541 1726 608 773 2\n")
