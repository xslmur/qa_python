from thread_for_class import CustomThread


def cat_sound():
    print(f"Ergo says meow")


def dog_sound(name):
    print(f"{name} says woof")


if __name__ == "__main__":
    # w/o args
    cats_thread = CustomThread(tid=1, target=cat_sound, daemon=True)
    # with args
    dogs_thread = CustomThread(tid=2, target=dog_sound, args=['Proxy'], daemon=True)

    cats_thread.start()
    dogs_thread.start()

    cats_thread.join()
    dogs_thread.join()
