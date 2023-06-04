import subprocess
import sys
import threading
import locale

class Local:
    # check if timeout occurred
    _timeout_occurred = False

    def on_timeout(self, process):
        self._timeout_occurred = True
        process.kill()
        # clear stdin buffer (for Linux)
        try:
            import termios
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
        except ImportError:
            # Windows, just exit
            pass

    def input_timer_main(self, prompt_in, timeout_sec_in):
        # print with no new line
        print(prompt_in, end="")
        sys.stdout.flush()

        # new python input process create
        cmd = [sys.executable, '-c', 'print(input())']
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
            timer_proc = threading.Timer(timeout_sec_in, self.on_timeout, [proc])
            try:
                # timer set
                timer_proc.start()
                stdout, stderr = proc.communicate()

                # get stdout and trim new line character
                result = stdout.decode(locale.getpreferredencoding()).strip("\r\n")
            finally:
                # timeout clear
                timer_proc.cancel()

        # timeout check
        if self._timeout_occurred or not result:
            # move the cursor to the next line
            print("")
            return None  # Return None when timeout occurs or no input is provided
        return result

def input_timer(prompt, timeout_sec):
    t = Local()
    return t.input_timer_main(prompt, timeout_sec)

try:
        start = None
        curr = None
        a = input_timer("* start: ", 2)
        if a is None:
            print("Timeout occurred!")
        else:
            start = a

        a = input_timer("* curr: ", 2)
        if a is None:
            print("Timeout occurred!")
        else:
            curr = a

        print("start:", start)
        print("curr:", curr)

except TimeoutError as e:
    print("Timeout...")
    print("start:", start)
    print("curr:", curr)
    pass

print("done")