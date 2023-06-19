import threading


class CustomThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None, tid: int):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.__tid = tid

    def run(self):
        print(f"{self.__tid} thread started")
        super().run()

