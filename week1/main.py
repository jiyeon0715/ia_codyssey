def print_hello():
    print('Hello Mars!')


def read_log_file(log_file):
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            print('\n--- 로그 파일 내용 ---')
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f'오류: 파일 "{log_file}"을 찾을 수 없습니다.')
    except PermissionError:
        print(f'오류: "{log_file}" 파일에 접근할 권한이 없습니다.')
    except Exception as error:
        print(f'예상치 못한 오류 발생: {error}')


def main():
    print_hello()
    log_file = 'mission_computer_main.log'
    read_log_file(log_file)


if __name__ == '__main__':
    main()
