def solution(phone_book):

    phone_dict = {}

    for p in phone_book:
        phone_dict[p] = True

    for phone in phone_book:
        header = ''
        for p in phone:
            header += p
            if header in phone_dict and header != phone:
                return False
    return True