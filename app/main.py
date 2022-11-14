from functions import handler, user_mistake, exit_func, hello_func, show_commands, start_func, exit_func
from constants import hello_words, exit_words


def main():
    show_commands()
    while True:
        command = input("Enter command: ").lower().strip()
        if command in handler:
            answer = handler[command]()
            if answer:
                # Here should be real command,and not print.Print just for showing
                print(answer)
            else:
                continue
        elif command in hello_words:
            hello_func()
        elif command in exit_words:
            exit_func()
        else:
            second_try = user_mistake(command)
            if second_try:
                answer = handler[second_try]()
                if answer:
                    # Here should be real command,and not print.Print just for showing
                    print(answer)
            else:
                print("Unknown command. Try another one")


if __name__ == '__main__':
    main()
