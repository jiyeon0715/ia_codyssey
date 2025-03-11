def print_hello():
    print('Hello Mars!')


def read_log_file(log_file):
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
           
            print('\n--- 로그 파일 내용 (시간 역순) ---')
            for line in reversed(lines):
                print(line.strip())
            
            error_logs = [line for line in lines if 'unstable' in line or 'explosion' in line]
            if error_logs:
                with open('problem_logs.txt', 'w', encoding='utf-8') as error_file:
                    error_file.writelines(error_logs)
                print('\nIssue logs have been saved in problem_logs.txt.')
    except FileNotFoundError:
        print(f'Error: The file "{log_file}" does not exist.')
    except PermissionError:
        print(f'Error: Permission denied while accessing "{log_file}".')
    except Exception as error:
        print(f'An unexpected error occurred: {error}')

def main():
    print_hello()
    log_file = 'mission_computer_main.log'
    read_log_file(log_file)

if __name__ == '__main__':
    main()
